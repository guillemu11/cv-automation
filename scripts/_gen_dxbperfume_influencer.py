"""One-off: generate Paula's CV tailored to the DXB Perfume
"Influencer & Creator Marketing Executive" role (Dubai, UAE).

DXB Perfume is a UAE fragrance retailer/brand. The role manages creator
partnerships end-to-end across markets — sourcing, outreach, negotiation,
gifting/PR, campaign management, affiliate & TikTok Shop / social commerce,
performance & ROI, and reporting. Crucially the JD repeats that this is
"not simply an influencer outreach role": every creator partnership must have a
clear objective, appropriate cost, expected deliverables and measurable outcome
— it wants a *commercially minded* operator who negotiates hard and protects the
marketing budget.

That commercial angle is Paula's genuine differentiator: she pairs a real
influencer programme built from zero (25–50 creators/campaign, sampling &
seeding, UGC, measurable sell-out) with a commercial/key-account/P&L background
(Miravia +30% GMV QoQ across 42 accounts; Glovo deal-making; Mondelez category
planning). And unusually for this brief, she has fragrance depth: as PIC
Fragrances at Alibaba's Miravia she onboarded the leading Arabian & oud houses
(Arabian Oud, Lattafa, Swiss Arabian, Ajmal). Already in Dubai on a residence
visa with a live UAE creator network.

Content is authored directly (no LLM API call) and kept strictly truthful —
NO invented experience (no fabricated TikTok Shop / affiliate-platform tenure;
those are framed honestly as adjacent/social-commerce strengths).

Fills the real CV template, converts to PDF via LibreOffice headless (keeping
the editable DOCX), and lands the package under
output/2026-08-16/DXB Perfume - Influencer & Creator Marketing Executive/.

Mirrors the pattern established in scripts/_gen_noon_influencer.py.
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
from career_ops.generators._paths import job_output_dir

COMPANY = "DXB Perfume"
TITLE = "Influencer & Creator Marketing Executive"
DATE_FOLDER = "2026-08-16"

JOB_DESCRIPTION = """\
Influencer & Creator Marketing Executive — DXB Perfume, Dubai, UAE.

DXB Perfume is looking for a highly organised, commercially minded and proactive
Influencer & Creator Marketing Executive to manage creator partnerships across
our markets. This role is responsible for identifying relevant creators, managing
outreach, negotiating partnerships, coordinating gifting and campaigns, tracking
deliverables and measuring performance. This is not simply an influencer outreach
role — every creator partnership should have a clear objective, appropriate cost,
expected deliverables and measurable outcome.

Key responsibilities:
- Creator research & sourcing: research and identify relevant influencers/creators;
  build and maintain an active creator database; assess creators on audience
  quality, engagement, content quality, relevance and commercial potential;
  identify emerging creators; monitor competitor influencer activity.
- Outreach & relationship management: conduct outreach; manage day-to-day creator
  communications; negotiate rates and deliverables; coordinate contracts; build
  long-term partnerships rather than one-off campaigns.
- Campaign management: develop creator recommendations for campaigns and product
  launches; prepare proposals, budgets and estimated costs; create creator briefs;
  coordinate product gifting and PR packages; manage timelines and deadlines;
  track all agreed deliverables; coordinate creator participation in events,
  launches and retail activations.
- Affiliate & social commerce: identify creators for affiliate partnerships;
  support TikTok Shop and other creator commerce initiatives; track affiliate
  performance; recommend increased investment in high performers.
- Performance & ROI: track influencer expenditure; monitor delivered vs agreed;
  track reach, engagement, traffic and sales; calculate cost per creator and cost
  per content piece; track creator-generated revenue; measure campaign ROI;
  reallocate budget.
- Reporting: maintain the influencer database and campaign tracker; produce weekly
  activity and monthly performance reports; highlight top and underperforming
  creators; provide clear recommendations, not just numbers.

