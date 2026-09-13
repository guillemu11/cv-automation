"""One-off: generate Paula's CV + cover letter tailored to the noon
"Account Manager" role on The Dubai Mall Online team (Dubai, UAE).

Content is authored directly (no LLM API call), filled into the real
templates, converted to PDF (keeping the editable DOCX too), placed under the
día → posición → categoría convention, and the job is registered in
scored_jobs.json so it shows up in the dashboard.

Mirrors the pattern established in scripts/_gen_colgate_cv.py.
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
TITLE = "Account Manager"
DATE_FOLDER = "2026-07-07"
CONTACT = "Tatiana Massaad"

JOB_DESCRIPTION = """\
Account Manager — noon, Dubai, United Arab Emirates (On-site). The Dubai Mall
Online team.

About: The Dubai Mall Online is the official digital platform of Dubai Mall,
bringing the mall's iconic retail brands into a single online shopping
destination. Joining offers the chance to build and scale a high-growth
business from the ground up, alongside some of the world's most recognized
brands, shaping the future of omnichannel retail in the GCC.

What you'll do:
- Manage and grow relationships with key brand partners and accounts.
- Serve as the primary point of contact for assigned brands, ensuring strong
  relationship management and operational excellence.
- Drive revenue growth through assortment optimization, pricing strategies and
  improved brand visibility on the platform.
- Collaborate with merchandising, marketing and operations teams to execute
  seasonal campaigns, launches and promotional activity.
- Lead onboarding of new fashion and sports brands onto the platform, ensuring
  smooth integration and readiness for launch.
- Monitor and analyze performance metrics including sales, traffic, conversion
  and customer engagement.
- Identify growth opportunities through data-driven insights and category trends.
- Manage end-to-end execution of product launches, campaigns and promotions.
- Resolve operational issues related to catalog accuracy, pricing, content
  quality, logistics and fulfillment.
- Conduct regular business reviews with brand partners and provide actionable
  performance feedback.
- Ensure alignment with commercial, marketing, supply chain and tech teams.

What you'll need:
- 3-5 years in Account Management, Brand Management or E-commerce Marketplace roles.
- Strong experience in fashion and/or sports retail industry highly preferred.
- Proven track record managing external brand relationships and driving
  commercial performance.
- Good understanding of digital commerce, online retail platforms and
  marketplace dynamics.
