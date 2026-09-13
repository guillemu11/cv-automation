"""One-off: generate Paula's CV + cover letter for Meituan (Keeta) "Fresh Category
Manager (F&V)" — on-site, Dubai. Owns the fruits & vegetables category with a
focus on IMPORTED produce: category strategy + procurement plans, imported
assortment optimisation, supply-chain management for imported F&V (overseas
suppliers/importers, procurement negotiation, cost control, import channels),
inventory/turnover + promotional strategy to reduce waste, cross-functional work
(procurement, logistics, customs, marketing), import-regulation/customs/cross-
border-logistics awareness, and team leadership.

Honest fit read (this is a STRETCH, not a slam-dunk — Warm, not Hot):
  STRONG / transferable:
    - Category management is her lineage: Category Planning at Mondelez
      (sell-in/sell-out, promo effectiveness, turnover) and category expansion as
      PIC Fragrances at Alibaba's Miravia (+30% GMV QoQ, 42 accounts vs P&L).
    - Deep quick-commerce & e-commerce operator — exactly the "retail, quick
      commerce (Q-commerce), e-commerce, supermarkets" experience the JD PREFERS:
      Glovo retail vertical, Alibaba/Miravia category, and DoFreeze integration
      into Noon/Talabat/Careem/Deliveroo today.
    - Alibaba (Miravia) grounding resonates with Meituan (a Chinese QC giant).
    - Negotiation (42 KAM accounts, Glovo deal-closing, distributor management),
      data analysis, forecasting, business acumen, cross-functional coordination
      with logistics/supply/marketing. Dubai-based.

  HONEST GAPS (stated plainly, NOT fabricated):
    - Her categories are FMCG / beauty / fragrances / fashion / chocolate — NOT
      fresh produce (fruits & vegetables). Fresh/perishable domain is new.
    - No personal ownership of fresh-produce IMPORT procedures, customs clearance
      or cross-border cold-chain logistics — she coordinates with logistics/supply
      but hasn't run imports/customs herself. Framed as ramp-up, not owned.
    - "5+ years in F&V category management or procurement" — she has ~4+ years and
      none in F&V procurement specifically. Not overclaimed.
    - Procurement of goods (vs commercial/partner/distributor negotiation) is
      adjacent, not identical — claimed as transferable commercial negotiation,
      not as done fresh-produce procurement.
    - Team leadership: cross-functional/partner leadership, not formal line
      management of direct reports.
    - Mandarin/Arabic not spoken (JD is in English; neither is required). English
      C1 business-level, not native.
    - NO "no sponsorship needed" claim — visa is employer-sponsored (standing
      rule); header only states "UAE Residence Visa".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-25/.
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

COMPANY = "Meituan"
TITLE = "Fresh Category Manager (F&V)"
DATE_FOLDER = "2026-08-25"

# No hiring manager named in the posting — letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Fresh Category Manager (F&V) — Meituan (Keeta), Dubai, UAE (on-site, full time).

Education: Bachelor's degree or above. Experience: 5+ years.

Key Responsibilities:
- Manage and oversee the fruits & vegetables category, with a focus on imported
  produce, developing category strategies and procurement plans.
- Analyse market trends, consumer demand and competition to optimise imported
  product assortment and improve sales and profitability.
- Handle supply-chain management for imported fruits & vegetables, establish strong
  relationships with overseas suppliers and importers, conduct procurement
  negotiations, control costs and optimise import supply channels.
- Monitor inventory and product turnover; develop promotional strategies to enhance
  inventory turnover and reduce waste.
- Collaborate with various departments (procurement, logistics, customs, marketing)
  to ensure smooth import operations, product quality and market promotion.
- Stay updated on import regulations, customs policies and international market
  trends to ensure compliance and continuously optimise procurement and operations.
- Lead and train the team to enhance professional capabilities and work efficiency.

Qualifications:
- Bachelor's degree or above, preferably in marketing, supply-chain management,
  food science or related fields.
- At least 5 years of experience in fruits & vegetables category management or
  procurement, with a strong focus on imported produce; experience in retail, quick
  commerce (Q-commerce), e-commerce, or supermarkets/hypermarkets preferred.
- Strong understanding of international fresh-produce markets, import supply chains
  and category-management methods.
- Familiarity with import procedures, customs clearance and cross-border logistics.
- Excellent negotiation, data-analysis and market-insight skills.
- Strong communication, coordination and team-management experience.
- High sense of responsibility, ability to work under pressure, keen business acumen
  with an innovative mindset.

Highlights: As a Fresh Produce (F&V) Import Category Manager you will drive rapid
business growth by spearheading new import initiatives and expanding your
international perspective.
"""

