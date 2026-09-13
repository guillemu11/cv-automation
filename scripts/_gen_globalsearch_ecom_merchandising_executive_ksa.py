"""One-off: generate Paula's CV + cover letter for The Global Search Company
"Ecommerce Merchandising Executive KSA" — LinkedIn Easy Apply, recruiter-posted
(advertiser: Steven Grundy, International Recruitment Manager). The end employer is
undisclosed ("our client, a growing international retail business"); the role is
based in Riyadh, Saudi Arabia (LinkedIn header shows UAE / remote).

Why this is a real fit on CONTENT:
  - The role IS online merchandising + digital trading: keep assortment, content,
    pricing and promotions accurate and ready to trade across owned platforms and
    third-party marketplaces; improve discoverability (search terms, taxonomy,
    filters, placement); manage product uploads, content and lifecycle; run
    promotional execution; and produce weekly trading reports with data-led
    recommendations. That is almost exactly Paula's live DoFreeze work — she owns the
    brand's Shopify store end-to-end (catalogue, collections, product presentation,
    discoverability, discounts, CRO, AOV) and has integrated brands into Noon,
    Talabat, Careem and Deliveroo (onboarding, listings, content, promo mechanics,
    availability, retail execution) — plus her Miravia digital-trading work
    (assortment, pricing, promotions, conversion/traffic/retention analysis, +30% GMV
    QoQ) and her Inditex/Massimo Dutti retail-merchandising roots.
  - Requirements are light and she clears them comfortably: 2+ yrs e-commerce / online
    merchandising / digital trading / retail merchandising (she has ~5), strong Excel,
    analytical, attention to detail, English, a bachelor's degree with an e-commerce
    specialisation.

Honest positioning (NO fabrication):
  - Seniority mismatch (inverted): this is an Executive/junior req (2 yrs; ~half of
    applicants entry-level) and Paula is a Manager (~5 yrs). Real overqualification /
    retention-risk screen. The CV does not hide her titles; the letter frames genuine
    interest in the hands-on merchandising & trading craft rather than pretending she
    is junior.
  - Location: JD says the role is BASED IN RIYADH, KSA; the LinkedIn header shows
    "UAE (remote)". Paula is Dubai-based. The letter states she is based in Dubai,
    works across the GCC and is comfortable supporting the KSA-facing digital channels
    — no relocation promise is invented and, per standing rule, NO "no sponsorship
    needed" claim is made anywhere.
  - Salary not posted; an Executive band likely sits below her 20k AED/month floor.
    Flagged in the dashboard record; no salary claimed.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice (soffice
headless — docx2pdf/Word silently fails on this Mac), registers the job for the
dashboard, and lands the package under output/2026-08-20/.
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

COMPANY = "The Global Search Company"
TITLE = "Ecommerce Merchandising Executive KSA"
DATE_FOLDER = "2026-08-20"

# Named advertiser on the LinkedIn post — the recruiter running the search.
CONTACT = "Steven Grundy"

JOB_DESCRIPTION = """\
Ecommerce Merchandising Executive KSA — The Global Search Company (recruiter).
End client: a growing international retail business. This position is based in
Riyadh, Saudi Arabia. Remote / Full-time. LinkedIn Easy Apply.

Our client is a growing international retail business. As the company expands its
presence across regional and international digital channels, they are seeking an
E-commerce Merchandising Executive to support product readiness, online merchandising
and day-to-day trading performance across owned platforms and third-party marketplaces.

The Opportunity: Reporting to the Digital Trading Manager, you will help ensure that
products, content, pricing and promotions are accurate, commercially presented and
ready to trade across all digital channels. The position combines online merchandising,
product management, content updates, promotional execution and performance reporting. It
would suit someone with early e-commerce or retail merchandising experience who is ready
to take greater ownership within a growing digital function.

Key Responsibilities:
- Conduct daily checks across websites and other digital channels to ensure product
  assortments, content, pricing and promotions are accurate.
