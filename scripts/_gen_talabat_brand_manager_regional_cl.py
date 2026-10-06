"""One-off: carta de presentación para **Brand Manager** (Regional Brand) en **talabat** (Dubái) —
reutiliza el job de `_gen_talabat_brand_manager_regional.py`.

Párrafos escritos a mano y mapeados a los pilares del JD: sistema de marca por ocasiones,
partnerships elegidas por encaje con la audiencia, brand-to-performance medido hasta la conversión,
herramientas de marca con IA e IA como práctica del equipo, y varias categorías en organizaciones
matriciales.

Gancho: el JD dice que la marca tiene que ganarse el cariño de clientes, empleados y **vendors**.
Paula es vendor de talabat hoy (DoFreeze) y trabajó en Glovo dentro de Delivery Hero.

Guardarraíles de honestidad (idénticos a los del CV):
- **Árabe** (requisito) y **8 años** (tiene 5): la carta los dice en una frase, sin excusas ni
  promesas que no estén confirmadas (nada de "trabajo con agencias arabófonas" ni "learning Arabic").
- Sin patrocinios, sin experiencia en agencia, sin "brand platform" ya construida: se habla de
  hacerlo "a menor escala".
- El avatar de IA explica el brief "en varios idiomas"; no se dice cuáles.
- No se nombra a Álvaro Martínez: el referral va por su lado, no en la carta.
- Visa: "UAE employment visa sponsored by my current employer"; nunca "no sponsorship".
- Plataformas: talabat, Noon, Careem; nunca Deliveroo.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_talabat_brand_manager_regional_cv",
    ROOT / "scripts" / "_gen_talabat_brand_manager_regional.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # hiring manager del equipo Regional Brand sin identificar → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "talabat's brand has to win over three groups: customers, employees and vendors. I belong to the third. "
        "As Brand & Marketing Manager at DoFreeze in Dubai I run campaigns on talabat for Befit, Eurocake and "
        "SMASH, and before that I worked at Glovo inside the Delivery Hero group. I am applying for the Brand "
        "Manager role in your Regional Brand team because the work you describe, an occasion-led brand system, "
        "partnerships chosen for audience fit and proof that brand work converts, is what I already do on a "
        "smaller scale."
    ),
    "body_paragraph_1": (
        "Our year is planned around occasions: Fitness Month in November, New Year New Me in January, Ramadan "
        "and back to school. Every campaign, creator wave, sampling and partnership hangs off that calendar. I "
        "pick partners for the audience they bring. With talabat we ran an in-app giveaway where each purchase "
        "earned an entry to win talabat cashback cards, plus seasonal samplings, and we work with running, padel "
        "and yoga communities that bring their own people and their own content. I then measure the result in "
        "sales rather than reach. For SMASH on talabat I used Befit as a control brand on the same platform and "
        "dates: daily sales rose 165%, against 4.7% for the control. On Noon, New Year New Me added 4,176 "
        "incremental units, 31% over baseline."
    ),
    "body_paragraph_2": (
        "AI is how my team of two, a designer and a social media executive, keeps up. I built a Claude-based "
        "system for campaign planning, content, market research and reporting that cut our manual work by about "
        "40%. When inbound requests to work with Befit kept growing, I set up an affiliate programme with a "
        "landing page built by AI agents and an AI avatar that explains the content brief in several languages, "
        "so every creator receives the same guidance. Your role asks for the same thing for markets and agencies, "
        "at a much larger size. My range across categories comes from chocolate at Mondelez; beauty, fragrance "
        "and fashion at Miravia (Alibaba), where I created the Beauty Club and Hot on Social projects and "
        "reported Flash Sales to the CEO; and food delivery at Glovo."
    ),
    "closing_paragraph": (
        "Two gaps are worth stating plainly: I have five years of experience rather than eight, and I speak "
        "English and Spanish but not Arabic. What I would bring is a vendor's view of the talabat brand, the "
        "habit of tying brand work to sales, and a team that already uses AI every day. I am based in Dubai on a "
        "UAE employment visa sponsored by my current employer, and I would welcome the chance to talk. Thank you "
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
