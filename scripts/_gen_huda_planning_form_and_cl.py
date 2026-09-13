"""Follow-up to _gen_huda_planning_manager_ecommerce.py — fills the application FORM fields
Huda Beauty's ATS asks for (Headline, max 127 chars · Summary · Cover letter) and produces the
cover letter as a PDF for upload.

Same honesty guardrails as the CV script: this is a demand planning / supply chain role behind an
"eCommerce" title. Nothing here claims a demand planning or supply chain seat, FuturMaster, ERP or
S&OP ownership, or forecast accuracy as an owned KPI. The cover letter states the gap in one line
and turns it into the argument — a planner who has owned the commercial inputs that move the
forecast, rather than the tool that stores it.

Outputs into output/2026-09-03/Huda Beauty - Planning Manager - eCommerce/:
  01_CV_y_Carta/CL_Paula_Huda_Beauty_Planning_Manager_-_eCommerce.pdf
  04_Aplicacion/Formulario_Huda.md   (headline + summary + CL in plain text, ready to paste)
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "Huda Beauty"
TITLE = "Planning Manager - eCommerce"
DATE_FOLDER = "2026-09-03"
CONTACT = None  # No named hiring manager in the posting.

HEADLINE_MAX = 127

# --- Field 1: Headline (hard limit 127 characters) -------------------------------------------
HEADLINE = (
    "Commercial & Category Planning · E-Commerce & Beauty · "
    "Launch, Assortment & Promo Planning across 50+ Markets"
)

# --- Field 2: Summary -------------------------------------------------------------------------
SUMMARY = (
    "Commercial and category planner with 5 years across FMCG, beauty and e-commerce, now running "
    "brand and commercial planning for a Dubai consumer group selling in 50+ markets.\n\n"
    "I own end-to-end product lifecycle planning for 6 launches a year — launch phasing, assortment "
    "decisions, pricing and go-live dates — and build the sales and stock forecast inputs behind each "
    "market's plan with commercial, supply and distributor teams. I align those plans with the "
    "promotional and trade calendar, including sampling, seeding and bundling mechanics, then read "
    "performance back within weeks of launch and adjust on early sell-out signals.\n\n"
    "My analytical grounding comes from category planning at Mondelez, where I ran sell-in/sell-out "
    "analysis and promotional effectiveness measurement for the chocolate category. At Miravia "
    "(Alibaba Group) I grew 42 beauty, fragrance and fashion accounts +30% GMV QoQ through assortment "
    "optimisation and pricing, and owned the Flash Sales channel for Beauty, Fashion and Home "
    "reporting to the CEO — sizing uplift events against P&L targets and reforecasting off early "
    "trading signals.\n\n"
    "Hands-on with Shopify, Power BI and advanced Excel, comfortable with large datasets and retail "
    "mathematics, and biased towards automating the reporting itself — I built an AI-assisted system "
    "that cut roughly 40% of manual planning and reporting work. Based in Dubai, Spanish and English, "
    "and most useful where commercial judgement and the numbers have to meet."
)

# --- Field 3: Cover letter ---------------------------------------------------------------------
CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Huda Beauty is one of the few beauty companies whose planning problem genuinely interests me: "
        "a global e-commerce business growing fast enough that launch phasing, assortment and "
        "promotional timing stop being administrative and start being the commercial strategy itself. "
        "I have spent five years on the commercial side of exactly that equation — two of them inside "
        "beauty and fragrance — and I would like to bring it to your planning team."
    ),
    "body_paragraph_1": (
        "The responsibilities in this brief are the ones I already carry. I own end-to-end product "
        "lifecycle planning for six launches a year across GCC, MENA, Asia, Europe, the USA and Africa "
        "— phasing, assortment updates, pricing and go-live dates — and I build the sales and stock "
        "forecast inputs behind each market's plan together with commercial, supply and distributor "
        "teams. I align those outputs with the promotional and trade calendar, including sampling, "
        "seeding and bundling mechanics, then monitor launch performance and adjust on early sell-out "
        "signals rather than waiting for the quarter to close. At Miravia (Alibaba Group) I grew 42 "
        "beauty, fragrance and fashion accounts by +30% GMV QoQ through assortment optimisation and "
        "pricing, and owned the Flash Sales channel for Beauty, Fashion and Home reporting to the CEO, "
        "where sizing an uplift event against P&L targets and reforecasting off early trading signals "
        "was the weekly job."
    ),
    "body_paragraph_2": (
        "I will be straightforward about where I sit. I have come to planning from the commercial side "
        "rather than from a demand planning seat: I have owned the inputs that move a forecast — launch "
        "phasing, assortment, the promotional calendar, early sell-out signals — rather than a "
        "dedicated planning tool such as FuturMaster. What that gives you is a planner who can explain "
        "why the number moved, not only that it did, and who can challenge a marketing assumption "
        "before it becomes an overstock. The analytical foundation is real: sell-in/sell-out analysis "
        "and promotional effectiveness measurement at Mondelez, retail mathematics and large-dataset "
        "work since, and hands-on Shopify, Power BI and advanced Excel. I also build the automation — "
        "an AI-assisted reporting system I put together cut around 40% of manual planning and "
        "reporting work, which is the direction this role explicitly wants to go."
    ),
    "closing_paragraph": (
        "I am based in Dubai and would welcome the chance to walk through how I plan a launch calendar "
        "across markets, and how I have handled the moments when the early signal disagreed with the "
        "plan. Thank you for your consideration — I would be glad to discuss the role further."
    ),
}


def make_job() -> Job:
    return Job(
        id="huda-beauty-planning-manager-ecommerce-dubai-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://to.indeed.com/aakpllfqwzx8",
        source="indeed",
        description="See _gen_huda_planning_manager_ecommerce.py for the full JD.",
        raw={},
    )


def _to_pdf_soffice(docx_path: Path) -> Path:
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    pdf_path = docx_path.with_suffix(".pdf")
    if Path(soffice).exists():
        try:
            subprocess.run(
                [soffice, "--headless", "--convert-to", "pdf", "--outdir",
                 str(docx_path.parent), str(docx_path)],
                check=True, capture_output=True, timeout=180,
            )
            if pdf_path.exists():
                docx_path.unlink(missing_ok=True)
                return pdf_path
        except Exception as exc:  # noqa: BLE001
            print("soffice conversion failed, falling back to docx2pdf:", exc)
    return cv._to_pdf(docx_path)


def build_form_doc() -> str:
    cl_text = "\n\n".join([
        CL_PARAGRAPHS["opening_paragraph"],
        CL_PARAGRAPHS["body_paragraph_1"],
        CL_PARAGRAPHS["body_paragraph_2"],
        CL_PARAGRAPHS["closing_paragraph"],
    ])
    return f"""\
