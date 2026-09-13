"""One-off: generate Paula's cover letter for Lenovo "Europe and META Visual
Marketing Manager" (Req WD00102450).

Reuses the job defined in _gen_lenovo_visual_mm.py. Paragraphs are authored
directly (no LLM API key in this repo) and kept strictly truthful — NO invented
tech-hardware / Visuals experience. The letter leans on the genuine fit (integrated
marketing across Europe + META, media & A&P budget with ROI, matrix stakeholders,
AI-enabled content localization) and addresses the sector gap honestly and with
confidence rather than hiding it.

Fills the real cover-letter template, converts to PDF via soffice, and lands the
package under output/2026-08-16/.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_lenovo_cv", ROOT / "scripts" / "_gen_lenovo_visual_mm.py"
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # no named contact yet → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Lenovo's promise of 'Smarter Technology for All' only lands if the marketing behind it is as "
        "fluent in Madrid as it is in Dubai — and that dual fluency across Europe and META is exactly "
        "where I operate. The Europe and META Visual Marketing Manager role caught my attention because "
        "it asks for something I do every week: lead integrated marketing across two very different "
        "regions at once, aligning global strategy with genuine local relevance. As a marketer who grew "
        "up professionally in Madrid and is now based in Dubai, I would relish helping the Visuals "
        "business grow across both."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze, I lead integrated marketing strategy and campaign "
        "execution across 50+ markets spanning Europe, META and Asia — owning end-to-end campaign "
        "planning, media strategy and the A&P / marketing-investment budget, and steering spend against "
        "ROI and ROAS for both Consumer and Commercial audiences. I work across a matrix of Sales, "
        "Business Units, Finance, PR, media and agency partners to keep marketing aligned with business "
        "priorities. Earlier, at Alibaba's Miravia, I grew 42 accounts by +30% GMV QoQ through "
        "campaign-led planning inside a 100,000-person organisation, and I sharpened my performance "
        "discipline at Mondelez — so budget management, media planning and ROI measurement are second "
        "nature."
    ),
    "body_paragraph_2": (
        "Two things set me apart for this role. First, your brief calls for adapting and localizing "
        "global content 'leveraging AI-enabled solutions' — I have already built exactly that: a "
        "generative-AI content system (Claude / GPT) that localizes campaigns at scale across 50+ markets "
        "and cut manual workload by ~40%, which is precisely how a lean EMEA team turns global assets into "
        "local relevance fast. Second, I offer genuine Europe + META reach in a single hire: a Spanish "
        "national, bilingual (English C1), already in Dubai on a residence visa — no relocation and no "
        "ramp-up on either region. I'll be candid that my background is FMCG, beauty and e-commerce rather "
        "than tech hardware; what I bring is category-agnostic regional-marketing rigor and a fresh "
        "consumer lens that travels across products — and I ramp fast."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of multi-market execution, budget and media discipline, "
        "and AI-enabled localization to Lenovo's Visuals business across Europe and META. I am available "
        "to start immediately and would welcome the chance to discuss how I would approach your quarterly "
        "planning and country-marketing cadence. Thank you for your consideration — I look forward to "
        "hearing from you."
    ),
}


def main() -> None:
    job = cvmod.make_job()
    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    cl_pdf = cvmod._to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    # Relocate into the dated package (same helper as the CV script)
    pos_dir = cl_pdf.parent.parent
    final_dir = cvmod._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
