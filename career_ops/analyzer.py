"""Job analyzer — scores each job against Paula's profile using Claude API.

The analyzer is the brain of the system. It takes a Job (with description) and
Paula's profile.yaml, and returns a structured score (0-100) with reasoning.

Key design decisions:
  - Uses Claude Sonnet for cost efficiency (~$0.003 per job analysis)
  - Caches results in SQLite by job.id to avoid re-scoring across runs
  - Prompt includes few-shot examples from golden_set.yaml once calibrated
  - Output is structured JSON via tool_use for reliable parsing
"""
from __future__ import annotations

import json
import logging
import sqlite3
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

from .config import settings
from .discovery.normalize import Job

logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# Analysis result schema
# -------------------------------------------------------------------

@dataclass
class JobAnalysis:
    score: int  # 0-100
    tier: str  # Hot / Warm / Cold
    skills_match: list[str] = field(default_factory=list)
    missing_skills: list[str] = field(default_factory=list)
    sector_fit: str = ""
    seniority_fit: str = ""
    red_flags: list[str] = field(default_factory=list)
    ats_keywords: list[str] = field(default_factory=list)
    reasoning: str = ""
    scored_by: str = ""  # "anthropic:claude-sonnet-4-..." or "gemini:gemini-2.5-flash" — provenance

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "JobAnalysis":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


def _tier(score: int) -> str:
    if score >= 80:
        return "Hot"
    if score >= 60:
        return "Warm"
    return "Cold"


# -------------------------------------------------------------------
# SQLite cache
# -------------------------------------------------------------------

def _get_cache_conn() -> sqlite3.Connection:
    path = settings.analysis_cache_path
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS analysis_cache (
            job_id TEXT PRIMARY KEY,
            result_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    return conn


def _cache_get(conn: sqlite3.Connection, job_id: str) -> JobAnalysis | None:
    row = conn.execute(
        "SELECT result_json FROM analysis_cache WHERE job_id = ?", (job_id,)
    ).fetchone()
    if row:
        return JobAnalysis.from_dict(json.loads(row[0]))
    return None


def _cache_set(conn: sqlite3.Connection, job_id: str, analysis: JobAnalysis) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO analysis_cache (job_id, result_json) VALUES (?, ?)",
        (job_id, json.dumps(analysis.to_dict(), ensure_ascii=False)),
    )
    conn.commit()


# -------------------------------------------------------------------
# Profile summary for the prompt (built once per run)
# -------------------------------------------------------------------

def _build_profile_summary() -> str:
    p = settings.profile
    lines = [
        f"Candidate: {p['personal']['name']}",
        f"Location: {p['personal']['location']} ({p['personal'].get('visa', 'N/A')})",
        f"Headline: {p['headline']}",
        "",
        "Target titles: " + ", ".join(p.get("target_titles", [])),
        "Target sectors: " + ", ".join(p.get("target_sectors", [])),
        "Seniority: " + ", ".join(p.get("seniority_levels", [])),
        "",
        "Experience:",
    ]
    for exp in p.get("experience", []):
        lines.append(f"  - {exp['role']} @ {exp['company']} ({exp['dates']})")
        for h in exp.get("highlights", [])[:4]:
            lines.append(f"    * {h}")
    lines.append("")
    lines.append("Core skills:")
    for category, skills in p.get("skills", {}).items():
        lines.append(f"  {category}: {', '.join(skills)}")
    lines.append("")
    lines.append("Key differentiators:")
    for d in p.get("differentiators", []):
        lines.append(f"  - {d}")
    lines.append("")
    lines.append(f"Languages: {', '.join(l['lang'] + ' (' + l['level'] + ')' for l in p.get('languages', []))}")
    return "\n".join(lines)


# -------------------------------------------------------------------
# Few-shot examples (loaded from golden_set.yaml if available)
# -------------------------------------------------------------------

def _load_few_shot() -> str:
    path = settings.golden_set_path
    if not path.exists():
        return ""
    with path.open("r", encoding="utf-8") as f:
        golden = yaml.safe_load(f)
    if not golden or not isinstance(golden, list):
        return ""

    examples = []
    for item in golden[:5]:  # max 5 few-shot examples
        examples.append(
            f"Example — {item.get('tier', '?')} (score {item.get('score', '?')}):\n"
            f"  Title: {item.get('title', '?')}\n"
            f"  Company: {item.get('company', '?')}\n"
            f"  Reasoning: {item.get('reasoning', '?')}\n"
        )
    return "\n".join(examples)


# -------------------------------------------------------------------
# Claude API call
# -------------------------------------------------------------------

_SYSTEM_PROMPT = """You are a senior recruiter specializing in FMCG, Beauty, and E-Commerce
roles in the GCC region (Dubai, UAE). You evaluate job postings against a candidate's
profile and provide a structured fit score.

Be rigorous but fair:
- A perfect match (same sector, same role title, same seniority, key skills align) = 85-100
- Good match (adjacent sector, similar role, most skills align) = 65-84
- Partial match (some overlap but missing key requirements) = 40-64
- Poor match (different sector, different seniority, few skills match) = 0-39

Pay special attention to:
1. UAE quick-commerce experience (Noon, Talabat, Careem, Deliveroo) is RARE and extremely valuable
2. FMCG + Beauty combined experience is a strong differentiator
3. The candidate already has UAE visa — zero relocation cost
4. NPD end-to-end experience across 50+ countries is unusual at this seniority
5. +30% GMV QoQ at Alibaba is a strong metric
"""

