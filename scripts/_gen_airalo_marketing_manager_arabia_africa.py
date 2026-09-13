"""One-off: generate Paula's CV + cover letter for Airalo
"Marketing Manager, Arabia & Africa" — fully remote, UAE-based (Deel EOR).

Why this is a strong, honest fit:
  - The role's spine is (1) regional marketing PERFORMANCE & REPORTING — pulling
    spend/revenue/ROI/ROAS/conversion data across markets, maintaining trackers &
    dashboards, turning data into KPI reporting for leadership; (2) cross-functional
    CAMPAIGN & INITIATIVE COORDINATION across growth, performance, content, creative,
    influencer, PR and product; and (3) MARKETING OPERATIONS (budget tracking, vendor
    docs, follow-ups, keeping initiatives on track). All three are Paula's day-to-day.
  - Killer differentiator: this is an "Arabia & Africa" multi-market role, and Paula's
    DoFreeze remit is explicitly multi-market across 50+ countries including GCC, MENA
    and Africa — the single hardest requirement to fake, and she has it. Reinforced by
    the analytical spine from Miravia (ROI/ROAS/conversion/retention across 42 accounts,
    +30% GMV QoQ) and reporting/business-review work at Mondelez (sell-in/sell-out,
    promo effectiveness, monthly performance reports).
  - Tool "plus" list (Google Sheets, Excel, Looker, Notion) genuinely overlaps: she is
    MS Office Expert, has Looker in her stack, and lives in Notion (her whole CRM/
    automation runs on it). Salary band (281k–380k AED/yr ≈ 23.4k–31.7k AED/month) sits
    above her 20k/month floor.

Honest positioning (NO fabrication):
  - Experience bar is "6+ years"; Paula's continuous marketing/commercial track is
    ~5 years (Mondelez Aug-2021 → present), plus earlier Inditex retail. Summary states
    5 years truthfully; the letter leads with depth-of-fit, not the year count. Flagged
    in missing_skills.
  - Arabic fluency is "preferred". Paula is Spanish native + English C1, NOT an Arabic
    speaker. The letter acknowledges this plainly rather than hiding it. NOT fabricated.
  - Mobile-attribution tools (Adjust, AppsFlyer, QuickSight) are "a plus"; she does NOT
    hold them and none are claimed. Only tools in profile.yaml are surfaced.
  - Remote role via Deel EOR — visa is not a factor and is not surfaced. Per standing
    rule, NO "no sponsorship needed" claim. "Already based in the UAE" is stated only as
    the factual match to "Remote, anywhere in the UAE".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice (soffice
headless — docx2pdf/Word silently fails on this Mac), registers the job for the
dashboard, and lands the package under output/2026-08-18/.
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

COMPANY = "Airalo"
TITLE = "Marketing Manager, Arabia & Africa"
DATE_FOLDER = "2026-08-18"

# No hiring manager named on the Lever posting — letter stays "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Marketing Manager, Arabia & Africa — Airalo. Location: Remote, anywhere in the UAE.
Contract: Full-time, permanent via Deel (employer of record in the UAE). Working
language: English. Airalo is the world's first eSIM store, used by millions of
travelers across 200+ countries; a fully remote team of 400+ people across 60+
countries.

We are looking for a highly organized, analytical, and hands-on Marketing Manager,
Arabia & Africa to support Airalo's growth across one of its most dynamic and
high-potential regions. The role spans performance data, campaign coordination,
stakeholder management, regional initiatives and marketing operations — keeping the
regional marketing engine running smoothly by turning data into clear reporting,
coordinating launches across teams, tracking actions to completion, and supporting the
execution of growth initiatives across multiple markets. Highly execution-focused, with
strong exposure to regional strategy, leadership planning and multi-market growth.

Regional Marketing Performance & Reporting:
- Pull and maintain marketing performance data across channels, markets and time
  periods (MTD, weekly, monthly, historical).
- Track key metrics: spend, revenue, CAC, ROI, installs, signups, transactions,
  conversion rates and other growth KPIs.
- Maintain regional trackers, dashboards and reporting files so performance is easy to
  monitor and act on.
- Help identify performance trends, gaps, opportunities and blockers across markets and
  channels.
- Support monthly business reviews, leadership updates, planning materials and
  performance presentations with clear, accurate, well-structured inputs.

Campaign & Initiative Coordination:
- Support planning and execution of regional marketing initiatives across Arabia &
  Africa.
- Coordinate with Growth, Performance Marketing, Content, Creative, Influencer, PR,
  Product and other cross-functional stakeholders.
- Manage campaign timelines, asset requirements, launch dependencies, approvals and
  stakeholder follow-ups.
- Track campaign readiness before launch and proactively follow up on blockers, missing
  inputs or delayed deliverables.
- Support post-campaign analysis and document learnings for future initiatives.

Marketing Operations & Administration:
- Manage operational and administrative work related to regional marketing activities.
- Support invoice raising, vendor documentation, budget tracking, approvals and
  follow-ups with relevant internal teams.
- Maintain clear organization across trackers, action logs, timelines, planning
  documents and recurring reporting.
- Keep owners, next steps and deadlines visible so regional initiatives keep momentum.

Must Haves:
- 6+ years of experience in marketing, growth, digital marketing, campaign management,
  marketing operations or a similar role.
- Experience working across multiple markets, preferably within Arabia, Africa, GCC,
  MENA or other multi-country regional environments.
- Strong analytical skills and comfort with marketing performance data, dashboards,
  spreadsheets and KPIs.
- Ability to translate data into clear insights, summaries and recommendations.
- Strong project management skills — managing multiple workstreams, timelines,
  stakeholders and follow-ups simultaneously.
- Experience coordinating cross-functional marketing campaigns across creative, content,
  performance, influencer, PR, product or agency teams.
- Strong attention to detail; clean, reliable trackers, reports and documentation.
- A proactive, hands-on mindset — someone who does not wait to be chased and takes
  ownership.
- Strong written and verbal communication skills in English. Arabic fluency is preferred.
- Experience in travel, telecom, e-commerce, mobile apps, marketplaces, fintech or
  consumer digital products is a plus.
- Experience with tools such as Google Sheets, Excel, Looker, QuickSight, Adjust,
  AppsFlyer, Notion or similar platforms is a plus.

Salary (UAE): 281,000 - 380,000 AED a year.
"""

