"""One-off: generate Paula's CV + cover letter tailored to the noon
"Category Manager" role (Home category, Dubai, UAE — reports to VP Commercials).

Content is authored directly (no LLM API call), filled into the real
templates, converted to PDF via LibreOffice (keeping the editable DOCX too),
placed under the día → posición → categoría convention, and the job is
registered in scored_jobs.json so it shows up in the dashboard.

Mirrors the pattern established in scripts/_gen_noon_am.py.

Honest fit notes driving the content:
- Real Home-category exposure: ran Miravia's Beauty, Fashion & Home Flash Sales channel.
- ~5 yrs across category/commercial roles in e-commerce, q-commerce & FMCG
  (Mondelez category planning Aug-2021 → present).
- P&L, assortment, pricing, seller sourcing/onboarding/negotiation are all real.
- NOT claimed: managing a large team of AMs/BDEs, deep Furniture/Hardlines
  specialism, or an MBA — positioned around genuine strengths instead.
- Per standing rule: never claim "no sponsorship needed"; only state she is
  already Dubai-based on a residence visa.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "noon"
TITLE = "Category Manager"
DATE_FOLDER = "2026-08-18"
CONTACT = None  # LinkedIn shows "Promocionado por técnico de selección" — no named recruiter

JOB_DESCRIPTION = """\
Category Manager — noon, Dubai, United Arab Emirates (On-site).
Reporting to: VP, Commercials.

About noon: A digital ecosystem of products and services powering everyday life
across the Middle East — fast, scalable and deeply customer-centric. Mission:
every door, every day.

What you'll do:
We are looking for a dynamic and commercially driven Category Manager to lead the
Home category. This role requires ownership of the category's P&L and a strong
strategic mindset to drive sustainable growth through well-planned assortment,
pricing, partnerships and execution excellence.

Responsibilities:
- Support development of the overall category roadmap & vision; identify the right
  growth levers to scale categories exponentially.
- Directly responsible for achieving revenue, P&L and CR targets for the category.
- Expand assortment, inventory planning and drive price leadership, key
  partnerships, on-time launches and monetization.
- Ensure best-in-class customer experience through compelling category assortment,
  strong site merchandising, world-class PDPs, inspiring content and excellent
  knowledge of consumer journeys.
- Develop deep, long-standing relationships with sellers/brands to address gaps in
  their offerings, increase campaign engagement and adoption of noon tools/platforms.
- Partner cross-functionally (product, site operations, seller support, marketing,
  ops, customer service, legal) to improve the platform and experience.
- Use customer data to identify and prioritize opportunities; own projects end-to-end.
- Stay up-to-date with regional competitors and global trends.
- Lead and develop talent: manage, coach and train a team of account managers & BDEs.

What you'll need:
- 5 years category management / buying experience in e-commerce / q-commerce.
- Strong analytical skills; comfortable with large data sets in Excel producing
  accurate, decision-ready analysis.
- Experience with AOP and business planning and a track record of driving category growth.
- Seller/vendor management: sourcing, onboarding and commercial negotiation.
- Comfort across both marketplace (3P) and retail (1P) models.
- Diligent and rigorous; able to operate in fast-moving, ambiguous environments.
- Good people skills.

