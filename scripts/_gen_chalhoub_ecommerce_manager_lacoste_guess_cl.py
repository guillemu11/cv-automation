"""One-off: carta de presentación para **E-Commerce Manager, Lacoste & Guess**
(Chalhoub Group, Dubai) — reutiliza el job de
`_gen_chalhoub_ecommerce_manager_lacoste_guess.py`.

Párrafos escritos a mano (no hay API key de LLM en el repo) y mapeados a los cuatro
pilares del JD: estrategia y P&L online, online merchandising, performance marketing
y analytics, y liderazgo cross-funcional/omnicanal.

Guardarraíles de honestidad (idénticos a los del CV):
- P&L: planes comerciales **alineados a P&L** y gestión de cost drivers de su canal.
  NO se afirma ownership pleno de un P&L de marca — se plantea como el siguiente paso.
- Sin apparel de lujo a escala Chalhoub ni Salesforce Commerce Cloud: no se insinúa.
- Sin árabe. Sin "no sponsorship needed": solo UAE Residence Visa.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_chalhoub_ecom_lg_cv",
    ROOT / "scripts" / "_gen_chalhoub_ecommerce_manager_lacoste_guess.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # sin contacto nombrado en la oferta → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Lacoste and Guess are two brands whose online business has to do something genuinely hard: hold a "
        "distinct brand world while trading hard enough to grow profitably, and stay coherent whether the "
        "customer meets them on the site, in store or on an e-Retail partner. That intersection — brand "
        "integrity and commercial discipline in the same calendar — is the work I enjoy most, and it is why "
        "the E-Commerce Manager role at Chalhoub Group caught my attention immediately."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze in Dubai, I run our D2C Shopify business end-to-end: "
        "assortment and collections, categorisation and product content, pricing, promotions and checkout — "
        "steering conversion rate and average order value through data-led online merchandising. I plan and "
        "optimise the performance marketing behind it on Meta and Google Ads, moving spend, creative and "
        "targeting on ROAS and acquisition-cost data, and I run the same trading calendar across our e-Retail "
        "partners (talabat, Noon, Careem, Deliveroo) so pricing and campaign execution stay consistent across "
        "channels. I lead a team of two and brief four external agencies, which is the day-to-day version of "
        "the cross-functional work this role describes."
    ),
    "body_paragraph_2": (
        "Before Dubai, I spent two years at Miravia (Alibaba Group) as Key Account Manager for Beauty, "
        "Fragrances and Fashion, managing 42 brand accounts — assortment strategy, pricing, competitive "
        "benchmarking and promotions — and growing GMV +30% quarter on quarter. I owned the Flash Sales "
        "channel for Beauty, Fashion and Home reporting directly to the CEO, building campaign calendars and "
        "item selection against commercial plans aligned to P&L targets. To be straightforward with you: I "
        "have run channel economics and cost drivers, not yet a full brand P&L end-to-end — that is precisely "
        "the step I am looking to take, and I would bring a numerate, margin-first habit to it from day one. "
        "My grounding in fashion is real: I started at Massimo Dutti (Inditex) on the shop floor and helped "
        "build Glovo's Retail vertical onboarding fashion and lifestyle brands."
    ),
    "closing_paragraph": (
        "I am already based in Dubai on a UAE residence visa, bilingual Spanish/English, and I would welcome "
        "the chance to walk you through how I would approach the trading calendar, the merchandising and site "
        "priorities, and the performance-marketing mix for Lacoste and Guess. Thank you for your "
        "consideration — I look forward to hearing from you."
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
