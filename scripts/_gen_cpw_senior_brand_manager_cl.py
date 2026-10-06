"""One-off: carta de presentación para **Senior Brand Manager** en **Cereal Partners Worldwide** (Nestlé &
General Mills, Dubái, req. 17327) — reutiliza el job de `_gen_cpw_senior_brand_manager.py`.

Probablemente la lee el mismo equipo que la del Brand Manager (`_gen_cpw_brand_manager_cl.py`), así que el
gancho es distinto: aquella abría con "New Year, New Me" ↔ FITNESS; esta abre con el grupo de control de
SMASH × talabat, que responde al pilar "Drive a Culture of Testing, Learning and Optimization" y al requisito
de datos y analítica.

Párrafos mapeados al JD: test & learn (apertura), plan anual por ocasiones + innovación + equipos
multifuncionales (cuerpo 1), eficacia de campaña + capacidades emergentes + base FMCG (cuerpo 2), y los gaps
dichos sin rodeos (cierre).

Guardarraíles de honestidad (idénticos a los del CV):
- **ATL y gestión regional de varios países MENA con equipos locales: no los tiene.** El cierre lo dice en
  vez de dejar que se descubra en la entrevista.
- Sin LTP a 3 años, sin Brand Essence formal, sin cereal / desayuno, sin R&D en las NPD.
- "Negoció -30%" y "75 contratados, 103 entregados" son de las campañas de creators con agencia.
- Visa: solo "based in Dubai"; nunca "no sponsorship needed".
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_cpw_senior_brand_manager_cv",
    ROOT / "scripts" / "_gen_cpw_senior_brand_manager.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # sin contacto nombrado en la oferta → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "When I put creators behind SMASH on talabat, I kept Befit out of the campaign on the same platform and "
        "in the same window, so we could see what the campaign alone had done. Daily sales rose 165% against "
        "4.7% for the control. That habit of testing, measuring and moving money to what works is why I am "
        "applying for the Senior Brand Manager role, and I would like to bring it to a breakfast cereals "
        "portfolio with the reach of NESQUIK, FITNESS and CHEERIOS."
    ),
    "body_paragraph_1": (
        "At DoFreeze in Dubai I lead brand and marketing for three food brands, Befit, Eurocake and Flair, sold "
        "in more than 50 markets. I own the annual activation calendar, built around the moments when our "
        "consumers buy: Ramadan, back to school, Fitness Month and New Year. I have taken six products to market "
        "end-to-end, from the brief and packaging to pricing and launch, and I plan each one with sales and our "
        "distributors channel by channel, across modern trade, quick-commerce and our own online store. I write "
        "the creative briefs for my team of two, a designer and a social media executive, and for four external "
        "agencies. Across three creator campaigns I negotiated 30% off and received 103 activations against 75 "
        "contracted."
    ),
    "body_paragraph_2": (
        "On Noon, our \"New Year, New Me\" campaign for Befit delivered 4,176 incremental units, 31% over "
        "baseline. When an agency's report estimated reach from follower counts and counted the same creator "
        "twice across waves, I rebuilt the KPI definitions and found that creators under 20K followers were "
        "performing 10 to 40 times above the campaign average. I also built an AI workflow with Claude for "
        "planning, content and reporting that cut our manual work by about 40%. My FMCG grounding comes from "
        "category planning at Mondelez with Nielsen data, and I know the customer side from 42 brand accounts "
        "at Miravia (Alibaba) and XL accounts at Glovo."
    ),
    "closing_paragraph": (
        "I want to be direct about where this role would stretch me. My media work is digital, creators and "
        "sampling rather than TV or other ATL campaigns, and I run export markets from a central team rather "
        "than leading brands with local teams across MENA. Those are the parts I would expect to learn from your "
        "agencies and markets. The activation calendar, the launch pipeline and the test-and-learn discipline I "
        "can bring from the first week. I am based in Dubai and would welcome a conversation. Thank you for your "
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
