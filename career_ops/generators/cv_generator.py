"""CV personalizer — adapts Paula's CV per job using Claude + python-docx.

For each job, Claude reorders experience bullets by relevance, adapts the
headline and professional summary, and injects ATS keywords — but NEVER
invents experience or skills the candidate doesn't have.

The template matches Paula's real CV layout: photo, nationality, visa,
dates right-aligned, context lines, skills table by category.

Output: ``output/CV_Paula_{Company}_{Role}.docx``
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

from docx import Document

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job
from . import angles
from ._paths import job_subdir

logger = logging.getLogger(__name__)

_TEMPLATE_PATH = settings.templates_dir / "cv_paula_template.docx"

# -------------------------------------------------------------------
# Claude prompt for CV adaptation
# -------------------------------------------------------------------

_SYSTEM = """\
You are an expert ATS-optimized CV writer specializing in FMCG, Beauty, and
E-Commerce roles in the GCC/Dubai market. You adapt existing CV content to
maximize relevance for a specific job posting.

Rules:
1. NEVER invent experience, metrics, or skills the candidate doesn't have.
2. Reorder and emphasize bullets that match the job requirements.
3. Mirror exact keywords from the job description (ATS optimization).
4. The CV MUST fit on ONE page. Keep the professional summary to ~2 lines (≈40 words).
5. Adapt the headline to match the target role title when appropriate.
6. For each company, select the 2-3 most relevant bullets (1-2 for older/junior
   roles), each ~1-2 lines. Fewer, sharper bullets — never 4+.
7. Reorder skills within each category by relevance; keep each category concise
   (≈6 items, one line) so the skills block stays compact.
8. Output via the submit_cv_content tool.
"""

_CV_TOOL = {
    "name": "submit_cv_content",
    "description": "Submit the adapted CV content for this job posting",
    "input_schema": {
        "type": "object",
        "properties": {
            "headline": {
                "type": "string",
                "description": "Adapted headline (e.g. 'Brand Manager · E-Commerce · Key Account Management · Trade Marketing')",
            },
            "professional_summary": {
                "type": "string",
                "description": "~2 line summary (≈40 words) adapted for this job. Keep real metrics. CV must fit one page.",
            },
            "experience": {
                "type": "array",
                "description": "One entry per company, with reordered/selected bullets",
                "items": {
                    "type": "object",
                    "properties": {
                        "company": {"type": "string"},
                        "role": {"type": "string"},
                        "dates": {"type": "string"},
                        "location": {"type": "string"},
                        "context": {"type": "string", "description": "Company context line (e.g. 'Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries')"},
                        "bullets": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "2-3 most relevant bullets (1-2 for older/junior roles), each ~1-2 lines, reordered by relevance. Keep the CV to one page.",
                        },
                    },
                    "required": ["company", "role", "dates", "bullets"],
                },
            },
            "skills_brand": {
                "type": "string",
                "description": "Brand & Marketing skills, comma-separated, reordered by relevance",
            },
            "skills_ecommerce": {
                "type": "string",
                "description": "E-Commerce & Digital skills, comma-separated, reordered by relevance",
            },
            "skills_commercial": {
                "type": "string",
                "description": "Commercial skills, comma-separated, reordered by relevance",
            },
            "skills_data": {
                "type": "string",
                "description": "Data & Analytics skills, comma-separated, reordered by relevance",
            },
            "skills_tools": {
                "type": "string",
                "description": "Tools, comma-separated, reordered by relevance",
            },
        },
        "required": ["headline", "professional_summary", "experience",
                      "skills_brand", "skills_ecommerce", "skills_commercial",
                      "skills_data", "skills_tools"],
    },
}


# -------------------------------------------------------------------
# Claude API call
# -------------------------------------------------------------------

def _build_profile_text() -> str:
    """Flatten profile.yaml into text for the prompt."""
    p = settings.profile
    lines = []
    for exp in p.get("experience", []):
        lines.append(f"\n{exp['role']} @ {exp['company']} ({exp['dates']}, {exp.get('location', '')})")
        lines.append(f"  Context: {exp.get('context', '')}")
        for h in exp.get("highlights", []):
            lines.append(f"  - {h}")
    lines.append("\nAll skills by category:")
    for cat, skills in p.get("skills", {}).items():
        lines.append(f"  {cat}: {', '.join(skills)}")
    return "\n".join(lines)


def _adapt_content(job: Job, analysis: JobAnalysis) -> dict:
    """Call the LLM to adapt CV content for this specific job."""
    p = settings.profile
    angle = angles.get((job.raw or {}).get("positioning_angle"))

    system_msg = _SYSTEM
    angle_block = ""
    if angle:
        system_msg = _SYSTEM + "\n\n" + angle.system_addendum
        angle_block = "\n\n" + angle.user_addendum

    user_msg = f"""\
