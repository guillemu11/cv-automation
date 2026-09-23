"""One-off: carta de presentación para **Sr. Specialist Retail Media Insight** (talabat / Delivery
Hero) — reutiliza el job de `_gen_talabat_sr_specialist_retail_media_insight.py`.

Párrafos escritos a mano y mapeados a los pilares del JD: análisis de performance e insights
accionables, frameworks de medición y definiciones de KPI, riesgo de under-delivery y optimización,
y comunicación a stakeholders senior multi-mercado.

Guardarraíles de honestidad (idénticos a los del CV):
- **Programática, modelos de atribución formales y modelado predictivo: no los tiene.** La carta lo
  dice explícitamente en vez de dejar que se descubra en la entrevista.
- Su retail media es de ANUNCIANTE, no del lado plataforma (revenue leakage, pacing de inventario,
  monetización). No se disfraza.
- Grado: BBA en CUNEF, no Estadística ni Analytics. No se reetiqueta.
- Sin árabe (el JD lo marca como preferido). Sin "no sponsorship needed": solo UAE Residence Visa.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_talabat_rmi_cv",
    ROOT / "scripts" / "_gen_talabat_sr_specialist_retail_media_insight.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # sin contacto nombrado en la oferta → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "I am one of the advertisers this role exists to serve. As Brand & Marketing Manager at DoFreeze in "
        "Dubai I buy and optimise retail media on talabat, Noon and Careem, and I have spent the past year "
        "on the question at the centre of this remit: how much of this revenue would have happened anyway? "
        "I am applying because that question is the work I enjoy most, and because the partner's-eye view "
        "is worth something to a regional insights function."
    ),
    "body_paragraph_1": (
        "Let me be clear about what I am not, so you can judge the fit properly. I have not done "
        "programmatic buying, have not built formal attribution or predictive models as a discipline, and "
        "have not worked the platform side of retail media — revenue leakage, inventory pacing and "
        "monetisation gaps are problems I have read about, not owned. My degree is in Business "
        "Administration, not statistics. What I do have is four years of commercial analysis in "
        "multi-market FMCG and e-commerce, an advanced Excel and BI habit (Power BI, Tableau, Looker), and "
        "a measurement instinct that is the harder half of this job to teach."
    ),
    "body_paragraph_2": (
        "In practice: rather than report a campaign's platform-side numbers, I ran SMASH on talabat against "
        "Befit as a control brand — same platform, same window — and measured the delta: +165% daily revenue "
        "against +4.7% for the control, roughly AED 32K incremental on AED 8.7K of spend. On Noon, 'New "
        "Year, New Me' delivered +4,176 incremental units, +31% over baseline; I do not lead with the +161% "
        "against October, because January is a natural peak for a fitness brand and that number flatters "
        "us. I also audited an agency's reporting and found reach estimated from follower counts rather "
        "than measured, the same creator counted twice across waves at 5× variance, and 'unique accounts' "
        "summed from estimates — then rebuilt the KPI definitions and moved spend to the cohorts genuinely "
        "outperforming. Before Dubai I owned the Flash Sales channel at Miravia (Alibaba) reporting to the "
        "CEO, pacing revenue against targets across 42 accounts, and began in category planning at Mondelez "
        "running sell-out analysis on Nielsen."
    ),
    "closing_paragraph": (
        "I am based in Dubai on a UAE residence visa, fluent in English and Spanish though not Arabic, and "
        "work across 50+ markets today. If the team wants a purely quantitative profile I am not the "
        "closest match, and I would rather say so. If there is room for someone who knows the advertiser's "
        "incentives from the inside and is stubborn about whether a number means what it claims, I would "
        "welcome the conversation. Thank you for your consideration."
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
