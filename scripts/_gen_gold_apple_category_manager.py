"""One-off: generate Paula's CV + cover letter for Gold Apple
"Category Manager" (Dubai, UAE — K-beauty category / beauty retail).

Strong fit. Gold Apple is a multinational omnichannel beauty retailer (Russia's
#1, 45+ stores, e-commerce = 50%+ of revenue) expanding into the GCC (UAE, Qatar,
Saudi) and doubling its brand portfolio by sourcing from Korea & Japan. The role
is a commercial Category Manager for the K-beauty category: develop/manage the
category, build brand & supplier relationships, onboard new brands, negotiate
commercial terms/pricing/margins/contracts, run assortment + pricing + the
promotional calendar, hit revenue and margin targets, analyse trends/competitors/
launches, and work cross-functionally with Marketing, Retail, E-commerce and
Supply Chain.

That maps cleanly onto Paula's real track: KAM for Beauty, Fragrances & Fashion at
Alibaba's Miravia (owned the beauty/fragrances category across 42 accounts, +30%
GMV growth QoQ via assortment/pricing/margin/promotions; led category expansion as
PIC Fragrances, onboarding & negotiating terms with 30+ brands/stores in two months
incl. Arabian Oud, Lattafa, Swiss Arabian, Ajmal), category-planning grounding at
Mondelez (sell-in/sell-out, Nielsen, promo effectiveness, planogram / assortment
gap), and omnichannel + e-commerce ownership at DoFreeze (Shopify store end-to-end,
UAE quick-commerce onboarding, distributor negotiation, NPD, margin).

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful:
  - NO invented K-beauty category tenure. Paula's beauty-category depth is
    fragrances + multibrand beauty/fashion retail (Miravia) — deep and directly
    adjacent, but not K-beauty specifically. K-beauty is positioned as a category
    she ramps into fast, never as owned tenure.
  - NO Korean language claim. The JD lists Korean as "a strong advantage" (not
    required); Paula does not speak it, so it is simply not claimed.
  - NO invented buying/procurement job title. She has genuine category management,
    assortment planning, supplier onboarding and commercial negotiation; buying /
    procurement is positioned as the same commercial muscle, not a held title.
  - VISA: already in Dubai on a UAE residence visa. Per the standing rule we NEVER
    claim "no sponsorship needed" — the visa is employer-sponsored. We only state
    she is already based in Dubai (zero relocation timeline).

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-26/.
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

COMPANY = "Gold Apple"
TITLE = "Category Manager"
DATE_FOLDER = "2026-08-26"

# Posted / advertised by Marina Tereshina (HR – Gold Apple, Middle East Team) with
# "responses managed outside LinkedIn" — she is the direct contact who reads the
# applications, so the letter is addressed to her by name.
CONTACT = "Marina Tereshina"

JOB_DESCRIPTION = """\
Category Manager — Gold Apple, Dubai, UAE (On-site, Full-Time).

A Category Manager is a crucial role in the commercial department, dealing with all
communications with vendors, distributors and beauty manufacturers, and ensuring the
availability of products to meet customer demand.

Responsibilities:
- Develop and manage the K-beauty category in line with the company's commercial strategy
- Build and maintain strong relationships with brands and suppliers
- Identify and onboard new K-beauty brands and products
- Negotiate commercial terms, pricing, margins and contractual conditions
- Manage the category assortment, pricing and promotional calendar
- Monitor sales performance, profitability and key category KPIs
- Achieve revenue and margin targets
- Analyse market trends, customer demand, competitors and new product launches
- Work closely with Marketing, Retail, E-commerce and Supply Chain teams to support
  category growth

Requirements:
- Strong knowledge of the K-beauty market, brands and current trends
- Previous experience in category management, buying, procurement or a similar role
- Experience in assortment planning and supplier management
- Strong commercial and negotiation skills
- Confident analytical skills and ability to work with sales and margin data
- Fluent English; Korean would be a strong advantage
- Results-oriented, proactive and able to work independently
- Strong communication, organisational and stakeholder management skills

