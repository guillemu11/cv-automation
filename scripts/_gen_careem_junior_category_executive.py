"""One-off: generate Paula's CV + cover letter for Careem
"Junior Category Executive" — Careem Groceries (Q-commerce), Dubai. LinkedIn job 5038636561.

Why this is a real (if unusually junior) fit:
  - The role IS category analytics: turn large volumes of category/supplier/customer
    data into insights, automate recurring reports, build self-serve dashboards, and
    package it into creative decks for supplier performance reviews and senior
    management. That is the exact shape of Paula's Mondelez Category Planning work
    (sell-in/sell-out, promo effectiveness, recurring performance reports for the
    chocolate category) and her Miravia analytics (assortment/pricing/promo analysis
    across 42 accounts, +30% GMV QoQ, performance decks reporting to the CEO).
  - Killer differentiator: it sits inside Careem GROCERIES / Q-commerce, and Paula has
    genuine, hands-on Q-commerce experience — she has integrated brands into Careem,
    Noon, Talabat and Deliveroo (onboarding, listings, promo mechanics, retail
    execution) and worked quick-commerce at Glovo. Real fluency in the Q-commerce
    business model (ads monetization, margin, promo/rebate mechanics) is hard to fake
    and she has it.
  - She builds dashboards and creative, well-structured decks day-to-day, and has built
    AI-powered reporting automation — mapping directly onto "automate recurring reports"
    and "creative decks for supplier and senior-management meetings". Advanced Excel /
    Google Sheets and BI tools (Power BI, Tableau, Looker) are in her stack.

Honest positioning (NO fabrication):
  - SQL is a MUST-HAVE ("hands-on experience writing SQL queries; run queries on
    Insights or similar BI tools"). Paula does NOT have SQL in her profile. It is NOT
    claimed anywhere in the CV skills or ATS list. Her real analytics stack (advanced
    Excel/Sheets, Power BI, Tableau, Looker) is surfaced instead, and the cover letter
    names SQL plainly as a fast-ramp area on top of that BI foundation. Flagged in
    missing_skills / red_flags.
  - Seniority mismatch the OTHER way: this is a "Junior" role (1-2 years) and Paula is a
    Manager with ~5 years. Real overqualification risk; the CV does not hide her titles.
    Flagged. The letter frames genuine interest in Careem's category/Q-commerce craft
    rather than pretending she is junior.
  - Salary not posted; a junior role likely sits below her 20k AED/month floor. Flagged;
    no salary claimed.
  - Per standing rule, NO "no sponsorship needed" claim. Visa is not surfaced; "already
    based in Dubai" is stated only as a factual availability match.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice (soffice
headless — docx2pdf/Word silently fails on this Mac), registers the job for the
dashboard, and lands the package under output/2026-08-19/.
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

COMPANY = "Careem"
TITLE = "Junior Category Executive"
DATE_FOLDER = "2026-08-19"

# Posting is "promoted by a recruiter, responses managed off LinkedIn" — no named
# hiring manager. Letter stays "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Junior Category Executive — Careem (Careem Groceries), Dubai, UAE. Full-time.
LinkedIn job 5038636561.

About the team: The Careem Groceries team is transforming the way people shop for
everyday essentials by offering a fast, reliable, and seamless Q-commerce experience.
Within this fast-paced environment, the Category Management team is responsible for
building the right assortment, pricing, and promotions that delight customers while
driving business growth.

About the role: As a Junior Category Executive, you will be the analytical engine of the
category team — turning large volumes of commercial data into clear insights,
dashboards, and presentations that shape decisions with suppliers and senior management.
This role is ideal for someone highly analytical, comfortable with SQL and data tools,
and eager to build a career in category management within a fast-paced Q-commerce
environment.

What you'll do:
- Analyse large volumes of category, supplier, and customer data to identify trends,
  risks, and opportunities — and translate them into clear insights and actionable next
  steps.
- Write and maintain queries on Insights and in SQL to extract, validate, and manipulate
  data for category and commercial analysis.
- Automate recurring data reports and build dashboards to enable day-on-day monitoring of
  sales, pricing, margins, and stock availability.
- Design easy-to-use, self-serve dashboards that allow the category team and stakeholders
  to track performance without manual effort.
- Create creative, well-structured decks and presentations — both ad-hoc and on a regular
  cadence — for external supplier performance reviews and senior management meetings,
  showcasing analytics in a comprehensive and understandable way.
- Support commercial analysis across key Q-commerce levers, including ads monetization,
  margin analysis, and rebate structures.
- Track performance of the category — including sales, pricing, promotions, and
  availability — and proactively flag risks or opportunities to the Category Manager.
- Support the preparation of periodic business reviews with key suppliers, including data
  packs, performance summaries, and recommendations.
- Collaborate with category, supply chain, and content teams to ensure data-driven
  decision-making across assortment, pricing, and promotions.

What you'll need:
- 1-2 years of experience in an analytical, commercial, or category role, preferably
  within retail, quick commerce, or e-commerce.
- Strong analytical skills with a proven ability to analyse large volumes of data and
  distil them into clear insights and recommended steps forward.
- Hands-on experience writing SQL queries; ability to build and run queries on Insights
  (or similar BI/reporting tools).
- Experience automating reports and building dashboards for day-on-day performance
  analysis; ability to create easy-to-use, intuitive dashboards for non-technical
  stakeholders.
- Strong storytelling and presentation skills — able to build creative, polished decks
  for supplier performance meetings and senior management, on both an ad-hoc and regular
  basis.
- Solid understanding of the Q-commerce business model, including ads monetization,
  margin analysis, and rebate structures.
- Advanced proficiency in Excel or Google Sheets; familiarity with data visualization and
  reporting tools is a strong plus.
- Strong understanding of commercial KPIs and category performance metrics.
- Detail-oriented with solid organizational and time management abilities.
- A proactive attitude, willingness to learn, and the ability to work in a dynamic,
  fast-paced environment.
"""