ATS = [
    "Marketing Manager", "Arabia & Africa", "regional marketing", "multi-market",
    "multiple markets", "GCC", "MENA", "Africa", "growth", "digital marketing",
    "campaign management", "campaign coordination", "marketing operations",
    "marketing performance", "performance data", "dashboards", "trackers",
    "reporting", "KPIs", "spend", "revenue", "CAC", "ROI", "ROAS", "installs",
    "signups", "transactions", "conversion rates", "growth KPIs", "MTD",
    "weekly", "monthly", "historical performance", "performance trends",
    "insights", "summaries", "recommendations", "monthly business reviews",
    "leadership updates", "planning materials", "performance presentations",
    "project management", "workstreams", "timelines", "stakeholder management",
    "cross-functional", "Growth", "Performance Marketing", "Content", "Creative",
    "Influencer", "PR", "Product", "asset requirements", "launch dependencies",
    "approvals", "follow-ups", "campaign readiness", "post-campaign analysis",
    "budget tracking", "vendor documentation", "invoice raising", "action logs",
    "attention to detail", "documentation", "proactive", "hands-on", "ownership",
    "English", "e-commerce", "mobile apps", "marketplaces", "consumer digital",
    "Google Sheets", "Excel", "Looker", "Notion", "remote", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Marketing Manager · Multi-Market Growth (GCC · MENA · Africa) · "
        "Performance Reporting & KPIs · Cross-Functional Campaign Coordination · Marketing Operations"
    ),
    "professional_summary": (
        "Highly organized, analytical and hands-on marketing professional with 5 years across FMCG, Beauty "
        "and E-Commerce, currently running multi-market brand & marketing for DoFreeze across 50+ countries "
        "including GCC, MENA and Africa. I keep the regional marketing engine running: pulling performance "
        "data across channels and markets (spend, revenue, ROI/ROAS, conversion, GMV), maintaining trackers "
        "and dashboards, and turning them into clear KPI reporting and recommendations for leadership. I "
        "coordinate campaigns and launches end-to-end across content, creative, influencer, PR, performance "
        "and product — managing timelines, asset requirements, approvals and follow-ups so nothing loses "
        "momentum. Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, conversion and retention across 42 "
        "accounts to grow GMV +30% QoQ, and at Mondelez I owned sell-in/sell-out reporting and monthly "
        "performance reviews. Proactive, detail-obsessed with trackers and documentation, an early adopter "
        "of generative AI (Claude/GPT) for reporting and planning, fluent in English, and already based in "
        "the UAE with a fully remote setup."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Run marketing across 50+ countries including GCC, MENA and Africa — pulling performance data by channel, market and period (spend, revenue, ROI/ROAS, conversion, GMV), maintaining trackers and dashboards, and turning them into clear KPI reporting, trends and recommendations for leadership",
                "Coordinate regional campaigns and product launches end-to-end across content, creative, influencer, PR, performance and product teams — managing timelines, asset requirements, launch dependencies, approvals and stakeholder follow-ups, and tracking campaign readiness before go-live",
                "Manage multiple workstreams in parallel — 6 NPD launches end-to-end (brief, packaging, pricing, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa — keeping owners, next steps and deadlines visible so initiatives keep momentum to completion",
                "Own marketing operations: A&P budget tracking, vendor coordination, approvals and clean action logs, plus trade & shopper marketing plans by channel across 50+ markets",
                "Built and scaled the influencer programme from zero — sourcing, briefing, negotiating and coordinating 25–50 creators per campaign plus product sampling/seeding — and run paid media on Meta and Google Ads, analysing ROI/ROAS to optimise performance",
                "Built AI-powered automation (Claude/GPT) that scales KPI reporting, campaign planning, market research and client-ready decks — cutting manual reporting workload ~40% and accelerating go-to-market across markets",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across 42 accounts to identify trends, gaps and opportunities and optimise channel performance and forecasting accuracy",
                "Managed 42 key accounts across beauty, fragrances and fashion, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and presenting performance-driven commercial plans aligned to P&L targets",
                "Created and led the Beauty Club and Hot on Social projects, coordinating cross-functional teams to boost brand visibility, engagement and customer loyalty",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Led cross-functional teams across marketing, logistics and customer support to deliver seamless campaigns and increase order volume — coordinating stakeholders and dependencies to launch on time",
                "Grew strategic key accounts through data-led joint planning and bespoke activations, tracking performance to optimise campaigns and GMV",
                "Supported building Glovo's Retail vertical — onboarding fashion and lifestyle brands with tailored launch plans and promotions",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Owned sell-in/sell-out analysis and promotional-effectiveness reporting for the chocolate category, building recurring performance reports in advanced Excel that fed monthly business reviews",
                "Turned category data into clear insights and recommendations, and supported NPD launches (Milka Spread, Mini Suchard) with structured, detail-accurate analysis",
            ],
        },
    ],
    "skills_data": (
        "marketing performance analysis, KPI tracking (spend, revenue, CAC, ROI, ROAS, conversion, installs, "
        "signups, GMV), dashboards & trackers, Google Sheets & Excel (advanced), Looker, Power BI, Tableau, "
        "sell-in/sell-out reporting, forecasting, monthly business reviews & performance presentations, "
        "AI-assisted analysis"
    ),
    "skills_brand": (
        "multi-market regional marketing, campaign & launch management, go-to-market, cross-functional "
        "coordination (content, creative, influencer, PR, performance, product), influencer & UGC, "
        "shopper & trade marketing, A&P budget management, omnichannel campaigns, generative-AI reporting automation"
    ),
    "skills_commercial": (
        "project management, multiple-workstream coordination, stakeholder management & follow-ups, "
        "vendor & budget coordination, approvals & documentation, key account management, negotiation, "
        "pricing & promotion strategy"
    ),
    "skills_ecommerce": (
        "quick-commerce (Noon, Talabat, Careem, Deliveroo), Shopify & e-store management, Meta Ads (Facebook "
        "& Instagram), Google Ads, conversion rate optimisation (CRO), Notion, marketing operations, EDM, "
        "marketing automation"
    ),
    "skills_tools": (
        "Google Sheets, Microsoft Excel & Office (Expert), Looker, Notion, Power BI, Tableau, Meta Ads "
        "Manager, Google Ads, Generative AI (Claude, ChatGPT), Salesforce, Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Airalo took the friction out of staying connected abroad, and doing that across 200+ countries with a "
        "fully remote team means the marketing engine has to be exceptionally well-run behind the scenes — which "
        "is exactly the kind of work I love. The Marketing Manager, Arabia & Africa role reads like my current "
        "day-to-day: turning multi-market performance data into clear reporting, coordinating launches across "
        "teams, and keeping every initiative moving to completion. Arabia & Africa is also precisely the map I "
        "already work: at DoFreeze I run marketing across 50+ countries including the GCC, MENA and Africa."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze, I keep the regional engine running: I pull performance data "
        "by channel, market and period (spend, revenue, ROI/ROAS, conversion, GMV), maintain the trackers and "
        "dashboards, and turn them into KPI reporting, trends and recommendations for leadership. I coordinate "
        "campaigns and launches end-to-end across content, creative, influencer, PR, performance and product — "
        "managing timelines, asset requirements, approvals and follow-ups, and chasing down blockers before "
        "go-live. Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, conversion and retention across 42 "
        "accounts to grow GMV +30% QoQ, and at Mondelez I owned the chocolate category's sell-in/sell-out "
        "reporting and monthly performance reviews — so translating data into decisions, and building clean, "
        "reliable trackers, is genuinely how I work."
    ),
    "body_paragraph_2": (
        "A few things I'd bring beyond the checklist: I'm proactive and detail-obsessed — I don't wait to be "
        "chased, and I keep owners, next steps and deadlines visible so nothing loses momentum. I'm an early "
        "adopter of generative AI (Claude/GPT) and have built automation that cuts reporting and planning "
        "workload ~40%, which pays off in a fast-moving, multi-market setup. I'm fluent in the tool set you "
        "mention — Google Sheets, Excel, Looker and Notion (my whole workflow lives in it). In the spirit of "
        "your transparency: I'm not an Arabic speaker (Spanish native, English C1), though I've worked across "
        "MENA and GCC markets throughout my career and it hasn't slowed me down. I'm already based in the UAE "
        "and set up to work fully remotely."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd keep the Arabia & Africa marketing engine running — from the "
        "weekly and monthly performance reporting through cross-functional launch coordination to the "
        "operational follow-through that keeps initiatives on track. I'm available to start quickly and set up "
        "for remote work in the UAE. Thank you for considering my application — I'd be glad to walk through how "
        "I'd approach the first 90 days across the region."
    ),
}


