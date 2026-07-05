"""Value-add deliverable generator — mini audits/proposals that differentiate Paula.

Four deliverable types:
  A) Digital Presence Audit   — website UX, SEO, brand consistency
  B) E-commerce Teardown      — Noon/Amazon.ae listings analysis
  C) Brand & Competitor       — positioning map, gap analysis
  D) 90-Day Action Plan       — onboarding + quick wins + strategic initiatives

Each generates a 1-2 page branded PDF via WeasyPrint (HTML → PDF).
Claude auto-selects the best type per job when ``deliverable_type=None``.
"""
from __future__ import annotations

import logging
import re
from datetime import date
from pathlib import Path

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job
from . import angles
from ._paths import job_subdir

logger = logging.getLogger(__name__)

DELIVERABLE_TYPES = ("digital_audit", "ecommerce_teardown", "brand_analysis", "action_plan")


# -------------------------------------------------------------------
# Company research via Firecrawl
# -------------------------------------------------------------------

def _scrape_company(company: str, company_url: str | None, deliverable_type: str) -> dict:
    """Scrape company data via Firecrawl. Returns dict with scraped content."""
    if settings.dry_run or not settings.firecrawl_api_key:
        return {
            "company": company,
            "url": company_url or f"https://www.{company.lower().replace(' ', '')}.com",
            "content": f"[Placeholder content for {company} — dry run or no Firecrawl key]",
            "scraped": False,
        }

    from firecrawl import FirecrawlApp

    app = FirecrawlApp(api_key=settings.firecrawl_api_key)
    result_data = {"company": company, "url": company_url, "scraped": False, "content": ""}

    target_url = company_url
    if not target_url:
        # Try to find the company website via a search scrape
        try:
            search_result = app.search(f"{company} Dubai official website", limit=1)
            if search_result and isinstance(search_result, list) and len(search_result) > 0:
                target_url = search_result[0].get("url", "")
                result_data["url"] = target_url
        except Exception as exc:
            logger.warning("Firecrawl search failed for %s: %s", company, exc)

    if not target_url:
        return result_data

    try:
        scrape = app.scrape_url(target_url, params={"formats": ["markdown"]})
        result_data["content"] = (scrape.get("markdown", "") or "")[:8000]
        result_data["scraped"] = True
        logger.info("scraped %s (%d chars)", target_url, len(result_data["content"]))
    except Exception as exc:
        logger.warning("Firecrawl scrape failed for %s: %s", target_url, exc)

    return result_data


# -------------------------------------------------------------------
# Auto-select deliverable type
# -------------------------------------------------------------------

def _auto_select_type(job: Job, analysis: JobAnalysis) -> str:
    """Use the LLM to pick the best deliverable type for this job."""
    available, _ = llm.is_available()
    if not available:
        return "action_plan"

    text = llm.generate_text(
        system=(
            "Pick the single best deliverable type for this job application. "
            "Options: digital_audit, ecommerce_teardown, brand_analysis, action_plan. "
            "Reply with ONLY the type name, nothing else.\n\n"
            "Guidelines:\n"
            "- E-Commerce / Key Account / Trade Marketing roles → ecommerce_teardown\n"
            "- Brand Manager / Category Manager roles → brand_analysis\n"
            "- Digital Marketing roles → digital_audit\n"
            "- If unsure or generic role → action_plan (always works)\n"
        ),
        user=f"Job: {job.title} at {job.company}\nSector: {analysis.sector_fit}",
        tier="haiku",
        max_tokens=64,
        temperature=0.0,
    )

    chosen = text.strip().lower().replace(" ", "_").strip(".")
    if chosen in DELIVERABLE_TYPES:
        return chosen

    logger.info("auto-select returned '%s', defaulting to action_plan", chosen)
    return "action_plan"


# -------------------------------------------------------------------
# Claude prompts per deliverable type
# -------------------------------------------------------------------

_TOOL_SCHEMA = {
    "name": "submit_deliverable",
    "description": "Submit the deliverable content sections",
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "Deliverable title (e.g. 'Digital Presence Insights — Chalhoub Group')",
            },
            "subtitle": {
                "type": "string",
                "description": "One-line subtitle summarizing the deliverable",
            },
            "sections": {
                "type": "array",
                "description": "3-5 observation sections",
                "items": {
                    "type": "object",
                    "properties": {
                        "heading": {"type": "string", "description": "Section heading"},
                        "finding": {"type": "string", "description": "What was observed"},
                        "insight": {"type": "string", "description": "Why it matters"},
                        "recommendation": {"type": "string", "description": "Specific action to take"},
                    },
                    "required": ["heading", "finding", "insight", "recommendation"],
                },
            },
            "closing": {
                "type": "string",
                "description": "1-2 sentence closing that ties back to the candidate's ability to execute",
            },
        },
        "required": ["title", "subtitle", "sections", "closing"],
    },
}

