"""One-off: generate Paula's CV (+ cover letter) for talabat — "Specialist,
Performance Marketing – instashop" (Delivery Hero q-commerce), Dubai.

Why this is a strong, honest fit:
  - talabat OWNS instashop (both under Delivery Hero). Paula integrates and
    grows brands on Talabat, Noon, Careem and Deliveroo TODAY at DoFreeze, and
    ran key accounts at Glovo — she is a genuine q-commerce INSIDER, which the
    JD lists as a "strong plus" (q-commerce / food delivery / e-commerce).
  - The role is explicitly AI-FIRST ("embed AI into your workflow", prompt
    engineering, ChatGPT/Claude/Gemini for reporting/analysis/brief writing/
    automation). This is Paula's signature, rare edge: she BUILT a generative-AI
    system (Claude/GPT) automating reporting, analysis, campaign planning and
    content — cutting manual workload ~40%. Arguably her single strongest hook.
  - Campaign execution & analysis: she plans and optimises paid media on Meta
    (Facebook & Instagram) and Google Ads — audience building, creative A/B
    testing, budget management and continuous ROI/ROAS optimisation — and turns
    full-funnel data (traffic, conversion, retention, ROAS) into decisions.
  - Multi-market (UAE & Egypt): she manages campaigns and brands across GCC/MENA
    and 50+ countries; comfortable with senior-stakeholder reporting.
  - Requirements met: Business Administration degree (CUNEF); 4+ yrs; strong
    analytical rigour (ROI/ROAS/conversion/retention); fast-paced, ownership-led.
  - Nice-to-have: brand + performance simultaneously (she does both); briefing
    creative teams and structured feedback on short-form video (she runs 25-50
    creators/campaign, UGC, Reels/TikTok content); hands-on AI tools. All real.

Honest gaps (DISCLOSED in the cover letter — NOT fabricated):
  - TikTok ADS depth: her paid platform strength is Meta (+ Google). TikTok is
    more content/short-form + influencer for her than deep TikTok Ads Manager.
    Framed as core-Meta + fast TikTok-Ads ramp; NOT claimed as expert.
  - MMPs (Adjust / AppsFlyer): she has NOT used these hands-on. She understands
    attribution/measurement (last-touch vs incrementality, ROI/ROAS/CAC) at the
    concept level with deep analytics chops — MMP tooling is a fast ramp.
    NEVER listed among her tools; disclosed honestly.
  - "2 years focused on paid social": her paid media is hands-on but sits inside
    broader brand/commercial/e-commerce roles rather than a pure paid-social
    specialist track. Positioned truthfully.
  - Seniority: "Specialist" (IC) sits a notch below her current Brand & Marketing
    Manager level — framed as genuine enthusiasm to go deep on performance +
    AI at talabat's scale, not a step-down. (Flagged to Paula/Guille separately.)
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-25/.
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
TITLE = "Specialist, Performance Marketing - instashop"
DATE_FOLDER = "2026-08-25"

CONTACT = None  # Reports to Head of Marketing at instashop; no name in posting — "Hiring Manager".

JOB_DESCRIPTION = """\
Specialist, Performance Marketing — instashop (talabat / Delivery Hero), Dubai.
instashop is the leading online local marketplace in the UAE and Egypt, part of
the Delivery Hero family. This is an individual-contributor role on the
Performance Marketing team: you own the day-to-day execution of paid campaigns
across channels, manage budgets, and drive customer acquisition. You work with
the Head of Marketing at instashop on Marcomms strategy, incentive tracking and
business performance analysis, with a dotted line to Talabat's performance
marketing lead. Hybrid role: part campaign executor, part strategic analyst.
The team runs lean — embed AI into your workflow and cut manual steps.

Campaign Execution: own end-to-end campaign setup, bidding and optimisation
across Meta, TikTok and other paid channels; take creatives live, test formats
and iterate on performance data; manage daily budget allocation and pacing to
hit CAC targets; monitor campaign health and flag issues early.