Preferred: MBA/Master's; prior Home, Furniture or Hardlines exposure; private label
or direct sourcing; entrepreneurial background; awards or clear excellence.
"""

ATS = [
    "Category Manager", "category management", "category roadmap", "category vision",
    "P&L", "revenue targets", "assortment", "assortment optimization",
    "inventory planning", "pricing strategy", "price leadership", "monetization",
    "seller management", "vendor management", "sourcing", "onboarding",
    "commercial negotiation", "key partnerships", "marketplace", "3P", "1P",
    "AOP", "business planning", "business reviews", "site merchandising", "PDP",
    "customer journey", "e-commerce", "q-commerce", "GMV", "conversion rate",
    "large data sets", "Excel", "cross-functional", "Home category", "noon",
]

# --------------------------------------------------------------------------
# CV content
# --------------------------------------------------------------------------
CV_CONTENT = {
    "headline": "Category & Commercial Manager · E-Commerce & Q-Commerce · P&L · Assortment, Pricing & Seller Partnerships",
    "professional_summary": (
        "Category and commercial manager with ~5 years across e-commerce and q-commerce marketplaces "
        "(Alibaba's Miravia, Glovo) and FMCG (Mondelez). I own the commercial levers of a category — "
        "assortment, pricing, promotions and seller partnerships — growing 42 accounts +30% GMV QoQ "
        "against P&L targets and onboarding 30+ sellers in two months. Direct Home-category experience "
        "running Miravia's Beauty, Fashion & Home Flash Sales channel, on top of category-planning "
        "foundations at Mondelez (AOP, sell-in/sell-out, NPD). Comfortable across marketplace (3P) and "
        "retail (1P) models, rigorous with large data sets in Excel, and fluent in noon and the UAE's "
        "quick-commerce platforms from my current Dubai role. Already based in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the digital shelf and category execution across noon, Careem, Talabat and Deliveroo — assortment, listings, catalogue and content quality, PDPs, pricing and promotional mechanics — driving on-platform visibility, net sales and sell-out",
                "Manage seller/distributor and brand-partner relationships end-to-end — sourcing, onboarding and commercial negotiation — running business reviews that turn sales, traffic and conversion data into assortment, pricing and promotion decisions",
                "Operate across 1P retail (own-brand distribution) and 3P marketplace models, coordinating product, marketing and operations cross-functionally to hit on-time launches",
                "Lead NPD and go-to-market end-to-end for 6 launches (brief, packaging, pricing, launch readiness) across GCC, MENA, Asia, Europe, USA and Africa",
                "Own the Shopify store end-to-end (assortment, PDPs, merchandising, promotions, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
                "Built an AI-powered automation system (Claude / generative AI) for planning, content and KPI reporting — cutting manual workload ~40% across 50+ markets",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Owned the commercial levers for 42 accounts — assortment optimisation, pricing strategy and targeted promotions — achieving +30% GMV growth QoQ against P&L-aligned commercial targets",
                "Ran the Beauty, Fashion & Home Flash Sales channel, reporting directly to the CEO and executing category plans aligned to P&L — direct hands-on Home-category commercial experience",
                "Led category expansion as PIC Fragrances — sourcing, onboarding and negotiating 30+ new sellers in two months, including official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Produced decision-ready analysis from large data sets — ROI, ROAS, conversion, traffic and retention — to steer assortment, pricing and forecasting",
                "Created and led the Beauty Club and Hot on Social projects, driving site merchandising, brand visibility and on-platform customer engagement",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team that built Glovo's Retail vertical — sourcing and onboarding fashion and lifestyle sellers and expanding the marketplace beyond food into non-food categories",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led assortment and promotional planning",
                "Led cross-functional teams across marketing, logistics and customer support to resolve operational issues and deliver campaigns on time",
                "Negotiated and closed high-impact commercial deals maximising profitability for both Glovo and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built the category-planning foundation: sell-in/sell-out analysis, promotional effectiveness and AOP-style performance reporting for the chocolate category",
                "Identified assortment and growth opportunities and contributed to NPD launches including Milka Spread and Mini Suchard",
            ],
        },
    ],
    "skills_brand": "category strategy & roadmap, assortment & range planning, promotional planning, monetisation, shopper marketing, trade marketing, go-to-market, NPD end-to-end, A&P budget management, generative AI campaigns",
    "skills_ecommerce": "marketplace management (3P & 1P), digital shelf & site merchandising, Noon, Talabat, Careem, Deliveroo, PDP & catalogue/content quality, quick-commerce, conversion rate optimisation (CRO), Shopify, Meta Ads, Google Ads",
    "skills_commercial": "category management, P&L ownership, seller/vendor sourcing & onboarding, commercial negotiation, pricing & price leadership, assortment planning, inventory planning, AOP & business planning, business reviews, distributor & key account management",
    "skills_data": "P&L management, category & KPI scorecards, large-dataset analysis (Advanced Excel), sell-in/sell-out, ROI, ROAS, conversion & traffic analysis, forecasting, AI-assisted analysis, Power BI, Looker, Nielsen",
    "skills_tools": "Advanced Excel, Power BI, Looker, Nielsen, Kantar, Salesforce, SAP, Shopify, Meta Ads Manager, Google Ads, Generative AI (Claude, ChatGPT), Canva",
}

# --------------------------------------------------------------------------
# Cover letter content
# --------------------------------------------------------------------------
CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm applying for the Category Manager role leading noon's Home category. Owning a category's "
        "P&L end-to-end — roadmap, assortment, pricing, seller partnerships and on-time launches — is "
        "exactly the work I do today across noon and the UAE's quick-commerce platforms, and it's where "
        "I've delivered my strongest commercial results."
    ),
    "body_paragraph_1": (
        "At Miravia (Alibaba Group) I owned the commercial levers for 42 accounts — assortment, pricing "
        "and promotions — growing GMV +30% QoQ against P&L targets, and I ran the Beauty, Fashion & Home "
        "Flash Sales channel reporting directly to the CEO, so I've managed a Home category in practice. "
        "As PIC Fragrances I sourced, onboarded and negotiated 30+ new sellers in two months. My "
        "category-planning foundation comes from Mondelez (sell-in/sell-out, promotional effectiveness, "
        "AOP-style planning and NPD), and today at DoFreeze I run the digital shelf and seller "
        "relationships across noon, Talabat, Careem and Deliveroo."
    ),
    "body_paragraph_2": (
        "I'm comfortable across both marketplace (3P) and retail (1P) models, rigorous with large data "
        "sets in Excel, and I turn numbers into decision-ready assortment and pricing actions. I'm "
        "already based in Dubai on a residence visa, bilingual Spanish/English (C1), and I know noon "
        "from the seller side — so I'd be productive from week one. The Home category's growth runway on "
        "the platform is exactly the kind of challenge I want to own."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd build and scale noon's Home category. I'm available to "
        "start immediately and would love to discuss the role — you can reach me at +971 50 386 3656 or "
        "paulich98@hotmail.com. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="noon-category-manager-home",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/noon/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Category Manager", "via": "LinkedIn", "category": "Home",
             "reports_to": "VP, Commercials", "apply": "Easy Apply"},
    )


def _convert_pdf(docx_path: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice headless (reliable, non-interactive).

    Keeps the editable DOCX alongside the PDF.
    """
    import subprocess

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
        "ai_score": 90,
        "ai_tier": "Hot",
        "skills_match": [
            "Category management (e-commerce/q-commerce)", "P&L ownership",
            "Assortment & pricing", "Seller sourcing/onboarding/negotiation",
            "Home-category exposure (Miravia Flash Sales)", "AOP & business planning",
            "Large-dataset analysis (Excel)", "3P marketplace + 1P retail",
            "Cross-functional execution", "noon platform (hands-on)",
        ],
        "missing_skills": [
            "Managing a sizeable team of AMs/BDEs (people-leadership at scale)",
            "Deep Furniture/Hardlines specialism",
            "MBA/Master's (preferred, not required)",
        ],
        "sector_fit": "exact",
        "seniority_fit": "close",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit: JD wants ~5 yrs category management in e-commerce/q-commerce owning P&L, "
            "assortment, pricing, seller sourcing/onboarding/negotiation and AOP/business planning — "
            "Paula's core. She grew 42 accounts +30% GMV QoQ at Miravia/Alibaba, onboarded 30+ sellers "
            "in two months, and genuinely ran a Beauty/Fashion/HOME channel, plus Mondelez category "
            "planning and current noon/q-commerce digital-shelf ownership at DoFreeze. Gaps vs the JD: "
            "leading a large AM/BDE team, deep Furniture/Hardlines specialism and an MBA (preferred). "
            "Dubai residence visa, C1 English."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _move_into_dated_folder() -> Path:
    """Move output/<Company> - <Role>/ under output/<DATE_FOLDER>/."""
    from career_ops.generators._paths import job_output_dir
    src = job_output_dir(make_job())            # output/noon - Category Manager
    dated_parent = settings.output_dir / DATE_FOLDER
    dated_parent.mkdir(parents=True, exist_ok=True)
    dest = dated_parent / src.name
    if src.resolve() == dest.resolve():
        return dest
    if dest.exists():
        for item in src.iterdir():
            shutil.move(str(item), str(dest / item.name))
        shutil.rmtree(src, ignore_errors=True)
    else:
        shutil.move(str(src), str(dest))
    return dest


def main() -> None:
    job = make_job()
    register_in_dashboard(job)
    print("STEP registered in dashboard")

    cv_docx = cv._fill_template(CV_CONTENT, job)
    print("STEP CV docx built:", cv_docx.name)

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    print("STEP CL docx built:", cl_docx.name)

    final_dir = _move_into_dated_folder()
    print("STEP moved to:", final_dir)

    cvd = final_dir / "01_CV_y_Carta" / cv_docx.name
    cld = final_dir / "01_CV_y_Carta" / cl_docx.name
    cv_pdf = _convert_pdf(cvd)
    cl_pdf = _convert_pdf(cld)

    print("OK_CV_DOCX", cvd.name, "(exists)" if cvd.exists() else "(MISSING)")
    print("OK_CV_PDF", cv_pdf.name, "(exists)" if cv_pdf.exists() else "(MISSING)")
    print("OK_CL_DOCX", cld.name, "(exists)" if cld.exists() else "(MISSING)")
    print("OK_CL_PDF", cl_pdf.name, "(exists)" if cl_pdf.exists() else "(MISSING)")
    print("FINAL_DIR", final_dir)


if __name__ == "__main__":
    main()