_PROMPTS = {
    "digital_audit": {
        "system": """\
You are a Digital Marketing & Brand strategist creating a brief audit of a company's
digital presence. You analyze their website, messaging, and overall brand consistency.

Output 3-5 observations with actionable recommendations. Be specific, not generic.
Focus on: UX/navigation clarity, messaging effectiveness, brand consistency,
mobile experience, SEO basics (meta titles, content structure), and social proof.

The candidate is Paula De Francisco, a Brand/Marketing Manager with deep FMCG,
Beauty, and E-Commerce expertise in Dubai. Her recommendations should reflect
this expertise.""",
        "label": "Digital Presence Insights",
    },

    "ecommerce_teardown": {
        "system": """\
You are an E-Commerce & Quick-Commerce specialist analyzing a company's online
retail presence (Noon, Amazon.ae, own e-shop). Paula De Francisco has direct
experience managing key accounts on Noon, Talabat, Careem, and Deliveroo in the UAE.

Output 3-5 observations about: product listing quality (photos, A+ content),
pricing strategy, review management, catalog completeness, competitive positioning,
and quick-commerce readiness. Be specific about what can be improved and how.""",
        "label": "E-Commerce & Quick-Commerce Analysis",
    },

    "brand_analysis": {
        "system": """\
You are a Brand Strategy expert analyzing a company's brand positioning in the
GCC/MENA market. Compare against 2-3 key competitors in their sector.

Output 3-5 observations about: brand positioning clarity, target audience definition,
product differentiation, market gaps, competitive advantages and vulnerabilities.
Include a brief competitive context for each observation.

The candidate is Paula De Francisco with experience at Mondelez, Alibaba/Miravia,
Glovo, and DoFreeze — spanning FMCG, Beauty, E-commerce, and F&B sectors.""",
        "label": "Brand & Competitive Analysis",
    },

    "action_plan": {
        "system": """\
You are a strategic Marketing/Brand leader creating a 90-day action plan for a
new hire in this role. Structure as:

Week 1-2: Onboarding & Audit (what to learn, who to meet, what to assess)
Month 1: Quick Wins (2-3 achievable initiatives with measurable targets)
Month 2-3: Strategic Initiatives (2-3 larger projects building on quick wins)

Be specific to the job and company. Reference the candidate's relevant experience
where it maps to proposed initiatives. Paula De Francisco brings FMCG brand
management, NPD (6 launches across 50+ countries), key account management
(+30% GMV QoQ at Alibaba), and UAE quick-commerce expertise.""",
        "label": "90-Day Action Plan",
    },
}


def _generate_content(
    job: Job,
    analysis: JobAnalysis,
    deliverable_type: str,
    company_data: dict,
) -> dict | None:
    """Call the LLM to generate deliverable content."""
    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate deliverable", reason)
        return None

    prompt_cfg = _PROMPTS[deliverable_type]
    angle = angles.get((job.raw or {}).get("positioning_angle"))

    system_msg = prompt_cfg["system"]
    brief_block = ""
    if angle:
        system_msg = (
            prompt_cfg["system"]
            + "\n\n" + angle.system_addendum
            + "\n\nDELIVERABLE BRIEF: " + angle.deliverable_brief
        )
        brief_block = (
            "\n\n### Positioning brief for this deliverable\n"
            f"{angle.deliverable_brief}\n"
            + angle.user_addendum
        )

    company_content = company_data.get("content", "No company data available")
    if not company_data.get("scraped"):
        company_content = "No website data scraped — use the job description and general industry knowledge."

    user_msg = f"""\
Create a {prompt_cfg['label']} for this job application.

## Target
- Role: {job.title}
- Company: {job.company}
- Location: {job.location}

### Job Description (excerpt)
{(job.description or 'No description')[:4000]}

### Match Analysis
- Score: {analysis.score}/100 ({analysis.tier})
- Skills match: {', '.join(analysis.skills_match)}
- Sector fit: {analysis.sector_fit}

### Company Website Data
{company_content[:5000]}{brief_block}

Use the submit_deliverable tool to return the content."""

    data = llm.generate_structured(
        system=system_msg,
        user=user_msg,
        tool_schema=_TOOL_SCHEMA,
        tier="sonnet",
        max_tokens=2048,
    )

    if not data:
        logger.warning("LLM did not return deliverable content")
        return None
    return data