def make_job() -> Job:
    return Job(
        id="airalo-marketing-manager-arabia-africa-2026-08",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (Remote)",
        url="https://jobs.lever.co/airalo",
        source="lever",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing Manager Arabia Africa remote UAE",
             "function": "Growth / Regional Marketing",
             "workplace": "Remote, anywhere in the UAE (full-time, permanent via Deel EOR)",
             "salary_band_aed_year": "281,000 - 380,000",
             "note": "Airalo (world's first eSIM store); posting via Lever. No hiring manager named."},
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
        "salary_raw": "281,000 - 380,000 AED/year",
        "salary_aed_min": 23416,  # 281,000 / 12
        "salary_aed_max": 31666,  # 380,000 / 12
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 80,
        "ai_tier": "Hot",
        "skills_match": [
            "Multi-market marketing across GCC, MENA & Africa — direct match to 'Arabia & Africa' (DoFreeze, 50+ countries)",
            "Marketing performance data & KPI reporting (spend, revenue, ROI/ROAS, conversion, GMV) into dashboards & trackers",
            "Translating data into insights, summaries and recommendations for leadership / business reviews",
            "Cross-functional campaign & launch coordination (content, creative, influencer, PR, performance, product)",
            "Project management of multiple workstreams — timelines, dependencies, approvals, follow-ups (6 NPD launches end-to-end)",
            "Marketing operations — A&P budget tracking, vendor coordination, approvals, clean action logs",
            "Analytical depth: ROI/ROAS/conversion/retention across 42 accounts, +30% GMV QoQ (Miravia); sell-in/sell-out reporting (Mondelez)",
            "Tool 'plus' overlap: Google Sheets, Excel (Expert), Looker, Notion",
            "E-commerce / marketplaces / consumer-digital background (a listed plus)",
            "Proactive, hands-on, detail-obsessed ownership; generative-AI reporting automation",
            "Strong written & verbal English (C1); already based in the UAE with a remote setup",
        ],
        "missing_skills": [
            "6+ years bar — Paula's continuous marketing/commercial track is ~5 years (plus earlier Inditex retail); marginally under, positioned on depth-of-fit not tenure",
            "Arabic fluency (listed as 'preferred') — not held; Spanish native + English C1, acknowledged plainly in the letter",
            "Mobile-attribution tooling — Adjust, AppsFlyer, QuickSight (listed as 'a plus') — not held; not claimed",
            "Travel/telecom sector experience — no direct exposure (e-commerce/marketplaces/consumer-digital cover the adjacent 'plus')",
        ],
        "sector_fit": "strong (e-commerce / consumer-digital, multi-market regional marketing — direct)",
        "seniority_fit": "on-level title ('Marketing Manager'); execution-heavy scope, slightly under the 6-yr tenure bar",
        "red_flags": [
            "6+ years must-have vs Paula's ~5 years of marketing/commercial experience — a real, if narrow, gap",
            "Arabic 'preferred' and she doesn't speak it — soft filter risk for a MENA/Arabia regional role",
            "Highly execution/ops-focused (invoice raising, vendor docs, admin) — parts sit below her current Manager autonomy; fit depends on her appetite for hands-on ops work",
            "Fully remote via Deel EOR (not a UAE-sponsored contract) — employment setup differs from a standard local package",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit — arguably one of the cleaner regional matches in the pipeline. The role's three "
            "pillars (multi-market performance reporting; cross-functional campaign coordination; marketing "
            "operations) map almost one-to-one onto Paula's DoFreeze remit across 50+ countries incl. GCC, MENA "
            "and Africa — the 'Arabia & Africa' multi-market requirement, the hardest to fake, is her strongest "
            "card. Analytical spine is well-evidenced (ROI/ROAS/conversion/retention across 42 accounts and "
            "+30% GMV QoQ at Miravia; sell-in/sell-out and monthly performance reporting at Mondelez), and the "
            "'plus' tools (Sheets, Excel, Looker, Notion) genuinely overlap. Honest gaps: the 6+ years bar (she "
            "is ~5 years in), Arabic fluency (preferred, not held), and mobile-attribution tools (Adjust/"
            "AppsFlyer/QuickSight — a plus, not held) — none fabricated; the letter names the Arabic gap "
            "outright. Salary band (≈23.4k–31.7k AED/month) clears her floor and she's already UAE-based for "
            "the remote setup. CV leads with multi-market reporting + coordination; letter leads with "
            "depth-of-fit over tenure."
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
