"""One-off: generate Paula's CV + cover letter for SELECTED RECRUITMENT
"Social Media Marketing Manager" (Marketing & Social Media Manager) — a premium
UK F&B brand launching in Dubai. Dubai, UAE. AED 20,000–25,000 + quarterly
commission. On-site, full-time. LinkedIn Easy Apply, posted by a recruiter.

Honest fit: STRONG. This is one of the closest matches to Paula's real profile —
much closer than the recent B2B stretches. The role owns UAE launch marketing for
a food brand: social-first (Instagram/TikTok), influencer & food-creator
partnerships, hands-on short-form content, launch campaigns / activations /
product drops, paid social (Meta/TikTok/Google), promotions with Talabat /
Deliveroo / Careem, community engagement, budget ownership and ROI across
footfall, orders, app installs and revenue. Genuine, truthful bridges:

  - F&B / FOOD FMCG is her day job. At DoFreeze she runs Brand & Marketing for
    Befit, Eurocake and Flair — food brands. Not a stretch; it's her sector.
  - SOCIAL MEDIA + CONTENT: she owns Instagram/TikTok content and built the
    influencer/UGC programme from zero (25–50 creators per campaign), including
    food/lifestyle creators, sampling & seeding.
  - QUICK-COMMERCE PROMOTIONS with the EXACT platforms named: Talabat, Deliveroo,
    Careem (+ Noon). Rare, hands-on, directly relevant — she integrates brands
    and runs promo mechanics on these apps today.
  - LAUNCH CAMPAIGNS / PRODUCT DROPS: leads NPD end-to-end (6 launches) — brief,
    packaging, pricing, go-to-market — i.e. brand launches and drops.
  - PAID SOCIAL: Meta Ads (Facebook & Instagram) and Google Ads, audience
    building, creative A/B testing, tracked on ROI/ROAS. (TikTok Ads adjacent —
    she runs TikTok organically + Meta paid; positioned truthfully.)
  - COMMERCIAL / ROI mindset: P&L exposure, +30% GMV QoQ across 42 accounts,
    budget ownership, KPI reporting.
  - UAE F&B + social landscape: she is Dubai-based, in food FMCG, on the ground.
  - Restaurant/F&B account credibility earlier: Glovo XL accounts were KFC, Taco
    Bell, La Tagliatella, Sushi Shop (restaurants), and Mondelez chocolate
    category (food FMCG).

Truthful gaps — positioned as adjacent, NEVER invented:
  - HANDS-ON VIDEO SHOOTING/EDITING: JD wants a "genuine hands-on content
    creator, not someone who only briefs agencies." Paula produces social content
    hands-on (Canva, short-form, UGC direction with creators) — positioned as
    hands-on social content, NOT as a claim of pro-grade video editing tenure.
  - TikTok PAID ADS specifically: she runs TikTok organically and Meta/Google
    paid — positioned as paid-social fluency that extends to TikTok Ads, not as
    named long TikTok-Ads tenure.
  - UAE DRIVING LICENCE ("essential"): UNKNOWN — NOT asserted anywhere in the CV
    or letter (would be invented otherwise). Flagged to Guille to confirm/add.
  - VISA: already in Dubai on an *employer-sponsored* UAE residence visa. Per the
    standing rule we NEVER claim "no sponsorship needed" — only that she is
    already based in Dubai (zero relocation timeline).

Content authored directly (no LLM API key in this repo) and kept strictly
truthful. Fills the real CV + cover-letter templates, converts to PDF via
LibreOffice (soffice headless — docx2pdf/Word silently fails on this Mac),
registers the job for the dashboard, and lands the package under
output/2026-08-26/.
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

COMPANY = "SELECTED RECRUITMENT"
TITLE = "Social Media Marketing Manager"
DATE_FOLDER = "2026-08-26"

# LinkedIn Easy Apply, promoted by a recruiter; the end client is an undisclosed
# premium UK F&B brand and there is no named hiring manager, so the letter stays
# addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Marketing & Social Media Manager — Premium UK F&B Brand Launch | Dubai.
AED 20,000–25,000 + Quarterly Commission. On-site, full-time. Via SELECTED
RECRUITMENT.

A hugely popular and internationally recognised UK food brand is launching in
Dubai, and we're looking for a hands-on Marketing & Social Media Manager to build
the brand locally from day one. This is a high-ownership role focused on creating
hype pre-launch, driving awareness and footfall once open, and making the brand
impossible to ignore across Dubai.

The Role — you will own:
- UAE launch marketing strategy
- Instagram, TikTok and social media content
- Influencer and food creator partnerships
- Hands-on content creation, including shooting and editing short-form video
- Launch campaigns, activations and product drops
- Paid social across Meta, TikTok and Google
- Promotions with Talabat, Deliveroo and Careem
- Community engagement and brand partnerships
- Marketing budget and campaign performance
- Measuring ROI across footfall, orders, app installs and revenue

What We're Looking For:
- 3+ years' Marketing / Social Media experience
- Ideally from F&B, restaurants, hospitality, food delivery or a strong consumer
  brand
- Strong knowledge of the UAE social and F&B landscape
- Genuine hands-on content creator — not someone who only briefs agencies
- Experience working with influencers and creators
- Commercial mindset with an understanding of budgets, performance and ROI
- Instagram, TikTok and Meta Ads experience
- UAE driving licence essential
- UAE/GCC experience strongly preferred
- Experience launching a new restaurant, venue or consumer brand would be a major
  advantage.

Package: a rare opportunity to help launch one of the UK's most exciting
independent food brands into Dubai and shape its UAE presence from the ground up.
"""