- Identify trading opportunities by analysing stock availability, conversion performance
  and customer demand.
- Maintain product categorisation, sorting and online presentation in line with the
  company's commercial strategy.
- Support cross-selling and upselling initiatives to improve conversion and the overall
  customer journey.
- Improve product discoverability through effective use of search terms, keywords,
  taxonomy, filters and product placement.
- Ensure products are fully prepared for launch across owned and third-party digital
  channels.
- Coordinate product imagery, descriptions, translations, attributes, pricing and other
  required information.
- Manage timely product uploads and updates in accordance with trading and promotional
  calendars.
- Maintain product lifecycle information, including the removal of discontinued,
  unavailable or outdated products.
- Publish and maintain digital content across homepages, category pages and other areas
  of the website.
- Support the delivery of promotional campaigns by ensuring all relevant products,
  content and digital assets are correctly implemented.
- Analyse website performance, customer behaviour and competitor activity to support
  merchandising decisions.
- Prepare weekly and ad hoc trading reports, highlighting trends, opportunities and
  areas requiring action.
- Present practical, data-led recommendations to improve digital performance and key
  e-commerce metrics.
- Support wider merchandising and digital trading projects, taking ownership of agreed
  actions and deadlines.
- Collaborate with internal teams to ensure product launches, campaigns and digital
  updates are delivered accurately and on time.

About You:
- A bachelor's degree or equivalent qualification.
- At least two years' experience in e-commerce, online merchandising, digital trading or
  retail merchandising.
- Experience managing product information, website content or online product uploads.
- An understanding of digital merchandising and the factors that influence online
  conversion.
- Strong Microsoft Excel skills.
- Good analytical, numerical and problem-solving abilities.
- Excellent attention to detail, particularly when working with product, pricing and
  promotional information.
- Strong planning and time-management skills.
- The ability to manage several priorities and deliver work within agreed deadlines.
- A collaborative working style, together with the confidence to manage individual
  responsibilities independently.
