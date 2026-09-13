"""One-off: generate Paula's CV (+ cover letter) for Perfetti Van Melle's
"Senior E-Commerce Executive" — Export Middle East & Africa, Dubai.

Source: Perfetti Van Melle careers (SuccessFactors) — Dubai, AE. Posted Aug 23, 2026.
Company: Perfetti Van Melle (confectionery FMCG — Mentos, Chupa Chups, Fruittella,
Alpenliebe, Airheads, Smint). Export Middle East & Africa BU.

Honest context (IMPORTANT):
  - VERY STRONG, honest fit — arguably one of Paula's best matches to date.
    The JD wants: drive & optimise ecommerce performance across priority markets;
    grow sales by nurturing e-retail relationships and finding new e-retail
    opportunities; annual budget plans; quarterly assortment assessments to
    optimise product mix; monthly rolling forecasts jointly with country managers
    and distributors; customer business plans with joint KPIs; SKU availability &
    service levels >85%; identify new ecommerce growth areas from market trends &
    consumer insights; optimise the customer digital journey / conversion / brand
    presence on e-retailer platforms; an e-retailer platform strategy. Candidate
    profile: 2+ years in quickCommerce or FMCG e-commerce, sales AND marketing,
    working with leading ecommerce platforms & digital marketplaces (preferably
    UAE / Middle East), strong analytical skills, Business Administration degree.
  - Paula matches essentially all of it from REAL experience:
      • DoFreeze (Dubai): integrated FMCG brands into UAE quick-commerce (Noon,
        Careem, Talabat, Deliveroo) — listings, promo mechanics, retail execution;
        distributor networks; Shopify e-store CRO & customer digital journey;
        trade/shopper plans across 50+ markets.
      • Miravia / Alibaba: 42 e-commerce key accounts, +30% GMV QoQ via pricing,
        assortment optimisation & targeted promotions; owned Flash Sales channel
        with P&L; onboarded 30+ new stores; ROI/ROAS/conversion/retention analysis.
      • Glovo: quick-commerce XL-account manager — data-led planning, GMV growth.
      • Mondelez: FMCG confectionery (chocolate category) sell-in/sell-out &
        promo-effectiveness analysis — direct confectionery adjacency to Perfetti.
      • CUNEF Business Administration, E-Commerce specialisation.
  - Seniority: JD asks for "at least 2 years" and titles it "Executive". Paula is
    4+ years at manager level — she EXCEEDS the minimum. No inflation needed; CV
    keeps her real titles. The role is a strong function/sector fit, not a stretch.
  - Per project rules: NOTHING fabricated (real titles/metrics kept). NO "own visa
    / no sponsorship" claim anywhere — the CV visa field ("UAE Residence Visa") is
    factual and stays; the letter asserts nothing about sponsorship (her residence
    visa is employer-sponsored).

Application channel: Perfetti Van Melle careers portal (SuccessFactors),
recruiter-managed, no named contact → CONTACT = None, letter to "Hiring Manager".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word fails on this Mac), registers the job for the
dashboard, and lands the package under output/2026-08-23/.
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
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "Perfetti Van Melle"
TITLE = "Senior E-Commerce Executive"
DATE_FOLDER = "2026-08-23"
JOB_URL = "https://careers.perfettivanmelle.com/"

CONTACT = None  # Careers portal (SuccessFactors), no named contact → "Hiring Manager".

JOB_DESCRIPTION = """\
Senior E-Commerce Executive — Perfetti Van Melle Export Middle East & Africa.
Dubai, UAE. Full-time. Confectionery FMCG.

Take ownership of driving and optimising ecommerce performance across assigned
priority markets. Manage sales growth by nurturing existing e-retail relationships
and identifying new opportunities within the digital retail landscape. Close
collaboration with internal teams (E-commerce, Marketing, Country Management) and
external stakeholders (distributors, key e-retail partners).

Key responsibilities:
- Lead and execute the ecommerce strategy to meet and exceed budgeted sales
  targets, aligned with overall PVM ecommerce goals.
- Develop annual budget plans with cross-functional teams; review progress via
  quarterly assortment assessments with e-retailers to optimise product mix.
- Maintain accurate, timely monthly rolling forecasts jointly with country
  managers and distributors to align inventory and sales.
- Create comprehensive customer business plans with joint KPIs and targets,
  fostering mutually beneficial partnerships with e-retailers.
- Ensure consistent SKU availability and high service levels across all customers,
  targeting service levels above 85%.
- Identify and capitalise on new ecommerce growth areas, leveraging market trends
  and consumer insights to expand the digital footprint.
- Implement and enhance the customer digital journey using data-driven insights to
  optimise engagement, sales conversion and brand presence on e-retailer platforms.
- Develop and execute a comprehensive e-retailer platform strategy.

