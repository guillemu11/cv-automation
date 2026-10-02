"""One-off: CV de una página para **E-commerce Operations Supervisor (Amazon)** en **ANTA
International** (ANTA Sports, HKEx 2020; marcas ANTA, FILA, DESCENTE, KOLON SPORT, MAIA ACTIVE,
JACK WOLFSKIN; mayor accionista de Amer Sports: Arc'teryx, Salomon, Wilson). Dubái, presencial,
jornada completa, LinkedIn Easy Apply, promocionado por técnico de selección. **1.023 solicitudes
(92 desde ayer)**, publicado hace ~1 semana. Anunciante: Gul Zarin (HR Specialist, 2º grado).
ANTA International en la región: 209 empleados, +79% en 2 años.

Pide el JD: operar el día a día de la tienda de **Amazon.ae**; planes de producto y operación
desde los targets, con ventas y rentabilidad desglosadas por categoría y SKU; análisis de mercado,
competencia y rendimiento para ajustar producto, precio, promoción y operación; ciclo de vida de
producto (lanzamientos, SKUs clave, producto de baja rotación, salud de inventario) y **planes de
reposición e inventario desde el forecast** para evitar roturas y exceso; plan y presupuesto de
**Amazon Ads** (tráfico, conversión, ROAS, **ACOS**); listings (títulos, bullets, descripciones,
imágenes, keywords, **A+ Content**); calendario promocional (Ramadán, Eid, White Friday, Prime Day);
KPIs (ventas, tráfico, conversión, ASP, inventario, ads, rentabilidad); trabajo con Merchandising,
Marketing, Supply Chain, Finanzas y Retail.
Requisitos: grado; **mínimo 3 años hands-on de operaciones en Amazon** (ideal Amazon UAE u otros
marketplaces de Oriente Medio); sportswear, calzado, moda o consumo como ventaja; **Seller
Central**, listings, Amazon Ads, promociones y tráfico; análisis comercial; merchandising e
inventario; inglés de trabajo; **árabe como ventaja** (no obligatorio).

Ángulo honesto de Paula:
- Operación de marketplace real en Oriente Medio, pero en **Noon, talabat y Careem**: alta,
  listings, mecánicas promocionales y ejecución. Noon es justo el "other Middle East marketplace"
  que el JD acepta como preferente.
- Inventario: **hace ella la revisión semanal de riesgo de stock por dark store** con cobertura de
  PO frente a demanda actual y próxima; definió el **MSL de la web**; **aporta** al forecast mensual
  de sell-in. Encaja con "minimise out-of-stock".
- Listings y conversión: la tienda **Shopify es suya** de principio a fin (fichas, colecciones,
  descuentos, merchandising con datos de conversión y AOV).
- Ads: Meta y Google Ads con audiencias, test A/B de creatividades, presupuesto y lectura de ROAS.
- Calendario promocional por temporada (Ramadán, back to school, Fitness Month, New Year) y 6
  lanzamientos; **Befit × Noon "New Year, New Me": +4.176 uds incrementales, +31% sobre baseline**.
- Lado plataforma en Miravia (Alibaba): 42 cuentas de belleza, fragancia y **moda**, +30% GMV QoQ
  con precio, surtido y promociones; canal Flash Sales reportando al CEO.
- Moda y retail: Massimo Dutti (Inditex), vertical Retail de Glovo, especialización en e-commerce
  y moda en CUNEF. Befit es marca fitness (comunidades de running y pádel): cercanía al deporte.

Guardarraíles de honestidad:
- **Amazon**: cero experiencia hands-on. Ni Seller Central, ni Vendor Central, ni Amazon Ads, ni
  ACOS, ni A+ Content, ni Prime Day. No se escribe "Amazon" en el CV.
- **DoFreeze NO está en Amazon.ae** (el script de Sanne lo decía y era una exageración). Canales:
  Shopify propio + talabat, Noon y Careem. Tampoco Deliveroo.
- **White Friday / Eid**: no constan como campañas suyas; no se mencionan.
- **Reposición**: no es dueña del plan; hace la revisión semanal de riesgo. **Forecast**: "contribute".
- **Producto de baja rotación, ASP, P&L por SKU**: sin evidencia concreta; no se afirman.
- **Nivel**: Supervisor frente a su Manager actual con dos reportes; banda probablemente por debajo
  del suelo (20.000 AED/mes). Confirmarla antes de invertir más.
- Sin árabe (ventaja, no requisito). Visa: "UAE Employment Visa (employer-sponsored)".
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

COMPANY = "ANTA International"
TITLE = "E-commerce Operations Supervisor (Amazon)"
DATE_FOLDER = "2026-10-02"

JOB_DESCRIPTION = """\
E-commerce Operations Supervisor (Amazon). ANTA International. Dubai, UAE. On-site, full time.
About us: "Keep moving". ANTA was established in 1991; ANTA Sports Products Limited, a global sportswear company, was
listed on the Main Board of HKEx in 2007. ANTA Sports engages in R&D, design, manufacturing, marketing and sales of
professional sports products including footwear, apparel and accessories, with a brand portfolio including ANTA,
FILA, DESCENTE, KOLON SPORT, MAIA ACTIVE and JACK WOLFSKIN. ANTA Sports is also the largest shareholder of Amer Sports
(Arc'teryx, Salomon, Wilson, Peak Performance, Atomic).
Job Responsibilities: manage the day-to-day operations of the Amazon UAE (Amazon.ae) store; develop product and
operational plans based on business targets, and break down sales and profitability targets by category and SKU.
Monitor UAE market trends, consumer demand, competitor activities and sales performance; conduct regular data
analysis and adjust product, pricing, promotion and operational strategies. Manage the product lifecycle on Amazon,
including new product launches, key SKU development, slow-moving product improvement and inventory health; develop
replenishment and inventory plans based on sales forecasts to minimize out-of-stock and excess inventory risks.
Develop and manage Amazon advertising plans and budgets; monitor traffic, conversion rate, ROAS and ACOS and optimize
advertising performance. Create, maintain and optimize product listings (titles, bullet points, descriptions,
images, keywords, A+ Content) to improve visibility, search ranking and conversion. Plan and execute key promotional
campaigns based on the UAE market and Amazon calendar, including Ramadan, Eid, White Friday and Prime Day. Monitor
and analyze sales, traffic, conversion rate, ASP, inventory, advertising performance and profitability, and develop
actionable improvement plans. Work closely with Merchandising, Marketing, Supply Chain, Finance, Retail and other
teams on product, inventory, pricing, promotion and sales plans.
Job Requirements: Bachelor's degree or above, with at least 3 years of hands-on Amazon operations experience;
experience with Amazon UAE or other Middle East marketplaces preferred; sportswear, footwear, fashion or consumer
goods an advantage. Strong knowledge of Amazon Seller Central, marketplace operations, listing optimization, Amazon
advertising, promotional campaigns and traffic management. Strong commercial awareness and analytical skills across
sales, traffic, conversion, advertising, inventory and profitability data. Good understanding of merchandising and
inventory management, with the ability to develop product and replenishment plans based on sales forecasts,
promotional activities and inventory levels. Good written and spoken English; Arabic is an advantage. Results-oriented
and self-driven, strong ownership and problem-solving in a fast-paced e-commerce environment. Strong communication
and cross-functional collaboration with Marketing, Merchandising, Supply Chain, Finance and other functions.
"""

ATS = [
    "e-commerce operations", "marketplace operations", "marketplace", "online store", "day-to-day operations",
    "sales targets", "category", "SKU", "product listings", "listing optimization", "titles", "descriptions",
    "images", "product content", "conversion", "traffic", "ROAS", "ROI", "advertising", "budgets",
    "promotional campaigns", "promotional calendar", "Ramadan", "pricing", "promotions", "new product launches",
    "product lifecycle", "inventory health", "out-of-stock", "replenishment", "purchase orders", "sales forecast",
    "forecasting", "assortment", "merchandising", "data analysis", "KPIs", "AOV", "GMV", "P&L", "dashboards",
    "Excel", "Noon", "talabat", "Careem", "Shopify", "Middle East marketplaces", "UAE", "GCC", "fashion",
    "sportswear", "consumer goods", "supply chain", "finance", "cross-functional", "Business Administration",
]

CONTENT = {
    "headline": "Marketplace & E-Commerce Operations · Listings, Promotions, Stock & Ads · UAE",
    "professional_summary": (
        "E-commerce and marketplace professional in Dubai who runs brands on Noon, talabat and Careem — "
        "listings, promotions, campaign calendar and a weekly stock-risk review — and owns a Shopify store "
        "and Meta/Google Ads on ROAS. Two years platform side at Miravia (Alibaba), growing 42 beauty and "
        "fashion accounts +30% GMV QoQ."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Flair) | Noon, talabat & Careem + Shopify D2C | 50+ markets",
            "bullets": [
                "Manage the brands' presence on Noon, talabat and Careem — onboarding, product listings and promotional mechanics — and own the Shopify store end-to-end: product pages, images, collections and discounts, merchandised on conversion and AOV data",
                "Run the weekly stock-risk review by dark store on Noon, talabat and Careem, checking PO coverage against current and upcoming demand to flag out-of-stock risk early; set the web must-stock list (MSL) and contribute to the monthly sell-in forecast",
                "Plan the promotional calendar — Ramadan, back to school, Fitness Month, New Year — with 6 product launches; Befit × Noon \"New Year, New Me\" delivered +4,176 incremental units, +31% over baseline",
                "Plan and optimise Meta and Google Ads (audiences, creative A/B tests, budget) on ROAS, conversion and traffic, and track SKU and channel performance on AI-assisted dashboards",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees | platform side",
            "bullets": [
                "Managed 42 beauty, fragrance and fashion seller accounts on assortment, product content, pricing and promotions, delivering +30% GMV QoQ; onboarded 30+ fragrance stores in two months",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO — event trading plans against P&L targets, using conversion, traffic, ROI and retention data to reallocate investment",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce marketplace | €500M+ revenue",
            "bullets": [
                "Helped build the Retail vertical, onboarding fashion and lifestyle brands, and grew GMV on XL accounts with in-app promotions, working across marketing, logistics and customer support",
            ],
        },
        {
            "company": "Mondelez International · Massimo Dutti (Inditex)",
            "role": "Trainee, Category Planning · Sales Associate",
            "dates": "Jun 2018 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG, Nielsen | Premium fashion retail & visual merchandising",
            "bullets": [
                "At Mondelez, sell-in/sell-out and promotional-effectiveness analysis with Nielsen; at Inditex, fashion retail, visual merchandising standards and product flow",
            ],
        },
    ],
    "skills_brand": (  # -> "Marketplace Ops"
        "product listings & content, catalogue, promotional mechanics, seller onboarding, NPD launches"
    ),
    "skills_ecommerce": (  # -> "Platforms & Ads"
        "Noon, talabat, Careem, Shopify (owner), Miravia (Alibaba), Glovo, Meta & Google Ads"
    ),
    "skills_commercial": (  # -> "Stock & Planning"
        "out-of-stock risk, PO coverage, MSL & assortment, forecast input, pricing, promo calendar"
    ),
    "skills_data": (  # -> "Analytics"
        "sales, traffic, conversion, ROAS, ROI, AOV, SKU & promo performance, P&L, dashboards"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel (Advanced), Power BI, Tableau, Looker, Salesforce, SAP, Canva & Adobe, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Marketplace Ops",
    "E-Commerce & Digital": "Platforms & Ads",
    "Commercial": "Stock & Planning",
    "Data & Analytics": "Analytics",
}


def make_job() -> Job:
    return Job(
        id="anta-ecommerce-operations-supervisor-amazon-dubai-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=ANTA%20International%20E-commerce%20Operations%20Supervisor%20Amazon",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "ANTA International E-commerce Operations Supervisor (Amazon) Dubai",
            "note": "ANTA Sports (FILA, DESCENTE, JACK WOLFSKIN; mayor accionista de Amer Sports). Operar la tienda "
                    "de Amazon.ae. Easy Apply, promocionado por técnico de selección, 1.023 solicitudes. Anunciante: "
                    "Gul Zarin (HR Specialist). Requisito duro: 3+ años hands-on en Amazon (Seller Central, Amazon "
                    "Ads, A+). Encaje: operación de marketplace en Noon/talabat/Careem, revisión semanal de stock, "
                    "Shopify propio, Miravia. Gaps: cero Amazon; nivel Supervisor.",
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
        "posted_date": "2026-09-25", "raw": job.raw,
        "ai_score": 52, "ai_tier": "Warm",
        "skills_match": [
            "Operación de marketplace en Oriente Medio: Noon, talabat y Careem (alta, listings, promociones)",
            "Revisión semanal de riesgo de stock por dark store y cobertura de PO frente a demanda",
            "Aporta al forecast mensual de sell-in y definió el MSL de la web",
            "Dueña de la tienda Shopify: fichas, imágenes, colecciones, descuentos y CRO",
            "Calendario promocional por temporada (Ramadán) y 6 lanzamientos; Befit × Noon +31% sobre baseline",
            "Meta y Google Ads con presupuesto, test A/B y lectura de ROAS",
            "Lado plataforma en Miravia (Alibaba): 42 cuentas de belleza y moda, +30% GMV QoQ, Flash Sales",
            "Moda y retail: Massimo Dutti (Inditex), vertical Retail de Glovo; marca fitness (Befit)",
        ],
        "missing_skills": [
            "Cero experiencia hands-on en Amazon: el JD pide 3+ años",
            "Amazon Seller Central, Amazon Ads (ACOS) y A+ Content: sin experiencia",
            "Prime Day, White Friday y Eid como eventos propios: no constan",
            "Plan de reposición propio y gestión de producto de baja rotación: sin evidencia",
        ],
        "sector_fit": "bueno — sportswear y moda; Paula tiene moda (Miravia, Inditex) y marca fitness (Befit)",
        "seniority_fit": "por debajo — Supervisor frente a su Manager actual con dos reportes",
        "red_flags": [
            "Requisito duro de 3+ años en Amazon que no cumple: lo filtrará un screening estricto",
            "1.023 solicitudes: sin contacto directo es lotería",
            "Nivel Supervisor: la banda puede quedar por debajo del suelo de 20.000 AED/mes",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El trabajo en sí encaja: operar un marketplace con listings, promociones, stock y ads en la UAE es lo "
            "que Paula hace en Noon, talabat y Careem, con la revisión semanal de stock y la tienda Shopify propia, "
            "y conoce la mecánica de marketplace desde el lado plataforma por Miravia. Pero el JD exige 3+ años "
            "hands-on en Amazon (Seller Central, Amazon Ads, A+ Content) y Paula no tiene ninguno, así que un "
            "screening estricto la descarta. Suma el paso atrás de nivel (Supervisor) y 1.023 solicitudes. Vale la "
            "pena si se acompaña de un mensaje directo al anunciante que venda Noon como el marketplace de Oriente "
            "Medio que el JD acepta."
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
