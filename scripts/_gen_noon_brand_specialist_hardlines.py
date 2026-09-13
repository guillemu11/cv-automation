"""One-off: generate Paula's CV (+ cover letter) for noon — "Brand Specialist"
(Hardlines / Electronics category), reporting to a Category Manager, Dubai.

Why this is an EXCELLENT, honest fit:
  - The role is marketplace CATEGORY / ACCOUNT MANAGEMENT: own a category
    end-to-end (selection & availability, growth, customer experience), vendor
    management & joint business plans, promotions/merchandising for traffic &
    conversion, analytics/benchmarking, cross-functional with ops/finance/tech.
  - This is the TWIN of Paula's Miravia role: Key Account Manager on a top-5
    e-commerce marketplace (Alibaba) — 42 brand accounts owned end-to-end,
    category expansion (PIC Fragrances: 30+ vendors onboarded), assortment/
    pricing, promotions & Flash Sales, and analytics, growing GMV +30% QoQ.
    Same job, different category.
  - DISTINCTIVE, honest edge: Paula knows noon FIRST-HAND from the brand side —
    she integrates products onto noon (and Talabat/Careem/Deliveroo) at DoFreeze
    today, so she understands noon's marketplace mechanics from the vendor seat.
  - Requirements are comfortably met: Business Administration degree (CUNEF);
    5 yrs vs 3+ asked; strong analytical/negotiation; advanced Excel + Power BI.
  - noon culture ("relentlessly resourceful, bias for action, fiercely original")
    fits her hands-on multi-market execution + AI-automation building.

Honest notes (NOT fabricated):
  - Category depth is Beauty/Fragrances/Fashion (Miravia) + FMCG (DoFreeze/
    Mondelez), NOT Electronics/Hardlines. Category/account management is
    transferable craft; electronics is a new vertical she'd ramp on fast.
    Disclosed in the cover letter.
  - Title "Brand Specialist" is arguably a touch below her KAM-at-Alibaba level;
    framed as genuine enthusiasm to own a category at noon's scale, not a
    step-down. (Flagged to Paula/Guille separately, not in the documents.)
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-21/.
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

COMPANY = "noon"
TITLE = "Brand Specialist – Electronics (Hardlines)"
DATE_FOLDER = "2026-08-21"

CONTACT = None  # Reports to a Category Manager; no name in posting — "Hiring Manager".

JOB_DESCRIPTION = """\
Brand Specialist — noon (Hardlines / Electronics), Dubai. Reporting to: Category
Manager. noon is building an ecosystem of digital products and services across the
Middle East — mission "every door, every day".

As a Brand Specialist for Hardlines you own your Electronics category end-to-end —
from driving selection and availability to optimizing growth and customer
experience. Build strong vendor relationships, leverage data to identify
opportunities, and collaborate cross-functionally to deliver commercial success.

- Category & business growth: drive category expansion, improve selection
  discoverability, deliver topline growth through data-driven strategies.
- Inventory & availability: keep products in stock via replenishment, reduced lead
  times, and supply-chain efficiency.
- Traffic & conversion: develop campaigns, promotions and merchandising strategies
  to increase traffic and boost conversion.
- Vendor management: main point of contact for key brands; build partnerships and
  align on joint business plans.
- Analytics & insights: monitor performance metrics, run competitive benchmarking,
  provide actionable insights to improve KPIs.
- Cross-functional collaboration: partner with operations, finance and tech to
  enhance processes and tools supporting growth.

What you'll need: Bachelor's in Business, Marketing, Economics or related; 3+ years
in account management, category management or e-commerce; strong analytical,
communication and negotiation skills; proficiency in Excel and data analysis.

