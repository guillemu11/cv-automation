"""One-off: carta de presentación para **Brand Manager** en **Cereal Partners Worldwide** (Nestlé &
General Mills, Dubái) — reutiliza el job de `_gen_cpw_brand_manager.py`.

Párrafos escritos a mano y mapeados a los pilares del JD: calendario anual de activación y
lanzamientos, briefs creativos y ecosistema de agencias, coordinación multi-mercado con Sales /
Trade / distribuidores, lado cliente (sell-in), y post-campaign review con eficacia medida.

Gancho: Befit es la marca better-for-you de DoFreeze y Paula hace cada enero "New Year, New Me" y
en noviembre Fitness Month — el mismo momento de consumo en el que compite FITNESS de CPW. Se
menciona como ocasión compartida, no como experiencia en cereal.

Guardarraíles de honestidad (idénticos a los del CV):
- **Matriz global → clúster y media ATL / agencia de medios: no los tiene.** La carta lo dice en una
  frase en vez de dejar que se descubra en la entrevista.
- Sin categoría cereal / desayuno; sin brand health tracking formal.
- "Negoció -30%" y "75 contratados, 103 entregados" son de las campañas de creators con agencia.
- Sin árabe (JD cortado, sin confirmar): no se menciona. Sin "no sponsorship needed": solo UAE
  Residence Visa.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_cpw_brand_manager_cv",
    ROOT / "scripts" / "_gen_cpw_brand_manager.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # sin contacto nombrado en la oferta → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Every January I run \"New Year, New Me\" for Befit, the better-for-you brand I manage at DoFreeze in "
        "Dubai, a consumer moment FITNESS knows well. I am applying for the Brand Manager role because what you "
        "describe, turning brand strategy into an activation calendar that several markets can execute and then "
        "proving what worked, is the job I do today. I would like to do it on brands with the reach of NESQUIK, "
        "FITNESS and CHEERIOS."
    ),
    "body_paragraph_1": (
        "At DoFreeze I own the annual activation calendar for three food brands sold in more than 50 markets: "
        "Ramadan, back to school, Fitness Month and New Year, plus six product launches run end-to-end from brief "
        "and packaging to pricing and go-to-market. I write the creative briefs for my team of two, a designer and "
        "a social media executive, and for four external agencies. Across three creator campaigns I negotiated "
        "30% off and received 103 creator activations against 75 contracted. Plans are built with sales and our "
        "distributors channel by channel, across modern trade, quick-commerce and our own online store. Before "
        "Dubai I sat on the customer side, with 42 brand accounts at Miravia (Alibaba) and XL accounts at Glovo, "
        "which taught me what a retailer needs to hear in a sell-in. I started in category planning at Mondelez, "
        "working with Nielsen data."
    ),
    "body_paragraph_2": (
        "I measure campaigns on sell-out, not on reach. For SMASH on talabat I used Befit as a control brand, "
        "same platform and same window with no creators, so the result means something: daily sales rose 165% "
        "against 4.7% for the control. On Noon, \"New Year, New Me\" delivered 4,176 incremental units, 31% over "
        "baseline. When an agency's report estimated reach from follower counts and counted the same creator "
        "twice across waves, I rebuilt the KPI definitions and found that micro-creators under 20K followers were "
        "performing 10 to 40 times above the campaign average. That is the post-campaign review your role asks "
        "for, and the habit I would bring to the cluster."
    ),
    "closing_paragraph": (
        "To be clear about the gaps: I have not worked inside a global matrix, taking a global brand strategy and "
        "cascading it to a cluster, because at DoFreeze I am the centre and adapt plans market by market. My media "
        "experience is paid social, search and creators rather than TV or a media agency. Those are the parts I "
        "would expect to learn from your team; the activation, briefing and measurement work I can do from the "
        "first week. I am based in Dubai on a UAE residence visa and would welcome a conversation. Thank you for "
        "your consideration."
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
