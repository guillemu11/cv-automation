"""One-off: CV de una página para **E-Commerce Specialist – IMEA** en **ECCO**
(marca danesa de calzado, familiar, fundada en 1963, ~5.800 empleados, vende en 100+ países).
Dubái, presencial, jornada completa, LinkedIn Easy Apply. Publicado por Menna Elhogaraty
(Head of People & Culture MEA). **1.050 solicitudes en un solo día** — brutal.
LinkedIn marca "Tu idoneidad para el puesto es alta".

Pide el JD: operaciones diarias de e-commerce (listings, contenido, pricing, promociones y
disponibilidad de stock); seguimiento de performance y KPIs online (conversión, tráfico, AOV,
sell-through); soporte al online trading, campañas de temporada, lanzamientos y actividad
promocional; gestión y optimización de **marketplaces** y de la relación con partners; contenido,
imagen y merchandising online correctos y a tiempo; análisis de datos con insights accionables;
coordinación con Marketing, Retail, Merchandising, Supply Chain, Finance y partners externos;
mejora de procesos y customer journey; soporte a proyectos regionales de e-commerce.
Requisitos: 3+ años en e-commerce / digital commerce / online retail, **preferiblemente en
fashion, footwear o lifestyle**; operaciones de e-commerce, online trading y KPIs comerciales;
plataformas de e-commerce, CMS y/o marketplaces; Excel y analítica fuertes; mentalidad comercial;
organizada, proactiva y hands-on; experiencia regional o multi-mercado como ventaja; inglés
fluido, **árabe como ventaja** (no obligatorio).

Ángulo honesto de Paula:
- DoFreeze: es dueña de la tienda Shopify end-to-end (catálogo, UX, colecciones, descuentos,
  checkout) con CRO y AOV, y gestiona los listings, mecánicas promocionales y disponibilidad en
  los marketplaces de EAU (Noon, talabat, Careem). Son literalmente las operaciones del JD.
- Miravia (Alibaba): **lado marketplace**, 42 cuentas de beauty, fragancias y fashion — surtido,
  pricing y calendario promocional, +30% GMV QoQ — y dueña del canal de Flash Sales reportando al
  CEO, que es online trading puro con calendario de temporada.
- Fashion y lifestyle de verdad: cuentas de fashion en Miravia, onboarding de marcas de moda al
  vertical Retail de Glovo, y base de retail en Massimo Dutti (Inditex) con visual merchandising.
- Multi-mercado: GCC, MENA y 50+ mercados de exportación.
- Excel avanzado y stack de BI (Power BI, Tableau, Looker) más dashboards automatizados con IA.

Guardarraíles de honestidad:
- **Footwear**: no lo ha trabajado. Se dice fashion y lifestyle, que sí, y no se insinúa calzado.
- **CMS / plataformas enterprise** (Salesforce Commerce Cloud, Magento, SAP Commerce): NO. Su
  plataforma es Shopify, más marketplaces. Se nombra Shopify, no se sugiere nada más.
- **Sell-through y planning de stock de moda por tallas**: gestiona disponibilidad y near-expiry en
  FMCG, no curvas de tallas. No se menciona sell-through como si lo dominara.
- **Nivel**: el puesto es Specialist y hoy es Manager. Puede ser un paso atrás de título y banda —
  verificar sueldo pronto (suelo 20.000 AED/mes).
- Sin árabe (el JD lo marca como ventaja). Visa solo "UAE Residence Visa"; nunca "no sponsorship".
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

COMPANY = "ECCO"
TITLE = "Ecommerce Specialist"
DATE_FOLDER = "2026-09-23"

JOB_DESCRIPTION = """\
E-Commerce Specialist – IMEA. ECCO. Dubai, UAE. Department: E-Commerce. Region: Middle East & Africa.
On-site, full time.
ECCO is looking for an E-Commerce Specialist to support the growth and day-to-day management of our
e-commerce business across the MEA region. The role is responsible for driving online sales performance,
maintaining strong digital execution and ensuring a seamless customer experience across ECCO's e-commerce
channels and marketplaces.
Key responsibilities: manage day-to-day e-commerce operations, including product listings, content, pricing,
promotions and stock availability; monitor online sales performance and key KPIs including conversion,
traffic, AOV and sell-through; support online trading, seasonal campaigns, product launches and promotional
activities; manage and optimise marketplace performance and relationships with relevant partners; ensure
accurate and timely product content, imagery and online merchandising; analyse e-commerce data and provide
actionable insights to improve sales and customer experience; coordinate with Marketing, Retail,
Merchandising, Supply Chain, Finance and external partners; identify opportunities to improve e-commerce
performance, processes and customer journey; support regional e-commerce projects and new digital initiatives.
What we're looking for: 3+ years of experience in E-Commerce, Digital Commerce or Online Retail, preferably
within fashion, footwear or lifestyle; strong understanding of e-commerce operations, online trading and
commercial KPIs; experience with e-commerce platforms, CMS and/or marketplaces; strong analytical and Excel
skills; commercial mindset with a strong focus on sales and results; highly organised, proactive and
hands-on; strong communication and stakeholder management skills; regional or multi-market experience is an
advantage; fluent English is required, Arabic is an advantage.
"""

ATS = [
    "e-commerce", "ecommerce", "digital commerce", "online retail", "e-commerce operations",
    "product listings", "content", "imagery", "online merchandising", "pricing", "promotions",
    "stock availability", "online trading", "seasonal campaigns", "product launches",
    "promotional activity", "marketplaces", "marketplace performance", "partner management",
    "conversion", "conversion rate optimisation", "CRO", "traffic", "AOV", "average order value",
    "sell-through", "KPIs", "commercial KPIs", "e-commerce platforms", "Shopify", "CMS",
    "catalogue management", "assortment", "customer journey", "customer experience", "UX",
    "data analysis", "actionable insights", "Excel", "Power BI", "Tableau", "Looker",
    "fashion", "lifestyle", "beauty", "retail", "multi-market", "regional", "MEA", "GCC", "MENA",
    "stakeholder management", "cross-functional", "supply chain", "merchandising", "finance",
]

CONTENT = {
    "headline": "E-Commerce & Marketplaces · Online Trading, Listings & CRO · GCC / MEA",
    "professional_summary": (
        "E-commerce and commercial manager who runs the store and the marketplaces hands-on — owning a "
        "Shopify D2C end-to-end (catalogue, content, pricing, promotions, CRO and AOV) plus listings and "
        "availability on Noon, talabat and Careem across the GCC. Two years marketplace side at Miravia "
        "(Alibaba) on 42 beauty and fashion accounts, +30% GMV QoQ, owning the Flash Sales trading calendar."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Flair) | Shopify D2C + Noon, talabat & Careem | GCC + 50+ markets",
            "bullets": [
                "Own the Shopify store end-to-end — catalogue, product content and imagery, collections, pricing, discounts, UX and checkout — lifting conversion and average order value through data-led merchandising",
                "Run day-to-day marketplace operations on Noon, talabat and Careem: listings and content, promotional mechanics, price positioning and stock availability, plus the partner relationship on each platform",
                "Trade the seasonal calendar — campaign and launch activity planned with marketing, retail and supply chain, then read daily on conversion, traffic, AOV and sell-out to adjust promotions and merchandising mid-flight",
                "Build automated dashboards and reporting on online performance across 50+ markets, turning the data into prioritised actions and executive-ready summaries for leadership",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees | platform side",
            "bullets": [
                "Managed 42 beauty, fragrance and fashion accounts on the marketplace — assortment, pricing strategy, content and promotional calendars — delivering +30% GMV growth QoQ and onboarding 30+ new stores in two months",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO: trading plans against P&L targets, revenue pacing and corrective action, tracking ROI, conversion, traffic and retention",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce platform | €500M+ revenue",
            "bullets": [
                "Helped build out the Retail vertical, onboarding fashion and lifestyle brands to the platform, and drove GMV on XL accounts through catalogue work and in-app promotional mechanics",
            ],
        },
        {
            "company": "Massimo Dutti (Inditex) · Mondelez International",
            "role": "Sales Associate · Trainee, Category Planning",
            "dates": "Jun 2018 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Premium fashion retail floor & visual merchandising | Global FMCG, Nielsen",
            "bullets": [
                "Inditex grounding in fashion retail, visual merchandising standards and product flow; at Mondelez, sell-in/sell-out and promotional-effectiveness analysis with Nielsen behind NPD launches",
            ],
        },
    ],
    "skills_brand": (  # -> "E-Commerce Operations"
        "catalogue & listings, product content & imagery, online merchandising, pricing & promotions, "
        "stock availability, UX & checkout, CRO"
    ),
    "skills_ecommerce": (  # -> "Platforms & Marketplaces"
        "Shopify (owner), Noon, talabat, Careem, Miravia (Alibaba), Glovo, marketplace partner management, "
        "Meta & Google Ads"
    ),
    "skills_commercial": (  # -> "Trading & Commercial"
        "online trading, seasonal & promotional calendar, launches, assortment, pricing strategy, "
        "partner negotiation, P&L exposure"
    ),
    "skills_data": (  # -> "Analytics & KPIs"
        "conversion, traffic, AOV, sell-out, ROI & ROAS, cohort analysis, automated dashboards, Nielsen"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel (Advanced), Shopify, Power BI, Tableau, Looker, Meta Ads, Google Ads, Salesforce, SAP, "
        "Canva & Adobe, Claude (AI automation)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "E-Commerce Ops",
    "E-Commerce & Digital": "Platforms & Marketplaces",
    "Commercial": "Trading & Commercial",
    "Data & Analytics": "Analytics & KPIs",
}


def make_job() -> Job:
    return Job(
        id="ecco-ecommerce-specialist-imea-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=ECCO%20Ecommerce%20Specialist%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "ECCO Ecommerce Specialist IMEA Dubai",
            "note": "Marca danesa de calzado (fundada 1963, familiar, ~5.800 empleados, 100+ países), rol de "
                    "e-commerce para la región MEA. Publicado por Menna Elhogaraty (Head of People & Culture "
                    "MEA) — contacto directo de RRHH, y Paula está a 2º grado. LinkedIn marca idoneidad alta. "
                    "1.050 solicitudes en un día: Easy Apply sola no basta. Encaje operativo muy directo "
                    "(Shopify + marketplaces + trading + KPIs). Ojo con el nivel: es Specialist y hoy es "
                    "Manager — verificar banda contra el suelo de 20.000 AED. Footwear no lo ha trabajado; "
                    "fashion y lifestyle sí. Sin árabe (ventaja, no requisito).",
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
        "ai_score": 76, "ai_tier": "Hot",
        "skills_match": [
            "Shopify end-to-end hoy mismo: catálogo, contenido, colecciones, descuentos, UX y checkout con CRO y AOV",
            "Operaciones de marketplace reales en Noon, talabat y Careem: listings, promociones, precio y disponibilidad",
            "Online trading con calendario de temporada — es lo que hacía como dueña de Flash Sales en Miravia",
            "Lado marketplace en Miravia (Alibaba): 42 cuentas de beauty, fragancias y fashion, +30% GMV QoQ",
            "Fashion y lifestyle de verdad: cuentas de moda en Miravia, onboarding de marcas de moda en Glovo, base de Inditex",
            "Multi-mercado: GCC, MENA y 50+ mercados, que el JD marca como ventaja",
            "Excel avanzado más Power BI, Tableau y Looker, y dashboards automatizados",
            "3+ años de e-commerce: los cumple con margen (Miravia + DoFreeze + Glovo)",
        ],
        "missing_skills": [
            "Footwear como categoría (nunca lo ha trabajado; fashion y lifestyle sí)",
            "CMS / plataformas enterprise tipo Salesforce Commerce Cloud, Magento o SAP Commerce (su plataforma es Shopify)",
            "Sell-through y planning de stock de moda por curva de tallas",
            "Árabe (marcado como ventaja, no requisito)",
        ],
        "sector_fit": "bueno — fashion y lifestyle sí, footwear no; e-commerce y marketplaces son su día a día",
        "seniority_fit": "por debajo — es un puesto de Specialist y hoy es Manager; verificar banda antes de invertir tiempo",
        "red_flags": [
            "1.050 solicitudes en un solo día: el Easy Apply se pierde en el montón",
            "Título Specialist frente a su Manager actual — posible paso atrás de banda y de scope",
            "Presencial, no híbrido",
            "ECCO lleva dos años de pérdidas según la ficha de LinkedIn — preguntar por la salud del negocio en MEA",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Es uno de los encajes más limpios de la lista a nivel de tareas: el JD describe operaciones de "
            "e-commerce y marketplaces, trading de temporada y lectura de conversión, tráfico y AOV, y eso es "
            "exactamente lo que Paula hace hoy entre la Shopify de DoFreeze y Noon, talabat y Careem, con dos "
            "años previos del lado marketplace en Miravia gestionando surtido, pricing y calendario promocional "
            "sobre 42 cuentas de beauty y fashion. El sector es fashion y lifestyle, que sí tiene; el calzado "
            "concretamente, no. Los dos peros de verdad no son de encaje: el título es Specialist cuando ella ya "
            "es Manager, así que hay riesgo de paso atrás en banda y scope, y hay 1.050 solicitudes del primer "
            "día. La vía es escribir a Menna Elhogaraty (Head of People & Culture MEA, es quien publica y está a "
            "2º grado) preguntando por el scope real y la banda antes de darlo por bueno."
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