Skills & experience:
- Essential: 3+ years in influencer/creator marketing, social media or digital
  marketing; strong understanding of TikTok and Instagram; experience communicating
  with creators; strong organisational and follow-up skills; good negotiation;
  strong Excel/Google Sheets; commercial awareness; excellent written/verbal
  communication.
- Desirable: beauty/fragrance/fashion/lifestyle/retail experience; TikTok Shop;
  affiliate marketing; influencer management platforms; managing paid creator
  campaigns; existing creator network in the UAE.

KPIs: influencer-generated revenue, campaign ROI, cost per creator, cost per content
piece, creator engagement, content delivery rate, affiliate revenue, number of
active high-performing creators, creator retention, budget efficiency.
"""

ATS = [
    "influencer marketing", "creator marketing", "creator partnerships",
    "creator sourcing", "creator database", "audience quality", "engagement",
    "content quality", "commercial potential", "emerging creators",
    "competitor activity", "outreach", "relationship management", "negotiation",
    "rates and deliverables", "contracts", "long-term partnerships",
    "campaign management", "product launches", "proposals", "budgets",
    "estimated costs", "creator briefs", "gifting", "PR packages", "timelines",
    "deliverables", "events", "launches", "retail activations",
    "affiliate marketing", "affiliate partnerships", "TikTok Shop",
    "social commerce", "creator commerce", "performance", "ROI", "reach",
    "traffic", "sales", "cost per creator", "cost per content piece",
    "creator-generated revenue", "budget efficiency", "reporting",
    "campaign tracker", "weekly reports", "monthly reports", "TikTok",
    "Instagram", "Excel", "Google Sheets", "commercial awareness", "beauty",
    "fragrance", "perfume", "fashion", "lifestyle", "retail", "UAE creator network",
]

# --------------------------------------------------------------------------
# CV content
# --------------------------------------------------------------------------
CV_CONTENT = {
    "headline": (
        "Influencer & Creator Marketing · Beauty & Fragrance · "
        "Affiliate & Social Commerce · Commercially-Minded, ROI-Led"
    ),
    "professional_summary": (
        "Influencer and creator marketer with 4+ years driving creator-led growth across Beauty, "
        "Fragrance and FMCG — currently in Dubai with a live UAE creator network. I built DoFreeze's "
        "influencer programme from zero: end-to-end ownership of creator sourcing, database-building, "
        "outreach, rate negotiation, briefing, gifting/seeding, deliverable tracking and reporting, "
        "running 25–50 creators per campaign to drive UGC and measurable sell-out. Unusually for this "
        "space I'm genuinely commercially minded — a key-account and P&L background (Alibaba's Miravia: "
        "+30% GMV QoQ across 42 beauty, fragrance & fashion accounts) means I treat every partnership as "
        "an investment with a clear objective, cost, deliverable and measured outcome, and I negotiate "
        "hard to protect budget. Fragrance-native (onboarded Arabian Oud, Lattafa, Swiss Arabian & Ajmal "
        "as PIC Fragrances), fluent in TikTok/Instagram and social commerce, and data-driven on reach, "
        "engagement, cost-per-creator and ROI. Already based in Dubai on a residence visa; bilingual "
        "Spanish/English (C1)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Built and own the influencer & creator programme end-to-end — researching and sourcing relevant creators, building and maintaining an active creator database, and assessing each on audience quality, engagement, content quality, relevance and commercial potential rather than follower count alone",
                "Run creator outreach and day-to-day communications, negotiate rates and deliverables, coordinate agreements and manage 25–50 creators per campaign — building repeat, long-term relationships with high performers instead of one-off collaborations",
                "Develop creator recommendations for campaigns and product launches, write creator briefs, prepare campaign budgets and estimated costs, and coordinate product gifting and seeding/PR packages across modern trade and quick-commerce",
                "Manage creator timelines and deadlines and track every agreed deliverable — following up to ensure content is delivered correctly and on brief — while turning creator content into measurable on-platform sell-out (Shopify, Noon, Talabat, Careem, Deliveroo) and creator commerce",
                "Track influencer expenditure and calculate cost per creator and cost per content piece; monitor reach, engagement, traffic and sales; and recommend where budget should be increased, reduced or reallocated to protect and stretch the marketing budget",
                "Report performance with clear recommendations — maintaining the campaign tracker and using an AI (Claude/GPT) reporting system that cuts manual workload ~40% — and plan/optimise paid creator and social campaigns on Meta (Instagram/Facebook) and Google Ads against ROI and ROAS",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Led the Fragrances category as PIC — sourcing, negotiating and onboarding 30+ brands in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — deep, directly-relevant perfume-category depth",
                "Created and led the Hot on Social and Beauty Club projects — creator- and content-led destinations that boosted engagement, loyalty and brand visibility and positioned Miravia as a beauty & lifestyle destination",
                "Managed 42 beauty, fragrance & fashion accounts to +30% GMV growth QoQ through pricing, assortment and targeted, trend-driven promotions — the commercial ownership this role demands (objective, cost, deliverable, measured outcome)",
                "Continuously analysed ROI, ROAS, conversion, traffic, retention and engagement to evaluate campaign and partner effectiveness, optimise investment and improve forecasting accuracy",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing commercial plans aligned with P&L targets",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Negotiated and closed high-impact commercial partnerships — managing rates, terms and deliverables to maximise profitability for both platform and partners",
                "Built partnerships onboarding fashion and lifestyle brands as Glovo expanded its marketplace beyond food, driving customer acquisition, order volume and category growth",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), delivering bespoke marketing activations and promotions on time and on budget",
                "Led cross-functional teams across marketing, logistics and CX to deliver seamless, high-impact campaigns and activations",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Analysed promotional effectiveness and sell-in/sell-out for the chocolate category, building performance reports and surfacing growth opportunities — a rigorous, data-first commercial grounding",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": (
        "influencer & creator marketing (mega/macro/micro/nano), creator sourcing & database-building, "
        "creator assessment (audience quality, engagement, relevance, commercial potential), creator "
        "briefs, gifting & seeding / PR packages, event & launch activations, UGC & content, long-term "
        "creator partnerships, campaign & budget planning, generative-AI campaigns"
    ),
    "skills_ecommerce": (
        "TikTok, Instagram, social-first content, social commerce & creator commerce, affiliate-style "
        "creator sell-out, Meta Ads (Instagram/Facebook), Google Ads, Shopify e-store, quick-commerce "
        "(Noon, Talabat, Careem, Deliveroo), marketing automation"
    ),
    "skills_commercial": (
        "rate & deliverable negotiation, contract management, commercial awareness & budget protection, "
        "cost-per-creator / cost-per-content management, key account management, relationship & "
        "stakeholder management, brand onboarding, competitor monitoring"
    ),
    "skills_data": (
        "campaign performance & ROI, cost per creator & cost per content piece, creator-generated "
        "revenue & affiliate tracking, reach & engagement, KPI dashboards & campaign trackers, weekly & "
        "monthly reporting with recommendations, Excel / Google Sheets (advanced), AI-assisted analysis, "
        "Looker, Power BI"
    ),
    "skills_tools": (
        "Excel / Google Sheets (advanced), Meta Business Suite, Meta Ads Manager, Instagram, TikTok, "
        "Google Ads, Shopify, Canva, Generative AI (Claude, ChatGPT), Power BI, Looker, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="dxbperfume-influencer-creator-marketing-executive-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Influencer & Creator Marketing Executive DXB Perfume",
             "via": "LinkedIn"},
    )


def _convert_pdf(docx_path: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice headless (reliable, non-interactive).

    Keeps the editable DOCX alongside the PDF. docx2pdf/Word silently fails on
    this Mac, so soffice headless is the supported path.
    """
    pdf_path = docx_path.with_suffix(".pdf")
    soffice = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    binary = soffice if Path(soffice).exists() else "soffice"
    try:
        subprocess.run(
            [binary, "--headless", "--convert-to", "pdf", "--outdir",
             str(docx_path.parent), str(docx_path)],
            check=True, capture_output=True, timeout=120,
        )
    except Exception as exc:  # noqa: BLE001
        print("WARN pdf conversion failed:", type(exc).__name__, exc)
    return pdf_path


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
        "ai_score": 90,
        "ai_tier": "Hot",
        "skills_match": [
            "Influencer/creator programme built end-to-end from zero (DoFreeze)",
            "Creator sourcing + database, briefs, gifting/seeding, deliverable tracking",
            "Rate & deliverable negotiation; budget protection",
            "Commercially minded: KAM + P&L (Miravia +30% GMV QoQ, 42 accounts)",
            "Fragrance depth: onboarded Arabian Oud, Lattafa, Swiss Arabian, Ajmal",
            "Cost-per-creator / cost-per-content / ROI tracking & reporting",
            "TikTok/Instagram + social commerce; creator content → measurable sell-out",
            "Live UAE creator network; already in Dubai (residence visa)",
            "3+ yrs exp (has 4+); advanced Excel/Sheets",
        ],
        "missing_skills": [
            "TikTok Shop (desirable) — social-commerce adjacent, not a named platform tenure",
            "Dedicated affiliate/influencer-management platforms (desirable, not essential)",
            "Arabic (advantage, not required)",
        ],
        "sector_fit": "excellent (beauty & fragrance / perfume retail — exact category)",
        "seniority_fit": "on-band (3+ yrs asked; Paula 4+) — clean fit",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, clean fit. The JD wants 3+ yrs in influencer/creator marketing with end-to-end "
            "ownership — sourcing, database, outreach, negotiation, briefs, gifting, deliverable tracking, "
            "affiliate/social commerce, ROI and weekly/monthly reporting — and, emphatically, a "
            "COMMERCIALLY MINDED operator (clear objective, cost, deliverable, measured outcome; negotiate "
            "hard; protect budget). Paula built DoFreeze's influencer programme from zero (25-50 creators/"
            "campaign, sampling & seeding, UGC, measurable sell-out) AND brings a rare commercial spine "
            "(Miravia KAM +30% GMV QoQ across 42 accounts, P&L to CEO; Glovo deal-making; Mondelez category "
            "planning) — exactly the 'not just outreach' profile they describe. Bonus: direct fragrance "
            "depth (PIC Fragrances, onboarded Arabian Oud/Lattafa/Swiss Arabian/Ajmal), a live UAE creator "
            "network, Dubai residence visa and advanced Excel/Sheets. Desirables she lacks (named TikTok "
            "Shop tenure, dedicated affiliate/influencer platforms, Arabic) are explicitly optional and "
            "covered adjacently by her social-commerce sell-out and analytics."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


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
    print("STEP registered in dashboard")

    cv_docx = cv._fill_template(CV_CONTENT, job)
    print("STEP CV docx built:", cv_docx.name)

    cv_pdf = _convert_pdf(cv_docx)
    print("STEP CV pdf built:", cv_pdf.name)

    pos_dir = job_output_dir(job)  # output/<Company> - <Role>/
    final_dir = _relocate_to_dated_folder(pos_dir)

    cvd = final_dir / "01_CV_y_Carta" / cv_docx.name
    cvp = final_dir / "01_CV_y_Carta" / cv_pdf.name
    print("OK_CV_DOCX", cvd.name, "(exists)" if cvd.exists() else "(MISSING)")
    print("OK_CV_PDF", cvp.name, "(exists)" if cvp.exists() else "(MISSING)")
    print("FINAL_DIR", final_dir)


if __name__ == "__main__":
    main()