ATS = [
    "Junior Category Executive", "Category Executive", "category management",
    "category analysis", "commercial analysis", "Q-commerce", "quick commerce",
    "quick-commerce", "e-commerce", "retail", "Careem", "Careem Groceries",
    "groceries", "assortment", "pricing", "promotions", "margin", "margin analysis",
    "rebate structures", "ads monetization", "retail media", "stock availability",
    "large volumes of data", "data analysis", "insights", "actionable next steps",
    "trends", "risks", "opportunities", "dashboards", "self-serve dashboards",
    "automate reports", "recurring reports", "day-on-day monitoring", "reporting",
    "performance tracking", "commercial KPIs", "category performance metrics",
    "sell-in", "sell-out", "sell-in/sell-out", "promotional effectiveness",
    "forecasting", "supplier performance reviews", "business reviews", "data packs",
    "performance summaries", "recommendations", "storytelling", "presentations",
    "decks", "senior management", "creative decks", "Excel", "Google Sheets",
    "advanced Excel", "data visualization", "Power BI", "Tableau", "Looker",
    "Nielsen", "detail-oriented", "organized", "proactive", "fast-paced", "GCC",
    "MENA", "UAE", "Dubai", "cross-functional", "supply chain", "data-driven",
]

CV_CONTENT = {
    "headline": (
        "Category & Commercial Analytics · Q-Commerce (Careem · Noon · Talabat · Deliveroo) · "
        "Assortment · Pricing · Promotions · Dashboards & KPI Reporting · Supplier Business Reviews"
    ),
    "professional_summary": (
        "Analytical category and commercial professional with 5 years across FMCG, Beauty and "
        "E-Commerce, and genuine hands-on Q-commerce experience — I have integrated brands into "
        "Careem, Noon, Talabat and Deliveroo (onboarding, listings, promo mechanics, retail "
        "execution) and worked quick-commerce at Glovo. My core is turning large volumes of "
        "category, supplier and customer data into clear insights, dashboards and decks: at "
        "Mondelez I owned sell-in/sell-out and promotional-effectiveness reporting for the "
        "chocolate category; at Alibaba's Miravia I analysed pricing, assortment, promotions, ROI "
        "and conversion across 42 accounts to grow GMV +30% QoQ and presented performance decks up "
        "to CEO level. I track the commercial levers this role lives on — sales, pricing, margin, "
        "promotions and availability — and understand the Q-commerce model (ads monetization, "
        "margin, promo/rebate mechanics). Advanced in Excel/Google Sheets with BI tooling (Power "
        "BI, Tableau, Looker), an early adopter of generative AI (Claude/GPT) that I use to "
        "automate recurring reporting and build stakeholder-ready dashboards and presentations. "
        "Detail-obsessed, proactive, fluent in English and already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Integrated brands into key UAE quick-commerce platforms — Careem, Noon, Talabat and Deliveroo — managing onboarding, product listings, assortment, promotional mechanics and retail execution, and tracking sales, pricing, promotions and availability day-on-day across the Q-commerce channel",
                "Turn large volumes of category and commercial data into clear insights and recommendations — analysing sales, pricing, margin and promo performance to flag risks and opportunities and shape assortment, pricing and promotion decisions",
                "Built AI-powered reporting automation (Claude/GPT) that automates recurring KPI reports and produces self-serve dashboards and creative, well-structured decks for management — cutting manual reporting workload ~40%",
                "Develop trade & shopper marketing and promotion plans by channel and manage A&P budgets, supporting category strategy and supplier/partner reviews across 50+ markets",
                "Own the brand's Shopify store end-to-end with data-led merchandising — assortment, pricing, promotions and CRO — lifting conversion and average order value",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Analysed large volumes of commercial data across 42 accounts — pricing, assortment, promotions, ROI, ROAS, conversion, traffic and retention — distilling them into clear insights and next steps that grew GMV +30% QoQ",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months through data-led assortment, trend-driven products and targeted promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO — building performance summaries, data packs and creative decks that translated analytics into commercial decisions",
                "Ran continuous pricing, assortment and promotion analysis to optimise channel performance, margin and forecasting accuracy, flagging risks and opportunities proactively",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Worked the quick-commerce model hands-on — managing strategic accounts, assortment and promotions to drive order volume and GMV through data-led joint planning",
                "Part of the team that built Glovo's Retail vertical — onboarding fashion and lifestyle brands with tailored assortment and promotion plans beyond food delivery",
                "Negotiated and closed commercial deals, tracking performance and margin to maximise profitability for both Glovo and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Owned sell-in/sell-out analysis and promotional-effectiveness reporting for the chocolate category, building recurring performance reports in advanced Excel that fed periodic business reviews",
                "Turned category and customer data into clear insights, trends and recommendations — identifying growth opportunities and supporting NPD launches (Milka Spread, Mini Suchard)",
                "Tracked category KPIs (sales, pricing, promotions, distribution) and packaged the analysis into structured, detail-accurate decks for stakeholders",
            ],
        },
    ],
    "skills_data": (
        "large-volume category & commercial data analysis, insights & recommendations, "
        "sell-in/sell-out, promotional-effectiveness analysis, KPI tracking (sales, pricing, "
        "margin, promotions, availability), recurring-report automation, dashboards & self-serve "
        "reporting, advanced Excel & Google Sheets, Power BI, Tableau, Looker, Nielsen, "
        "forecasting, AI-assisted analysis"
    ),
    "skills_commercial": (
        "category management, assortment planning, pricing strategy, margin analysis, "
        "promotions & mechanics, rebate & commercial-deal structures, supplier & business reviews, "
        "data packs & performance summaries, key account management, negotiation, forecasting"
    ),
    "skills_brand": (
        "storytelling & creative decks for supplier and senior-management reviews, "
        "performance presentations (ad-hoc & recurring), trade & shopper marketing, "
        "promotion planning, go-to-market, generative-AI reporting automation"
    ),
    "skills_ecommerce": (
        "Q-commerce (Careem, Noon, Talabat, Deliveroo) — onboarding, listings, assortment, "
        "promo mechanics, availability & retail execution; ads monetization / retail media on "
        "marketplaces; Shopify & e-store management; conversion rate optimisation (CRO)"
    ),
    "skills_tools": (
        "Microsoft Excel & Office (Expert), Google Sheets, Power BI, Tableau, Looker, Nielsen, "
        "Kantar, Salesforce, SAP, Generative AI (Claude, ChatGPT), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Careem Groceries is exactly the kind of fast, data-driven Q-commerce environment I want to "
        "do my best category work in — and it's a world I already know from the inside. As Brand & "
        "Marketing Manager at DoFreeze I integrate brands into Careem, Noon, Talabat and Deliveroo "
        "day-to-day, and I began my career on a category team at Mondelez doing precisely what this "
        "role is built around: turning large volumes of commercial data into insights, reports and "
        "decks that shape assortment, pricing and promotion decisions. The Junior Category Executive "
        "brief reads like a description of the analytical craft I most enjoy."
    ),
    "body_paragraph_1": (
        "The core of this role — being the analytical engine of the category team — is where I'm "
        "strongest. At Mondelez I owned sell-in/sell-out and promotional-effectiveness reporting for "
        "the chocolate category, building the recurring performance reports that fed business "
        "reviews. At Alibaba's Miravia I analysed pricing, assortment, promotions, ROI and "
        "conversion across 42 accounts to grow GMV +30% QoQ, and — running the Flash Sales channel "
        "reporting to the CEO — I packaged that analysis into performance summaries, data packs and "
        "creative decks for senior stakeholders. At DoFreeze I track the exact Q-commerce levers "
        "this job lists — sales, pricing, margin, promotions and availability — and I've built "
        "AI-powered automation that generates recurring reports and self-serve dashboards, so "
        "\"automate the reporting and build the dashboards\" is already how I work."
    ),
    "body_paragraph_2": (
        "Two honest notes, in the spirit of a good hire. First, on tooling: my analytics stack is "
        "advanced Excel and Google Sheets plus BI tools (Power BI, Tableau, Looker), and I build "
        "dashboards and decks in them today; I don't yet write production SQL, but querying is the "
        "natural next step on that foundation and I'd ramp it fast — I pick up data tools quickly "
        "and use generative AI to accelerate exactly that. Second, my recent titles are at Manager "
        "level, but I'm genuinely drawn to Careem's category and Q-commerce craft and to doing the "
        "hands-on analytical work well — I understand the Q-commerce model (ads monetization, "
        "margin, promo and rebate mechanics) and I'm happy rolling up my sleeves on the data. I'm "
        "already based in Dubai and available to start quickly."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd turn category, supplier and customer data into the "
        "insights, dashboards and supplier-review decks that keep a Q-commerce category growing. "
        "Thank you for considering my application — I'd be glad to walk through how I'd approach the "
        "first 90 days on the Careem Groceries category team."
    ),
}


