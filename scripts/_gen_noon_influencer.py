"""One-off: generate Paula's CV tailored to the noon
"Influencer, Social Media & Strategic Partnerships Specialist" role for
noon Minutes (15-min FMCG/grocery q-commerce, UAE + KSA), Dubai.

Content is authored directly (no LLM API call) and kept strictly truthful —
NO invented experience. This is a STRONG fit and is re-angled to lead with the
genuine matches the JD asks for: an influencer programme Paula built from zero
(25-50 creators/campaign, mega->nano, sampling & seeding, UGC, measurable
sell-out), social-first storytelling projects (Miravia "Hot on Social" /
"Beauty Club"), strategic brand partnerships & onboarding, hands-on UAE
quick-commerce (noon, Talabat, Careem, Deliveroo) and data-driven ROI/ROAS/CAC
optimisation.

Fills the real CV template, converts to PDF via LibreOffice headless (keeping
the editable DOCX), and lands the package under
output/2026-08-12/noon - Influencer, Social Media & Strategic Partnerships Specialist/.

Mirrors the pattern established in scripts/_gen_noon_am.py.
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

COMPANY = "noon"
TITLE = "Influencer, Social Media & Strategic Partnerships Specialist"
DATE_FOLDER = "2026-08-12"

JOB_DESCRIPTION = """\
Influencer, Social Media & Strategic Partnerships Specialist — noon (noon Minutes),
Dubai, UAE. noon Minutes is noon's fastest hyper-local delivery platform, offering
a localized assortment of FMCG & grocery products with 15-minute delivery, live
across the UAE and Saudi Arabia.

Drive creator-led growth, social storytelling and strategic partnerships that
accelerate customer acquisition, strengthen brand relevance and unlock scalable
growth for noon Minutes — sitting at the intersection of marketing, partnerships
and analytics.

What you'll do:
- Own influencer campaigns end-to-end: strategy, creator sourcing, briefing,
  execution, reporting and optimisation.
- Build and manage relationships with creators across mega, macro, micro and nano
  tiers, ensuring authentic, high-performing collaborations.
- Negotiate commercial terms; manage contracts, campaign deliverables, timelines
  and budgets.
- Develop and execute social-first campaigns aligned to product launches,
  promotions and cultural moments.
- Partner with Brand and Content teams to shape social calendars and channel
  strategy across Instagram, TikTok, YouTube, X and Snapchat.
- Identify emerging trends and react quickly with high-impact content and creator
  activations.
- Identify, develop and manage strategic partnerships with brands, communities,
  universities, residential compounds, sports clubs, content platforms and other
  local ecosystems to drive customer growth.
- Design partnership initiatives that generate measurable outcomes: customer
  acquisition, order frequency, basket size and market penetration.
- Collaborate cross-functionally with Commercial, Growth, Operations, Brand and
  Performance Marketing to activate partnerships across digital, in-app, on-ground
  and creator channels.
- Use data to evaluate influencer effectiveness, optimise investment and prioritise
  partnerships; analyse hub/area performance to find high-potential markets.
- Track performance vs KPIs (reach, engagement, CAC, orders, ROI, sentiment) and
  build repeatable playbooks scalable across cities and markets.

What you'll need:
- 3+ years in influencer marketing, social media, strategic partnerships, growth
  marketing or a related field.
- Proven end-to-end influencer campaigns and external partnerships.
- Strong understanding of UAE & KSA creator ecosystems, social platforms, digital
  culture.
- Growth-focused partnerships with measurable business outcomes.
- Strong analytical skills with campaign data, dashboards and marketing metrics.
- Experience evaluating influencer audiences, performance and ROI to optimise
  investments.
