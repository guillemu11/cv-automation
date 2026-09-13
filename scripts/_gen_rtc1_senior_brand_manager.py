"""One-off: generate Paula's CV for RTC1 Recruitment Services
"Senior Brand Manager" (Dubai, UAE — on-site). Client (undisclosed on the post):
a leading technology-enabled, on-demand HOME SERVICES company.

Strong, ON-BAND fit (not a stretch):
  - Qualification bar is "minimum 5 years of marketing experience within GCC
    startups, FMCG, e-commerce, or high-growth consumer internet brands" — Paula
    is ~5+ years and hits multiple of those buckets directly: Glovo (high-growth
    consumer internet / quick-commerce), Miravia (Alibaba marketplace / e-commerce),
    DoFreeze (FMCG in the GCC) and Mondelez (FMCG).
  - The JD is a digital-first, data-driven BRAND + GROWTH role: own growth &
    marketing strategy for assigned categories and drive category performance;
    use consumer insights/data/trends to build plans and find growth; improve
    customer journey, conversion, onboarding and repeat usage via testing &
    optimization; lead brand campaigns and agency partnerships across digital,
    CRM, influencer and offline. All of that maps cleanly onto Paula's real work.

Honest positioning (NO fabrication):
  - No invented "home services / on-demand" sector tenure — she has consumer
    internet (Glovo), marketplace/e-commerce (Miravia) and FMCG (DoFreeze,
    Mondelez), which the JD explicitly accepts. Sector adjacency stated, not faked.
  - Real, evidenced work only: influencer programme 0 -> 25-50 creators, Shopify
    CRO / A-B testing, CRM/EDM lifecycle & retention, +30% GMV QoQ, category
    expansion, NPD launches, agency/creator partnerships.
  - Visa: already in Dubai on a UAE residence visa; per standing rule, NO "no
    sponsorship needed" claim.

APPLICATION FORMAT (IMPORTANT): the client asks for the CV in WORD format, emailed
to MKTGJOBS2020@gmail.com with subject "Senior Brand Manager". So this script
KEEPS the .docx (the deliverable she emails) and ALSO produces a .pdf preview —
it does NOT delete the docx after conversion.

Lands the package under output/2026-08-29/ and registers the job for the dashboard.
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

COMPANY = "RTC1 Recruitment Services"
TITLE = "Senior Brand Manager"
DATE_FOLDER = "2026-08-29"

JOB_DESCRIPTION = """\
Senior Brand Manager — RTC1 Recruitment Services, Dubai, UAE (on-site, full-time).
Salary depending on experience; benefits per UAE labour law, annual air ticket &
Employee Stock Option Plan. Client: a leading technology-enabled home services
company offering on-demand household services.

Job Description:
- Own growth and marketing strategy for assigned service categories and drive
  overall category performance.
- Use consumer insights, data and market trends to develop effective marketing
  plans and identify new growth opportunities.
- Improve the customer journey, conversion, onboarding and repeat usage through
  testing, analysis and continuous optimization.
- Lead brand campaigns and agency partnerships across digital, CRM, influencer and
  offline channels, ensuring strong brand visibility and consistency.

Qualifications:
- Minimum 5 years of marketing experience within GCC startups, FMCG, e-commerce or
  high-growth consumer internet brands.
- Strong understanding of digital-first brand building, paired with data-driven
  analytical skills for decision-making.
