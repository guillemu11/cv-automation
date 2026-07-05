"""Landing-page deliverable generator — replaces the old docx deliverable
for speculative job targets. Produces a self-contained HTML+CSS+JS bundle
inside ``output/<Company_Role>/landing/``.

Rewritten 2026-05-19 against the 7-section structured-pitch redesign.
Previous "editorial silence" attempt left readers unable to see the
proposal. New shape is closer to the validated
``output/landings/landing_gloria-jeans/`` reference: diagnosis → thesis →
named 3-phase plan → proof → win → closing. Word budget raised from 120
to 600 to allow the plan to actually be readable.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job
from . import angles
from . import landing_template
from ._paths import job_subdir

logger = logging.getLogger(__name__)


# OKLCH editorial palette. Burnt sienna replaces the previous champagne-gold
# (gold is the fashion-AI cliché). All values are raw CSS strings written
# directly into the stylesheet by landing_template.render.
_DEFAULT_BRAND = {
    "ink":        "oklch(0.18 0.01 60)",
    "paper":      "oklch(0.97 0.008 80)",
    "paper_deep": "oklch(0.94 0.012 70)",
    "accent":     "oklch(0.55 0.14 35)",
    "muted":      "oklch(0.55 0.005 60)",
}


# Words that pattern-match consultancy-speak. Logged post-call.
_BANNED_PHRASES = (
    "synergy", "synergies",
    "leverage",
    "best-in-class",
    "ecosystem",
    "world-class",
    "stakeholder", "stakeholders",
    "robust",
    "holistic",
    "seamless", "seamlessly",
    "ideate", "ideating", "ideation",
    "operationalise", "operationalize",
    "touchpoint", "touchpoints",
    "drive traffic",
    "fuel loyalty",
    "unlock value",
    "value proposition",
    "next-gen", "next generation",
)


_SYSTEM = """\
You are writing the copy for a single-page editorial landing that Paula De
Francisco — a Brand & Marketing Manager based in Dubai — sends as a cold-
outreach proposal to a target fashion-retail company.

The landing is a *pitch* — a real, structured proposal. Not a mood-board,
not a poster. It has SEVEN named sections and a six-month plan with
named phases. The reader should finish it knowing: (1) what gap Paula
sees, (2) what she proposes to do about it, (3) the three concrete
phases, (4) why she's qualified, (5) what success looks like.

Total word budget: 500-700 words. NOT a tweet, NOT an essay. A real
proposal that respects the reader's time.

Editorial register — like a Business of Fashion or Monocle feature. Short
declarative sentences. Confident, never apologetic. No buzzwords:
"synergy", "leverage", "ecosystem", "best-in-class", "stakeholders",
"robust", "holistic", "seamless", "ideate", "touchpoints" are banned.

Every section's body must contain at least ONE concrete fact — a real
brand name, a real moment (Ramadan, back-to-school, Italian Week), a real
operating mechanic (drop, window reset, creator drop) — pulled from the
research dossier when one is provided.

The seven sections:

1. **HERO** — headline (4-8 words, complete thought), support (single
   line max 14 words), and CHAPTERS: a list of 3-4 short chapter labels
   that act as the index of the proposal. Each ≤4 words. The reader sees
   this index and knows what they're about to scroll through.

2. **DIAGNOSIS** ("01 — the gap" or similar):
   - eyebrow: "01 — <theme>"
   - heading: ≤12 words. A clean observation about the company's
     current moment. Concrete and specific.
   - body_paragraphs: 2-3 paragraphs, total 60-90 words. Cite the
     dossier facts. Example tone: "Gloria Jeans' MENA presence reads
     like an afterthought — under 300 followers on the Oman handle,
     zero Arabic content. The first store opens in Q4. There is a
     six-month runway sitting unused."

3. **THESIS** ("02 — the thesis" or "02 — the answer"):
   - eyebrow
   - headline: ≤12 words. ITALIC display size — it's the page's
     personality moment. A bold reframe. Examples: "Build the brand
     before the store opens." "Eataly is the prototype, not the
     exception."
   - body_paragraphs: 1-2 paragraphs, 40-70 words. Defend the thesis.

4. **PLAN** ("03 — the plan"):
   - eyebrow
   - headline: ≤8 words, two-line punch. Example: "Three phases. Six
     months." or "Three quarters. One transformation."
   - lede: ≤30 words intro to the plan
   - phases: EXACTLY 3 phases. Each has:
     - span: time window, e.g. "Weeks 1-4", "Months 2-3", "Months 4-6"
     - name: 2-4 words, e.g. "Build the foundation", "Find the voice",
       "Launch in market"
     - body: 30-50 words. CONCRETE actions. Not "build awareness" —
       "monthly UAE creator drops, Arabic-first IG/TikTok cadence,
       three modesty-aware capsule narratives."

