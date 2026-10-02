"""One-off: CV de una página para **Experienced Brand Manager** en **Procter & Gamble**, Dubai General
Office. Presencial, jornada completa. LinkedIn "Promocionado por técnico de selección", respuestas
gestionadas fuera de LinkedIn (se solicita en el portal de P&G). Job Number R000159197. **320 clics en
«Solicitar», 92 en el último día.** P&G tiene a la vez un Senior Brand Manager abierto en Dubái.
Paula tiene 6 antiguos alumnos de CUNEF en P&G (P&G ha contratado a 6 personas de CUNEF).

El JD es la plantilla genérica de P&G "Category End to End - Band 1": participar en el desarrollo e
implantación de nuevas ideas, procedimientos, servicios o productos bajo supervisión; centrarse en
tareas o segmentos concretos de una categoría con objetivos definidos; identificar, definir y analizar
problemas; colaborar con el equipo inmediato; aprender. Requisitos: **2-4 años de experiencia de marca**;
**árabe es un plus** (no obligatorio). Job Segmentation: "Entry Level" (Band 1 es el escalón de
Assistant Brand Manager / Brand Manager de contratación experimentada en P&G).

Ángulo honesto de Paula (la escuela P&G: consumidor → producto, packaging, comunicación, ejecución en
punto de venta y valor → resultados de negocio):
- Brand management FMCG hoy en DoFreeze (Befit, Eurocake, Flair; 50+ mercados): 6 lanzamientos NPD
  end-to-end (brief y posicionamiento, packaging, precio, go-to-market) = innovación de producto.
- Calendario de marca por momentos de consumo (Ramadán, back to school, Fitness Month, New Year) con
  briefs creativos y equipo de dos (diseñador + social media executive).
- Resultados medidos sobre sell-out: 4 agencias, 103 activaciones de creator en 3 campañas; Befit × Noon
  +31% sobre baseline (+4.176 uds incrementales); SMASH × talabat +165% de venta diaria contra +4,7% del
  grupo de control (Befit).
- "Identify, define and analyze problems": auditó el informe de la agencia (reach estimado desde
  seguidores, cuentas contadas dos veces) y evalúa campañas sobre sell-out contra una marca control;
  negoció -30% en fees de agencia.
- Base FMCG multinacional en Mondelez (sell-in/sell-out, eficacia promocional con Nielsen, NPD Milka
  Spread y Mini Suchard).
- Belleza desde el lado comercial (Miravia: 42 marcas, incl. KIKO Milano), relevante si la vacante cae
  en Beauty / Personal Care (Pantene, H&S, Herbal Essences, Olay).

Guardarraíles de honestidad:
- **Años de brand**: su título de marca es desde oct-2025 + trainee de category planning en Mondelez;
  el resto es key account. No se dice "4+ years in brand management"; se dice FMCG brand, category y
  key accounts.
- **Categoría P&G**: no ha trabajado haircare, fabric care, oral care ni baby care. No se insinúa.
- **Brand health tracking / equity research** (BHT, Kantar, CMK): sin evidencia; no aparece.
- **Media ATL / TV / agencia de medios**: su media es Meta, Google y creators.
- **Matriz global → local**: no la ha vivido desde marketing.
- **Forecast**: la dueña es la e-commerce manager; no aparece.
- **Deliveroo**: DoFreeze NO está en Deliveroo. Plataformas: talabat, Noon, Careem.
- Sin árabe (es un plus, no un requisito). Visa solo "UAE Residence Visa"; nunca "no sponsorship".
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from docx import Document

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Procter & Gamble"
TITLE = "Experienced Brand Manager"
DATE_FOLDER = "2026-10-01"

JOB_DESCRIPTION = """\
Experienced Brand Manager. Procter & Gamble. Dubai General Office, UAE. On-site, full time. Job Number R000159197.
Job Description: Category End to End - Band 1.
Job Family Summary: The Category End to End job family encompasses a range of roles that contribute to the
management and execution of strategies within a team or organization. These roles participate in the development
and implementation of new ideas, techniques, procedures, services, or products under guidance.
Job Description: This role supports and assists in executing strategies within the team or organization. The focus
is on specific tasks or segments within a category with clearly defined and narrow objectives, often at a local or
site level. The role requires identifying, defining, and analyzing straightforward problems. Solutions are generally
found within the body of know-how or experience and are subject to review.
Key Responsibilities: participate in the development and implementation of new ideas, techniques, procedures,
services, or products under guidance; focus on specific tasks or segments within a category with clearly defined
objectives; identify, define and analyze straightforward problems; collaborate effectively within immediate team or
work domain as required to maximize job impact and personal learning; work under direct supervision and follow
well-defined precedents and policies.
Qualifications: ability to work under direct supervision and follow well-defined precedents and policies;
capability to identify, define, and analyze straightforward problems; demonstrated ability to collaborate
effectively within immediate team or work domain; eagerness for personal learning and growth; Arabic speaking is a plus.
Job Qualifications: 2-4 years of brand experience. Arabic Speaking is a plus.
Job Schedule: Full time. Job Segmentation: Entry Level.
"""

ATS = [
    "brand manager", "brand management", "brand experience", "brand building", "brand strategy",
    "brand positioning", "category", "category management", "FMCG", "consumer goods", "beauty",
    "personal care", "consumer", "consumer moments", "innovation", "new products", "NPD", "product launches",
    "packaging", "pricing", "go-to-market", "brand communication", "creative briefs", "integrated campaigns",
    "social media", "influencer marketing", "agency management", "retail execution", "in-store",
    "modern trade", "e-commerce", "quick-commerce", "trade promotions", "distributors", "key accounts",
    "problem solving", "analysis", "analytical", "identify, define and analyze problems", "data-driven",
    "Nielsen", "sell-in", "sell-out", "promotional effectiveness", "control group", "ROI", "ROAS",
    "business results", "P&L", "collaboration", "cross-functional", "team", "learning", "leadership",
    "GCC", "UAE", "multi-market",
]

CONTENT = {
    "headline": "Brand Manager · FMCG & Beauty · Innovation & Retail Execution · UAE",
    "professional_summary": (
        "FMCG brand manager in Dubai building three food brands sold in 50+ markets: 6 launches end-to-end, "
        "a team of two, and every campaign judged on sell-out. Category planning at Mondelez (Nielsen, NPD) "
        "and 42 beauty, fragrance and fashion brands at Alibaba's Miravia, incl. KIKO Milano."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group | Befit, Eurocake, Flair | modern trade, talabat, Noon, Careem | 50+ markets",
            "bullets": [
                "Lead 6 product launches end-to-end — brief and positioning, packaging, pricing and go-to-market — across modern trade, quick-commerce (talabat, Noon, Careem) and 50+ export markets",
                "Own the brand calendar for three brands around key consumer moments (Ramadan, back to school, Fitness Month, New Year), writing creative briefs and leading a team of two — designer and social media executive",
                "Run creator campaigns with four agencies — 103 activations over three campaigns: Befit × Noon +31% over baseline (+4,176 incremental units); SMASH × talabat lifted daily sales +165% vs +4.7% for the control brand",
                "Audited agency reports (reach estimated from followers, accounts double-counted) and judge every campaign on sell-out against a control brand; negotiated agency fees down 30% and plan trade promotions with sales and distributors",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 beauty, fragrance and fashion brands — incl. KIKO Milano makeup & skincare — on assortment, pricing and promotional calendars, delivering +30% GMV QoQ across the portfolio",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO, and created the Beauty Club and Hot on Social programmes to lift brand visibility",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL accounts (KFC, Taco Bell, La Tagliatella) on GMV and joint marketing activations, coordinating marketing, logistics and customer support to deliver campaigns",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | chocolate category (Milka, Suchard)",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis with Nielsen and supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # -> "Brand & Innovation"
        "brand strategy & positioning, 6 NPD launches, packaging & pricing, creative briefs, team of two"
    ),
    "skills_ecommerce": (  # -> "Brand Communication"
        "integrated campaigns, social media, creator marketing, agency management, Meta & Google Ads"
    ),
    "skills_commercial": (  # -> "Retail Execution"
        "modern trade, quick-commerce (talabat, Noon, Careem), trade promotions, distributors, key accounts"
    ),
    "skills_data": (  # -> "Analysis & Results"
        "sell-in/sell-out, Nielsen, promotional effectiveness, control-group testing, ROI & ROAS, P&L targets"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel & PowerPoint (Advanced), Power BI, Nielsen, SAP, Salesforce, Canva & Adobe, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Innovation",
    "E-Commerce & Digital": "Brand Communication",
    "Commercial": "Retail Execution",
    "Data & Analytics": "Analysis & Results",
}


def make_job() -> Job:
    return Job(
        id="pg-experienced-brand-manager-dubai-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=Procter%20%26%20Gamble%20Experienced%20Brand%20Manager%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Procter & Gamble Experienced Brand Manager Dubai",
            "note": "Dubai General Office, presencial. Job Number R000159197. JD genérico de P&G 'Category End to "
                    "End - Band 1': 2-4 años de experiencia de marca, árabe es un plus. Segmentación 'Entry Level' "
                    "(Band 1 = escalón de entrada a brand management en P&G). Se solicita en el portal de P&G. "
                    "320 clics en «Solicitar», 92 en el último día. 6 alumni de CUNEF en P&G. P&G publica a la vez "
                    "un Senior Brand Manager en Dubái. Encaje FMCG brand + NPD + sell-out medido; gap: categorías "
                    "P&G (hair/fabric/oral) y años de brand con título.",
        },
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id, "title": job.title, "company": job.company, "location": job.location,
        "url": job.url, "source": job.source, "description": job.description,
        "salary_raw": "Not disclosed",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": "2026-09-28", "raw": job.raw,
        "ai_score": 76, "ai_tier": "Hot",
        "skills_match": [
            "Brand management FMCG hoy mismo: Befit, Eurocake y Flair, vendidas en 50+ mercados",
            "6 lanzamientos NPD end-to-end (posicionamiento, packaging, precio, go-to-market) = innovación de producto",
            "Resultados sobre sell-out con grupo de control: Noon +31% sobre baseline, talabat +165% frente a +4,7%",
            "Problema identificado y analizado: auditó el informe de reach inflado de la agencia",
            "Base FMCG multinacional en Mondelez con Nielsen, sell-in/sell-out y eficacia promocional",
            "Belleza desde el lado comercial (42 marcas en Miravia, incl. KIKO Milano) si la vacante es Beauty",
            "Ejecución en punto de venta: modern trade, talabat, Noon y Careem",
            "CUNEF: 6 alumni trabajan en P&G",
        ],
        "missing_skills": [
            "Categorías P&G (haircare, fabric care, oral care, baby care): no las ha trabajado",
            "Años de brand con título: 1 año en DoFreeze + 1 de category planning en Mondelez (el resto es key account)",
            "Brand health / equity research formal (BHT, Kantar): su medición es sobre sell-out",
            "Media ATL y TV: su media es Meta, Google y creators",
            "Árabe: es un plus, no lo tiene",
        ],
        "sector_fit": "muy bueno — FMCG y brand management, la escuela P&G",
        "seniority_fit": "por debajo — Band 1 'Entry Level' frente a su Brand & Marketing Manager actual; el nombre P&G lo compensa",
        "red_flags": [
            "320 solicitudes y subiendo (92 en un día): conviene un referido vía los alumni de CUNEF",
            "Band 1 'Entry Level': paso atrás en título y probablemente en salario",
            "P&G suele pedir un assessment online tras el CV: proceso largo",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El oficio encaja: brand management FMCG con innovación de producto, calendario de marca, briefs, "
            "ejecución en punto de venta y resultados medidos sobre sell-out con grupo de control, más base de "
            "Mondelez con Nielsen. El JD es la plantilla genérica de P&G y pide 2-4 años de marca: Paula los "
            "cubre sumando DoFreeze y Mondelez, con key account de apoyo. Gaps: no conoce las categorías P&G "
            "(hair, fabric, oral) ni el brand health tracking formal, y no habla árabe (solo es un plus). El "
            "rol es Band 1 'Entry Level', un paso atrás en título, pero la marca P&G pesa en el CV. Con 320 "
            "solicitudes, la vía real es un referido de los 6 alumni de CUNEF."
        ),
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relabel_for_role(docx_path: Path) -> None:
    doc = Document(str(docx_path))
    for table in doc.tables:
        for row in table.rows:
            first = row.cells[0]
            new = ROLE_LABELS.get(first.text.strip())
            if not new:
                continue
            para = first.paragraphs[0]
            if para.runs:
                para.runs[0].text = new
                for r in para.runs[1:]:
                    r.text = ""
            else:
                para.add_run(new)
    doc.save(str(docx_path))


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


def _relocate_to_dated_folder(pos_dir: Path) -> Path:
    dated_parent = settings.output_dir / DATE_FOLDER
    dated_parent.mkdir(parents=True, exist_ok=True)
    dest = dated_parent / pos_dir.name
    if pos_dir.resolve() == dest.resolve():
        return dest
    if dest.exists():
        for sub in pos_dir.iterdir():
            target = dest / sub.name
            if sub.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                for f in sub.iterdir():
                    shutil.move(str(f), str(target / f.name))
            else:
                shutil.move(str(sub), str(target))
        shutil.rmtree(pos_dir, ignore_errors=True)
    else:
        shutil.move(str(pos_dir), str(dest))
    return dest


def main() -> None:
    job = make_job()
    register_in_dashboard(job)

    cv_docx = cv._fill_template(CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
