"""One-off: CV de una página para **Manager – Ecommerce (Category Management)** en
**Landmark Group** (marca Home Box — homeware/furniture e-com, Dubai).

Pide el JD: planes de negocio por categoría para el negocio e-com de Home Box; estrategia
comercial y pricing frente a la competencia online (seguimiento diario/semanal/mensual de
furniture); planificar promociones y eventos de e-commerce; forecast de productos y
cantidades asegurando disponibilidad de stock; que el rango esté bien representado en la
web; trabajar con Buyers (incl. exclusivos e-com); analizar MIS/reportes y marcar tendencias;
contenido y promoción online (95% de listing de livestock, testeo de links, comunicación de
promos con Buyers/Retail Ops/Marketing); competition mapping y market research; reportes
semanales (top sellers, ageing, NPS, feedback de producto); revisión de presupuestos de venta.

Ángulo honesto de Paula: Miravia (Alibaba) — 42 cuentas beauty/fragancias/moda con pricing,
surtido y promociones (+30% GMV QoQ), dueña del canal Flash Sales reportando al CEO; DoFreeze
— Shopify end-to-end más listings en talabat/Noon/Careem, promos, revisión semanal de riesgo
de stock por dark store; Mondelez — category planning con Nielsen (sell-in/sell-out,
efectividad promocional).

Guardarraíles de honestidad:
- Forecast: **contribuye** con Sales/Finance, no es dueña (la e-commerce manager lo es).
- Sin experiencia en homeware/furniture ni en retail de gran superficie — no se insinúa.
- Visa: solo "UAE Residence Visa" (patrocinada por el empleador); nunca "no sponsorship needed".
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

COMPANY = "Landmark Group"
TITLE = "Manager - Ecommerce (Category Management)"
DATE_FOLDER = "2026-09-22"

JOB_DESCRIPTION = """\
Manager - Ecommerce (Category Management) — Landmark Group (Home Box), Dubai, UAE. On-site, full time.
The job holder will be responsible for developing and implementing business plans for the Homeware
categories (Ecom business) to achieve the strategic and financial objectives of Home Box.
Sales and Commercial Performance: formulate and implement strategies and procedures for better commercial
performance; study online competition for Furniture on a daily/weekly/monthly basis; take corrective actions
on pricing and recommend items based on past learning and ongoing competition activities; plan
promotions/events for E-commerce sales; forecast products and quantities for the sale and ensure
inventory/stock availability; work closely to ensure the range is represented rightly on E-Com/Website;
work closely with Buyers for E-commerce exclusive product and range; analyse MIS/reports and highlight key
trends and way forward; suggest improvements based on benchmark practices.
Content and Online Promotion: ensure 95% listing of all livestock on the e-commerce portal at any given time;
circulate weekly count of active items listed vs active stocks by department; ensure timely testing of links
and implementation on the e-commerce portal; recommend e-commerce store promotions in consultation with
Buyers, Retail Ops and Marketing; ensure all required communications for promotions are developed and designed
within timeline; recommend events specific to brand, product category and season; forecast with Buyers and
Retail Operations for the increase in footfall sales during promotions.
Competition Mapping: periodic market research on customer profile/preferences and buying patterns; market
research on media campaign effectiveness vs spend with the digital marketing team; proactive tracking of
competition websites and corrective actions.
MIS: weekly category reports (top seller, ageing analysis, ecom exclusive sharing); operations reports
(NPS, CC complaints, product feedback).
Budgeting and Planning: review sales budgets and make recommendations to management.
"""

ATS = [
    "e-commerce", "category management", "business plans", "homeware", "commercial performance",
    "pricing", "online competition", "competition mapping", "market research", "promotions", "events",
    "forecast", "quantities", "inventory", "stock availability", "range", "assortment", "website",
    "buyers", "e-commerce exclusive", "MIS", "reports", "trends", "benchmark", "listing", "livestock",
    "active items", "product content", "link testing", "retail ops", "marketing", "digital marketing",
    "seasonal events", "top seller", "ageing analysis", "NPS", "customer feedback", "sales budgets",
    "budgeting", "planning", "sell-through", "conversion", "GMV", "marketplaces",
]

CONTENT = {
    "headline": "E-Commerce · Category Management · Pricing, Assortment & Promotions",
    "professional_summary": (
        "E-commerce and category professional with 5 years across Alibaba's Miravia (42 accounts: assortment, "
        "pricing and promotions, +30% GMV QoQ), Glovo and FMCG category planning, now running Shopify and "
        "marketplace categories in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Flair) | Shopify D2C + talabat, Noon, Careem | 50+ markets",
            "bullets": [
                "Own the Shopify store end-to-end — catalogue listing, product content, collections, pricing and checkout — lifting conversion rate and AOV through data-led merchandising",
                "Plan and run e-commerce promotions and seasonal events (Ramadan, New Year, 6 NPD launches) across web, talabat, Noon and Careem, aligning Buyers, Retail Ops, Marketing and 4 agencies on assets and timelines",
                "Run a weekly stock-risk and listing review by dark store to keep live SKUs available and correctly represented online; contribute to the monthly forecast with Sales and Finance",
                "Build weekly MIS dashboards on sales, conversion, sell-out and top sellers, track competitor pricing and assortment, and turn findings into corrective pricing and range actions",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 accounts as category owner — assortment, pricing strategy, online competition benchmarking and targeted promotions — delivering +30% GMV growth QoQ",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO: event calendar, item selection, quantities and P&L-aligned commercial plans",
                "Led category expansion as PIC Fragrances (30+ stores onboarded in two months) and analysed traffic, conversion, ROI and forecast accuracy to steer the range",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL partners (KFC, Taco Bell, Sushi Shop) on catalogue, promotions and GMV, and helped build the Retail vertical onboarding fashion and lifestyle brands",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness reports with Nielsen and flagged category trends and growth opportunities to the commercial team",
            ],
        },
    ],
    "skills_brand": (  # label -> "Category & Commercial"
        "category business plans, assortment & range, pricing strategy, promotions & events, sales budgets"
    ),
    "skills_ecommerce": (  # label -> "E-Commerce"
        "Shopify, marketplaces (Noon, talabat, Careem), listing & catalogue accuracy, product content, CRO"
    ),
    "skills_commercial": (  # label -> "Stakeholders"
        "buyers, retail ops, marketing, supply chain, finance, key accounts, negotiation"
    ),
    "skills_data": (  # label -> "Analytics & Planning"
        "MIS & weekly reporting, competition mapping, sell-in/sell-out, forecast support, stock availability, Nielsen"
    ),
    "skills_tools": (  # label -> "Tools"
        "Excel (Expert), PowerPoint, Shopify, Power BI, Tableau, Looker, SAP, Salesforce, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Category & Commercial",
    "E-Commerce & Digital": "E-Commerce",
    "Commercial": "Stakeholders",
    "Data & Analytics": "Analytics & Planning",
}


def make_job() -> Job:
    return Job(
        id="landmark-group-ecommerce-category-management-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://www.linkedin.com/jobs/search/?keywords=Landmark%20Group%20Manager%20Ecommerce%20Category%20Management",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Landmark Group Manager Ecommerce Category Management Dubai",
            "note": "Home Box (homeware/furniture) e-com category management. Fuerte encaje funcional "
                    "(pricing, surtido, promos, listing, MIS) pero sin experiencia en homeware/furniture "
                    "ni en retail de gran superficie. +100 solicitudes, 837 candidatos.",
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
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 72, "ai_tier": "Hot",
        "skills_match": [
            "Category ownership en Miravia: 42 cuentas, pricing, surtido y promociones (+30% GMV QoQ)",
            "Flash Sales channel owner (Beauty, Fashion & Home) reportando al CEO: calendario, selección de ítems y cantidades",
            "Shopify end-to-end + listings en talabat/Noon/Careem: catálogo, contenido, promos y disponibilidad",
            "MIS semanal (ventas, conversión, sell-out, top sellers) y benchmarking de competencia online",
            "Category planning en Mondelez con Nielsen: sell-in/sell-out y efectividad promocional",
        ],
        "missing_skills": [
            "Homeware / furniture como categoría",
            "Retail de gran superficie (buying team, ageing analysis formal)",
            "Ownership pleno de forecast y replenishment",
        ],
        "sector_fit": "medio-alto — e-commerce y category management sí; homeware/furniture no",
        "seniority_fit": "encaje — Manager, en línea con su título actual",
        "red_flags": [
            "837 candidatos y +100 solicitudes: mucha competencia",
            "Sin experiencia en homeware/furniture ni en el ecosistema Landmark/retail de gran superficie",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El JD es category management de e-commerce puro: pricing vs competencia, promociones y eventos, "
            "listing del 95% del livestock, MIS semanal y trabajo con Buyers. Paula ha hecho exactamente eso en "
            "Miravia (42 cuentas, Flash Sales) y lo hace hoy en Shopify y quick-commerce. La brecha real es la "
            "categoría (homeware/furniture) y el retail de gran superficie — se compensa con el track de marketplace."
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
