"""One-off: generate Paula's cover letter for instashop "Sr. Specialist Marketing".

Reuses the job defined in _gen_instashop_sr_specialist.py. Paragraphs are authored
directly (no LLM API key in this repo) and kept strictly truthful. Fills the real
cover-letter template and saves the DOCX; PDF conversion is done afterwards with
soffice (docx2pdf/Word is unreliable headless in this environment).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import importlib.util

spec = importlib.util.spec_from_file_location(
    "_gen_instashop_cv", ROOT / "scripts" / "_gen_instashop_sr_specialist.py"
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # no named contact yet → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "instashop has pulled off something rare: it has turned a local q-commerce marketplace into a brand "
        "people across the UAE actually feel affection for — and doing that inside the Delivery Hero family gives "
        "it a reach few can match. That exact intersection of brand-building and quick-commerce is where I have "
        "spent the last few years, which is why the Sr. Specialist Marketing role feels like such a natural next "
        "step. As a marketer already based in Dubai who works with talabat every week, I would relish the chance "
        "to keep instashop top-of-mind across the Emirates."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze, I own integrated 360 campaigns end-to-end — seasonal, tactical "
        "and brand — from strategy through online and offline execution, and I design FMCG and retail co-marketing "
        "initiatives with brand and modern-trade partners. Crucially, I run quick-commerce hands-on, integrating "
        "brands into Noon, talabat, Careem and Deliveroo — owning listings, promotional mechanics and the in-app "
        "and push briefs that turn a campaign into repeat orders. Earlier, at Alibaba's Miravia marketplace, I grew "
        "42 brand accounts by +30% GMV QoQ through campaign-led promotions and built brand programmes (Beauty Club, "
        "Hot on Social) that positioned the platform as a lifestyle destination."
    ),
    "body_paragraph_2": (
        "Two things set me apart here. First, quick-commerce fluency is genuinely rare — I don't just market on "
        "these platforms, I helped launch one (Glovo's Retail vertical) and operate on them daily, so I understand "
        "the mechanics behind conversion, spend efficiency and repeat purchase, not only the creative. Second, I am "
        "already in Dubai on a UAE residence visa, GCC-fluent and bilingual Spanish/English — no relocation and no "
        "ramp-up on the local consumer. I am also AI-native: I built a generative-AI system that cuts campaign "
        "reporting workload by ~40%, which means faster, sharper market-intelligence turnarounds when a competitor "
        "moves or a growth window opens."
    ),
    "closing_paragraph": (
        "I would love to bring this blend of brand craft and q-commerce rigor to instashop's UAE growth story. I am "
        "available to start immediately and would welcome the chance to talk through how I would approach your "
        "seasonal and co-marketing calendar. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def main() -> None:
    job = cvmod.make_job()
    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    print("OK_CL_DOCX", cl_docx)

    # Relocate into the dated package (same helper as the CV script)
    pos_dir = cl_docx.parent.parent
    final_dir = cvmod._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
