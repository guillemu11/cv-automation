"""One-off: generate Paula's CV + cover letter for AA Sends
"Klaviyo Account Manager / Email Strategist For E-commerce Brands"
(remote, UAE — email/SMS/WhatsApp retention agency across MENA).

Why this is an honest, decent fit:
  - Account management is Paula's spine: 42 key accounts at Alibaba's Miravia
    (+30% GMV QoQ, main point of contact, weekly reporting) and XL accounts at
    Glovo — exactly the "own the client relationship end-to-end, keep accounts
    retained, performing and happy" mission of this role.
  - Real e-commerce / retention execution: she owns a Shopify DTC store
    end-to-end (catalogue, CRO, promotions and email/EDM), plans campaign
    calendars, A/B-tests creative and reads open/click/conversion data.
  - AI-first operator: builds generative-AI automation for campaign planning,
    content and reporting (~40% manual workload cut) — the speed an agency pod
    runs on.

Honest positioning (NO fabrication):
  - Paula does NOT have dedicated Klaviyo / email-agency tenure. Her email work
    has run through Shopify + EDM inside a broader omnichannel remit, not as a
    pure-play Klaviyo email strategist. Framed truthfully as directly
    transferable — platform-agnostic, ramps on Klaviyo fast — and the CL states
    the gap head-on. NO invented Klaviyo flows/SMS/WhatsApp agency claims.
  - Role is remote via an agency, so visa is a non-issue; per standing rule we
    make NO "no sponsorship needed" claim and simply note remote-ready / based
    in Dubai.
  - Application is via a Typeform (no email / named contact), so there is NO
    outreach email and the letter stays addressed to "Hiring Manager".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-18/.
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

COMPANY = "AA Sends"
TITLE = "Klaviyo Account Manager - Email Strategist"
DATE_FOLDER = "2026-08-18"

# Applications go only through the Typeform; no hiring manager named.
CONTACT = None

JOB_DESCRIPTION = """\
Klaviyo Account Manager / Email Strategist For E-commerce Brands — AA Sends.
United Arab Emirates (Remote), full-time.

ABOUT AA Sends: a leading email, SMS and WhatsApp marketing agency in the MENA
region, partnering with the biggest and fastest-growing e-commerce brands in the
Gulf. We run retention as a full revenue channel — strategy, copy, design and
Klaviyo execution end to end — measured by the revenue we add without a single
dollar of extra ad spend.

MISSION: Account Managers own their client relationships end to end — strategy,
communication, execution and results. You are the bridge between our internal
team and each brand we serve, and your job is to keep every account retained,
performing and happy.

CORE RESPONSIBILITIES:
- Strategy & Execution: own the full email marketing strategy for each account —
  flows, campaigns and any initiative that moves revenue.
- Flows: build and maintain every automated flow, with consistent A/B testing and
  strategic updates.
- Campaigns: plan and execute weekly campaigns, from calendar creation through
  final approval and send.
- Pop-Up Forms: build and continuously optimise high-converting pop-ups through
  A/B testing and performance tracking.
- Client Communication: act as the main client contact — regular updates, leading
  calls, and fast, clear responses.
- Client Revisions: handle client-requested email revisions yourself.
- Team Oversight: lead your pod with daily check-ins and full accountability for
  quality and deadlines.

CADENCE: respond to client/team messages within 60 minutes; acknowledge revisions
within 2 hours and complete within 24; ensure every email is error-free, approved
and scheduled; send a Monday status and performance report per client; run a
weekly Klaviyo audit; keep 3+ A/B tests live per account; get calendars approved
two weeks ahead; deliver a monthly performance deck.

COMPENSATION: competitive base plus recurring performance bonuses tied to the
revenue you generate and the clients you keep. Top performers move into Senior
Account Manager and lead their own team of AMs.