Performance Analysis: analyse campaign performance full-funnel (impression to
conversion); build and maintain performance reports for the Head of Marketing
and senior stakeholders across UAE & Egypt; track incentive performance and
contribute to business reviews; identify CAC efficiency opportunities with
data-backed recommendations.

Experimentation: design and run A/B tests on creatives, audiences, bids and
landing experiences; document hypotheses, results and learnings; propose new
experiments from platform signals and competitive benchmarks.

Strategy & Marcomms: work with the Head of Marketing on marcomms planning and
calendar; support incentive design and tracking; contribute to quarterly
planning with performance data and channel insights.

Qualifications: strong Meta Ads Manager knowledge (campaign structures, bidding,
Advantage+, creative); working knowledge of TikTok Ads; familiarity with
short-form content in paid vs organic; working knowledge of Google, Apple Ads,
Snapchat; understanding of attribution & MMP mechanics (Adjust, AppsFlyer).
AI-first way of working (AI tools for reporting, analysis, brief writing,
automation; prompt engineering). Analytical rigour (CAC, LTV, ROAS, CPM;
incrementality vs last-touch). Speed and ownership. 3-5 years hands-on
performance marketing, at least 2 years focused on paid social; budget
management across channels and markets; proven Meta & TikTok track record;
MMP experience; q-commerce / food delivery / e-commerce exposure a strong plus;
Bachelor's in Marketing, Business or related.

