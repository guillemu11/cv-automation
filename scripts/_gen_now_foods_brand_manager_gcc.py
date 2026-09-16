"""One-off: CV de Paula para el puesto de Brand Manager de NOW Foods (nutracéuticos /
suplementos) en GCC, dentro de NCH.

NOTA DE FIT (honesta — es un STRETCH claro):
  - La oferta pide 8+ años en brand management en wellness/healthcare, licenciatura
    en Farmacia o Nutrición + MBA, y experiencia gestionando equipos dentro de
    nutracéuticos / suplementos / consumer healthcare. Paula tiene ~5 años, BBA
    (CUNEF), sin MBA, y NO viene de pharma ni de suplementos.
  - Lo que SÍ es suyo y sostiene la candidatura: brand strategy y plan anual,
    ownership de presupuesto A&P y trade, NPD end-to-end (6 lanzamientos),
    distribución y desarrollo de canal (modern trade + quick-commerce UAE),
    forecasting y coordinación con supply chain, gestión de equipo (2 reportes)
    y accountability comercial real (Miravia, 42 cuentas, +30% GMV QoQ).
  - Gancho de categoría real: Befit, la marca better-for-you / health snacking de
    DoFreeze que ella lidera — es lo más cercano a wellness que tiene, y es cierto.
  - P&L: en Miravia trabajó el canal Flash Sales contra objetivos de P&L. NO se
    dice que sea dueña de un P&L de marca completo. En DoFreeze es dueña del
    presupuesto A&P/trade, no del forecast (ver memoria dofreeze-ecommerce-forecast-ownership).
  - NO se inventa: farmacia, medical detailing, field force, tender business,
    regulatory de healthcare, MBA ni árabe.

VISA: su residencia la patrocina/paga su empresa actual. NO se dice "no necesita
sponsorship" en ningún punto.

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

COMPANY = "NCH - NOW Foods GCC"
TITLE = "Brand Manager - NOW Foods (GCC)"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Brand Manager - NOW Foods (www.nowfoods.com), GCC markets. End-to-end management of
an assigned nutraceutical brand across GCC, covering strategy development, commercial
performance and operational execution. Accountable for revenue growth, profitability
and market share while ensuring compliance with healthcare regulations, internal
governance standards and brand guidelines.

What You Will Own:
- Brand Strategy, Business Planning & P&L: own short and long-term GCC strategy;
  lead annual business planning (revenue, profitability, market share, distribution,
  portfolio, brand investment); direct accountability for brand P&L including gross
  margin, marketing investment and trade spend; manage trade-offs between growth,
  margin, pricing and inventory; lead business reviews and corrective actions.
- Distribution & Channel Development: define and implement distribution strategy
  across key accounts and channels; expand high-potential accounts and rationalise
  underperformers; monitor channel contribution; contribute to tender and
  institutional business planning; align with Sales on execution.
- Marketing Strategy & Budget Governance: manage annual brand marketing and trade
  budget offline and online against ROI targets; allocate across medical, trade and
  digital; ensure compliance with brand guidelines and regulatory requirements;
  manage accruals and variances with Finance; partner with principals to localise
  global strategies.
- Brand Activation & Omnichannel Execution: translate strategy into integrated plans
  across medical promotion, trade and digital; ensure consistent messaging and visual
  identity; optimise campaign effectiveness; leverage digital platforms and analytics
  for omnichannel growth.
- Forecasting, Supply & Inventory Management: lead brand-level forecasting and demand
  planning; work with Supply Chain on availability and service levels; manage
  slow-moving and near-expiry stock; support launches, relaunches and phase-outs;
  identify portfolio gaps and contribute to NPD and line extensions.
- Field Excellence & Customer Engagement: define medical detailing priorities, target
  segments and core messages; refine segmentation and targeting for field force
  effectiveness; equip field teams with compliant materials; conduct field visits;
  leverage CRM insights.
- Team Contribution & Cross-Functional Collaboration: contribute to a high-performance
  team in line with NCH Culture DNA; support development through coaching and feedback;
  drive cross-functional collaboration with Sales, Marketing, Medical, Supply Chain,
  Regulatory, Finance and Digital.

Qualifications & Skills:
- Bachelor's degree in Pharmacy, Nutrition or a related field, with an MBA.
- 8+ years of experience in brand management and business development in the
  wellness/healthcare industry across channels including pharmacies, tender and e-commerce.
- Strong experience managing teams within nutraceuticals, dietary supplements,
  consumer healthcare or another relevant consumer-led sector.
- Proven responsibility for a significant brand, category, portfolio or business unit
  and hands-on experience managing P&L, revenue, gross margin, pricing, budgets and profitability.
- Experience managing international brand principals, manufacturers or regional partners
  is strongly preferred.
- Strong critical thinking, commercial negotiation, stakeholder management and influencing.
"""

