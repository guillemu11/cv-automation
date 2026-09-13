"""One-off: generate Paula's CV + Cover Letter for the Deliveroo
"Vendor / Category Manager — Deliveroo Hop UAE" role (Dubai, DIFC, hybrid).

Deliveroo Hop is Deliveroo's 24/7 digital-only supermarket (grocery q-commerce).
The role owns the performance of a CATEGORY: range selection, sourcing, pricing,
cost/contract negotiation, promotions, merchandising and marketing — plus VENDOR
management (supplier relationships, contract negotiation, performance/compliance,
sourcing, in-stock coordination, driving vendor media spend on platform). Asks for
3+ yrs in vendor/category management or buying (grocery a benefit, NOT a
requirement), an analytical/problem-solving mindset, negotiation + communication,
comfort in a fast-paced/ambiguous environment, and Excel/Gsheets. Desirable:
international FMCG/fresh sourcing, and BI tools (SQL, Tableau, Power BI).

Paula's fit is strong and squarely commercial (not marketing-only):
- **Category muscle is real and documented.** Started in **Category & Commercial
  Planning at Mondelez** (sell-in/sell-out, promo effectiveness, category reports
  for chocolate). At **Miravia (Alibaba)** she optimised assortment + pricing +
  promotions across a 42-account portfolio to **+30% GMV QoQ** and led category
  expansion as PIC Fragrances, sourcing/onboarding 30+ vendors in two months.
- **Vendor side is credible.** At **Glovo** she helped build the Retail vertical —
  sourcing/onboarding brand partners and **negotiating and closing commercial
  deals/contracts**. At **DoFreeze** she manages distributor/supplier relationships
  across 50+ markets and drives vendor-funded activations.
- **Quick-commerce native.** Today at DoFreeze she owns range, pricing, SKU
  nomination, promo mechanics and retail execution across **Deliveroo, Noon,
  talabat and Careem** — the exact platform world of Deliveroo Hop.
- **Analytics + tools** the JD names: Excel/Gsheets (Expert), Power BI, Tableau.

Honest gaps (surfaced, not hidden): grocery/fresh *buy-side sourcing* specifically
is the newest part of the brief (her sourcing is NPD/brand + partner onboarding),
and she does not use SQL (has Power BI/Tableau). Neither is blocking — grocery is
explicitly "a benefit, not a requirement" and SQL is only "desirable".

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience, NO Arabic claim, and NO "no sponsorship needed"
claim (Paula's residence visa is employer-sponsored). Fills the real CV and
cover-letter templates, converts to PDF with LibreOffice soffice (docx2pdf/Word is
unreliable headless on this Mac), and lands the package under
output/2026-08-25/Deliveroo - Vendor & Category Manager - Deliveroo Hop/.
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

COMPANY = "Deliveroo"
TITLE = "Vendor & Category Manager - Deliveroo Hop"
DATE_FOLDER = "2026-08-25"
CONTACT = None  # no named contact yet → "Hiring Manager"

JOB_DESCRIPTION = """\
Vendor / Category Manager — Deliveroo Hop, Dubai (DIFC), UAE (Hybrid).

Deliveroo Hop is Deliveroo's 24/7 supermarket — a digital-only experience that lets
customers shop online for all their groceries, ingredients, household essentials and
more, on-demand and delivered in minutes.

Role overview: As Vendor / Category Manager you are responsible for the performance
of a category within Deliveroo Hop. Working closely with the Vendor Management Lead,
you shape category strategy through range selection, sourcing, pricing, cost and
contract negotiations, promotions, merchandising and marketing campaigns, as well as
managing the vendors within that category. Reports to the Senior Vendor Manager.

Category Management:
- Support the Vendor Management Lead in selecting a great range of products and set
  pricing, per selection and pricing principles and in line with the Hop CVP.
- Ensure the right SKUs are nominated for effective and efficient promotional
  campaigns and events.
- Monitor SKU performance and optimise the range.
- Deep dive category performance vs plan and define/execute plans to drive
  improvement and sustainable growth.

Vendor Management:
- Develop and manage relationships with local and international grocery suppliers.
- Negotiate contracts and agreements with vendors for favourable terms/service levels.
- Analyse vendor performance and take corrective actions to improve service/quality.
- Manage vendor compliance and adherence to regulatory requirements.
- Work with the in-stock team to source new products and maintain inventory levels.
- Resolve vendor issues/disputes/escalations (invoice, payment, account reconciliation).
- Monitor market trends and competitor activity to identify new vendor/range opportunities.
- Drive media spend with vendors on the platform to promote products and enhance visibility.