- Strong analytical skills; excellent communication and stakeholder management.
- Ability to work in a fast-paced, high-growth, cross-functional environment.
"""

ATS = [
    "Account Manager", "account management", "brand management", "brand partners",
    "e-commerce marketplace", "marketplace dynamics", "fashion retail",
    "sports retail", "assortment optimization", "pricing strategy",
    "brand visibility", "brand onboarding", "business reviews", "digital commerce",
    "online retail platform", "conversion", "traffic", "customer engagement",
    "category trends", "promotional activity", "product launches",
    "stakeholder management", "cross-functional", "GMV", "noon",
]

# --------------------------------------------------------------------------
# CV content
# --------------------------------------------------------------------------
CV_CONTENT = {
    "headline": "Key Account Manager · E-Commerce Marketplaces · Brand Partnerships · Fashion & FMCG",
    "professional_summary": (
        "Key Account and E-Commerce manager with 4+ years growing brand partnerships across "
        "marketplaces in Fashion, Beauty and FMCG. Alibaba-trained at Miravia, where I managed "
        "42 key accounts to +30% GMV QoQ through assortment, pricing and promotions and onboarded "
        "30+ brands in two months. Currently lead Brand & E-Commerce at DoFreeze (Dubai), running "
        "the digital shelf across UAE marketplaces — including onboarding and scaling brands directly "
        "on noon, Talabat, Careem and Deliveroo. Data-driven operator fluent in business reviews, "
        "catalogue and content quality, pricing and full-funnel growth. Inditex-trained (Massimo "
        "Dutti) with genuine fashion-retail instinct, already based in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Run the UAE marketplace digital shelf across noon, Careem, Talabat and Deliveroo — owning brand onboarding, product listings, catalogue and content quality, pricing and promotional mechanics — driving on-platform visibility, net sales and sell-out",
                "Act as commercial lead for the brand portfolio, managing external partner and distributor relationships end-to-end and running business reviews that turn sales, traffic and conversion data into assortment, pricing and promotion actions",
                "Drive revenue growth through assortment optimisation, pricing strategy and improved brand visibility, coordinating seasonal campaigns and launches with merchandising, marketing and operations teams",
                "Lead NPD and go-to-market end-to-end for 6 launches (brief, packaging, pricing, launch readiness) across GCC, MENA, Asia, Europe, USA and Africa",
                "Own the Shopify e-commerce store end-to-end (catalogue, UX, collections, promotions, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
                "Built an AI-powered automation system (Claude / generative AI) for campaign planning, content and KPI reporting — cutting manual workload ~40% across 50+ markets",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 key brand accounts across fashion, beauty and fragrances as their primary point of contact, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Led brand onboarding as PIC Fragrances — integrating 30+ new stores in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — ensuring smooth catalogue integration and launch readiness",
                "Ran regular business reviews with brand partners, translating sales, traffic, conversion and retention data into growth actions, actionable feedback and forecasting",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing commercial plans aligned with P&L targets",
                "Created and led the Beauty Club and Hot on Social projects, boosting brand visibility, loyalty and on-platform customer engagement",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team that built Glovo's Retail vertical — onboarding fashion and lifestyle brands and expanding the marketplace beyond food into apparel, beauty and non-food categories",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) and integrated new partners, driving GMV growth through data-led planning and bespoke activations",
                "Led cross-functional teams across marketing, logistics and customer support to resolve operational issues and deliver seamless campaigns",
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
                "Conducted sell-in/sell-out analysis, evaluated promotional effectiveness and built performance reports for the chocolate category",
                "Identified growth opportunities and contributed to NPD launches including Milka Spread and Mini Suchard",
            ],
        },
    ],
    "skills_brand": "brand partnerships, go-to-market, shopper marketing, trade marketing, omnichannel campaigns, NPD end-to-end, brand strategy, influencer marketing, A&P budget management, generative AI campaigns",
    "skills_ecommerce": "marketplace management, digital shelf, Noon, Talabat, Careem, Deliveroo, catalogue & content quality, e-store & Shopify, conversion rate optimisation (CRO), quick-commerce, UX optimisation, Meta Ads, Google Ads",
    "skills_commercial": "key account management, brand & partner relationship management, brand onboarding, assortment planning, pricing strategy, category management, business reviews, negotiation, distributor management, modern trade, forecasting",
    "skills_data": "P&L management, KPI tracking & scorecards, sell-in/sell-out, ROI, ROAS, conversion & traffic analysis, AI-assisted analysis & forecasting, retail execution, Looker, Nielsen, Salesforce, SAP",
    "skills_tools": "Salesforce, SAP, Shopify, Meta Ads Manager, Google Ads, Looker, Nielsen, Kantar, Microsoft Office (Expert), Generative AI (Claude, ChatGPT), Canva",
}

# --------------------------------------------------------------------------
# Cover letter content
# --------------------------------------------------------------------------
CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm writing to apply for the Account Manager role on The Dubai Mall Online team. Building a "
        "high-growth marketplace from the ground up alongside the world's most recognised fashion and "
        "sports brands is exactly the work I love — and exactly what I do today, onboarding and scaling "
        "brands on noon and the UAE's quick-commerce platforms from my current role here in Dubai."
    ),
    "body_paragraph_1": (
        "At Miravia (Alibaba Group) I managed 42 key brand accounts across fashion, beauty and "
        "fragrances as their primary point of contact, growing GMV +30% QoQ through assortment "
        "optimisation, pricing and promotions, and onboarding 30+ new brands in two months. At Glovo I "
        "helped build the Retail vertical from scratch, onboarding fashion and lifestyle brands onto the "
        "marketplace. Today at DoFreeze I run the digital shelf across noon, Talabat, Careem and "
        "Deliveroo — managing listings, content quality, pricing and campaigns — so I already know your "
        "platform from the brand-partner side."
    ),
    "body_paragraph_2": (
        "Two things set me apart here: I've already onboarded and grown brands directly on noon, so I'd "
        "be productive from week one; and my career began on the Inditex retail floor (Massimo Dutti), "
        "giving me genuine fashion-retail instinct to pair with marketplace analytics and business "
        "reviews. I'm already based in Dubai on a residence visa — no sponsorship needed, immediate "
        "start — and bilingual Spanish/English (C1), useful for European brands expanding into the GCC."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd grow noon's fashion and sports brand partnerships. I'm "
        "available to start immediately and would love to discuss the role — you can reach me at "
        "+971 50 386 3656 or paulich98@hotmail.com. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="noon-account-manager-dubaimall",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/noon/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Account Manager", "via": "LinkedIn", "team": "The Dubai Mall Online",
             "recruiter": CONTACT},
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
        "ai_score": 94,
        "ai_tier": "Hot",
        "skills_match": [
            "Marketplace account management", "Brand partner relationships",
            "Fashion & sports retail", "Brand onboarding", "Assortment & pricing",
            "Business reviews", "Conversion & traffic analytics",
            "Cross-functional execution", "noon platform (hands-on)", "3-5 yrs exp",
        ],
        "missing_skills": [],
        "sector_fit": "exact",
        "seniority_fit": "exact",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Near-perfect fit: the JD asks for 3-5 yrs Account/Brand/Marketplace management with "
            "fashion/sports retail — Paula's exact profile. 42 key accounts at Miravia/Alibaba "
            "(+30% GMV QoQ), onboarded 30+ brands, built Glovo's fashion Retail vertical, and "
            "currently manages brands directly on noon + UAE quick-commerce. Inditex fashion "
            "pedigree, Dubai residence visa (no sponsorship), C1 English."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _move_into_dated_folder() -> Path:
    """Move output/<Company> - <Role>/ under output/<DATE_FOLDER>/."""
    pos_dir = cv.job_subdir  # not used; compute directly
    from career_ops.generators._paths import job_output_dir
    src = job_output_dir(make_job())            # output/noon - Account Manager
    dated_parent = settings.output_dir / DATE_FOLDER
    dated_parent.mkdir(parents=True, exist_ok=True)
    dest = dated_parent / src.name
    if src.resolve() == dest.resolve():
        return dest
    if dest.exists():
        # merge contents
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

    # Convert the DOCX files that now live in the dated folder.
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