ATS = [
    "Brand Manager", "brand management", "brand strategy", "nutraceutical",
    "dietary supplements", "consumer healthcare", "wellness", "health and nutrition",
    "GCC", "UAE", "Dubai", "MENA", "annual business planning", "business planning",
    "P&L", "profit and loss", "revenue growth", "gross margin", "profitability",
    "market share", "brand investment", "trade spend", "pricing", "portfolio development",
    "distribution strategy", "channel development", "key accounts", "modern trade",
    "pharmacies", "e-commerce", "omnichannel", "business reviews", "corrective actions",
    "marketing budget", "trade budget", "A&P budget", "budget governance", "ROI",
    "accruals", "variances", "Finance", "brand guidelines", "compliance",
    "brand principals", "international principals", "regional partners", "distributor management",
    "brand activation", "integrated marketing plans", "campaign effectiveness",
    "digital campaigns", "data analytics", "customer engagement", "CRM",
    "forecasting", "demand planning", "supply chain", "inventory management",
    "stock-outs", "near-expiry", "slow-moving stock", "product lifecycle",
    "launches", "relaunches", "phase-outs", "NPD", "new product development",
    "line extensions", "portfolio optimisation", "segmentation", "targeting",
    "team leadership", "people management", "coaching", "cross-functional collaboration",
    "stakeholder management", "commercial negotiation", "critical thinking",
    "go-to-market", "sell-in", "sell-out", "GMV", "category management", "trade marketing",
]

CV_CONTENT = {
    "headline": (
        "Brand Manager · Health & Wellness FMCG · Annual Planning & Budget · Distribution, Trade & E-Commerce · GCC"
    ),
    "professional_summary": (
        "Brand and commercial manager with 5 years across health-positioned FMCG, beauty and e-commerce in "
        "the UAE and Europe. Leads Befit, a better-for-you nutrition brand, across GCC and 50+ export markets — "
        "owning brand strategy, the annual plan, the A&P and trade budget, distribution, NPD and forecasting, with a team of two."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Brands: Befit (better-for-you nutrition), Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own brand strategy and the annual plan for a health-positioned portfolio across GCC and export markets — objectives for revenue, distribution, portfolio and brand investment, with business reviews to close gaps",
                "Govern the full A&P and trade budget across trade, retail and digital — allocating by channel on ROI data, tracking variances with Finance, and managing pricing and promo trade-offs to protect margin",
                "Define distribution and channel strategy across modern trade, distributors and UAE e-commerce and quick-commerce (Noon, Talabat, Careem, Deliveroo), monitoring account contribution",
                "Lead NPD end-to-end for 6 launches plus relaunches and phase-outs, and feed brand-level forecasting with Supply Chain to protect availability and manage slow-moving and near-expiry stock",
                "Lead and coach a team of two (designer + social media executive) and partner with international principals to localise global brand guidelines compliantly",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts with full commercial accountability, delivering +30% GMV growth QoQ through negotiation, joint business planning, pricing and assortment",
                "Owned the Flash Sales channel for Beauty, Fashion & Home against P&L targets, reporting revenue, margin and channel contribution directly to the CEO and driving corrective actions",
                "Led category expansion as portfolio lead, onboarding 30+ accounts in two months, reducing over-reliance on a few partners",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) and negotiated high-impact commercial deals maximising profitability for both sides",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | 90K+ employees",
            "bullets": [
                "Analysed sell-in/sell-out and promotional effectiveness with Nielsen, supporting NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (
        "brand strategy, annual business planning, portfolio & lifecycle management, NPD & line extensions, "
        "brand activation, trade & shopper marketing, team leadership"
    ),
    "skills_commercial": (
        "distribution & channel strategy, key account management, distributor & principal management, "
        "modern trade, commercial negotiation, pricing & assortment"
    ),
    "skills_data": (
        "A&P & trade budget governance, margin & ROI, P&L targets, forecasting & demand planning, "
        "inventory health, sell-in/sell-out, Nielsen"
    ),
    "skills_ecommerce": (
        "e-commerce & quick-commerce (Noon, Talabat, Careem, Deliveroo), Shopify, listings & promo mechanics, "
        "Meta & Google Ads, CRM"
    ),
    "skills_tools": (
        "Excel (Advanced), PowerPoint (Advanced), Power BI, Nielsen, SAP, Salesforce, Generative AI (Claude)"
    ),
}


