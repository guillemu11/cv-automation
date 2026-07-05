"""Cover letter generator — personalized per job using Claude + python-docx.

Generates a 4-paragraph cover letter: company-specific opening, experience
mapping, differentiators, and closing CTA.

Output: ``output/CL_Paula_{Company}_{Role}.docx``
"""
from __future__ import annotations

import logging
import re
from datetime import date
from pathlib import Path

from docx import Document

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job
from . import angles
from ._paths import job_subdir

logger = logging.getLogger(__name__)

_TEMPLATE_PATH = settings.templates_dir / "cover_letter_template.docx"

# -------------------------------------------------------------------
# Claude prompt
# -------------------------------------------------------------------

_SYSTEM = """\
You write personalized cover letters for Paula De Francisco, a Brand/Marketing
Manager applying to roles in Dubai's FMCG, Beauty, and E-Commerce sectors.

Rules:
1. Opening: Show you researched the company. Reference something specific about
   them (a product launch, market expansion, etc.).
2. Body 1: Map 2-3 of Paula's achievements to the job's requirements. Use
   concrete metrics (+30% GMV QoQ, 42 key accounts, 50+ countries, 6 NPD launches).
3. Body 2: Highlight differentiators — UAE quick-commerce experience (Noon,
   Talabat, Careem, Deliveroo), already based in Dubai with residence visa,
   bilingual Spanish/English.
4. Closing: Express enthusiasm, mention availability, suggest next steps.
5. Tone: Professional but warm. Not generic. Under 350 words total.
6. NEVER invent achievements not in the profile.
7. Output via the submit_cover_letter tool.
"""

_CL_TOOL = {
    "name": "submit_cover_letter",
    "description": "Submit the personalized cover letter paragraphs",
    "input_schema": {
        "type": "object",
        "properties": {
            "opening_paragraph": {
                "type": "string",
                "description": "Company-specific opening (2-3 sentences)",
            },
            "body_paragraph_1": {
                "type": "string",
                "description": "Experience mapping — 2-3 achievements matched to job requirements",
            },
            "body_paragraph_2": {
                "type": "string",
                "description": "Differentiators and unique value proposition",
            },
            "closing_paragraph": {
                "type": "string",
                "description": "Call to action and availability",
            },
        },
        "required": ["opening_paragraph", "body_paragraph_1", "body_paragraph_2", "closing_paragraph"],
    },
}


# -------------------------------------------------------------------
# Claude API call
# -------------------------------------------------------------------

def _generate_paragraphs(job: Job, analysis: JobAnalysis, contact_name: str | None) -> dict:
    """Call the LLM to generate personalized cover letter paragraphs."""
    p = settings.profile
    angle = angles.get((job.raw or {}).get("positioning_angle"))
    speculative = bool((job.raw or {}).get("speculative"))

    system_msg = _SYSTEM
    angle_block = ""
    if angle:
        system_msg = _SYSTEM + "\n\n" + angle.system_addendum
        angle_block = "\n\n" + angle.user_addendum
    if speculative:
        system_msg += (
            "\n\nSPECULATIVE OUTREACH: There is no public job posting for this role. "
            "The opening paragraph should acknowledge this gracefully — reach out about "
            "the company's direction (recent moves, expansion, brand work) rather than "
            "responding to a specific vacancy."
        )

    user_msg = f"""\
Write a cover letter for this job application.

## Target Job
- Title: {job.title}
- Company: {job.company}
- Location: {job.location}
- Contact: {contact_name or 'Hiring Manager'}

### Job Description
{(job.description or 'No description available')[:4000]}

### Scorer notes
- Score: {analysis.score}/100 ({analysis.tier})
- Skills match: {', '.join(analysis.skills_match)}
- Missing (be honest about these): {', '.join(analysis.missing_skills)}
- Key ATS terms: {', '.join(analysis.ats_keywords)}

## Candidate Profile
{p['personal']['name']} — {p['headline']}
{p['professional_summary']}

Key metrics to use:
- +30% GMV growth QoQ managing 42 key accounts at Alibaba Group (Miravia)
- 6 NPD launches end-to-end across 50+ countries at DoFreeze
- Scaled influencer programme from zero to 25-50 creators per campaign
- UAE quick-commerce platforms: Noon, Talabat, Careem, Deliveroo
- Already in Dubai with UAE residence visa{angle_block}

Use the submit_cover_letter tool to return the 4 paragraphs."""

    data = llm.generate_structured(
        system=system_msg,
        user=user_msg,
        tool_schema=_CL_TOOL,
        tier="sonnet",
        max_tokens=1024,
    )

    if not data:
        logger.warning("LLM did not return cover letter paragraphs")
    return data


