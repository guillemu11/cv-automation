"""One-off: generate Paula's CV + cover letter for Unilever
"Key Account Executive - Personal Care" (Dubai, UAE — Modern Trade / Sales).

Strong, direct fit. The role is a Modern-Trade Key Account / trade-marketing
executive for MT customers in the UAE across Skin Cleansing, Deos & Oral Care —
i.e. store-specific category plans, planogram & shelf-share audits, POSM &
merchandising execution, retailer-specific promo plans + ROI, pricing compliance,
NPI listing / product master data, and sell-out / market-share / secondary-sales
analysis (EPOS + Dunnhumby portal). That maps cleanly onto Paula's real track:
category planning at Mondelez (sell-in/sell-out, Nielsen, promo effectiveness),
42 key accounts at Alibaba's Miravia (+30% GMV QoQ via assortment / pricing /
promotions), and modern-trade + distributor + quick-commerce execution at DoFreeze
across the UAE.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful:
  - NO invented Dunnhumby experience. The JD asks candidates to "use the available
    Dunnhumby portal" and lists EPOS reading as preferred; Paula has genuine
    EPOS/sell-out + Nielsen analysis, so that is what is claimed. Dunnhumby is a
    portal she would pick up, not a tool she already uses — it is simply not
    claimed in the CV.
  - NO invented personal-care (Skin Cleansing / Deos / Oral Care) category tenure.
    Her category depth is chocolate (Mondelez) and beauty/fragrances (Miravia);
    personal care is positioned as adjacent FMCG/beauty, never as owned tenure.
  - NO invented named-grocery-MT (Carrefour / Lulu / Spinneys) account tenure.
    She runs UAE modern trade + quick-commerce via DoFreeze — adjacent, positioned
    as such.
  - VISA: she is already in Dubai on a UAE residence visa. Per the standing rule,
    we NEVER claim "no sponsorship needed" — the visa is employer-sponsored. We
    only state she is already based in Dubai (zero relocation timeline).

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-25/.
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

COMPANY = "Unilever"
TITLE = "Key Account Executive - Personal Care"
DATE_FOLDER = "2026-08-25"

# Promoted by a recruiter; no named hiring manager in the post ("Muhammad Hamza"
# is a network connection, not the hiring manager), so the letter stays addressed
# to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Key Account Executive - Personal Care — Unilever, Dubai, UAE (On-site, Full-Time).

Job Purpose: work on loved brands and improve the lives of consumers, driven by
Unilever's purpose to make sustainable living commonplace. Responsible for key
account management for Modern Trade (MT) customers in the UAE.

Key Responsibilities:
Retail-Centric Category Strategy — develop account store-specific category plans for
Skin Cleansing, Deos & Oral Care aligned to retailer objectives; run store audits to
assess shelf share, competitor placements and planogram compliance; plan and implement
customer events married to brand/category objectives; identify assortment gap vs.
potential and recommend range adjustments; track spend vs. planned budgets at
customer/category level.
Head Office Coordination — bridge execution teams and head office; align on new
product launches, discontinuations and promotions with timebound listing of NPIs;
manage product master data in the customer system; share store-level insights
(slow-moving SKUs, promo effectiveness) to refine national strategies; ensure timely
planning and execution of POSM and merchandising guidelines.
Promotion & Pricing Execution — design retailer-specific promo plans and track ROI;
negotiate with HO to implement the right promotion for the right store; monitor pricing
compliance vs. competitors.
Data-Driven Decision Making — analyse sell-out data, market share and secondary sales
to recommend corrective actions; prepare weekly/monthly reports for head office on
category performance; use the available Dunnhumby portal to take data-driven decisions.

Required Qualifications: Bachelor's degree; 3+ years in FMCG Modern Trade category
management / trade marketing, preferably in personal care/hygiene, with a track record
of performance; expertise in retail store operations and head office processes;
proficiency in planogram and EPOS data analysis.
Soft Skills: strong negotiation; collaborative mindset to work with HO and cross-
functional teams.
Performance Metrics: category sales growth (value/volume) in assigned accounts; OSA &
listing compliance; promo ROI; turnover achievement.
Preferred: Joint Business Planning end-to-end understanding; EPOS reading ability.
"""

