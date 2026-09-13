"""One-off: generate Paula's CV + cover letter for Unilever
"Key Account Executive - Home Care" (Dubai, UAE — Modern Trade / Sales).

Sibling posting to the Unilever "Key Account Executive - Personal Care" role
(already packaged 2026-08-25). Same job family: a Modern-Trade Key Account
Executive owning assigned UAE accounts. This posting names its customer cluster
(Cluster 3: Nesto, Sharjah Coops, Westone, Union Coops & Choithram) and — despite
the "Home Care" title — its Experiences & Qualifications section asks for
"3-5 years of UAE Health & Beauty market experience... preferably within FMCG or
key beauty brands." That requirement actually plays to Paula's strength: 42
beauty/fragrance key accounts at Alibaba's Miravia (+30% GMV QoQ). So the package
leads with Health & Beauty + Modern-Trade key account management, backed by UAE
modern-trade execution at DoFreeze and category planning at Mondelez.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful:
  - NO invented Home-Care (detergents/cleaning) category tenure. Her depth is
    beauty/fragrances (Miravia) and food FMCG (DoFreeze/Mondelez); home care is
    positioned as adjacent FMCG modern trade, never as owned tenure.
  - The "Health & Beauty" requirement is met HONESTLY via her real beauty/
    fragrance key-account track at Miravia (Spain e-commerce) — flagged as such,
    not misrepresented as UAE brick-and-mortar H&B tenure.
  - NO invented named-account tenure (Nesto / coops / Choithram). She runs UAE
    modern trade + quick-commerce via DoFreeze — adjacent, positioned as such.
  - NO UAE driving-license claim. The JD lists it as "typically required"; we do
    not claim it (Paula to confirm separately).
  - VISA: already in Dubai on a UAE residence visa. Per the standing rule we NEVER
    claim "no sponsorship needed" — the visa is employer-sponsored. We only state
    she is already based in Dubai (zero relocation timeline).

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-27/.
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
TITLE = "Key Account Executive - Home Care"
DATE_FOLDER = "2026-08-27"

# Promoted by a recruiter; "Muhammad Hamza" is a network connection, not the
# hiring manager, so the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Key Account Executive - Home Care — Unilever, Dubai, UAE (On-site, Full-Time).

Job Purpose: drive sustainable sales growth and brand presence in the UAE by
managing key accounts, executing category-specific strategies and delivering a
seamless customer experience aligned with company objectives. Customers in
Cluster 3 include: Nesto, Sharjah Coops, Westone, Union Coops & Choithram.

Main Responsibilities: manage and grow sales across assigned UAE-based accounts;
develop and implement localized sales plans, promotions and trade initiatives
tailored to the UAE market; build and maintain strong relationships with key retail
partners and distributors; ensure optimal product availability, visibility and
planogram in stores; analyse sales performance, shopper behaviour and competitor
activity within the UAE retail landscape; negotiate pricing, listings, promotional
support and in-store execution with key accounts; monitor and report on key KPIs
including sell-in/sell-out data, market share and ROI on trade spend; unlock white
spaces and opportunities within the trade.

What You Need To Succeed: deep understanding of the UAE market and key players;
knowledge of shopper behaviour, cultural preferences and local regulations; strong
sales and negotiation skills (close deals, negotiate terms, secure prime shelf
placements); experience driving sell-in and sell-out performance; oversee stock
inventory at the customer end; relationship management with retail partners and
distributors; execution excellence (flawless promotions, displays, merchandising,
in-store visibility); data-driven mindset (POS data, market trends, consumer
insights; Nielsen, Power BI or Excel to track performance and market share);
adaptability and initiative in a fast-paced multicultural market; unlock white
spaces; collaboration cross-functionally with marketing, trade marketing, supply
chain and finance; communication and presentation (compelling pitches and reports
to internal and external stakeholders); quarterly business reviews (QBR) with
customers to ensure business stability and alignment.

KPIs: monthly sales target delivery by customer and category; full-year growth for
the cluster/category; increasing brand listing, availability and space across the
channel; market-share gain in the cluster/customer; maintain positive OSA, share of
folder, service level and healthy stock inventory.

Experiences & Qualifications: Bachelor's degree in Business Administration,
Marketing or a related field; fluent in English; valid UAE driving license is
typically required; 3-5 years of UAE Health & Beauty market experience in
sales/account management, preferably within FMCG or key beauty brands; solid
knowledge of UAE retail dynamics, shopper trends and major retail groups.

Skills: proven ability to achieve targets and grow market share in a competitive
environment; strong interpersonal, communication and negotiation skills with
multicultural fluency; proficient in data analysis and sales reporting (Nielsen,
POS data, Excel/Power BI); experience working with distributors and Health & Beauty
partners in the UAE is preferred.
"""

