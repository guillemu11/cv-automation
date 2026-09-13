"""One-off: generate Paula's CV + cover letter for Beiersdorf Middle East FZCO
"Key Account Manager - Modern Trade - UAE" (Dubai, Sales function).

This is a *strong, direct* fit — arguably stronger than the Eucerin ABM role —
because it maps onto Paula's explicit Key Account Management track: 42 key accounts
at Alibaba's Miravia (+30% GMV QoQ) via joint planning / assortment / pricing /
promotions, modern-trade + distributor orchestration at DoFreeze across the UAE and
50+ markets, XL account management at Glovo, and category planning with Nielsen /
sell-in-sell-out at Mondelez. SAP and Nielsen are genuinely in her toolkit.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful:
  - NO invented Carrefour / Lulu / Spinneys account tenure (she has DoFreeze
    modern trade + UAE quick-commerce, which is adjacent — positioned as such,
    never as named-grocery-MT experience).
  - NO invented Dunnhumby (JD lists it as an advantage; she doesn't have it, so
    it is simply omitted).
  - "JBP" is used where she genuinely did joint/annual account planning; it is a
    reframe of real work, not a fabricated process.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-17/.
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

COMPANY = "Beiersdorf"
TITLE = "Key Account Manager - Modern Trade"
DATE_FOLDER = "2026-08-25"

# Named contact in the JD is the TA lead (queries), not the hiring manager, so
# the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Key Account Manager - Modern Trade - UAE — Beiersdorf Middle East FZCO, Dubai, UAE.
Contract: Unlimited / Full-Time. Job Function: Sales.

Own and grow strategic modern trade key accounts in the UAE (Carrefour, Lulu,
Spinneys), delivering sustainable Net Sales, market share and profitability through
best-in-class Joint Business Planning, omnichannel execution and distributor
orchestration. Act as single-point-of-account leadership, translating shopper and
EPOS insights into flawless execution. Coordination of UAE and Carrefour at Middle
East level.

Key Outcomes: Net Sales and share growth ahead of market; strong JBPs with clear
value exchange; high-quality forecasts and disciplined S&OP inputs; excellent OTIF,
availability and shelf execution; trusted partner status with customers and
distributors.

Core Responsibilities: lead annual JBP and commercial negotiations (terms, BDAs,
visibility, activation); own 4P execution by account with a clear ROI mindset;
translate EPOS, shopper and market data into actions; own forecast accuracy and
demand shaping; manage customer budgets and financial reconciliation; drive flawless
execution with distributor and S&CM teams.

Distributor & Cross-Functional Leadership: orchestrate distributor execution against
agreed plans; work closely with Shopper Marketing, Marketing, Finance and Supply
Chain; actively manage risks (stock, DIH, delisting, promo gaps).

Store-Level & Execution Excellence: ensure availability, planogram compliance and
promo execution; track and act on competitive activity; ensure weekly sell-out data
quality and insights.

Profile: 3-6 years of Key Account Management experience in Modern Trade, preferably
within a multinational FMCG company; distributor management preferred; prior exposure
to UAE Modern Trade retailers such as Carrefour and Lulu strongly preferred; proven
experience in Joint Business Planning (JBP) and commercial negotiations; account
and/or category management a plus. Fluent English; strong relationship and
stakeholder management; strong analytical and data interpretation (IMS, EPOS, Nielsen);
ability to drive value creation beyond price. Tools: SAP, Nielsen, Dunnhumby an
advantage.
"""