ATS = [
    "Social Media Marketing Manager", "Marketing & Social Media Manager",
    "social media", "social media content", "social media strategy",
    "Instagram", "TikTok", "short-form video", "content creation",
    "hands-on content creator", "UGC", "user generated content",
    "influencer marketing", "influencer partnerships", "food creators",
    "creator partnerships", "launch marketing", "go-to-market",
    "launch campaign", "brand launch", "activations", "product drops",
    "pre-launch hype", "brand awareness", "footfall",
    "paid social", "Meta Ads", "Facebook Ads", "Instagram Ads", "TikTok Ads",
    "Google Ads", "performance marketing", "quick-commerce",
    "Talabat", "Deliveroo", "Careem", "Noon", "food delivery",
    "promotions", "community engagement", "brand partnerships",
    "marketing budget", "budget ownership", "campaign performance",
    "ROI", "ROAS", "orders", "app installs", "revenue",
    "F&B", "food and beverage", "FMCG", "consumer brand", "hospitality",
    "restaurants", "UAE", "Dubai", "GCC", "MENA",
]

CV_CONTENT = {
    "headline": (
        "Social Media & Brand Marketing · F&B / FMCG · Influencer & Creator Partnerships · "
        "Instagram / TikTok Content · Meta & Google Paid Social · Quick-Commerce (Talabat, Deliveroo, Careem)"
    ),
    "professional_summary": (
        "Social-first Brand & Marketing Manager with 4+ years across F&B / FMCG, Beauty and E-Commerce, "
        "currently running brand and social marketing for a Dubai food business (Befit, Eurocake, Flair). "
        "Owns Instagram and TikTok content end-to-end, built an influencer and creator programme from zero "
        "(25–50 creators per campaign) and runs promotions on Talabat, Deliveroo, Careem and Noon — the exact "
        "quick-commerce platforms this launch relies on. Leads product launches and drops (6 NPDs end-to-end), "
        "plans paid social on Meta and Google, and tracks every campaign on ROI/ROAS across orders and revenue. "
        "Commercial track record: +30% GMV QoQ across 42 key accounts. Early adopter of generative AI for "
        "content and campaign planning. Already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Food FMCG brand owner | Brands: Befit, Eurocake, Flair | Dubai-based, 50+ markets",
            "bullets": [
                "Own Instagram and TikTok content end-to-end for food brands — planning, hands-on short-form content, community engagement and always-on social calendars to build awareness and hype",
                "Built and scaled the influencer and food-creator programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign, plus product sampling and seeding — driving UGC, reach and measurable sell-out",
                "Run promotions and campaign mechanics on the UAE's quick-commerce apps — Talabat, Deliveroo, Careem and Noon — from onboarding and listings to promo drops that convert social buzz into orders",
                "Lead product launches and drops end-to-end (6 NPDs: brief, packaging, pricing, go-to-market), building pre-launch hype and activations that drive trial and awareness",
                "Plan and optimise paid social on Meta Ads (Facebook & Instagram) and Google Ads — audience building, creative A/B testing and EDM — tracking ROI/ROAS to grow orders and revenue",
                "Built an AI-powered content and campaign engine (Claude / generative AI) automating social content, campaign planning and KPI reporting — cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Created and led the Beauty Club and 'Hot on Social' projects — social-led content and community programmes that boosted brand visibility, engagement and loyalty",
                "Managed 42 key accounts, delivering +30% GMV growth QoQ through targeted promotions, assortment and pricing strategy",
                "Owned the Flash Sales channel for Beauty, Fashion & Home (reporting directly to the CEO), executing commercial plans and product drops aligned with P&L targets",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise campaign performance and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce / food-delivery leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic F&B and restaurant accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) on a food-delivery platform, driving order volume through bespoke marketing activations and promotions",
                "Helped build Glovo's Retail vertical — onboarding brand partners and running campaigns that grew GMV via data-led planning",
                "Partnered cross-functionally with marketing, logistics and operations to deliver seamless campaigns and increase orders",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global food FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, turning data into commercial recommendations",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf — early hands-on exposure to food brand launches",
            ],
        },
    ],
    "skills_brand": (
        "social media marketing (Instagram, TikTok), social content & short-form, influencer & creator "
        "partnerships, UGC, sampling & seeding, launch marketing & product drops, brand activations, "
        "community engagement, go-to-market, generative AI content"
    ),
    "skills_ecommerce": (
        "paid social — Meta Ads (Facebook & Instagram), Google Ads, TikTok, quick-commerce (Talabat, "
        "Deliveroo, Careem, Noon), promo mechanics, Shopify & e-store management, conversion rate "
        "optimisation (CRO), EDM, marketing automation"
    ),
    "skills_commercial": (
        "marketing budget ownership, campaign performance, key account management, promotions & pricing, "
        "assortment planning, negotiation, brand partnerships"
    ),
    "skills_data": (
        "ROI / ROAS, orders, app installs & revenue tracking, KPI reporting, P&L management, "
        "sell-in/sell-out, AI-assisted analysis, Power BI, Nielsen"
    ),
    "skills_tools": (
        "Meta Ads Manager, Meta Business Suite, Google Ads, TikTok, Instagram, Canva, Shopify, "
        "Generative AI (Claude, ChatGPT), Salesforce, Power BI, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Launching a much-loved UK food brand in Dubai — building pre-launch hype, driving footfall from day "
        "one and making it impossible to ignore across the city — is exactly the kind of work I do every week, "
        "just for food brands already in my portfolio. The Social Media & Marketing Manager role caught my eye "
        "because it asks for the precise mix I bring: social-first content on Instagram and TikTok, an "
        "influencer and food-creator engine, launch campaigns and product drops, paid social, and promotions "
        "on Talabat, Deliveroo and Careem — all measured on ROI. I'm Dubai-based and live in the UAE F&B and "
        "social landscape today."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze, I run brand and social marketing for food brands (Befit, "
        "Eurocake, Flair). I own Instagram and TikTok content end-to-end, and I built the influencer and "
        "food-creator programme from zero — briefing, negotiating and managing 25–50 creators per campaign "
        "plus sampling and seeding to turn social buzz into orders. Crucially for this launch, I run "
        "promotions and campaign mechanics directly on Talabat, Deliveroo, Careem and Noon — the exact "
        "quick-commerce apps a Dubai food launch lives or dies on — and I lead product launches and drops "
        "end-to-end. My paid social sits on Meta and Google, always tracked on ROI/ROAS across orders and "
        "revenue, and earlier I owned 42 key accounts at Alibaba's Miravia with +30% GMV QoQ, so the "
        "commercial and budget side is second nature."
    ),
    "body_paragraph_2": (
        "I'm a genuinely hands-on marketer, not someone who only briefs agencies: I plan and produce social "
        "content myself, direct creators and shoot short-form for the feed, and I've built an AI-powered "
        "content and campaign engine (Claude/GPT) that lets me ship more, faster. My food credentials run "
        "deep — food FMCG at DoFreeze and Mondelez, and restaurant accounts (KFC, Taco Bell, La Tagliatella, "
        "Sushi Shop) on Glovo's food-delivery platform — so I understand both the brand-building and the "
        "delivery-app growth this role needs. I'm already in Dubai on a UAE residence visa, so I can start "
        "immediately and hit the pre-launch runway without any relocation timeline."
    ),
    "closing_paragraph": (
        "I'd love to help take one of the UK's most exciting food brands from launch-day hype to a permanent "
        "fixture in Dubai's F&B scene. I'm available to start immediately and would welcome the chance to walk "
        "through how I'd approach the pre-launch social plan, the creator roster and the Talabat/Deliveroo/"
        "Careem promo calendar. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="selected-recruitment-social-media-marketing-manager-fnb-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Social Media Marketing Manager",
             "end_client": "Undisclosed premium UK F&B brand launching in Dubai",
             "recruiter": "SELECTED RECRUITMENT",
             "function": "Social Media / Brand / Launch Marketing (B2C, F&B)",
             "salary_raw": "AED 20,000–25,000 + quarterly commission",
             "industry": "Food & Beverage / Hospitality / Consumer brand"},
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
        "salary_raw": "AED 20,000–25,000 + quarterly commission",
        "salary_aed_min": 20000,
        "salary_aed_max": 25000,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 84,
        "ai_tier": "Hot",
        "skills_match": [
            "F&B / food FMCG is her sector (DoFreeze: Befit, Eurocake, Flair)",
            "Social media content — owns Instagram & TikTok end-to-end",
            "Influencer & food-creator programme built from zero (25–50 creators/campaign) + UGC, sampling/seeding",
            "Quick-commerce promotions on the EXACT apps named — Talabat, Deliveroo, Careem (+ Noon)",
            "Launch campaigns / product drops — leads NPD end-to-end (6 launches)",
            "Paid social on Meta Ads (FB & IG) + Google Ads, tracked on ROI/ROAS",
            "Commercial / budget & ROI mindset (+30% GMV QoQ, 42 accounts, P&L)",
            "Restaurant/F&B account credibility (Glovo: KFC, Taco Bell, La Tagliatella, Sushi Shop; Mondelez chocolate)",
            "Dubai-based, in UAE F&B + social landscape — UAE/GCC experience",
            "AI-powered content & campaign engine (Claude/GPT) — ships more, faster",
        ],
        "missing_skills": [
            "Hands-on pro video shooting/editing — produces social content hands-on (Canva, short-form, UGC direction), positioned as such, not claimed as pro-editor tenure",
            "TikTok PAID Ads specifically — runs TikTok organically + Meta/Google paid (paid-social fluency extends to TikTok Ads)",
            "UAE driving licence ('essential') — UNKNOWN, not asserted; Guille to confirm/add",
            "Launching a restaurant/venue specifically — has consumer/food brand launches (NPD) + delivery-app growth (adjacent)",
        ],
        "sector_fit": "strong (F&B / food FMCG + social + quick-commerce is her core)",
        "seniority_fit": "on band (4+ yrs vs. 3+; brand/marketing manager)",
        "red_flags": [
            "JD lists 'UAE driving licence essential' — status unknown; not asserted in CV/CL. Confirm before applying; add a line if she holds one.",
            "'Genuine hands-on content creator, not someone who only briefs agencies' — Paula produces social content hands-on but is not positioned as a pro video editor; truthful framing.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit — one of the closest matches to Paula's real profile, not a stretch. The role owns "
            "UAE launch marketing for a premium UK food brand: social-first (Instagram/TikTok), influencer & "
            "food-creator partnerships, hands-on short-form content, launch campaigns/activations/product "
            "drops, paid social (Meta/TikTok/Google), promotions on Talabat/Deliveroo/Careem, community "
            "engagement, budget ownership and ROI across footfall/orders/app installs/revenue. Paula does "
            "almost exactly this today at DoFreeze for food brands (Befit, Eurocake, Flair): owns IG/TikTok "
            "content, built the influencer/creator + UGC programme from zero (25–50 creators), runs promo "
            "mechanics on the exact quick-commerce apps named, leads NPD launches/drops, and plans Meta/Google "
            "paid social on ROI/ROAS. Commercial track record (+30% GMV QoQ, 42 accounts, P&L) covers the "
            "budget/ROI ask; Glovo restaurant accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) and "
            "Mondelez chocolate add food/hospitality credibility; she is Dubai-based in the UAE F&B landscape. "
            "Honest gaps positioned truthfully, never invented: pro-grade video shooting/editing (she is "
            "hands-on with social content and creator direction, not claimed as a pro editor), TikTok PAID Ads "
            "specifically (organic TikTok + Meta/Google paid), launching a restaurant/venue specifically "
            "(consumer/food-brand launches + delivery-app growth are adjacent), and the 'essential' UAE "
            "driving licence (status unknown — deliberately not asserted; flagged to Guille). No 'no "
            "sponsorship needed' claim — she is on an employer-sponsored UAE residence visa."
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
