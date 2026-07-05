"""Build Paula's master CV PDF straight from profile.yaml (no per-job Claude).

Fills templates/cv_paula_template.docx with the canonical profile data and
writes Paula_De_Francisco_CV_Dubai.pdf at the repo root. Used to refresh the
master CV after editing profile.yaml.
"""
from __future__ import annotations

from pathlib import Path

from docx import Document

from career_ops.config import settings
from career_ops.generators.cv_generator import _replace_in_paragraphs, _to_pdf

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = settings.templates_dir / "cv_paula_template.docx"
# Master CV shows the 4 most recent roles (template has 4 experience slots).
MAX_EXP = 4


def main() -> None:
    prof = settings.profile
    p = prof["personal"]
    doc = Document(str(TEMPLATE))

    # Header
    _replace_in_paragraphs(doc, "{{FULL_NAME}}", p["name"])
    _replace_in_paragraphs(doc, "{{PHONE}}", p["phone"])
    _replace_in_paragraphs(doc, "{{EMAIL}}", p["email"])
    _replace_in_paragraphs(doc, "{{LINKEDIN}}", p.get("linkedin", ""))
    _replace_in_paragraphs(doc, "{{LOCATION}}", p["location"])
    _replace_in_paragraphs(doc, "{{NATIONALITY}}", p.get("nationality", "Spanish"))
    _replace_in_paragraphs(doc, "{{VISA}}", p.get("visa", "UAE Residence Visa"))
    _replace_in_paragraphs(doc, "{{HEADLINE}}", prof["headline"])
    _replace_in_paragraphs(doc, "{{PROFESSIONAL_SUMMARY}}", " ".join(prof["professional_summary"].split()))

    # Experience (first MAX_EXP roles)
    exps = prof.get("experience", [])[:MAX_EXP]
    for i, exp in enumerate(exps, start=1):
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_ROLE}}}}", exp.get("role", ""))
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_DATES}}}}", exp.get("dates", ""))
        parts = [x for x in [exp.get("company", ""), exp.get("context", ""), exp.get("location", "")] if x]
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_CONTEXT}}}}", " · ".join(parts))
        bullets = "\n".join(f"• {b}" for b in exp.get("highlights", []))
        _replace_in_paragraphs(doc, f"{{{{EXP_{i}_BULLETS}}}}", bullets)
    for i in range(len(exps) + 1, MAX_EXP + 1):
        for suffix in ("ROLE", "DATES", "CONTEXT", "BULLETS"):
            _replace_in_paragraphs(doc, f"{{{{EXP_{i}_{suffix}}}}}", "")

    # Skills
    s = prof.get("skills", {})
    _replace_in_paragraphs(doc, "{{SKILLS_BRAND}}", ", ".join(s.get("brand_marketing", [])))
    _replace_in_paragraphs(doc, "{{SKILLS_ECOMMERCE}}", ", ".join(s.get("ecommerce_digital", [])))
    _replace_in_paragraphs(doc, "{{SKILLS_COMMERCIAL}}", ", ".join(s.get("commercial", [])))
    _replace_in_paragraphs(doc, "{{SKILLS_DATA}}", ", ".join(s.get("data_analytics", [])))
    _replace_in_paragraphs(doc, "{{SKILLS_TOOLS}}", ", ".join(s.get("tools", [])))

    # Education
    edu = prof.get("education", [])
    main_edu = next((e for e in edu if isinstance(e, dict) and "degree" in e), {})
    _replace_in_paragraphs(
        doc, "{{EDUCATION_TITLE}}",
        f"{main_edu.get('degree', '')} — {main_edu.get('school', '')}, {main_edu.get('location', '').split(',')[0]}",
    )
    _replace_in_paragraphs(doc, "{{EDUCATION_DATES}}", main_edu.get("dates", ""))
    _replace_in_paragraphs(doc, "{{EDUCATION_DETAILS}}", main_edu.get("notes", ""))
    certs = next((e for e in edu if isinstance(e, dict) and "certifications" in e), {}).get("certifications", [])
    _replace_in_paragraphs(doc, "{{CERTIFICATIONS}}", " · ".join(certs))

    # Languages
    langs = prof.get("languages", [])
    if langs:
        _replace_in_paragraphs(doc, "{{LANG_1_NAME}}", langs[0]["lang"])
        _replace_in_paragraphs(doc, "{{LANG_1_LEVEL}}", langs[0]["level"])
    if len(langs) >= 2:
        _replace_in_paragraphs(doc, "{{LANG_2_NAME}}", langs[1]["lang"])
        _replace_in_paragraphs(doc, "{{LANG_2_LEVEL}}", langs[1]["level"])

    docx_path = ROOT / "Paula_De_Francisco_CV_Dubai.docx"
    doc.save(str(docx_path))
    pdf_path = _to_pdf(docx_path)
    print(f"Master CV written: {pdf_path}")


if __name__ == "__main__":
    main()