- Excellent negotiation, stakeholder management and relationship-building.
- Highly organised, multi-project, fast-paced high-growth environment.
- Strong communication and presentation. English required; Arabic a strong plus.
"""

ATS = [
    "influencer marketing", "social media", "strategic partnerships",
    "growth marketing", "creator", "mega macro micro nano", "creator sourcing",
    "briefing", "campaign optimisation", "UGC", "social-first", "Instagram",
    "TikTok", "YouTube", "Snapchat", "content", "customer acquisition",
    "order frequency", "basket size", "market penetration", "CAC", "ROI",
    "reach", "engagement", "sentiment", "negotiation", "stakeholder management",
    "budget management", "playbooks", "quick-commerce", "noon", "FMCG",
    "UAE", "KSA", "cross-functional", "performance marketing",
]

# --------------------------------------------------------------------------
# CV content
# --------------------------------------------------------------------------
CV_CONTENT = {
    "headline": "Influencer Marketing · Social Media · Strategic Partnerships · Quick-Commerce Growth",
    "professional_summary": (
        "Influencer, social and partnerships marketer with 4+ years driving creator-led growth across "
        "FMCG, Beauty and e-commerce — currently in Dubai. At DoFreeze I built the influencer programme "
        "from zero: end-to-end ownership of strategy, creator sourcing, briefing, negotiation, execution "
        "and reporting across mega, macro, micro and nano tiers, running 25–50 creators per campaign with "
        "sampling & seeding, UGC and measurable sell-out. At Alibaba's Miravia I created social-first "
        "destinations (Hot on Social, Beauty Club) and led strategic brand partnerships, onboarding 30+ "
        "brands while growing 42 accounts +30% GMV QoQ. Hands-on across UAE quick-commerce (noon, Talabat, "
        "Careem, Deliveroo) — the exact 15-minute grocery surface noon Minutes runs on — and data-driven on "
        "reach, engagement, CAC, ROI and ROAS. Already based in Dubai on a residence visa; bilingual "
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
                "Built and scaled the influencer marketing programme from zero — owning it end-to-end (strategy, creator sourcing, briefing, negotiation, contracts, execution, reporting and optimisation) across mega, macro, micro and nano tiers, running 25–50 creators per campaign to drive authentic UGC, brand awareness and measurable sell-out",
                "Develop and execute social-first campaigns across Instagram and TikTok aligned to product launches, promotions and cultural moments — spotting emerging trends and reacting fast with high-impact content and creator activations",
                "Run product sampling and seeding programmes with creators across modern trade and quick-commerce, converting creator content into on-platform demand, orders and sell-out",
                "Integrate and grow brands on UAE quick-commerce platforms — noon, Careem, Talabat and Deliveroo, the same 15-minute grocery q-commerce surface as noon Minutes — managing listings, promotional mechanics and retail execution to lift orders and basket size",
                "Negotiate commercial terms and manage creator, agency and A&P budgets, coordinating external agencies and creators to ensure seamless, consistently high-quality delivery",
                "Plan and optimise paid social on Meta (Instagram/Facebook) and Google Ads — audience building, creative A/B testing — analysing ROI, ROAS and acquisition cost to prioritise investment; built an AI-powered automation system (Claude/GPT) for campaign planning, content and KPI reporting, cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account & Social Projects Lead – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Created and led the Hot on Social and Beauty Club projects — social-first, content-led destinations that boosted brand visibility, engagement and loyalty and positioned Miravia as a beauty & lifestyle destination",
                "Led strategic brand partnerships as PIC Fragrances — sourcing, negotiating and onboarding 30+ brands in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — expanding the brand ecosystem and customer reach",
                "Managed 42 key brand accounts and partnerships, achieving +30% GMV growth QoQ through pricing, assortment optimisation and targeted, trend-driven promotions",
                "Continuously analysed ROI, ROAS, conversion, traffic, retention and engagement to evaluate campaign effectiveness, optimise investment and improve forecasting accuracy",
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
                "Built strategic partnerships onboarding fashion and lifestyle brands as Glovo expanded its q-commerce marketplace beyond food — driving customer acquisition, order volume and category growth",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning and bespoke marketing activations",
                "Led cross-functional teams across marketing, logistics and customer support to deliver seamless, high-impact campaigns and activations",
                "Negotiated and closed high-impact commercial deals, managing terms and deliverables to maximise profitability for both platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Analysed promotional effectiveness and sell-in/sell-out for the chocolate category, building performance reports and surfacing growth opportunities",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": "influencer marketing (mega/macro/micro/nano), creator sourcing & briefing, social-first campaigns, UGC & content, sampling & seeding, strategic partnerships, brand strategy, go-to-market, A&P & creator budget management, generative-AI campaigns",
    "skills_ecommerce": "Instagram, TikTok, YouTube, Snapchat, social media management & calendars, quick-commerce (noon, Talabat, Careem, Deliveroo), Meta Ads (Instagram/Facebook), Google Ads, Shopify, marketing automation",
    "skills_commercial": "strategic partnerships, creator & brand negotiation, contract & deliverable management, stakeholder management, brand onboarding, key account management, budget & timeline management",
    "skills_data": "campaign performance analytics, reach & engagement, CAC, ROI, ROAS, KPI dashboards & scorecards, audience & influencer evaluation, sentiment analysis, sell-in/sell-out, AI-assisted analysis, Looker, Power BI",
    "skills_tools": "Meta Business Suite, Meta Ads Manager, Instagram, TikTok, Google Ads, Shopify, Canva, Generative AI (Claude, ChatGPT), Power BI, Looker, Salesforce, Microsoft Office (Expert)",
}


def make_job() -> Job:
    return Job(
        id="noon-influencer-social-partnerships-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/noon/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Influencer, Social Media & Strategic Partnerships Specialist",
             "via": "LinkedIn", "team": "noon Minutes"},
    )


def _convert_pdf(docx_path: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice headless (reliable, non-interactive).

    Keeps the editable DOCX alongside the PDF.
    """
    pdf_path = docx_path.with_suffix(".pdf")
    try:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", "--outdir",
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
        "ai_score": 92,
        "ai_tier": "Hot",
        "skills_match": [
            "Influencer programme built end-to-end (DoFreeze)",
            "Mega/macro/micro/nano creators, 25-50 per campaign",
            "Sampling & seeding + UGC + measurable sell-out",
            "Social-first storytelling (Miravia Hot on Social / Beauty Club)",
            "Strategic partnerships & brand onboarding (30+ brands)",
            "Hands-on UAE quick-commerce (noon, Talabat, Careem, Deliveroo)",
            "ROI / ROAS / CAC & campaign analytics",
            "Negotiation, budgets, stakeholder management",
            "Already in Dubai (residence visa)", "3+ yrs exp",
        ],
        "missing_skills": ["Arabic (advantage, not required)"],
        "sector_fit": "exact (FMCG q-commerce)",
        "seniority_fit": "exact",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit: the JD wants 3+ yrs in influencer marketing, social media and strategic "
            "partnerships with end-to-end campaign ownership, tiered creators, UGC, ROI/CAC analytics "
            "and UAE/KSA creator-ecosystem fluency. Paula built DoFreeze's influencer programme from "
            "zero (25-50 creators/campaign, mega->nano, sampling & seeding, measurable sell-out), ran "
            "social-first projects at Miravia (Hot on Social, Beauty Club), led strategic brand "
            "partnerships (30+ onboarded), and works hands-on across noon + UAE quick-commerce — the "
            "exact 15-min grocery surface noon Minutes runs. Dubai residence visa, C1 English. Arabic "
            "would be a plus she doesn't have, but it's explicitly not required."
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