- Excellent creative judgment and multi-campaign project management skills.
- Cross-functional influence with a hands-on, bias-for-action mindset.
"""

ATS = [
    "Senior Brand Manager", "brand manager", "brand strategy", "growth strategy",
    "marketing strategy", "category performance", "assigned categories",
    "consumer insights", "data-driven", "market trends", "marketing plans",
    "growth opportunities", "customer journey", "conversion", "onboarding",
    "repeat usage", "retention", "testing", "A/B testing", "optimization",
    "brand campaigns", "agency partnerships", "digital", "CRM", "influencer",
    "offline", "brand visibility", "brand consistency", "digital-first brand building",
    "analytical", "creative judgment", "multi-campaign", "project management",
    "cross-functional", "bias for action", "hands-on", "GCC", "startups", "FMCG",
    "e-commerce", "consumer internet", "high-growth", "UGC", "performance marketing",
    "Meta Ads", "Google Ads", "GMV", "ROI", "ROAS", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Senior Brand Manager · Digital-First Brand Building · Category Growth & Performance · "
        "CRM, Influencer & Performance Marketing · Consumer Internet / FMCG / E-Commerce"
    ),
    "professional_summary": (
        "Digital-first, data-driven brand and growth marketer with 5+ years across high-growth consumer "
        "internet, marketplaces and FMCG — Glovo, Alibaba's Miravia, DoFreeze and Mondelez. Currently own brand "
        "and growth strategy for a multi-brand portfolio at DoFreeze across 50+ countries, building "
        "consumer-insight- and data-led marketing plans, driving category performance and identifying new "
        "growth opportunities. I improve the customer journey, conversion, onboarding and repeat usage through "
        "testing and continuous optimization, and lead brand campaigns and agency/creator partnerships across "
        "digital, CRM, influencer and offline channels. Proven results: +30% GMV growth QoQ across 42 accounts, "
        "an influencer programme scaled from zero to 25–50 creators per campaign, and generative-AI automation "
        "cutting workload ~40%. Hands-on, bias-for-action, fluent English, already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own brand and growth strategy for the portfolio and its categories across 50+ markets — turning consumer insights, data and market trends into marketing plans and identifying new growth opportunities and white spaces",
                "Lead brand campaigns and agency/creator partnerships across digital, CRM, influencer and offline channels, ensuring strong, consistent brand visibility across markets",
                "Built and scaled the influencer programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign (incl. paid collaborations), plus sampling and seeding — driving awareness, UGC and measurable repeat purchase",
                "Improve customer journey and conversion on the Shopify e-store through A/B testing, analysis and continuous optimization (CRO), and drive onboarding and repeat usage via CRM/EDM lifecycle campaigns",
                "Run multi-campaign delivery hands-on — 6 NPD launches end-to-end plus paid media on Meta and Google Ads — and built AI-powered automation (Claude/GPT) that scales planning, reporting and content, cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Owned category growth across 42 beauty, fragrance and fashion accounts, driving +30% GMV growth QoQ (ahead of category) through consumer-insight- and data-led assortment, pricing and promotion",
                "Led category expansion as PIC Fragrances, launching 30+ partner brands in two months by reading market trends and spotting growth opportunities",
                "Continuously analysed conversion, traffic and retention to improve the customer journey and repeat purchase, sharpening channel performance and forecasting",
                "Created and led the Beauty Club and Hot on Social brand projects — digital-first brand building that boosted visibility, engagement and customer loyalty",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "High-growth consumer-internet / quick-commerce | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew strategic accounts and helped build Glovo's Retail vertical at a high-growth consumer-internet platform — data-led planning and bespoke brand activations",
                "Led cross-functional campaigns across marketing, operations and support to grow order volume and repeat usage",
                "Negotiated and closed high-impact commercial deals with a hands-on, bias-for-action approach",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran category analysis for chocolate — sell-in/sell-out and promotional-effectiveness reporting — turning data into insights that fed brand and category plans",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": (
        "digital-first brand building, brand & growth strategy, category growth & performance, brand campaigns "
        "(digital, CRM, influencer, offline), influencer & UGC programmes, go-to-market & NPD, creative "
        "direction, multi-campaign project management, A&P budget management"
    ),
    "skills_ecommerce": (
        "customer journey & conversion (CRO, A/B testing), onboarding & repeat usage, lifecycle/retention, CRM "
        "& EDM, quick-commerce & marketplaces (Noon, Talabat, Careem, Deliveroo), Shopify, Meta & Google Ads, "
        "marketing automation"
    ),
    "skills_commercial": (
        "category management, consumer insights & market trends, growth-opportunity identification, agency & "
        "creator partnerships, stakeholder management & cross-functional influence, negotiation, pricing & "
        "promotion strategy"
    ),
    "skills_data": (
        "data-driven decision-making, consumer & market insights, funnel & conversion analysis, "
        "retention/repeat-purchase analysis, ROI/ROAS, GMV, Nielsen, Power BI, A/B testing, business reviews, "
        "AI-assisted analysis"
    ),
    "skills_tools": (
        "Meta Ads Manager, Google Ads, Shopify, Generative AI (Claude, ChatGPT), Power BI, Tableau, Looker, "
        "Nielsen, Salesforce, Canva, Adobe Creative Suite, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="rtc1-senior-brand-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs (RTC1 Recruitment Services)",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Senior Brand Manager Dubai RTC1",
             "function": "Brand / Growth Marketing",
             "client": "Undisclosed — technology-enabled on-demand home services company",
             "apply_via": "Email CV in WORD format to MKTGJOBS2020@gmail.com, subject 'Senior Brand Manager'",
             "benefits": "UAE labour law + annual air ticket + Employee Stock Option Plan",
             "recruiter": "Kyla Mae M. (RTC1)"},
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
        "salary_raw": "Depending on experience (+ UAE labour-law benefits, annual air ticket, ESOP)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 85,
        "ai_tier": "Hot",
        "skills_match": [
            "On-band: ~5+ yrs vs 'minimum 5 years' asked",
            "Sector buckets hit directly: consumer internet (Glovo), e-commerce/marketplace (Miravia), FMCG (DoFreeze, Mondelez), GCC (Dubai)",
            "Own growth & marketing strategy for categories + drive category performance (Miravia PIC Fragrances, DoFreeze portfolio, Mondelez category planning)",
            "Consumer insights, data & market trends → marketing plans & growth opportunities",
            "Customer journey, conversion, onboarding & repeat usage via testing/optimization (Shopify CRO, A/B, CRM/EDM, retention)",
            "Brand campaigns + agency/creator partnerships across digital, CRM, influencer & offline",
            "Influencer programme 0 -> 25-50 creators (incl. paid), UGC",
            "Digital-first brand building + data-driven analytics",
            "Multi-campaign project management; hands-on, bias-for-action",
            "+30% GMV QoQ; generative-AI automation (-40% workload)",
            "Already in Dubai (UAE residence visa)",
        ],
        "missing_skills": [
            "On-demand home-services sector specifically — has consumer internet / marketplace / FMCG, which the JD explicitly accepts (adjacent, not identical)",
            "Pure 'startup' tenure — companies are high-growth/large-scale rather than early startups (JD allows FMCG/e-commerce/consumer internet too)",
        ],
        "sector_fit": "strong (consumer internet / e-commerce / FMCG — all named-acceptable; home-services adjacent)",
        "seniority_fit": "on-band (Senior Brand Manager; ~5+ yrs vs minimum 5)",
        "red_flags": [
            "Undisclosed client via recruitment agency (RTC1) — role/company details limited until screening",
            "On-site in Dubai (not remote/hybrid) — fine given she's Dubai-based",
            "Salary 'depending on experience' — undisclosed band",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, on-band fit and one of the cleaner brand roles in the pipeline. The client is a "
            "technology-enabled on-demand home-services company and the role is a digital-first, data-driven "
            "Senior Brand Manager: own growth & marketing strategy for assigned categories and drive category "
            "performance; use consumer insights/data/trends to build plans and find growth; improve customer "
            "journey, conversion, onboarding and repeat usage via testing & optimization; and lead brand "
            "campaigns and agency partnerships across digital, CRM, influencer and offline. All map onto Paula's "
            "real work — category growth (+30% GMV QoQ at Miravia; PIC Fragrances expansion; Mondelez category "
            "planning), CRO/A-B testing and CRM/EDM lifecycle & retention, an influencer programme scaled 0->25-50 "
            "creators, omnichannel brand campaigns and agency/creator partnerships, and generative-AI "
            "automation. Crucially the qualification bar (min 5 yrs within GCC startups / FMCG / e-commerce / "
            "high-growth consumer internet) is hit on multiple fronts: Glovo (consumer internet), Miravia "
            "(marketplace/e-commerce), DoFreeze & Mondelez (FMCG), all GCC-relevant now. Only real softness is "
            "the exact home-services sector (adjacent via consumer internet/marketplace, which the JD accepts) "
            "and 'startup' tenure. Apply by emailing the CV in WORD format to MKTGJOBS2020@gmail.com with "
            "subject 'Senior Brand Manager'. No 'no sponsorship needed' claim."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_keep_docx(docx_path: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice but KEEP the .docx (Word is the deliverable)."""
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    pdf_path = docx_path.with_suffix(".pdf")
    if Path(soffice).exists():
        try:
            subprocess.run(
                [soffice, "--headless", "--convert-to", "pdf", "--outdir",
                 str(docx_path.parent), str(docx_path)],
                check=True, capture_output=True, timeout=180,
            )
        except Exception as exc:  # noqa: BLE001
            print("soffice conversion failed (docx still available):", exc)
    return pdf_path


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

    cv_docx = cv._fill_template(CV_CONTENT, job)   # Word deliverable (kept)
    cv_pdf = _to_pdf_keep_docx(cv_docx)            # PDF preview (docx kept)
    print("OK_CV_DOCX", cv_docx)
    print("OK_CV_PDF", cv_pdf if cv_pdf.exists() else "(pdf preview skipped)")

    pos_dir = cv_docx.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
