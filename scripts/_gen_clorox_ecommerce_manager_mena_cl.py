"""One-off: carta de presentación para **Ecommerce Manager MENA** en **The Clorox Company** (Dubái) — reutiliza
el job de `_gen_clorox_ecommerce_manager_mena.py`.

El puesto pide 12+ años y P&L regional; Paula tiene 5. La carta no lo esconde: abre con el trabajo que sí hace
(mix de quick commerce, pure play y D2C en EAU, con resultados), y el cierre reconoce el salto de nivel y deja la
puerta abierta al nuevo eCommerce Operations Manager, Gulf que el propio JD dice que se creará.

Párrafos mapeados al JD: mix de canal (apertura), clientes y activación (cuerpo 1), lado comercial / P&L /
captación de clientes (cuerpo 2), seniority sin rodeos (cierre).

Guardarraíles de honestidad (idénticos a los del CV): sin P&L regional como dueña, sin JBP ni renovaciones de
contrato desde el lado marca, sin retail media de pago confirmado, sin KSA, sin gestionar managers.
Visa: solo "based in Dubai"; nunca "no sponsorship needed".
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_clorox_ecommerce_manager_mena_cv",
    ROOT / "scripts" / "_gen_clorox_ecommerce_manager_mena.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # sin contacto nombrado en la oferta → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Every week in Dubai I sell the same FMCG brands through three different kinds of e-commerce: quick commerce "
        "on talabat and Careem, a pure play on Noon, and our own Shopify store. Each one needs a different mix of "
        "price, promotion, content and stock, and getting that mix right is the part of e-commerce I enjoy most. It "
        "is why I am applying for the Ecommerce Manager MENA role, where channel mix sits at the centre of the "
        "strategy."
    ),
    "body_paragraph_1": (
        "At DoFreeze I manage three brands, Befit, Eurocake and Flair, on those platforms: listings, pricing, "
        "promotional mechanics and joint activations such as a purchase-linked cashback giveaway with talabat. When "
        "we launched SMASH on talabat, I kept another brand out of the campaign as a control, and daily sales rose "
        "165% against 4.7%. On Noon, our \"New Year, New Me\" event for Befit added 4,176 incremental units, 31% over "
        "baseline. I run a weekly stock-risk review by dark store, contribute to the monthly sell-in forecast, write "
        "the channel plans our distributors use in more than 50 markets, and lead a team of two and four agencies."
    ),
    "body_paragraph_2": (
        "I also know the retailer's side of the negotiation. At Miravia (Alibaba) I managed 42 beauty and fragrance "
        "accounts, including KIKO Milano, growing GMV 30% quarter on quarter, and onboarded more than 30 new stores "
        "in two months. I ran the Flash Sales channel against P&L targets, reporting to the CEO, and before that I "
        "negotiated commercial terms with XL accounts such as KFC and Taco Bell at Glovo. My FMCG grounding comes from "
        "category planning at Mondelez."
    ),
    "closing_paragraph": (
        "I want to be direct: this role asks for more than twelve years and ownership of a regional P&L, and I have "
        "five years and have not yet led managers. If the team decides it needs that level of experience, I would "
        "be glad to be considered for the eCommerce Operations Manager, Gulf role you plan to add, which is very "
        "close to what I do today. I am based in Dubai and would welcome a conversation. Thank you for your "
        "consideration."
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

    final_cl = final_dir / "01_CV_y_Carta" / cl_pdf.name
    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cl)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)


if __name__ == "__main__":
    main()
