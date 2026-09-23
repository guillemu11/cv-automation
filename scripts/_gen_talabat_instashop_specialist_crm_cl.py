"""One-off: carta de presentación para **Specialist CRM – instashop** (talabat / Delivery Hero) —
reutiliza el job de `_gen_talabat_instashop_specialist_crm.py`.

Párrafos escritos a mano y mapeados a los pilares del JD: lifecycle y retención, segmentación y
datos de cliente, A/B testing y optimización, y colaboración cross-funcional con brand, commercial
y performance.

Guardarraíles de honestidad (idénticos a los del CV, y aquí es especialmente importante):
- **Braze: no lo ha usado.** La carta lo DICE de frente en vez de esquivarlo, y explica qué sí
  tiene y por qué la herramienta es lo aprendible. Es mejor que el recruiter lo lea en sus
  términos que lo deduzca del CV.
- No se reclaman journeys automatizados con triggers, ni push/in-app/SMS, ni compliance GDPR.
- Sin árabe. Sin "no sponsorship needed": solo UAE Residence Visa.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_talabat_instashop_crm_cv",
    ROOT / "scripts" / "_gen_talabat_instashop_specialist_crm.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # sin contacto nombrado en la oferta → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "instashop's retention problem is one I have been on the other side of. I am a brand that sells on "
        "q-commerce in the UAE — talabat, Noon and Careem — so I spend my time on the question your CRM "
        "function asks every week: what actually brings a customer back, and how would we know it was us? "
        "That is why this role caught my attention, and why I want to be direct about where I am strong "
        "and where I am not."
    ),
    "body_paragraph_1": (
        "Starting with the gap, because it is the one that matters: I have not worked in Braze, have not "
        "owned a lifecycle journey inside a CRM platform, and have not run push, in-app or SMS as my own "
        "channels. What I have built is the thinking the platform executes. At DoFreeze I own our Shopify "
        "D2C business end-to-end — customer base, segmentation, EDM, merchandising and checkout — and run "
        "it for repeat purchase and average order value, not traffic. I A/B test creative, audiences and "
        "offers on Meta and Google Ads and move budget on what the data says; Salesforce has been in my "
        "stack since Miravia. The platform is what I would have to learn; the customer logic I already do."
    ),
    "body_paragraph_2": (
        "The habit I would bring is measuring retention honestly. Running SMASH with talabat, I did not "
        "report the campaign's own numbers — I held Befit as a control brand on the same platform and "
        "window: SMASH went from AED 355 to 940 in daily revenue, +165%, holding at roughly double "
        "afterwards, against +4.7% for the control. On Noon, 'New Year, New Me' delivered +4,176 "
        "incremental units, +31% over baseline. I designed a purchase-to-enter cashback activation with "
        "talabat, which is a frequency mechanic dressed as a giveaway. At Miravia (Alibaba) I created "
        "'Beauty Club', a loyalty programme built for repeat purchase, and analysed conversion, traffic and "
        "retention across 42 accounts. I have also audited an agency's reporting and found reach estimated "
        "from follower counts — so I check how a metric is built before I trust a dashboard."
    ),
    "closing_paragraph": (
        "I am based in Dubai on a UAE residence visa and know the q-commerce customer here from both sides "
        "— inside a platform at Glovo, and as a merchant on talabat, Noon and Careem. If you are open to "
        "someone who would need a ramp on Braze but arrives fluent in the business, the segments and the "
        "honest measurement of retention, I would very much like to talk. Thank you for your consideration."
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