Company: Gold Apple is a multinational, omnichannel beauty retailer with 11,000+
employees and 45+ beauty stores across 25 locations in 6 countries (incl. UAE, Qatar,
Saudi Arabia). E-commerce drives over 50% of revenue, supported by an award-winning
beauty app. The company doubled its brand portfolio by sourcing replacements from
Korea and Japan and is rapidly expanding its international presence in the GCC.
"""

ATS = [
    "Category Manager", "Category Management", "K-beauty", "beauty retail",
    "commercial", "vendors", "distributors", "beauty manufacturers", "suppliers",
    "supplier management", "vendor management", "brand relationships",
    "identify and onboard", "onboarding", "new brands", "product availability",
    "assortment", "assortment planning", "range", "buying", "procurement",
    "negotiate", "negotiation", "commercial terms", "pricing", "margins",
    "contractual conditions", "promotional calendar", "promotions",
    "sales performance", "profitability", "category KPIs", "revenue targets",
    "margin targets", "market trends", "customer demand", "competitors",
    "new product launches", "NPD", "Marketing", "Retail", "E-commerce",
    "Supply Chain", "category growth", "sales and margin data", "analytical",
    "stakeholder management", "omnichannel", "FMCG", "fragrances", "GCC",
    "MENA", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Category Management & Buying · Beauty & Fragrances Retail · Assortment, "
        "Pricing & Margin · Supplier Onboarding & Negotiation · Omnichannel / E-Commerce"
    ),
    "professional_summary": (
        "Category, commercial and beauty-retail professional with 4+ years across Beauty, Fragrances, "
        "Fashion and FMCG. At Alibaba's Miravia I owned the Beauty & Fragrances category across 42 accounts, "
        "growing GMV +30% QoQ through assortment optimisation, pricing, margin management and a data-led "
        "promotional calendar — and, as PIC Fragrances, identified, onboarded and negotiated terms with 30+ new "
        "brands/stores in two months. Today at DoFreeze I run assortment, pricing, distributor negotiation and "
        "an end-to-end Shopify e-commerce store across the UAE and 50+ markets, with category-planning grounding "
        "at Mondelez (sell-in/sell-out, Nielsen, promo effectiveness, assortment-gap analysis). Fluent English, "
        "already based in Dubai on a UAE residence visa, and comfortable turning sales and margin data into "
        "category decisions."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own category and assortment across the brand portfolio — building the range, pricing and promotional calendar and negotiating commercial terms, margins and listings with distributors and retail partners to hit revenue and margin targets across 50+ markets",
                "Identify and onboard products into UAE beauty/FMCG modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo) — managing listings, assortment and promo mechanics with Retail, E-commerce and Supply Chain teams to secure product availability",
                "Run the brand's Shopify e-commerce store end-to-end (catalogue, merchandising, pricing, promotions), lifting conversion and average order value — directly relevant to an omnichannel beauty retailer where e-commerce drives 50%+ of revenue",
                "Analyse sell-out, profitability and category KPIs to steer assortment decisions, close range gaps and react to competitor moves and new product launches",
                "Lead NPD end-to-end for 6 launches (assortment fit, pricing, margin, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned the Beauty & Fragrances category across 42 accounts, delivering +30% GMV growth QoQ through assortment optimisation, pricing strategy, margin management and a data-led promotional calendar",
                "Led category expansion as PIC Fragrances — identifying, onboarding and negotiating commercial terms with 30+ new brands/stores in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Built and maintained strong brand and supplier relationships, negotiating pricing, margins, promotional support and contractual conditions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing against P&L, revenue and margin targets",
                "Analysed market trends, competitors, new product launches, ROI and conversion to refine assortment, forecasting and the promotional calendar",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Onboarded fashion, beauty and lifestyle brands as Glovo built out its Retail vertical — negotiating commercial terms and building assortment beyond food delivery",
                "Managed strategic XL accounts and negotiated/closed high-impact commercial deals, maximising profitability for both platform and partners",
                "Led cross-functional teams across marketing, logistics and operations to deliver activations and grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran category deep dives — sell-in/sell-out, Nielsen performance reporting and promotional-effectiveness analysis — feeding assortment and category planning",
                "Assessed shelf share, planogram compliance and assortment gaps vs. potential to inform range recommendations",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf, translating sales and margin data into commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "category management, assortment planning, supplier & vendor management, brand onboarding, "
        "buying / procurement, commercial negotiation, pricing & margin management, promotional calendar, "
        "distributor management, stakeholder management"
    ),
    "skills_data": (
        "sales & margin data analysis, profitability & category KPIs, sell-in/sell-out, P&L management, "
        "market & competitor analysis, ROI / ROAS, forecasting, Nielsen, Power BI"
    ),
    "skills_brand": (
        "beauty & fragrances category, brand & supplier relationships, NPD end-to-end, promotional planning, "
        "shopper & trade marketing, product availability, go-to-market, A&P & trade budget management"
    ),
    "skills_ecommerce": (
        "omnichannel beauty retail, e-commerce (Shopify, Alibaba / Miravia), quick-commerce (Noon, Talabat, "
        "Careem, Deliveroo), online merchandising & assortment, conversion rate optimisation (CRO), "
        "listings & promo mechanics"
    ),
    "skills_tools": (
        "SAP, Nielsen, Salesforce, Power BI, Tableau, Kantar, Shopify, Microsoft Office (Expert), "
        "Generative AI (Claude, ChatGPT), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Gold Apple's rise from Russia's #1 beauty retailer to an omnichannel destination now expanding across "
        "the UAE, Qatar and Saudi Arabia — doubling its brand portfolio by sourcing fresh names from Korea and "
        "Japan, with e-commerce already driving over half of revenue — is exactly the kind of beauty business I "
        "want to help build. The Category Manager role caught my attention because it asks for what I do: own a "
        "beauty category end-to-end, onboard and negotiate with brands and suppliers, and turn assortment, "
        "pricing, margin and the promotional calendar into category growth."
    ),
    "body_paragraph_1": (
        "Beauty category and commercial work is the spine of my career. At Alibaba's Miravia I owned the Beauty "
        "& Fragrances category across 42 accounts and grew GMV +30% QoQ through assortment optimisation, pricing, "
        "margin management and a data-led promotional calendar — and, as PIC Fragrances, I identified, onboarded "
        "and negotiated commercial terms with 30+ new brands and stores in just two months, including the "
        "official distributors of leading Arabian and oud houses. My category grounding at Mondelez (sell-in/"
        "sell-out, Nielsen, promo effectiveness and assortment-gap analysis) means reading sales and margin data "
        "to steer a range is second nature, and at DoFreeze I now run assortment, distributor negotiation and an "
        "end-to-end Shopify e-commerce store across the UAE and 50+ markets."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, I am already in Dubai on a UAE residence visa and operating across UAE "
        "beauty/FMCG retail and quick-commerce (Noon, Talabat, Careem, Deliveroo) with a genuine omnichannel view "
        "— no relocation timeline. Second, I lead with category- and margin-led value, not just top-line. I'll be "
        "candid that my category depth has been in fragrances and multibrand beauty/fashion rather than K-beauty "
        "specifically, and I don't yet speak Korean — but I ramp fast on a category, I'm genuinely excited by "
        "K-beauty's momentum in the region, and I already speak the language of assortment, supplier onboarding, "
        "margin and promotional planning that the role runs on."
    ),
    "closing_paragraph": (
        "I would love to bring this blend of beauty-category ownership, supplier negotiation and data-led "
        "assortment to Gold Apple's K-beauty growth in the GCC. I am based in Dubai, available to start "
        "immediately, and would welcome the chance to discuss how I would develop the category, onboard new "
        "brands and manage assortment, pricing and margin. Thank you for your consideration — I look forward to "
        "hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="gold-apple-category-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/view/gold-apple-category-manager",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Category Manager", "function": "Commercial / Category Management",
             "category": "K-beauty", "channel": "Omnichannel beauty retail",
             "recruiter": "Marina Tereshina (HR – Gold Apple, Middle East Team)"},
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
        "ai_score": 86,
        "ai_tier": "Hot",
        "skills_match": [
            "Beauty & Fragrances category ownership (Miravia, 42 accounts, +30% GMV QoQ)",
            "Identify + onboard + negotiate terms with new brands/suppliers (Miravia PIC Fragrances: 30+ in 2 months)",
            "Assortment planning + pricing + promotional calendar (Miravia, DoFreeze)",
            "Commercial negotiation: terms, pricing, margins, contractual conditions",
            "Sales & margin data → category KPIs, profitability, revenue/margin targets (P&L at Miravia)",
            "Category planning grounding: sell-in/sell-out, Nielsen, promo effectiveness, assortment gap (Mondelez)",
            "Omnichannel + e-commerce (Shopify end-to-end, Alibaba/Miravia, UAE quick-commerce)",
            "Cross-functional with Marketing, Retail, E-commerce, Supply Chain (DoFreeze)",
            "Fluent English; already in Dubai (UAE residence visa)",
        ],
        "missing_skills": [
            "K-beauty-specific category tenure — has fragrances + multibrand beauty/fashion (Miravia), adjacent not identical",
            "Korean language (JD: 'strong advantage', not required) — not claimed",
            "Held 'buyer/procurement' title — has category mgmt + assortment + supplier onboarding + negotiation, adjacent",
        ],
        "sector_fit": "very strong (omnichannel beauty retail; beauty/fragrances category is Paula's core)",
        "seniority_fit": "on band (Category Manager; 4+ yrs category + KAM track)",
        "red_flags": [
            "Strong K-beauty market knowledge is the headline requirement — Paula's beauty-category depth is fragrances/multibrand beauty, K-beauty is a fast ramp not owned tenure",
            "Korean is 'a strong advantage' — Paula does not speak it",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit. Gold Apple is an omnichannel beauty retailer (e-commerce 50%+ of revenue) expanding in "
            "the GCC and doubling its portfolio with Korea/Japan sourcing; the role is a commercial Category "
            "Manager for K-beauty — develop/manage the category, build brand & supplier relationships, onboard "
            "new brands, negotiate terms/pricing/margins/contracts, run assortment + pricing + promotional "
            "calendar, hit revenue & margin targets, analyse trends/competitors/launches, and partner with "
            "Marketing/Retail/E-commerce/Supply Chain. Maps cleanly onto Paula's track: owned the Beauty & "
            "Fragrances category at Alibaba's Miravia (42 accounts, +30% GMV QoQ via assortment/pricing/margin/"
            "promotions; onboarded & negotiated with 30+ brands as PIC Fragrances), category planning at Mondelez "
            "(sell-in/sell-out, Nielsen, promo effectiveness, assortment gap), and omnichannel + e-commerce + "
            "distributor negotiation at DoFreeze (Shopify end-to-end, UAE quick-commerce). Honest gaps: K-beauty-"
            "specific tenure (has fragrances/multibrand beauty, adjacent), Korean language (not required, not "
            "claimed), and a held buyer/procurement title (has the equivalent commercial muscle). Positioned "
            "truthfully; no invented K-beauty/Korean claims and no 'no sponsorship needed' claim (she is on an "
            "employer-sponsored UAE residence visa)."
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