Ideal candidate:
- Bachelor's degree in Business Administration, Sales, or a related field.
- At least two years within quickCommerce or FMCG e-commerce, with results across
  sales and marketing roles.
- Demonstrated expertise working with leading ecommerce platforms and digital
  marketplaces, preferably within the UAE or Middle East region.
- Strong analytical skills for interpreting sales data and identifying growth.
- Excellent organisational and time-management abilities; juggling multiple
  projects and deadlines in a fast-paced environment.
- Adapts quickly to changing market dynamics, customer needs and emerging trends.
- Exceptional communication and interpersonal skills across levels and geographies.
- Self-motivated, results-driven, proactive with innovative ideas.
"""

ATS = [
    "e-commerce", "ecommerce strategy", "quickCommerce", "quick-commerce",
    "FMCG e-commerce", "e-retail", "e-retailers", "e-retail partners",
    "digital marketplaces", "ecommerce platforms", "e-retailer platform strategy",
    "sales growth", "budgeted sales targets", "annual budget plans",
    "assortment optimisation", "assortment assessment", "product mix",
    "rolling forecast", "forecasting", "country managers", "distributors",
    "distributor management", "customer business plans", "joint KPIs",
    "SKU availability", "service levels", "digital retail", "customer digital journey",
    "sales conversion", "conversion rate optimisation", "CRO", "brand presence",
    "consumer insights", "market trends", "growth opportunities", "sales data",
    "data-driven", "analytical skills", "Noon", "Talabat", "Careem", "Deliveroo",
    "UAE", "Middle East", "GCC", "MENA", "modern trade", "key account management",
    "GMV", "ROI", "ROAS", "P&L", "pricing strategy", "promotions", "Shopify",
    "confectionery", "FMCG", "stakeholder management", "cross-functional",
    "Business Administration",
]

CV_CONTENT = {
    "headline": (
        "Senior E-Commerce Executive · FMCG & Quick-Commerce · E-Retail Key Account "
        "Management · Noon / Talabat / Careem / Deliveroo · Assortment, Forecasting & "
        "Sales Growth · Distributor Management · Dubai, UAE"
    ),
    "professional_summary": (
        "E-commerce and commercial professional with 4+ years across FMCG, "
        "quick-commerce, beauty and fashion — driving online sales growth on leading "
        "platforms and digital marketplaces. Currently owns e-commerce for DoFreeze "
        "in Dubai, integrating FMCG brands into UAE quick-commerce (Noon, Talabat, "
        "Careem, Deliveroo) and running the Shopify store end-to-end — listings, "
        "assortment, promo mechanics and the customer digital journey. At Alibaba's "
        "Miravia, grew 42 e-retail accounts +30% GMV QoQ through pricing, assortment "
        "optimisation and targeted promotions, with full P&L ownership of the Flash "
        "Sales channel. Strong analytical, forecasting and stakeholder skills across "
        "distributors and country teams; Business Administration graduate (CUNEF, "
        "E-Commerce specialisation). Already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (E-Commerce & Commercial)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own e-commerce performance across priority markets — integrating FMCG brands into leading UAE quick-commerce platforms and digital marketplaces (Noon, Talabat, Careem, Deliveroo): product listings, assortment, promotional mechanics and retail execution to grow online sales",
                "Run monthly rolling forecasts and assortment reviews jointly with distributors and country teams to align inventory and sell-out, protecting SKU availability and service levels across customers",
                "Own and optimise the brand's Shopify e-store end-to-end (catalogue, UX, collections, discounts, checkout), lifting conversion (CRO) and average order value by improving the customer digital journey with data-led merchandising",
                "Build customer business and trade/shopper plans by channel with joint KPIs, supporting key account strategy and category management across GCC, MENA, Asia, Europe, USA and Africa",
                "Identify new e-commerce growth areas from market trends and consumer insights, and plan paid media on Meta and Google Ads — analysing ROI/ROAS and conversion to drive continuous performance improvement",
                "Built an AI-powered automation system (Claude / generative AI) for campaign planning, content, market research and KPI reporting — cutting manual workload ~40% and accelerating go-to-market across 50+ markets",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – E-Commerce (Beauty, Fragrances & Fashion)",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 e-retail key accounts, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions — nurturing existing partnerships and onboarding new ones",
                "Owned the Flash Sales channel (Beauty, Fashion & Home) with full P&L, reporting directly to the CEO and executing commercial plans against budgeted sales targets",
                "Led category expansion as PIC Fragrances, onboarding 30+ new e-retail stores in two months via strategic promotions and trend-driven assortment",
                "Continuously analysed sales data — ROI, ROAS, conversion, traffic and retention — to optimise channel performance, product mix and forecasting accuracy",
                "Created and led the 'Beauty Club' and 'Hot on Social' projects, strengthening brand presence, engagement and customer loyalty on the platform",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts (Quick-Commerce)",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts on a quick-commerce marketplace (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning and bespoke activations",
                "Part of the team building Glovo's retail vertical — onboarding fashion and lifestyle brands and expanding the marketplace beyond food",
                "Negotiated and closed high-impact commercial deals, managing budgets to maximise profitability for partners and platform",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG confectionery leader | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Conducted sell-in/sell-out and promotional-effectiveness analysis for the chocolate/confectionery category, building performance reports and identifying growth opportunities",
                "Contributed to NPD launches (Milka Spread, Mini Suchard), sharpening category, assortment and trade-marketing judgement inside a global FMCG confectionery leader",
            ],
        },
    ],
    "skills_ecommerce": (
        "FMCG e-commerce & quick-commerce (Noon, Talabat, Careem, Deliveroo), leading "
        "marketplaces & e-retail platforms, e-retailer platform strategy, Shopify / "
        "e-store, assortment & product-mix optimisation, customer digital journey, "
        "conversion rate optimisation (CRO), Meta Ads, Google Ads, EDM"
    ),
    "skills_commercial": (
        "e-retail key account management, distributor management, customer business "
        "plans & joint KPIs, sales growth vs budgeted targets, pricing & promotions, "
        "assortment planning, category management, modern trade, negotiation"
    ),
    "skills_data": (
        "sales-data analysis, rolling forecasting, P&L, GMV, ROI, ROAS, conversion & "
        "retention, sell-in/sell-out, SKU availability & service levels, KPI tracking, "
        "Power BI, Nielsen, Kantar, SAP"
    ),
    "skills_brand": (
        "e-commerce growth strategy, go-to-market, shopper & trade marketing, "
        "promotional planning, NPD, influencer & UGC, omnichannel campaigns, "
        "generative-AI content & automation"
    ),
    "skills_tools": (
        "Shopify, Meta Business Suite, Google Ads, SAP, Power BI, Salesforce, "
        "Microsoft Office (Expert), Generative AI (Claude, ChatGPT), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Perfetti Van Melle's Senior E-Commerce Executive role reads like a "
        "description of what I do every day. From Dubai, I own e-commerce for an FMCG "
        "portfolio across priority markets — growing online sales on leading "
        "marketplaces and quick-commerce platforms, nurturing e-retail relationships "
        "and opening new ones. Doing that for a confectionery leader across the Middle "
        "East & Africa is exactly the challenge I'm looking for."
    ),
    "body_paragraph_1": (
        "The brief maps almost point-for-point onto my experience. At DoFreeze I "
        "integrate FMCG brands into the UAE's leading e-retail and quick-commerce "
        "platforms (Noon, Talabat, Careem, Deliveroo) — managing listings, assortment, "
        "promotional mechanics and retail execution — and I run monthly rolling "
        "forecasts and assortment reviews jointly with distributors and country teams "
        "to protect SKU availability and service levels. I own the Shopify store "
        "end-to-end, optimising the customer digital journey and conversion, and I "
        "build customer business plans with joint KPIs by channel. Before Dubai, at "
        "Alibaba's Miravia I grew 42 e-retail accounts +30% GMV quarter-on-quarter "
        "through pricing, assortment optimisation and targeted promotions, owning the "
        "Flash Sales channel P&L against budgeted sales targets."
    ),
    "body_paragraph_2": (
        "What I'd bring to Perfetti Van Melle specifically: rare hands-on fluency with "
        "the exact UAE / Middle East e-retail platforms this role manages; a genuinely "
        "analytical, data-led approach to sales, forecasting and growth opportunities; "
        "and FMCG grounding that includes confectionery itself — I started in category "
        "planning at Mondelez, running sell-in/sell-out and promotional analysis for "
        "the chocolate category. I work naturally across distributors, country managers "
        "and cross-functional teams, I'm already based in Dubai, and I hold a Business "
        "Administration degree with an E-Commerce specialisation."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to discuss how my UAE quick-commerce and e-retail "
        "account experience would translate into growth for Perfetti Van Melle across "
        "the Middle East & Africa. Thank you for considering my application — I look "
        "forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="perfetti-van-melle-senior-ecommerce-executive-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url=JOB_URL,
        source="perfetti_careers",
        description=JOB_DESCRIPTION,
        raw={"query": "Perfetti Van Melle Senior E-Commerce Executive Dubai FMCG",
             "function": "E-commerce commercial / e-retail key account management (FMCG confectionery)",
             "sector": "FMCG — confectionery (Perfetti Van Melle: Mentos, Chupa Chups, Fruittella, Alpenliebe)",
             "note": "VERY STRONG honest fit. JD core — drive/optimise ecommerce across priority "
                     "markets, grow sales via e-retail relationships, annual budget plans, quarterly "
                     "assortment assessments, monthly rolling forecasts with country managers & "
                     "distributors, customer business plans with joint KPIs, SKU availability/service "
                     "levels >85%, new ecommerce growth from market trends & consumer insights, "
                     "customer digital journey / conversion / brand presence on e-retailer platforms, "
                     "e-retailer platform strategy — maps onto Paula's real work (DoFreeze UAE "
                     "quick-commerce integration + Shopify CRO + distributor forecasting; Miravia 42 "
                     "e-retail accounts +30% GMV QoQ + Flash Sales P&L; Glovo quick-commerce KAM; "
                     "Mondelez confectionery category planning). JD asks 2+ years / 'Executive'; "
                     "Paula is 4+ years at manager level — EXCEEDS the minimum. Nothing fabricated; no "
                     "'own visa / no sponsorship' claim (employer-sponsored residence visa)."},
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
        "salary_raw": "Not disclosed (FMCG confectionery band, Dubai; 'Executive' — confirm vs 20k AED floor)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 90,
        "ai_tier": "Excellent",
        "skills_match": [
            "FMCG e-commerce & UAE quick-commerce: integrates brands into Noon, Talabat, Careem, Deliveroo — listings, assortment, promo mechanics, retail execution (DoFreeze, Dubai) — the exact platforms the role manages",
            "E-retail key account management + GMV growth: 42 accounts, +30% GMV QoQ via pricing, assortment optimisation & targeted promotions; Flash Sales channel P&L vs budgeted targets (Miravia/Alibaba)",
            "Forecasting & distributor alignment: rolling forecasts + assortment reviews with distributors and country teams; SKU availability & service-level focus (DoFreeze)",
            "Customer digital journey & conversion: owns Shopify e-store end-to-end, CRO, product mix, data-led merchandising; brand presence on e-retailer platforms",
            "Strong analytical / sales-data skills (ROI, ROAS, conversion, sell-in/sell-out); Business Administration degree, E-Commerce specialisation; confectionery adjacency via Mondelez chocolate category planning; already in Dubai",
        ],
        "missing_skills": [
            "Title is 'Executive' with a 2-year minimum — Paula is 4+ years at manager level (over the bar, not a gap); ensure the comp band still clears her floor",
            "No specific prior confectionery-brand e-commerce ownership (adjacent FMCG confectionery via Mondelez category planning only) — not fabricated",
        ],
        "sector_fit": "FMCG confectionery e-commerce — direct hit; UAE/Middle East e-retail focus matches Paula's Dubai quick-commerce experience exactly",
        "seniority_fit": "at/above band — JD asks 2+ years; Paula is 4+ years at manager level (strong, not a stretch)",
        "red_flags": [
            "Salary not disclosed and titled 'Executive' — confirm the package clears the 20k AED/month floor before investing further (FMCG confectionery 'Executive' bands can sit below her current level).",
            "Slightly more junior title than her current 'Manager' role — framed as depth of e-commerce/e-retail ownership, not a downgrade; worth a quick expectations check.",
            "Nothing fabricated; no 'own visa / no sponsorship' claim (employer-sponsored residence visa).",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Excellent, honest fit for Perfetti Van Melle's Senior E-Commerce Executive (Export "
            "Middle East & Africa, Dubai). The JD's core — driving/optimising e-commerce across "
            "priority markets, growing sales via e-retail relationships, annual budget plans, "
            "quarterly assortment assessments, monthly rolling forecasts with country managers & "
            "distributors, customer business plans with joint KPIs, SKU availability & service levels, "
            "new growth from market trends & consumer insights, customer digital journey / conversion "
            "/ brand presence on e-retailer platforms, and an e-retailer platform strategy — maps "
            "almost point-for-point onto Paula's real experience. She integrates FMCG brands into the "
            "UAE's leading quick-commerce platforms (Noon, Talabat, Careem, Deliveroo) at DoFreeze, "
            "runs distributor/country forecasts, and owns a Shopify store end-to-end; at Alibaba's "
            "Miravia she grew 42 e-retail accounts +30% GMV QoQ with Flash Sales P&L ownership; at "
            "Glovo she managed quick-commerce key accounts; and at Mondelez she did confectionery "
            "category planning (a direct sector adjacency to Perfetti). The only nuances are the "
            "'Executive' title / 2-year minimum (Paula is over the bar at 4+ years) and undisclosed "
            "pay — worth confirming the band clears her floor. Nothing fabricated; real titles/metrics "
            "kept; no 'own visa / no sponsorship' claim. Recommended path: tailored CV+CL → apply via "
            "the Perfetti careers portal → optional LinkedIn note to the Export MEA e-commerce/"
            "commercial lead."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (docx2pdf/Word fails on this Mac)."""
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
    """Move output/<Company> - <Role>/ under output/<DATE_FOLDER>/."""
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

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