# -------------------------------------------------------------------
# DOCX template filling
# -------------------------------------------------------------------

def _sanitize(s: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "", s).strip().replace(" ", "_")[:50]


def _replace_in_paragraphs(doc: Document, placeholder: str, value: str) -> None:
    """Replace placeholder in all paragraphs, handling split runs."""
    for para in doc.paragraphs:
        full_text = "".join(run.text for run in para.runs)
        if placeholder not in full_text:
            continue
        new_text = full_text.replace(placeholder, value)
        if para.runs:
            para.runs[0].text = new_text
            for run in para.runs[1:]:
                run.text = ""
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


def _fill_template(paragraphs: dict, job: Job, contact_name: str | None) -> Path:
    """Fill the DOCX template with generated paragraphs and save."""
    doc = Document(str(_TEMPLATE_PATH))
    p = settings.profile["personal"]

    _replace_in_paragraphs(doc, "{{DATE}}", date.today().strftime("%d %B %Y"))
    _replace_in_paragraphs(doc, "{{COMPANY}}", job.company)
    _replace_in_paragraphs(doc, "{{ROLE}}", job.title)
    _replace_in_paragraphs(doc, "{{HIRING_MANAGER}}", contact_name or "Hiring Manager")
    _replace_in_paragraphs(doc, "{{OPENING_PARAGRAPH}}", paragraphs.get("opening_paragraph", ""))
    _replace_in_paragraphs(doc, "{{BODY_PARAGRAPH_1}}", paragraphs.get("body_paragraph_1", ""))
    _replace_in_paragraphs(doc, "{{BODY_PARAGRAPH_2}}", paragraphs.get("body_paragraph_2", ""))
    _replace_in_paragraphs(doc, "{{CLOSING_PARAGRAPH}}", paragraphs.get("closing_paragraph", ""))
    _replace_in_paragraphs(doc, "{{FULL_NAME}}", p["name"])
    _replace_in_paragraphs(doc, "{{PHONE}}", p["phone"])
    _replace_in_paragraphs(doc, "{{EMAIL}}", p["email"])

    company_safe = _sanitize(job.company)
    role_safe = _sanitize(job.title)
    out_path = job_subdir(job, "cv_cl") / f"CL_Paula_{company_safe}_{role_safe}.docx"
    doc.save(str(out_path))
    return out_path


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

def _to_pdf(docx_path: Path) -> Path:
    """Convert DOCX to PDF via Word and remove the intermediate DOCX.

    Tolerates the post-success ``Word.Application.Quit`` COM teardown error
    that ``docx2pdf`` raises on Windows — the PDF is already on disk when
    that fires.
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


def generate_cover_letter(
    job: Job,
    analysis: JobAnalysis,
    contact_name: str | None = None,
) -> Path | None:
    """Generate a cover letter for a specific job. Returns PDF output path."""
    if not _TEMPLATE_PATH.exists():
        logger.error("Cover letter template not found: %s", _TEMPLATE_PATH)
        return None

    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate cover letter", reason)
        return None

    logger.info("generating cover letter for %s @ %s", job.title[:40], job.company)

    paragraphs = _generate_paragraphs(job, analysis, contact_name)
    if not paragraphs:
        return None

    docx_path = _fill_template(paragraphs, job, contact_name)
    out_path = _to_pdf(docx_path)
    logger.info("cover letter saved: %s", out_path)
    return out_path
