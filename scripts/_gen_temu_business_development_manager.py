"""One-off: generate Paula's CV (+ cover letter) for Temu — Business Development
Manager (marketplace merchant/seller recruitment & development).

Why this is a strong, honest fit:
  - The role is marketplace BD: proactively recruit and develop local partnerships
    with merchandise partners, manufacturers and brands; help them establish and
    grow on the platform; guide them on market positioning, product planning,
    brand marketing and operational strategy; run industry/data analysis to steer
    category strategy.
  - This is the direct twin of work Paula has DONE: at Alibaba's Miravia she
    recruited/onboarded 30+ new vendors/brands in two months (PIC Fragrances) and
    grew 42 merchant accounts +30% GMV QoQ; at Glovo she helped build the Retail
    vertical 0-to-1, proactively onboarding new brands onto the platform. Both are
    literally "recruit and develop partnerships with merchandise partners and
    brands + help them grow on the platform".
  - Chinese-marketplace familiarity: Miravia = Alibaba, so the platform-operations
    playbook Temu (PDD) runs on is familiar terrain — an honest, differentiated
    edge.
  - Requirements met: 5 yrs vs 3+ (brand management + platform operations); strong
    data/industry analysis (advanced Excel, Power BI); marketing-innovation and
    merchant-guidance capability; works under pressure / peak logistics (Glovo QC
    peaks, Miravia Flash Sales).

Honest notes (NOT fabricated):
  - "Extensive local UAE seller/vendor networks" is only "a plus"; Paula has been
    building UAE vendor/distributor relationships for ~1 year (via DoFreeze) — a
    fast-growing network, NOT a decade-deep local rolodex. Framed honestly.
  - Her categories are beauty/fragrances/fashion + FMCG; Temu is all-category — BD
    craft is category-agnostic, disclosed lightly.
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-22/.
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

COMPANY = "Temu"
TITLE = "Business Development Manager"
DATE_FOLDER = "2026-08-22"

CONTACT = None  # No hiring manager named — letter addressed to "Hiring Manager".

JOB_DESCRIPTION = """\
Business Development Manager — Temu (rapidly growing e-commerce marketplace).

Responsibilities:
- Proactively recruit and develop effective local partnerships with merchandise
  partners, manufacturers and brands. Focus on category selection to increase
  overall value, aligned with business and customer needs.
- Assist merchandise partners in establishing themselves on the platform and their
  growth. Guide partners in developing comprehensive plans including market
  positioning, product planning, brand marketing and operational strategies.
- Propose innovative ideas based on the current status of the categories; create
  and implement projects through resource integration and merchant guidance.
- Conduct industry analysis reports, explore potential customer needs through data
  analysis, and adjust strategies based on market trends.

Required skills:
- 3+ years of operational experience, including but not limited to brand
  management or platform operations.
- Extensive connections/relationships with local seller and vendor networks is a
  plus.
- Strong data analysis skills — analyse industry trends and manage projects
  through data, and summarise conclusions.
- Market exploration and marketing-innovation capability; able to guide overall
  merchant marketing plans.
