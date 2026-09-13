"""One-off: generate Paula's CV tailored to the Deliveroo Hop
"Vendor / Category Manager" role (Deliveroo Hop — 24/7 digital supermarket /
grocery q-commerce), Dubai (DIFC), hybrid.

Content is authored directly (no LLM API call) and kept strictly truthful —
NO invented experience. This is a STRONG commercial/category fit and is
re-angled to lead with the genuine matches the JD asks for:
  - Category management foundation (Mondelez Category Planning: sell-in/sell-out,
    promo effectiveness, range & NPD vs plan)
  - Range / assortment / pricing & promotional-SKU work (Miravia: 42 accounts,
    +30% GMV QoQ, category expansion, Flash Sales channel with P&L)
  - Vendor / supplier sourcing, onboarding & contract negotiation (Miravia:
    onboarded 30+ vendors/distributors incl. Arabian Oud, Lattafa, Swiss
    Arabian, Ajmal; Glovo: negotiated & closed commercial deals with partners)
  - Hands-on UAE quick-commerce INCLUDING Deliveroo (DoFreeze integrates brands
    into Deliveroo/Noon/Talabat/Careem — listings, pricing, promo mechanics,
    vendor-funded media) — she knows Deliveroo's platform from the vendor side
  - Analytical toolkit: P&L, category performance vs plan, ROI/ROAS/GMV,
    Power BI / Tableau / Looker and expert spreadsheets (Excel / Gsheets)

Fills the real CV template, converts to PDF via LibreOffice headless (keeping
the editable DOCX), and lands the package under
output/2026-08-12/Deliveroo Hop - Vendor Category Manager/.

Mirrors the pattern established in scripts/_gen_noon_influencer.py.
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
from career_ops.generators._paths import job_output_dir

COMPANY = "Deliveroo Hop"
TITLE = "Vendor Category Manager"          # clean filename; real title uses a slash
TITLE_DISPLAY = "Vendor / Category Manager"
DATE_FOLDER = "2026-08-12"

JOB_DESCRIPTION = """\
Vendor / Category Manager — Deliveroo Hop, Dubai (DIFC), hybrid (3 days office),
reporting to the Senior Vendor Manager. Deliveroo Hop is Deliveroo's 24/7
digital-only supermarket: customers shop online for groceries, ingredients and
household essentials, delivered on-demand in minutes.

Responsible for the performance of a category within Deliveroo Hop — shaping the
category strategy through range selection, sourcing, pricing, cost and contract
negotiations, promotions, merchandising and marketing campaigns, and managing the
vendors within that category. Strong commercial mindset focused on driving growth
and a creative approach to problem solving.

Category Management:
- Support the Vendor Management Lead in selecting a great range of products and
  set pricing per selection & pricing principles and the Deliveroo Hop CVP.
- Ensure the right SKUs are nominated for effective, efficient promotional
  campaigns and events.
- Monitor SKU performance and optimise the range.
- Deep-dive category performance vs plan; define and execute plans to drive
  improvement and sustainable growth.

Vendor Management:
- Develop and manage relationships with local and international grocery suppliers.
- Negotiate contracts and agreements with vendors for favourable terms and
  service levels.
- Analyse vendor performance and take corrective actions to improve service and
  quality; manage vendor compliance and regulatory adherence.
- Work with the in-stock team to source new products and maintain inventory.
- Resolve vendor issues/disputes and escalations, incl. invoice, payment and
  account reconciliation.
- Monitor market trends and competitor activity to find new vendor & range
  opportunities.
- Drive media spend with vendors on the platform to promote products and enhance
  visibility.

Requirements:
- 3+ years in vendor/category management or a buying function (grocery a benefit,
  not a requirement).
