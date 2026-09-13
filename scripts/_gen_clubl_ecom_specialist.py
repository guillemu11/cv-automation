"""One-off: generate Paula's CV for the Club L London "E-commerce Specialist"
(Dubai HQ) role.

This is one of the strongest *honest* fits in the pipeline: a fashion D2C
e-commerce trading role in Dubai asking to own the commercial performance and
day-to-day trading of the GCC (+ Australia) digital business across D2C and
wholesale, run weekly trading plans / launches / promotions, optimise onsite
merchandising, search, navigation and conversion, deliver a localised GCC
customer experience, grow wholesale e-commerce partners, and produce trading
reports with actionable insights on revenue, conversion, AOV and gross margin.

Almost all of which Paula genuinely has:
- Owns DoFreeze's D2C Shopify store end-to-end (catalogue, UX, collections,
  discounts, checkout), lifting CRO and AOV via data-led merchandising — and
  Shopify is one of the exact platforms the JD names.
- Ran the Beauty, Fragrances & *Fashion* category at Alibaba's Miravia
  marketplace (42 accounts, +30% GMV QoQ) with weekly promotions, trading and
  conversion/traffic/retention analytics — a direct online-trading analogue,
  and includes managing brand/wholesale partners selling on the platform.
- Localises content, campaigns and promotions across 50+ GCC/MENA/global
  markets — the JD's "localise the GCC customer experience" pillar.
- Deep, genuine *fashion* pedigree, which the JD explicitly prefers: Inditex /
  Massimo Dutti retail floor, Miravia Fashion KAM, Glovo's fashion Retail
  vertical, and a CUNEF thesis with a Fashion Industry specialisation.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented Arabic fluency (JD lists it only as "preferably"; logged
honestly as a gap), NO invented Salesforce Commerce Cloud / Magento platform
ownership (she owns Shopify, which the JD also names), NO invented fashion titles.

Fills the real CV template, converts to PDF via LibreOffice, registers the job
for the dashboard, and lands the package under output/2026-08-16/.
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
from career_ops.generators import cv_generator as cv

COMPANY = "Club L London"
TITLE = "E-commerce Specialist"
DATE_FOLDER = "2026-08-16"

JOB_DESCRIPTION = """\
E-commerce Specialist — Club L London, Dubai Office (HQ). E-Commerce, Full-time.

Club L London is a next-generation online fashion retailer specialising in
accessible luxury womenswear (occasion, prom, maternity, bridal and beyond),
with fresh collections dropping weekly for a global community of trend-setting
consumers, influencers and content creators.

The Role: Own the commercial performance and day-to-day execution of the GCC &
Australia digital business across both D2C and wholesale channels. Drive online
sales, deliver a best-in-class localised customer experience, and execute the
regional trading strategy across English/Arabic storefronts and wholesale
partners.

Key Responsibilities:
- Own the day-to-day trading of the GCC D2C website.
- Manage the complete onsite customer journey across English and Arabic websites.
- Develop and execute weekly trading plans, product launches, promotions and campaigns.
- Optimise onsite merchandising, navigation, search and conversion to maximise commercial performance.
- Own the localisation of the GCC customer experience, ensuring all content,
  campaigns, promotions and communications are relevant, culturally appropriate
  and optimised for GCC audiences.
- Champion the Arabic customer experience with high-quality localisation.
- Support and grow GCC wholesale e-commerce partners, ensuring strong commercial
  performance and consistent brand presentation.
- Monitor trading performance and identify opportunities to improve revenue,
  conversion, AOV and profitability.
- Ensure all website content, pricing, promotions and product information are accurate and up to date.
- Conduct regular website QA and resolve issues quickly with internal teams.
- Collaborate with Marketing, CRM, Buying, Operations and Technology teams to
  deliver seamless campaigns, launches and customer experiences.
- Produce regular trading reports with actionable insights and recommendations.

KPIs: Revenue, Conversion Rate, AOV, Gross Margin, Website Conversion, Trading &
Merchandising Accuracy, Localisation & Arabic Site Quality, Wholesale Partner
Performance, Campaign Execution.

