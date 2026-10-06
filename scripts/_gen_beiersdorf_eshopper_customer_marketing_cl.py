"""One-off: carta de presentación + respuesta del campo "Additional information" para **Ecommerce Shopper and
Customer Marketing Manager - Middle East** en **Beiersdorf** (Dubái) — reutiliza el job de
`_gen_beiersdorf_eshopper_customer_marketing.py`. Va dirigida al reclutador, Akash Sharma, que es el mismo de las
candidaturas anteriores a Beiersdorf.

Gancho principal: **Paula llevó la cuenta de NIVEA en Miravia durante 3 meses** (dato de Guille, 2026-10-06), así
que ya conoce Beiersdorf desde el lado retailer. Sin métricas propias de NIVEA: el +30% GMV QoQ es de toda la cartera.
Gancho de fondo: el digital shelf y los planes por cliente desde los dos lados (retailer en Miravia, marca en talabat, Noon
y Careem). Párrafos mapeados al JD: planes por cliente (apertura), activación online + disponibilidad +
lanzamientos (cuerpo 1), social commerce + agencias + datos (cuerpo 2), gaps de herramientas sin rodeos (cierre).

Guardarraíles de honestidad (idénticos a los del CV):
- Salsify, Profitero y GEO: no los ha usado; el cierre lo dice.
- Sin ratings/reviews ni cuota de mercado online como KPI; sin live commerce ni TikTok Shop.
- "-30%" es lo negociado con las agencias de influencers. Deliveroo: DoFreeze NO está.
- Visa: solo "based in Dubai"; nunca "no sponsorship needed".
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_beiersdorf_eshopper_customer_marketing_cv",
    ROOT / "scripts" / "_gen_beiersdorf_eshopper_customer_marketing.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = "Akash Sharma"

PARAGRAPHS = {
    "opening_paragraph": (
        "I already know Beiersdorf from the other side of the table: at Miravia (Alibaba) I managed the NIVEA "
        "account for three months. It was one of 42 beauty and fragrance brands, KIKO Milano among them, with which I "
        "agreed visibility, campaign slots, promotions and assortment, growing GMV 30% quarter on quarter across the "
        "portfolio. Today I am on the brand side in Dubai, getting three FMCG brands found and bought on talabat, Noon "
        "and Careem. That is why I am applying for the Ecommerce Shopper and Customer Marketing Manager role in your "
        "Middle East team."
    ),
    "body_paragraph_1": (
        "At DoFreeze I build the activation plan with each platform: listings, pricing, promotional mechanics and "
        "joint activations such as a purchase-linked cashback giveaway with talabat and seasonal sampling. When we "
        "launched SMASH on talabat, I kept another of our brands out of the campaign so we could read what the "
        "campaign alone had done: daily sales rose 165% against 4.7% for the control. On Noon, our \"New Year, New "
        "Me\" event for Befit added 4,176 incremental units, 31% over baseline. Because none of that works without "
        "stock, I run a weekly review of stock risk by dark store, checking PO coverage against demand, and I own our "
        "Shopify store end-to-end, from product content to checkout."
    ),
    "body_paragraph_2": (
        "I built our creator programme from zero to 25 to 50 creators per campaign, with sampling and seeding "
        "measured on sell-out rather than reach, which is the base I would bring to your social commerce pilots. I "
        "lead a team of two and manage four influencer agencies, where I negotiated 30% off across our creator "
        "campaigns. I also built an AI workflow with Claude "
        "for planning, content and reporting that cut our manual work by about 40%. My analytical grounding comes "
        "from category planning at Mondelez, measuring sell-in, sell-out and promotional effectiveness."
    ),
    "closing_paragraph": (
        "I want to be clear about the tools: I have not used Salsify or Profitero, and my work on content has been "
        "on our own store and on the platforms rather than through a syndication system. The work those tools "
        "support, content readiness, availability and reading what a promotion returned, is what I do every week, "
        "and I would expect to learn the systems quickly. I am based in Dubai and would welcome a conversation. "
        "Thank you for your consideration."
    ),
}

ADDITIONAL_INFO = """\
# Beiersdorf Career Page — "Additional information"

Ecommerce Shopper and Customer Marketing Manager - Middle East · Recruiter: Akash Sharma · Deadline: 19 Oct 2026

## Answer (paste as-is, ~130 words)

I already know Beiersdorf from the retailer side: at Miravia (Alibaba) I managed the NIVEA account for three months.
It was one of 42 beauty and fragrance brands, including KIKO Milano, with which I agreed visibility, promotions and
assortment, growing GMV 30% quarter on quarter across the portfolio. Today, in Dubai, I activate three FMCG brands on talabat, Noon and Careem: our SMASH launch on talabat lifted
daily sales 165% against 4.7% for a control brand, and Befit's "New Year, New Me" event on Noon added 4,176
incremental units. I also run a weekly stock-risk review by dark store to protect availability.

Of the Beiersdorf roles I have applied to, this is the closest to my day-to-day work, and the one where I could
contribute from the first week. I am based in Dubai.

## Shorter variant (~60 words), if the field is tight

I know Beiersdorf from the retailer side: at Miravia (Alibaba) I managed the NIVEA account for three months,
among 42 beauty brands (+30% GMV QoQ). Now I am activating FMCG brands on talabat, Noon and Careem with results read against a
control group (+165% daily sales). The closest of Beiersdorf's roles to my day-to-day work. Based in Dubai.

## Notes
- The CV in this package has NO photo — Beiersdorf asks for that. Upload `Paula De Francisco - CV.pdf` from this folder.
- No sponsorship claim anywhere (standing rule).
- Not claimed: Salsify, Profitero, GEO, ratings and reviews, live commerce, paid retail media. Real gaps, left out.
- NIVEA: Paula managed the account at Miravia for 3 months. No NIVEA-specific metrics — the +30% GMV is portfolio-level.
- The Salsify / Profitero gap is stated in the cover letter (read by the hiring manager), not in this screening field.
"""


def main() -> None:
    job = cvmod.make_job()
    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    cl_pdf = cvmod._to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cl_pdf.parent.parent
    final_dir = cvmod._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)

    app_dir = final_dir / "04_Aplicacion"
    app_dir.mkdir(parents=True, exist_ok=True)
    info = app_dir / "Additional_information_answer.md"
    info.write_text(ADDITIONAL_INFO, encoding="utf-8")
    print("OK_INFO", info)

    final_cl = final_dir / "01_CV_y_Carta" / cl_pdf.name
    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cl)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)


if __name__ == "__main__":
    main()