- Professional fluency in written and spoken English.
"""

ATS = [
    "Ecommerce Merchandising Executive", "e-commerce merchandising", "online merchandising",
    "digital merchandising", "digital trading", "retail merchandising", "merchandising",
    "product readiness", "product management", "product information", "product uploads",
    "product content", "content updates", "website content", "product presentation",
    "product categorisation", "sorting", "assortment", "assortment accuracy",
    "pricing", "promotions", "promotional execution", "promotional calendars",
    "trading calendars", "product discoverability", "search terms", "keywords",
    "taxonomy", "filters", "product placement", "cross-selling", "upselling",
    "conversion", "conversion rate", "CRO", "customer journey", "stock availability",
    "customer demand", "trading opportunities", "product lifecycle", "product launch",
    "owned platforms", "third-party marketplaces", "marketplaces", "homepages",
    "category pages", "digital content", "digital assets", "promotional campaigns",
    "website performance", "customer behaviour", "competitor activity", "trading reports",
    "weekly reports", "ad hoc reports", "performance reporting", "data-led recommendations",
    "e-commerce metrics", "Microsoft Excel", "Excel", "analytical", "numerical",
    "problem-solving", "attention to detail", "planning", "time management",
    "multiple priorities", "collaborative", "English", "Noon", "Talabat", "Careem",
    "Deliveroo", "Shopify", "KSA", "Saudi Arabia", "Riyadh", "GCC", "e-commerce",
]

CV_CONTENT = {
    "headline": (
        "E-Commerce Merchandising & Digital Trading · Online Assortment, Pricing & Promotions · "
        "Product Content, Uploads & Discoverability · Conversion (CRO) · Marketplace Operations "
        "(Noon · Talabat · Careem · Deliveroo) · Shopify"
    ),
    "professional_summary": (
        "E-commerce and digital-trading professional with ~5 years across FMCG, Beauty, Fashion "
        "and E-Commerce whose day-to-day is exactly this role: keeping assortment, content, "
        "pricing and promotions accurate, commercially presented and ready to trade across owned "
        "platforms and third-party marketplaces. At DoFreeze I own the brand's Shopify store "
        "end-to-end — catalogue, collections, product presentation and discoverability, product "
        "content, discounts and checkout — lifting conversion (CRO) and average order value, and I "
        "have integrated brands into Noon, Talabat, Careem and Deliveroo (onboarding, listings, "
        "content, promo mechanics, availability and retail execution). At Alibaba's Miravia I ran "
        "digital trading across 42 accounts — assortment, pricing and promotions, analysing "
        "conversion, traffic and retention — to grow GMV +30% QoQ, and my career began on the "
        "Inditex (Massimo Dutti) shop floor with its visual-merchandising and product-presentation "
        "discipline. Strong Microsoft Excel with BI tooling (Power BI, Tableau, Looker), detail-"
        "obsessed with product, pricing and promotional data, fluent in English and based in Dubai, "
        "working across the GCC."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the brand's Shopify store end-to-end — catalogue, categorisation and collections, product presentation and discoverability, content, discounts and checkout — running data-led online merchandising that lifts conversion rate (CRO) and average order value",
                "Manage product readiness across owned and third-party channels: product uploads and updates, imagery, descriptions, attributes and pricing, keeping assortment, content, pricing and promotions accurate and ready to trade, and retiring discontinued or unavailable products",
                "Integrated brands into UAE marketplaces — Noon, Talabat, Careem and Deliveroo — managing onboarding, listings, content, promotional mechanics, availability and retail execution across owned platforms and third-party marketplaces",
                "Improve product discoverability through search terms, keywords, taxonomy, filters and placement, and support cross-sell/upsell to improve conversion and the overall customer journey",
                "Execute promotional campaigns against trading and promotional calendars — implementing the right products, content and digital assets — and publish/maintain digital content across homepages and category pages",
                "Analyse website and channel performance, customer behaviour and competitor activity, and produce weekly and ad-hoc trading reports with practical, data-led recommendations to improve e-commerce metrics",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Ran digital trading across 42 accounts — assortment optimisation, pricing strategy and targeted promotions — growing GMV +30% QoQ, continuously analysing conversion, traffic, retention, ROI and ROAS to spot trading opportunities and flag risks",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months through data-led assortment, trend-driven products and promotional mechanics — keeping product content and presentation accurate and ready to trade",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO — building the trading reports and performance decks that turned merchandising and conversion analysis into commercial decisions",
                "Optimised online presentation and assortment across the catalogue to improve discoverability, conversion and the customer journey on the marketplace",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team that built Glovo's Retail vertical — onboarding fashion and lifestyle brands to the marketplace, setting up listings, assortment and product content beyond food delivery",
                "Managed assortment, pricing and promotional execution for strategic accounts, driving order volume and GMV through data-led joint planning",
                "Tracked trading performance and availability, flagging opportunities and coordinating cross-functional teams (marketing, logistics, support) to keep campaigns and launches accurate and on time",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built weekly and ad-hoc performance reports for the chocolate category in advanced Excel — sell-in/sell-out, promotional effectiveness and KPI tracking — turning data into clear trends, opportunities and recommendations",
                "Analysed pricing, promotions and distribution to support assortment and merchandising decisions, and contributed to NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_ecommerce": (
        "online merchandising, digital trading, product readiness & product management, "
        "assortment & online presentation, product discoverability (search terms, keywords, "
        "taxonomy, filters, placement), product content (imagery, descriptions, attributes, "
        "translations, pricing), product uploads & lifecycle management, marketplace operations "
        "(Noon, Talabat, Careem, Deliveroo — owned & third-party), Shopify & e-store management, "
        "conversion rate optimisation (CRO), cross-sell/upsell, promotional execution"
    ),
    "skills_commercial": (
        "assortment planning, pricing strategy, promotions & promotional mechanics, "
        "category management, trading-opportunity identification (stock availability, conversion, "
        "demand), competitor analysis, key account management, negotiation, forecasting"
    ),
    "skills_data": (
        "website & trading-performance analysis, conversion/traffic/retention analysis, "
        "weekly & ad-hoc trading reports, data-led recommendations, e-commerce & KPI metrics, "
        "advanced Microsoft Excel, Power BI, Tableau, Looker, Nielsen, forecasting, "
        "AI-assisted analysis"
    ),
    "skills_brand": (
        "promotional campaigns & digital-asset implementation, digital content publishing "
        "(homepages & category pages), product launch & go-to-market readiness, visual "
        "merchandising (Inditex-trained), storytelling & trading-report presentations, "
        "generative-AI reporting automation"
    ),
    "skills_tools": (
        "Microsoft Excel & Office (Expert), Shopify, Google Sheets, Power BI, Tableau, Looker, "
        "Nielsen, Meta Ads, Google Ads, Salesforce, SAP, Generative AI (Claude, ChatGPT), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm writing about the E-commerce Merchandising Executive role you're recruiting for your "
        "client's growing international retail business. The brief reads like a description of my "
        "day-to-day: keeping assortment, content, pricing and promotions accurate, commercially "
        "presented and ready to trade across owned platforms and third-party marketplaces. As Brand "
        "& Marketing Manager at DoFreeze I own our Shopify store end-to-end and merchandise brands "
        "across Noon, Talabat, Careem and Deliveroo, so online merchandising and digital trading "
        "are exactly the craft I want to keep doing."
    ),
    "body_paragraph_1": (
        "Mapping directly to the role: I run daily-to-weekly trading on our Shopify store — "
        "categorisation, product presentation and discoverability (search terms, taxonomy, filters, "
        "placement), product uploads and content (imagery, descriptions, attributes, pricing), "
        "promotional execution against trading calendars, and product-lifecycle housekeeping — "
        "lifting conversion (CRO) and average order value. Across Noon, Talabat, Careem and "
        "Deliveroo I've managed listings, content, promo mechanics and availability across owned and "
        "third-party channels. Earlier, at Alibaba's Miravia, I ran digital trading across 42 "
        "accounts — assortment, pricing and promotions — growing GMV +30% QoQ while analysing "
        "conversion, traffic and retention, and I built the weekly trading reports and data-led "
        "recommendations that fed commercial decisions. Strong Excel, attention to detail on "
        "product/pricing/promotional data, and a bachelor's degree with an e-commerce specialisation "
        "round out the essentials."
    ),
    "body_paragraph_2": (
        "One honest note, in the spirit of a good hire: my recent titles are at Manager level, "
        "while this is an Executive role — but I'm genuinely drawn to the hands-on merchandising and "
        "trading work and happy to own it end-to-end; I'm not looking to sit above the detail, I "
        "like being in it. I'm based in Dubai and work across the GCC, so I'm well placed to support "
        "the KSA-facing digital channels, and my career began on the Inditex (Massimo Dutti) shop "
        "floor, where visual-merchandising and product-presentation standards are drilled in — a "
        "foundation I still bring to how I merchandise online."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd keep your client's assortment, content, pricing and "
        "promotions accurate and trading well across every digital channel. Thank you for "
        "considering my application, Steven — I'd be glad to walk through how I'd approach the first "
        "90 days in the role."
    ),
}


def make_job() -> Job:
    return Job(
        id="globalsearch-ecom-merchandising-executive-ksa",
        title=TITLE,
        company=COMPANY,
        location="Riyadh, Saudi Arabia (LinkedIn header: UAE / Remote)",
        url="https://www.linkedin.com/jobs/search/?keywords=Ecommerce%20Merchandising%20Executive%20The%20Global%20Search%20Company",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Ecommerce Merchandising Executive KSA The Global Search Company",
             "function": "E-Commerce Merchandising / Digital Trading",
             "team": "Digital Trading (reports to Digital Trading Manager)",
             "workplace": "Based in Riyadh, KSA; LinkedIn header shows UAE / Remote",
             "recruiter": "Steven Grundy — International Recruitment Manager (advertiser)",
             "end_client": "Undisclosed — a growing international retail business",
             "apply": "LinkedIn Easy Apply (94 applicants at time of capture)",
             "note": "Recruiter-run search; end employer undisclosed. Address letter to Steven Grundy."},
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
        "salary_raw": "Not posted (Executive band — likely below Paula's 20k AED/month floor)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 60,
        "ai_tier": "Warm",
        "skills_match": [
            "Online merchandising + digital trading IS her day-to-day: owns the DoFreeze Shopify store end-to-end (categorisation, presentation, discoverability, content, discounts, CRO, AOV)",
            "Product readiness across owned + third-party marketplaces: uploads, content, promo mechanics, availability on Noon, Talabat, Careem, Deliveroo",
            "Digital trading at Alibaba's Miravia — assortment, pricing, promotions across 42 accounts, +30% GMV QoQ, conversion/traffic/retention analysis",
            "Weekly & ad-hoc trading reports with data-led recommendations (DoFreeze, Miravia, Mondelez)",
            "Strong Microsoft Excel + BI (Power BI, Tableau, Looker); analytical, numerical, detail-obsessed with product/pricing/promo data",
            "Retail-merchandising roots at Inditex / Massimo Dutti (visual merchandising, product presentation)",
            "Bachelor's degree with an e-commerce specialisation; professional English (C1)",
            "Clears the 2+ yrs requirement comfortably (~5 yrs) and is based in Dubai, across the GCC",
        ],
        "missing_skills": [
            "Overqualified: Executive/junior req (2 yrs; ~half of applicants entry-level) vs Paula's ~5 yrs at Manager level — overqualification / retention-risk screen",
            "Location: JD says role is BASED IN RIYADH, KSA (LinkedIn header shows UAE/remote); Paula is Dubai-based — clarify remote-from-Dubai vs relocation; conflicts with her 'remote_ok: false / no relocation' preference",
            "Salary likely below her 20k AED/month floor for an Executive band",
        ],
        "sector_fit": "strong (e-commerce online merchandising / digital trading — direct match)",
        "seniority_fit": "INVERTED mismatch — Executive/junior role (2 yrs); Paula is a Manager with ~5 yrs. Overqualified; real screen risk",
        "red_flags": [
            "Overqualification: a Manager applying to an Executive req — common auto-reject ('too senior / will leave / too expensive')",
            "Location ambiguity: Riyadh-based per JD vs UAE/remote in the LinkedIn header — needs clarifying; against Paula's stated no-remote / no-relocation preference",
            "Salary: Executive band, not posted, likely under her 20k AED/month floor",
            "End employer undisclosed (recruiter-run search) — can't research the actual company/brand",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Content fit is genuinely strong — the role's spine (keep assortment, content, pricing & "
            "promotions accurate and ready to trade across owned + third-party channels; product "
            "uploads, content & discoverability; promotional execution; weekly trading reports with "
            "data-led recommendations; conversion/CRO focus) maps almost one-to-one onto Paula's live "
            "DoFreeze Shopify + marketplace merchandising, her Miravia digital trading (+30% GMV QoQ) "
            "and her Inditex retail-merchandising start. Requirements are light (2+ yrs, strong Excel, "
            "analytical, English, degree) and she clears them easily. The drags are not skills but "
            "level and place: it's an Executive/junior req and she's a Manager (~5 yrs), so "
            "overqualification and a likely sub-floor salary are the real risks; and the JD places the "
            "role in Riyadh while the LinkedIn header shows UAE/remote, which needs clarifying against "
            "her no-remote / no-relocation preference. Worth applying only if Paula specifically wants "
            "a merchandising/trading-track role and is comfortable with the level, pay and location "
            "arrangement. CV leads with e-commerce merchandising + digital trading; letter names the "
            "level and location plainly and makes no sponsorship claim."
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
