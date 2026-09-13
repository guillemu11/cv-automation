"""One-off: generate Paula's CV + cover letter for dsm-firmenich
"Account Manager Fine Fragrance Experience" (Dubai, Sales function).

Why this is a strong, honest fit:
  - Fine fragrance is where Paula has her sharpest commercial edge: at Alibaba's
    Miravia she led the Fragrances category as PIC, onboarding the official
    distributors of the leading Arabian & oud houses (Arabian Oud, Lattafa,
    Swiss Arabian, Ajmal) — genuine Middle East fine-fragrance market fluency.
  - Core role skills are her explicit track: key account management (42 accounts,
    +30% GMV QoQ), client-relationship ownership, sales & distribution / channel
    development (DoFreeze distributor networks across 50+ markets), forecasting &
    pipeline management, tailored commercial proposals, and end-to-end project
    management (6 NPD launches).

Honest positioning (NO fabrication):
  - Paula's fragrance experience is on the BRAND / RETAIL / DISTRIBUTION side
    (managing fragrance-brand accounts and distributors on a marketplace), NOT
    selling fragrance creations/concentrates B2B from a creative house. Framed as
    adjacent — deep market + account fluency — never as fragrance-ingredient sales.
  - NO invented perfumery / olfactive brief / technical fragrance-development
    claims.
  - Per standing rule, NO "no sponsorship needed" claim — her UAE residence visa
    is employer-sponsored. States "already based in Dubai" only.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-18/.
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

COMPANY = "dsm-firmenich"
TITLE = "Account Manager Fine Fragrance Experience"
DATE_FOLDER = "2026-08-18"

# Search is managed directly at dsm-firmenich; no hiring manager named in the
# posting, so the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Account Manager Fine Fragrance Experience — dsm-firmenich, Dubai, UAE. Presencial,
full-time. Managed directly at dsm-firmenich (no agencies).

Leverage your passion for fragrances and strategic sales skills to drive growth and
client satisfaction. Your creativity and business acumen will ensure strong
partnerships and valued clients.

Key Responsibilities:
- Lead client relationships across key fine fragrance accounts in the Middle East,
  ensuring strong partnerships, customer satisfaction, and sustainable business growth.
- Drive sales performance by identifying new opportunities, developing tailored
  fragrance proposals, and achieving annual revenue and margin targets.
- Develop an in-depth knowledge of company offerings, pricing, and policies, and
  improve existing sales proposals.
- Forecast, monitor, and analyze sales performance to ensure alignment with business
  objectives and accurate pipeline management.
- Provide insight into product development and competitive positioning.
- Manage the end-to-end project cycle.
- Develop and implement distribution channels.

You bring:
- Bachelor's degree or equivalent (Business Management or Administration, Finance,
  Marketing or related field).
- Minimum 3-5 years of industry experience or related fields in international
  environment.
- Proven experience in Sales and Distribution business.
- Good team player, that can work well in a collaborative environment, with passion
  for the fragrance industry.
- Effective communication skills and able to develop strong relationships.
- Excellent analytical, problem-solving and project management skills.
- Fluent in English.

About dsm-firmenich: innovators in nutrition, health and beauty; a house of master
perfumers and flavorists with 150+ years of R&D, competing with Givaudan, IFF and
Symrise in flavors and fragrances. Apply via the career portal.
"""

ATS = [
    "Account Manager", "Fine Fragrance", "fragrance", "fragrance industry",
    "client relationships", "key accounts", "Middle East", "partnerships",
    "customer satisfaction", "business growth", "sustainable growth",
    "sales performance", "drive sales", "new opportunities",
    "tailored fragrance proposals", "sales proposals", "revenue targets",
    "margin targets", "product knowledge", "pricing", "policies",
    "forecast", "monitor", "analyze", "pipeline management", "sales pipeline",
    "product development", "competitive positioning", "end-to-end project cycle",
    "project management", "distribution channels", "distribution",
    "Sales and Distribution", "international environment", "analytical",
    "problem-solving", "relationship building", "communication",
    "Business Administration", "Marketing", "fluent English", "GCC", "MENA",
    "UAE", "Dubai", "beauty",
]

