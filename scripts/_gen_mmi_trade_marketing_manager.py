"""One-off: CV de Paula para MMI (Maritime & Mercantile International) —
"Trade Marketing Manager" del portfolio Pernod Ricard en UAE. MMI es la
distribuidora/retailer de vinos y espirituosos del Emirates Group (Le Clos,
MMI Cheers Club).

NOTA DE FIT (honesta):
  - Trade marketing, activaciones, POS, gestión de presupuesto A&P y KPI
    reporting SÍ son suyos (DoFreeze: planes de trade/shopper por canal,
    activaciones, sampling & seeding, modern trade + quick-commerce).
  - Key account / negociación comercial con accountability de ventas SÍ
    (Miravia 42 cuentas +30% GMV QoQ; Glovo KFC, Taco Bell, La Tagliatella,
    Sushi Shop = lo más parecido a on-trade hospitality).
  - Categoría/planning FMCG con Nielsen y sell-in/sell-out SÍ (Mondelez).
  - NO tiene experiencia en liquor/beverage alcohol ni red existente de
    bartenders/venues on-trade en Dubái. No se inventa en ningún sitio.
  - Árabe: NO lo tiene y la oferta no lo pide — se omite, no se falsea.
  - Experiencia: Mondelez (ago-2021) → hoy = 5 años de trayectoria comercial,
    que cubre el "5+ years" pedido; se enuncia como trayectoria, sin inflar.

VISA: su residencia la patrocina/paga su empresa actual. NO se dice "no
necesita sponsorship" en ningún punto — solo "ya reside en Dubái, disponible
de inmediato, sin reubicación".

Rellena las plantillas reales, convierte a PDF con LibreOffice (docx2pdf/Word
falla en silencio en este Mac), registra el job para el dashboard y deja el
paquete en output/2026-09-16/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "MMI - Maritime and Mercantile International"
TITLE = "Trade Marketing Manager"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Trade Marketing Manager — MMI (Maritime & Mercantile International), Dubai, UAE.
Subsidiary of the Emirates Group. Leading distributor and retailer of premium
wines, spirits, champagne, beer and non-alcoholic beverages (Le Clos Fine Wines
& Luxury Spirits, MMI Cheers Club loyalty programme).

Job Purpose: responsible for the management of the Pernod Ricard brand portfolio
across relevant channels within the UAE market, dependable on delivery of key
agency targets and performance. Blends Trade Marketing and Brand Management to
execute strategic brand plans across the Dubai trade universe — exceptional brand
experiences across top-tier on-trade accounts while building brand presence in
retail and home delivery.

Key Responsibilities:
- Roll out brand toolkits, POS materials, and execute promotional campaigns.
- Act as the face of the brand in trade, building advocacy among bartenders and venues.
- Lead impactful activations such as tastings, rituals, incentives, and events.
- Manage budgets, report on KPIs, and track competitor activity to ensure ROI.

Required Qualifications & Experience:
- Proven track record in sales, business development and account management within
  premium beverages, luxury FMCG, or hospitality.
- 5+ years' experience in trade marketing, brand activation, or commercial roles
  with sales accountability.
- Strong negotiation, relationship management and presentation skills.
- Deep understanding of on-trade and off-trade dynamics in the UAE.
- Proficiency in Microsoft PowerPoint and Excel.

Desirable: marketing or relevant commercial qualification; international experience
or exposure; existing liquor industry expertise.
"""

ATS = [
    "Trade Marketing", "Trade Marketing Manager", "Brand Management", "brand plans",
    "brand portfolio", "Pernod Ricard", "agency targets", "on-trade", "off-trade",
    "retail", "home delivery", "brand toolkits", "POS materials", "point of sale",
    "promotional campaigns", "brand advocacy", "bartenders", "venues", "activations",
    "tastings", "rituals", "incentives", "events", "budget management", "A&P budget",
    "KPIs", "reporting", "competitor activity", "ROI", "sales accountability",
    "business development", "account management", "key account management",
    "premium beverages", "luxury FMCG", "hospitality", "negotiation",
    "relationship management", "presentation skills", "PowerPoint", "Excel",
    "UAE", "Dubai", "GCC", "MENA", "FMCG", "modern trade", "distributor management",
    "sell-in", "sell-out", "rate of sale", "visibility", "merchandising",
    "shopper marketing", "go-to-market", "P&L", "GMV", "international experience",
]

