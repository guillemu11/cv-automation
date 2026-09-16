"""One-off: Paula's CV for TripleTen — "Senior User Acquisition Manager"
(fully remote, EdTech, US market, Meta-led paid acquisition, ~$200K/month budget).

Honest read of the fit — this is a STRETCH application, and the CV is written to
lead with what is genuinely true rather than to paper over the gaps:

  Real, defensible matches
  - Hands-on Meta Ads (Facebook & Instagram) + Google Ads ownership at DoFreeze:
    audience building, campaign/ad-set structure, creative A/B testing, budget
    allocation and daily optimisation against ROAS, CAC, conversion rate and
    CTR/CPC/CPM across 50+ markets.
  - "Brief the content producer and judge the output on metrics — you don't write
    scripts or build pages yourself" maps 1:1 to her actual job: she leads a
    graphic designer and a social media executive, briefs every creative and
    reviews the output on performance.
  - "AI is already how you work — Claude, MCP connectors, choosing the right
    model, catching hallucinations" is her sharpest differentiator: she built a
    working generative-AI (Claude/GPT) marketing automation system for campaign
    planning, research, content and KPI reporting.
  - Reads commercial data alongside the ad account: Salesforce (CRM), Power BI /
    Tableau / Looker, ROI/ROAS/conversion/retention analysis across 42 accounts
    at Alibaba's Miravia (+30% GMV QoQ), plus P&L and A&P budget ownership.
  - Traffic quality over cost-per-lead: her whole commercial background is
    sell-out / GMV quality, not vanity volume.
  - Judgment on thin data and narrow audiences: routine in 50+ small markets
    where no campaign ever reaches statistical comfort.

  Honest gaps — stated, never disguised
  - Budget scale: the role owns ~$200K/month in Meta spend scaling several times
    over. Paula's paid budgets are FMCG A&P scale, materially smaller. Not
    claimed otherwise anywhere in the CV.
  - Vertical: the JD wants expensive acquisition with long, multi-step funnels
    (education, B2B, fintech, high-ticket) in the last 2–3 years. Hers are
    short B2C e-commerce / FMCG funnels. Genuine gap.
  - Sales-funnel economics: lead-to-call, call-to-sale, sales call transcripts,
    cohort contribution — she has not owned a lead→call→sale motion. Not claimed.
  - Attribution ownership: she runs pixel/UTM tracking on her own Shopify + Meta
    setup, but "separate buying infrastructure" and full conversion-event/QA
    ownership at scale is beyond what she has done. Framed at her real level.
  - Channels: Meta + Google are hands-on; YouTube, LinkedIn, Reddit and Twitter
    ads are not. No claim made.
  - Title: she is a Brand & Marketing Manager who runs paid, not a career UA
    specialist.
  - English C1 (professional) — stated as-is, matches "full professional English".
  - NO "no sponsorship needed" claim (standing rule).
  - NO Arabic claim (irrelevant here, but the standing rule holds).

Fills the real CV template, converts DOCX -> PDF via LibreOffice (docx2pdf/Word
silently fails on this Mac), registers the job for the dashboard, and lands the
package under output/2026-09-16/.
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

COMPANY = "TripleTen"
TITLE = "Senior User Acquisition Manager"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Senior User Acquisition Manager — TripleTen. Fully remote. Full-time.
Listed at EUR 200,000 / year (Indeed). EdTech company running tech career
learning programs for the US and Latin American markets, cohort-based, built on
its own platform and curriculum in partnership with Nebius AI. Fully remote,
globally distributed team.

Data-driven and strategic Senior User Acquisition Manager to lead Meta Ads
efforts across the US region. Reports to the Marketing Lead. Responsible for
scaling high-budget campaigns and optimising complex funnels to drive enrolment
for high-value tech programs.

Requirements:
- 4+ years in performance marketing or user acquisition, with hands-on account
  work at real budgets in expensive markets in the last year or two.
- Experience with expensive acquisition and long, multi-step funnels — education,
  B2B, fintech, high-ticket services — in the last two to three years.
- Comfort with narrow audiences and thin data, where judgment fills the gap
  statistics won't; a clear answer to what "enough delivery to decide" means.
- Full-funnel economics — CAC, contribution, cohorts, lead-to-call, call-to-sale —
  reading CRM and BI data alongside the ad account.
- Attribution, conversion events, pixels and tracking QA owned first-hand.
- Strong craft: A/B testing offers and creatives, and briefs a production team
  can run with.
- AI is already how you work — Claude, call-analysis tools, MCP connectors,
  choosing the right model, catching hallucinations.
- Full professional English level.

What you will do:
- Own the budget and paid strategy for the advanced programs line — roughly
  $200K/month today, scaling several times over by year-end.
- Run Meta and Google (YouTube included) as core volume channels; open LinkedIn
  and run experiments in Reddit and Twitter.
- Own campaign and ad-set architecture, plus the keep-or-kill calls: small
  batches, a data threshold before deciding, weekly cadence, an honest decision log.
- Brief the content producer and judge the output on metrics — you don't write
  scripts or build pages, creatives or dashboards yourself.
- Own traffic quality rather than cost per lead: read sales call transcripts, see
  who actually shows up, influence target-audience share.
- Own attribution and conversion events — pixel and event setup, separate buying
  infrastructure, reconciling the ad account against CRM and BI.
- Take each new program into your channels with its own funnel and targets,
  adding sales rather than redistributing share.

What they offer: competitive compensation, full-time remote contract with a
flexible schedule, international team, all software licences and remote tools
(Slack, Miro, Notion, Zoom).
"""