5. **PROOF** ("04 — what I bring" or "what makes this work"):
   - eyebrow
   - headline: ≤12 words. Example: "Track record across three categories."
   - stats: EXACTLY 3. number + label (≤5 words) + optional sublabel
     (≤8 words). REAL metrics from Paula's experience only.

6. **WIN** ("05 — what success looks like"):
   - eyebrow
   - headline: ≤12 words. Example: "In six months, the market will
     know you."
   - metrics: 2-4 items. Each = number + text (≤10 words). These are
     CONCRETE outcomes the plan delivers. Examples:
     "+100K verified IG followers", "15% engagement on creator drops",
     "3 capsule launches with measurable sell-through"

7. **CLOSING**:
   - paragraph: ≤30 words. Direct. Not a recap.
   - cta_line: ≤10 words. Example: "Thirty minutes — coffee or call."

NEVER invent. If the dossier doesn't support a fact, don't claim it.
Output via the submit_landing_content tool.
"""


_TOOL = {
    "name": "submit_landing_content",
    "description": "Submit the structured proposal content (7 sections, 500-700 words total).",
    "input_schema": {
        "type": "object",
        "properties": {
            "hero": {
                "type": "object",
                "properties": {
                    "headline": {"type": "string", "maxLength": 80},
                    "support":  {"type": "string", "maxLength": 110},
                    "chapters": {
                        "type": "array",
                        "minItems": 3, "maxItems": 4,
                        "items": {"type": "string", "maxLength": 30},
                    },
                },
                "required": ["headline", "support", "chapters"],
            },
            "diagnosis": {
                "type": "object",
                "properties": {
                    "eyebrow": {"type": "string", "maxLength": 40},
                    "heading": {"type": "string", "maxLength": 100},
                    "body_paragraphs": {
                        "type": "array",
                        "minItems": 2, "maxItems": 3,
                        "items": {"type": "string", "maxLength": 320},
                    },
                },
                "required": ["eyebrow", "heading", "body_paragraphs"],
            },
            "thesis": {
                "type": "object",
                "properties": {
                    "eyebrow":  {"type": "string", "maxLength": 40},
                    "headline": {"type": "string", "maxLength": 100},
                    "body_paragraphs": {
                        "type": "array",
                        "minItems": 1, "maxItems": 2,
                        "items": {"type": "string", "maxLength": 280},
                    },
                },
                "required": ["eyebrow", "headline", "body_paragraphs"],
            },
            "plan": {
                "type": "object",
                "properties": {
                    "eyebrow":  {"type": "string", "maxLength": 40},
                    "headline": {"type": "string", "maxLength": 70},
                    "lede":     {"type": "string", "maxLength": 200},
                    "phases": {
                        "type": "array",
                        "minItems": 3, "maxItems": 3,
                        "items": {
                            "type": "object",
                            "properties": {
                                "span": {"type": "string", "maxLength": 30},
                                "name": {"type": "string", "maxLength": 40},
                                "body": {"type": "string", "maxLength": 320},
                            },
                            "required": ["span", "name", "body"],
                        },
                    },
                },
                "required": ["eyebrow", "headline", "lede", "phases"],
            },
            "proof": {
                "type": "object",
                "properties": {
                    "eyebrow":  {"type": "string", "maxLength": 40},
                    "headline": {"type": "string", "maxLength": 100},
                    "stats": {
                        "type": "array",
                        "minItems": 3, "maxItems": 3,
                        "items": {
                            "type": "object",
                            "properties": {
                                "number":   {"type": "string", "maxLength": 10},
                                "label":    {"type": "string", "maxLength": 40},
                                "sublabel": {"type": "string", "maxLength": 60},
                            },
                            "required": ["number", "label"],
                        },
                    },
                },
                "required": ["eyebrow", "headline", "stats"],
            },
            "win": {
                "type": "object",
                "properties": {
                    "eyebrow":  {"type": "string", "maxLength": 50},
                    "headline": {"type": "string", "maxLength": 100},
                    "metrics": {
                        "type": "array",
                        "minItems": 2, "maxItems": 4,
                        "items": {
                            "type": "object",
                            "properties": {
                                "number": {"type": "string", "maxLength": 12},
                                "text":   {"type": "string", "maxLength": 80},
                            },
                            "required": ["number", "text"],
                        },
                    },
                },
                "required": ["eyebrow", "headline", "metrics"],
            },
            "closing": {
                "type": "object",
                "properties": {
                    "paragraph": {"type": "string", "maxLength": 220},
                    "cta_line":  {"type": "string", "maxLength": 70},
                },
                "required": ["paragraph", "cta_line"],
            },
        },
        "required": ["hero", "diagnosis", "thesis", "plan",
                     "proof", "win", "closing"],
    },
}


def _request_content(job: Job, analysis: JobAnalysis) -> dict | None:
    """Call the LLM to produce the structured-pitch content for this job."""
    angle = angles.get((job.raw or {}).get("positioning_angle"))

    if angle:
        clean_system_addendum = _strip_brand_names(angle.system_addendum)
        clean_user_addendum   = _strip_brand_names(angle.user_addendum)
        clean_brief           = _strip_brand_names(angle.deliverable_brief)
        system_msg = (
            _SYSTEM
            + "\n\n" + clean_system_addendum
            + "\n\nDELIVERABLE BRIEF FOR THIS LANDING: " + clean_brief
            + "\n\nFINAL REMINDER — the brand-suppression rule overrides "
            "everything above: do NOT output the words 'Inditex' or "
            "'Massimo Dutti' anywhere in this landing, including section "
            "bodies, captions, attributions, eyebrows or labels. Translate "
            "the method into neutral retail language (drops, floor cadence, "
            "visual merchandising standards, store-team rhythm)."
        )
        angle_block = (
            "\n\n## Positioning angle\n"
            + clean_user_addendum
            + "\n\nDeliverable brief: " + clean_brief
        )
    else:
        system_msg = _SYSTEM
        angle_block = ""

    # Optional research dossier
    dossier_path = (job.raw or {}).get("research_dossier_path")
    dossier_block = ""
    if dossier_path and Path(dossier_path).is_file():
        try:
            dossier_text = Path(dossier_path).read_text(encoding="utf-8")
            dossier_block = (
                "\n\n## Research dossier (GROUND TRUTH — prioritise facts "
                "from here over general knowledge; do not invent beyond it)\n"
                + dossier_text[:6000]
            )
        except OSError as exc:
            logger.warning("dossier read failed (%s): %s", dossier_path, exc)

    p = settings.profile
    user_msg = f"""\