ATS = [
    "Key Account Executive", "Key Account Management", "Modern Trade", "MT",
    "FMCG", "personal care", "hygiene", "category management", "trade marketing",
    "category strategy", "store-specific category plans", "shelf share",
    "store audits", "competitor placements", "planogram", "planogram compliance",
    "assortment", "range adjustments", "assortment gap", "customer events",
    "POSM", "merchandising", "merchandising guidelines", "NPI", "new product launch",
    "product master data", "head office", "HO coordination", "promo plans",
    "promo ROI", "promotion", "pricing", "pricing compliance", "sell-out",
    "sell-out data", "market share", "secondary sales", "EPOS", "EPOS reading",
    "data-driven decision making", "category performance", "OSA",
    "on-shelf availability", "listing compliance", "turnover", "category sales growth",
    "Joint Business Planning", "JBP", "negotiation", "Nielsen", "corrective actions",
    "GCC", "MENA", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Key Account & Trade Marketing · Modern Trade · FMCG / Personal Care · "
        "Category, Planogram & POSM · Promo ROI, EPOS & Sell-out"
    ),
    "professional_summary": (
        "Commercial, key account and trade-marketing professional with 4+ years across FMCG, Beauty and "
        "E-Commerce. Currently drive modern-trade execution for DoFreeze (Befit, Eurocake, Flair) across the "
        "UAE — store-specific assortment, planogram compliance, POSM & merchandising, retailer promo mechanics "
        "and on-shelf availability. Previously owned 42 key accounts at Alibaba's Miravia (+30% GMV growth QoQ) "
        "via assortment optimisation, pricing strategy and targeted promotions, with category-planning "
        "grounding at Mondelez (sell-in/sell-out, Nielsen, promo effectiveness). Fluent in EPOS/sell-out "
        "analysis, promo ROI and JBP; already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own modern-trade category execution across UAE accounts — store-specific assortment, planogram compliance and POSM/merchandising guidelines — driving on-shelf availability (OSA) and listing compliance",
                "Design retailer-specific promo plans and pricing, tracking promo ROI and monitoring price compliance vs. competitors, and negotiating the right mechanic for the right store with head office",
                "Track spend vs. planned trade budgets at customer/category level and manage product master data, timebound NPI listings and new promotions as the bridge between execution teams and head office",
                "Analyse sell-out, market-share and secondary-sales data to recommend corrective actions and prepare weekly/monthly category-performance reports for head office",
                "Plan customer events and activations married to brand/category objectives across modern trade and UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), identifying assortment gap vs. potential and recommending range adjustments",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned 42 key accounts, delivering +30% GMV growth QoQ (ahead of category) through assortment optimisation, pricing strategy and targeted promotions",
                "Identified assortment gaps vs. potential and recommended range adjustments; led category expansion as PIC Fragrances, onboarding 30+ stores in two months via trend-driven assortment",
                "Ran monthly category, pricing and competitor deep dives, turning market-share, promo and launch data into corrective actions and clear recommendations for accounts and buyers",
                "Negotiated commercial terms and promo plans — owning the Flash Sales channel, reporting to the CEO and executing against P&L targets",
                "Steered conversion, retention, ROI and ROAS to sharpen forecasting accuracy and channel performance",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic XL key accounts and helped build Glovo's Retail vertical, growing GMV through data-led joint planning and bespoke activations",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both platform and partners",
                "Led cross-functional squads across marketing, logistics and operations to deliver flawless execution and grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran category deep dives for chocolate — sell-in/sell-out, Nielsen performance reporting and promotional-effectiveness analysis — feeding trade and category planning",
                "Assessed shelf share and planogram compliance and identified assortment gaps vs. potential to inform range recommendations",
                "Supported NPD/NPI launches (Milka Spread, Mini Suchard) from concept to shelf, coordinating with head office on listings, and translated Nielsen / EPOS-style data into commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "key account management, modern trade, category management, trade marketing, assortment planning, "
        "planogram compliance, joint business planning (JBP), pricing strategy, commercial negotiation, "
        "distributor management"
    ),
    "skills_data": (
        "EPOS & sell-out analysis, secondary-sales analysis, Nielsen, market-share tracking, category deep "
        "dives, promo ROI, planogram / Planorama, P&L management, corrective-action reporting, Power BI"
    ),
    "skills_brand": (
        "shopper marketing, trade marketing, POSM & merchandising execution, in-store activation & visibility, "
        "customer events, NPI / NPD launch, A&P & trade budget management, go-to-market"
    ),
    "skills_ecommerce": (
        "modern trade + quick-commerce (Noon, Talabat, Careem, Deliveroo), on-shelf availability & listing "
        "compliance, omnichannel retail execution, listings & promo mechanics, product master data"
    ),
    "skills_tools": (
        "SAP, Nielsen, Planorama, Microsoft Excel (Advanced), PowerPoint (Advanced), Power BI, Salesforce, "
        "Generative AI (Claude, ChatGPT), Kantar, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Unilever's belief that doing business the right way drives superior performance — carried by brands "
        "people genuinely love, from Dove and Rexona to your oral-care portfolio — is exactly the kind of "
        "personal-care business I want to help grow on the modern-trade shelf. The Key Account Executive – "
        "Personal Care role caught my attention because it asks for what I do every week: build store-specific "
        "category plans, keep planograms and shelf share honest, design retailer promo plans with a clear ROI "
        "lens, and turn sell-out and market-share data into corrective on-shelf action."
    ),
    "body_paragraph_1": (
        "Modern-trade category and key account work is the spine of my career. Today, as Brand & Marketing "
        "Manager at DoFreeze, I own modern-trade execution across UAE accounts — store-specific assortment, "
        "planogram compliance, POSM and merchandising, retailer-specific promo mechanics, pricing compliance "
        "and OSA — while tracking spend vs. trade budgets and managing NPI listings and product master data "
        "with head office. Before Dubai, I owned 42 key accounts at Alibaba's Miravia and grew GMV +30% QoQ, "
        "ahead of category, through assortment optimisation, pricing strategy and targeted promotions. And my "
        "category grounding at Mondelez — sell-in/sell-out, Nielsen deep dives and promo-effectiveness "
        "analysis — means EPOS and sell-out data are already how I build account recommendations."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, I am already in Dubai on a UAE residence visa and operating inside UAE "
        "modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo) — a real omnichannel account view "
        "from day one, with no relocation timeline. Second, I lead with category- and shopper-led value, not "
        "just price. I'll be candid that my category depth has been in beauty/fragrances and food rather than "
        "personal care specifically, and that my UAE modern-trade tenure is via DoFreeze rather than a named "
        "grocery banner — but I already speak the language of JBP, planograms, promo ROI and EPOS-led "
        "corrective action, and I ramp fast on a new category."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of key account ownership, trade-marketing execution and "
        "data-led decision making to Unilever's personal-care business in the UAE. I am available to start "
        "immediately and would welcome the chance to discuss how I would approach store-specific category "
        "plans, promo ROI and shelf execution across Skin Cleansing, Deos and Oral Care. Thank you for your "
        "consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="unilever-kae-personal-care-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.unilever.com",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Key Account Executive - Personal Care",
             "function": "Sales / Customer Development", "entity": "Unilever Gulf FZE",
             "channel": "Modern Trade", "categories": "Skin Cleansing, Deos, Oral Care"},
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
        "ai_score": 85,
        "ai_tier": "Hot",
        "skills_match": [
            "Modern-trade category management + trade marketing (DoFreeze, UAE)",
            "Key Account Management (Miravia 42 accounts +30% GMV QoQ, Glovo XL)",
            "Category planning: sell-in/sell-out, Nielsen, promo effectiveness (Mondelez)",
            "Planogram compliance + shelf-share audits + assortment gap vs. potential",
            "POSM & merchandising execution",
            "Retailer-specific promo plans + promo ROI + pricing compliance",
            "EPOS / sell-out / secondary-sales analysis → corrective actions",
            "NPI listing + product master data + head-office coordination",
            "JBP end-to-end understanding",
            "Already in Dubai (UAE residence visa)",
        ],
        "missing_skills": [
            "Personal-care (Skin Cleansing/Deos/Oral Care) category tenure — has beauty/fragrances + food FMCG, adjacent",
            "Dunnhumby portal (JD asks to use it) — has genuine EPOS/Nielsen/sell-out analysis instead",
            "Named grocery-MT banner tenure (Carrefour/Lulu/etc.) — has UAE modern trade + q-commerce via DoFreeze, adjacent",
        ],
        "sector_fit": "strong (FMCG modern trade; beauty/personal-care adjacent)",
        "seniority_fit": "slightly above band (4+ yrs + KAM track vs. Executive 3+)",
        "red_flags": [
            "Personal-care category and named-grocery-banner tenure are 'preferred'/expected — Paula's are adjacent (beauty/food FMCG; DoFreeze UAE modern trade + q-commerce), not identical",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, direct fit. This is a Modern-Trade Key Account / trade-marketing executive role — "
            "store-specific category plans, planogram & shelf-share audits, POSM & merchandising, retailer "
            "promo plans + ROI, pricing compliance, NPI listing / product master data, and sell-out / "
            "market-share / secondary-sales analysis (EPOS + Dunnhumby portal). That maps cleanly onto Paula's "
            "track: category planning at Mondelez (sell-in/sell-out, Nielsen, promo effectiveness), 42 key "
            "accounts +30% GMV QoQ at Miravia via assortment/pricing/promotions, and modern-trade + "
            "distributor + quick-commerce execution at DoFreeze across the UAE. Honest gaps: personal-care "
            "category tenure (has beauty/fragrances + food FMCG), the Dunnhumby portal specifically (has "
            "genuine EPOS/Nielsen/sell-out analysis), and named grocery-banner tenure (has UAE modern trade + "
            "q-commerce via DoFreeze). Tenure sits slightly above the 3+ band. Positioned truthfully; no "
            "invented personal-care, Dunnhumby or named-account claims, and no 'no sponsorship needed' claim "
            "(she is on an employer-sponsored UAE residence visa)."
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
