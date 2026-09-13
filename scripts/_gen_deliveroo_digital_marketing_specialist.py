"""One-off: generate Paula's CV for the Deliveroo "Digital Marketing Specialist"
(Dubai, remote — Brand & Experience team) role.

This is a full-funnel DIGITAL / PERFORMANCE MARKETING role: manage and execute
data-driven digital campaigns across YouTube, Meta, Snapchat, TikTok & programmatic;
media planning & scheduling; performance reporting (ROI/KPI); post-campaign analysis
and stakeholder insight-sharing; consumer-centric, test-and-learn mindset; attention
to detail in copywriting + visual design. Asks 3–5 yrs in Digital Marketing or Media,
a marketing/related degree, and strong understanding of the local (UAE) media landscape.

Paula's fit (all strictly truthful, from profile.yaml — NO invented experience):
- At **DoFreeze (Dubai)** she plans and optimises paid media on **Meta (FB & IG) and
  Google Ads** — audience building, creative A/B testing, paid social and EDM —
  managing budget against **ROI/ROAS** and running post-campaign analysis; she also
  built an **AI (Claude/GPT) reporting + campaign-planning system** and runs
  **creator/social campaigns on Instagram & TikTok** (25–50 creators/campaign).
- At **Alibaba's Miravia** she continuously analysed **ROI, ROAS, conversion, traffic
  and retention** and led the "Hot on Social" / Beauty Club social programmes.
- **Google Digital Marketing** and **Google E-Commerce** certificates; BBA (CUNEF,
  E-Commerce specialisation, 9.5/10 thesis).

Honest gaps (surfaced, not hidden): Snapchat / programmatic / YouTube ads hands-on
(her documented paid media is Meta + Google; TikTok/Instagram/Pinterest organic +
creator) and formal agency experience (a "good to have"). NOT claimed.

Content authored directly (no LLM key needed here) and kept strictly truthful. Fills
the real CV template, converts to PDF with LibreOffice soffice (docx2pdf/Word is
unreliable headless on this Mac), and lands the package under
output/2026-08-30/Deliveroo - Digital Marketing Specialist/.
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

COMPANY = "Deliveroo"
TITLE = "Digital Marketing Specialist"
DATE_FOLDER = "2026-08-30"

JOB_DESCRIPTION = """\
Digital Marketing Specialist — Deliveroo, Dubai, UAE (Remote). Brand & Experience team.

We're looking for a Digital Marketing Specialist to join our Dubai team, responsible for
managing and executing full-funnel digital marketing campaigns driven by data insights,
collaborating with multiple teams and stakeholders to drive growth. Requires in-depth
knowledge of digital marketing tools, platforms and analytics stacks, including the full
digital suite by Meta, Google, TikTok, Snapchat & local publishers, plus post-campaign
analysis and insight-sharing with stakeholders.

What you'll be doing:
- Campaign Management: day-to-day management of digital campaigns, ensuring brand
  consistency across YouTube, Meta, Snapchat, TikTok & programmatic.
- Media Planning & Scheduling: develop and execute media plans, scheduling campaigns for
  creative and performance efficiency against marketing objectives.
- Collaboration & Innovation: work closely with brand and platform teams, sharing best
  practices and innovative social strategies.
- Performance Reporting: build comprehensive reports tracking ROI and KPI metrics to inform
  strategic decisions.
- Trend Monitoring: stay updated on emerging digital tools, platforms and trends.

What you'll need:
- 3–5 years of experience in Digital Marketing or Media.
- Bachelor's Degree in Marketing or a related field.
- Strong understanding of the local media landscape.
- Proven experience in media planning, media management and campaign implementation.
- Agency experience good to have.
- Consumer-centric, data-driven approach; test-and-learn mindset; flexibility in a
  fast-paced environment; meticulous attention to detail in copywriting and visual design.