ATS = [
    "Key Account Executive", "Key Account Management", "Modern Trade", "MT",
    "FMCG", "Health & Beauty", "beauty", "home care", "sales growth",
    "assigned accounts", "localized sales plans", "promotions", "trade initiatives",
    "retail partners", "distributors", "distributor management", "product availability",
    "visibility", "planogram", "shelf placement", "sales performance",
    "shopper behaviour", "competitor activity", "UAE retail", "negotiate pricing",
    "listings", "promotional support", "in-store execution", "sell-in", "sell-out",
    "market share", "ROI on trade spend", "trade spend", "white spaces",
    "POS data", "Nielsen", "Power BI", "Excel", "consumer insights",
    "execution excellence", "merchandising", "displays", "OSA",
    "on-shelf availability", "share of folder", "service level", "stock inventory",
    "QBR", "quarterly business review", "cross-functional", "trade marketing",
    "category management", "negotiation", "multicultural", "target achievement",
    "GCC", "MENA", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Key Account Management · Modern Trade · FMCG / Health & Beauty · "
        "Sell-out, Market Share & Trade ROI · Negotiation & In-store Execution"
    ),
    "professional_summary": (
        "Commercial and key account professional with 4+ years across FMCG, Beauty & Fragrances and "
        "E-Commerce. Currently drive modern-trade execution for DoFreeze (Befit, Eurocake, Flair) across the "
        "UAE — managing assigned accounts, availability, visibility, planogram, retailer promotions and "
        "in-store execution. Previously owned 42 beauty, fragrance and fashion key accounts at Alibaba's "
        "Miravia, delivering +30% GMV growth QoQ through pricing, assortment and targeted promotions, with "
        "category-planning grounding at Mondelez (sell-in/sell-out, Nielsen, promo effectiveness). Strong in "
        "negotiation, distributor management and sell-out/market-share analysis; multicultural, fluent English, "
        "and already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Manage and grow sales across assigned UAE accounts — building localized sales plans, promotions and trade initiatives, and negotiating listings, pricing and promotional support with key retail partners and distributors",
                "Ensure optimal product availability, visibility and planogram in store — driving on-shelf availability (OSA), prime shelf placement, displays and flawless in-store execution",
                "Analyse sell-in/sell-out, market share and competitor activity across the UAE retail landscape, tracking ROI on trade spend and preparing performance reports and reviews for internal and customer stakeholders",
                "Oversee stock inventory at the customer end and unlock white spaces — identifying assortment gaps vs. potential and range opportunities to grow listing, availability and space across the channel",
                "Run a true omnichannel account footprint across modern trade and UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), collaborating cross-functionally with marketing, trade marketing, supply chain and finance",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned 42 beauty, fragrance and fashion key accounts, delivering +30% GMV growth QoQ (ahead of category) and growing market share through pricing strategy, assortment optimisation and targeted promotions",
                "Led category expansion as PIC Fragrances, onboarding 30+ accounts in two months — including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — via trend-driven, value-creating assortment",
                "Negotiated commercial terms, listings and promo plans — owning the Flash Sales channel, reporting to the CEO and executing against P&L targets",
                "Ran monthly category, pricing and competitor deep dives, turning market-share, promo and launch data into corrective actions and clear recommendations for accounts and buyers",
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
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf and translated Nielsen / POS-style data into commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "key account management, modern trade, distributor management, sales & negotiation, listings & "
        "pricing negotiation, assortment planning, category management, planogram & shelf placement, "
        "joint business planning (JBP), white-space development"
    ),
    "skills_data": (
        "sell-in/sell-out analysis, market-share tracking, Nielsen, POS data, ROI on trade spend, category "
        "deep dives, promo ROI, secondary-sales analysis, P&L management, KPI reporting, Power BI"
    ),
    "skills_brand": (
        "trade marketing, shopper marketing, in-store execution & visibility, displays & merchandising, "
        "customer events & activation, A&P & trade budget management, promotional planning, go-to-market"
    ),
    "skills_ecommerce": (
        "modern trade + quick-commerce (Noon, Talabat, Careem, Deliveroo), on-shelf availability & listing "
        "compliance, omnichannel retail execution, listings & promo mechanics, product master data"
    ),
    "skills_tools": (
        "Nielsen, SAP, Microsoft Excel (Advanced), PowerPoint (Advanced), Power BI, Salesforce, "
        "Generative AI (Claude, ChatGPT), Kantar, Planorama, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Unilever's conviction that doing business the right way drives superior performance — carried by "
        "brands people genuinely love — is exactly the kind of business I want to help grow on the UAE modern-"
        "trade shelf. The Key Account Executive – Home Care role fits what I do every week: manage and grow "
        "assigned UAE accounts, negotiate listings, pricing and promotions, keep availability, visibility and "
        "planograms honest, and turn sell-out, market-share and trade-spend ROI into decisions — the ownership "
        "you'll want across Cluster 3 customers like Nesto, the co-ops and Choithram."
    ),
    "body_paragraph_1": (
        "Key account management is the spine of my career, and it maps directly onto your Health & Beauty "
        "requirement. At Alibaba's Miravia I owned 42 beauty, fragrance and fashion key accounts and grew GMV "
        "+30% QoQ — ahead of category — through pricing, assortment and targeted promotions, negotiating terms "
        "and listings and reporting channel P&L to the CEO; as PIC Fragrances I onboarded 30+ accounts in two "
        "months, including the official distributors of Arabian Oud, Lattafa, Swiss Arabian and Ajmal. Today at "
        "DoFreeze I run modern-trade execution across UAE accounts — availability, visibility, planogram, "
        "promotions, in-store execution and trade-spend ROI — and my category grounding at Mondelez "
        "(sell-in/sell-out, Nielsen, promo effectiveness) means POS and market-share data are already how I "
        "build account actions."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, I am already in Dubai on a UAE residence visa and operating inside UAE "
        "modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo) — a multicultural account view from "
        "day one, available immediately with no relocation timeline. Second, I lead with market-share and "
        "category-led value, not just price. I'll be candid that my hands-on category depth has been in "
        "beauty/fragrances and food FMCG rather than home care specifically — but I already speak the language "
        "of listings, planograms, trade ROI and sell-out-led corrective action, and I ramp fast on a new "
        "category and customer set."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of key account ownership, negotiation and data-led execution to "
        "Unilever's Home Care business in the UAE. I am available to start immediately and would welcome the "
        "chance to discuss how I would approach the cluster sales plan, promotion ROI and shelf execution across "
        "Nesto, the co-ops, Westone and Choithram. Thank you for your consideration — I look forward to hearing "
        "from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="unilever-kae-home-care-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.unilever.com",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Key Account Executive - Home Care",
             "function": "Sales / Customer Development", "entity": "Unilever Gulf FZE",
             "channel": "Modern Trade", "cluster": "Cluster 3",
             "customers": "Nesto, Sharjah Coops, Westone, Union Coops, Choithram"},
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
            "Key Account Management (Miravia 42 accounts +30% GMV QoQ, Glovo XL)",
            "Beauty & Fragrances key-account depth → maps to JD's 'Health & Beauty' requirement",
            "Modern-trade execution across UAE accounts (DoFreeze)",
            "Sales & negotiation: listings, pricing, promotional support, in-store execution",
            "Sell-in/sell-out, market share, competitor & POS analysis (Nielsen, Power BI)",
            "ROI on trade spend + trade budget management",
            "Distributor management + retail-partner relationships",
            "Planogram, visibility, OSA & white-space development",
            "Category planning grounding (Mondelez: Nielsen, promo effectiveness)",
            "Multicultural, fluent English, already in Dubai (UAE residence visa)",
        ],
        "missing_skills": [
            "UAE driving license — JD lists as 'typically required'; Paula to confirm (NOT claimed in CV)",
            "Home-care (detergents/cleaning) category tenure — has beauty/fragrances + food FMCG, adjacent",
            "3-5 yrs UAE Health & Beauty specifically — beauty key-account depth is Spain e-commerce (Miravia); UAE tenure is FMCG modern trade (DoFreeze)",
            "Named grocery/co-op banner tenure (Nesto/Choithram/coops) — has UAE modern trade + q-commerce via DoFreeze, adjacent",
        ],
        "sector_fit": "strong (FMCG modern trade; beauty/fragrances matches JD 'Health & Beauty' ask)",
        "seniority_fit": "on-band (4+ yrs KAM vs 3-5 asked)",
        "red_flags": [
            "Valid UAE driving license 'typically required' — status unconfirmed",
            "3-5 yrs UAE Health & Beauty market experience expected — Paula's beauty depth is Spain e-commerce; her UAE tenure is food FMCG modern trade (DoFreeze), so the exact UAE-H&B combination is adjacent, not identical",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit and a sibling to the Unilever KAE – Personal Care role. This is a Modern-Trade Key "
            "Account Executive owning assigned UAE accounts (Cluster 3: Nesto, coops, Westone, Choithram): "
            "localized sales plans, listings/pricing/promo negotiation, availability/visibility/planogram, "
            "sell-in/sell-out + market-share + trade-spend ROI analysis, distributor management and white-space "
            "development. That maps cleanly onto Paula's KAM track — 42 beauty/fragrance key accounts +30% GMV "
            "QoQ at Miravia, UAE modern-trade execution at DoFreeze, XL accounts at Glovo, and Nielsen category "
            "planning at Mondelez. Notably the JD's Experiences & Qualifications ask for 'UAE Health & Beauty "
            "market experience, preferably key beauty brands' — which her Miravia beauty/fragrance account "
            "depth genuinely addresses (positioned honestly as Spain e-commerce, not UAE brick-and-mortar). "
            "Honest gaps: a valid UAE driving license (listed as typically required — NOT claimed; Paula to "
            "confirm), home-care category tenure (has beauty + food FMCG), and the exact UAE-H&B combination. "
            "Tenure on-band (4+ vs 3-5). No invented home-care, named-account or driving-license claims, and no "
            "'no sponsorship needed' claim (employer-sponsored UAE residence visa)."
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
