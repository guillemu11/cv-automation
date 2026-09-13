"""One-off: generate Paula's CV (+ cover letter) for talabat — "Sr. Specialist
Influencer Marketing" (Regional, MENA), Dubai. Job Ref JR0084766. Part of
Delivery Hero. Regional paid-influencer leadership across MENA, campaign planning
& execution, agency & stakeholder management, a big "Technology, Tools & AI"
mandate (champion AI adoption across the influencer workflow), performance
measurement/analytics, cross-functional collaboration and innovation.

Why the fit is genuinely strong (a warm, advocate-backed application):
  - INFLUENCER MARKETING is Paula's exact craft: she BUILT and scaled DoFreeze's
    creator programme from ZERO — sourcing, briefing, negotiating and managing
    25-50 creators per campaign (paid + organic), plus sampling & seeding —
    across 50+ markets, integrated into social/digital/CRM/quick-commerce.
  - AI is the rare differentiator this JD explicitly wants: it dedicates a large
    "Technology, Tools & AI" section to championing AI across creator discovery,
    content evaluation/creative scoring, predictive planning, performance
    forecasting, automated reporting, workflow automation and AI-generated
    campaign summaries. Paula is AI-first — she already builds generative-AI
    (Claude/GPT) automation for exactly these steps. Very few influencer
    marketers are also AI builders.
  - Multi-market (50+), cross-functional campaign delivery, performance/ROI
    measurement and creator/agency coordination — all genuine strengths.
  - Warm advocate: Álvaro Martínez (Regional Sr. Director, talabat) explicitly
    encouraged her to apply and to "forget the 7 years, bring the hunger".

HONEST gaps (NOT fabricated):
  - **7+ years** required; Paula is at ~5 (from Mondelez 2021). This is THE gap —
    the one the internal advocate told her to not be put off by. Documents do not
    invent tenure; they lead with what she has built and its velocity/impact.
  - Scale of REGIONAL AGENCY management: her influencer work is more in-house /
    creator-led than large multi-market agency-network management. Transferable
    (briefing, governance, KPIs, coordination); framed honestly, not overstated.
  - "Sr. Specialist" sits roughly at/just below her Manager level — fine; framed
    as genuine interest in owning influencer at regional scale in a top platform.
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, lands the package under
output/2026-08-29/, and drops a short-named 'Paula De Francisco - CV.pdf' copy.
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

COMPANY = "talabat"
TITLE = "Sr. Specialist Influencer Marketing"
DATE_FOLDER = "2026-08-29"

CONTACT = None  # No named hiring manager in posting — "Hiring Manager".

JOB_DESCRIPTION = """\
Sr. Specialist Influencer Marketing — talabat (Delivery Hero), Dubai. Regional
(MENA) influencer marketing role. Job Ref JR0084766.

Regional Influencer Marketing Leadership: lead paid influencer marketing across
all talabat MENA markets; build a regional operating model balancing local
flexibility with regional governance; drive consistency in planning, execution,
reporting and measurement; consolidate initiatives, negotiate efficiencies and
leverage regional scale; build annual roadmaps.

Campaign Planning & Execution: partner with local marketing managers to develop
influencer campaigns aligned with brand, commercial and seasonal objectives;
coordinate regional and local campaigns from planning through execution and
post-campaign evaluation; integrate influencer activity into broader campaigns
across digital, social, offline and CRM; partner with agencies to identify the
most relevant creators and content strategies; deliver on time, on budget, to a
high standard.

Agency & Stakeholder Management: manage regional influencer agencies and oversee
local agency relationships; establish governance, KPIs and service standards;
build relationships across Marketing, Brand, Digital, Media, Creative, Legal,
Procurement and Finance; act as regional subject-matter expert.

Technology, Tools & AI: own talabat's influencer marketing technology ecosystem;
lead implementation, optimization and adoption of influencer platforms; drive
full utilization across creator discovery, audience validation, brand-fit
analysis, fraud detection, campaign management, contract management, performance
tracking, reporting and benchmarking. Champion AI adoption across influencer
marketing — AI-assisted creator discovery, content evaluation and creative
scoring, audience insights, predictive campaign planning, performance
forecasting, automated reporting, workflow automation, and AI-generated campaign
summaries and recommendations; continuously automate manual processes.

