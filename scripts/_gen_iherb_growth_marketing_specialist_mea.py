"""One-off: generate Paula's CV + cover letter for iHerb
"Growth Marketing Specialist, MEA" — execution-focused paid media role across
Middle East & Africa markets.

Why this is a strong, honest fit:
  - The role's spine is hands-on paid media EXECUTION: campaign setup, QA, launch,
    pacing, optimisation and reporting on Google Ads and Meta Ads across MEA
    markets, tracking CAC / ROAS / conversion / CTR / CPC / CPM, running creative
    and A/B tests, coordinating localisation, and keeping tracking/UTM/reporting
    accurate. That is genuinely Paula's day-to-day at DoFreeze, where she plans,
    launches and optimises Meta (Facebook & Instagram) and Google Ads across GCC,
    MENA, Asia, Europe and AFRICA (50+ countries) — the exact MEA footprint.
  - E-commerce is the terrain she owns: Shopify store end-to-end + CRO/AOV, UAE
    quick-commerce (Noon, Talabat, Careem, Deliveroo), and — at Alibaba's Miravia —
    ROI/ROAS/conversion/retention analysis across 42 accounts with +30% GMV QoQ.
  - Tooling overlap: Looker, Tableau, Power BI, Google Ads, Meta Ads Manager /
    Business Suite, Microsoft Office (Expert), plus generative-AI automation for
    reporting and creative.

Honest positioning (NO fabrication):
  - This is a SPECIALIST / execution-level role (2–5 yrs); Paula is at Brand &
    Marketing MANAGER level. Framed truthfully — she brings the hands-on craft the
    role runs on and would step into a focused execution seat; stated plainly.
  - Arabic or Hebrew is "preferred" (not required). Paula works across
    Arabic-speaking MENA markets and coordinates localisation, but her own fluency
    is English (C1) and Spanish (native) — stated honestly, not overclaimed.
  - Apple Search Ads / app-acquisition and formal incrementality/geo/holdout/lift
    studies are NOT her core — surfaced as honest gaps in the dashboard record; the
    CV/letter lead with the real Meta/Google performance craft and do not claim ASA
    or incrementality tests she hasn't run. NO Amplitude / Google Analytics claim
    (not in profile). NO "no sponsorship needed" claim (standing rule).

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-21/.
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

COMPANY = "iHerb"
TITLE = "Growth Marketing Specialist, MEA"
DATE_FOLDER = "2026-08-21"

# No hiring manager named in the posting — letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Growth Marketing Specialist, MEA (Middle East & Africa) — iHerb.

iHerb is a global e-commerce brand on a mission to make healthy, balanced living
easy and accessible ("For A Better You"). We are looking for a Growth Marketing
Specialist, MEA to support the execution, optimisation and operational management
of paid media campaigns across key MEA markets. This role is highly
execution-focused and ideal for someone with hands-on paid media experience,
strong attention to detail, and a passion for campaign operations, performance
analysis, creative testing and process improvement.

Job expectations:
- Execute and support paid media campaigns across assigned MEA markets — campaign
  setup, QA, launch, monitoring, pacing, optimisation and reporting.
- Manage day-to-day campaign operations across Google Ads, Meta Ads, TikTok Ads,
  Apple Search Ads and other relevant regional paid media platforms.
- Implement campaign structures, audience targeting, bidding strategies, budgets,
  creative rotations, tracking parameters and platform settings based on approved
  growth plans.
- Monitor campaign performance daily and identify issues related to spend pacing,
  delivery, tracking, creative fatigue, audience performance, conversion rates,
  CAC, ROAS and other core KPIs.
- Support optimisation against new customer acquisition, revenue, ROAS, CAC, LTV,
  payback period, contribution margin and conversion rate.
- Assist with budget pacing and reallocation across markets, platforms, campaigns,
  ad groups, audiences and creative assets.
- Support structured testing roadmaps across creative, audiences, bids, landing
  pages, campaign structures, offers, localisation and platform features.
- Coordinate performance creative workflows — briefing, asset trafficking,
  localisation, naming conventions, version control, approvals, uploads and
  post-launch performance tracking.
- Partner with creative, localisation and regional stakeholders to ensure ads are
  accurate, culturally relevant, platform-compliant and aligned with testing needs.
- Analyse performance creative by format, hook, message, offer, language, market,
  audience, placement and funnel stage.
- Maintain campaign documentation, testing trackers, launch calendars, QA
  checklists, naming conventions, UTM standards and reporting processes.
- Support measurement initiatives — incrementality tests, geo tests, platform lift
  studies, holdout tests, attribution analysis and cohort reporting.
- Prepare recurring performance reports, insights summaries and test readouts.
- QA tracking, attribution, pixels, conversion events, product feeds, landing URLs,
  UTMs and campaign taxonomy to ensure reporting accuracy.
- Support agency, platform partner and vendor coordination.

Required knowledge, skills and abilities:
- Hands-on experience executing or supporting paid media campaigns across Google
  Ads, Meta Ads, TikTok Ads, Apple Search Ads or similar performance channels.
- Experience with MEA-specific / regional paid media platforms strongly preferred.
- Strong campaign operations skills — setup, trafficking, QA, budget pacing, naming
  conventions, tracking and performance reporting.
- Working knowledge of paid search, paid social, app acquisition, display,
  retargeting, shopping campaigns, catalog ads and feed-based advertising.
- Ability to analyse campaign performance and identify practical optimisations.
- Familiarity with CAC, ROAS, LTV, conversion rate, CTR, CPC, CPM, CVR, payback
  period, retention and contribution margin.
- Exposure to incrementality, lift studies, holdout, geo testing, attribution or
  media mix measurement preferred.
- Experience supporting creative testing and translating results into learnings.
- Strong attention to detail; manage multiple campaigns, markets and stakeholders.
- Comfortable with spreadsheets, dashboards, reporting and campaign platforms.
- Professional/native fluency in English required; Arabic or Hebrew preferred.
- Microsoft Office; Google Business Suite preferred; analytics/BI tools such as
  Looker, Tableau, Google Analytics, Amplitude; e-commerce marketing ops tools.
- 2–5 years in performance marketing, growth marketing, paid media, digital
  marketing or marketing operations. Bachelor's degree preferred.
"""

