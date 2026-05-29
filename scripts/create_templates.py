#!/usr/bin/env python3
"""One-time script to generate DOCX templates with placeholders.

Creates:
  - templates/cv_paula_template.docx   (matches Paula's real CV layout)
  - templates/cover_letter_template.docx

These templates use {{PLACEHOLDER}} markers that the generators replace
with Claude-adapted content for each job application.

Re-run this script any time you want to regenerate the base templates.
"""
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
TEMPLATES.mkdir(exist_ok=True)

PHOTO_PATH = TEMPLATES / "paula_photo.jpg"

# -- Colors (black + navy for headers, gray for secondary text) --
NAVY = RGBColor(44, 62, 80)      # #2C3E50 — section headers
BLACK = RGBColor(0, 0, 0)        # headline (was gold, now black per user request)
GRAY = RGBColor(120, 120, 120)   # contact info, dates
CONTEXT = RGBColor(50, 50, 50)   # context lines (company info) — neutral dark, readable
BODY = RGBColor(30, 30, 30)      # body text


def _run(paragraph, text, size=10, bold=False, color=BODY, name="Calibri"):
    """Add a styled run to a paragraph and return it."""
    r = paragraph.add_run(text)
    r.font.name = name
    r.font.size = Pt(size)
    r.bold = bold
    r.font.color.rgb = color
    return r


def _set_spacing(paragraph, before=0, after=0, line=None):
    """Set paragraph spacing in points."""
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    if line is not None:
        fmt.line_spacing = Pt(line)


def _add_divider(doc):
    """Add a thin horizontal line as a section divider."""
    p = doc.add_paragraph()
    _set_spacing(p, before=6, after=6)
    # Use a bottom border on the paragraph
    pPr = p._p.get_or_add_pPr()
    pBdr = pPr.makeelement(qn("w:pBdr"), {})
    bottom = pBdr.makeelement(qn("w:bottom"), {
        qn("w:val"): "single",
        qn("w:sz"): "4",
        qn("w:space"): "1",
        qn("w:color"): "CCCCCC",
    })
    pBdr.append(bottom)
    pPr.append(pBdr)


def _section_header(doc, text):
    """Add a section header (e.g. 'PROFESSIONAL SUMMARY') with underline."""
    p = doc.add_paragraph()
    _set_spacing(p, before=14, after=4)
    _run(p, text, size=11, bold=True, color=NAVY)
    _add_divider(doc)


