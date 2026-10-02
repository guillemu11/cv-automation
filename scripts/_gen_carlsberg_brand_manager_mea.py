"""One-off: CV de una página para **Brand Manager – MEA** en **Carlsberg Group** (Dubái, presencial).
Equipo de Marketing MEA. LinkedIn "Promocionado por técnico de selección", respuestas gestionadas
fuera de LinkedIn. **883 clics en «Solicitar» (363 en el último día)**. Fecha límite: 12-oct-2026.

Portfolio de Carlsberg Middle East (prensa 2024-2025): **Holsten** (bebida de malta premium,
foco Arabia Saudí), **Moussy**, **Carlsberg** y una marca nueva lanzada en 2025. Foco GCC, sobre
todo KSA y EAU. Agencia: M&C Saatchi Middle East (estrategia, PR y creatividad, contrato de 3 años
desde nov-2024), más Dentsu en medios. Campaña de referencia: "Georgina's Favourite Treat" (Holsten
× Georgina Rodríguez, Riyadh, jun-2025) — humor + hiper-localización, rodada en un baqala.
**Dorothea Drews** = Head of Marketing MEA (ex Coca-Cola Britain): con toda probabilidad la hiring
manager. Sally Shin aparece como Brand Manager en esa campaña.

Pide el JD: plan de marca y estrategia, de insight a iniciativas; oportunidades de crecimiento por
categoría, consumidor y competencia; gestionar el rendimiento de marca (ventas, volumen, cuota,
eficacia de campaña); desarrollo de comunicación con equipos internos y agencias; innovación de la
idea al lanzamiento en varios mercados; trabajar con Commercial y trade partners; Nielsen/NIQ y datos
internos para diagnosticar. Requisitos: grado o máster en Marketing/Empresa; **4+ años de marketing
FMCG** con brand management hands-on; estrategia, campañas e innovación; mentalidad analítica y
comercial (Nielsen/NIQ, research, datos comerciales); proyectos cross-funcionales; inglés fluido;
**árabe "is an advantage"** (no es requisito).

Ángulo honesto de Paula:
- Hoy es FMCG brand-side en Dubái: plan de marca y calendario de tres marcas de alimentación
  (Befit, Eurocake, Flair) en el GCC y 50+ mercados de exportación.
- Comunicación con agencias medida en venta: 4 agencias, 103 activaciones de creator; Befit × Noon
  +31% sobre baseline (+4.176 uds incrementales); SMASH × talabat +165% de venta diaria frente a +4,7%
  del grupo de control. Auditó el informe de reach de la agencia → "campaign effectiveness".
- Innovación: 6 lanzamientos NPD end-to-end.
- Commercial y trade partners: trabaja con ventas y distribuidores, modern trade y quick-commerce.
- Nielsen: en Mondelez (sell-in/sell-out y eficacia promocional en chocolate, NPD Milka Spread y
  Mini Suchard). Grado en ADE por CUNEF = cumple el requisito de titulación.

Guardarraíles de honestidad:
- **Bebidas / cerveza / malta**: no las ha trabajado. DoFreeze es alimentación. No se insinúa.
- **4+ años de FMCG marketing**: estrictamente brand-side FMCG suma ~2 años (DoFreeze + Mondelez
  trainee). El resto es lado cliente (Miravia, Glovo). No se escribe "4+ years FMCG"; el resumen
  habla de FMCG brand-side hoy y de los años totales sin etiquetarlos.
- **Cuota de mercado**: no hay evidencia de que la haya gestionado. Se habla de venta, volumen
  (unidades incrementales) y eficacia de campaña, que sí son suyos.
- **Nielsen/NIQ en DoFreeze**: no consta. Nielsen solo en Mondelez.
- **Brand health tracking / research formal**: no consta; no se menciona.
- **Traditional trade / baqalas**: su trade es modern trade + quick-commerce.
- **Forecast**: la dueña es la e-commerce manager; no aparece.
- **Deliveroo**: DoFreeze NO está en Deliveroo. Plataformas: talabat, Noon, Careem.
- Sin árabe (ES nativo + EN C1). Visa solo "UAE Residence Visa"; nunca "no sponsorship".
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

COMPANY = "Carlsberg Group"
TITLE = "Brand Manager - MEA"
DATE_FOLDER = "2026-10-01"

JOB_DESCRIPTION = """\
Brand Manager – MEA. Carlsberg Group. Dubai, UAE. On-site.
We are looking for an experienced and commercially minded Brand Manager to join our MEA Marketing team. This role
requires someone who can take real ownership of brands and projects — from identifying growth opportunities through
innovation and communication development, to commercial execution and performance management. The successful
candidate will combine strong marketing capabilities with a hands-on approach, strong analytical skills, and the
ability to lead cross-functional projects across markets, functions, and external partners.
What you'll be doing: manage every aspect of your brands – from strategy and innovation to execution and
performance. Leading the development and execution of brand plans and strategies, turning insights into actionable
initiatives. Identifying growth opportunities based on category, consumer, and competitive trends. Managing brand
performance across sales, volume, market share, and campaign effectiveness. Driving communication development with
internal teams and external agencies. Leading innovation projects from idea to launch, ensuring consumer relevance
and strong execution across markets. Collaborating with Commercial and trade partners to bring brand strategies to
life in-market. Using Nielsen/NIQ and internal data to diagnose performance and recommend impactful actions.
What we're looking for: Bachelor's or Master's Degree in Marketing, Business, Management, or a related field. 4+
years of FMCG marketing experience with strong hands-on brand management expertise. Proven experience developing and
executing brand strategies, communication campaigns, and innovation initiatives. Strong analytical and commercial
mindset, with experience using Nielsen/NIQ, consumer research, and commercial data to identify opportunities and
drive business decisions. Experience managing cross-functional projects and influencing diverse stakeholders.
Ability to balance strategic thinking with hands-on execution. A proactive, consumer-focused professional who takes
ownership and identifies growth opportunities. Strong communication and stakeholder management skills in an
international environment. Fluent English; Arabic is an advantage.
Deadline for applying: 12 October. Applications in English only, via the link.
"""

ATS = [
    "brand manager", "brand management", "brand plans", "brand strategy", "FMCG", "food", "beverages",
    "consumer-focused", "consumer insights", "category trends", "competitive trends", "growth opportunities",
    "brand performance", "sales", "volume", "campaign effectiveness", "communication development",
    "communication campaigns", "agencies", "creative briefs", "innovation", "NPD", "idea to launch",
    "product launches", "multi-market", "MEA", "GCC", "commercial", "trade partners", "trade marketing",
    "shopper marketing", "modern trade", "distributors", "key accounts", "Nielsen", "NIQ",
    "commercial data", "sell-in", "sell-out", "control group", "ROI", "ROAS", "performance diagnosis",
    "cross-functional projects", "stakeholder management", "international environment", "ownership",
    "hands-on execution", "team leadership", "social media", "influencer marketing", "Meta Ads",
    "Google Ads", "quick-commerce", "Business Administration",
]

CONTENT = {
    "headline": "Brand Manager · FMCG · Brand Plans, Innovation & Agency Communication · GCC",
    "professional_summary": (
        "FMCG brand manager in Dubai owning brand plans, innovation and communication for a food group sold "
        "in 50+ markets (Befit, Eurocake, Flair), leading a team of two. Develops campaigns with agencies "
        "and judges them on sell-out and volume — +31% over baseline on Noon. Grounded in Nielsen-based "
        "category planning at Mondelez."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Befit (better-for-you nutrition), Eurocake, Flair | GCC + 50+ markets",
            "bullets": [
                "Own the brand plans and annual calendar for three brands — Ramadan, back to school, Fitness Month and New Year peaks — turning consumer, channel and competitor insights into initiatives across the GCC and export markets",
                "Drive communication development with four agencies and 103 creator activations from creative brief to sell-out: Befit × Noon delivered +31% over baseline (+4,176 incremental units); SMASH × talabat lifted daily sales +165% vs +4.7% for the control brand",
                "Lead 6 innovation launches from idea to shelf (brief, packaging, pricing, go-to-market) and a team of two — designer and social media executive",
                "Diagnose brand performance on sell-out, volume and campaign ROI — including auditing agency reach reporting — and work with sales and distributors on trade plans across modern trade and quick-commerce",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 brand accounts (incl. KIKO Milano) on assortment, pricing and promotional calendars, delivering +30% GMV QoQ, and onboarded 30+ fragrance stores in two months as category PIC",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO — commercial plans against P&L targets, reading promotional ROI, conversion and retention to reallocate investment",
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
                "Used Nielsen for sell-in/sell-out and promotional-effectiveness analysis, identified growth opportunities and supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # -> "Brand & Innovation"
        "brand plans & strategy, consumer insights, innovation & NPD, go-to-market, team leadership"
    ),
    "skills_ecommerce": (  # -> "Communication"
        "creative briefs, agency management, integrated campaigns, social & creators, Meta & Google Ads"
    ),
    "skills_commercial": (  # -> "Commercial & Trade"
        "trade & shopper marketing, distributors & modern trade, key accounts, A&P budgets, negotiation"
    ),
    "skills_data": (  # -> "Performance & Data"
        "Nielsen, sell-in/sell-out, volume, campaign effectiveness, control groups, ROI & ROAS"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel & PowerPoint (Advanced), Power BI, Nielsen, SAP, Salesforce, Canva & Adobe, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Innovation",
    "E-Commerce & Digital": "Communication",
    "Commercial": "Commercial & Trade",
    "Data & Analytics": "Performance & Data",
}


def make_job() -> Job:
    return Job(
        id="carlsberg-brand-manager-mea-dubai-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=Carlsberg%20Brand%20Manager%20MEA%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Carlsberg Group Brand Manager MEA Dubai",
            "note": "Equipo de Marketing MEA en Dubái, presencial. Portfolio ME: Holsten (malta premium, foco KSA), "
                    "Moussy, Carlsberg. Agencia M&C Saatchi ME. Head of Marketing MEA: Dorothea Drews (ex Coca-Cola), "
                    "probable hiring manager. Promocionado por técnico de selección; solo se aceptan solicitudes por "
                    "el enlace. 883 clics en «Solicitar» (363 en un día). Fecha límite 12-oct. Árabe = ventaja, no "
                    "requisito. Gaps: bebidas, 4+ años FMCG estrictos, cuota de mercado y NIQ en el puesto actual.",
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
        "posted_date": "2026-09-29", "raw": job.raw,
        "ai_score": 74, "ai_tier": "Warm",
        "skills_match": [
            "FMCG brand-side hoy mismo en Dubái: plan de marca de Befit, Eurocake y Flair en el GCC y 50+ mercados",
            "Comunicación con agencias medida en venta: Noon +31% sobre baseline, talabat +165% frente a +4,7% del control",
            "Eficacia de campaña real: auditó el informe de reach de la agencia y midió con grupo de control",
            "Innovación de la idea al lanzamiento: 6 NPD end-to-end",
            "Trabaja con ventas, distribuidores, modern trade y quick-commerce (talabat, Noon, Careem)",
            "Nielsen, sell-in/sell-out y eficacia promocional en Mondelez",
            "Grado en ADE (CUNEF) y equipo propio de dos personas",
            "Árabe solo como ventaja, no como requisito",
        ],
        "missing_skills": [
            "Categoría bebidas / malta / cerveza: no la ha trabajado",
            "4+ años de FMCG marketing estrictos: brand-side suma ~2 (DoFreeze + Mondelez)",
            "Gestión de cuota de mercado y NIQ en su puesto actual",
            "Brand health tracking y research formal",
            "Traditional trade (baqalas), clave para Holsten en KSA",
        ],
        "sector_fit": "bueno — FMCG brand-side y multi-mercado GCC, aunque en alimentación, no bebidas",
        "seniority_fit": "en línea — Brand Manager frente a su Brand & Marketing Manager actual",
        "red_flags": [
            "883 solicitudes: hace falta la vía directa a Dorothea Drews además de solicitar",
            "Solo aceptan solicitudes por el enlace: el mensaje acompaña, no sustituye",
            "El filtro de 4+ años FMCG puede pesar en el primer corte",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El puesto pide lo que Paula hace hoy en DoFreeze: plan de marca, comunicación con agencias, "
            "innovación y trabajo con ventas y distribuidores en varios mercados del GCC, con resultados de "
            "venta medidos con grupo de control. Cumple la titulación y el árabe no es requisito. Le restan el "
            "salto de categoría a bebidas, que su experiencia FMCG brand-side es de ~2 años frente a los 4+ "
            "que piden, y que no ha gestionado cuota de mercado ni NIQ en su puesto actual. Con 883 "
            "solicitudes, la vía buena es escribir directamente a Dorothea Drews, Head of Marketing MEA."
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