CV_CONTENT = {
    "headline": (
        "Key Account Manager · Fine Fragrance & Beauty · Sales & Distribution · "
        "Client Relationships · Forecasting & Pipeline"
    ),
    "professional_summary": (
        "Commercial and key account professional with 4+ years driving sales, client relationships and "
        "category growth across Beauty, Fragrances, FMCG and E-Commerce — with genuine fine-fragrance depth. "
        "At Alibaba's Miravia I owned 42 key accounts (+30% GMV growth QoQ) and led the Fragrances category "
        "as PIC, onboarding the official distributors of the leading Arabian & oud houses (Arabian Oud, "
        "Lattafa, Swiss Arabian, Ajmal) — building real fluency in the Middle East fine-fragrance market. "
        "Today at DoFreeze I drive sales and develop distribution channels across 50+ markets, owning "
        "distributor networks, tailored commercial proposals, sales forecasting and pipeline management. "
        "Strong in relationship building, competitive positioning and end-to-end project management. Business "
        "Administration graduate, fluent English, already based in Dubai — with a real passion for fragrance."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Drive sales and develop distribution channels across 50+ markets (GCC, MENA, Asia, Europe, USA, Africa) — building and managing distributor networks, identifying new opportunities and developing tailored commercial proposals to hit revenue and margin targets",
                "Own sales forecasting, performance monitoring and pipeline management — analysing results against business objectives and adjusting plans to keep the pipeline accurate and on-track",
                "Lead the end-to-end project cycle for 6 NPD launches (brief, packaging, pricing, go-to-market), coordinating cross-functional teams from concept through in-market execution",
                "Develop in-depth knowledge of the product range, pricing and commercial policies to sharpen sales proposals and competitive positioning by market",
                "Manage modern-trade and UAE quick-commerce distribution (Noon, Talabat, Careem, Deliveroo) — onboarding, listings, promotional mechanics and retail execution",
                "Turn market, consumer and competitor analysis into product-development and positioning insight that feeds the portfolio and go-to-market",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Led the Fragrances category as PIC — onboarding 30+ accounts in two months, including the official distributors of the leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — building deep fluency in the Middle East fine-fragrance market and its brands",
                "Owned 42 key accounts across beauty, fragrances and fashion, achieving +30% GMV growth QoQ through tailored proposals, pricing strategy, assortment optimisation and targeted promotions",
                "Led end-to-end client relationships — building strong, long-term partnerships and ensuring customer satisfaction and sustainable business growth across the account portfolio",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO and executing commercial plans aligned to revenue and margin targets",
                "Forecasted and analysed sales, ROI, conversion and retention to sharpen pipeline accuracy and channel performance",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic XL key accounts, growing revenue through data-led joint planning and bespoke commercial activations",
                "Negotiated and closed high-impact commercial deals, maximising profitability and margin for both platform and partners",
                "Helped build Glovo's Retail vertical — developing new distribution and onboarding fashion and lifestyle partners onto the marketplace",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, feeding sales forecasting and commercial planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf — early grounding in end-to-end project management",
                "Built management-ready analyses in advanced Excel, translating category and market data into actionable commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "key account management, client relationship management, sales & distribution, distribution-channel "
        "development, tailored commercial proposals, pricing strategy, negotiation, revenue & margin targets, "
        "new business development, account & category management, distributor management"
    ),
    "skills_data": (
        "sales forecasting & monitoring, pipeline management, competitive positioning analysis, market analysis, "
        "P&L management, ROI/ROAS, sell-in/sell-out, KPI tracking, forecast accuracy, Power BI, Salesforce"
    ),
    "skills_brand": (
        "fine fragrance & beauty category, product & portfolio knowledge, NPD end-to-end, go-to-market, "
        "end-to-end project management, product-development insight, trade & shopper marketing, "
        "A&P budget management"
    ),
    "skills_ecommerce": (
        "distribution across modern trade + UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), e-commerce & "
        "marketplace account management, Shopify, listings & promo mechanics, omnichannel execution, "
        "conversion rate optimisation (CRO)"
    ),
    "skills_tools": (
        "Salesforce, SAP, Microsoft Excel (Advanced), PowerPoint (Advanced), Power BI, "
        "Generative AI (Claude, ChatGPT), Tableau, Kantar, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "A house of master perfumers competing at the level of Givaudan, IFF and Symrise is exactly where I "
        "want to build the next chapter of my commercial career — and the Account Manager Fine Fragrance role "
        "caught my eye because fine fragrance is where I already have my sharpest edge. At Alibaba's Miravia I "
        "led the Fragrances category as PIC, personally onboarding the official distributors of the leading "
        "Arabian & oud houses — Arabian Oud, Lattafa, Swiss Arabian and Ajmal — so I know this market, its "
        "brands and its buyers, and I bring a genuine passion for fragrance to it."
    ),
    "body_paragraph_1": (
        "Key account management is the spine of my career, and it maps directly onto what this role asks. At "
        "Miravia I owned 42 key accounts and grew GMV +30% QoQ through tailored proposals, pricing strategy and "
        "targeted promotions, owning client relationships end-to-end and reporting channel performance against "
        "revenue and margin targets to the CEO. Today, as Brand & Marketing Manager at DoFreeze, I drive sales "
        "and develop distribution channels across 50+ markets — building distributor networks, developing "
        "commercial proposals, and owning sales forecasting and pipeline management — while leading the "
        "end-to-end project cycle on new-product launches from brief to in-market execution."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, real fine-fragrance market fluency in the Middle East — the accounts, "
        "the Arabian & oud houses and the commercial dynamics — combined with a true passion for the category. "
        "Second, I am already based in Dubai and immediately available. I'll be candid that my fragrance work "
        "has been on the brand, retail and distribution side rather than selling fragrance creations from a "
        "creative house — but I already own the account management, sales, distribution-channel and forecasting "
        "craft this role runs on, I know the market and its clients, and I ramp fast. I hold a Business "
        "Administration degree and am fluent in English."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of key account ownership, fine-fragrance market fluency and "
        "data-led sales discipline to dsm-firmenich's fine fragrance business in the Middle East. I am "
        "available to start immediately and would welcome the chance to discuss how I would approach growing "
        "and deepening your key fine fragrance accounts across the region. Thank you for your consideration — I "
        "look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="dsm-firmenich-am-fine-fragrance-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.dsm-firmenich.com/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Account Manager Fine Fragrance Experience",
             "function": "Sales", "workplace": "On-site",
             "note": "Managed directly at dsm-firmenich; apply via career portal"},
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
            "Fine-fragrance category leadership (Miravia PIC — Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "Middle East fine-fragrance market fluency (brands, distributors, buyers)",
            "Key Account Management (42 accounts, +30% GMV QoQ)",
            "Client-relationship ownership end-to-end",
            "Sales & Distribution / distribution-channel development (DoFreeze, 50+ markets)",
            "Sales forecasting, monitoring & pipeline management",
            "Tailored commercial proposals, pricing & margin targets",
            "End-to-end project cycle (6 NPD launches)",
            "Product / competitive-positioning insight",
            "International environment (50+ countries)",
            "Bachelor's in Business Administration; fluent English",
            "Passion for the fragrance industry (genuine — specialised in it)",
            "Already based in Dubai",
        ],
        "missing_skills": [
            "B2B fragrance-creation/ingredient sales from a creative house (her fragrance experience is brand/retail/distribution-side — adjacent, not identical)",
            "Technical perfumery / olfactive brief development with perfumers (not held)",
        ],
        "sector_fit": "strong (Beauty & Fragrances — direct category match; her sharpest specialisation)",
        "seniority_fit": "on-band (4+ yrs vs 3-5 asked)",
        "red_flags": [
            "Role sits in a fragrance creative house (B2B fragrance-creation sales); Paula's fragrance tenure is brand/retail/distribution-side — positioned truthfully as adjacent",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit and one of Paula's best-aligned openings on the category axis. This is an "
            "Account Manager role for fine fragrance in the Middle East asking for key account management, "
            "client-relationship ownership, sales & distribution + channel development, tailored commercial "
            "proposals, sales forecasting/pipeline management, end-to-end project management and a genuine "
            "passion for fragrance — all of which are Paula's explicit track. Her standout hook is having led "
            "the Fragrances category as PIC at Alibaba's Miravia, onboarding the leading Arabian & oud houses "
            "(Arabian Oud, Lattafa, Swiss Arabian, Ajmal), which gives real Middle East fine-fragrance market "
            "fluency; plus 42 key accounts +30% GMV QoQ, distributor/channel development at DoFreeze across "
            "50+ markets, and Business Administration + fluent English. Tenure is on-band (4+ vs 3-5). Honest "
            "gap: the role sits inside a fragrance creative house (B2B fragrance-creation sales) whereas "
            "Paula's fragrance experience is on the brand/retail/distribution side — positioned truthfully as "
            "adjacent, with no invented ingredient-sales or perfumery claims."
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