Who will excel: high standards, hard work, relentlessly resourceful, deep bias for
action, courage to be fiercely original, readiness to adapt, pivot and learn.
"""

ATS = [
    "Brand Specialist", "category management", "account management", "e-commerce",
    "marketplace", "category growth", "business growth", "topline growth",
    "selection", "assortment", "discoverability", "availability", "inventory",
    "replenishment", "lead times", "supply chain", "traffic", "conversion",
    "campaigns", "promotions", "merchandising", "vendor management",
    "vendor relationships", "brand partnerships", "joint business plans", "JBP",
    "key accounts", "negotiation", "analytics", "insights", "performance metrics",
    "competitive benchmarking", "KPIs", "data-driven", "data analysis", "Excel",
    "Power BI", "cross-functional", "operations", "finance", "tech",
    "noon", "Talabat", "Careem", "Deliveroo", "quick-commerce", "GMV", "ROI",
    "ROAS", "pricing", "customer experience", "Dubai", "UAE", "bias for action",
]

CV_CONTENT = {
    "headline": (
        "E-Commerce Category & Key Account Manager · Marketplace Vendor & Brand Management (JBP) · Selection, "
        "Merchandising & Conversion Growth · Data & Advanced Excel · Ex-Alibaba Marketplace · noon-integration experience"
    ),
    "professional_summary": (
        "E-commerce category and account manager with five years across top marketplaces and consumer brands, "
        "now driving brand growth across UAE quick-commerce (including noon) from Dubai. I've done this role's "
        "twin: at Alibaba's Miravia I owned 42 brand accounts on a top-5 marketplace end-to-end — selection and "
        "assortment, vendor management and joint business plans, promotions and merchandising, and analytics — "
        "growing GMV +30% QoQ. I turn data into category growth: expanding selection and discoverability, "
        "building campaigns and merchandising that lift traffic and conversion, coordinating availability and "
        "replenishment with cross-functional partners, and benchmarking competitors to move KPIs. I know noon "
        "first-hand from the brand side, having integrated products onto its platform, and I work fluently in "
        "Excel, Power BI and data analysis. Business Administration graduate (CUNEF) — relentlessly resourceful, "
        "with a deep bias for action."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Brands: Befit, Eurocake, Flair | UAE quick-commerce + 50+ countries",
            "bullets": [
                "Drive brand growth across UAE quick-commerce marketplaces — integrating and managing products on noon, Talabat, Careem and Deliveroo (listings, selection, availability, promo mechanics and retail execution)",
                "Build campaigns, promotions and merchandising strategies that increase traffic and boost conversion across e-commerce and marketplace channels",
                "Manage assortment, pricing and availability across markets — coordinating replenishment and retail execution with operations and supply-chain partners",
                "Own vendor and partner relationships and align on joint plans, acting as the main commercial point of contact",
                "Monitor performance metrics and competitive benchmarks (Excel, Power BI) and translate them into actionable next steps",
                "Built an AI-powered analytics & automation system (Claude / generative AI) that accelerates reporting, benchmarking and campaign planning",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees",
            "bullets": [
                "Owned 42 brand accounts end-to-end on a top-5 e-commerce marketplace — the direct equivalent of this category/account role — growing GMV +30% QoQ through selection, pricing, assortment and promotions",
                "Led category expansion as PIC Fragrances — onboarding 30+ new brands/vendors in two months (incl. Arabian Oud, Lattafa, Swiss Arabian, Ajmal) and improving selection discoverability",
                "Acted as the main point of contact for key brands — building partnerships and aligning joint business plans",
                "Owned the Flash Sales channel and ran promotions and merchandising to drive traffic and conversion, reporting to the CEO against P&L targets",
                "Analysed conversion, traffic, retention, ROI and ROAS and benchmarked competitors to steer assortment and campaigns",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts on a quick-commerce super-app, driving GMV growth through data-led planning and promotions",
                "Negotiated and closed commercial deals and joint activations with brand partners",
                "Coordinated cross-functionally across marketing, operations and logistics to improve availability and delivery",
                "Helped build the Retail vertical — onboarding new brands to the platform (selection expansion, 0-to-1)",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and category-planning analysis — availability, replenishment signals and promotional effectiveness for the chocolate category",
                "Built performance reports and competitive / category benchmarking in Excel for the commercial team",
                "Supported NPD launches and identified assortment and growth opportunities",
            ],
        },
    ],
    "skills_brand": (
        "category management, selection & assortment strategy, merchandising, promotions & campaigns, "
        "traffic & conversion growth, brand growth, go-to-market"
    ),
    "skills_ecommerce": (
        "e-commerce & marketplace management, noon / Talabat / Careem / Deliveroo integration, "
        "selection & discoverability, conversion rate optimisation (CRO), listings & catalogue, "
        "availability & inventory execution, Shopify, EDM"
    ),
    "skills_commercial": (
        "key account management, vendor & brand management, joint business plans (JBP), negotiation, "
        "replenishment & availability coordination, cross-functional collaboration (ops, finance, tech), "
        "pricing strategy, category expansion"
    ),
    "skills_data": (
        "data analysis (Excel — advanced), competitive benchmarking, performance metrics & KPIs, "
        "sell-in/sell-out, ROI / ROAS / conversion / traffic analysis, Power BI, forecasting, Nielsen, Kantar"
    ),
    "skills_tools": (
        "Excel (Advanced), Power BI, Salesforce (CRM), SAP, Generative AI (Claude, ChatGPT), Shopify, "
        "Nielsen, Kantar, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "noon's mission — every door, every day — runs on people who can own a category end-to-end and make the "
        "numbers move, and that's exactly the work I love. I'm an e-commerce category and account manager who "
        "has already done this role's twin: at Alibaba's Miravia I owned 42 brand accounts on a top-5 "
        "marketplace, growing GMV +30% QoQ. And I know noon from the other side of the table — I integrate and "
        "grow brands on noon today from Dubai — so I understand your marketplace mechanics from the vendor seat, "
        "which is a useful head start for owning a category from the inside."
    ),
    "body_paragraph_1": (
        "The responsibilities map almost one-to-one onto what I've done. At Miravia I drove category growth and "
        "selection discoverability, led a category expansion that onboarded 30+ new vendors in two months, acted "
        "as the main point of contact for key brands and aligned joint business plans, and ran promotions and "
        "merchandising (owning the Flash Sales channel, reporting to the CEO) to lift traffic and conversion — "
        "all steered by constant analysis of conversion, traffic, ROI and ROAS plus competitive benchmarking. "
        "At DoFreeze I now manage selection, availability, pricing and promo mechanics across UAE marketplaces "
        "(noon, Talabat, Careem, Deliveroo), coordinating replenishment and retail execution with operations. "
        "I'm fluent in Excel and Power BI, and I built an AI-powered system (Claude) that speeds up my reporting "
        "and benchmarking — useful in a bias-for-action environment."
    ),
    "body_paragraph_2": (
        "One honest note so we're clear-eyed: my category depth is beauty, fragrances, fashion and FMCG rather "
        "than electronics and hardlines — but category and account management is a craft that travels, the "
        "requirements here are the ones I've lived (vendor management, JBPs, selection, promotions, analytics), "
        "and I'd get up the electronics learning curve fast. What I bring beyond the checklist is a genuine "
        "insider-outsider view of noon, quick-commerce fluency in this exact market, and the resourceful, "
        "hands-on, learn-fast attitude your team is built around."
    ),
    "closing_paragraph": (
        "I'd be excited to own an Electronics category at noon's scale and prove it in selection, availability "
        "and conversion — and I can share commercial case studies and results (from +30% GMV QoQ to category "
        "expansion and promotional wins). I'm based in Dubai and ready to move fast. Thank you for your "
        "consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="noon-brand-specialist-hardlines-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://careers.noon.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Brand Specialist category account management",
             "function": "E-commerce category / account management (marketplace, Hardlines/Electronics)",
             "sector": "E-commerce marketplace (noon)",
             "note": "Excellent, honest fit — the direct twin of her Miravia KAM-on-a-marketplace role, at a "
                     "top UAE employer she already knows from the brand/vendor side (integrates onto noon today). "
                     "Honest notes: category depth is beauty/fragrances/fashion + FMCG, not electronics "
                     "(transferable, disclosed); 'Brand Specialist' title is arguably a touch below her KAM "
                     "level. No 'own visa / no sponsorship' claim."},
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
            "DIRECT TWIN of her role: Key Account Manager on a top-5 e-commerce marketplace (Alibaba/Miravia) — 42 brand accounts owned end-to-end, +30% GMV QoQ",
            "Category & business growth — category expansion (PIC Fragrances: 30+ vendors onboarded), selection & discoverability, data-driven topline growth",
            "Vendor management — main point of contact for key brands, partnerships, joint business plans (JBP)",
            "Traffic & conversion — promotions, merchandising, Flash Sales channel ownership",
            "Analytics & insights — conversion/traffic/ROI/ROAS analysis, competitive benchmarking, advanced Excel + Power BI (JD requires Excel)",
            "DISTINCTIVE EDGE: knows noon from the brand side — integrates products onto noon/Talabat/Careem/Deliveroo TODAY at DoFreeze",
            "Availability/replenishment exposure — quick-commerce retail execution (DoFreeze) + category planning (Mondelez)",
            "Cross-functional (ops/logistics/marketing); negotiation; Business Administration degree; 5 yrs vs 3+ asked",
            "noon culture fit — relentlessly resourceful, bias for action, learn-fast (AI-automation builder, hands-on multi-market operator)",
        ],
        "missing_skills": [
            "Electronics/Hardlines category domain — her category depth is beauty/fragrances/fashion (Miravia) + FMCG (DoFreeze/Mondelez). Transferable category/account craft; disclosed honestly; electronics is a fast ramp, not a requirement (JD asks account/category/e-commerce experience generally)",
            "Deep supply-chain/replenishment ownership is lighter than her commercial/analytics strengths — has real exposure (QC retail execution + category planning), not a dedicated ops background",
        ],
        "sector_fit": "excellent (e-commerce marketplace category/account management is exactly her Miravia + DoFreeze work; knows noon first-hand)",
        "seniority_fit": "strong / slightly over — 'Brand Specialist' (3+ yrs) vs her KAM-at-Alibaba level (5 yrs); positioned as genuine enthusiasm to own a category at noon's scale",
        "red_flags": [
            "Title 'Brand Specialist' may sit a notch below her Key Account Manager level — confirm scope/band and comp before advancing; upside is noon's brand value + category ownership + UAE market.",
            "Electronics vertical is new to her (category craft transfers) — disclosed honestly in the cover letter, not hidden.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Excellent, honest fit — arguably the best of the batch alongside the beauty brand role. noon's "
            "'Brand Specialist' is marketplace category/account management (own a category end-to-end: selection "
            "& availability, growth, vendor management & JBPs, promotions/merchandising for traffic & "
            "conversion, analytics/benchmarking, cross-functional with ops/finance/tech). This is the direct "
            "twin of Paula's Miravia role — Key Account Manager on a top-5 marketplace (Alibaba), 42 accounts "
            "owned end-to-end, category expansion, +30% GMV QoQ — and she meets every requirement (Business "
            "degree, 5 yrs vs 3+, strong analytics/negotiation, advanced Excel/Power BI). Her rare, honest edge "
            "is knowing noon from the brand/vendor side (she integrates onto noon at DoFreeze today). Honest "
            "gaps: electronics/hardlines is a new category (transferable craft, disclosed), and the 'Specialist' "
            "title sits a touch below her KAM level (framed as enthusiasm to own a category at noon's scale). "
            "Confirm scope/band/comp given the title. No 'own visa / no sponsorship' claim."
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