ATS = [
    "user acquisition", "UA", "Senior User Acquisition Manager", "performance marketing",
    "paid acquisition", "paid media", "paid social", "Meta Ads", "Meta Ads Manager",
    "Meta Business Suite", "Facebook Ads", "Instagram Ads", "Google Ads", "campaign architecture",
    "ad set", "ad-set structure", "budget management", "high-budget campaigns", "scaling budgets",
    "A/B testing", "creative testing", "offer testing", "test-and-learn", "experimentation",
    "keep-or-kill", "decision log", "creative briefs", "briefing a production team",
    "full-funnel", "funnel optimisation", "conversion funnels", "landing pages",
    "CAC", "ROAS", "ROI", "CPL", "CPA", "conversion rate", "CVR", "CTR", "CPC", "CPM",
    "cohorts", "contribution", "traffic quality", "target audience", "audience building",
    "lookalike audiences", "retargeting", "attribution", "conversion events", "pixel",
    "Meta pixel", "tracking QA", "UTM tracking", "CRM", "Salesforce", "BI", "Power BI",
    "Tableau", "Looker", "data-driven", "analytics", "reporting", "forecasting",
    "generative AI", "Claude", "LLM", "AI automation", "AI tools", "MCP",
    "e-commerce", "Shopify", "CRO", "conversion rate optimisation", "growth marketing",
    "demand generation", "remote", "English",
]

CV_CONTENT = {
    "headline": (
        "Performance & Paid Acquisition · Meta and Google Ads · Creative Testing · AI-First (Claude)"
    ),
    "professional_summary": (
        "Performance-minded marketer with 4+ years across e-commerce, FMCG and beauty. I run Meta and Google "
        "paid acquisition hands-on across 50+ markets — campaign architecture, creative A/B testing, daily "
        "CAC/ROAS optimisation — brief a creative team, and build Claude-powered AI into the workflow."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE (remote across 50+ markets)",
            "context": "FMCG / e-commerce group | Brands: Befit, Eurocake, Flair | 50+ markets (GCC, MENA, Europe, Asia, USA, Africa)",
            "bullets": [
                "Own paid acquisition hands-on on Meta Ads (Facebook & Instagram) and Google Ads: campaign and ad-set architecture, audiences and retargeting, budget allocation, creative and offer A/B testing, and keep-or-kill calls against CAC, ROAS, CVR and CTR/CPC/CPM — on narrow audiences and thin data",
                "Brief and review a two-person production team (designer + social media executive), judging creative output on performance metrics rather than taste and turning test results into the next briefs",
                "Built a generative-AI (Claude/GPT) automation system that drafts campaign plans, creative concepts, competitor research and KPI reporting — ~40% less manual work, with a human check on model output",
                "Own the Shopify store and the click-to-purchase funnel — landing pages, checkout, pixel and UTM tracking — lifting conversion rate (CRO) and AOV through data-led testing",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Analysed ROI, ROAS, conversion, traffic quality and retention across 42 accounts, reconciling channel data against CRM and BI (Salesforce, Power BI, Looker) to steer spend",
                "Grew a 42-account portfolio +30% GMV QoQ through pricing, assortment and promotional testing — measured on sell-out quality, not headline traffic",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew strategic accounts through data-led joint planning and bespoke marketing activations, tracking campaign performance to optimise order volume and conversion",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, building the performance reports that informed spend decisions",
            ],
        },
    ],
    "skills_brand": (
        "paid acquisition strategy, campaign & ad-set architecture, creative and offer testing, "
        "creative briefing & production management, full-funnel growth, go-to-market, AI-first workflows"
    ),
    "skills_ecommerce": (
        "Meta Ads Manager & Business Suite, Facebook & Instagram Ads, Google Ads, audience building & "
        "retargeting, A/B testing, landing pages, Meta pixel & UTM tracking, CRO, Shopify, EDM"
    ),
    "skills_commercial": (
        "budget & A&P ownership, P&L awareness, pricing & promotion strategy, team leadership (2 reports)"
    ),
    "skills_data": (
        "CAC, ROAS, ROI, CPL, CVR, CTR/CPC/CPM analysis, funnel & cohort reporting, A/B test reading, "
        "traffic quality, forecasting, Salesforce (CRM), Power BI, Looker, advanced Excel"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Meta Ads Manager, Google Ads, Shopify, Salesforce, Power BI, "
        "Looker, Microsoft Office — Expert, Canva"
    ),
}


