"""One-off: generate Paula's CV (+ cover letter) for Careem — "Growth Manager"
(Careem Food, Dubai/UAE). Leads the growth function for Careem Food in Dubai:
bottom-up growth planning, performance tracking vs plan, initiative design across
acquisition→retention→monetisation, program management and cross-functional
alignment, with direct revenue accountability.

Why the fit is genuinely strong (a reach, but a reachable one):
  - FOOD DELIVERY DNA (the rare part): Paula worked INSIDE Glovo (quick-commerce
    super-app / food delivery) driving GMV growth for strategic accounts (KFC,
    Taco Bell, La Tagliatella, Sushi Shop), and today integrates DoFreeze brands
    into Careem / Talabat / Deliveroo / Noon as a partner. JD asks for "deep
    understanding of food delivery market dynamics" — she has it first-hand.
  - Growth vs revenue targets: +30% GMV QoQ across 42 accounts at Miravia
    (Alibaba), P&L accountability, pricing/promotions balanced against margin.
  - Initiative design acquisition→engagement→retention→monetisation: paid media
    (Meta & Google Ads) with creative A/B testing, influencer 0→25-50/campaign,
    EDM/CRM, promo mechanics, Shopify CRO — all live at DoFreeze.
  - Cross-functional program management: coordinated marketing/ops/logistics/CX
    at Glovo and runs NPD launches as cross-functional programs at DoFreeze.
  - MENA / Dubai-based with UAE Residence Visa — "MENA experience a strong plus".
  - LinkedIn's own matcher flags her as a TOP/"destacado" candidate for this role
    (vs "media" for the Junior Category Executive).

HONEST gaps (NOT fabricated — reflected as-is, never overclaimed):
  - SQL / statistical modelling / cohort & churn / CLTV modelling: this is the
    most technical-analytical bar and Paula is more brand/commercial than a
    SQL-heavy growth analyst. She IS strongly data-led (Power BI, Tableau, Looker,
    funnel & retention analysis, A/B testing, ROI/ROAS, forecasting, AI-assisted
    analysis) — documents lean on THAT and do NOT claim SQL she doesn't have.
  - Experience: JD asks 5-7 yrs; counting from Mondelez (Aug 2021) she is at ~5
    yrs — bottom of the range, stated honestly.
  - Competitive manager-level role. Framed on genuine domain edge, not seniority.
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-28/. Also drops a short-named 'Paula De Francisco - CV.pdf'
copy for portals that reject long filenames.
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

COMPANY = "Careem"
TITLE = "Growth Manager"
DATE_FOLDER = "2026-08-28"

CONTACT = None  # Growth sits under Marketing; no named hiring manager in posting — "Hiring Manager".

JOB_DESCRIPTION = """\
Growth Manager — Careem (Careem Food), Dubai / UAE. Leads the growth function for
Careem Food in Dubai and, by extension, the UAE. Owns bottom-up planning, tracks
performance against plan, designs and program-manages growth initiatives, and
ensures cross-functional alignment, with direct accountability for Food hitting
its revenue targets in the market.

Growth Planning & Bottom-Up Strategy: own the bottom-up growth plan for Dubai/UAE,
translating market opportunity into measurable targets across MAUs, OPU, ARPU and
revenue; build and maintain the quarterly and annual growth roadmap aligned to
revenue goals.

Performance Tracking & Reporting: own the performance rhythm (weekly/monthly plan
vs actuals, funnel health checks, initiative-level tracking); build dashboards
across the customer funnel; diagnose gaps vs plan, find root causes and drive
corrective action.

Commercial Partnership & Revenue Accountability: primary growth point of contact
for the Food commercial team; co-own revenue delivery; design offers, incentives
and promotions balancing growth with unit economics.

Initiative Design & Execution: design growth initiatives end-to-end across user
acquisition, engagement, retention and monetisation; lead A/B testing and
experimentation to optimise across channels.

Program Management: own execution cadence (scoping, resourcing, launch timelines,
post-launch measurement); manage cross-team dependencies; escalate blockers.

Cross-Functional Stakeholder Management: align Product, Engineering, Operations
and Marketing around the growth agenda; communicate performance and strategy to
senior stakeholders.