# Formulario de solicitud — Huda Beauty · {TITLE}

> Recuerda: esta oferta es **demand planning**, no e-commerce. Lee primero
> `LEEME_ANTES_DE_APLICAR.md` en esta misma carpeta. Nada de lo de abajo afirma haber sido
> demand planner ni haber usado FuturMaster, ERP o S&OP.

---

## 1. Headline · {len(HEADLINE)}/{HEADLINE_MAX} caracteres

```
{HEADLINE}
```

---

## 2. Summary (campo obligatorio) · {len(SUMMARY)} caracteres

{SUMMARY}

---

## 3. Cover letter

Sube el PDF de `01_CV_y_Carta/CL_Paula_Huda_Beauty_Planning_Manager_-_eCommerce.pdf`.
Si el campo es de texto y no admite adjunto, pega esto:

---

Dear Hiring Manager,

{cl_text}

Kind regards,
Paula De Francisco Pérez
+971 50 386 3656 · paulich98@hotmail.com

---

## Notas para la entrevista (si llega)

- El párrafo 3 de la carta reconoce el gap de frente: viene del lado comercial, no de un puesto de
  demand planning, y no ha usado FuturMaster. Está dicho como argumento, no como disculpa —
  mantén esa línea si te lo preguntan, no la contradigas.
- Si preguntan por forecast accuracy como KPI propio: no lo ha tenido. Lo honesto es "he sido dueña
  de los inputs (phasing, surtido, calendario promocional, señal temprana), no del KPI".
- Prepara un ejemplo concreto de Flash Sales en Miravia: cómo dimensionaba un evento de uplift y
  qué hacía cuando la señal temprana no coincidía con el plan.
- Nunca "no necesito sponsorship": visado de residencia EAU patrocinado por su empresa actual.
"""


def main() -> None:
    assert len(HEADLINE) <= HEADLINE_MAX, f"Headline too long: {len(HEADLINE)} > {HEADLINE_MAX}"

    job = make_job()
    final_dir = settings.output_dir / DATE_FOLDER / f"{COMPANY} - {TITLE}"
    if not final_dir.exists():
        raise SystemExit(f"Package folder missing — run _gen_huda_planning_manager_ecommerce.py first: {final_dir}")

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL_TMP", cl_pdf)

    dest_cl = final_dir / "01_CV_y_Carta" / cl_pdf.name
    dest_cl.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(cl_pdf), str(dest_cl))
    print("OK_CL", dest_cl)

    # Clean the scratch package folder the path helper created at the output root.
    stray = cl_pdf.parent.parent
    if stray.exists() and stray.resolve() != final_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)

    form_path = final_dir / "04_Aplicacion" / "Formulario_Huda.md"
    form_path.parent.mkdir(parents=True, exist_ok=True)
    form_path.write_text(build_form_doc(), encoding="utf-8")
    print("OK_FORM", form_path)
    print(f"HEADLINE_LEN {len(HEADLINE)}/{HEADLINE_MAX}")
    print(f"SUMMARY_LEN {len(SUMMARY)}")

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(dest_cl)).pages)
        print(f"CL_PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)


if __name__ == "__main__":
    main()