# -------------------------------------------------------------------
# PDF rendering (DOCX via python-docx, then DOCX→PDF via Word)
# -------------------------------------------------------------------
# We use the same toolchain as cv_generator (docx2pdf calls Word) to avoid
# WeasyPrint's GTK/Pango runtime dependency on Windows. Word is already
# installed on Paula's machine and produces high-quality PDFs.

def _sanitize(s: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "", s).strip().replace(" ", "_")[:50]


_BRAND_BLUE = (44, 62, 80)        # #2c3e50
_BRAND_GREEN = (26, 107, 60)      # #1a6b3c
_BRAND_GREY = (85, 85, 85)        # #555
_BRAND_LIGHT = (136, 136, 136)    # #888


def _set_run(run, *, bold: bool = False, italic: bool = False,
             size: int | None = None, color: tuple[int, int, int] | None = None,
             font: str = "Segoe UI") -> None:
    run.font.name = font
    if size is not None:
        from docx.shared import Pt
        run.font.size = Pt(size)
    if color is not None:
        from docx.shared import RGBColor
        run.font.color.rgb = RGBColor(*color)
    run.bold = bold
    run.italic = italic


def _render_pdf(content: dict, deliverable_type: str, job: Job) -> Path:
    """Render deliverable content to a branded PDF via DOCX + Word."""
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Cm, Pt, RGBColor

    p = settings.profile["personal"]
    today = date.today().strftime("%d %B %Y")
    type_label = _PROMPTS[deliverable_type]["label"]

    doc = Document()

    # A4 + tighter margins than default Word so it stays 1-2 pages.
    section = doc.sections[0]
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

    # ─── Header: type badge + title + subtitle + meta ──────────────────
    badge_p = doc.add_paragraph()
    badge_run = badge_p.add_run(f" {type_label.upper()} ")
    _set_run(badge_run, bold=True, size=8, color=(255, 255, 255))
    # Word can't render rounded backgrounds easily; we underline instead
    # with a colored bar by setting paragraph shading via XML.
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    pPr = badge_p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "2c3e50")
    pPr.append(shd)

    title_p = doc.add_paragraph()
    title_run = title_p.add_run(content.get("title", f"{type_label} — {job.company}"))
    _set_run(title_run, bold=True, size=18, color=_BRAND_BLUE)
    title_p.paragraph_format.space_after = Pt(2)

    subtitle = content.get("subtitle", "")
    if subtitle:
        sub_p = doc.add_paragraph()
        sub_run = sub_p.add_run(subtitle)
        _set_run(sub_run, italic=True, size=11, color=_BRAND_GREY)
        sub_p.paragraph_format.space_after = Pt(4)

    meta_p = doc.add_paragraph()
    meta_run = meta_p.add_run(
        f"Prepared by {p['name']}  ·  {today}  ·  For: {job.title} at {job.company}"
    )
    _set_run(meta_run, size=9, color=_BRAND_LIGHT)

    # Divider line below header
    div_p = doc.add_paragraph()
    pPr_div = div_p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")
    bottom.set(qn("w:color"), "2c3e50")
    pBdr.append(bottom)
    pPr_div.append(pBdr)
    div_p.paragraph_format.space_before = Pt(2)
    div_p.paragraph_format.space_after = Pt(8)

    # ─── Sections ──────────────────────────────────────────────────────
    for i, sec in enumerate(content.get("sections", []), start=1):
        head_p = doc.add_paragraph()
        head_run = head_p.add_run(f"{i}. {sec.get('heading', '')}")
        _set_run(head_run, bold=True, size=12, color=_BRAND_BLUE)
        head_p.paragraph_format.space_before = Pt(8)
        head_p.paragraph_format.space_after = Pt(2)
        # Left border on heading paragraph (mimics border-left in HTML)
        pPr_h = head_p._p.get_or_add_pPr()
        bdr = OxmlElement("w:pBdr")
        left = OxmlElement("w:left")
        left.set(qn("w:val"), "single")
        left.set(qn("w:sz"), "18")
        left.set(qn("w:color"), "2c3e50")
        left.set(qn("w:space"), "8")
        bdr.append(left)
        pPr_h.append(bdr)

        for label, key, color in (
            ("Finding:", "finding", None),
            ("Insight:", "insight", None),
            ("Recommendation:", "recommendation", _BRAND_GREEN),
        ):
            text = sec.get(key, "")
            if not text:
                continue
            body_p = doc.add_paragraph()
            label_run = body_p.add_run(f"{label} ")
            _set_run(label_run, bold=True, size=10, color=color or (26, 26, 26))
            text_run = body_p.add_run(text)
            _set_run(text_run, size=10, color=color or (26, 26, 26))
            body_p.paragraph_format.space_after = Pt(3)
            body_p.paragraph_format.left_indent = Cm(0.3)

    # ─── Closing ───────────────────────────────────────────────────────
    closing = content.get("closing", "")
    if closing:
        # Top border as separator before closing
        close_p = doc.add_paragraph()
        pPr_c = close_p._p.get_or_add_pPr()
        bdr_c = OxmlElement("w:pBdr")
        top = OxmlElement("w:top")
        top.set(qn("w:val"), "single")
        top.set(qn("w:sz"), "6")
        top.set(qn("w:color"), "DDDDDD")
        bdr_c.append(top)
        pPr_c.append(bdr_c)
        close_p.paragraph_format.space_before = Pt(14)
        close_run = close_p.add_run(closing)
        _set_run(close_run, italic=True, size=10, color=(68, 68, 68))

    # ─── Footer ────────────────────────────────────────────────────────
    footer_p = section.footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_run = footer_p.add_run(
        f"{p['name']}  ·  {p['email']}  ·  {p.get('linkedin', '')}  ·  {p['phone']}"
    )
    _set_run(footer_run, size=8, color=_BRAND_LIGHT)

    # ─── Save DOCX → convert to PDF ────────────────────────────────────
    company_safe = _sanitize(job.company)
    role_safe = _sanitize(job.title)
    type_safe = deliverable_type.replace("_", "-")
    docx_path = job_subdir(job, "deliverables") / f"Deliverable_Paula_{company_safe}_{role_safe}_{type_safe}.docx"
    doc.save(str(docx_path))

    pdf_path = docx_path.with_suffix(".pdf")
    # Use direct COM automation (pywin32) instead of docx2pdf. The latter
    # opens Word visibly and triggers RPC failures on this machine; driving
    # Word ourselves with Visible=False is reliable. CoInitialize is
    # mandatory in any thread that uses COM (FastAPI BackgroundTasks runs
    # sync callbacks on a worker thread that has not initialized COM).
    import pythoncom
    pythoncom.CoInitialize()
    try:
        try:
            import win32com.client as win32
            word = win32.gencache.EnsureDispatch("Word.Application")
            word.Visible = False
            try:
                doc_obj = word.Documents.Open(str(docx_path))
                # 17 = wdFormatPDF
                doc_obj.SaveAs(str(pdf_path), FileFormat=17)
                doc_obj.Close(False)
            finally:
                word.Quit()
            docx_path.unlink()
            return pdf_path
        except Exception:
            logger.exception("Word PDF conversion failed — keeping DOCX: %s", docx_path)
            return docx_path
    finally:
        pythoncom.CoUninitialize()


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