Customer Segmentation & Lifecycle: build and manage customer segments using
behavioural, demographic and transactional data; design retention and engagement
programmes using cohort and lifecycle insights.

What you'll need: Bachelor's/Master's in Business, Marketing, Engineering, Data
Science or related; 5-7 years in growth, product marketing or strategy, focused on
e-commerce, food delivery or consumer tech platforms; proven track record owning
growth plans and delivering against revenue/engagement targets; cross-functional
coordination across product, engineering and commercial; high-growth, fast-paced
market experience (MENA a strong plus); strong analytical skills (data mining,
statistical modelling, SQL); A/B testing, cohort analysis, churn modelling, CLTV;
growth metrics (CAC, LTV, ARPU, OPU, conversion); program management; stakeholder
management and influencing; clear communication; deep understanding of food
delivery market dynamics, customer behaviour and the competitive landscape.
"""

ATS = [
    "growth", "growth manager", "growth strategy", "bottom-up plan", "growth plan",
    "growth roadmap", "MAU", "OPU", "ARPU", "CAC", "LTV", "CLTV", "conversion rate",
    "revenue", "revenue targets", "GMV", "funnel", "funnel health", "cohort analysis",
    "retention", "churn", "lifecycle", "customer segmentation", "A/B testing",
    "experimentation", "acquisition", "engagement", "monetisation", "unit economics",
    "offers", "incentives", "promotions", "program management", "cross-functional",
    "stakeholder management", "plan vs actuals", "dashboards", "KPIs",
    "paid media", "Meta Ads", "Google Ads", "CRM", "EDM", "Power BI", "Tableau",
    "Looker", "food delivery", "quick-commerce", "q-commerce", "e-commerce",
    "consumer tech", "super-app", "MENA", "Dubai", "UAE", "Careem", "Talabat",
    "Deliveroo", "Glovo", "P&L", "ROI", "ROAS", "go-to-market", "generative AI",
]

CV_CONTENT = {
    "headline": (
        "Growth & Brand Manager · Food Delivery & Quick-Commerce (Glovo · Careem · Talabat · Deliveroo) · "
        "Revenue & GMV Growth · Acquisition→Retention Initiatives · A/B Testing & Paid Media · MENA / Dubai"
    ),
    "professional_summary": (
        "Dubai-based growth & brand professional (~5 yrs) with hands-on food-delivery and quick-commerce "
        "experience — inside Glovo, and today as a Careem, Talabat and Deliveroo partner. Owns growth plans against "
        "revenue/GMV targets (+30% GMV QoQ), designs acquisition-to-retention initiatives with A/B testing and paid "
        "media, and runs them as cross-functional programs across marketing, ops and commercial. Strongly data-led "
        "(BI dashboards, funnel & retention analysis, ROI/ROAS, forecasting) and AI-first (Claude/GPT)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Integrated brands into UAE quick-commerce (Careem, Talabat, Noon, Deliveroo) — onboarding, listings, promo mechanics and retail execution — and run the D2C Shopify store end-to-end, lifting conversion (CRO) and AOV",
                "Design and run growth initiatives across acquisition, engagement and retention: paid media (Meta & Google Ads) with creative A/B testing, an influencer programme scaled 0→25-50 creators/campaign, EDM/CRM and sampling — tracked by ROI/ROAS and sell-out",
                "Lead 6 NPD launches as cross-functional programs (brief, pricing, GTM, timelines, A&P budgets); AI-first (Claude/GPT) analytics and reporting cutting ~40% manual work",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees",
            "bullets": [
                "Owned growth for 42 accounts, delivering +30% GMV QoQ through pricing, assortment and targeted promotions balanced against margin and unit economics",
                "Ran the Flash Sales channel (reporting to the CEO) and continuously analysed conversion, traffic, retention and forecasting against P&L targets — a weekly plan-vs-actuals rhythm",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app / food delivery | €500M+ revenue",
            "bullets": [
                "Drove GMV growth for strategic food-delivery accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) via bespoke marketing activations, promotions and data-led planning on a quick-commerce platform",
                "Coordinated cross-functional teams (marketing, ops, logistics, CX) to launch campaigns and lift order volume in a fast-paced, high-growth market — the exact food-delivery growth dynamics of this role",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG multinational | €36B revenue | 90K+ employees",
            "bullets": [
                "Analytics grounding: sell-in/sell-out analysis, promotional-effectiveness evaluation and performance reporting; contributed to NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (
        "growth strategy, bottom-up growth planning, acquisition→retention initiatives, "
        "promotions & offers design, go-to-market, NPD, lifecycle & retention programmes"
    ),
    "skills_ecommerce": (
        "food delivery & quick-commerce (Careem, Talabat, Deliveroo, Noon, Glovo), e-commerce (Shopify/CRO), "
        "paid media (Meta & Google Ads), CRM/EDM, A/B testing & experimentation"
    ),
    "skills_commercial": (
        "revenue & GMV growth, P&L, pricing & unit economics, key account management, "
        "cross-functional program management, stakeholder management"
    ),
    "skills_data": (
        "growth metrics (GMV, CAC, LTV, ARPU, conversion, ROI/ROAS), funnel & retention analysis, "
        "KPI dashboards & plan-vs-actuals, forecasting, AI-assisted analysis"
    ),
    "skills_tools": (
        "Power BI, Tableau, Looker, Meta Ads, Google Ads, Shopify, Salesforce, SAP, "
        "MS Excel — Expert, Generative AI (Claude, ChatGPT)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Careem Food's growth agenda is exactly the kind of problem I love — turning market opportunity into a "
        "bottom-up plan, then shipping the initiatives that actually move MAUs, orders and revenue. What I'd bring "
        "that's rare is genuine food-delivery and quick-commerce DNA: I worked inside Glovo driving GMV for major "
        "food accounts, and today I run DoFreeze's growth as a Careem, Talabat and Deliveroo partner — so I already "
        "think in this platform's mechanics and market."
    ),
    "body_paragraph_1": (
        "The role maps closely onto what I do. I design growth initiatives end-to-end across acquisition, "
        "engagement and retention — paid media (Meta & Google Ads) with creative A/B testing, promo and offer "
        "mechanics balanced against margin, CRM/EDM lifecycle and Shopify CRO — and I run them as cross-functional "
        "programs with clear owners, timelines and post-launch measurement. On revenue accountability, I owned "
        "growth for 42 accounts at Miravia (Alibaba) and delivered +30% GMV QoQ through pricing, assortment and "
        "targeted promotions, working a weekly plan-vs-actuals rhythm against P&L. At Glovo I coordinated marketing, "
        "ops and logistics to launch campaigns and lift order volume in a fast-paced market — the same food-delivery "
        "growth dynamics this role lives in."
    ),
    "body_paragraph_2": (
        "I'm strongly data-led: I live in dashboards, funnel and retention analysis, and A/B testing, and I track "
        "growth by the metrics that matter — GMV, conversion, ROI/ROAS, ARPU and unit economics (Power BI, Tableau, "
        "Looker). I'll be candid that my edge is commercial-and-growth rather than deep SQL modelling, but I read "
        "data fast, turn it into decisions, and I use an AI-first workflow (Claude/GPT) to move quicker on analysis "
        "and reporting. Add that I'm MENA-based with the partner-side view of Careem, and I can be productive from "
        "week one."
    ),
    "closing_paragraph": (
        "I'd be genuinely excited to help Careem Food hit its Dubai/UAE growth targets, and I can walk through "
        "growth, promotion and retention case studies from Glovo, Miravia and DoFreeze. I'm already based in Dubai "
        "and ready to start fast. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="careem-growth-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://www.careem.com/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Growth Manager Careem Food quick-commerce food delivery growth plan revenue",
             "function": "Growth (Careem Food — bottom-up growth planning, initiatives acquisition→retention, revenue accountability)",
             "sector": "Quick-commerce / food delivery / consumer tech (Careem — Uber / e& super-app)",
             "note": "STRONG domain fit (food delivery DNA via Glovo + Careem/Talabat/Deliveroo partner; +30% GMV; "
                     "acquisition→retention initiatives with A/B testing & paid media; cross-functional program mgmt; "
                     "MENA/Dubai-based) — a reachable REACH. Honest gaps: SQL/statistical/cohort/churn/CLTV modelling "
                     "(she is data-led via BI + A/B + ROI/ROAS, NOT a SQL analyst — never fabricated); ~5 yrs vs 5-7 "
                     "asked (bottom of range); competitive manager role. LinkedIn matcher flags her 'destacado'. No "
                     "'own visa / no sponsorship' claim."},
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
        "ai_score": 70,
        "ai_tier": "Warm-Hot",
        "skills_match": [
            "Food-delivery DNA (rare): worked INSIDE Glovo driving GMV for KFC/Taco Bell/La Tagliatella/Sushi Shop, and today a Careem/Talabat/Deliveroo partner — 'deep understanding of food delivery market dynamics' first-hand",
            "Growth vs revenue targets: +30% GMV QoQ across 42 accounts (Miravia/Alibaba), P&L accountability, pricing/promotions balanced against margin/unit economics",
            "Initiative design acquisition→engagement→retention→monetisation: paid media (Meta & Google Ads) + creative A/B testing, influencer 0→25-50/campaign, EDM/CRM, promo mechanics, Shopify CRO",
            "Cross-functional program management: coordinated marketing/ops/logistics/CX at Glovo; runs NPD as cross-functional programs at DoFreeze",
            "Data-led: BI dashboards (Power BI/Tableau/Looker), funnel & retention analysis, ROI/ROAS, forecasting, AI-assisted analysis",
            "MENA / Dubai-based with UAE Residence Visa ('MENA experience a strong plus'); ~5 yrs experience; Business Administration degree",
        ],
        "missing_skills": [
            "SQL / statistical modelling / cohort & churn / CLTV modelling — the most technical-analytical bar; Paula is data-led via BI + A/B + ROI/ROAS but NOT a SQL-heavy growth analyst (never fabricated; documents lean on BI, not SQL)",
            "Experience: JD asks 5-7 yrs; she is at ~5 (bottom of range) — stated honestly",
            "Competitive manager-level role (16% of applicants are Managers, 10% Directors)",
        ],
        "sector_fit": "excellent — quick-commerce / food delivery, her exact domain (Glovo inside + Careem partner)",
        "seniority_fit": "in-band Manager (~5 yrs vs 5-7 asked); reachable reach, framed on domain edge not seniority",
        "red_flags": [
            "SQL / statistical-modelling bar is real — she competes below more technical growth-analyst profiles here; documents do not fabricate SQL. Lean the pitch on domain + growth track record.",
            "~5 yrs sits at the bottom of the 5-7 asked.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Genuinely one of Paula's better Careem matches and clearly stronger than the Junior Category Executive "
            "(LinkedIn's own matcher flags her 'destacado'/top candidate here vs 'media' there). The role leads growth "
            "for Careem Food in Dubai — bottom-up planning, initiatives across acquisition→retention→monetisation, "
            "A/B testing, promotions balanced against unit economics, cross-functional program management and revenue "
            "accountability. Paula brings rare food-delivery DNA (inside Glovo + Careem/Talabat/Deliveroo partner "
            "today), a +30% GMV QoQ growth track record, live acquisition-to-retention execution (paid media, A/B "
            "testing, CRM, CRO) and cross-functional coordination, all MENA/Dubai-based. The honest gap is the "
            "technical-analytical bar (SQL, statistical/cohort/churn/CLTV modelling): she is strongly data-led via BI "
            "(Power BI/Tableau/Looker), funnel/retention analysis, A/B testing and ROI/ROAS, but not a SQL analyst — "
            "never fabricated. Experience ~5 yrs sits at the bottom of the 5-7 asked. A reachable reach: pitch the "
            "domain edge and growth results, and pair with a warm inbound via a Careem marketing contact. No 'own "
            "visa / no sponsorship' claim."
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

    # Short-named copy for portals that reject long/special-char filenames.
    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    if cv_pdf.exists():
        shutil.copy(str(final_dir / "01_CV_y_Carta" / cv_pdf.name), str(short))
        print("OK_SHORT", short)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