Write the structured-pitch landing for a speculative outreach to {job.company}.

## Target
- Company: {job.company}
- Location: {job.location}
- Role framing: {job.title}

### Context provided to inform the proposal
{(job.description or 'No additional context.')[:4000]}

## Candidate
{p['personal']['name']} — {p['headline']}
{p['professional_summary']}

Experience anchors (use these for proof stats — REAL metrics only):
- 42 multibrand key accounts at Miravia/Alibaba (Beauty, Fragrances, Fashion)
- +30% GMV growth QoQ at Miravia/Alibaba
- 50+ countries managed currently at DoFreeze (Dubai-based)
- 6 NPD launches end-to-end across GCC, MENA, Asia, Europe, USA, Africa
- Glovo Retail vertical (onboarded fashion + lifestyle brands)
- UAE Residence Visa, no relocation needed{dossier_block}{angle_block}

Use the submit_landing_content tool. Total target ~600 words across all
sections — diagnosis 60-90w, thesis 40-70w, plan ~150w (lede + 3 phases),
proof 30-50w, win 50-80w, closing ≤40w. The phases must have NAMED phase
titles and SPECIFIC actions, not abstractions."""

    data = llm.generate_structured(
        system=system_msg,
        user=user_msg,
        tool_schema=_TOOL,
        tier="sonnet",
        max_tokens=4096,
    )
    if not data:
        logger.warning("LLM did not return landing content")
    return data


# Brand-name suppression — only for landing prompts.
_SUPPRESSED_BRAND_NAMES = ("Inditex", "Massimo Dutti")


def _strip_brand_names(text: str) -> str:
    out = text
    out = out.replace("Inditex / Massimo Dutti", "premium fashion retail")
    out = out.replace("Inditex retail playbook", "premium retail playbook")
    out = out.replace("'Inditex Retail Playbook'", "'Retail Operating Playbook'")
    out = out.replace("Inditex operating principles", "premium retail operating principles")
    out = out.replace("Inditex-trained", "premium-retail-trained")
    for name in _SUPPRESSED_BRAND_NAMES:
        out = out.replace(name, "the premium fashion retailer she trained at")
    while "  " in out:
        out = out.replace("  ", " ")
    return out


def _word_count(content: dict) -> int:
    """Total words across every textual field in the new 7-section schema."""
    pieces: list[str] = []

    def walk(node) -> None:
        if isinstance(node, str):
            pieces.append(node)
        elif isinstance(node, dict):
            # skip number-fields that are tracking tags not prose
            for k, v in node.items():
                if k == "number":
                    continue
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(content)
    return sum(len(p.split()) for p in pieces)


def _flag_banned_phrases(content: dict) -> list[str]:
    hits: set[str] = set()
    blob: list[str] = []

    def walk(node) -> None:
        if isinstance(node, str):
            blob.append(node)
        elif isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(content)
    text = " ".join(blob).lower()
    for phrase in _BANNED_PHRASES:
        if re.search(r"\b" + re.escape(phrase) + r"\b", text):
            hits.add(phrase)
    return sorted(hits)


def _build_content(job: Job, claude_data: dict) -> dict:
    """Merge Claude's blocks with candidate identity fields.

    Identity comes AFTER ``**claude_data`` so Claude can't overwrite Paula's
    real contact info. Schema doesn't expose those keys to Claude anyway,
    but defensive ordering costs nothing.
    """
    p = settings.profile["personal"]
    return {
        **claude_data,
        "company": job.company,
        "candidate_name": p["name"],
        "candidate_email": p["email"],
        "candidate_phone": p["phone"],
        "candidate_linkedin": p.get(
            "linkedin", "linkedin.com/in/paula-de-francisco-perez"
        ),
    }


def generate_landing(job: Job, analysis: JobAnalysis) -> Path | None:
    """Generate the landing-page deliverable. Returns the path to index.html."""
    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate landing", reason)
        return None

    logger.info("generating landing for %s @ %s", job.title[:40], job.company)

    claude_data = _request_content(job, analysis)
    if not claude_data:
        return None

    wc = _word_count(claude_data)
    # Soft window 400-800; warn outside
    if wc < 400 or wc > 800:
        logger.warning(
            "landing for %s outside target word range (%d, want 500-700)",
            job.company, wc,
        )
    banned = _flag_banned_phrases(claude_data)
    if banned:
        logger.warning(
            "landing for %s contains banned phrases: %s", job.company, banned,
        )

    content = _build_content(job, claude_data)
    landing_dir = job_subdir(job, "deliverables") / "landing"
    landing_dir.mkdir(parents=True, exist_ok=True)

    files = landing_template.render(content, _DEFAULT_BRAND, landing_dir=landing_dir)
    for name, body in files.items():
        (landing_dir / name).write_text(body, encoding="utf-8")

    index = landing_dir / "index.html"
    logger.info(
        "landing saved: %s  (%d words, %d banned-phrase hits)",
        index, wc, len(banned),
    )

    # Derive a one-page PDF from the live landing so Paula can attach it to
    # an email without sending an HTML bundle. Failures are non-fatal —
    # the HTML version is the source of truth.
    try:
        pdf_path = landing_to_pdf(landing_dir)
        logger.info("landing PDF saved: %s", pdf_path)
    except Exception:
        logger.exception(
            "PDF export failed for %s — HTML landing remains usable",
            job.company,
        )

    return index


# ───────────────────────────────────────────────────────────────────────────
# PDF export — see landing-to-pdf SKILL.md for the full gotcha catalogue
# ───────────────────────────────────────────────────────────────────────────

_REVEAL_OVERRIDE_CSS = """
  [data-reveal] {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
  .b-hero__line {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
"""


def landing_to_pdf(
    landing_dir: Path,
    *,
    dashboard_port: int = 8067,
    viewport_width: int = 1440,
    device_scale_factor: int = 2,
) -> Path:
    """Render the landing at ``landing_dir`` as a single-page PDF next to it."""
    from playwright.sync_api import sync_playwright
    from PIL import Image

    landing_dir = Path(landing_dir)
    if not (landing_dir / "index.html").exists():
        raise FileNotFoundError(f"No landing index.html at {landing_dir}")

    job_folder = landing_dir.parent.name
    encoded = (
        job_folder.replace(" ", "%20")
                  .replace("(", "%28")
                  .replace(")", "%29")
    )
    url = f"http://127.0.0.1:{dashboard_port}/output/{encoded}/landing/index.html"

    out_pdf = landing_dir.parent / "landing.pdf"
    tmp_png = landing_dir.parent / "_landing_full.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            ctx = browser.new_context(
                viewport={"width": viewport_width, "height": 900},
                device_scale_factor=device_scale_factor,
            )
            page = ctx.new_page()
            page.goto(url, wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")

            page.evaluate(
                """() => new Promise(r => {
                    const h = document.documentElement.scrollHeight;
                    let y = 0;
                    const step = () => {
                        window.scrollTo(0, y);
                        y += 800;
                        if (y >= h) { window.scrollTo(0, 0); r(); }
                        else setTimeout(step, 50);
                    };
                    step();
                })"""
            )
            page.wait_for_load_state("networkidle")
            page.add_style_tag(content=_REVEAL_OVERRIDE_CSS)
            page.wait_for_timeout(200)
            page.screenshot(path=str(tmp_png), full_page=True, type="png")
        finally:
            browser.close()

    img = Image.open(tmp_png)
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (250, 247, 242))
        bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
        img = bg
    img.save(str(out_pdf), "PDF", resolution=144.0)
    tmp_png.unlink(missing_ok=True)

    return out_pdf