_ANALYSIS_TOOL = {
    "name": "submit_analysis",
    "description": "Submit the structured job analysis result",
    "input_schema": {
        "type": "object",
        "properties": {
            "score": {
                "type": "integer",
                "description": "Fit score 0-100",
                "minimum": 0,
                "maximum": 100,
            },
            "skills_match": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Skills from the candidate's profile that match this job",
            },
            "missing_skills": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Skills required by the job that the candidate lacks",
            },
            "sector_fit": {
                "type": "string",
                "description": "How well the candidate's sector experience matches (exact/adjacent/weak/none)",
            },
            "seniority_fit": {
                "type": "string",
                "description": "How well the seniority level matches (exact/stretch-up/overqualified/underqualified)",
            },
            "red_flags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Any concerns about this job (vague description, unrealistic requirements, etc.)",
            },
            "ats_keywords": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Keywords from the job description that should be in the candidate's CV",
            },
            "reasoning": {
                "type": "string",
                "description": "1-3 sentence explanation of the score",
            },
        },
        "required": ["score", "skills_match", "missing_skills", "sector_fit", "seniority_fit", "ats_keywords", "reasoning"],
    },
}


def _build_user_content(job: Job, profile_summary: str, few_shot: str) -> str:
    user_content = f"""Analyze this job posting against the candidate profile below.

## Job Posting
- Title: {job.title}
- Company: {job.company}
- Location: {job.location}
- Source: {job.source}
- Salary: {job.salary_raw or 'Not specified'}

### Job Description
{job.description[:6000] if job.description else 'No description available — score based on title/company/sector only, with a penalty for missing information.'}

## Candidate Profile
{profile_summary}
"""
    if few_shot:
        user_content += f"\n## Calibration Examples\n{few_shot}\n"
    return user_content


# -------------------------------------------------------------------
# Gemini provider
# -------------------------------------------------------------------

_GEMINI_MODEL = "gemini-2.5-flash"

# JSON schema in OpenAPI format (what google.genai expects)
_GEMINI_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "score": {"type": "INTEGER"},
        "skills_match": {"type": "ARRAY", "items": {"type": "STRING"}},
        "missing_skills": {"type": "ARRAY", "items": {"type": "STRING"}},
        "sector_fit": {"type": "STRING"},
        "seniority_fit": {"type": "STRING"},
        "red_flags": {"type": "ARRAY", "items": {"type": "STRING"}},
        "ats_keywords": {"type": "ARRAY", "items": {"type": "STRING"}},
        "reasoning": {"type": "STRING"},
    },
    "required": ["score", "skills_match", "missing_skills", "sector_fit", "seniority_fit", "ats_keywords", "reasoning"],
}