Requirements:
- 3+ years experience in vendor/category management or a buying function (grocery
  experience a benefit but NOT a requirement).
- Analytical and problem-solving mindset to evaluate vendor/category performance.
- Good negotiation skills and the ability to build strong vendor partnerships.
- Strong communication and interpersonal skills to collaborate with internal teams.
- Ability to work in a fast-paced, ambiguous environment and adapt to change.
- Proactive, results-driven approach to vendor management and procurement.
- Good knowledge of spreadsheets (Excel / Gsheets).

Desirable: international FMCG sourcing and sourcing of fresh categories; knowledge of
BI/data-analytics tools like SQL, Tableau, Power BI.
"""

ATS = [
    "vendor management", "category management", "vendor/category manager", "buying",
    "buyer", "sourcing", "procurement", "range selection", "assortment",
    "assortment planning", "pricing", "pricing strategy", "cost negotiation",
    "contract negotiation", "supplier management", "vendor onboarding",
    "vendor performance", "vendor compliance", "promotions", "promotional campaigns",
    "SKU nomination", "SKU performance", "range optimisation", "category strategy",
    "category performance", "deep dive vs plan", "merchandising", "in-stock",
    "inventory levels", "account reconciliation", "retail media",
    "drive media spend with vendors", "market trends", "competitor analysis",
    "grocery", "FMCG", "fresh categories", "quick-commerce", "q-commerce",
    "grocery delivery", "Deliveroo Hop", "Deliveroo", "Noon", "talabat", "Careem",
    "modern trade", "distributor management", "key account management", "negotiation",
    "commercial", "P&L", "margin", "profitability", "ROI", "ROAS", "GMV",
    "sell-in/sell-out", "forecasting", "data analysis", "problem-solving",
    "Excel", "Google Sheets", "Gsheets", "Power BI", "Tableau", "Looker",
    "cross-functional", "stakeholder management", "fast-paced", "GCC", "UAE", "Dubai",
]

CONTENT = {
    "headline": (
        "Category & Vendor Management · Quick-Commerce & FMCG · "
        "Range, Pricing, Sourcing & Promotions · Dubai / UAE"
    ),
    "professional_summary": (
        "Commercial and category management professional with 4+ years across FMCG, quick-commerce, beauty "
        "and e-commerce in the GCC and Europe. I started in Category & Commercial Planning at Mondelez "
        "(sell-in/sell-out, promotional effectiveness and category reporting), then grew a 42-account portfolio "
        "at Alibaba's Miravia to +30% GMV QoQ by optimising assortment, setting pricing and building promotional "
        "calendars, and helped build Glovo's Retail vertical — sourcing/onboarding vendors and negotiating the "
        "commercial deals behind them. Today at DoFreeze I own range, pricing, SKU nomination, promotional "
        "mechanics and vendor-funded activations across the UAE's quick-commerce platforms — Deliveroo, Noon, "
        "talabat and Careem. Analytical and negotiation-led, an Excel/Gsheets and Power BI/Tableau power user, "
        "already in Dubai on a UAE residence visa; bilingual Spanish/English."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own category and go-to-market across the UAE's quick-commerce platforms — Deliveroo, Noon, talabat and Careem — managing range/listings, pricing, promotional mechanics and retail execution to drive SKU performance and sell-out",
                "Lead NPD and range end-to-end for 6 launches (brief, sourcing, packaging, pricing, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa — selecting the right assortment and price for each market",
                "Manage distributor and supplier relationships across 50+ markets — negotiating terms and joint activations, monitoring performance, and taking corrective action to grow the category",
                "Nominate SKUs for promotional campaigns and drive vendor-funded media and activations on platform to lift product visibility and conversion",
                "Track category and channel performance against plan (ROI, ROAS, conversion, sell-out) with an AI (Claude/GPT) reporting system, deep-diving underperformance and executing plans to improve",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Optimised assortment and pricing across a 42-account portfolio to +30% GMV QoQ — selecting range, setting pricing and building promotional calendars that grew each category",
                "Led category expansion as PIC Fragrances, sourcing and onboarding 30+ new vendors in two months — including the official distributors of leading Arabian oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Owned the Flash Sales channel end-to-end — nominating SKUs and negotiating promotional terms with brands — and reported performance directly to the CEO",
                "Analysed category and vendor performance continuously (traffic, conversion, retention, ROI) to optimise the range and defend margin",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts (Retail vertical build-out)",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce & food-delivery leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical — sourcing and onboarding new brand/vendor partners onto the marketplace and expanding assortment beyond food into apparel, beauty and non-food categories",
                "Negotiated and closed high-impact commercial deals and contracts, maximising profitability for both Glovo and its partners",
                "Managed strategic accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), using performance data to build activations that grew order volume and GMV",
                "Worked cross-functionally with marketing, logistics/in-stock and operations to keep assortment live and campaigns running in a fast-moving environment",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out analysis, evaluated promotional effectiveness and built category performance reports for the chocolate category — core category-management analytics",
                "Identified range and growth opportunities and contributed to NPD launches (Milka Spread, Mini Suchard), turning category data into range decisions",
            ],
        },
    ],
    "skills_brand": (
        "category strategy, range & assortment planning, promotional planning, "
        "trade & shopper marketing, go-to-market, NPD & sourcing, merchandising, "
        "retail media / vendor-funded activations"
    ),
    "skills_ecommerce": (
        "quick-commerce & grocery q-commerce (Deliveroo, Noon, talabat, Careem), marketplaces "
        "(Miravia, AliExpress), listings & SKU management, promotional mechanics, retail execution, "
        "in-stock / inventory coordination, Meta & Google Ads"
    ),
    "skills_commercial": (
        "vendor & supplier management, category management, buying & sourcing, contract & commercial "
        "negotiation, pricing strategy, vendor onboarding, distributor management, key account management, "
        "vendor performance management, cross-functional stakeholder management"
    ),
    "skills_data": (
        "category & vendor performance analysis, sell-in/sell-out, SKU & range optimisation, P&L & margin, "
        "KPI tracking & reporting, ROI, ROAS, GMV, forecasting, AI-assisted analysis, "
        "Power BI, Tableau, Looker, Nielsen, Kantar"
    ),
    "skills_tools": (
        "Excel / Google Sheets (Expert), Power BI, Tableau, Looker, Generative AI (Claude / ChatGPT), "
        "Salesforce, SAP, Nielsen, Kantar, Planorama"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Deliveroo Hop's model — a 24/7 digital-only supermarket where the right range, pricing and promotions "
        "decide whether a category grows — is the exact world I work in every day. At DoFreeze I own category "
        "and go-to-market across the UAE's quick-commerce platforms, Deliveroo included, and before that I grew "
        "category portfolios at Alibaba's Miravia and helped build Glovo's Retail vertical. I would be thrilled "
        "to bring that to Deliveroo Hop as Vendor / Category Manager."
    ),
    "body_paragraph_1": (
        "My category muscle is well-built. I started in Category & Commercial Planning at Mondelez, running "
        "sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, then grew a "
        "42-account portfolio at Miravia to +30% GMV QoQ by optimising assortment, setting pricing and building "
        "promotional calendars — sourcing and onboarding 30+ new vendors in two months as category lead for "
        "Fragrances. At Glovo I helped build the Retail vertical, sourcing and onboarding brand partners and "
        "negotiating the commercial deals and contracts behind them. Today at DoFreeze I own range, pricing, SKU "
        "nomination and vendor-funded activations across Deliveroo, Noon, talabat and Careem — so I know the "
        "platform mechanics behind this role from the inside."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, I know quick-commerce from within — I manage brand categories on "
        "Deliveroo and its UAE peers now, so I read SKU performance, pull the right promo levers and act on the "
        "data. Second, I am analytical and commercial in equal measure: fluent in sell-in/sell-out, ROI and "
        "margin, an Excel/Gsheets and Power BI/Tableau power user, and a confident negotiator across vendors and "
        "distributors. Grocery and fresh sourcing would be the newest part of the brief, and I am genuinely "
        "excited to go deep there. I am already in Dubai on a UAE residence visa, so there is no relocation, and "
        "I am bilingual Spanish/English."
    ),
    "closing_paragraph": (
        "I would welcome the chance to talk through how I would approach a category at Deliveroo Hop — range, "
        "pricing, promotions and vendor growth — and can share a short view on a category on request. I am "
        "available to start quickly. Thank you for your consideration; I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="deliveroo-vendor-category-manager-hop-uae-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/ (Deliveroo Hop — Vendor / Category Manager, DIFC, hybrid)",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Vendor Category Manager Deliveroo Hop Dubai grocery q-commerce",
            "via": "LinkedIn (promoted by recruiter; responses managed outside LinkedIn)",
            "department": "Deliveroo Hop — Vendor Management, UAE",
            "work_model": "Hybrid (3 days/week, DIFC)",
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
        "salary_raw": None,
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 88,
        "ai_tier": "Hot",
        "skills_match": [
            "Category management is documented, not a stretch: Category & Commercial Planning at Mondelez (sell-in/sell-out, promo effectiveness, category reporting)",
            "Assortment + pricing + promotions across a 42-account portfolio to +30% GMV QoQ at Miravia (Alibaba)",
            "Sourcing & onboarding 30+ vendors in two months as category lead (PIC Fragrances, Miravia)",
            "Vendor side credible: built Glovo's Retail vertical — sourced/onboarded partners and negotiated & closed commercial deals/contracts",
            "Quick-commerce native: owns range, pricing, SKU nomination, promo mechanics & retail execution on Deliveroo/Noon/talabat/Careem today (DoFreeze) — the Deliveroo Hop platform world",
            "Drives vendor-funded media/activations on platform (matches JD 'drive media spend with vendors')",
            "Analytical + tools the JD names: Excel/Gsheets (Expert), Power BI, Tableau; fluent in ROI/margin/forecasting",
            "3+ yrs asked; Paula 4+ — on band. Already in Dubai on UAE residence visa (no relocation)",
        ],
        "missing_skills": [
            "Grocery/fresh BUY-SIDE sourcing specifically is the newest part of the brief (her sourcing is NPD/brand + partner onboarding, not grocery procurement) — but grocery is explicitly 'a benefit, not a requirement'",
            "SQL not used (has Power BI/Tableau) — SQL is only 'desirable'",
            "Experience skews sell-side/partner-side vs pure buy-side procurement — skills transfer (negotiation, performance analysis, contract terms)",
        ],
        "sector_fit": "excellent (grocery quick-commerce category/vendor management — Paula manages brand categories on Deliveroo & UAE q-commerce today; Glovo is the same platform model)",
        "seniority_fit": "on-band (3+ yrs asked; Paula 4+). Role is 'support the Vendor Management Lead' / reports to Senior Vendor Manager — mid level, slight lateral vs her Manager ambition, but Deliveroo + priority platform",
        "red_flags": [
            "High competition: 5,000+ applicants clicked Apply, recruiter-promoted, 'responses managed outside LinkedIn' — Easy Apply alone won't cut through; pair with direct recruiter/hiring-manager outreach",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, squarely-commercial fit (~8/10). Unlike a marketing-only role, this plays to Paula's category "
            "and vendor experience: Category & Commercial Planning at Mondelez; assortment/pricing/promotions to "
            "+30% GMV QoQ across 42 accounts at Miravia with 30+ vendors sourced/onboarded as category lead; "
            "vendor sourcing, onboarding and contract negotiation building Glovo's Retail vertical; and, today at "
            "DoFreeze, ownership of range, pricing, SKU nomination, promo mechanics and vendor-funded activations "
            "across Deliveroo/Noon/talabat/Careem — the exact Deliveroo Hop platform world. She hits the named "
            "requirements (3+ yrs, analytical, negotiation, Excel/Gsheets) and desirables she has (Power BI, "
            "Tableau). Non-blocking gaps: grocery/fresh buy-side sourcing specifically (explicitly 'a benefit, not "
            "a requirement') and SQL ('desirable'); her background skews sell/partner-side vs pure buy-side "
            "procurement, though the negotiation and performance-analysis skills transfer. Given 5,000+ applicants "
            "and off-LinkedIn response handling, apply via the official channel AND pair with direct outreach."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX → PDF with LibreOffice headless (docx2pdf/Word fails on this Mac)."""
    subprocess.run(
        [
            "soffice", "--headless", "--convert-to", "pdf",
            "--outdir", str(docx_path.parent), str(docx_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    pdf_path = docx_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError(f"soffice did not produce {pdf_path}")
    return pdf_path


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

    cv_docx = cv._fill_template(CONTENT, job)
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
