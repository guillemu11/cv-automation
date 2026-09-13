"""One-off: generate Paula's application package for the talabat
"Product Manager - Beauty" (Dubai) role — a 0->1 quick-commerce beauty venture
inside talabat's New Ventures org.

This is a *stretch* application: the posting is a digital Product Manager role
(roadmap ownership, Jira/Agile, "5+ yrs in digital product management") while
Paula's background is brand / e-commerce / category / key-account. Content is
authored directly (no LLM API key in this repo) and kept strictly truthful —
NO invented PM/Jira/roadmap/engineering experience. It is re-angled to lead with
the genuine bridges the JD itself asks for: a 0->1 new-vertical launch (Glovo
Retail), deep beauty category depth (Miravia), hands-on quick-commerce (talabat,
Noon, Careem, Deliveroo) and AI-native building.

Fills the real CV + cover-letter templates, converts to PDF, and lands the
package under output/2026-07-07/talabat - Product Manager - Beauty/.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "talabat"
TITLE = "Product Manager - Beauty"
DATE_FOLDER = "2026-07-07"

JOB_DESCRIPTION = """\
Product Manager - Beauty — talabat, Dubai, UAE (On-site, Full-time).

We're building talabat Beauty, the first quick-commerce beauty destination in the
Middle East. This is a 0->1 venture role inside talabat's New Ventures product
organization. You'll be a core Product Manager on a small, dedicated Beauty
venture team, shaping how millions of MENA shoppers discover, evaluate, and
re-buy beauty — a category that behaves nothing like food or grocery delivery.
Beauty is brand-led, discovery-driven, content-heavy, with premium delivery
expectations. You'll work directly with the Beauty Venture Leader, engineering,
design, data, commercial, brand and CX.

What's on your plate: champion features that solve real Beauty shopper needs
(discovery, re-purchase, brand-led browsing, post-purchase confidence); build for
scale across diverse shopper segments and MENA market contexts; work within a
cross-functional Product/Engineering/Data team; partner with commercial, marketing
and brand teams to define and launch go-to-market plans; lead discovery end-to-end
from problem framing to solution validation; combine customer interviews, data and
market insight to de-risk opportunities; rapidly ideate, prototype and test; own
the roadmap.