"""

ATS = [
    "digital marketing", "performance marketing", "full-funnel", "media planning",
    "media management", "media buying", "campaign management", "campaign implementation",
    "campaign scheduling", "paid media", "paid social", "paid search",
    "Meta", "Meta Ads", "Facebook Ads", "Instagram Ads", "Google Ads", "TikTok",
    "Instagram", "YouTube", "Snapchat", "programmatic", "social media",
    "creative A/B testing", "test-and-learn", "consumer-centric", "data-driven",
    "performance reporting", "post-campaign analysis", "insights", "reporting",
    "ROI", "ROAS", "KPI", "conversion", "retention", "CRO", "EDM", "CRM",
    "analytics", "dashboards", "forecasting", "marketing automation", "generative AI",
    "brand consistency", "copywriting", "art direction", "visual design",
    "stakeholder management", "cross-functional", "local media landscape",
    "quick-commerce", "Deliveroo", "e-commerce", "Shopify", "GCC", "UAE", "Dubai",
    "Google Digital Marketing", "Google E-Commerce",
]

CONTENT = {
    "headline": (
        "Digital & Performance Marketing · Full-Funnel Paid Media (Meta · Google · TikTok) · "
        "Campaign Analytics & Reporting · Dubai / UAE"
    ),
    "professional_summary": (
        "Digital and performance marketer with 4+ years running data-driven, full-funnel campaigns across "
        "FMCG, Beauty, Fashion and e-commerce in the GCC and Europe. At DoFreeze (Dubai) I plan, schedule and "
        "optimise paid media on Meta (Facebook & Instagram) and Google Ads — audience building, creative A/B "
        "testing, paid social and EDM — managing budgets against ROI and ROAS and turning post-campaign data "
        "into decisions, supported by an AI-powered (Claude/GPT) reporting and planning system I built. I have "
        "analysed conversion, traffic and retention at Alibaba's Miravia, run always-on creator campaigns across "
        "Instagram and TikTok, and hold Google Digital Marketing and Google E-Commerce certificates. "
        "Consumer-centric, test-and-learn and detail-obsessed across copy and creative; already based in Dubai "
        "on a UAE residence visa; bilingual Spanish/English."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Brands: Befit, Eurocake, Flair | sold across 50+ countries",
            "bullets": [
                "Plan, schedule and optimise full-funnel paid-media campaigns on Meta (Facebook & Instagram) and Google Ads — audience building, creative A/B testing, paid social and EDM — managing budgets against ROI and ROAS and running post-campaign analysis to compound performance",
                "Built an AI-powered (Claude / generative AI) reporting and campaign-planning system that automates KPI dashboards and post-campaign insight decks, cutting manual reporting ~40% and speeding stakeholder decisions",
                "Run always-on creator and social campaigns across Instagram and TikTok — sourcing, briefing and managing 25–50 creators per campaign — driving UGC, awareness and measurable sell-out",
                "Keep brand and messaging consistent across every digital touchpoint — owning the Shopify e-store and UAE quick-commerce presence (Deliveroo, Noon, talabat, Careem) end-to-end and lifting conversion (CRO)",
                "Partner daily with brand, design and platform stakeholders across 50+ markets, tracking emerging platforms, formats and trends to keep campaigns creative-first and performance-efficient",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across channels to optimise campaign performance and forecasting accuracy — the core of data-driven media decisions",
                "Created and led the 'Hot on Social' and Beauty Club programmes, boosting brand visibility, engagement and loyalty across social",
                "Ran pricing and promotional mechanics across a 42-account portfolio to +30% GMV growth QoQ, translating performance data into growth stories stakeholders acted on",
                "Reported the Flash Sales channel directly to the CEO, turning traffic, conversion and retention data into clear commercial recommendations",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce & food-delivery leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Built bespoke, data-led marketing activations and campaigns for strategic accounts on a food-delivery platform, lifting order volume and GMV through targeted promotions",
                "Worked cross-functionally with marketing, operations and customer support to deliver seamless multi-channel campaigns on time",
                "Helped build out Glovo's new Retail vertical, onboarding fashion and lifestyle brands and expanding the marketplace beyond food",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built promotional-effectiveness and performance reports for the chocolate category — the foundation of post-campaign analysis and using data to tell a story",
                "Identified growth opportunities and contributed to NPD launches (Milka Spread, Mini Suchard), turning category and campaign data into action",
            ],
        },
    ],
    "skills_brand": (
        "full-funnel campaign planning, paid social & search, creator/influencer marketing, "
        "social content & UGC, art direction & copywriting (Adobe, Canva), brand consistency across channels, "
        "go-to-market, generative-AI campaigns"
    ),
    "skills_ecommerce": (
        "Meta Ads (Facebook & Instagram), Google Ads, TikTok, Instagram, Pinterest, EDM/CRM, "
        "Shopify e-store, conversion rate optimisation (CRO), quick-commerce (Deliveroo, Noon, talabat, Careem), "
        "marketing automation"
    ),
    "skills_commercial": (
        "media planning & buying, campaign management & scheduling, promotional mechanics, "
        "stakeholder & cross-functional collaboration (brand, design, platform teams), "
        "key account management, negotiation"
    ),
    "skills_data": (
        "performance reporting, ROI, ROAS, KPI dashboards, post-campaign analysis, "
        "conversion & retention analysis, A/B testing, forecasting, AI-assisted analysis, "
        "Power BI, Tableau, Looker"
    ),
    "skills_tools": (
        "Meta Ads Manager, Meta Business Suite, Google Ads, Generative AI (Claude / ChatGPT), "
        "Shopify, Power BI, Tableau, Looker, Adobe Creative Suite (Photoshop, Illustrator), Canva, "
        "Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="deliveroo-digital-marketing-specialist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (Remote)",
        url="https://www.linkedin.com/jobs/",  # LinkedIn verified job; managed off-LinkedIn by recruiter
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Digital Marketing Specialist Deliveroo Dubai", "via": "LinkedIn (verified job)", "team": "Brand & Experience", "remote": True},
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
        "ai_score": 84,
        "ai_tier": "Hot",
        "skills_match": [
            "Runs paid media on Meta (FB & IG) + Google Ads today at DoFreeze — audience building, creative A/B testing, EDM, budget vs ROI/ROAS",
            "Data-driven performance reporting: built an AI (Claude/GPT) KPI + post-campaign insight system; ROI/ROAS/conversion/retention analysis at Miravia (Alibaba)",
            "Creator/social campaigns on Instagram & TikTok (25–50 creators/campaign) — social strategy + UGC",
            "Google Digital Marketing + Google E-Commerce certificates; BBA (E-Commerce specialisation)",
            "Consumer-centric, test-and-learn (A/B testing), detail-focused in copy + creative",
            "Understands the local UAE media landscape — runs UAE campaigns from Dubai; knows Deliveroo/quick-commerce from the inside",
            "4+ yrs experience — on-band for the 3–5 ask",
        ],
        "missing_skills": [
            "Snapchat / programmatic / YouTube ads hands-on (documented paid media is Meta + Google; TikTok/Instagram/Pinterest organic + creator)",
            "Formal media-agency experience (a 'good to have', not required)",
        ],
        "sector_fit": "excellent (digital/performance marketing for a quick-commerce brand she already integrates into — Deliveroo)",
        "seniority_fit": "on-band (3–5 yrs asked; Paula 4+)",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, on-band fit for a full-funnel digital/performance marketing role. Paula plans and optimises "
            "paid media on Meta and Google Ads at DoFreeze (audience building, A/B testing, EDM, ROI/ROAS), built "
            "an AI-powered KPI + post-campaign reporting system, and runs creator/social campaigns on Instagram and "
            "TikTok — matching campaign management, media scheduling, performance reporting and trend monitoring. "
            "She analysed conversion/traffic/retention at Alibaba's Miravia and holds Google Digital Marketing + "
            "E-Commerce certificates. Non-blocking gaps: hands-on Snapchat/programmatic/YouTube ads (her paid stack "
            "is Meta + Google; TikTok/IG/Pinterest organic + creator) and formal agency experience (a 'good to have'). "
            "Bonus: she already integrates brands into Deliveroo and is based in Dubai on a residence visa."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "CV Ready",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX → PDF with LibreOffice headless (docx2pdf/Word fails on this Mac)."""
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(docx_path.parent), str(docx_path)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    pdf_path = docx_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError(f"soffice did not produce {pdf_path}")
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

    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