def generate_deliverable(
    job: Job,
    analysis: JobAnalysis,
    deliverable_type: str | None = None,
    company_url: str | None = None,
) -> Path | None:
    """Generate a value-add deliverable for a job. Returns output path.

    Args:
        job: The target job.
        analysis: Claude's scoring analysis of the job.
        deliverable_type: One of DELIVERABLE_TYPES, or None to auto-select.
        company_url: Optional company website URL to scrape.

    Returns:
        Path to the generated PDF, or None on failure.
    """
    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate deliverable", reason)
        return None

    # Auto-select type if not specified. A positioning angle's suggested
    # type wins over the generic LLM auto-pick — angles encode the campaign
    # framing and the operator already chose them deliberately.
    if deliverable_type is None:
        angle = angles.get((job.raw or {}).get("positioning_angle"))
        if angle and angle.suggested_deliverable_type in DELIVERABLE_TYPES:
            deliverable_type = angle.suggested_deliverable_type
        else:
            deliverable_type = _auto_select_type(job, analysis)
    elif deliverable_type not in DELIVERABLE_TYPES:
        logger.error("Unknown deliverable type: %s (valid: %s)", deliverable_type, DELIVERABLE_TYPES)
        return None

    logger.info("generating %s deliverable for %s @ %s", deliverable_type, job.title[:40], job.company)

    # Scrape company data
    company_data = _scrape_company(job.company, company_url, deliverable_type)

    # Generate content via Claude
    content = _generate_content(job, analysis, deliverable_type, company_data)
    if not content:
        return None

    # Render to PDF
    out_path = _render_pdf(content, deliverable_type, job)
    logger.info("deliverable saved: %s", out_path)
    return out_path


def generate_all_deliverables(
    job: Job,
    analysis: JobAnalysis,
    company_url: str | None = None,
) -> list[Path]:
    """Generate all 4 deliverable types for a job. For evaluation purposes."""
    paths = []
    for dtype in DELIVERABLE_TYPES:
        path = generate_deliverable(job, analysis, deliverable_type=dtype, company_url=company_url)
        if path:
            paths.append(path)
    return paths
