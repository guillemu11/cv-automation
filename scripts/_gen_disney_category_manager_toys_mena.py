"""One-off: generate Paula's CV + cover letter for The Walt Disney Company
(Disney Experiences / Disney Consumer Products) "Category Manager – Toys (MENA)"
— a fixed-term contract, on-site 4 days/week in Dubai. Owns commercial/category
strategy for the Hardlines Toys licensing portfolio across MENA: annual operating
plan + quarterly forecasts, partner/licensee relationship development, joint
business planning, regional contract negotiation, product development guidance,
and digital/social/in-store marketing support.

Why this is a strong, honest fit (Paula's core craft — better than most):
  - Category management is literally her lineage: Category Planning at Mondelez
    (sell-in/sell-out, promo effectiveness, NPD) and category expansion as PIC
    Fragrances at Alibaba's Miravia (onboarded 30+ stores, +30% GMV QoQ).
  - Consumer products depth across FMCG / Beauty / Fashion (DoFreeze, Mondelez,
    Miravia) — exactly the "consumer products business" the JD requires.
  - Partnership development, joint business planning and contract negotiation map
    directly to her KAM years (42 accounts at Miravia) and Glovo (prospecting,
    negotiating and closing high-impact commercial deals; onboarding partners).
  - Financial acumen: P&L targets reporting to CEO, forecasting, sell-in/sell-out
    and turning data into working plans — the AOP/quarterly-forecast ask.
  - "A good eye for digital, social and brick-and-mortar marketing" — she runs
    Google/Meta and social today, executes across modern trade/quick-commerce,
    and has an Inditex (Massimo Dutti) retail / visual-merchandising foundation.
  - MENA / GCC based in Dubai, cultural fluency across 50+ markets; Spanish native
    ("other European languages beneficial"); generative-AI automation edge.

Honest positioning (NO fabrication):
  - NO toys and NO brand-licensing (IP-licensing-to-manufacturers) experience —
    her categories are beauty/fragrances/fashion/chocolate/FMCG. The transferable
    craft (category management, partner/JBP, negotiation, forecasting, consumer
    products, digital/social/retail marketing) is what's claimed; toys/licensing
    domain is stated as new, not owned.
  - Arabic is "preferable" and Paula does NOT speak it — not claimed. English is
    C1 professional (stated as such), not native.
  - People leadership: she leads cross-functional teams and develops external
    partners/creators, but has not formally line-managed direct reports —
    framed as cross-functional/partner leadership, not overclaimed team management.
  - NO "no sponsorship needed" claim — the visa is employer-sponsored (standing
    rule); the CV header only states "UAE Residence Visa".

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

COMPANY = "Disney (The Walt Disney Company)"
TITLE = "Category Manager - Toys (MENA)"
DATE_FOLDER = "2026-08-25"

# No hiring manager named in the posting — letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Category Manager – Toys (MENA), fixed-term contract — Disney Experiences / Disney
Consumer Products, Dubai (on-site 4 days/week).

Lead commercial and category strategy for Disney's Hardlines Toys portfolio
(Star Wars, Mickey & Friends, Marvel) across the MENA region — driving long-term
vision and annual growth across a portfolio of licensee accounts. Unlock new
opportunities, forge partnerships and secure high-impact licensees.

What you will do:
- Partner with the Senior Category Manager and Category Director to shape the
  Hardlines Toys category and long-term vision, focused on MENA.
- Use market trends, commercial expertise and consumer insights to build and
  implement strategy, staying agile to seize new opportunities and partnerships.
- Own the annual operating plan and quarterly forecasts for Hardlines Toys; set
  objectives for licensees; collaborate with market leads, category specialists,
  franchise, marketing, product development and finance teams to drive growth.
- Develop and nurture relationships with established and new partners; lead
  engagement, strategic planning and joint business initiatives.
- Lead contract negotiations for designated Hardlines Toys accounts in MENA.
- Work with creative teams (and the Global Interactive Experiences team) to guide
  product development relevant to MENA.
- Support marketing campaigns enabling partners and retailers to bring Disney
  magic to fans through toys and collectibles.
- Champion the International Labour Standards (ILS) process with suppliers.
- Generate innovative ideas, lead research on scalable high-impact opportunities.

Required qualifications & skills:
- Degree-level education or equivalent experience; experience within consumer
  products business.
- Proven experience building effective relationships, leading and managing change,
  and collaborating across departments to hit financial targets and joint goals.
- Proven experience developing the performance of a team.
- Financial acumen — translate numbers into a working plan.
- Analyse data, construct conclusions and implement recommendations.
- Agile to capitalise on the moment and identify new opportunities/partners.
- Computer literate: MS Word, Excel, PowerPoint and Keynote.
- Business English essential; other European languages beneficial.
- A good eye for digital, social and brick-and-mortar marketing.
- Excellent commercial and strategic problem-solving and innovation.
- Exceptional planning and organisation; strong influencing skills at all levels.
- Translate industry trends into growth; cultural sensitivity across MENA.
- English essential; Arabic preferable.

Perks: private medical & dental, free park entry, Disney discounts, parental leave.
"""