ATS = [
    "Key Account Management", "Key Account Manager", "Modern Trade", "FMCG",
    "multinational", "Joint Business Planning", "JBP", "commercial negotiation",
    "terms", "BDA", "visibility", "activation", "4P execution", "ROI",
    "distributor management", "distributor orchestration", "EPOS", "IMS",
    "Nielsen", "shopper insights", "market data", "forecast accuracy",
    "demand shaping", "S&OP", "customer budgets", "financial reconciliation",
    "Shopper Marketing", "S&CM", "Supply Chain", "OTIF", "availability",
    "planogram", "promo execution", "sell-out", "sell-in", "competitive activity",
    "market share", "Net Sales", "profitability", "category management",
    "assortment", "pricing", "stakeholder management", "value creation",
    "P&L", "SAP", "Carrefour", "Lulu", "GCC", "MENA", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Key Account Manager · Modern Trade & Distributors · FMCG · "
        "JBP & Commercial Negotiation · Category & Shopper"
    ),
    "professional_summary": (
        "Commercial and key account professional with 4+ years managing accounts, distributors and "
        "category growth across FMCG, Beauty and E-Commerce. Currently orchestrate distributor networks "
        "and modern-trade + quick-commerce execution for DoFreeze (Befit, Eurocake, Flair) across the UAE "
        "and 50+ markets; previously owned 42 key accounts at Alibaba's Miravia, delivering +30% GMV growth "
        "QoQ through joint planning, assortment, pricing strategy and targeted promotions. Category-planning "
        "grounding at Mondelez (sell-in/sell-out, Nielsen, promotional effectiveness) and XL account "
        "leadership at Glovo. Strong in commercial negotiation, forecasting, P&L and turning EPOS/Nielsen "
        "data into flawless 4P execution — hands-on with SAP and Nielsen. Fluent English, already based in "
        "Dubai on a UAE residence visa and available immediately (no relocation timeline)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own modern-trade and distributor execution across the UAE and 50+ markets — orchestrating distributor plans, assortment, pricing and promotional mechanics, and driving on-shelf availability and execution against agreed plans",
                "Lead annual commercial planning and negotiations with accounts and distributors (terms, visibility, activation), building joint plans with clear value exchange beyond price through category and shopper initiatives",
                "Manage A&P and trade budgets end-to-end — planning, tracking and financial reconciliation with Finance — and actively manage commercial risks (stock, promo gaps, delisting)",
                "Own demand forecasting and partner with Supply Chain, Shopper Marketing and Marketing to align availability, OTIF and KPI delivery",
                "Run a true omnichannel account footprint — integrating brands into UAE quick-commerce (Noon, Talabat, Careem, Deliveroo) alongside modern trade with listings, promo mechanics and retail execution",
                "Turn category, EPOS/sell-out and competitor data into account actions — tracking competitive activity and safeguarding weekly sell-out data quality",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned 42 key accounts, delivering +30% GMV growth QoQ (ahead of category) through joint business planning, assortment optimisation, pricing strategy and targeted promotions",
                "Led commercial negotiations and annual account plans — owning the Flash Sales channel, reporting to the CEO and executing plans aligned to P&L targets",
                "Ran monthly category, pricing and competitor deep dives, turning share, promotion and launch data into clear recommendations and corrective actions for accounts and buyers",
                "Led category expansion as PIC Fragrances, onboarding 30+ accounts and distributor-backed houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) in two months via trend-driven, value-creating assortment",
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
                "Ran category deep dives for chocolate — sell-in/sell-out, Nielsen performance reporting and promotional-effectiveness analysis — feeding demand and commercial planning inputs",
                "Identified growth opportunities and supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
                "Built management-ready analyses in advanced Excel, translating Nielsen/IMS-style data into actionable commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "key account management, modern trade, distributor management, joint business planning (JBP), "
        "commercial negotiation, terms & BDA management, pricing strategy, assortment planning, category "
        "management, planogram compliance, forecasting & demand shaping, 4P execution"
    ),
    "skills_data": (
        "Nielsen, EPOS & sell-out analysis, IMS, sell-in/sell-out, category deep dives, market-share "
        "tracking, P&L management, forecast accuracy, KPI tracking, ROI/ROAS, SAP, Power BI"
    ),
    "skills_brand": (
        "shopper marketing, trade marketing, joint business planning, activation & visibility, A&P & trade "
        "budget management, promotional planning, omnichannel execution, go-to-market, value creation beyond price"
    ),
    "skills_ecommerce": (
        "modern trade + quick-commerce (Noon, Talabat, Careem, Deliveroo), eCommerce visibility & "
        "availability, omnichannel retail execution, shopper-journey optimisation, listings & promo mechanics, "
        "conversion rate optimisation (CRO)"
    ),
    "skills_tools": (
        "SAP, Nielsen, Microsoft Excel (Advanced), PowerPoint (Advanced), Power BI, Salesforce, "
        "Generative AI (Claude, ChatGPT), Tableau, Kantar, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Beiersdorf's belief that CARE CHANGES EVERYTHING is exactly the kind of brand equity — NIVEA, "
        "Eucerin, Labello — that earns its place on the modern-trade shelf, and I would relish the chance to "
        "own and grow it with Carrefour, Lulu and Spinneys. The Key Account Manager – Modern Trade role "
        "caught my attention because it asks for what I do every week: run strategic accounts and distributors "
        "in the UAE, build joint plans with a clear value exchange, and turn shopper and EPOS insight into "
        "flawless on-shelf execution."
    ),
    "body_paragraph_1": (
        "Key account management is the spine of my career. At Alibaba's Miravia I owned 42 key accounts and "
        "grew GMV +30% QoQ — ahead of category — through joint business planning, assortment, pricing "
        "strategy and targeted promotions, negotiating commercial terms and reporting channel P&L to the CEO. "
        "Today, as Brand & Marketing Manager at DoFreeze, I orchestrate distributor execution and modern-trade "
        "plans across the UAE and 50+ markets — assortment, promo mechanics, availability and financial "
        "reconciliation — while owning demand forecasting with Supply Chain. My category grounding at Mondelez "
        "(sell-in/sell-out, Nielsen deep dives, promo effectiveness) means IMS, EPOS and Nielsen data are how "
        "I already build account actions, and SAP is part of my toolkit."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, I am already in Dubai on a UAE residence visa and operating in UAE "
        "modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo) — an omnichannel account view "
        "from day one, available immediately with no relocation timeline. Second, I lead with value creation beyond price: "
        "category- and shopper-led growth, not just terms. I'll be candid that my direct tenure has been "
        "across e-commerce, beauty and FMCG accounts rather than a named grocery banner like Carrefour or "
        "Lulu specifically — but I already work inside UAE modern trade and distributor networks, I speak the "
        "language of JBP, 4P and forecast discipline, and I ramp fast."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of key account ownership, distributor orchestration and "
        "data-led execution to Beiersdorf's modern-trade business in the UAE. I am available to start "
        "immediately and would welcome the chance to discuss how I would approach the annual JBP cycle and "
        "shelf-execution cadence with Carrefour, Lulu and Spinneys. Thank you for your consideration — I look "
        "forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="beiersdorf-kam-modern-trade-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.beiersdorf.com/careers",
        source="company_site",
        description=JOB_DESCRIPTION,
        raw={"query": "Key Account Manager - Modern Trade - UAE",
             "recruiter": "Kartik Kulshrestha (Talent Acquisition Lead)",
             "function": "Sales", "entity": "Beiersdorf Middle East FZCO"},
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
            "Key Account Management (explicit — Miravia 42 accounts, Glovo XL)",
            "Modern trade + distributor orchestration (DoFreeze, UAE)",
            "Joint Business Planning / commercial negotiation",
            "+30% GMV QoQ track record",
            "Category management + Nielsen / sell-in-sell-out (Mondelez)",
            "Forecasting & demand shaping",
            "EPOS / IMS / Nielsen data interpretation",
            "Pricing, assortment, promo & 4P execution",
            "SAP + Nielsen in toolkit",
            "Value creation beyond price (category/shopper-led)",
            "Already in Dubai (residence visa)",
        ],
        "missing_skills": [
            "Named grocery MT tenure (Carrefour/Lulu/Spinneys) — has UAE modern trade + q-commerce, adjacent",
            "Dunnhumby (JD lists as advantage — not held)",
            "Formal S&OP process ownership (has demand-forecasting inputs)",
        ],
        "sector_fit": "strong (FMCG modern trade; beauty/personal-care adjacent to NIVEA/Eucerin)",
        "seniority_fit": "on-band (4+ yrs KAM vs 3-6 asked)",
        "red_flags": [
            "Carrefour/Lulu named-account exposure 'strongly preferred' — Paula's MT is via DoFreeze + UAE q-commerce, not a named grocery banner",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, direct fit — arguably stronger than the Eucerin ABM role. This is a core Modern-Trade "
            "Key Account Manager position (JBP, 4P by account, distributor orchestration, forecast/S&OP "
            "inputs, EPOS/Nielsen-led execution, customer budgets & reconciliation) and KAM is Paula's "
            "explicit track: 42 key accounts +30% GMV QoQ at Miravia via joint planning/assortment/pricing/"
            "promotions, modern-trade + distributor execution at DoFreeze across the UAE, XL account "
            "management at Glovo, and Nielsen category planning at Mondelez. SAP and Nielsen are genuinely "
            "in her toolkit; she's already in Dubai on a residence visa. Honest gaps: named grocery-banner "
            "tenure (Carrefour/Lulu — has adjacent UAE modern trade + quick-commerce) and Dunnhumby (an "
            "advantage, not held). Tenure sits on-band (4+ vs 3-6). Positioned truthfully as a modern-trade "
            "key account manager; no invented named-account or Dunnhumby claims."
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