def make_job() -> Job:
    return Job(
        id="tripleten-senior-user-acquisition-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Remote — US region coverage",
        url="https://es.indeed.com/",
        source="indeed",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Senior User Acquisition Manager TripleTen remote",
            "function": "Performance Marketing / User Acquisition (Meta-led)",
            "workplace": "Fully remote, full-time contract",
            "salary": "EUR 200,000 / year (as listed on Indeed)",
            "note": (
                "EdTech, US market, ~$200K/month Meta budget scaling several times by year-end. "
                "Reports to Marketing Lead. Stretch application: Paula's paid budgets are far smaller "
                "and her funnels are short B2C e-commerce, not long high-ticket education funnels."
            ),
        },
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
        "salary_raw": "EUR 200,000 / year (Indeed listing)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 52,
        "ai_tier": "Cold",
        "skills_match": [
            "Hands-on Meta Ads + Google Ads owner: campaign/ad-set architecture, audiences, creative A/B testing, daily CAC/ROAS/CVR optimisation across 50+ markets",
            "Briefs and judges a production team (designer + social exec) on metrics — exactly the 'brief the content producer, don't build it yourself' mandate",
            "AI-first by default: built a working Claude/GPT marketing automation system and checks model output — matches the JD's explicit Claude/AI requirement",
            "Reads commercial data next to the ad account: Salesforce CRM, Power BI, Tableau, Looker; ROI/ROAS/conversion/retention across 42 accounts (+30% GMV QoQ at Alibaba's Miravia)",
            "Traffic-quality mindset from a sell-out/GMV background rather than cheap-lead volume",
            "Comfortable deciding on thin data in small markets where campaigns never reach statistical comfort",
            "Owns pixel and UTM tracking on her own Shopify + Meta setup",
            "Fully remote, globally distributed team — she already works across 50+ markets remotely; Spanish native, English C1",
        ],
        "missing_skills": [
            "Budget scale: role owns ~$200K/month Meta spend scaling several times over; Paula's paid budgets are FMCG A&P scale, materially smaller — the single biggest gap",
            "Vertical: JD wants expensive acquisition with long multi-step funnels (education, B2B, fintech, high-ticket) in the last 2-3 years; hers are short B2C e-commerce / FMCG funnels",
            "Sales-funnel economics: lead-to-call, call-to-sale, cohort contribution, sales call transcripts — she has never owned a lead->call->sale motion",
            "Attribution at scale: conversion-event setup, separate buying infrastructure and tracking QA beyond her own pixel/UTM setup are not hers",
            "Channels: YouTube, LinkedIn, Reddit and Twitter ads not used — Meta + Google only",
            "US market acquisition: her markets are GCC/MENA/Europe/Asia; no US paid experience",
            "Title/track: Brand & Marketing Manager who runs paid, not a career user-acquisition specialist",
        ],
        "sector_fit": "distant (B2C FMCG/beauty/e-commerce vs US EdTech high-ticket enrolment funnels)",
        "seniority_fit": "on-band by years (4+ yrs) but below the required budget scale and funnel complexity",
        "red_flags": [
            "Core requirement — hands-on account work at real budgets in expensive markets in the last year or two — is where Paula is weakest; $200K/month is an order of magnitude above her paid spend",
            "Long, multi-step high-ticket funnels (education/B2B/fintech) explicitly required 'in the last two to three years'; she does not have them",
            "Fully remote role outside her Dubai market, listed at EUR 200,000/year — verify the salary figure and contract terms before investing time",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Stretch application. The honest overlap is real but narrow: Paula genuinely owns Meta and Google "
            "paid acquisition hands-on (campaign/ad-set architecture, audiences, creative A/B testing, daily "
            "CAC/ROAS optimisation) across 50+ markets, briefs and judges a two-person creative production team "
            "on metrics — which is literally how the JD describes the job — and is AI-first in a way the JD "
            "explicitly asks for (a working Claude/GPT automation system, with the habit of catching model "
            "errors). She reads CRM and BI alongside the ad account (Salesforce, Power BI, Looker; 42 accounts, "
            "+30% GMV QoQ at Alibaba's Miravia). What she does not have is the part the role is actually built "
            "around: ~$200K/month Meta spend, long multi-step high-ticket funnels in education/B2B/fintech, and "
            "the lead-to-call / call-to-sale economics with conversion-event and attribution ownership at that "
            "scale. The CV leads with the transferable craft, the creative-briefing match and the AI build, and "
            "makes no claim to budget scale, US paid experience, YouTube/LinkedIn/Reddit/Twitter channels or "
            "sales-call funnel ownership."
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

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