def make_job() -> Job:
    return Job(
        id="nch-now-foods-brand-manager-gcc-2026-09",
        title=TITLE,
        company="NCH (NOW Foods GCC)",
        location="Dubai, United Arab Emirates",
        url="https://www.nowfoods.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Brand Manager NOW Foods nutraceuticals GCC",
             "brand": "NOW Foods (nutraceuticals / dietary supplements)",
             "function": "Brand Management / Commercial",
             "scope": "GCC markets"},
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
        "ai_score": 52,
        "ai_tier": "Stretch",
        "skills_match": [
            "Brand strategy + annual plan ownership (DoFreeze, GCC + 50 mercados export)",
            "Gobierno de presupuesto A&P y trade, ROI, variances con Finance",
            "Distribución y desarrollo de canal: modern trade, distribuidores, e-commerce y quick-commerce UAE",
            "NPD end-to-end (6 lanzamientos) + relanzamientos y phase-outs",
            "Forecasting y demand planning con Supply Chain; stock lento y near-expiry",
            "Gestión de equipo (designer + social media executive) y coaching",
            "Accountability comercial y negociación (Miravia, 42 cuentas, +30% GMV QoQ)",
            "Canal contra objetivos de P&L reportando a CEO (Miravia Flash Sales)",
            "Gestión de principals internacionales y partners regionales",
            "Categoría better-for-you / nutrición (Befit) — el ángulo wellness más real que tiene",
        ],
        "missing_skills": [
            "8+ años pedidos vs ~5 reales — gap de seniority explícito",
            "Licenciatura en Farmacia o Nutrición + MBA — tiene BBA (CUNEF), sin MBA ni titulación sanitaria",
            "Nutracéuticos / suplementos / consumer healthcare — sin experiencia en la categoría",
            "Canal farmacia y tender / institutional business — no lo ha trabajado",
            "Medical detailing, field force y CRM de fuerza de ventas médica — no lo ha hecho",
            "Regulatory de healthcare y compliance sanitario — sin exposición",
            "Ownership de un P&L de marca completo — ha trabajado contra objetivos de P&L de canal y presupuesto A&P, no es lo mismo",
        ],
        "sector_fit": "stretch (nutracéuticos / consumer healthcare; lo más cercano de Paula es FMCG de alimentación better-for-you con Befit)",
        "seniority_fit": "por debajo (5 años vs 8+ pedidos; además pide MBA)",
        "red_flags": [
            "Requisitos duros de titulación (Pharmacy/Nutrition + MBA) que Paula no cumple — riesgo alto de filtro ATS",
            "Medio JD (medical detailing, field force, tender, regulatory sanitario) es territorio nuevo",
            "Rol con accountability directa de P&L de marca; su experiencia de P&L es de canal, no de marca",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Candidatura de stretch generada a petición de Guille. El JD es un rol de Brand Manager senior de "
            "nutracéuticos en NCH para NOW Foods en GCC, con P&L de marca, canal farmacia, tender business y "
            "medical detailing. La mitad comercial-de-marca encaja bien y es lo que vertebra el CV: estrategia "
            "de marca y plan anual, gobierno de presupuesto A&P y trade con ROI y variances, estrategia de "
            "distribución y desarrollo de canal, NPD end-to-end con relanzamientos y phase-outs, forecasting "
            "con supply chain e inventario (near-expiry, slow-moving), gestión de equipo y de principals "
            "internacionales. El gancho de categoría es Befit, la marca better-for-you de DoFreeze que sí "
            "lidera — real, no inventado. Los gaps son grandes y se dejan escritos: 5 años vs 8+, sin Farmacia/"
            "Nutrición ni MBA, sin experiencia en suplementos, sin canal farmacia, sin tender, sin medical "
            "detailing ni field force, sin regulatory sanitario. P&L: se dice 'canal contra objetivos de P&L' "
            "(Miravia) y 'presupuesto A&P y trade' (DoFreeze), nunca 'owned brand P&L'. Forecast de DoFreeze: "
            "se enuncia como 'feed brand-level forecasting con Supply Chain', no como ownership. Árabe no se "
            "menciona (no lo tiene y la oferta no lo pide). Visa: solo 'ya reside en Dubái', nunca 'no necesita "
            "sponsorship'."
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