Performance Measurement & Analytics: develop a robust measurement framework;
create regional dashboards and standardized reporting; track reach, engagement,
video completion, earned media value, creator effectiveness, cost efficiency and
business impact; deliver performance reviews with recommendations; build
benchmark databases; use data to improve performance and ROI.

Cross-functional Collaboration: work with Online Branding to integrate influencer
into digital media plans; coordinate timing, audience, creative and paid
amplification; partner with Creative to improve creator content quality.

Innovation: stay ahead of creator trends, platforms, AI capabilities and
influencer technologies; pilot new formats, capabilities and measurement
solutions; develop paid-partnership frameworks; foster test-and-learn.

What we're looking for: Bachelor's in Marketing, Communications, Business, Digital
Media or related; 7+ years in influencer marketing, digital marketing, social
media or integrated marketing; experience managing regional influencer programs
across multiple markets; experience with leading influencer agencies and creator
ecosystems; experience in matrix organizations managing multiple stakeholders.
"""

ATS = [
    "influencer marketing", "paid influencer", "creator marketing", "creators",
    "creator discovery", "creator ecosystem", "content strategy", "UGC",
    "campaign planning", "campaign execution", "post-campaign evaluation",
    "agency management", "stakeholder management", "matrix organization",
    "regional", "MENA", "multi-market", "governance", "KPIs", "roadmap",
    "social media", "Instagram", "TikTok", "digital marketing", "CRM", "EDM",
    "paid media", "Meta Ads", "Google Ads", "paid amplification",
    "technology ecosystem", "AI", "generative AI", "AI-assisted creator discovery",
    "content evaluation", "creative scoring", "predictive campaign planning",
    "performance forecasting", "automated reporting", "workflow automation",
    "campaign summaries", "measurement framework", "dashboards", "reach",
    "engagement", "earned media value", "EMV", "creator effectiveness",
    "cost efficiency", "ROI", "ROAS", "benchmarking", "test-and-learn",
    "sampling", "seeding", "brand", "go-to-market", "budget", "Dubai", "UAE",
    "quick-commerce", "Talabat", "Noon", "Careem", "Deliveroo",
]

CV_CONTENT = {
    "headline": (
        "Influencer Marketing & Brand Manager · AI-Powered Creator Programs (0→50 creators/campaign, paid + organic) · "
        "Multi-Market MENA/GCC · Sampling & Seeding · Performance, EMV & ROI · Dubai-based"
    ),
    "professional_summary": (
        "Dubai-based influencer & brand marketer who built and scaled a creator programme from zero to 25-50 "
        "influencers per campaign (paid + organic) across 50+ markets — and does it AI-first, using generative AI "
        "(Claude/GPT) for creator discovery, content evaluation, campaign planning and automated reporting. Combines "
        "hands-on influencer execution with brand building, cross-functional campaign delivery, agency/creator "
        "coordination and performance/ROI measurement. Brings real hunger, ownership and a test-and-learn drive."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Built and scaled the influencer marketing programme from ZERO — sourcing, briefing, negotiating and managing 25-50 creators per campaign (paid + organic), plus product sampling & seeding — driving awareness, UGC and measurable sell-out across 50+ markets",
                "AI-first influencer workflow: use generative AI (Claude/GPT) for creator discovery & shortlisting, content evaluation, campaign planning and automated reporting/summaries — cutting ~40% of manual work and speeding briefs, recaps and performance reviews",
                "Integrate influencer activity into broader campaigns across social (Instagram/TikTok), digital, EDM/CRM and quick-commerce (Talabat, Noon, Careem, Deliveroo); run paid media (Meta & Google Ads) and track reach, engagement, EMV, ROI/ROAS",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees",
            "bullets": [
                "Led creator- and social-driven brand projects (Beauty Club, Hot on Social) across 42 accounts, +30% GMV QoQ — building visibility, UGC and promotions, reporting to the CEO",
                "Coordinated multi-stakeholder relationships and creator/agency activations across beauty, fragrance and fashion — planning, execution and post-campaign evaluation",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app / food delivery | €500M+ revenue",
            "bullets": [
                "Ran bespoke partner marketing activations and campaigns cross-functionally (marketing, ops, logistics) on a quick-commerce super-app, on time and on budget in a fast-paced market",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG multinational | €36B revenue | 90K+ employees",
            "bullets": [
                "Global-FMCG grounding — campaign/promo effectiveness analysis and performance reporting; supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (
        "influencer marketing (paid + organic), creator sourcing / briefing / negotiation, sampling & seeding, "
        "UGC & content strategy, brand building, multi-market campaign planning & execution, go-to-market"
    ),
    "skills_ecommerce": (
        "social (Instagram, TikTok, Pinterest), paid media & amplification (Meta & Google Ads), EDM/CRM, "
        "quick-commerce (Talabat, Noon, Careem, Deliveroo)"
    ),
    "skills_commercial": (
        "agency & creator-ecosystem management, stakeholder management (matrix orgs), cross-functional coordination, "
        "budget management, regional / multi-market governance"
    ),
    "skills_data": (
        "AI-assisted creator discovery, content scoring & automated reporting (Claude/GPT); influencer KPIs — reach, "
        "engagement, EMV, creator effectiveness, cost efficiency; dashboards, ROI/ROAS, Power BI"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Meta Ads, Google Ads, Instagram/TikTok, Shopify, Power BI, "
        "Canva, Adobe, MS Office — Expert"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Influencer marketing at regional scale, run AI-first — that's the exact intersection I work at, so talabat's "
        "Sr. Specialist role reads like it was written for how I like to build. I'm a Dubai-based influencer & brand "
        "marketer who built a creator programme from zero and runs it with a generative-AI toolkit, and I'd bring "
        "genuine hunger and ownership to owning influencer across MENA."
    ),
    "body_paragraph_1": (
        "The core of the role is what I already do. At DoFreeze I built the influencer programme from scratch — "
        "sourcing, briefing, negotiating and managing 25-50 creators per campaign (paid + organic), plus sampling and "
        "seeding — and I run it across 50+ markets, integrated into social (Instagram/TikTok), digital, CRM and "
        "quick-commerce, with paid amplification on Meta and Google Ads. I plan and execute end-to-end, coordinate "
        "creators and agencies, deliver on time and on budget, and measure what matters — reach, engagement, EMV, "
        "creator effectiveness, cost efficiency and ROI/ROAS — feeding it back into the next plan. I'm used to "
        "juggling multiple stakeholders and markets at once and keeping activity consistent and on-brand."
    ),
    "body_paragraph_2": (
        "Where I'd add something rare is the AI mandate in this role. I'm AI-first: I already use generative AI "
        "(Claude/GPT) for creator discovery and shortlisting, content evaluation, campaign planning and automated "
        "reporting and summaries — cutting ~40% of the manual work and speeding briefs, recaps and reviews. That's "
        "precisely the 'champion AI adoption across the influencer workflow' brief, from someone who builds these "
        "systems rather than just talks about them. I'll be straight that my experience is a few years rather than "
        "seven, but I've built and scaled fast, I bring real drive and a test-and-learn mindset, and I'm hungry to "
        "grow this at talabat's scale."
    ),
    "closing_paragraph": (
        "I'd love to help talabat set the regional standard for AI-powered influencer marketing, and I can walk "
        "through creator-programme, campaign and AI-automation case studies from my current work. I'm already based "
        "in Dubai and ready to start fast. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="talabat-sr-specialist-influencer-marketing-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://careers.talabat.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Sr Specialist Influencer Marketing talabat MENA AI creators",
             "function": "Influencer marketing (regional/MENA — creator programs, agency mgmt, AI-powered workflow, measurement)",
             "sector": "Quick-commerce / food delivery (talabat — Delivery Hero)",
             "ref": "JR0084766",
             "note": "STRONG craft fit (influencer marketing built 0→25-50 creators paid+organic, sampling/seeding, "
                     "50+ markets) + RARE AI edge that the JD explicitly wants (generative-AI creator discovery, "
                     "content scoring, predictive planning, automated reporting). Gap: 7+ yrs required, she is ~5 — "
                     "the internal advocate (Álvaro Martínez, Regional Sr. Director) told her to apply anyway and "
                     "'bring the hunger'. Also: regional agency-network scale is a stretch (more in-house/creator-led "
                     "for her, transferable). No 'own visa / no sponsorship' claim."},
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
        "ai_score": 74,
        "ai_tier": "Hot",
        "skills_match": [
            "Influencer marketing is her exact craft: built DoFreeze's creator programme from ZERO — 25-50 creators/campaign (paid + organic), sampling & seeding — across 50+ markets, integrated into social/digital/CRM/quick-commerce",
            "RARE AI edge the JD explicitly wants: AI-first, already uses generative AI (Claude/GPT) for creator discovery, content evaluation, planning and automated reporting — the literal 'Technology, Tools & AI' mandate",
            "Multi-market campaign planning & execution + creator/agency coordination + post-campaign evaluation; paid amplification (Meta & Google Ads)",
            "Performance measurement: reach, engagement, EMV, creator effectiveness, cost efficiency, ROI/ROAS; dashboards & Power BI",
            "Cross-functional / multi-stakeholder working across brand, digital, creative; MENA / Dubai-based",
            "Warm internal advocate: Álvaro Martínez (Regional Sr. Director, talabat) encouraged the application",
        ],
        "missing_skills": [
            "7+ years required; Paula is at ~5 — THE gap. Internal advocate explicitly said to apply anyway ('forget the 7 years, bring the hunger'). Documents do not fabricate tenure; they lead with what she built and its velocity",
            "Regional AGENCY-NETWORK management at scale is a stretch — her influencer work is more in-house/creator-led (transferable: briefing, governance, KPIs, coordination)",
            "'Sr. Specialist' sits ~at/just below her Manager level (fine; framed as owning influencer at regional scale)",
        ],
        "sector_fit": "excellent — quick-commerce / food delivery (talabat); she is already a talabat partner from the brand side",
        "seniority_fit": "in-band; ~5 yrs vs 7+ asked (the advocate-dismissed gap). Strong craft, framed on impact + hunger",
        "red_flags": [
            "7+ yrs is an explicit requirement she doesn't fully meet (~5). Mitigated by a warm internal advocate who urged applying; lead the pitch on influencer craft + AI edge + drive.",
            "Regional agency-network scale is larger than her in-house/creator-led experience — transferable but honest to flag.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "One of Paula's strongest talabat matches on craft, and warm: it pairs her single best specialism "
            "(influencer marketing — she built a 0→25-50-creator programme, paid + organic, sampling & seeding, across "
            "50+ markets) with the exact AI mandate the JD spends a whole section on (champion AI across creator "
            "discovery, content/creative scoring, predictive planning, performance forecasting, automated reporting, "
            "workflow automation). Paula is genuinely AI-first and already builds these generative-AI workflows — a "
            "rare influencer+AI combination. She also brings multi-market planning/execution, creator & agency "
            "coordination, cross-functional/stakeholder working and performance/ROI measurement (reach, engagement, "
            "EMV, ROAS). The honest blocker is tenure: 7+ years required vs her ~5 — precisely the gap her internal "
            "advocate (Álvaro Martínez, Regional Sr. Director) told her to disregard and apply with hunger. Regional "
            "agency-network scale is a stretch (more in-house/creator-led for her). Documents never fabricate years or "
            "agency scale; they lead with what she has built, its velocity and the AI edge. Apply, paired with the "
            "warm inbound. No 'own visa / no sponsorship' claim."
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

    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    src = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if src.exists():
        shutil.copy(str(src), str(short))
        print("OK_SHORT", short)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
