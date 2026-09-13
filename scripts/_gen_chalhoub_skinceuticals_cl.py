"""One-off: generate Paula's cover letter for the Chalhoub Group / SkinCeuticals
"Ecommerce Specialist" (Middle East) role.

Reuses the job defined in _gen_chalhoub_skinceuticals_ecom.py. Paragraphs are
authored directly (no LLM API key in this repo) and kept strictly truthful —
mapped to the JD's pillars (D2C ownership + P&L, e-business animation plan across
search/paid media/CRM, premium online experience, first-party data & CLV, beauty)
without inventing skincare/medical-aesthetic tenure, Arabic, or a standalone
CRM-platform role. Fills the real cover-letter template, converts to PDF with
soffice, and lands next to the CV under output/2026-08-16/.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_chalhoub_cv", ROOT / "scripts" / "_gen_chalhoub_skinceuticals_ecom.py"
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # no named contact yet → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Chalhoub Group has spent seven decades turning luxury into experiences the region trusts, and few brands "
        "embody that promise like SkinCeuticals — a medical-aesthetic name whose D2C business lives or dies on how "
        "credible and premium its online experience feels. Owning that direct-to-consumer business end-to-end, and "
        "steering it to profitable growth in the Middle East, is exactly the challenge I want next. As an e-commerce "
        "marketer already based in Dubai who runs a D2C store every day, I was genuinely excited to see the Ecommerce "
        "Specialist role open."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze, I own our D2C Shopify business end-to-end — strategy, catalogue, "
        "UX, content, merchandising and checkout — and I run it against commercial KPIs and A&P budget, lifting "
        "conversion (CRO) and average order value. I build the e-business animation calendar that drives traffic "
        "through search, paid media (Meta and Google, steered on ROAS) and CRM/EDM, then use first-party data and "
        "loyalty to grow retention and customer lifetime value. Earlier, at Alibaba's Miravia marketplace, I owned "
        "the Beauty & Fragrances online category across 42 accounts — growing GMV +30% QoQ and running the Flash "
        "Sales P&L reporting to the CEO — so I know how a premium beauty business is merchandised, promoted and "
        "measured online."
    ),
    "body_paragraph_2": (
        "Two things set me apart for this role. First, I combine genuine e-commerce P&L ownership with real beauty "
        "depth — I don't just execute campaigns, I steer the numbers behind traffic, conversion, spend efficiency and "
        "repeat purchase. Second, I am already in Dubai on a UAE residence visa (no relocation, no ramp-up on the GCC "
        "consumer), bilingual Spanish/English, and AI-native: I built a generative-AI system that cut reporting and "
        "content workload ~40%, which means faster, sharper reads on the D2C data whenever a growth window opens or a "
        "competitor moves."
    ),
    "closing_paragraph": (
        "I would love to bring this mix of D2C ownership, P&L rigor and beauty craft to SkinCeuticals' growth story "
        "in the Middle East. I am available to start immediately and would welcome the chance to walk through how I "
        "would approach the animation calendar, the first-party-data strategy and the online experience. Thank you "
        "for your consideration — I look forward to hearing from you."
    ),
}


def main() -> None:
    job = cvmod.make_job()
    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    cl_pdf = cvmod._to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cl_pdf.parent.parent
    final_dir = cvmod._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