def make_job() -> Job:
    return Job(
        id="careem-junior-category-executive-5038636561",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/view/5038636561",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Junior Category Executive Careem Groceries Dubai",
             "function": "Category Management / Commercial Analytics",
             "team": "Careem Groceries — Category Management",
             "workplace": "On-site, Dubai (4 days office / 1 day home)",
             "linkedin_job_id": "5038636561",
             "note": "Promoted by recruiter, responses managed off LinkedIn. No hiring manager named."},
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
        "salary_raw": "Not posted (Junior band — likely below Paula's 20k AED/month floor)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 62,
        "ai_tier": "Warm",
        "skills_match": [
            "Category analytics is the core: sell-in/sell-out & promo-effectiveness reporting for the chocolate category (Mondelez) — a direct match to 'analytical engine of the category team'",
            "Genuine hands-on Q-commerce: integrates brands into Careem, Noon, Talabat, Deliveroo (DoFreeze) + Glovo quick-commerce — rare and hard to fake",
            "Large-volume commercial data → insights: pricing/assortment/promo/ROI/conversion across 42 accounts, +30% GMV QoQ (Miravia)",
            "Automates recurring reports & builds dashboards; AI-powered reporting automation (DoFreeze)",
            "Storytelling & creative decks for senior management — Flash Sales channel reporting to CEO with data packs & performance decks (Miravia)",
            "Q-commerce model fluency — ads monetization / retail media, margin, promo & rebate mechanics",
            "Advanced Excel & Google Sheets; BI tooling (Power BI, Tableau, Looker), Nielsen",
            "Commercial KPIs & category performance metrics — sales, pricing, margin, promotions, availability",
            "Detail-oriented, proactive, fast-paced; already based in Dubai",
        ],
        "missing_skills": [
            "SQL (must-have: 'hands-on experience writing SQL queries; run queries on Insights') — NOT held; not claimed. Real analytics stack is Excel/Sheets + Power BI/Tableau/Looker; named plainly in the letter as a fast-ramp area",
            "Careem 'Insights' internal BI tool — no direct exposure (adjacent BI tools held)",
            "Overqualified: 'Junior' role (1-2 yrs) vs Paula's ~5 yrs at Manager level — overqualification / retention-risk screen",
            "Salary likely below her 20k AED/month floor for a junior band",
        ],
        "sector_fit": "strong (Q-commerce / e-commerce category management — direct)",
        "seniority_fit": "INVERTED mismatch — role is Junior (1-2 yrs); Paula is a Manager with ~5 yrs. Overqualified, real screen risk",
        "red_flags": [
            "SQL is an explicit must-have and Paula does not have it — hard-filter risk on an analytics-first role; positioned honestly, not fabricated",
            "Overqualification: a Manager applying to a Junior req — common auto-reject ('will leave / too senior / too expensive')",
            "Salary: junior band, not posted, likely under her 20k AED/month floor",
            "On-site Dubai (4/1) — fine on location, but a step down in scope/autonomy vs her current Manager remit",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Content fit is genuinely strong — the role's spine (analyse large-volume category data → "
            "insights; automate reports & build dashboards; creative decks for supplier & senior-mgmt "
            "reviews; track sales/pricing/margin/promo/availability in a Q-commerce environment) maps "
            "almost one-to-one onto Paula's Mondelez category-planning start, her Miravia analytics "
            "(+30% GMV QoQ, decks to CEO) and her live DoFreeze Q-commerce integration across Careem/"
            "Noon/Talabat/Deliveroo. Two real drags keep this Warm rather than Hot: (1) SQL is an "
            "explicit must-have she doesn't hold — surfaced honestly via her BI/Excel stack and named "
            "as a ramp area, never faked; and (2) it's a JUNIOR req and she's a Manager (~5 yrs), so "
            "overqualification and a likely sub-floor salary are the biggest risks, not the skills. "
            "Worth applying only if Paula specifically wants a foot inside Careem / a category-track "
            "role and is comfortable with the level and pay. CV leads with category analytics + "
            "Q-commerce; letter names the SQL gap and the level plainly."
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