def _call_gemini(job: Job, profile_summary: str, few_shot: str) -> JobAnalysis:
    """Call Gemini 2.5 Flash with JSON-mode structured output."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.gemini_api_key)
    user_content = _build_user_content(job, profile_summary, few_shot)
    user_content += (
        "\nReturn a JSON object matching the requested schema with your structured analysis. "
        "Score 0-100. sector_fit ∈ {exact, adjacent, weak, none}. "
        "seniority_fit ∈ {exact, stretch-up, overqualified, underqualified}."
    )

    response = client.models.generate_content(
        model=_GEMINI_MODEL,
        contents=user_content,
        config=types.GenerateContentConfig(
            system_instruction=_SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=_GEMINI_SCHEMA,
            temperature=0.2,
            max_output_tokens=2048,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    )

    if not response.text:
        logger.warning("Gemini returned empty response for job %s", job.id)
        return JobAnalysis(score=50, tier="Warm", reasoning="Empty response — defaulting to Warm",
                           scored_by=f"gemini:{_GEMINI_MODEL}")

    data = json.loads(response.text)
    score = int(data.get("score", 0))
    return JobAnalysis(
        score=score,
        tier=_tier(score),
        skills_match=data.get("skills_match", []),
        missing_skills=data.get("missing_skills", []),
        sector_fit=data.get("sector_fit", ""),
        seniority_fit=data.get("seniority_fit", ""),
        red_flags=data.get("red_flags", []),
        ats_keywords=data.get("ats_keywords", []),
        reasoning=data.get("reasoning", ""),
        scored_by=f"gemini:{_GEMINI_MODEL}",
    )


def _call_chatqueue(job: Job, profile_summary: str, few_shot: str) -> JobAnalysis:
    """Scoring via the chatqueue provider — request lands in
    ``data/chat_queue/inbox/`` and waits for a human-in-chat reply.

    Reuses ``llm.generate_structured`` so we don't duplicate the queue
    machinery from ``career_ops/llm.py``.
    """
    from . import llm

    user_content = _build_user_content(job, profile_summary, few_shot)
    user_content += "\nUse the submit_analysis tool to provide your structured analysis."

    data = llm.generate_structured(
        system=_SYSTEM_PROMPT,
        user=user_content,
        tool_schema=_ANALYSIS_TOOL,
    )

    if not data:
        logger.warning("chatqueue: empty/timeout analysis for job %s — defaulting Warm", job.id)
        return JobAnalysis(
            score=50, tier="Warm",
            reasoning="Analysis failed (chatqueue timeout) — defaulting to Warm for manual review",
            scored_by="chatqueue",
        )

    score = int(data.get("score", 0))
    return JobAnalysis(
        score=score,
        tier=_tier(score),
        skills_match=data.get("skills_match", []),
        missing_skills=data.get("missing_skills", []),
        sector_fit=data.get("sector_fit", ""),
        seniority_fit=data.get("seniority_fit", ""),
        red_flags=data.get("red_flags", []),
        ats_keywords=data.get("ats_keywords", []),
        reasoning=data.get("reasoning", ""),
        scored_by="chatqueue",
    )


def _call_claude(job: Job, profile_summary: str, few_shot: str) -> JobAnalysis:
    """Call Claude API to analyze a single job. Uses tool_use for structured output."""
    import anthropic

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    user_content = _build_user_content(job, profile_summary, few_shot)
    user_content += "\nUse the submit_analysis tool to provide your structured analysis."

    model_id = "claude-sonnet-4-20250514"
    response = client.messages.create(
        model=model_id,
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        tools=[_ANALYSIS_TOOL],
        messages=[{"role": "user", "content": user_content}],
    )

    # Extract tool use result
    for block in response.content:
        if block.type == "tool_use" and block.name == "submit_analysis":
            data = block.input
            score = int(data.get("score", 0))
            return JobAnalysis(
                score=score,
                tier=_tier(score),
                skills_match=data.get("skills_match", []),
                missing_skills=data.get("missing_skills", []),
                sector_fit=data.get("sector_fit", ""),
                seniority_fit=data.get("seniority_fit", ""),
                red_flags=data.get("red_flags", []),
                ats_keywords=data.get("ats_keywords", []),
                reasoning=data.get("reasoning", ""),
                scored_by=f"anthropic:{model_id}",
            )

    # Fallback: if no tool use (shouldn't happen with forced tool)
    logger.warning("Claude did not return tool_use for job %s — assigning score 50", job.id)
    return JobAnalysis(score=50, tier="Warm", reasoning="Analysis failed — defaulting to Warm for manual review",
                       scored_by=f"anthropic:{model_id}")


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

def _resolve_scorer():
    """Pick LLM call based on settings.llm_provider. Returns (callable, label)."""
    provider = settings.llm_provider
    if provider == "gemini":
        if not settings.gemini_api_key:
            return None, "gemini (no GEMINI_API_KEY)"
        return _call_gemini, f"gemini:{_GEMINI_MODEL}"
    if provider == "anthropic":
        if not settings.anthropic_api_key:
            return None, "anthropic (no ANTHROPIC_API_KEY)"
        return _call_claude, "anthropic:claude-sonnet-4"
    if provider == "chatqueue":
        return _call_chatqueue, "chatqueue"
    return None, f"unknown provider '{provider}'"


def analyze_jobs(jobs: list[Job]) -> list[tuple[Job, JobAnalysis]]:
    """Analyze a list of jobs against Paula's profile. Uses cache to skip re-analysis.

    Returns list of (job, analysis) tuples sorted by score descending.
    """
    scorer, label = _resolve_scorer()
    if scorer is None:
        logger.warning("LLM scorer unavailable: %s — skipping analysis", label)
        return [(j, JobAnalysis(score=50, tier="Warm", reasoning=f"No scorer available ({label})")) for j in jobs]

    logger.info("analyzer using %s", label)
    profile_summary = _build_profile_summary()
    few_shot = _load_few_shot()
    conn = _get_cache_conn()

    results: list[tuple[Job, JobAnalysis]] = []
    cached_count = 0
    api_count = 0

    for job in jobs:
        # Check cache first
        cached = _cache_get(conn, job.id)
        if cached:
            results.append((job, cached))
            cached_count += 1
            continue

        try:
            analysis = scorer(job, profile_summary, few_shot)
            _cache_set(conn, job.id, analysis)
            results.append((job, analysis))
            api_count += 1
            logger.info(
                "scored job=%s title=%r score=%d tier=%s by=%s",
                job.id[:8], job.title[:40], analysis.score, analysis.tier, analysis.scored_by,
            )
        except Exception as exc:  # noqa: BLE001
            logger.error("analysis failed for job %s: %s", job.id, exc)
            fallback = JobAnalysis(score=50, tier="Warm", reasoning=f"Analysis error: {exc}",
                                   scored_by=f"{label}:error")
            results.append((job, fallback))

    conn.close()
    logger.info("analysis complete: %d jobs (%d cached, %d API calls)", len(results), cached_count, api_count)

    # Sort by score descending
    results.sort(key=lambda x: x[1].score, reverse=True)
    return results