ATS = [
    "Growth Marketing", "Growth Marketing Specialist", "performance marketing",
    "paid media", "paid social", "paid search", "campaign operations",
    "campaign setup", "QA", "launch", "pacing", "optimisation", "optimization",
    "reporting", "Google Ads", "Meta Ads", "Meta Ads Manager",
    "Meta Business Suite", "Facebook Ads", "Instagram Ads", "TikTok Ads",
    "audience targeting", "bidding", "budgets", "budget pacing",
    "creative rotations", "creative testing", "A/B testing", "landing pages",
    "retargeting", "lookalike audiences", "shopping campaigns", "catalog ads",
    "feed-based advertising", "tracking", "UTM", "attribution", "pixels",
    "conversion events", "product feeds", "naming conventions", "campaign taxonomy",
    "CAC", "ROAS", "LTV", "conversion rate", "CTR", "CPC", "CPM", "CVR",
    "payback period", "retention", "contribution margin", "new customer acquisition",
    "localisation", "localization", "MEA", "Middle East & Africa", "MENA", "GCC",
    "Africa", "e-commerce", "ecommerce", "marketing operations", "Looker",
    "Tableau", "Power BI", "spreadsheets", "dashboards", "performance reports",
    "test-and-learn", "data-driven", "English",
]

CV_CONTENT = {
    "headline": (
        "Growth & Performance Marketing · Paid Media (Meta & Google Ads) · "
        "E-Commerce & ROAS · MENA & Africa Markets"
    ),
    "professional_summary": (
        "Growth and performance marketer with 4+ years across E-Commerce, FMCG and Beauty who executes paid "
        "media hands-on across Middle East & Africa markets. At DoFreeze I plan, launch and optimise Meta Ads "
        "(Facebook & Instagram) and Google Ads across GCC, MENA, Asia, Europe and Africa (50+ countries) — "
        "campaign setup, QA, budget pacing, audience and bidding strategy, creative rotations and A/B testing, "
        "UTM/tracking hygiene and daily performance reporting against CAC, ROAS, conversion rate and CTR/CPC/CPM. "
        "Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, conversion and retention across 42 accounts to "
        "optimise channel performance (+30% GMV QoQ). Detail-obsessed campaign operator, comfortable in "
        "spreadsheets, dashboards (Looker, Tableau, Power BI) and fast test-and-learn cycles, and an early "
        "adopter of generative AI (Claude/GPT) to scale campaign planning, creative and reporting. Business "
        "Administration graduate, fluent English (C1), based in Dubai on the MEA time zone."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG e-commerce distributor | Brands: Befit, Eurocake, Flair | 50+ countries (GCC, MENA, Africa, Asia, Europe, USA)",
            "bullets": [
                "Execute and optimise paid media end-to-end on Meta Ads (Facebook & Instagram) and Google Ads across GCC, MENA and Africa markets — campaign setup, QA, launch, spend pacing, optimisation and reporting against new-customer-acquisition, ROAS and conversion goals",
                "Run day-to-day campaign operations: audience targeting, bidding strategies, budgets, creative rotations, UTM/tracking parameters and naming conventions — monitoring delivery, creative fatigue, CAC, ROAS, CTR/CPC/CPM and conversion rate daily to catch pacing and tracking issues early",
                "Run structured test-and-learn across creative, audiences, offers, placements and landing pages, and coordinate performance-creative workflows with design and localisation — briefing, versioning, approvals and post-launch performance tracking across markets and languages",
                "Prepare recurring performance reports and insight summaries for stakeholders, and built AI-powered automation (Claude/GPT) that scales campaign planning, creative and KPI reporting — cutting manual workload ~40%",
                "Own the brand's Shopify store end-to-end (catalogue, UX, checkout), lifting conversion rate (CRO) and average order value, and integrated brands into UAE quick-commerce (Noon, Talabat, Careem, Deliveroo) — closing the loop from paid click to purchase",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across 42 accounts to optimise channel performance and forecasting accuracy — turning performance data into practical optimisation decisions",
                "Managed 42 key accounts across beauty, fragrances and fashion, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO, and created the Beauty Club and Hot on Social projects — boosting brand visibility and engagement across social channels",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew strategic accounts through data-led joint planning and bespoke marketing activations, tracking performance to optimise campaigns and order volume",
                "Supported building Glovo's Retail vertical — onboarding fashion and lifestyle brands with tailored launch campaigns and promotions",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, building performance reports in advanced Excel that informed spend and commercial planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) with data-driven analysis, turning category data into actionable recommendations",
            ],
        },
    ],
    "skills_ecommerce": (
        "Meta Ads Manager, Meta Business Suite, Facebook & Instagram Ads, Google Ads, TikTok, paid social, "
        "paid search, retargeting / lookalike audiences, shopping & catalog ads, A/B & creative testing, "
        "landing-page testing, Shopify, conversion rate optimisation (CRO), quick-commerce (Noon, Talabat, "
        "Careem, Deliveroo), UTM tracking, EDM, marketing automation"
    ),
    "skills_data": (
        "ROAS / CAC / ROI optimisation, campaign performance & KPI analysis (CTR, CPC, CPM, CVR, conversion "
        "rate, retention), budget & spend pacing, A/B test analysis, attribution & tracking QA (UTMs, pixels, "
        "feeds, taxonomy), forecasting, performance reporting, Looker, Tableau, Power BI"
    ),
    "skills_brand": (
        "growth & performance marketing, paid media execution & operations, full-funnel campaigns, audience & "
        "creative testing, localisation workflows, go-to-market across 50+ markets, influencer & UGC, "
        "generative-AI campaign & reporting automation"
    ),
    "skills_commercial": (
        "new customer acquisition & growth, budget management, pricing & promotion strategy, stakeholder & "
        "vendor coordination, agency / platform-partner management, key account management, negotiation"
    ),
    "skills_tools": (
        "Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, Generative AI (Claude, ChatGPT), Looker, "
        "Tableau, Power BI, Microsoft Office — Expert (Excel, PowerPoint, Word), Google Workspace, Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "iHerb's mission to make healthy living easy and accessible — everywhere, in every market — is exactly "
        "the kind of e-commerce challenge I like, so the Growth Marketing Specialist, MEA role caught my eye. "
        "Executing and optimising paid media across Middle East & Africa markets is close to my day-to-day: at "
        "DoFreeze I plan, launch and optimise Meta and Google Ads campaigns across GCC, MENA and Africa, so "
        "running performance campaigns market-by-market across this exact footprint is already what I do."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze, I own paid media execution end-to-end — campaign setup, QA, "
        "launch, budget pacing and optimisation on Meta Ads (Facebook & Instagram) and Google Ads — building "
        "audience targeting, bidding and creative rotations, keeping UTM tracking and naming conventions clean, "
        "and monitoring CAC, ROAS, conversion rate and CTR/CPC/CPM daily to catch pacing, delivery and "
        "creative-fatigue issues early. I run structured A/B and creative tests and coordinate performance "
        "creative with design and localisation across languages and markets. Earlier, at Alibaba's Miravia, I "
        "analysed ROI, ROAS, conversion and retention across 42 accounts to grow GMV +30% QoQ — so the "
        "detail-heavy, data-driven side of campaign operations is second nature."
    ),
    "body_paragraph_2": (
        "A few things I'd bring beyond the checklist: I'm already based in Dubai on the MEA time zone and "
        "available immediately, I own an e-commerce Shopify store and its conversion rate (CRO) so I optimise "
        "the full journey from paid click to purchase, and I'm an early adopter of generative AI (Claude/GPT) "
        "with automation that scales campaign planning, creative and reporting — genuinely useful for testing "
        "roadmaps and recurring readouts. I'll be straightforward about two things: this is a specialist, "
        "execution-focused seat and I currently sit at Manager level, so I'm applying because the hands-on "
        "paid-media craft is what I most enjoy; and while I work across Arabic-speaking MENA markets and "
        "coordinate localisation, my own fluency is English (C1) and Spanish (native)."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd set up, QA, launch and optimise MEA campaigns for iHerb — from "
        "audience and bidding structures through creative testing and budget pacing to the clean tracking and "
        "reporting that keep ROAS and CAC honest. I'm fluent in English, based in Dubai and available to start "
        "quickly. Thank you for considering my application — I'd be glad to walk through how I'd approach a "
        "first 90 days of MEA paid media."
    ),
}


