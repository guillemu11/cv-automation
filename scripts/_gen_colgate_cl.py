"""One-off: generate Paula's cover letter for the Colgate-Palmolive Ecommerce
Manager (Dubai) posting. Paragraphs authored directly, filled into the real
template, converted to PDF, then moved under the dated position folder.
"""
from __future__ import annotations

import shutil

from career_ops.config import settings
from career_ops.generators import cover_letter as cl

from scripts._gen_colgate_cv import DATE_FOLDER, make_job

PARAGRAPHS = {
    "opening_paragraph": (
        "I am applying for the Ecommerce Manager role in Dubai (Job #174114). "
        "Colgate-Palmolive's products are trusted in more households than any other "
        "brand in the world, and the chance to translate that trust into digital-shelf "
        "excellence — turning rich content and data into measurable conversion across "
        "Oral, Personal, Home and Pet Care — is exactly the challenge I am looking for. "
        "I already build this every day in Dubai's FMCG and quick-commerce market."
    ),
    "body_paragraph_1": (
        "As Brand & E-Commerce Manager at DoFreeze (Befit, Eurocake, Flair), I own the "
        "Shopify store end-to-end and run the UAE quick-commerce digital shelf — listings, "
        "content, promotions and net-sales delivery — using ROI/ROAS analytics and "
        "scorecards to drive conversion and corrective action. Earlier, trained at Alibaba "
        "(Miravia/AliExpress), I managed 42 key accounts to +30% GMV growth QoQ through "
        "pricing, assortment and promotion strategy, reporting on Flash Sales P&L directly "
        "to the CEO. That blend of digital commerce strategy, customer alignment and "
        "full-funnel execution maps directly to this role's remit."
    ),
    "body_paragraph_2": (
        "What sets me apart for a UAE FMCG mandate: hands-on experience across every key "
        "e-retailer and quick-commerce platform in this market — Noon, Talabat, Careem and "
        "Deliveroo — plus FMCG category-planning foundations from Mondelez and an AI-first "
        "approach (I built generative-AI automation for content, campaign planning and KPI "
        "reporting that cut manual workload ~40%). I am already based in Dubai on a UAE "
        "residence visa, so there is zero relocation cost or delay, and I work fluently in "
        "English and Spanish."
    ),
    "closing_paragraph": (
        "I would welcome the chance to discuss how I can accelerate Colgate-Palmolive's "
        "digital commerce growth in the region. I am available to start at short notice and "
        "can share a short portfolio of e-commerce and digital-shelf work on request. Thank "
        "you for your consideration — I look forward to speaking with you."
    ),
}


def main() -> None:
    job = make_job()
    docx_path = cl._fill_template(PARAGRAPHS, job, contact_name=None)
    pdf_path = cl._to_pdf(docx_path)

    # Move into the dated position folder (the CV already created it).
    dated = settings.output_dir / DATE_FOLDER / pdf_path.parent.parent.name / pdf_path.parent.name
    dated.mkdir(parents=True, exist_ok=True)
    dest = dated / pdf_path.name
    if pdf_path.resolve() != dest.resolve():
        shutil.move(str(pdf_path), str(dest))
        # clean up the now-empty root position folder created by the generator
        root_pos = settings.output_dir / pdf_path.parent.parent.name
        try:
            shutil.rmtree(root_pos)
        except OSError:
            pass
    print("OK_PDF", dest)


if __name__ == "__main__":
    main()
