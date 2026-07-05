"""One-off: generate Paula's CV adapted to the Colgate-Palmolive Ecommerce
Manager (Dubai) posting. Content authored directly (no LLM API call needed),
then filled into the real template + converted to PDF, and the job is
registered in scored_jobs.json so it shows up in the dashboard.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Colgate-Palmolive"
TITLE = "Ecommerce Manager"
DATE_FOLDER = "2026-06-11"

JOB_DESCRIPTION = """\
Ecommerce Manager — Colgate-Palmolive, Dubai, UAE (Hybrid). Job #174114.

Key Responsibilities:
- Develop digital commerce strategies with a longer term vision including growth
  ambition, customer prioritization and key business capabilities.
- Build and deepen strategic alignment with customers and cross functional teams
  to elevate growth with deep focus on value creation.
- Ensure continuous improvement in eCapabilities for DAM, Content, Packaging,
  Net Sales, P&L, Analytics reporting.
- Use data and analytics to drive better and bolder decision-making.
- Launch exciting, personalized, differentiated innovation ensuring best in class
  execution.
- Develop rich content that converts providing higher click & conversion rates.
- Define all metrics that matter for digital shelf excellence, review critical
  metrics through a scorecard and recommend corrective actions.
- Leverage digital to drive demand and purchase with a full funnel approach
  focusing on consumer journeys.
- Drive category growth across all sub channels and develop promotion strategy.
- 360 Marketing Communications aligned with consumer marketing across digital
  platforms.
- Estimate and track yearly sales, traffic distribution, marketing spending and
  channel performance for eCommerce retailers.
- Coordinate digital marketing activities with agencies and digital technology
  platforms.
- Work with consumer marketing, retail marketing, key accounts, supply chain and
  customers to drive commercial strategy.

Required Qualification:
- Bachelor's Degree, preferably Economics/Management.
- Minimum 4 years in eCommerce marketing or account management, preferably
  multinational FMCG with leading brands.