CV_CONTENT = {
    "headline": (
        "Trade Marketing & Brand Manager · On-Trade & Off-Trade Activation · "
        "Premium FMCG · Key Accounts & Sales Accountability · UAE"
    ),
    "professional_summary": (
        "Trade marketing and brand professional with 5 years in premium FMCG, beauty and F&B across the UAE "
        "and Europe. Builds brand plans by channel and executes them in trade — POS, promotions, activations "
        "and events — owning the budget, the KPIs and the sales number (42 key accounts, +30% GMV QoQ)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Build and execute trade and shopper marketing plans by channel across the UAE — brand toolkits, POS materials, promotional campaigns, activations and sampling across modern trade, retail and home delivery (Noon, Talabat, Careem, Deliveroo)",
                "Own the A&P and trade budget end-to-end, report brand and channel KPIs to senior leadership and track competitor activity and pricing to protect ROI and rate of sale",
                "Lead brand plans and go-to-market for 6 NPD launches across GCC, MENA, Europe and the USA, managing a team of two (designer + social) who deliver all trade and brand assets",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts with full sales accountability, delivering +30% GMV growth QoQ through negotiation, joint business plans, pricing, assortment and targeted promotional campaigns",
                "Grew the premium and luxury portfolio as category lead, onboarding 30+ accounts in two months — including the official distributors of Arabian Oud, Lattafa, Swiss Arabian and Ajmal",
                "Owned the Flash Sales channel for Beauty, Fashion & Home against P&L targets, reporting performance and competitor benchmarks directly to the CEO",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic hospitality and F&B accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), building relationships on the ground and growing volume through bespoke promotional activations",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Analysed sell-in/sell-out and promotional effectiveness for the chocolate category with Nielsen and advanced Excel/PowerPoint, supporting NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": (
        "trade marketing, brand management & brand plans, POS & brand toolkits, promotional campaigns, "
        "activations & events, sampling & seeding, shopper marketing, A&P & trade budget"
    ),
    "skills_commercial": (
        "key account management, sales accountability, negotiation, distributor management, modern trade"
    ),
    "skills_data": (
        "KPI tracking & reporting, ROI, sell-in/sell-out, rate of sale, competitor tracking, P&L, Nielsen"
    ),
    "skills_ecommerce": (
        "off-trade & retail execution, home delivery / quick-commerce (Noon, Talabat, Careem, Deliveroo), "
        "listings & promo mechanics, e-commerce & Shopify, Meta Ads"
    ),
    "skills_tools": (
        "PowerPoint (Advanced), Excel (Advanced), Power BI, Nielsen, Salesforce, SAP, Generative AI (Claude)"
    ),
}


def make_job() -> Job:
    return Job(
        id="mmi-trade-marketing-manager-pernod-ricard-2026-09",
        title=TITLE,
        company="MMI",
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/mmi/life/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Trade Marketing Manager Pernod Ricard MMI Dubai",
             "group": "Emirates Group (MMI & ELR)",
             "portfolio": "Pernod Ricard agency brands, UAE",
             "function": "Trade Marketing / Brand Management"},
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "url": job.url,
        "source": job.source,
        "description": job.description,
        "salary_raw": None,
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 68,
        "ai_tier": "Warm",
        "skills_match": [
            "Trade marketing & shopper plans by channel (DoFreeze, UAE)",
            "POS materials, brand toolkits, promotional campaigns & activations",
            "A&P / trade budget ownership + KPI & ROI reporting",
            "Competitor and pricing tracking",
            "Sales accountability & key account management (Miravia, 42 accounts, +30% GMV QoQ)",
            "Hospitality/F&B account management (Glovo — KFC, Taco Bell, La Tagliatella, Sushi Shop)",
            "Off-trade / retail + home-delivery execution (Noon, Talabat, Careem, Deliveroo)",
            "Category & promo analytics with Nielsen (Mondelez)",
            "Advanced PowerPoint & Excel",
            "International exposure (50+ markets) + BBA — matches desirable criteria",
        ],
        "missing_skills": [
            "Liquor / premium-beverage industry expertise — NOT held (listed as desirable)",
            "Existing on-trade network among bartenders and Dubai venues — building, not inherited",
            "Deep UAE on-trade dynamics — off-trade/retail side is strong, on-trade is adjacent (Glovo F&B)",
        ],
        "sector_fit": "adjacent (premium beverages/liquor; Paula's premium exposure is FMCG food, beauty/fragrance and F&B accounts)",
        "seniority_fit": "on-band (5 yrs commercial/trade trajectory vs 5+ asked)",
        "red_flags": [
            "Role asks for deep on-trade UAE understanding and brand advocacy among bartenders — no existing network",
            "No liquor-industry background; agency-target delivery for Pernod Ricard is a demanding, sales-accountable brief",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Solid adjacent fit generado a petición de Guille. La oferta es mitad trade marketing, mitad brand "
            "management sobre el portfolio de Pernod Ricard en UAE, con accountability de targets de agencia. "
            "Lo que encaja de verdad y se usa como columna vertebral: planes de trade/shopper por canal, POS y "
            "toolkits, campañas promocionales, activaciones y sampling, propiedad del presupuesto A&P, "
            "reporting de KPIs/ROI y seguimiento de competencia (DoFreeze, Dubái); accountability de ventas y "
            "gestión de key accounts con negociación (Miravia, 42 cuentas, +30% GMV QoQ); cuentas de "
            "hostelería/F&B en Glovo como análogo más cercano al on-trade; y analítica de categoría con Nielsen "
            "y PowerPoint/Excel avanzados (Mondelez). Gaps declarados sin maquillar: cero experiencia en "
            "liquor/bebidas alcohólicas y sin red previa de bartenders y venues on-trade en Dubái. Árabe no se "
            "menciona (no lo tiene y la oferta no lo pide). Visa: solo 'ya reside en Dubái, disponible de "
            "inmediato, sin reubicación' — nunca 'no necesita sponsorship'."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """DOCX -> PDF headless con LibreOffice (docx2pdf/Word falla en este Mac)."""
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

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    final_dir = _relocate_to_dated_folder(cv_pdf.parent.parent)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