Qualifications: 5+ years in digital product management; launched products to
market, ideally at least one 0->1 launch (new vertical / business model /
marketplace); AI-fluent as a builder (vibe-code prototypes, use shared context
libraries) and as a product thinker (ship AI capabilities, raise AI literacy);
strong instinct for content, merchandising and category navigation — you think
like a category manager as much as a PM (assortment, hero products, seasonality,
shopper missions); comfortable in ambiguity; resilient at influencing partner
teams without authority; Agile fluency; hands-on with tools like Jira; e-commerce
/ marketplace / q-commerce / content-discovery experience a strong plus; beauty,
fashion or lifestyle category experience a very strong plus.
"""

ATS = [
    "Product Manager", "0->1", "new vertical", "quick-commerce", "q-commerce",
    "beauty", "discovery", "re-purchase", "brand-led", "content-heavy",
    "merchandising", "assortment", "hero products", "category navigation",
    "shopper missions", "go-to-market", "roadmap", "product discovery",
    "cross-functional", "AI-fluent", "prototype", "marketplace", "MENA",
]

CONTENT = {
    "headline": "Beauty & E-Commerce Builder · 0→1 New-Vertical Launches · Quick-Commerce & Category · AI-Native",
    "professional_summary": (
        "Beauty and quick-commerce builder who thinks like a category manager as much as a product owner. "
        "4+ years launching and scaling brand-led, discovery-heavy shopping experiences across e-commerce, "
        "marketplace and q-commerce — including a genuine 0→1 new vertical (Glovo Retail) and beauty & "
        "fragrances category ownership at Alibaba's Miravia (42 accounts, +30% GMV QoQ). Today at DoFreeze "
        "I own a Shopify shopping experience end-to-end — how shoppers discover, evaluate and re-buy — and "
        "run the UAE quick-commerce shelf on talabat, Noon, Careem and Deliveroo. AI-native builder who "
        "designs and vibe-codes generative-AI tooling (Claude/GPT) and raises the team's AI literacy."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the brand's Shopify shopping experience end-to-end — catalogue, UX, collections, merchandising, discount mechanics and checkout — shaping how shoppers discover, evaluate and re-buy, and lifting conversion (CRO) and average order value through continuous, data-led iteration",
                "AI-native builder: designed and vibe-coded a generative-AI system (Claude/GPT) that prototypes campaigns, market research, content and KPI reporting — cutting manual workload ~40% and raising the team's AI literacy",
                "Run the UAE quick-commerce shelf across talabat, Noon, Careem and Deliveroo — assortment, hero-product selection, content and promotional mechanics — the exact q-commerce discovery-and-merchandising surface this venture owns",
                "Lead NPD end-to-end for 6 launches (problem framing, brief, packaging, pricing, go-to-market) across GCC, MENA and beyond — validating solutions and shipping to market under ambiguity",
                "Partner across commercial, brand, trade and creative to define go-to-market and shopper-mission plans by channel — influencing partner teams without owning them",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned the Beauty & Fragrances category across 42 key accounts, growing GMV +30% QoQ through assortment, hero-product curation, pricing and seasonal promotions — category-manager thinking on a content- and discovery-heavy marketplace",
                "Created and launched Beauty Club and Hot on Social from 0→1 — brand-led, content-heavy destinations that lifted discovery, loyalty and re-purchase on platform",
                "Led category expansion as PIC Fragrances, onboarding 30+ beauty & fragrance houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) in two months via trend-driven assortment",
                "Analysed conversion, traffic, retention and ROI to de-risk decisions and shape the channel roadmap — forming opinions with incomplete data and revising them on evidence",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical from the ground up — a genuine 0→1 new vertical taking a food-delivery platform into beauty, apparel and non-food q-commerce, the same shape as talabat Beauty: a new vertical inside a scaled platform",
                "Onboarded and scaled new lifestyle and beauty partners, defining assortment and merchandising for a category that behaved nothing like food",
                "Led cross-functional squads across marketing, logistics and CX to ship activations and grow order volume",
                "Negotiated high-impact commercial deals maximising profitability for platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Category planning for chocolate — sell-in/sell-out analysis, promotional effectiveness and shopper insight to surface growth opportunities",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": "0→1 new-venture launches, go-to-market, NPD end-to-end, brand-led merchandising, shopper missions & discovery, product discovery, influencer & UGC, content strategy, generative-AI campaigns, omnichannel",
    "skills_ecommerce": "Shopify e-store ownership, quick-commerce (talabat, Noon, Careem, Deliveroo), assortment & merchandising, conversion rate optimisation (CRO), UX & discovery, retention & re-purchase, Meta Ads, Google Ads, marketing automation",
    "skills_commercial": "category management, assortment planning, hero-product curation, pricing strategy, key account management, negotiation, forecasting, modern trade, distributor management",
    "skills_data": "product & category analytics, KPI dashboards, A/B testing, conversion & retention analysis, ROI/ROAS, sell-in/sell-out, AI-assisted analysis & forecasting, Looker, Nielsen, Kantar, Salesforce, SAP",
    "skills_tools": "AI building — Claude / ChatGPT (vibe-coding prototypes & automation), Shopify, Meta Ads Manager, Google Ads, Looker, Power BI, Tableau, Salesforce, SAP, Canva, Microsoft Office (Expert)",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "talabat Beauty is the rare thing I look for: a true 0→1 venture — the first quick-commerce beauty "
        "destination in MENA — built inside a profitable, scaled platform. I already work with talabat every "
        "week from the other side of the marketplace, listing and merchandising FMCG brands on your q-commerce "
        "shelf, so I know both the platform and how differently beauty behaves from food and grocery."
    ),
    "body_paragraph_1": (
        "I come to product from the category and commerce side — which this role explicitly values (\"think like "
        "a category manager as much as a PM\"). At Glovo I helped build the Retail vertical from 0→1, taking a "
        "food-delivery platform into beauty and non-food — the same shape as talabat Beauty. At Miravia/AliExpress "
        "I owned the Beauty & Fragrances category across 42 accounts (+30% GMV QoQ), curated assortment and hero "
        "products, and launched Beauty Club and Hot on Social from zero — brand-led, content-heavy destinations "
        "built around discovery and re-purchase. Today at DoFreeze I own a Shopify shopping experience end-to-end, "
        "from discovery to re-buy."
    ),
    "body_paragraph_2": (
        "Two things set me apart for this venture. First, I'm AI-native as a builder: I designed and vibe-coded a "
        "generative-AI system (Claude/GPT) that prototypes campaigns, research and content and raises my team's AI "
        "literacy — the builder-and-product-thinker profile you describe. Second, I bring hands-on MENA depth — "
        "talabat, Noon, Careem and Deliveroo on the q-commerce side; Arabian Oud, Lattafa and Swiss Arabian on the "
        "beauty side — and I'm already in Dubai on a residence visa, so I can start with zero relocation. I'll be "
        "candid: my last four years are in category, e-commerce and brand rather than a formal PM title — but the "
        "work (0→1 launches, owning a shopping experience, discovery and merchandising, shipping under ambiguity) "
        "is the substance of this role."
    ),
    "closing_paragraph": (
        "I'd love to walk the Beauty Venture team through how I'd approach discovery, assortment and the "
        "first-impression experience for MENA beauty shoppers. I'm based in Dubai and available immediately — "
        "thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="talabat-pm-beauty-2026-07",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/view/talabat-product-manager-beauty",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Product Manager - Beauty", "via": "LinkedIn Easy Apply"},
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
        "ai_score": 68,
        "ai_tier": "Warm",
        "skills_match": [
            "0→1 new-vertical launch (Glovo Retail)", "Beauty category depth (Miravia)",
            "Quick-commerce hands-on (talabat, Noon, Careem, Deliveroo)",
            "Assortment / hero products / merchandising", "AI-native builder (Claude/GPT)",
            "Owns e-commerce discover→evaluate→re-buy experience", "Go-to-market & cross-functional",
            "Already in Dubai (residence visa)",
        ],
        "missing_skills": [
            "5+ yrs formal digital product management", "Roadmap ownership with engineering squads",
            "Jira / Agile product tooling",
        ],
        "sector_fit": "strong (beauty + q-commerce)",
        "seniority_fit": "stretch (PM tenure gap)",
        "red_flags": ["Role is digital PM, not brand/marketing — core PM-title gap"],
        "ats_keywords": ATS,
        "reasoning": (
            "Stretch application. talabat 'Product Manager - Beauty' is a digital PM role (roadmap, "
            "Jira/Agile, 5+ yrs product management) — Paula's 4+ yrs are brand/e-commerce/category/KAM, "
            "so the core PM-title requirement is a genuine gap. BUT the JD itself values a category-manager "
            "mindset, a 0→1 new-vertical launch, beauty depth, q-commerce and AI-fluent builders — all of "
            "which Paula truly has (Glovo Retail 0→1, Miravia Beauty category, talabat/Noon/Careem/Deliveroo, "
            "Claude/GPT tooling). Positioned honestly as a category/commerce builder crossing into product; "
            "the cover letter addresses the PM-title gap head-on."
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
        # merge contents
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

    # --- CV ---
    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    # --- Cover letter ---
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, contact_name=None)
    cl_pdf = cl._to_pdf(cl_docx)
    print("OK_CL", cl_pdf)

    # position dir is .../<Company> - <Role>/ (parent of 01_CV_y_Carta)
    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