def make_job() -> Job:
    return Job(
        id="iherb-growth-marketing-specialist-mea-2026-08",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (MEA)",
        url="https://www.linkedin.com/jobs/search/?keywords=iHerb%20Growth%20Marketing%20Specialist%20MEA",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Growth Marketing Specialist MEA iHerb",
             "function": "Growth / Performance Marketing",
             "workplace": "MEA (Middle East & Africa)",
             "note": "Execution-focused paid media specialist role across MEA markets; no hiring manager named in posting"},
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
        "ai_score": 73,
        "ai_tier": "Warm",
        "skills_match": [
            "Hands-on paid media execution on Meta Ads (Facebook & Instagram) and Google Ads — setup, QA, launch, pacing, optimisation, reporting",
            "Runs campaigns across the exact MEA footprint today (GCC, MENA, Africa) at DoFreeze — 50+ countries",
            "Day-to-day campaign operations: audience targeting, bidding, budgets, creative rotations, UTM tracking, naming conventions",
            "Core KPI fluency: CAC, ROAS, conversion rate, CTR, CPC, CPM, retention — monitored daily",
            "Structured A/B & creative testing across creative, audiences, offers, placements, landing pages",
            "Performance-creative + localisation workflow coordination (briefing, versioning, approvals, post-launch tracking)",
            "Tracking / attribution QA — UTMs, tracking parameters, campaign taxonomy, reporting accuracy",
            "E-commerce marketing ops: Shopify + CRO/AOV, UAE quick-commerce (Noon, Talabat, Careem, Deliveroo)",
            "Dashboards & reporting: Looker, Tableau, Power BI; comfortable in spreadsheets",
            "ROI/ROAS/conversion/retention analysis across 42 accounts, +30% GMV QoQ (Alibaba's Miravia)",
            "Generative-AI automation for campaign planning, creative & reporting",
            "Fluent English (C1); already based in Dubai on the MEA time zone, available immediately",
        ],
        "missing_skills": [
            "Apple Search Ads / app-acquisition (ASA) — not part of her core; her paid media is Meta + Google (positioned honestly, not claimed)",
            "TikTok Ads as a paid channel — she works with TikTok organically but Meta/Google are her hands-on paid platforms",
            "Formal incrementality / geo / holdout / lift studies (listed as 'exposure preferred') — she does ROAS/attribution analysis but not those specific test designs",
            "Arabic or Hebrew fluency (preferred, not required) — she works across Arabic-speaking MENA markets but her own fluency is English (C1) + Spanish (native)",
            "Amplitude / Google Analytics not in profile — dashboards covered via Looker, Tableau, Power BI",
        ],
        "sector_fit": "strong (global e-commerce / performance marketing — direct; wellness vertical adjacent to FMCG/Beauty)",
        "seniority_fit": "above-band on title (Brand & Marketing Manager vs a specialist/execution 2–5 yr role) but squarely within the 2–5 yr experience window",
        "red_flags": [
            "Specialist, execution-focused level sits below Paula's current Manager seniority — a lateral/step-into-execution move; framed truthfully in the letter",
            "Arabic or Hebrew is 'preferred' and Paula holds neither; English required (she has C1) so not a hard blocker, but a genuine soft gap for MEA localisation",
            "JD emphasises Apple Search Ads / app acquisition and formal incrementality testing — outside her core; she leads with Meta/Google performance craft instead",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit on the core axis. The role is an execution-focused paid-media specialist for "
            "MEA: set up, QA, launch, pace, optimise and report on Google Ads and Meta Ads across Middle East "
            "& Africa markets, tracking CAC/ROAS/conversion/CTR/CPC/CPM, running creative and A/B tests, "
            "coordinating localisation, and keeping UTM/tracking/reporting clean — all of which Paula does "
            "hands-on today at DoFreeze across GCC, MENA and Africa (50+ countries), reinforced by "
            "ROI/ROAS/conversion/retention analysis across 42 accounts and +30% GMV QoQ at Alibaba's Miravia, "
            "plus a Shopify/CRO e-commerce loop and quick-commerce experience. Honest gaps: Apple Search Ads / "
            "app acquisition and formal incrementality/geo/holdout studies are outside her core; she doesn't "
            "hold Arabic or Hebrew (preferred, not required); and this is a specialist/execution seat below her "
            "current Manager title. CV + letter lead with the genuine Meta/Google performance-ops craft and the "
            "MEA market footprint, and state the seniority and language nuances plainly; no ASA, incrementality, "
            "Amplitude or GA claims."
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