- Excellent problem-solving, self-motivation, strategic thinking, quick to adapt.
- Ability to work under pressure and manage logistics during high-demand periods.
"""

ATS = [
    "Business Development Manager", "business development", "BD",
    "merchant recruitment", "seller recruitment", "vendor recruitment",
    "partnerships", "local partnerships", "merchandise partners", "manufacturers",
    "brands", "onboarding", "platform operations", "marketplace", "e-commerce",
    "category selection", "category growth", "selection", "assortment",
    "merchant growth", "market positioning", "product planning", "brand marketing",
    "operational strategy", "merchant guidance", "resource integration",
    "project management", "industry analysis", "data analysis", "market trends",
    "competitive benchmarking", "Excel", "Power BI", "KPIs", "negotiation",
    "joint business plans", "vendor networks", "distributor management",
    "quick-commerce", "noon", "Talabat", "Careem", "Deliveroo", "GMV", "ROI",
    "ROAS", "under pressure", "logistics", "Dubai", "UAE", "marketing innovation",
]

CV_CONTENT = {
    "headline": (
        "Business Development & Marketplace Partnerships · Merchant / Vendor Recruitment & Onboarding · "
        "Seller Growth, Category & Brand Guidance · Industry & Data Analysis · Ex-Alibaba Marketplace"
    ),
    "professional_summary": (
        "Business-development and marketplace-partnerships manager with five years across top e-commerce "
        "platforms and consumer brands, now building brand and vendor partnerships across UAE marketplaces from "
        "Dubai. I recruit, onboard and grow merchant partners: at Alibaba's Miravia I onboarded 30+ new "
        "vendors/brands in two months and grew 42 accounts +30% GMV QoQ, and at Glovo I helped build the Retail "
        "vertical from 0-to-1, taking new brands onto the platform. I guide partners on what makes them succeed "
        "on a marketplace — market positioning, product and assortment planning, brand marketing and operational "
        "strategy — and I run the data behind it: industry analysis, trend-spotting and benchmarking in Excel "
        "and Power BI. Trained inside a Chinese-owned marketplace (Alibaba), fluent in the platform-operations "
        "playbook, resourceful and comfortable under pressure. Business Administration graduate (CUNEF), based "
        "in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Brands: Befit, Eurocake, Flair | UAE marketplaces + 50+ countries",
            "bullets": [
                "Build and manage vendor, distributor and marketplace partnerships across the UAE — onboarding and growing brands on noon, Talabat, Careem and Deliveroo (listings, selection, promo mechanics, retail execution)",
                "Guide brands and partners on what wins on-platform — market positioning, assortment / product planning, brand marketing and operational strategy",
                "Identify category and selection opportunities through industry and competitive analysis (Excel, Power BI) and turn them into projects and growth plans",
                "Negotiate joint plans and promotions with partners, aligning on shared targets through resource integration",
                "Operate across 50+ markets under fast-moving, high-demand conditions, coordinating supply and logistics with cross-functional teams",
                "Built an AI-powered analytics & automation system (Claude / generative AI) that speeds up industry analysis, reporting and partner planning",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees",
            "bullets": [
                "Recruited and onboarded 30+ new brands/vendors in two months as PIC Fragrances — the direct equivalent of this BD role — including leading houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Owned 42 merchant accounts end-to-end on a top-5 e-commerce marketplace (Alibaba), growing GMV +30% QoQ through selection, pricing, assortment and promotions",
                "Helped partners establish and grow on the platform — guiding market positioning, assortment planning, brand marketing and promotional strategy",
                "Ran industry, competitive and performance analysis (conversion, traffic, ROI, ROAS) to steer category strategy and adapt to market trends",
                "Owned the Flash Sales channel under deadline-driven, high-demand conditions, reporting to the CEO",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical from 0-to-1 — proactively recruiting and onboarding new brands and partners onto the platform",
                "Negotiated and closed high-impact commercial deals and joint activations with partners",
                "Managed logistics and delivery under high-demand peaks, coordinating cross-functional teams",
                "Drove GMV growth for strategic partners through data-led planning and promotions",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Produced industry, category and consumer-trend analysis and performance reports for the commercial team",
                "Ran sell-in/sell-out analysis and identified assortment and growth opportunities",
                "Supported NPD launches from concept to execution",
            ],
        },
    ],
    "skills_brand": (
        "merchant / partner marketing guidance, market positioning, product & assortment planning, "
        "brand marketing, category growth, promotions & campaigns, marketing innovation, go-to-market"
    ),
    "skills_ecommerce": (
        "marketplace / platform operations, seller & vendor onboarding, e-commerce & quick-commerce "
        "(noon, Talabat, Careem, Deliveroo), selection & catalogue growth, listings, merchandising, Shopify"
    ),
    "skills_commercial": (
        "business development, merchant / vendor / brand recruitment, partnership development, "
        "negotiation & deal closing, joint business plans, resource integration, key account management, "
        "distributor management, working under pressure / peak logistics"
    ),
    "skills_data": (
        "industry & market-trend analysis, data analysis (Excel — advanced), competitive benchmarking, "
        "project management through data, performance metrics & KPIs, ROI / ROAS / conversion, Power BI, forecasting"
    ),
    "skills_tools": (
        "Excel (Advanced), Power BI, Salesforce (CRM), SAP, Generative AI (Claude, ChatGPT), Shopify, "
        "Nielsen, Kantar, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Temu's growth runs on business developers who can go out, recruit merchant partners, and actually make "
        "them succeed on the platform — and that's a job I've done. At Alibaba's Miravia I recruited and "
        "onboarded 30+ new vendors and brands in two months and grew 42 merchant accounts +30% GMV QoQ; at "
        "Glovo I helped build the Retail vertical from zero, proactively bringing new brands onto the platform. "
        "Having come up inside a Chinese-owned marketplace (Alibaba), the platform-operations playbook Temu runs "
        "on is familiar terrain, and I'm now building vendor and brand partnerships in the UAE market from Dubai."
    ),
    "body_paragraph_1": (
        "The responsibilities map directly onto my experience. I recruit and develop partnerships with "
        "merchandise partners and brands, and I help them establish and grow — guiding market positioning, "
        "product and assortment planning, brand marketing and operational strategy, exactly as I did for the "
        "merchants I onboarded at Miravia and the brands I took onto Glovo. I focus category selection to grow "
        "value, propose and run projects through resource integration and merchant guidance, and I steer it all "
        "with data: industry and competitive analysis, trend-spotting and project management through numbers in "
        "Excel and Power BI. I'm also comfortable under pressure and through peak periods — I owned Miravia's "
        "Flash Sales channel on tight deadlines and managed logistics through high-demand peaks at Glovo — and "
        "I've built an AI-powered system (Claude) that accelerates my industry analysis and reporting."
    ),
    "body_paragraph_2": (
        "One honest note on the 'plus' you mention: I've been building UAE vendor and distributor relationships "
        "over the past year through my current role — a fast-growing local network rather than a decade-deep "
        "rolodex yet, but I know how to open and develop these relationships from scratch, which is what BD "
        "actually rewards. My category background is beauty, fragrances, fashion and FMCG, and Temu spans every "
        "category — but recruiting merchants, guiding their growth and reading a category through data is craft "
        "that travels, and I adapt fast. What I bring is a proven marketplace-BD track record, Chinese-platform "
        "familiarity, and the self-motivated, resourceful, move-fast attitude this role is built for."
    ),
    "closing_paragraph": (
        "I'd be excited to help Temu recruit and grow its merchant base and prove it in selection, partnerships "
        "and GMV — and I can share case studies (from onboarding 30+ vendors in two months to +30% GMV QoQ). "
        "I'm based in Dubai and ready to move fast. Thank you for your consideration — I look forward to hearing "
        "from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="temu-business-development-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Business Development Manager marketplace",
             "function": "Marketplace BD / merchant recruitment & development / platform operations",
             "sector": "E-commerce marketplace (Temu / PDD)",
             "note": "Strong, honest fit — direct twin of her Miravia vendor-onboarding + Glovo platform-vertical "
                     "BD, plus Chinese-marketplace familiarity (Alibaba). Honest notes: 'extensive local UAE "
                     "seller network' is only 'a plus' and hers is ~1yr/growing, not a legacy rolodex "
                     "(disclosed); categories are beauty/fashion/FMCG vs Temu all-category (BD is category-"
                     "agnostic). Location not stated in posting; assumed Dubai. Temu is known for an intense "
                     "work culture — worth a human go/no-go. No 'own visa / no sponsorship' claim."},
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
            "DIRECT TWIN: recruited & onboarded 30+ new vendors/brands in two months at Alibaba's Miravia (PIC Fragrances) — literally 'recruit and develop partnerships with merchandise partners and brands'",
            "Platform-vertical BD from 0-to-1 — helped build Glovo's Retail vertical, proactively onboarding new brands onto the platform",
            "Help partners establish & grow — guides market positioning, product/assortment planning, brand marketing, operational strategy",
            "Category selection to increase value; +30% GMV QoQ across 42 merchant accounts",
            "Strong data/industry analysis — trend analysis, competitive benchmarking, project mgmt through data (advanced Excel + Power BI)",
            "Chinese-marketplace familiarity (Alibaba/Miravia) — Temu/PDD platform-ops playbook is familiar terrain",
            "Works under pressure / peak logistics — Miravia Flash Sales (deadline-driven) + Glovo high-demand logistics",
            "Marketing-innovation & merchant marketing guidance; negotiation & deal closing; 5 yrs vs 3+ asked; based in Dubai",
        ],
        "missing_skills": [
            "'Extensive local UAE seller/vendor network' (only a 'plus') — Paula's UAE vendor/distributor network is ~1yr old and growing, NOT a legacy local rolodex. Disclosed honestly; she brings proven ability to open/develop relationships from scratch",
            "Category background is beauty/fragrances/fashion + FMCG vs Temu all-category — BD craft is category-agnostic; disclosed lightly",
        ],
        "sector_fit": "excellent (marketplace merchant recruitment/development = her Miravia + Glovo + DoFreeze work; Chinese-platform familiarity)",
        "seniority_fit": "on-band / slightly over (5 yrs vs 3+; KAM/AM/Brand Mgr experience covers BD craft)",
        "red_flags": [
            "Temu is known for an intense, high-pressure work culture (the JD itself stresses 'work under pressure' and 'manage logistics during high-demand periods') — worth a candid human go/no-go on lifestyle fit.",
            "Location not stated in the posting (assumed Dubai given 'local partnerships') — confirm before advancing.",
            "Local-vendor-network 'plus' is partially met (growing, not deep) — disclosed honestly, not inflated.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit. Temu's BD role is marketplace merchant/seller recruitment and development: "
            "proactively recruit local merchandise partners/manufacturers/brands, help them establish and grow "
            "on-platform, guide them on positioning/product planning/brand marketing/ops, and run industry/data "
            "analysis to steer category strategy. This is the direct twin of what Paula has done — onboarding "
            "30+ vendors in two months and growing 42 merchant accounts +30% GMV QoQ at Alibaba's Miravia, and "
            "building Glovo's Retail vertical 0-to-1 by recruiting brands onto the platform — with the added, "
            "honest edge of Chinese-marketplace familiarity (Alibaba). She meets the requirements (5 yrs vs 3+, "
            "brand management + platform operations, advanced Excel/Power BI industry analysis, works under "
            "pressure/peaks). Honest gaps: the 'extensive local UAE seller network' plus is only partly met "
            "(hers is ~1yr and growing, disclosed) and her categories are beauty/fashion/FMCG vs Temu's all-"
            "category (BD is category-agnostic). Temu's intense culture warrants a human go/no-go. No 'own visa "
            "/ no sponsorship' claim."
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