Remote job from anywhere. Apply via the application form (Typeform); applications
sent anywhere else won't be considered.
"""

ATS = [
    "Klaviyo", "Account Manager", "Email Strategist", "email marketing",
    "email marketing strategy", "flows", "automated flows", "campaigns",
    "weekly campaigns", "campaign calendar", "A/B testing", "pop-up forms",
    "pop-ups", "high-converting", "conversion", "retention", "retention marketing",
    "lifecycle marketing", "e-commerce", "e-commerce brands", "DTC", "Shopify",
    "SMS", "WhatsApp", "client relationships", "client communication",
    "main client contact", "account management", "account retention",
    "performance report", "performance tracking", "reporting", "status report",
    "monthly performance deck", "revenue", "revenue channel", "copy", "design",
    "pod", "daily check-ins", "deadlines", "MENA", "Gulf", "GCC", "UAE",
    "remote", "fluent English",
]

CV_CONTENT = {
    "headline": (
        "E-Commerce & Retention Marketing · Email / Lifecycle · Account Management · "
        "Shopify DTC · Campaigns & A/B Testing"
    ),
    "professional_summary": (
        "E-commerce and retention-minded marketer with 4+ years owning client relationships and driving "
        "revenue across Beauty, FMCG and DTC e-commerce. I run a Shopify DTC store end-to-end — catalogue, "
        "CRO, promotions and email/EDM campaigns — planning campaign calendars, A/B-testing creative and "
        "messaging, and reading open, click and conversion data to decide what ships next. Account management "
        "is my spine: at Alibaba's Miravia I owned 42 key accounts as the main point of contact (+30% GMV QoQ), "
        "and at Glovo I managed XL accounts end-to-end — so weekly reporting, fast responses and keeping "
        "accounts retained, performing and happy are second nature. I'm an AI-first operator who builds "
        "generative-AI automation for campaign planning, content and reporting (~40% manual workload cut) — "
        "the kind of speed an agency pod runs on. Platform-agnostic and quick to ramp on Klaviyo. Fluent "
        "English, remote-ready, already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own a Shopify DTC e-commerce store end-to-end — catalogue, UX, collections, discounts and checkout — lifting conversion rate (CRO) and average order value through data-led merchandising and on-site optimisation",
                "Plan and run email/EDM and social campaigns across weekly calendars — building audiences, A/B testing creative and messaging, and analysing open, click and conversion performance to decide what ships next",
                "Build AI-powered marketing automation (Claude / generative AI) that plans campaigns, produces content and copy, and generates KPI reporting — cutting manual workload ~40% and accelerating turnaround",
                "Optimise on-site conversion elements — promotional mechanics, offers, discounts and landing pages — through continuous testing and performance tracking",
                "Coordinate campaigns from brief through final approval and send across 50+ markets, leading cross-functional teams to hit quality standards and deadlines",
                "Own influencer and seeding programmes (25–50 creators per campaign), driving UGC, awareness and measurable sell-out",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned 42 key accounts end-to-end as the main point of contact — building strong, long-term client relationships and driving +30% GMV growth QoQ through tailored plans, pricing and targeted promotions",
                "Owned the Flash Sales channel (Beauty, Fashion & Home) — planning weekly promotional calendars and campaigns and reporting performance directly to the CEO",
                "Sent regular status and performance updates to accounts and stakeholders, turning ROI, conversion and retention analysis into clear next actions",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via strategic promotions and trend-driven assortment",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic XL key accounts as the primary contact — daily communication, joint planning and fast turnaround on client requests",
                "Grew account revenue through data-led planning and bespoke marketing activations; negotiated and closed high-impact commercial deals",
                "Led cross-functional teams (marketing, logistics, support) to deliver campaigns on deadline and increase order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, feeding campaign and commercial planning",
                "Built management-ready performance reports, translating campaign and market data into actionable recommendations",
            ],
        },
    ],
    "skills_ecommerce": (
        "email marketing / EDM, retention & lifecycle marketing, Shopify DTC store management, campaign "
        "calendars, A/B testing, conversion rate optimisation (CRO), on-site conversion & pop-up optimisation, "
        "landing pages, marketing automation, Meta Ads, Google Ads, quick-commerce (Noon, Talabat, Careem, "
        "Deliveroo)"
    ),
    "skills_commercial": (
        "key account management, client relationship ownership, client communication & weekly reporting, "
        "account retention, campaign planning, promotions & offers, pricing strategy, negotiation, "
        "cross-functional coordination"
    ),
    "skills_data": (
        "A/B testing, open/click/conversion analysis, KPI tracking & reporting, performance decks, ROI/ROAS, "
        "sell-in/sell-out, forecasting, Power BI, Salesforce, advanced Excel"
    ),
    "skills_brand": (
        "campaign strategy, email & lifecycle campaigns, copy & content briefing, go-to-market, promotional "
        "mechanics, influencer & UGC, AI-assisted content & planning"
    ),
    "skills_tools": (
        "Shopify, Meta Ads Manager, Google Ads, Generative AI (Claude, ChatGPT), Salesforce, Power BI, "
        "Microsoft Excel (Advanced), PowerPoint (Advanced), Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Retention is where e-commerce revenue is quietly won or lost, so an agency that runs it as a full "
        "revenue channel — better email, SMS and flows, no extra ad spend — is exactly the kind of work I want "
        "to own. I'm applying for the Klaviyo Account Manager / Email Strategist role because it sits right at "
        "the intersection of my two strongest muscles: owning client relationships end to end, and driving "
        "e-commerce performance through campaigns, flows and relentless A/B testing."
    ),
    "body_paragraph_1": (
        "Account management is the spine of my career. At Alibaba's Miravia I owned 42 key accounts as their "
        "main point of contact — building long-term relationships, sending weekly status and performance "
        "reports, and growing GMV +30% QoQ through tailored plans, pricing and targeted promotions. At Glovo I "
        "managed XL accounts end to end with daily communication and fast turnaround on every request. Keeping "
        "accounts retained, performing and happy — with clear reporting and quick, honest responses — is "
        "already how I work, so your 60-minute response and Monday-report cadence feels like home rather than a "
        "stretch."
    ),
    "body_paragraph_2": (
        "On execution, I own a Shopify DTC store end to end — catalogue, CRO, promotions and email/EDM "
        "campaigns — and I plan campaign calendars, A/B-test creative and messaging, optimise on-site "
        "conversion, and read open, click and conversion data to decide what ships next. I'm also an AI-first "
        "operator: I've built generative-AI automation that plans campaigns, produces copy and content, and "
        "generates reporting, cutting ~40% of manual workload — the kind of speed a pod runs on. I'll be candid "
        "that my hands-on email work has run through Shopify and EDM rather than Klaviyo specifically, but I "
        "already understand flows, campaigns, pop-ups and pod-level reporting, I'm platform-agnostic, and I ramp "
        "on new tools fast — I'd expect to be productive in Klaviyo within days, not weeks."
    ),
    "closing_paragraph": (
        "I'd love to bring this mix of end-to-end account ownership, e-commerce retention execution and "
        "AI-driven speed to AA Sends and the brands you serve. I'm available immediately, comfortable working "
        "remotely across MENA hours, and I'm applying through the form as requested. Thank you for your "
        "consideration — I'd welcome the chance to show how I'd own and grow a pod of retention accounts."
    ),
}


def make_job() -> Job:
    return Job(
        id="aa-sends-klaviyo-am-email-strategist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (Remote)",
        url="https://form.typeform.com/to/kq6oiutC",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Klaviyo Account Manager Email Strategist e-commerce",
             "function": "Marketing / Account Management", "workplace": "Remote",
             "note": "Apply ONLY via Typeform: https://form.typeform.com/to/kq6oiutC"},
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
        "salary_raw": "Competitive base + recurring performance bonuses",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 70,
        "ai_tier": "Warm",
        "skills_match": [
            "Client relationship ownership end-to-end (main point of contact)",
            "Key Account Management (42 accounts @ Miravia, +30% GMV QoQ)",
            "Account retention & weekly performance reporting",
            "E-commerce / DTC execution — Shopify store owned end-to-end",
            "Email / EDM campaigns + campaign calendars",
            "A/B testing & conversion optimisation (CRO)",
            "On-site conversion / pop-up & offer optimisation",
            "AI-first automation (campaign planning, content, reporting — ~40% workload cut)",
            "Cross-functional / pod coordination to deadlines",
            "Fluent English; remote-ready; based in Dubai (MENA hours)",
        ],
        "missing_skills": [
            "Dedicated Klaviyo tenure (email work has run through Shopify + EDM, not Klaviyo specifically — positioned as transferable, ramps fast)",
            "Pure-play email/SMS/WhatsApp agency background (her email sits inside a broader omnichannel remit)",
            "SMS / WhatsApp flow building at agency scale (adjacent, not held)",
        ],
        "sector_fit": "good (e-commerce / DTC retention — adjacent to her Shopify + account-management core)",
        "seniority_fit": "on-band to slightly under (she's a Brand & Marketing Manager; this is an AM/specialist agency role)",
        "red_flags": [
            "Role is a Klaviyo email-agency specialist; Paula's email is Shopify/EDM inside a broader remit — positioned truthfully as transferable, no invented Klaviyo claims",
            "Remote agency, commission-heavy comp (competitive base + revenue-tied bonuses) — below her manager remit; apply only if the retention-specialist direction appeals",
            "Apply ONLY via Typeform (https://form.typeform.com/to/kq6oiutC) — no email outreach; CV + CL are for attaching/reference",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Decent, honest fit on the account-management + e-commerce axes. The role's core mission — own "
            "client relationships end to end, keep accounts retained/performing/happy, weekly reporting, "
            "plan and A/B-test campaigns and flows — maps directly onto Paula's spine: 42 key accounts at "
            "Miravia (+30% GMV QoQ, main point of contact), XL accounts at Glovo, and hands-on Shopify DTC "
            "ownership with email/EDM, CRO and campaign calendars today at DoFreeze. Her AI-first automation "
            "is a genuine edge for an agency optimising pod throughput. Honest gaps: she has no dedicated "
            "Klaviyo/email-agency tenure (her email runs through Shopify + EDM inside a broader omnichannel "
            "remit) and no agency-scale SMS/WhatsApp flow building — positioned truthfully as directly "
            "transferable with a fast Klaviyo ramp, no fabrication. Note it's a remote, commission-heavy "
            "specialist AM role (a step sideways/down from her manager remit), and applications go ONLY "
            "through the Typeform, so there is no outreach email — the CV + CL are for the form/attachment."
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