def _make_invisible_table(doc, rows, cols):
    """Create a table with no visible borders."""
    table = doc.add_table(rows=rows, cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Remove all borders
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else tbl.makeelement(qn("w:tblPr"), {})
    borders = tblPr.makeelement(qn("w:tblBorders"), {})
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = borders.makeelement(qn(f"w:{edge}"), {
            qn("w:val"): "none", qn("w:sz"): "0",
            qn("w:space"): "0", qn("w:color"): "auto",
        })
        borders.append(el)
    tblPr.append(borders)
    if tbl.tblPr is None:
        tbl.insert(0, tblPr)
    return table


# =====================================================================
# CV TEMPLATE
# =====================================================================

def create_cv_template():
    doc = Document()

    # -- Page setup --
    for section in doc.sections:
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    # ── HEADER: Name + Photo in a 2-col table (compact) ──
    header_table = _make_invisible_table(doc, rows=1, cols=2)
    left = header_table.cell(0, 0)
    left.width = Cm(13.5)

    p = left.paragraphs[0]
    _set_spacing(p, before=0, after=0)
    _run(p, "{{FULL_NAME}}", size=20, bold=True, color=NAVY)

    p = left.add_paragraph()
    _set_spacing(p, before=0, after=0)
    _run(p, "{{HEADLINE}}", size=9.5, bold=False, color=BLACK)

    p = left.add_paragraph()
    _set_spacing(p, before=0, after=0)
    _run(p, "{{LOCATION}} | {{PHONE}} | {{EMAIL}}", size=8.5, color=GRAY)

    p = left.add_paragraph()
    _set_spacing(p, before=0, after=0)
    _run(p, "{{LINKEDIN}} | Nationality: {{NATIONALITY}} | {{VISA}}", size=8.5, color=GRAY)

    # Right cell: photo
    right = header_table.cell(0, 1)
    right.width = Cm(3)
    rp = right.paragraphs[0]
    rp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if PHOTO_PATH.exists():
        rp.add_run().add_picture(str(PHOTO_PATH), width=Cm(2.7))
    else:
        _run(rp, "{{PHOTO}}", size=8, color=GRAY)

    # ── PROFESSIONAL SUMMARY ──
    _section_header(doc, "PROFESSIONAL SUMMARY")
    p = doc.add_paragraph()
    _set_spacing(p, after=4, line=14)
    _run(p, "{{PROFESSIONAL_SUMMARY}}", size=10)

    # ── WORK EXPERIENCE ──
    _section_header(doc, "WORK EXPERIENCE")

    for i in range(1, 5):
        # Role + Dates on same line using a 2-col table
        exp_table = _make_invisible_table(doc, rows=1, cols=2)
        role_cell = exp_table.cell(0, 0)
        role_cell.width = Cm(12)
        date_cell = exp_table.cell(0, 1)
        date_cell.width = Cm(5)

        rp = role_cell.paragraphs[0]
        _set_spacing(rp, before=8, after=0)
        _run(rp, f"{{{{EXP_{i}_ROLE}}}}", size=11, bold=True, color=BODY)

        dp = date_cell.paragraphs[0]
        dp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        _set_spacing(dp, before=8, after=0)
        _run(dp, f"{{{{EXP_{i}_DATES}}}}", size=10, color=GRAY)

        # Context line (company + info) — neutral black, not faint gray
        p = doc.add_paragraph()
        _set_spacing(p, before=0, after=4)
        _run(p, f"{{{{EXP_{i}_CONTEXT}}}}", size=9.5, color=CONTEXT)

        # Bullets
        p = doc.add_paragraph()
        _set_spacing(p, after=2, line=13)
        _run(p, f"{{{{EXP_{i}_BULLETS}}}}", size=10)

    # ── CORE SKILLS & TOOLS ──
    _section_header(doc, "CORE SKILLS & TOOLS")

    # Skills: category label (narrow) + skills text (wide)
    # Force exact cell widths via XML to avoid the gap problem
    LEFT_W = Cm(3)
    RIGHT_W = Cm(14)

    skill_categories = [
        ("Brand & Marketing", "{{SKILLS_BRAND}}"),
        ("E-Commerce & Digital", "{{SKILLS_ECOMMERCE}}"),
        ("Commercial", "{{SKILLS_COMMERCIAL}}"),
        ("Data & Analytics", "{{SKILLS_DATA}}"),
        ("Tools", "{{SKILLS_TOOLS}}"),
    ]

    for cat_name, placeholder in skill_categories:
        row_table = _make_invisible_table(doc, rows=1, cols=2)
        # Force cell widths via XML
        cat_cell = row_table.cell(0, 0)
        cat_cell.width = LEFT_W
        tc = cat_cell._tc
        tcPr = tc.get_or_add_tcPr()
        tcW = tcPr.makeelement(qn("w:tcW"), {qn("w:w"): str(int(LEFT_W.emu / 635)), qn("w:type"): "dxa"})
        tcPr.append(tcW)

        val_cell = row_table.cell(0, 1)
        val_cell.width = RIGHT_W
        tc2 = val_cell._tc
        tcPr2 = tc2.get_or_add_tcPr()
        tcW2 = tcPr2.makeelement(qn("w:tcW"), {qn("w:w"): str(int(RIGHT_W.emu / 635)), qn("w:type"): "dxa"})
        tcPr2.append(tcW2)

        p = cat_cell.paragraphs[0]
        _set_spacing(p, before=2, after=2)
        _run(p, cat_name, size=9.5, bold=True, color=BODY)

        p = val_cell.paragraphs[0]
        _set_spacing(p, before=2, after=2)
        _run(p, placeholder, size=9.5, color=BODY)

    # ── EDUCATION ──
    _section_header(doc, "EDUCATION")

    edu_table = _make_invisible_table(doc, rows=1, cols=2)
    edu_table.cell(0, 0).width = Cm(12)
    edu_table.cell(0, 1).width = Cm(5)

    p = edu_table.cell(0, 0).paragraphs[0]
    _set_spacing(p, after=0)
    _run(p, "{{EDUCATION_TITLE}}", size=11, bold=True, color=BODY)

    p = edu_table.cell(0, 1).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _set_spacing(p, after=0)
    _run(p, "{{EDUCATION_DATES}}", size=10, color=GRAY)

    p = doc.add_paragraph()
    _set_spacing(p, before=0, after=1)
    _run(p, "{{EDUCATION_DETAILS}}", size=9, color=GRAY)

    p = doc.add_paragraph()
    _set_spacing(p, before=0, after=0)
    _run(p, "{{CERTIFICATIONS}}", size=9, color=GRAY)

    # ── LANGUAGES ──
    _section_header(doc, "LANGUAGES")

    lang_table = _make_invisible_table(doc, rows=1, cols=4)
    for col_idx, placeholder in enumerate([
        "{{LANG_1_NAME}}", "{{LANG_1_LEVEL}}", "{{LANG_2_NAME}}", "{{LANG_2_LEVEL}}"
    ]):
        p = lang_table.cell(0, col_idx).paragraphs[0]
        _set_spacing(p, after=0)
        bold = col_idx % 2 == 0  # bold the language name, normal for level
        _run(p, placeholder, size=10, bold=bold, color=BODY)

    # Save
    path = TEMPLATES / "cv_paula_template.docx"
    doc.save(str(path))
    print(f"Created: {path}")


# =====================================================================
# COVER LETTER TEMPLATE
# =====================================================================

def create_cover_letter_template():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    p = doc.add_paragraph()
    _run(p, "{{DATE}}", size=11)

    doc.add_paragraph()

    p = doc.add_paragraph()
    _run(p, "Dear {{HIRING_MANAGER}},", size=11)

    doc.add_paragraph()

    for placeholder in ["{{OPENING_PARAGRAPH}}", "{{BODY_PARAGRAPH_1}}", "{{BODY_PARAGRAPH_2}}", "{{CLOSING_PARAGRAPH}}"]:
        p = doc.add_paragraph()
        _set_spacing(p, after=8, line=15)
        _run(p, placeholder, size=11)

    doc.add_paragraph()

    p = doc.add_paragraph()
    _run(p, "Best regards,", size=11)

    doc.add_paragraph()

    p = doc.add_paragraph()
    _run(p, "{{FULL_NAME}}", size=11, bold=True)

    p = doc.add_paragraph()
    _run(p, "{{PHONE}} | {{EMAIL}}", size=10, color=GRAY)

    path = TEMPLATES / "cover_letter_template.docx"
    doc.save(str(path))
    print(f"Created: {path}")


# =====================================================================
# FORM RESPONSES TEMPLATE
# =====================================================================

def create_form_responses_template():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    # ── HEADER ──
    p = doc.add_paragraph()
    _set_spacing(p, after=2)
    _run(p, "Application Form Responses", size=16, bold=True, color=NAVY)

    p = doc.add_paragraph()
    _set_spacing(p, after=2)
    _run(p, "{{COMPANY}} — {{ROLE}}", size=12, bold=True, color=BODY)

    p = doc.add_paragraph()
    _set_spacing(p, after=8)
    _run(p, "Generated: {{DATE}}", size=10, color=GRAY)

    _add_divider(doc)

    # ── SECTION 1: PERSONAL INFORMATION ──
    _section_header(doc, "PERSONAL INFORMATION")

    personal_fields = [
        ("Full Name", "{{FULL_NAME}}"),
        ("Email", "{{EMAIL}}"),
        ("Phone", "{{PHONE}}"),
        ("LinkedIn", "{{LINKEDIN}}"),
        ("Location", "{{LOCATION}}"),
        ("Nationality", "{{NATIONALITY}}"),
        ("Work Authorization", "{{WORK_AUTH}}"),
    ]
    for label, placeholder in personal_fields:
        table = _make_invisible_table(doc, rows=1, cols=2)
        table.cell(0, 0).width = Cm(4.5)
        table.cell(0, 1).width = Cm(12)
        p = table.cell(0, 0).paragraphs[0]
        _set_spacing(p, before=2, after=2)
        _run(p, label, size=10, bold=True, color=BODY)
        p = table.cell(0, 1).paragraphs[0]
        _set_spacing(p, before=2, after=2)
        _run(p, placeholder, size=10, color=BODY)

    # ── SECTION 2: PROFESSIONAL INFORMATION ──
    _section_header(doc, "PROFESSIONAL INFORMATION")

    prof_fields = [
        ("Current Title", "{{CURRENT_TITLE}}"),
        ("Years of Experience", "{{YEARS_EXP}}"),
        ("Current Company", "{{CURRENT_COMPANY}}"),
        ("Notice Period", "{{NOTICE_PERIOD}}"),
        ("Education Level", "{{EDUCATION_LEVEL}}"),
        ("Work Model", "{{WORK_MODEL}}"),
        ("Willing to Relocate", "{{RELOCATE}}"),
        ("Requires Sponsorship", "{{SPONSORSHIP}}"),
    ]
    for label, placeholder in prof_fields:
        table = _make_invisible_table(doc, rows=1, cols=2)
        table.cell(0, 0).width = Cm(4.5)
        table.cell(0, 1).width = Cm(12)
        p = table.cell(0, 0).paragraphs[0]
        _set_spacing(p, before=2, after=2)
        _run(p, label, size=10, bold=True, color=BODY)
        p = table.cell(0, 1).paragraphs[0]
        _set_spacing(p, before=2, after=2)
        _run(p, placeholder, size=10, color=BODY)

    # ── SECTION 3: NARRATIVE ANSWERS ──
    _section_header(doc, "NARRATIVE ANSWERS")

    narrative_fields = [
        ("Why are you interested in this role?", "{{WHY_INTERESTED}}"),
        ("What makes you a good fit?", "{{WHY_GOOD_FIT}}"),
        ("Describe your greatest professional achievement", "{{GREATEST_ACHIEVEMENT}}"),
        ("What are your salary expectations?", "{{SALARY_EXPECTATION}}"),
        ("When can you start?", "{{AVAILABILITY}}"),
    ]
    for question, placeholder in narrative_fields:
        p = doc.add_paragraph()
        _set_spacing(p, before=10, after=2)
        _run(p, f"Q: {question}", size=10, bold=True, color=NAVY)
        p = doc.add_paragraph()
        _set_spacing(p, before=2, after=6, line=14)
        _run(p, placeholder, size=10, color=BODY)

    # ── SECTION 4: ADDITIONAL Q&A ──
    _section_header(doc, "ADDITIONAL Q&A")

    p = doc.add_paragraph()
    _set_spacing(p, after=6, line=14)
    _run(p, "{{ADDITIONAL_QA}}", size=10, color=BODY)

    # ── FOOTER ──
    _add_divider(doc)
    p = doc.add_paragraph()
    _set_spacing(p, before=8)
    _run(p, "Generated for review — do not auto-submit", size=9, color=GRAY)

    path = TEMPLATES / "form_responses_template.docx"
    doc.save(str(path))
    print(f"Created: {path}")


if __name__ == "__main__":
    create_cv_template()
    create_cover_letter_template()
    create_form_responses_template()
    print("\nDone! Templates ready in templates/")