ATS = [
    "Fresh Category Manager", "category manager", "category management",
    "category strategy", "category methods", "fruits & vegetables", "fresh produce",
    "imported produce", "assortment optimisation", "assortment", "range planning",
    "procurement", "procurement plans", "procurement negotiation", "sourcing",
    "supplier relationships", "overseas suppliers", "importers", "cost control",
    "supply chain management", "import supply channels", "import operations",
    "import regulations", "customs clearance", "cross-border logistics",
    "inventory", "product turnover", "inventory turnover", "reduce waste",
    "promotional strategy", "promotions", "market trends", "consumer demand",
    "competition analysis", "sales and profitability", "P&L", "forecasting",
    "data analysis", "market insight", "negotiation", "quick commerce",
    "Q-commerce", "e-commerce", "retail", "supermarkets", "hypermarkets",
    "modern trade", "distributor management", "cross-functional collaboration",
    "logistics", "marketing", "team management", "business acumen", "innovation",
    "GCC", "MENA", "UAE", "Dubai", "FMCG",
]

CV_CONTENT = {
    "headline": (
        "Category & Commercial Manager · Quick-Commerce & E-Commerce · "
        "Category Strategy, Assortment, Promotions & Commercial Negotiation · Dubai / GCC"
    ),
    "professional_summary": (
        "Category and commercial manager with 4+ years across consumer goods and quick-commerce — FMCG, Beauty, "
        "Fragrances and Fashion — building category strategy, assortment and promotional plans, negotiating "
        "commercial terms and turning data into working plans across Dubai and 50+ markets. Category is my "
        "lineage: Category Planning at Mondelez (sell-in/sell-out, promotional effectiveness, turnover) and "
        "category expansion as PIC Fragrances at Alibaba's Miravia (+30% GMV QoQ across 42 accounts against P&L "
        "targets through pricing, assortment and promotions). I'm a hands-on quick-commerce and e-commerce "
        "operator — built out Glovo's retail vertical, ran category on Alibaba's Miravia, and integrate brands "
        "into Noon, Talabat, Careem and Deliveroo today at DoFreeze — coordinating cross-functionally with "
        "supply, logistics and marketing. Strong in negotiation, data analysis, forecasting and business acumen, "
        "Dubai-based with an Alibaba e-commerce grounding, native Spanish and business English (C1), plus an "
        "early-adopter edge in generative AI (Claude/GPT) for market research and category insight."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "FMCG consumer goods & distribution | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Develop category, assortment and trade strategy by channel across 50+ markets — building category and promotional plans that grow sell-out, optimise product turnover and improve profitability",
                "Integrate the portfolio into UAE quick-commerce platforms (Noon, Talabat, Careem, Deliveroo) — managing onboarding, listings, assortment and promotional mechanics, and coordinating with logistics for availability and fulfilment",
                "Negotiate with distributors and modern-trade / quick-commerce partners, managing distributor networks, pricing and cost to expand supply channels across markets",
                "Own forecasting and performance tracking — turning sell-in/sell-out, ROI and market/competition data into working category and promotional plans and clear recommendations",
                "Lead NPD end-to-end for 6 launches (brief, pricing, go-to-market), coordinating cross-functionally with supply, product and marketing to launch cleanly",
                "Built an AI-powered automation system (Claude/GPT) for market research, category insight and reporting — cutting manual workload ~40% and accelerating decisions across markets",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees | Category & commercial",
            "bullets": [
                "Led category expansion as PIC Fragrances — building supplier and partner relationships and onboarding 30+ new stores in two months, including official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Managed 42 key accounts against P&L targets (reporting to the CEO on the Flash Sales channel), achieving +30% GMV growth QoQ through pricing, assortment and promotional strategy",
                "Optimised assortment and promotions to grow turnover and profitability, and negotiated commercial terms with brand and distributor partners",
                "Analysed ROI, ROAS, conversion, traffic, competition and retention to construct conclusions and implement recommendations that improved channel performance",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team building Glovo's retail vertical on a leading quick-commerce platform — onboarding new brand and lifestyle partners with tailored plans, launch campaigns and promotions",
                "Managed strategic accounts and negotiated / closed high-impact commercial deals, maximising profitability for both partners and Glovo",
                "Led cross-functional teams across marketing, logistics and customer support to deliver seamless activations and grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees | Category planning",
            "bullets": [
                "Ran category planning for chocolate — sell-in/sell-out analysis, promotional-effectiveness evaluation and turnover/performance reporting that informed commercial planning and spend",
                "Identified growth opportunities and contributed to NPD launches (Milka Spread, Mini Suchard), translating category and competition data into practical recommendations",
            ],
        },
    ],
    "skills_brand": (
        "category strategy, category management (methods), assortment & range planning, promotional strategy & "
        "planning, inventory turnover & waste reduction, market-trend / consumer-demand / competition analysis, "
        "go-to-market, NPD, cross-functional coordination"
    ),
    "skills_ecommerce": (
        "quick-commerce (Noon, Talabat, Careem, Deliveroo), e-commerce & marketplace operations, retail & "
        "modern-trade activation, listings & assortment management, Shopify, digital & social marketing"
    ),
    "skills_commercial": (
        "commercial & distributor negotiation, supplier & partner relationship development, key account "
        "management, distributor & modern-trade management, pricing & cost control, supply & channel "
        "coordination, stakeholder management"
    ),
    "skills_data": (
        "business acumen, P&L management, forecasting, sell-in/sell-out, inventory-turnover analysis, "
        "data analysis → recommendations, KPI tracking, ROI, market & competition insight, "
        "Power BI, Tableau, Nielsen, Kantar"
    ),
    "skills_tools": (
        "Microsoft Office — Expert (Excel, PowerPoint, Word), Power BI, Tableau, Looker, Nielsen, Kantar, "
        "Salesforce, SAP, Generative AI (Claude, ChatGPT), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Meituan's push into Dubai quick-commerce — and building a fresh fruits & vegetables category from a "
        "strong imported base — is exactly the kind of category-and-commercial challenge I'm drawn to, so the "
        "Fresh Category Manager (F&V) role caught my attention. Category strategy, assortment and promotional "
        "planning, commercial negotiation and quick-commerce operations are the spine of my career, I'm "
        "Dubai-based, and I bring an Alibaba (Miravia) e-commerce grounding that resonates with how Meituan builds."
    ),
    "body_paragraph_1": (
        "My background is squarely category and commercial. At Alibaba's Miravia I led category expansion as PIC "
        "Fragrances — building supplier and partner relationships, onboarding 30+ stores in two months, and "
        "managing 42 accounts against P&L targets to grow GMV +30% QoQ through pricing, assortment and "
        "promotions. Before that I ran Category Planning for chocolate at Mondelez (sell-in/sell-out, promotional "
        "effectiveness, turnover). Today at DoFreeze I own category, assortment and go-to-market strategy across "
        "50+ markets, negotiate with distributors and modern-trade partners, integrate the portfolio into UAE "
        "quick-commerce (Noon, Talabat, Careem, Deliveroo), and turn forecasting, market and competition data "
        "into working category and promotional plans — coordinating cross-functionally with supply, logistics "
        "and marketing. That mix — category methods, negotiation, data-led decisions and quick-commerce / "
        "e-commerce operations — is precisely what this role runs on."
    ),
    "body_paragraph_2": (
        "I want to be transparent about where I'd be ramping. My categories have been FMCG, beauty, fragrances "
        "and fashion rather than fresh produce, and while I coordinate closely with logistics and supply, I "
        "haven't personally owned fresh-produce import procedures, customs clearance or cross-border cold-chain — "
        "I'd get up to speed on those quickly and lean on the specialists around me. What I bring instead is a "
        "strong, transferable category-and-commercial craft, genuine quick-commerce and e-commerce depth in this "
        "market, sharp negotiation and data analysis, and a generative-AI edge (Claude/GPT) that accelerates "
        "market research and category insight. My English is business-level C1 (I don't speak Mandarin or Arabic)."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to talk through how I'd approach the first 90 days — mapping the imported F&V "
        "assortment and supplier landscape, building the category and promotional plan to grow turnover and "
        "reduce waste, and coordinating procurement, logistics and marketing to launch and scale cleanly. I'm "
        "already based in Dubai and available for on-site work, I bring real category, commercial and "
        "quick-commerce depth, and I'd be genuinely excited to help Meituan build fresh in the UAE. Thank you "
        "for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="meituan-fresh-category-manager-fv-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (On-site)",
        url="https://www.linkedin.com/jobs/view/meituan-fresh-category-manager-fv",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Meituan Fresh Category Manager F&V Dubai",
             "function": "Category Management / Procurement (Fresh Produce — imported F&V)",
             "workplace": "On-site, Dubai; full time",
             "note": "Meituan (Keeta) quick-commerce; imported fruits & vegetables category; heavy import/customs/cross-border-logistics component; 5+ years F&V category/procurement asked; no hiring manager named; salary not disclosed"},
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
        "salary_raw": "Not disclosed",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 63,
        "ai_tier": "Warm",
        "skills_match": [
            "Category management lineage: Category Planning at Mondelez (sell-in/sell-out, promo effectiveness, turnover) + category expansion as PIC Fragrances at Alibaba's Miravia",
            "Exactly the PREFERRED experience: retail, quick-commerce (Q-commerce) and e-commerce — Glovo retail vertical, Alibaba/Miravia category, DoFreeze integration into Noon/Talabat/Careem/Deliveroo",
            "Alibaba (Miravia) grounding resonates with Meituan (a Chinese quick-commerce giant expanding in Dubai)",
            "Negotiation (42 KAM accounts vs P&L, Glovo deal-closing, distributor management) + data analysis + forecasting + business acumen",
            "Assortment optimisation, promotional strategy and turnover/waste thinking across FMCG categories",
            "Cross-functional coordination with logistics, supply, product and marketing",
            "+30% GMV QoQ across 42 accounts; onboarded 30+ new stores in two months (Alibaba's Miravia)",
            "Dubai-based; native Spanish; business English C1; generative-AI automation edge (Claude/GPT)",
        ],
        "missing_skills": [
            "NOT a fresh-produce (fruits & vegetables) category background — her categories are FMCG/beauty/fragrances/fashion/chocolate; perishable/fresh domain is new (transferable category craft is claimed, F&V domain is not)",
            "No personal ownership of fresh-produce IMPORT procedures, customs clearance or cross-border cold-chain logistics — she coordinates with logistics/supply but hasn't run imports/customs herself (framed as ramp-up, not owned)",
            "'5+ years in F&V category management or procurement' — she has ~4+ years total and none in F&V procurement specifically; not overclaimed",
            "Procurement of goods vs commercial/partner/distributor negotiation is adjacent, not identical — claimed as transferable commercial negotiation, not as done fresh-produce procurement",
            "Team leadership is cross-functional/partner leadership, not formal line-management of direct reports",
            "Mandarin/Arabic not spoken (neither required; JD is English); English C1 business-level, not native",
        ],
        "sector_fit": "partial — quick-commerce / e-commerce / retail category management is a direct match; imported fresh-produce (F&V) + customs/cross-border-logistics is the new element, positioned honestly",
        "seniority_fit": "on-band — Category Manager matches Paula's Brand & Marketing Manager / KAM seniority (lateral), though the JD asks 5+ years F&V-specific which she does not have",
        "red_flags": [
            "Fresh produce (F&V) domain is genuinely new to her — the single biggest gap; framed truthfully (category & commercial craft transfers, fresh/perishable + imports are new)",
            "Import procedures / customs clearance / cross-border cold-chain not personally owned — soft coordination only",
            "JD asks 5+ years F&V category/procurement; Paula ~4+ years, none F&V-specific — a real stretch on the hard requirement",
            "On-site in Dubai — no issue (she's Dubai-based)",
            "Salary not disclosed — cannot confirm against her 20,000 AED/month floor",
            "Meituan/Keeta is Mandarin-heavy internally in some teams — not required in the JD but worth noting",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Honest, transparent stretch fit (Warm, not Hot). The role is a category & commercial manager for "
            "Meituan/Keeta's imported fruits & vegetables category in Dubai quick-commerce: own category strategy "
            "and procurement plans, optimise imported assortment, manage supply chain and overseas suppliers, run "
            "procurement negotiations and cost control, drive inventory turnover and waste reduction via "
            "promotions, coordinate procurement/logistics/customs/marketing, and stay on top of import "
            "regulations and customs. Paula's core craft maps well on category management, assortment, "
            "promotions, negotiation, data/business acumen and — critically — the PREFERRED quick-commerce / "
            "e-commerce / retail experience (Glovo retail vertical, Alibaba's Miravia category, DoFreeze QC "
            "integration into Noon/Talabat/Careem/Deliveroo), plus an Alibaba grounding that resonates with "
            "Meituan. The real gaps are the fresh-produce (F&V) domain, hands-on import/customs/cross-border "
            "cold-chain, and the 5+ years F&V-specific requirement — none of which she owns. CV leads with the "
            "category/commercial/quick-commerce/negotiation/data craft; the cover letter states the fresh-produce "
            "and import/customs gaps plainly and frames them as fast ramp-up. No fabricated F&V or import "
            "experience, no native-English/Mandarin/Arabic claim, no 'no sponsorship needed' claim."
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
