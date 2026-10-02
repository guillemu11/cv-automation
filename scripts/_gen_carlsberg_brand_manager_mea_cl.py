"""One-off: carta de presentación para **Brand Manager – MEA** en **Carlsberg Group** (Dubái) —
reutiliza el job de `_gen_carlsberg_brand_manager_mea.py`.

Párrafos escritos a mano y mapeados a los pilares del JD: planes de marca desde el insight,
innovación de la idea al lanzamiento, desarrollo de comunicación con agencias, ejecución con
Commercial y trade partners, y rendimiento de marca (ventas, volumen, eficacia de campaña) con
datos y Nielsen.

Gancho: "Georgina's Favourite Treat" (Holsten × Georgina Rodríguez, Riad, 2025), que Dorothea
Drews explicó como "humour and hyper-localisation" — encaja con cómo Paula ancla las marcas a los
momentos de la región (Ramadán, back to school) y a comunidades locales (running, pádel, yoga).

Guardarraíles de honestidad (idénticos a los del CV y el outreach):
- **Bebidas / malta / cerveza: no las ha trabajado.** La carta lo dice en una frase.
- No se escribe "4+ years FMCG" (brand-side suma ~2 años); tampoco se resalta.
- **Cuota de mercado y NIQ en DoFreeze: no.** Nielsen solo en Mondelez.
- Sin árabe (ventaja, no requisito): no se menciona. Sin "no sponsorship needed": solo UAE
  Residence Visa. Plataformas: talabat, Noon, Careem; nunca Deliveroo.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_carlsberg_brand_manager_mea_cv",
    ROOT / "scripts" / "_gen_carlsberg_brand_manager_mea.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # Dorothea Drews es la hiring manager probable, sin confirmar → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Holsten's \"Georgina's Favourite Treat\" turned a global name into neighbourhood gossip at a baqala, "
        "and that mix of humour and local detail is the kind of communication I enjoy building. I am applying "
        "for the Brand Manager – MEA role because the remit you describe, owning brands from insight and "
        "innovation through agency work to performance in market, is what I do today for three FMCG food "
        "brands at DoFreeze in Dubai."
    ),
    "body_paragraph_1": (
        "I own the brand plans for Befit, Eurocake and Flair across the GCC and more than 50 export markets, "
        "built around the moments that move the region: Ramadan, back to school, Fitness Month and New Year. "
        "I have taken six products from idea to shelf, covering brief, packaging, pricing and go-to-market. I "
        "develop the communication with four agencies and my own team of two, a designer and a social media "
        "executive, and I work through local communities as well as individual creators, from running and "
        "padel clubs to yoga sessions. A plan only lands in market if sales and distributors carry it, so I "
        "build ours with the commercial team channel by channel, across modern trade and quick-commerce."
    ),
    "body_paragraph_2": (
        "I judge brand work on sales and volume, not reach. For SMASH on talabat I used Befit as a control "
        "brand, same platform and same window with no creators: daily sales rose 165% against 4.7% for the "
        "control. On Noon, \"New Year, New Me\" delivered 4,176 incremental units, 31% over baseline. When an "
        "agency's report estimated reach from follower counts and counted the same creator twice, I rebuilt "
        "the KPI definitions. My Nielsen grounding comes from category planning at Mondelez, running "
        "sell-in/sell-out and promotional-effectiveness analysis behind the Milka Spread and Mini Suchard "
        "launches. Two years at Miravia (Alibaba), managing 42 brand accounts and reporting Flash Sales to the "
        "CEO, taught me how trade partners read a brand plan."
    ),
    "closing_paragraph": (
        "Beverages would be a new category for me. The brand-building and trade mechanics are the same, and I "
        "would bring the habit of tying every campaign to volume. I am based in Dubai on a UAE residence visa "
        "and would welcome the chance to discuss how I could contribute to your brands across MEA. Thank you "
        "for your consideration."
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