Skills & Experience:
- 3-5 years' experience in e-commerce, digital trading or online merchandising.
- Strong understanding of D2C e-commerce, digital trading and onsite optimisation.
- Experience managing e-commerce platforms such as Shopify, Salesforce Commerce Cloud or Magento.
- Strong commercial acumen with the ability to analyse performance data and translate insights into actions.
- Experience localising digital experiences and content for regional markets.
- Preferably fluent in Arabic and English (written and spoken).
- Excellent organisational skills with strong attention to detail.
- Experience within fashion, luxury or retail is preferred.
"""

ATS = [
    "E-commerce Specialist", "e-commerce", "digital trading", "online merchandising",
    "D2C", "DTC", "direct-to-consumer", "day-to-day trading", "trading strategy",
    "weekly trading plans", "product launches", "promotions", "campaigns",
    "onsite merchandising", "navigation", "search", "conversion", "conversion rate",
    "conversion rate optimisation", "CRO", "AOV", "average order value",
    "gross margin", "profitability", "revenue", "commercial performance",
    "commercial acumen", "onsite optimisation", "customer journey", "UX",
    "customer experience", "localisation", "localise", "GCC", "MENA",
    "regional markets", "culturally appropriate", "Arabic storefront",
    "wholesale", "wholesale e-commerce", "wholesale partners", "brand presentation",
    "Shopify", "website QA", "pricing", "product information", "content",
    "trading reports", "actionable insights", "performance data", "KPIs",
    "ROI", "ROAS", "GMV", "fashion", "luxury", "retail", "accessible luxury",
    "influencers", "content creators", "campaign execution", "cross-functional",
    "Marketing", "CRM", "Buying", "Operations", "Technology",
]

CONTENT = {
    "headline": "E-Commerce & Digital Trading Specialist · Fashion & D2C · GCC · Onsite Merchandising, CRO & AOV · Trading Plans & Wholesale Partners",
    "professional_summary": (
        "E-commerce and digital trading professional with 4+ years across fashion, beauty and marketplace "
        "commerce, scoped exactly like this role: owning day-to-day D2C trading, weekly trading plans, launches "
        "and promotions, onsite merchandising and conversion, and the commercial performance of a regional "
        "(GCC) digital business across D2C and wholesale. Currently own DoFreeze's D2C Shopify store end-to-end "
        "(catalogue, UX, collections, search, discounts, checkout) — one of the exact platforms named in this "
        "role — lifting conversion (CRO) and average order value through data-led merchandising, and localising "
        "content, campaigns and promotions across 50+ GCC/MENA/global markets. Previously ran the Beauty, "
        "Fragrances & Fashion category at Alibaba's Miravia marketplace (42 accounts / brand & wholesale "
        "partners, +30% GMV QoQ), steering weekly promotions, conversion, traffic and retention. Genuine "
        "fashion pedigree — Inditex (Massimo Dutti), Miravia Fashion and Glovo's fashion Retail vertical, with "
        "a CUNEF thesis specialised in the Fashion Industry. Already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (E-Commerce & Digital Trading)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the D2C Shopify store end-to-end — catalogue, onsite merchandising, navigation, search, collections, promotions, discounts and checkout — running the day-to-day trading and lifting conversion (CRO) and average order value (AOV) through data-led merchandising (Shopify is one of the exact platforms named in this role)",
                "Build and execute weekly and seasonal trading plans — product launches, promotions and campaigns — steering the digital business against commercial KPIs (revenue, conversion, AOV, gross margin) and the A&P budget",
                "Own localisation of the customer experience across 50+ GCC/MENA/global markets, ensuring content, campaigns, promotions and communications are relevant, culturally appropriate and optimised per market",
                "Support and grow wholesale, distributor and marketplace partners across GCC modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo) — onboarding, product content, pricing, promotional mechanics and consistent brand presentation",
                "Run website QA and keep content, pricing, promotions and product information accurate and up to date, resolving issues quickly with cross-functional Marketing, CRM, Buying, Operations and Technology teams",
                "Produce trading reports with actionable insights — turning conversion, traffic and sell-out data into recommendations — supported by an AI-powered (Claude/GPT) analytics and content system that cut manual reporting ~40% and sped go-to-market",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Owned the online commercial performance of the Beauty, Fragrances & Fashion category across 42 accounts, growing GMV +30% QoQ through assortment, pricing, weekly promotions and best-in-class digital trading",
                "Ran the trading calendar for the Flash Sales channel (Beauty, Fashion & Home) reporting to the CEO, executing weekly and seasonal plans aligned with revenue and profitability targets",
                "Supported and grew brand & wholesale partners selling on the platform — onboarding 30+ houses in two months as PIC Fragrances via trend-driven assortment and promotions, with consistent brand presentation",
                "Drove onsite discovery and conversion through platform search, promotions and the Beauty Club and Hot on Social programmes — lifting visibility, loyalty and repeat purchase",
                "Continuously analysed conversion, traffic, AOV, retention, ROI and ROAS, translating performance data into trading actions and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts (Retail / Fashion vertical)",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical, onboarding fashion and lifestyle brands to the platform and growing GMV through data-led planning and bespoke digital activations",
                "Managed strategic key & wholesale accounts, coordinating launches, product content and promotional activity across marketing, operations and logistics",
                "Negotiated high-impact commercial deals maximising profitability for platform and partners",
            ],
        },
        {
            "company": "Massimo Dutti (Inditex) · earlier: Mondelez Trainee",
            "role": "Fashion Retail (Inditex) & FMCG Category Planning",
            "dates": "2018 – 2022",
            "location": "Madrid, Spain",
            "context": "Inditex premium fashion retail + Mondelez global FMCG (€36B)",
            "bullets": [
                "Inditex / Massimo Dutti: hands-on premium fashion retail — visual merchandising standards, product flow, styling and customer experience — the operational fluency in fashion this role prefers",
                "Mondelez: category deep dives (sell-in/sell-out, promo effectiveness, Nielsen reporting) turning data into actionable commercial recommendations, and NPD launches from concept to shelf",
            ],
        },
    ],
    "skills_brand": "Digital trading & day-to-day trading, weekly & seasonal trading plans, product launches, promotions & campaign execution, onsite merchandising, content & brand presentation, localisation for regional markets, influencer & UGC activation, go-to-market",
    "skills_ecommerce": "D2C / DTC e-commerce, Shopify e-store (end-to-end), onsite optimisation (navigation, search, merchandising), conversion rate optimisation (CRO), AOV growth, UX & customer journey, website QA, wholesale / marketplace e-commerce, quick-commerce (Noon, Talabat, Careem, Deliveroo), Meta Ads, Google Ads",
    "skills_commercial": "Commercial performance & acumen, revenue / AOV / gross margin & profitability, pricing strategy, assortment & merchandising planning, key account & wholesale partner management, negotiation, forecasting, category management",
    "skills_data": "Trading & performance reporting, actionable insights, conversion / traffic / retention analysis, KPI monitoring, ROI, ROAS, GMV, data-driven decisions, AI-assisted analysis, Power BI, Tableau, Looker, Salesforce",
    "skills_tools": "Shopify, Meta Ads Manager, Google Ads, Salesforce, Power BI, Tableau, Looker, Generative AI (Claude, ChatGPT), Microsoft Excel (Advanced), PowerPoint (Advanced), Canva, Microsoft Office (Expert)",
}


def make_job() -> Job:
    return Job(
        id="clubl-london-ecom-specialist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://career.clubllondon.com/jobs",
        source="career_site",
        description=JOB_DESCRIPTION,
        raw={"query": "E-commerce Specialist Club L London",
             "brand": "Club L London",
             "division": "E-Commerce — Fashion (accessible luxury womenswear), GCC & Australia"},
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
        "ai_score": 87,
        "ai_tier": "Hot",
        "skills_match": [
            "D2C e-commerce ownership (Shopify end-to-end — a platform the JD names)",
            "Day-to-day digital trading, weekly trading plans, launches & promotions",
            "Onsite merchandising, search, navigation & conversion (CRO, AOV)",
            "Commercial performance & KPIs (revenue, conversion, AOV, gross margin)",
            "Localisation of content/campaigns across GCC/MENA regional markets",
            "Wholesale / marketplace / distributor partner management",
            "Genuine fashion pedigree (Inditex/Massimo Dutti, Miravia Fashion, Glovo fashion vertical, CUNEF fashion thesis)",
            "Trading reports with actionable insights",
            "Cross-functional (Marketing, CRM, Buying, Operations, Technology)",
            "Already in Dubai (UAE residence visa, no sponsorship)",
        ],
        "missing_skills": [
            "Arabic language (JD lists it as 'preferably' — Paula is ES native / EN C1; she localises for GCC but does not write Arabic)",
            "Native Arabic-storefront editorial ownership (adjacent multi-market localisation, not Arabic copywriting)",
            "Salesforce Commerce Cloud / Magento platform tenure (owns Shopify, which the JD also lists as acceptable)",
        ],
        "sector_fit": "very strong (fashion D2C e-commerce; genuine fashion + marketplace pedigree)",
        "seniority_fit": "strong (4+ yrs e-commerce/trading; 'Specialist' / 3-5 yrs fits her range well)",
        "red_flags": [
            "Arabic fluency preferred and Arabic-site quality is a KPI — Paula localises across GCC/MENA but is not an Arabic speaker",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "One of the strongest honest fits in the pipeline. The Club L London E-commerce Specialist is a "
            "fashion D2C digital-trading role (own day-to-day GCC D2C trading + wholesale, weekly trading plans / "
            "launches / promotions, onsite merchandising / search / navigation / conversion, localised GCC "
            "customer experience, grow wholesale e-commerce partners, trading reports on revenue/conversion/AOV/"
            "gross margin) — nearly all of which Paula genuinely has. She owns the DoFreeze D2C Shopify store "
            "end-to-end (Shopify is one of the exact platforms the JD names), runs weekly trading and promotions, "
            "lifts CRO/AOV via merchandising, localises content/campaigns across 50+ GCC/MENA markets, and manages "
            "wholesale/marketplace partners; she ran the Beauty, Fragrances & Fashion category at Alibaba's Miravia "
            "(42 accounts, +30% GMV QoQ) with weekly promotions and conversion/traffic/retention analytics. Crucially "
            "the JD *prefers* fashion/luxury/retail and Paula has real fashion depth (Inditex/Massimo Dutti, Miravia "
            "Fashion KAM, Glovo fashion Retail vertical, CUNEF Fashion-Industry thesis). Genuine gap: Arabic — but "
            "here it is only 'preferably' (softer than a hard must). Positioned truthfully; no invented Arabic, "
            "SFCC/Magento or fashion titles."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (docx2pdf/Word is unreliable here)."""
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

    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