Nice to have: brand + performance objectives simultaneously; briefing creative
teams and structured feedback on short-form video; hands-on use of AI tools in
marketing (ChatGPT, Claude, Gemini).
"""

ATS = [
    "performance marketing", "paid social", "paid media", "campaign execution",
    "campaign setup", "bidding", "optimisation", "Meta Ads", "Meta Ads Manager",
    "Facebook Ads", "Instagram Ads", "Advantage+", "TikTok Ads", "Google Ads",
    "Apple Ads", "Snapchat", "budget allocation", "pacing", "customer acquisition",
    "CAC", "CAC efficiency", "LTV", "ROAS", "CPM", "ROI", "conversion",
    "full-funnel", "impression to conversion", "attribution", "MMP", "Adjust",
    "AppsFlyer", "incrementality", "last-touch", "A/B testing", "experimentation",
    "creative testing", "short-form content", "Reels", "TikTok", "UGC",
    "performance reports", "performance analysis", "business reviews",
    "incentive tracking", "marcomms", "quarterly planning", "AI-first",
    "AI automation", "prompt engineering", "generative AI", "Claude", "ChatGPT",
    "q-commerce", "quick-commerce", "food delivery", "e-commerce", "marketplace",
    "instashop", "talabat", "Noon", "Careem", "Deliveroo", "Delivery Hero",
    "UAE", "Egypt", "Dubai", "multi-market", "stakeholder reporting", "ownership",
]

CV_CONTENT = {
    "headline": (
        "Performance & Growth Marketing · Paid Social (Meta) & Google Ads · AI-First Marketer (Claude/GPT "
        "Automation) · Full-Funnel Analytics (ROI/ROAS/CAC) · UAE Quick-Commerce Insider (Talabat, Noon, Careem, Deliveroo)"
    ),
    "professional_summary": (
        "Performance-minded brand and growth marketer with 4+ years across FMCG, e-commerce and quick-commerce, "
        "now running paid media and AI-powered marketing automation from Dubai. I plan and optimise paid campaigns "
        "on Meta (Facebook & Instagram) and Google Ads — audience building, creative A/B testing, budget management "
        "and continuous ROI/ROAS optimisation — and I turn full-funnel data (traffic, conversion, retention, ROAS) "
        "into decisions. My rare edge is being genuinely AI-first: I built a generative-AI system (Claude/GPT) that "
        "automates reporting, analysis, brief writing and campaign planning, cutting manual workload ~40% — exactly "
        "the lean, automate-everything way of working this team wants. And I know q-commerce from the inside, "
        "integrating and growing brands on Talabat, Noon, Careem and Deliveroo today, after running key accounts at "
        "Glovo. Business Administration graduate (CUNEF), bilingual (ES native / EN C1), fast-paced and ownership-driven."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Brands: Befit, Eurocake, Flair | UAE quick-commerce + 50+ countries",
            "bullets": [
                "Plan, set up and optimise paid campaigns on Meta Ads (Facebook & Instagram) and Google Ads — audience building, creative A/B testing, budget allocation and bid/pacing management — analysing ROI and ROAS to drive continuous performance improvement",
                "Built an AI-first marketing system (Claude / generative AI) that automates performance reporting, analysis, brief writing and campaign planning — cutting manual workload ~40% and letting the team run lean, exactly the AI-embedded way of working this role calls for",
                "Grow brands across UAE quick-commerce (Talabat, Noon, Careem, Deliveroo) — driving customer acquisition and sell-out via listings, promotional mechanics and retail-media activation, giving me an insider view of q-commerce marketing in this exact market",
                "Run full-funnel performance analysis (traffic, conversion, retention, ROI/ROAS) and build KPI reports and business reviews for senior stakeholders across GCC, MENA and 50+ markets",
                "Own creative and short-form video: brief and manage 25–50 creators per campaign (UGC, Instagram Reels, TikTok content) and give structured feedback on assets — informing paid-social creative testing and iteration",
                "Design and run A/B tests on audiences, creatives and promotions, documenting hypotheses and learnings to compound performance over time",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees",
            "bullets": [
                "Continuously analysed conversion, traffic, retention, ROI and ROAS across the funnel to optimise channel performance and improve forecasting accuracy — the strategic-analyst half of a performance role",
                "Owned 42 brand accounts and grew GMV +30% QoQ through pricing, assortment optimisation and targeted promotions and campaigns that drove acquisition and conversion",
                "Owned the Flash Sales channel for Beauty, Fashion & Home end-to-end — running promotions and merchandising to lift traffic and conversion, reporting directly to the CEO against P&L targets",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via data-driven promotions and trend-led selection",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Drove GMV growth and customer acquisition for strategic accounts on a quick-commerce super-app through data-led planning, promotions and bespoke marketing activations",
                "Coordinated cross-functionally across marketing, operations and logistics to deliver campaigns and increase order volume",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both Glovo and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out analysis and evaluated promotional effectiveness for the chocolate category, building performance reports for the commercial team",
                "Identified growth opportunities and contributed to successful NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (
        "performance & growth marketing, paid media planning, customer acquisition, A/B testing & experimentation, "
        "creative testing & short-form video briefing, campaign optimisation, brand + performance, go-to-market"
    ),
    "skills_ecommerce": (
        "Meta Ads (Facebook & Instagram Ads), Google Ads, paid social, campaign setup & optimisation, "
        "quick-commerce (Talabat, Noon, Careem, Deliveroo), short-form content (Reels, TikTok), "
        "conversion rate optimisation (CRO), Shopify, EDM, marketing automation"
    ),
    "skills_commercial": (
        "budget & A&P management, budget pacing & allocation, pricing & promotions, incentive tracking, "
        "key account management, senior-stakeholder reporting, cross-functional collaboration"
    ),
    "skills_data": (
        "full-funnel analytics, ROI / ROAS / conversion / traffic / retention analysis, CAC efficiency, "
        "attribution & measurement (last-touch vs incrementality), KPI reporting, A/B testing, "
        "AI-assisted analysis & forecasting, Power BI, Looker"
    ),
    "skills_tools": (
        "Meta Ads Manager, Meta Business Suite, Google Ads, Generative AI (Claude, ChatGPT), Shopify, "
        "Power BI, Looker, Tableau, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "instashop runs on people who can execute paid campaigns and read the data behind them — and do it lean, "
        "with AI baked into the workflow. That is exactly how I work. I'm a performance-minded marketer who plans "
        "and optimises paid media on Meta and Google Ads, and my rare edge is being genuinely AI-first: I built a "
        "generative-AI system (Claude/GPT) that automates my reporting, analysis, brief writing and campaign "
        "planning. Just as relevant, I know q-commerce from the inside — I integrate and grow brands on Talabat, "
        "Noon, Careem and Deliveroo today, so I understand instashop's marketplace and customer-acquisition context "
        "from the operator's seat before day one."
    ),
    "body_paragraph_1": (
        "The role maps closely onto what I do. On the execution side I own campaign setup, audience building, "
        "creative A/B testing, budget allocation and bid/pacing on Meta (Facebook & Instagram) and Google Ads, "
        "optimising against ROI and ROAS. On the analyst side I run full-funnel analysis — traffic, conversion, "
        "retention, ROAS — and build KPI reports and business reviews for senior stakeholders across GCC/MENA "
        "markets, which is the UAE-and-Egypt, multi-market reporting this job needs. I design and document A/B "
        "tests, and I brief and manage 25–50 creators per campaign on short-form video (UGC, Reels, TikTok "
        "content), so I'm fluent in the creative-iteration loop that paid social lives on. Because my AI system "
        "does the manual heavy lifting, I can move at the pace this team runs at."
    ),
    "body_paragraph_2": (
        "Two honest notes so we're clear-eyed. First, my paid-media strength is Meta (with Google); I have working "
        "TikTok content and creative experience rather than deep TikTok Ads Manager tenure, and I'd ramp that fast. "
        "Second, I understand attribution and measurement — last-touch versus incrementality, CAC, ROAS, CPM — but "
        "I haven't yet used an MMP like Adjust or AppsFlyer hands-on, so that's a tool I'd pick up quickly rather "
        "than one I'll overstate. My background is broader brand-and-commercial with hands-on paid media, more than "
        "a pure paid-social specialist track — but what I bring beyond the checklist is genuine AI-first working, "
        "real q-commerce fluency in this market, and strong analytical rigour, all of which map directly onto how "
        "this team wants to operate."
    ),
    "closing_paragraph": (
        "I'd be genuinely excited to go deep on performance marketing and AI at instashop's scale, and to prove it "
        "in CAC efficiency and full-funnel results — I can walk through paid-media, promotion and analytics case "
        "studies (from +30% GMV QoQ to AI automation that cut ~40% of manual work). I'm based in Dubai and ready to "
        "move fast. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="talabat-perf-mktg-specialist-instashop-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://careers.talabat.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Performance Marketing Specialist paid social Meta TikTok q-commerce",
             "function": "Performance / growth marketing (paid social & search, individual contributor)",
             "sector": "Quick-commerce marketplace (instashop / talabat / Delivery Hero)",
             "note": "Strong, honest fit powered by two rare edges: genuinely AI-first working (JD explicitly "
                     "wants AI embedded in the workflow — Paula BUILT a Claude/GPT automation system) and "
                     "q-commerce insider knowledge (integrates onto Talabat — which owns instashop — plus Noon/"
                     "Careem/Deliveroo today; ex-Glovo). Core paid platform is Meta (+Google) with real A/B "
                     "testing and ROI/ROAS optimisation. Honest gaps disclosed in the CL: TikTok Ads depth "
                     "(strong on Meta; TikTok more content/creative), MMPs Adjust/AppsFlyer (not used hands-on; "
                     "understands attribution concepts), and 'dedicated paid-social specialist' framing (her paid "
                     "media sits inside broader brand/commercial roles). 'Specialist' IC title sits a notch below "
                     "her current Brand & Marketing Manager level — framed as enthusiasm to go deep, not a "
                     "step-down; confirm scope/band/comp. No 'own visa / no sponsorship' claim."},
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
        "ai_score": 82,
        "ai_tier": "Hot",
        "skills_match": [
            "AI-FIRST (JD's explicit ask) — BUILT a generative-AI system (Claude/GPT) automating reporting, analysis, brief writing and campaign planning; ~40% less manual work. This is her signature, rare edge and maps 1:1 to 'embed AI into your workflow / prompt engineering'",
            "Q-COMMERCE INSIDER — integrates & grows brands on Talabat (which OWNS instashop), Noon, Careem, Deliveroo TODAY at DoFreeze; ex-Glovo AM. JD lists q-commerce/food-delivery/e-commerce as a strong plus",
            "Paid media execution — plans, sets up and optimises Meta Ads (Facebook & Instagram) + Google Ads: audience building, creative A/B testing, budget allocation & bid/pacing, ROI/ROAS optimisation",
            "Analytical rigour (the 'strategic analyst' half) — full-funnel analysis (traffic, conversion, retention, ROI/ROAS), KPI reporting & business reviews for senior stakeholders across multi-market GCC/MENA (JD: UAE & Egypt)",
            "Experimentation — designs/documents A/B tests on audiences, creatives and promotions",
            "Short-form creative (nice-to-have) — briefs & manages 25–50 creators/campaign; UGC, Reels, TikTok content; structured creative feedback",
            "Brand + performance simultaneously (nice-to-have); Business Administration degree (CUNEF); 4+ yrs; Dubai-based; fast-paced/ownership-led",
        ],
        "missing_skills": [
            "TikTok ADS depth — her paid strength is Meta (+Google); TikTok is more content/short-form + influencer than deep TikTok Ads Manager. Fast ramp; disclosed honestly in CL, not overstated",
            "MMPs (Adjust / AppsFlyer) — NOT used hands-on. Understands attribution/measurement conceptually (last-touch vs incrementality, CAC/ROAS/CPM) with strong analytics; MMP tooling is a fast ramp. Disclosed; never listed among her tools",
            "'2 years focused on paid social' — her hands-on paid media sits inside broader brand/commercial/e-commerce roles rather than a dedicated paid-social specialist track. Positioned truthfully",
        ],
        "sector_fit": "excellent — quick-commerce marketplace marketing is exactly her DoFreeze + Glovo world; talabat owns instashop and she integrates onto Talabat today",
        "seniority_fit": "strong / slightly over — 'Specialist' (IC, 3-5 yrs) vs her current Brand & Marketing Manager level; framed as genuine enthusiasm to go deep on performance + AI, not a step-down",
        "red_flags": [
            "IC 'Specialist' title sits a notch below her Brand & Marketing Manager level — confirm scope/band/comp before advancing; upside is talabat/Delivery Hero brand + a genuine performance-marketing + AI deepening.",
            "TikTok Ads depth and MMP (Adjust/AppsFlyer) hands-on are genuine gaps — disclosed honestly in the CL, framed as fast ramps, not hidden or fabricated.",
            "Paid-social tenure is embedded in broader roles, not a dedicated 2-year specialist track — stated truthfully.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit carried by two rare edges. (1) AI-first: the JD explicitly wants AI embedded in "
            "the workflow, prompt engineering and hands-on ChatGPT/Claude/Gemini — Paula BUILT a Claude/GPT "
            "automation system for reporting, analysis, brief writing and campaign planning (~40% less manual "
            "work), which is exactly the 'run lean' operating model. (2) Q-commerce insider: talabat owns "
            "instashop, and she integrates and grows brands on Talabat/Noon/Careem/Deliveroo today (ex-Glovo AM), "
            "so she understands the marketplace/acquisition context from the operator seat. On execution she runs "
            "paid media on Meta (Facebook & Instagram) and Google Ads with real A/B testing, budget/pacing and "
            "ROI/ROAS optimisation; on analysis she does full-funnel reporting for senior stakeholders across "
            "multi-market GCC/MENA. Honest gaps, all disclosed in the cover letter: TikTok Ads depth (Meta is her "
            "core paid platform; TikTok is more content/creative), MMPs Adjust/AppsFlyer (understands attribution "
            "concepts but hasn't used the tools hands-on), and 'dedicated paid-social specialist' framing (her "
            "paid media sits inside broader brand/commercial roles). The IC 'Specialist' title is a touch below "
            "her current level — positioned as enthusiasm to go deep on performance + AI at talabat's scale; "
            "confirm scope/band/comp. No 'own visa / no sponsorship' claim."
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