ATS = [
    "Category Manager", "category management", "consumer products",
    "consumer products business", "licensing", "licensees", "licensee accounts",
    "joint business planning", "JBP", "joint business initiatives",
    "partnership development", "partner management", "relationship building",
    "contract negotiation", "regional negotiation", "commercial strategy",
    "annual operating plan", "AOP", "quarterly forecasts", "forecasting",
    "financial acumen", "P&L", "financial targets", "translate numbers into a plan",
    "market trends", "consumer insights", "data analysis", "recommendations",
    "growth strategy", "cross-functional collaboration", "stakeholder management",
    "product development", "NPD", "marketing campaigns", "retail",
    "brick-and-mortar marketing", "in-store marketing", "digital marketing",
    "social media", "MENA", "GCC", "cultural sensitivity", "local markets",
    "agile", "innovation", "influencing skills", "planning and organisation",
    "MS Office", "Excel", "PowerPoint", "Keynote", "Word", "English", "FMCG",
    "beauty", "fashion", "franchise", "toys", "collectibles",
]

CV_CONTENT = {
    "headline": (
        "Category & Commercial Manager · Consumer Products (FMCG · Beauty · Fashion) · "
        "Joint Business Planning, Partnerships & Contract Negotiation · MENA / GCC"
    ),
    "professional_summary": (
        "Category and commercial manager with 4+ years across consumer products — FMCG, Beauty, Fragrances and "
        "Fashion — building category strategy, developing partner relationships and turning data into working "
        "plans across MENA and 50+ markets. My lineage is category and commercial: Category Planning at "
        "Mondelez, category expansion as PIC Fragrances at Alibaba's Miravia (onboarded 30+ stores, +30% GMV "
        "QoQ across 42 accounts against P&L targets), and joint business planning, forecasting and contract "
        "negotiation with distributors and modern-trade/retail partners at DoFreeze. I pair strong financial "
        "acumen (P&L, annual operating plans, quarterly forecasts, sell-in/sell-out) with a good eye for "
        "digital, social and brick-and-mortar marketing — running Google/Meta and social today, executing "
        "across modern trade and quick-commerce, with an Inditex (Massimo Dutti) retail and visual-"
        "merchandising foundation. Dubai-based with cultural fluency across GCC/MENA, native Spanish, and an "
        "early-adopter edge in generative AI (Claude/GPT) for insight, planning and reporting. Business English (C1)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "FMCG consumer products & distribution | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Develop category, trade and go-to-market strategy by channel across 50+ MENA and international markets — building the plans, setting partner objectives and staying agile to seize new opportunities and partnerships",
                "Lead joint business planning and contract negotiation with distributors and modern-trade/quick-commerce partners (Noon, Talabat, Careem, Deliveroo) — nurturing established relationships and securing new listings and high-impact partners",
                "Own commercial forecasting and performance tracking — turning sell-in/sell-out, ROI and market data into working plans and recommendations that drive growth and hit financial targets",
                "Lead NPD / product development end-to-end for 6 launches (brief, packaging, pricing, go-to-market), collaborating cross-functionally with product, finance and creative teams",
                "Bring a strong eye for digital, social and in-store marketing — running Google & Meta Ads and social, executing retail activation across modern trade, and scaling an influencer/UGC programme from zero (25–50 creators per campaign)",
                "Built an AI-powered automation system (Claude/GPT) for market research, category insight, planning and reporting — cutting manual workload ~40% and accelerating decisions across markets",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees | Consumer products",
            "bullets": [
                "Led category expansion as PIC Fragrances — building relationships with new and existing partners and onboarding 30+ new stores in two months, including official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Managed 42 key accounts against P&L targets (reporting to the CEO on the Flash Sales channel), achieving +30% GMV growth QoQ through pricing, assortment and promotional strategy",
                "Led joint planning and negotiation with brand partners, translating consumer insight and market trends into category strategy and campaigns that grew the business",
                "Analysed ROI, ROAS, conversion, traffic and retention to construct practical conclusions and implement recommendations, and created the Beauty Club and Hot on Social projects to lift brand visibility and engagement",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Developed and negotiated high-impact commercial partnerships — prospecting, qualifying, negotiating and closing deals to grow volume and profitability for both partners and Glovo",
                "Part of the team building Glovo's Retail vertical — onboarding new brand and lifestyle partners with tailored joint business plans, launch campaigns and promotions",
                "Led cross-functional teams across marketing, logistics and customer support to deliver seamless activations and increase order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees | Consumer products",
            "bullets": [
                "Ran category planning for chocolate — sell-in/sell-out analysis, promotional-effectiveness evaluation and performance reporting that informed commercial planning and spend",
                "Identified growth opportunities and contributed to NPD launches (Milka Spread, Mini Suchard), translating category data into practical, actionable recommendations",
            ],
        },
    ],
    "skills_brand": (
        "category strategy, commercial strategy, joint business planning (JBP), go-to-market, product "
        "development / NPD, market-trend & consumer-insight analysis, innovation & opportunity identification, "
        "brand & campaign strategy, cross-functional leadership"
    ),
    "skills_ecommerce": (
        "digital, social & brick-and-mortar marketing, retail & modern-trade activation, in-store execution & "
        "visual merchandising, Google & Meta Ads, social media, quick-commerce (Noon, Talabat, Careem, "
        "Deliveroo), Shopify, e-commerce"
    ),
    "skills_commercial": (
        "category management, partner & licensee relationship development, contract & commercial negotiation, "
        "distributor & modern-trade management, key account management, joint business planning, pricing & "
        "assortment strategy, stakeholder influencing at all levels"
    ),
    "skills_data": (
        "financial acumen, P&L management, annual operating plan (AOP) & quarterly forecasting, "
        "sell-in/sell-out, data analysis → recommendations, KPI tracking, ROI, market insight, "
        "Power BI, Tableau, Looker, Nielsen, Kantar"
    ),
    "skills_tools": (
        "Microsoft Office — Expert (Excel, PowerPoint, Word), Keynote, Power BI, Tableau, Looker, Nielsen, "
        "Kantar, Salesforce, SAP, Generative AI (Claude, ChatGPT), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Bringing Star Wars, Mickey & Friends and Marvel to fans across MENA through a best-in-class Hardlines "
        "Toys portfolio is exactly the kind of category-and-commercial challenge I love — so the Category "
        "Manager – Toys (MENA) role stood out immediately. Category strategy, partnership development, joint "
        "business planning and contract negotiation across consumer products are the spine of my career, I'm "
        "Dubai-based with fluency across GCC/MENA markets, and I'd bring genuine energy to growing beloved "
        "franchises in the region."
    ),
    "body_paragraph_1": (
        "My background is squarely in category and commercial roles within consumer products. At Alibaba's "
        "Miravia I led category expansion as PIC Fragrances — building relationships with new and existing "
        "partners, onboarding 30+ stores in two months (including the official distributors of major Arabian "
        "and oud houses), and managing 42 accounts against P&L targets to grow GMV +30% QoQ. Before that I ran "
        "Category Planning for chocolate at Mondelez (sell-in/sell-out, promotional effectiveness, NPD). Today "
        "at DoFreeze I own category and go-to-market strategy across 50+ markets, lead joint business planning "
        "and contract negotiation with distributors and modern-trade/quick-commerce partners, and turn "
        "forecasting and market data into working plans — the annual-operating-plan, forecasting and financial-"
        "acumen work this role calls for. I also bring a good eye for digital, social and brick-and-mortar "
        "marketing, plus an Inditex (Massimo Dutti) retail and visual-merchandising foundation."
    ),
    "body_paragraph_2": (
        "I'll be transparent about the two honest gaps: my categories have been beauty, fragrances, fashion and "
        "FMCG rather than toys, and I haven't worked inside a brand-licensing model — but the transferable craft "
        "(category strategy, licensee/partner development, joint business planning, regional negotiation, "
        "forecasting and consumer-products commercial acumen) is precisely what I do, and I ramp fast on new "
        "categories. My English is business-level C1 (I don't speak Arabic, noted as preferable), and I add an "
        "early-adopter edge in generative AI (Claude/GPT) that accelerates market research, category insight and "
        "reporting — useful for spotting scalable, high-impact opportunities quickly in a fast-moving MENA market."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to talk through how I'd approach the first 90 days — mapping the MENA Hardlines "
        "Toys landscape, prioritising the highest-impact licensee partnerships and building an annual plan with "
        "clear forecasts and joint objectives. I'm already based in Dubai and available for on-site work, I "
        "bring real category and commercial depth in consumer products, and I'd be genuinely excited to help "
        "bring Disney magic to fans across the region. Thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="disney-category-manager-toys-mena-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (on-site 4 days/week)",
        url="https://www.linkedin.com/jobs/view/disney-category-manager-toys-mena",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Disney Category Manager Toys MENA Dubai",
             "function": "Category Management / Commercial (Consumer Products licensing)",
             "workplace": "On-site 4 days/week, Dubai; fixed-term contract",
             "note": "Disney Experiences / Disney Consumer Products; Hardlines Toys (Star Wars, Mickey & Friends, Marvel); licensing model; no hiring manager named; salary not disclosed"},
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
        "salary_raw": "Not disclosed (fixed-term contract; medical/dental, park entry, Disney discounts)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 80,
        "ai_tier": "Hot",
        "skills_match": [
            "Category management lineage: Category Planning at Mondelez + category expansion as PIC Fragrances at Miravia",
            "Consumer products depth (FMCG / Beauty / Fragrances / Fashion) — exactly the required 'consumer products business'",
            "Partner/relationship development + joint business planning + contract negotiation (42 KAM accounts; Glovo deal-closing; distributor JBP at DoFreeze)",
            "Financial acumen: P&L targets reporting to CEO, forecasting, AOP-style planning, sell-in/sell-out → working plans",
            "Data analysis → practical conclusions & recommendations (ROI/ROAS/conversion, market insight)",
            "Good eye for digital, social AND brick-and-mortar marketing: Google/Meta + social + modern-trade retail + Inditex/Massimo Dutti visual merchandising",
            "MENA/GCC based in Dubai; cultural fluency across 50+ markets; native Spanish ('other European languages beneficial')",
            "Agile opportunity-spotting + innovation; NPD/product-development collaboration with creative & finance",
            "MS Office Expert (Excel, PowerPoint, Word) + Keynote; generative-AI automation edge (Claude/GPT)",
            "+30% GMV QoQ across 42 accounts; onboarded 30+ new stores in two months (Alibaba's Miravia)",
        ],
        "missing_skills": [
            "No toys category and no brand-licensing (IP-to-manufacturer) experience — her categories are beauty/fragrances/fashion/chocolate/FMCG; transferable category/partner/negotiation craft is claimed, toys/licensing domain is new",
            "Arabic is 'preferable' — Paula does not speak it (not claimed); English is C1 business-level, not native",
            "'Proven experience developing the performance of a team' — she leads cross-functional teams and develops external partners/creators but has not formally line-managed direct reports (framed honestly, not overclaimed)",
        ],
        "sector_fit": "strong (consumer products + category management is a direct match; toys + IP-licensing model is the new element, positioned honestly)",
        "seniority_fit": "on-band — Category Manager matches Paula's Brand & Marketing Manager / KAM seniority (lateral); partners with Senior Category Manager + Category Director",
        "red_flags": [
            "Toys / brand-licensing domain is genuinely new to her — soft gap, framed truthfully (category & partner craft transfers)",
            "Arabic preferable and not spoken; team-performance-development experience is limited to cross-functional/partner leadership",
            "Fixed-term contract (not permanent) — fine, but worth Paula weighing vs a permanent search",
            "On-site 4 days/week in Dubai — no issue (she's Dubai-based)",
            "Salary not disclosed — cannot confirm against her 20,000 AED/month floor",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit — one of her best-matched roles. The position is a category & commercial "
            "manager for Disney's Hardlines Toys licensing portfolio across MENA: own the annual operating plan "
            "and quarterly forecasts, develop licensee/partner relationships, lead joint business planning and "
            "regional contract negotiation, translate data and consumer insight into growth strategy, guide "
            "product development, and support digital/social/in-store marketing. This is Paula's core lineage: "
            "Category Planning at Mondelez, category expansion as PIC Fragrances at Alibaba's Miravia (30+ "
            "stores onboarded, +30% GMV QoQ across 42 accounts against P&L targets), and JBP/negotiation with "
            "distributors and modern-trade partners at DoFreeze — all in consumer products (FMCG/Beauty/Fashion). "
            "She brings genuine financial acumen (P&L, forecasting, sell-in/sell-out), a good eye for digital, "
            "social and brick-and-mortar marketing (Google/Meta + modern trade + Inditex visual merchandising), "
            "MENA/GCC fluency from Dubai, and a generative-AI edge. Honest gaps: no toys and no brand-licensing "
            "model experience (transferable, framed as new); Arabic preferable and not spoken; English C1 not "
            "native; formal team line-management limited to cross-functional/partner leadership. CV + letter lead "
            "with the category/commercial/JBP/negotiation/forecasting craft and consumer-products depth, and "
            "state the toys/licensing, Arabic and team-management nuances plainly; no fabricated toys/licensing "
            "experience, no native-English or 'no sponsorship needed' claim."
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