Adapt this candidate's CV for the following job posting.

## Target Job
- Title: {job.title}
- Company: {job.company}
- Location: {job.location}

### Job Description
{(job.description or 'No description available')[:5000]}

### Scorer notes
- Score: {analysis.score}/100 ({analysis.tier})
- Skills match: {', '.join(analysis.skills_match)}
- Missing skills: {', '.join(analysis.missing_skills)}
- ATS keywords to weave in: {', '.join(analysis.ats_keywords)}

## Candidate's Current CV Data
Name: {p['personal']['name']}
Current headline: {p['headline']}
Current summary: {p['professional_summary']}

{_build_profile_text()}{angle_block}

## Instructions
Reorder bullets and adapt headline/summary to maximize relevance for this job.
Reorder skills within each category so the most relevant ones come first.
Include the context line for each experience entry.
Use the submit_cv_content tool to return the adapted content."""

    data = llm.generate_structured(
        system=system_msg,
        user=user_msg,
        tool_schema=_CV_TOOL,
        tier="sonnet",
        max_tokens=2048,
    )

    if not data:
        logger.warning("LLM did not return CV content — using defaults")
    return data


# -------------------------------------------------------------------
# DOCX template filling
# -------------------------------------------------------------------

def _sanitize_filename(s: str) -> str:
    """Remove characters not safe for filenames."""
    return re.sub(r'[<>:"/\\|?*]', "", s).strip().replace(" ", "_")[:50]


def _replace_in_paragraphs(doc: Document, placeholder: str, value: str) -> None:
    """Replace a {{placeholder}} in all paragraphs, handling split runs.

    python-docx can split text across multiple XML runs, so we join all runs
    in each paragraph, do the replacement, then rewrite into a single run
    (preserving the first run's formatting).
    """
    for para in doc.paragraphs:
        full_text = "".join(run.text for run in para.runs)
        if placeholder not in full_text:
            continue
        new_text = full_text.replace(placeholder, value)
        if para.runs:
            para.runs[0].text = new_text
            for run in para.runs[1:]:
                run.text = ""

    # Also check table cells
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    full_text = "".join(run.text for run in para.runs)
                    if placeholder not in full_text:
                        continue
                    new_text = full_text.replace(placeholder, value)
                    if para.runs:
                        para.runs[0].text = new_text
                        for run in para.runs[1:]:
                            run.text = ""


def _fill_template(content: dict, job: Job) -> Path:
    """Fill the DOCX template with adapted content and save."""
    doc = Document(str(_TEMPLATE_PATH))
    prof = settings.profile
    p = prof["personal"]

    # -- Static header fields --
    _replace_in_paragraphs(doc, "{{FULL_NAME}}", p["name"])
    _replace_in_paragraphs(doc, "{{PHONE}}", p["phone"])
    _replace_in_paragraphs(doc, "{{EMAIL}}", p["email"])
    linkedin = p.get("linkedin", "linkedin.com/in/paula-de-francisco-perez")
    portfolio = p.get("portfolio")
    if portfolio:
        portfolio_display = portfolio.replace("https://", "").replace("http://", "")
        linkedin = f"{linkedin} | Portfolio: {portfolio_display}"
    _replace_in_paragraphs(doc, "{{LINKEDIN}}", linkedin)
    _replace_in_paragraphs(doc, "{{LOCATION}}", p["location"])
    _replace_in_paragraphs(doc, "{{NATIONALITY}}", p.get("nationality", "Spanish"))
    _replace_in_paragraphs(doc, "{{VISA}}", p.get("visa", "UAE Residence Visa"))

    # -- Dynamic fields from Claude --
    _replace_in_paragraphs(doc, "{{HEADLINE}}", content.get("headline", prof["headline"]))
    _replace_in_paragraphs(doc, "{{PROFESSIONAL_SUMMARY}}", content.get("professional_summary", prof["professional_summary"]))

    # -- Experience sections --
    profile_exp = prof.get("experience", [])
    for i, exp in enumerate(content.get("experience", []), start=1):
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_ROLE}}}}", exp.get("role", ""))
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_DATES}}}}", exp.get("dates", ""))

        # Context line: always start with company name, then context details
        company = exp.get("company", "")
        location = exp.get("location", "")
        context_detail = exp.get("context", "")
        # Fall back to profile.yaml for context details
        if not context_detail and i <= len(profile_exp):
            pe = profile_exp[i - 1]
            context_detail = pe.get("context", "")
            if not location:
                location = pe.get("location", "")
        # Build: "DoFreeze LLC · Global FMCG distributor | Brands: ... · Dubai, UAE"
        parts = [p for p in [company, context_detail, location] if p]
        context_line = " · ".join(parts)
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_CONTEXT}}}}", context_line)

        bullets_text = "\n".join(f"• {b}" for b in exp.get("bullets", []))
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_BULLETS}}}}", bullets_text)

    # Clear unused experience slots
    for i in range(len(content.get("experience", [])) + 1, 5):
        for suffix in ("ROLE", "DATES", "CONTEXT", "BULLETS"):
            _replace_in_paragraphs(doc, f"{{{{EXP_{i}_{suffix}}}}}", "")

    # -- Skills by category --
    skills = prof.get("skills", {})
    _replace_in_paragraphs(doc, "{{SKILLS_BRAND}}", content.get("skills_brand", ", ".join(skills.get("brand_marketing", []))))
    _replace_in_paragraphs(doc, "{{SKILLS_ECOMMERCE}}", content.get("skills_ecommerce", ", ".join(skills.get("ecommerce_digital", []))))
    _replace_in_paragraphs(doc, "{{SKILLS_COMMERCIAL}}", content.get("skills_commercial", ", ".join(skills.get("commercial", []))))
    _replace_in_paragraphs(doc, "{{SKILLS_DATA}}", content.get("skills_data", ", ".join(skills.get("data_analytics", []))))
    _replace_in_paragraphs(doc, "{{SKILLS_TOOLS}}", content.get("skills_tools", ", ".join(skills.get("tools", []))))

    # -- Education --
    edu = prof.get("education", [])
    main_edu = next((e for e in edu if isinstance(e, dict) and "degree" in e), {})
    _replace_in_paragraphs(doc, "{{EDUCATION_TITLE}}", f"{main_edu.get('degree', '')} — {main_edu.get('school', '')}, {main_edu.get('location', '').split(',')[0]}")
    _replace_in_paragraphs(doc, "{{EDUCATION_DATES}}", main_edu.get("dates", ""))
    _replace_in_paragraphs(doc, "{{EDUCATION_DETAILS}}", main_edu.get("notes", ""))

    certs_entry = next((e for e in edu if isinstance(e, dict) and "certifications" in e), {})
    certs = certs_entry.get("certifications", [])
    _replace_in_paragraphs(doc, "{{CERTIFICATIONS}}", " · ".join(certs))

    # -- Languages --
    langs = prof.get("languages", [])
    if len(langs) >= 1:
        _replace_in_paragraphs(doc, "{{LANG_1_NAME}}", langs[0]["lang"])
        _replace_in_paragraphs(doc, "{{LANG_1_LEVEL}}", langs[0]["level"])
    if len(langs) >= 2:
        _replace_in_paragraphs(doc, "{{LANG_2_NAME}}", langs[1]["lang"])
        _replace_in_paragraphs(doc, "{{LANG_2_LEVEL}}", langs[1]["level"])

    # -- Save --
    company_safe = _sanitize_filename(job.company)
    role_safe = _sanitize_filename(job.title)
    out_path = job_subdir(job, "cv_cl") / f"CV_Paula_{company_safe}_{role_safe}.docx"
    doc.save(str(out_path))
    return out_path


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

def _to_pdf(docx_path: Path) -> Path:
    """Convert DOCX to PDF via Word and remove the intermediate DOCX.

    ``docx2pdf`` on Windows sometimes raises ``AttributeError: Word.Application.Quit``
    *after* writing the PDF — Word's COM proxy is already torn down by the time
    the library calls ``.Quit()``. Tolerate it as long as the PDF exists on disk.
    """
    from docx2pdf import convert

    pdf_path = docx_path.with_suffix(".pdf")
    try:
        convert(str(docx_path), str(pdf_path))
    except Exception as exc:  # AttributeError on Quit, or pywintypes.com_error from RPC teardown
        if not pdf_path.exists():
            raise
        logger.info("docx2pdf reported COM teardown after success (%s) — PDF exists, continuing", type(exc).__name__)
    if pdf_path.exists():
        docx_path.unlink(missing_ok=True)
    return pdf_path


def generate_cv(job: Job, analysis: JobAnalysis) -> Path | None:
    """Generate an adapted CV for a specific job. Returns the PDF output path."""
    if not _TEMPLATE_PATH.exists():
        logger.error("CV template not found: %s — run scripts/create_templates.py first", _TEMPLATE_PATH)
        return None

    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate CV", reason)
        return None

    logger.info("generating CV for %s @ %s", job.title[:40], job.company)

    content = _adapt_content(job, analysis)
    if not content:
        return None

    docx_path = _fill_template(content, job)
    out_path = _to_pdf(docx_path)
    logger.info("CV saved: %s", out_path)
    return out_path