- Analytical, problem-solving mindset to evaluate vendor & category performance.
- Good negotiation skills; ability to build strong vendor partnerships.
- Strong communication & interpersonal skills.
- Ability to work in a fast-paced, ambiguous environment.
- Proactive, results-driven approach to vendor management & procurement.
- Good knowledge of spreadsheets (Excel / Gsheets).
Desirable: international FMCG sourcing incl. fresh categories; BI / data tools
(SQL, Tableau, Power BI, etc.).
"""

ATS = [
    "vendor management", "category management", "buying", "range selection",
    "assortment", "pricing", "cost negotiation", "contract negotiation",
    "promotions", "promotional campaigns", "SKU nomination", "SKU performance",
    "range optimisation", "category performance vs plan", "sourcing",
    "supplier management", "vendor performance", "corrective actions",
    "vendor compliance", "in-stock", "inventory", "reconciliation",
    "market trends", "competitor analysis", "media spend", "retail media",
    "merchandising", "commercial", "growth", "negotiation", "FMCG", "grocery",
    "quick-commerce", "Deliveroo", "Noon", "Talabat", "Careem", "P&L", "GMV",
    "ROI", "ROAS", "Excel", "Gsheets", "Power BI", "Tableau", "Looker",
    "stakeholder management", "Dubai", "UAE",
]

# --------------------------------------------------------------------------
# CV content  (strictly truthful — re-angled for vendor/category management)
# --------------------------------------------------------------------------
CV_CONTENT = {
    "headline": "Category & Vendor Management · Commercial & Contract Negotiation · Quick-Commerce · FMCG",
    "professional_summary": (
        "Commercial and category professional with 4+ years across FMCG, Beauty and e-commerce, currently "
        "in Dubai. Category & buying foundation from Mondelez (category planning: sell-in/sell-out, "
        "promotional effectiveness and range vs plan), scaled into hands-on vendor and account management — "
        "42 accounts at Alibaba's Miravia grown +30% GMV QoQ through range, pricing and promotions, plus "
        "sourcing and onboarding 30+ vendors/distributors and negotiating commercial terms. At DoFreeze she "
        "integrates brands end-to-end into UAE quick-commerce including Deliveroo — managing range, listings, "
        "pricing, promotional mechanics and vendor-funded media — so she already knows the Deliveroo platform "
        "from the vendor side. Strong on negotiation, P&L, category performance vs plan, ROI/ROAS, BI "
        "(Power BI/Tableau/Looker) and expert spreadsheets (Excel/Gsheets). Already in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Integrate and grow brands end-to-end across UAE quick-commerce — Deliveroo, Noon, Talabat and Careem — owning range/listings, pricing, promotional-SKU selection and retail execution to drive sell-out (the exact platform side this role sits opposite)",
                "Source products and manage vendor/distributor relationships across modern trade and quick-commerce, negotiating terms and service levels and resolving listing, pricing and supply issues to keep ranges live and in stock",
                "Nominate SKUs for promotional campaigns and events, build channel/category promo calendars and drive vendor-funded on-platform media to lift product visibility and conversion",
                "Deep-dive category and SKU performance vs plan, optimise the range and reallocate investment — analysing ROI, ROAS and sell-out to define corrective actions and sustainable growth plans",
                "Develop trade & shopper marketing plans by channel and category, supporting key-account strategy and NPD go-to-market across 50+ markets",
                "Built an AI-powered automation system (Claude/GPT) for category reporting, competitor/market tracking and KPI dashboards, cutting manual workload ~40% and speeding decisions",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts, achieving +30% GMV growth QoQ through range selection, assortment optimisation, pricing strategy and targeted promotions — classic category management on a marketplace",
                "Led category expansion as PIC Fragrances — sourcing, negotiating and onboarding 30+ new vendors/stores in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Owned the Flash Sales channel for Beauty, Fashion & Home with full P&L, reporting to the CEO — nominating the right SKUs and vendors for each event and executing commercial plans to hit targets",
                "Analysed vendor and category performance (ROI, ROAS, conversion, traffic, retention) to take corrective actions, optimise the range and improve forecasting accuracy",
                "Negotiated commercial agreements, promotional co-investment and service levels with brands and distributors, resolving pricing, stock and account issues to protect margin and availability",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Negotiated and closed high-impact commercial deals with partners — terms, deliverables and service levels — maximising profitability for both platform and vendor",
                "Sourced and onboarded fashion and lifestyle brands as Glovo expanded its q-commerce marketplace beyond food, growing range, order volume and category coverage",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning and bespoke activations",
                "Coordinated cross-functional teams across marketing, logistics and customer support — including stock and operations — to keep campaigns and availability on track",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and category performance analysis vs plan for the chocolate category, building reports that surfaced range and growth opportunities",
                "Evaluated promotional effectiveness and pricing/promo mechanics to inform range and investment decisions",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf, working across commercial and category teams",
            ],
        },
    ],
    "skills_commercial": (
        "category management, vendor & supplier management, sourcing & vendor onboarding, contract & "
        "commercial negotiation, pricing strategy, range & assortment planning, promotional-SKU selection, "
        "key account management, distributor management, modern trade, forecasting"
    ),
    "skills_data": (
        "category performance vs plan, sell-in/sell-out, SKU & vendor performance analysis, P&L management, "
        "ROI, ROAS, GMV, KPI tracking, Power BI, Tableau, Looker, Nielsen, Kantar, expert spreadsheets (Excel / Gsheets)"
    ),
    "skills_ecommerce": (
        "quick-commerce (Deliveroo, Noon, Talabat, Careem), listing & catalogue management, promotional "
        "mechanics, vendor-funded / retail media, merchandising, Shopify, Meta Ads, Google Ads, marketing automation"
    ),
    "skills_brand": (
        "trade marketing, shopper marketing, promotions & campaign planning, NPD end-to-end, go-to-market, "
        "A&P & promo budget management, brand strategy, generative-AI automation"
    ),
    "skills_tools": (
        "Excel / Google Sheets (Expert), Power BI, Tableau, Looker, Nielsen, Kantar, SAP, Salesforce, "
        "Generative AI (Claude, ChatGPT), Canva, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="deliveroo-hop-vendor-category-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.deliveroo.co.uk/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Vendor / Category Manager",
             "via": "LinkedIn / Deliveroo Careers",
             "team": "Deliveroo Hop", "office": "Dubai — DIFC (hybrid, 3 days)"},
    )


def _convert_pdf(docx_path: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice headless (reliable, non-interactive).

    Keeps the editable DOCX alongside the PDF.
    """
    pdf_path = docx_path.with_suffix(".pdf")
    try:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", "--outdir",
             str(docx_path.parent), str(docx_path)],
            check=True, capture_output=True, timeout=120,
        )
    except Exception as exc:  # noqa: BLE001
        print("WARN pdf conversion failed:", type(exc).__name__, exc)
    return pdf_path


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id,
        "title": TITLE_DISPLAY,
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
        "ai_score": 88,
        "ai_tier": "Hot",
        "skills_match": [
            "Category management foundation (Mondelez Category Planning)",
            "Range / assortment / pricing / promo-SKU (Miravia, +30% GMV QoQ)",
            "Vendor sourcing, onboarding & contract negotiation (30+ vendors)",
            "Commercial deal negotiation & service levels (Glovo)",
            "Hands-on UAE quick-commerce incl. Deliveroo (DoFreeze)",
            "Category performance vs plan, ROI/ROAS/GMV, P&L",
            "Power BI / Tableau / Looker + expert Excel/Gsheets",
            "3+ yrs commercial/category experience",
            "Already in Dubai (residence visa, DIFC-accessible)",
        ],
        "missing_skills": [
            "Grocery-specific buying (benefit, not required)",
            "SQL (desirable, not required)",
        ],
        "sector_fit": "strong (FMCG / grocery q-commerce)",
        "seniority_fit": "exact (3+ yrs vendor/category)",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong commercial/category fit: the JD wants 3+ yrs in vendor/category management or buying, "
            "range/pricing/promo-SKU work, contract negotiation, vendor sourcing & performance, category "
            "deep-dives vs plan, analytical BI/spreadsheet skills and a growth mindset in a fast-paced "
            "environment. Paula has the category-planning foundation (Mondelez), ran category management on "
            "a marketplace (Miravia: 42 accounts, +30% GMV QoQ, 30+ vendors onboarded, Flash Sales P&L), "
            "negotiated & closed commercial deals (Glovo), and today integrates brands into Deliveroo + UAE "
            "q-commerce at DoFreeze — she knows the platform from the vendor side, the exact counterpart to "
            "this role. BI (Power BI/Tableau/Looker) + expert Excel/Gsheets. Grocery buying and SQL are "
            "desirables she partly lacks but both are explicitly non-blocking. Dubai residence visa."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


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
    print("STEP registered in dashboard")

    cv_docx = cv._fill_template(CV_CONTENT, job)
    print("STEP CV docx built:", cv_docx.name)

    cv_pdf = _convert_pdf(cv_docx)
    print("STEP CV pdf built:", cv_pdf.name)

    pos_dir = job_output_dir(job)  # output/<Company> - <Role>/
    final_dir = _relocate_to_dated_folder(pos_dir)

    cvd = final_dir / "01_CV_y_Carta" / cv_docx.name
    cvp = final_dir / "01_CV_y_Carta" / cv_pdf.name
    print("OK_CV_DOCX", cvd.name, "(exists)" if cvd.exists() else "(MISSING)")
    print("OK_CV_PDF", cvp.name, "(exists)" if cvp.exists() else "(MISSING)")
    print("FINAL_DIR", final_dir)


if __name__ == "__main__":
    main()