- Proficient in English; Microsoft Office / Google Suite.
"""

# ATS keywords drawn from the JD
ATS = [
    "Ecommerce Manager", "digital commerce strategy", "eCommerce retailers",
    "digital shelf", "content that converts", "conversion rate", "full funnel",
    "analytics", "scorecard", "P&L", "Net Sales", "category growth",
    "promotion strategy", "360 marketing", "key accounts", "FMCG",
    "consumer journeys", "data-driven", "agency management",
]

CONTENT = {
    "headline": "E-Commerce Manager · Digital Commerce Strategy · Key Account Management · FMCG",
    "professional_summary": (
        "E-Commerce and Commercial Manager with 4+ years building digital commerce strategy "
        "across FMCG, Beauty and Fashion. Currently leading Brand & E-Commerce for DoFreeze "
        "(Befit, Eurocake, Flair) in Dubai — owning the Shopify store, the UAE quick-commerce "
        "digital shelf (Noon, Talabat, Careem, Deliveroo), content that converts and full-funnel "
        "digital media across 50+ markets. Alibaba-trained at Miravia/AliExpress, managing 42 key "
        "accounts to +30% GMV QoQ via assortment, pricing and promotions. Data-driven operator "
        "fluent in digital-shelf scorecards, ROI/ROAS analytics, P&L and 360 marketing, with strong "
        "agency and cross-functional collaboration. BBA (CUNEF, 9.5/10 thesis, E-Commerce "
        "specialisation) and early adopter of generative AI for content and analytics at scale."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own and optimise the brand's Shopify e-commerce store end-to-end (catalogue, theme & UX, collections, discount mechanics, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising — rich content that converts",
                "Run the UAE quick-commerce digital shelf across e-retailers (Noon, Careem, Talabat, Deliveroo): onboarding, product listings, content and promotional mechanics across modern trade, driving net sales and sell-out",
                "Plan and optimise full-funnel paid media on Meta Ads and Google Ads — audience building, creative A/B testing, social and EDM — analysing ROI/ROAS to drive demand, traffic and purchase across consumer journeys",
                "Built an AI-powered marketing automation system (Claude / generative AI) automating campaign planning, content creation, market research and KPI/scorecard reporting — cutting manual workload ~40% across 50+ markets",
                "Develop trade & shopper marketing and promotion plans by channel, supporting key account strategy and category growth across all sub-channels in 50+ markets",
                "Lead NPD end-to-end for 6 differentiated launches (brief, packaging, pricing, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts across beauty, fragrances and fashion, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing commercial plans aligned with P&L targets",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting accuracy — digital-shelf metrics and scorecard discipline",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via strategic promotions and trend-driven assortment",
                "Created and led the Beauty Club and Hot on Social projects, boosting visibility, loyalty and personalised content on platform",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team that built Glovo's Retail vertical — onboarding fashion and lifestyle brands and expanding the marketplace beyond food into apparel, beauty and non-food e-commerce categories",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) and integration of new partners, driving GMV growth through data-led planning and bespoke activations",
                "Led cross-functional teams across marketing, logistics and customer support to deliver seamless campaigns and increase order volume",
                "Negotiated and closed high-impact commercial deals maximising profitability for both Glovo and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Conducted sell-in/sell-out analysis, evaluated promotional effectiveness and built performance reports for the chocolate category",
                "Identified growth opportunities and contributed to NPD launches including Milka Spread and Mini Suchard",
            ],
        },
    ],
    "skills_brand": "go-to-market, omnichannel campaigns, 360 marketing, shopper marketing, trade marketing, NPD end-to-end, brand strategy, A&P budget management, influencer marketing, generative AI campaigns",
    "skills_ecommerce": "e-store management, Shopify, digital shelf, conversion rate optimisation (CRO), quick-commerce, Noon, Talabat, Careem, Deliveroo, UX optimisation, Meta Ads (Facebook & Instagram Ads), Google Ads, marketing automation, EDM",
    "skills_commercial": "key account management, distributor management, modern trade, pricing strategy, assortment planning, category management, negotiation, forecasting, planogram, general trade",
    "skills_data": "P&L management, KPI tracking & scorecards, ROI, ROAS, sell-in/sell-out, AI-assisted analysis & forecasting, retail execution, Looker, Nielsen, Kantar, Salesforce, SAP",
    "skills_tools": "Shopify, Meta Ads Manager, Google Ads, Microsoft Office (Expert), Looker, Salesforce, SAP, Nielsen, Kantar, Generative AI (Claude, ChatGPT), Canva",
}


def make_job() -> Job:
    return Job(
        id="colgate-ecom-174114",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://jobs.colgate.com/job/Dubai-Ecommerce-Manager-DU/174114-en_US/",
        source="company_site",
        description=JOB_DESCRIPTION,
        raw={"query": "E-Commerce Manager", "via": "Colgate Careers", "job_number": "174114"},
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
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
        "posted_date": "2026-06-11",
        "raw": job.raw,
        "ai_score": 93,
        "ai_tier": "Hot",
        "skills_match": [
            "Digital commerce strategy", "eCommerce retailers", "Digital shelf",
            "Content that converts / CRO", "Full-funnel digital media",
            "Key account management", "Category growth & promotion strategy",
            "Analytics, P&L & scorecards", "360 marketing", "FMCG / multinational",
        ],
        "missing_skills": ["DAM tooling (explicit)"],
        "sector_fit": "exact",
        "seniority_fit": "exact",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Near-perfect fit: Paula runs FMCG e-commerce end-to-end (Shopify + UAE "
            "quick-commerce digital shelf), manages key accounts (42 at Miravia, +30% "
            "GMV QoQ), and is fluent in P&L, ROI/ROAS analytics and full-funnel media — "
            "exactly the Colgate eCommerce Manager remit. 4+ yrs FMCG e-commerce/account "
            "management, English C1, MS Office expert, already in Dubai on a residence visa."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": "2026-06-11T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    job = make_job()
    register_in_dashboard(job)

    # Fill template + convert to PDF using the real generator internals.
    docx_path = cv._fill_template(CONTENT, job)
    pdf_path = cv._to_pdf(docx_path)

    # Honour the día → posición convention: move the position folder under the
    # date folder (the generator writes to output/<Company> - <Role>/).
    pos_dir = pdf_path.parent.parent          # .../<Company> - <Role>
    dated_parent = settings.output_dir / DATE_FOLDER
    dated_parent.mkdir(parents=True, exist_ok=True)
    dest = dated_parent / pos_dir.name
    if pos_dir.resolve() != dest.resolve():
        if dest.exists():
            # merge: move the produced PDF into existing dated folder
            target = dest / pdf_path.parent.name
            target.mkdir(parents=True, exist_ok=True)
            shutil.move(str(pdf_path), str(target / pdf_path.name))
            shutil.rmtree(pos_dir, ignore_errors=True)
            final = target / pdf_path.name
        else:
            shutil.move(str(pos_dir), str(dest))
            final = dest / pdf_path.parent.name / pdf_path.name
    else:
        final = pdf_path

    print("OK_PDF", final)


if __name__ == "__main__":
    main()
