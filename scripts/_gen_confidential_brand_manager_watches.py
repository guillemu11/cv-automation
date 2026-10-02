"""One-off: CV de una página para **Brand Manager - Watches** (en el JD: "Brand, Licensing & Marketing
Manager") en una empresa **Confidential**, Dubái. Presencial, jornada completa, Solicitud sencilla en
LinkedIn. Publicado por técnico de selección ("Hiring Solutions", servicios de RRHH). Publicado hace 3
horas el 2026-10-02 y ya con **110 solicitudes**. Sin salario. Sin requisito de árabe.

El puesto es de distribuidor/licenciatario de marcas de relojería y joyería: gestiona el ciclo completo
de las marcas — desarrollo de colección con diseñadores (renderings, archivos AI, muestras), marketing y
PR, relación con los brand principals y licencias (aprobaciones, royalties), apoyo a ventas (POSM,
presentaciones, formación), proveedores y pedidos, y salud del stock (best sellers, slow movers, ageing,
phase-in/phase-out, liquidación) con presupuestos de venta y compra. Pide 3-5 años en brand, marketing,
producto o rol comercial; relojería/joyería "highly preferred"; lujo, retail premium, distribución o
FMCG "will be an advantage".

Ángulo honesto de Paula (marca de punta a punta, con disciplina comercial y de stock):
- Brand management hoy en DoFreeze (Befit, Eurocake, Flair) para UAE + 50+ mercados de exportación:
  6 lanzamientos de brief a lineal; lidera a un diseñador gráfico y a una social media executive.
- Calendario de marca y campañas con 4 agencias: 103 activaciones de creator, Befit × Noon +31% sobre
  baseline (+4.176 uds), SMASH × talabat +165% vs +4,7% de la marca control.
- Stock: revisión semanal de riesgo de stock por dark store contra las PO de las plataformas (la hace
  ella), aporta al forecast mensual de sell-in, MSL por canal (la web suya; plataformas con e-commerce
  sales).
- Apoyo a ventas: su sistema de IA genera estudios de mercado, reporting de KPIs y pitch decks.
- Premium/lifestyle: 42 marcas de belleza, fragancia y moda en Miravia (incl. KIKO Milano); abrió la
  categoría Fragancias con los distribuidores oficiales de Arabian Oud, Lattafa, Swiss Arabian y Ajmal
  (relación con dueños de marca y distribuidores); tienda en Massimo Dutti (Inditex).

Guardarraíles de honestidad:
- **Relojería / joyería**: nunca ha trabajado la categoría. No se insinúa.
- **Licencias, royalties, brand principals desde el lado licenciatario**: sin experiencia. No aparece.
- **Compras a proveedor / colocación de pedidos / value engineering**: no lo ha hecho; ella recibe PO
  de las plataformas, no las emite. No aparece.
- **Forecast**: la dueña es la e-commerce manager; Paula "contribute". Nunca "own forecast".
- **Liquidación de slow movers**: no confirmado; Flash Sales se describe como canal, sin inventar
  sell-through.
- **Deliveroo**: DoFreeze NO está en Deliveroo. Plataformas: talabat, Noon, Careem.
- Sin árabe (no se pide). Visa "UAE Employment Visa (employer-sponsored)"; nunca "no sponsorship".
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

COMPANY = "Confidential"
TITLE = "Brand Manager - Watches"
DATE_FOLDER = "2026-10-02"

JOB_DESCRIPTION = """\
Brand Manager - Watches. Confidential (posted by recruiter). Dubai, UAE. On-site, full time.
Job Purpose: We are looking for a dynamic and commercially driven Brand, Licensing & Marketing Manager to manage the
end-to-end lifecycle of our watch and jewelry brands — from product development and supplier coordination to brand
positioning, marketing execution, sales support, and stock management. The role requires a strong understanding of
luxury brand management, product trends, marketing, licensing, and the UAE/regional market, with the ability to
translate market insights into commercially successful products and brand strategies.
Brand & Product Management: develop product plans and coordinate with designers on new collections and product
concepts; liaise with designers and coordinate renderings, AI files, samples, corrections, and product development;
review value-engineering projects to ensure product quality and cost effectiveness; monitor market trends, customer
requirements, competitor activity, and product developments; provide recommendations on product design, content,
positioning, and brand development; support the sales team with product information, POSM, displays, and brand
presentations.
Marketing & Brand Communication: develop and implement strategic marketing plans across multiple channels and markets;
coordinate brand campaigns and marketing activities with internal creative/studio teams and regional teams; manage
catalogues, product communication, advertising calendars, PR, media planning, and promotional activities; coordinate
GWP and other marketing materials; ensure consistent brand positioning and communication across all markets and
customer touchpoints.
Licensing & Brand Principal Management: develop and maintain strong relationships with international brand principals
and licensing partners; understand brand DNA and ensure products and marketing activities remain aligned with brand
guidelines; coordinate product and marketing approvals with brand principals; keep brand principals updated on new
developments, collections, and marketing initiatives; monitor contractual requirements, including royalty payments.
Sales, Market & Customer Management: work closely with sales teams to develop brand and product strategies for UAE and
export markets; conduct regular market visits and competitor analysis covering products, pricing, styling, and market
trends; support new collection launches across customers and regional markets; prepare and present product updates
during sales meetings and train sales teams on key product attributes; support customer requirements, order planning,
product proposals, and slow-moving stock strategies.
Supplier & Supply Chain Coordination: coordinate with suppliers on collection planning, forecasting, pricing, and
order placement; ensure new collections are rolled out to customers well in advance; follow up on pending orders,
pricing issues, production, and deliveries; coordinate with logistics teams on incoming shipments, local deliveries,
and documentation; resolve shipment, stock, and product discrepancies.
Stock & Commercial Management: monitor sales, stock levels, product performance, and category-wise performance across
customers; analyze stock health and identify best sellers, slow movers, ageing stock, and dead stock; develop action
plans for replenishment, phase-in/phase-out of collections, and liquidation of slow-moving products; review customer
stock and recommend replenishment or pull-back strategies; monitor defective and damaged products; prepare sales,
purchase, forecasting, stock, and performance reports.
Budgeting & Performance: prepare annual sales and purchase budgets for assigned brands and channels; track monthly
performance against targets; monitor marketing and purchase budgets; analyze brand performance and provide regular
business updates to management; review credit notes and commercial adjustments related to slow-moving stock.
Requirements: Bachelor's degree or diploma in Marketing, Brand Management, Business Administration, or related field;
3-5 years of relevant experience in brand management, marketing, product management, or a related commercial role;
previous experience in watches and jewelry is highly preferred; experience in luxury, premium retail, distribution,
or FMCG/consumer brands will be an advantage; strong understanding of brand management, marketing, product
development, and UAE market dynamics; experience in advertising, promotions, campaign planning, and market analysis;
strong commercial understanding with experience in budgeting, forecasting, sales analysis, and stock management;
strong communication, negotiation, coordination, and stakeholder-management skills; ability to work with suppliers,
sales teams, creative teams, logistics, finance, and international brand principals; proficiency in Microsoft
Office, particularly Excel and PowerPoint.
Key Competencies: Brand & Product Management; Strategic Marketing; Commercial Acumen; Market & Competitor Analysis;
Licensing & Stakeholder Management; Budgeting & Forecasting; Sales & Stock Analysis; Negotiation & Communication;
Project Management; Attention to Detail.
"""

ATS = [
    "brand manager", "brand management", "brand marketing", "brand positioning", "brand guidelines",
    "brand DNA", "product development", "product management", "new collections", "product launches", "NPD",
    "designers", "creative briefs", "market trends", "competitor analysis", "market analysis", "luxury",
    "premium retail", "fashion", "beauty", "fragrance", "lifestyle", "consumer brands", "FMCG", "distribution",
    "distributors", "export markets", "UAE", "GCC", "marketing plans", "campaign planning", "advertising",
    "promotions", "PR", "media planning", "marketing calendar", "agency management", "sales support",
    "brand presentations", "trade marketing", "modern trade", "key accounts", "stock management",
    "stock health", "replenishment", "assortment", "sell-in", "sell-out", "forecasting", "budgeting",
    "A&P budget", "sales analysis", "performance reports", "KPI", "negotiation", "stakeholder management",
    "project management", "Excel", "PowerPoint", "Adobe Illustrator", "attention to detail",
]

CONTENT = {
    "headline": "Brand Manager · Product Launches · Premium Retail & Distribution · UAE & Export Markets",
    "professional_summary": (
        "Brand manager in Dubai for three FMCG brands sold across the UAE and 50+ export markets: 6 launches "
        "from brief to shelf, a team of two, and weekly sell-out and stock reviews. Before that, 42 beauty, "
        "fragrance and fashion brands at Alibaba's Miravia, and premium retail at Massimo Dutti (Inditex)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group | Befit, Eurocake, Flair | modern trade, talabat, Noon, Careem | 50+ markets",
            "bullets": [
                "Lead 6 product launches end-to-end — brief and positioning, packaging, pricing and go-to-market — for UAE retail and 50+ export markets, and lead a team of two (graphic designer and social media executive), briefing and reviewing all creative",
                "Own the brand calendar for three brands (Ramadan, back to school, New Year) with four agencies — 103 creator activations: Befit × Noon +31% over baseline (+4,176 incremental units); SMASH × talabat daily sales +165% vs +4.7% for the control brand",
                "Run the weekly stock-risk review by dark store against platform POs, contribute to the monthly sell-in forecast, and set must-stock lists by channel with the e-commerce sales team",
                "Support sales and distributors with trade promotions and brand presentations; negotiated agency fees down 30%; built an AI system (Claude) for market research, KPI reports and pitch decks, cutting ~40% of manual work",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 beauty, fragrance and fashion brands — incl. KIKO Milano — on assortment, pricing and promotional calendars, delivering +30% GMV QoQ; owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO",
                "Launched the Fragrances category as PIC, onboarding 30+ stores in two months, including the official distributors of Arabian Oud, Lattafa, Swiss Arabian and Ajmal",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build the Retail vertical, onboarding fashion and lifestyle brands beyond food delivery, and grew XL accounts (KFC, Taco Bell, La Tagliatella) through joint marketing activations",
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
    "skills_brand": (  # -> "Brand & Product"
        "brand positioning, product launches, designer briefs, packaging, market & competitor analysis"
    ),
    "skills_ecommerce": (  # -> "Marketing"
        "marketing calendars, campaigns, creator marketing, sampling & seeding, agencies, Meta & Google Ads"
    ),
    "skills_commercial": (  # -> "Sales & Distribution"
        "UAE & export markets, distributors, modern trade, quick-commerce, trade promotions, negotiation"
    ),
    "skills_data": (  # -> "Stock & Budgets"
        "sell-in/sell-out, stock-risk reviews, must-stock lists, forecast input, A&P budgets, ROI, Nielsen"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel & PowerPoint (Advanced), Adobe Illustrator & Photoshop, Canva, Power BI, SAP, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Product",
    "E-Commerce & Digital": "Marketing",
    "Commercial": "Sales & Distribution",
    "Data & Analytics": "Stock & Budgets",
}


def make_job() -> Job:
    return Job(
        id="confidential-brand-manager-watches-dubai-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=Brand%20Manager%20Watches%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Brand Manager - Watches Dubai (Confidential)",
            "note": "Empresa confidencial, publicado por técnico de selección (Hiring Solutions). Presencial en "
                    "Dubái, Solicitud sencilla en LinkedIn. En el JD el puesto es 'Brand, Licensing & Marketing "
                    "Manager' de marcas de relojería y joyería con licencia: producto con diseñadores, marketing, "
                    "brand principals y royalties, proveedores, stock y presupuestos. 3-5 años; relojería/joyería "
                    "muy preferida. 110 solicitudes en 3 horas. Sin árabe. Sin salario.",
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
        "posted_date": "2026-10-02", "raw": job.raw,
        "ai_score": 62, "ai_tier": "Warm",
        "skills_match": [
            "Brand management de punta a punta hoy: 6 lanzamientos de brief a lineal en DoFreeze",
            "UAE + 50+ mercados de exportación vía distribuidores: el mismo mapa 'UAE and export markets' del JD",
            "Lidera a un diseñador gráfico: brief y revisión de toda la creatividad (Adobe Illustrator en sus herramientas)",
            "Stock: revisión semanal de riesgo por dark store contra PO y must-stock lists por canal",
            "Calendario de marca y campañas con 4 agencias, con resultados sobre sell-out",
            "Lifestyle/premium: 42 marcas de belleza, fragancia y moda en Miravia; Massimo Dutti (Inditex)",
            "Relación con dueños de marca y distribuidores oficiales (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "3-5 años pedidos: ~4 años entre Mondelez, Glovo, Miravia y DoFreeze",
        ],
        "missing_skills": [
            "Relojería y joyería: 'highly preferred' y no la ha trabajado",
            "Licencias, royalties y aprobaciones con brand principals desde el lado licenciatario",
            "Compras a proveedor: planificación de colección, colocación de pedidos, seguimiento de producción",
            "Value engineering de producto",
            "Presupuestos anuales de venta y compra (su forecast lo cierra la e-commerce manager; ella aporta)",
            "Liquidación de slow movers y notas de crédito con clientes",
        ],
        "sector_fit": "medio — lifestyle/belleza/moda y FMCG sí; relojería y joyería no",
        "seniority_fit": "bueno — pide 3-5 años y Paula tiene ~4, con título de Brand & Marketing Manager",
        "red_flags": [
            "110 solicitudes en 3 horas: competencia alta y llegan perfiles de relojería",
            "Empresa confidencial vía agencia: no se puede investigar ni buscar contacto directo",
            "Mucho peso operativo (proveedores, pedidos, stock, royalties): más distribución que marketing",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "La mitad de marca y marketing encaja: lanzamientos de brief a lineal, trabajo con diseñador, "
            "calendario y campañas, apoyo a ventas y distribuidores en UAE y 50+ mercados de exportación, y "
            "revisión semanal de stock. Los gaps están en la mitad de distribuidor: no ha trabajado relojería ni "
            "joyería (muy preferida), ni licencias y royalties con brand principals, ni compras a proveedor. "
            "Belleza, fragancia y moda en Miravia más Massimo Dutti cubren el plus de retail premium. Sin "
            "árabe exigido. Merece el clic de Solicitud sencilla, pero con 110 candidatos en 3 horas es Warm."
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
