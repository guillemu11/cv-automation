"""One-off: generate Paula's CV + Cover Letter for the Deliveroo
"Account Manager" (Restaurants, Dubai) role.

This is a restaurant-partner-facing Account Management role: manage a portfolio of
Deliveroo's most important restaurants (high-volume drivers, global brands), act as
a data-driven "restaurant consultant" who grows partners' (and Deliveroo's)
profitability, and work cross-functionally with Marketing and Operations. Asks for
3–5 years, someone very data-conversant who can "use data to tell a story", strong
organisational + team-player qualities, and a passion for growing relationships.
Restaurant-industry knowledge and Arabic are pluses (not required).

Paula's fit is exceptionally direct — arguably one of her cleanest:
- She was literally an **Account Manager – XL Accounts at Glovo**, a quick-commerce
  FOOD-DELIVERY platform, managing strategic restaurant chains (KFC, Taco Bell, La
  Tagliatella, Sushi Shop) — the exact shape of this role.
- As **Key Account Manager at Alibaba's Miravia** she ran a 42-account portfolio to
  +30% GMV QoQ, reporting Flash Sales to the CEO — proof she manages high-value
  portfolios and tells growth stories with data.
- At **DoFreeze** she integrates brands into Deliveroo (and Noon/talabat/Careem)
  today and works cross-functionally with Marketing and Operations.
- Her Mondelez trainee stint was pure sell-in/sell-out data analysis — the "use
  data to tell a story" muscle.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. Arabic is NOT claimed. Fills the real CV and
cover-letter templates, converts to PDF with LibreOffice soffice (docx2pdf/Word is
unreliable headless on this Mac), and lands the package under
output/2026-08-16/Deliveroo - Account Manager/.
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

COMPANY = "Deliveroo"
TITLE = "Mid Market Account Manager"
DATE_FOLDER = "2026-08-16"
CONTACT = None  # no named contact yet → "Hiring Manager"

JOB_DESCRIPTION = """\
Account Manager — Deliveroo, Dubai, UAE.

As Deliveroo grows, it becomes a major revenue channel for restaurants — and the
Account Management team are the restaurant consultants who use data-driven insight
and industry knowledge to help partner restaurants grow. Account Managers oversee
restaurant relationships and provide strategic value to Deliveroo's partners.

What you will do:
- Manage a portfolio of Deliveroo's most important restaurants, including
  high-sales-volume drivers and global restaurant brands.
- Oversee relationships with important restaurant industry partners.
- Analyse data to achieve growth and profitability, both for your partners and for
  Deliveroo.
- Work cross-functionally with other departments (Marketing, Operations) to drive
  new projects.

What skills you'll need:
- Minimum of 3–5 years of experience in a relevant industry.
- Very data conversant with an ability to utilise data to tell a story.
- Great organisational skills with excellent team-player qualities.
- Passionate about people and growing relationships.
- Enjoy working in a constantly evolving environment.
- Strong knowledge of the restaurant industry is a plus.
- Fluency in English and Arabic is a plus.
"""

ATS = [
    "account management", "key account management", "account manager",
    "portfolio management", "restaurant partners", "restaurant industry",
    "global restaurant brands", "high-volume accounts", "relationship management",
    "restaurant consultant", "strategic partnerships", "partner growth",
    "growth and profitability", "profitability", "P&L", "revenue growth",
    "data-driven", "data conversant", "data storytelling", "use data to tell a story",
    "analytics", "insights", "reporting", "KPI tracking", "forecasting",
    "sell-in/sell-out", "ROI", "ROAS", "GMV", "commercial", "negotiation",
    "quick-commerce", "food delivery", "q-commerce", "marketplace",
    "Deliveroo", "Glovo", "Noon", "talabat", "Careem",
    "cross-functional", "Marketing", "Operations", "stakeholder management",
    "promotions", "campaign activation", "upsell", "retention",
    "constantly evolving environment", "team player", "organisational skills",
    "GCC", "UAE", "Dubai", "English",
]

CONTENT = {
    "headline": (
        "Account & Key Account Management · Quick-Commerce & Food Delivery · "
        "Data-Driven Partner Growth · Dubai / UAE"
    ),
    "professional_summary": (
        "Commercial and account management professional with 4+ years growing high-value partner "
        "portfolios on quick-commerce and food-delivery platforms in the GCC and Europe. I started as an "
        "Account Manager at Glovo, managing strategic restaurant chains (KFC, Taco Bell, La Tagliatella, Sushi "
        "Shop) on a food-delivery marketplace, then ran a 42-account portfolio at Alibaba's Miravia to +30% GMV "
        "QoQ. Today at DoFreeze I integrate brands into Deliveroo, Noon, talabat and Careem and partner daily with "
        "Marketing and Operations. I am very data-conversant — I turn sell-in/sell-out, ROI and conversion data "
        "into growth stories partners act on — organised, relationship-driven, and energised by fast-moving "
        "environments. Already in Dubai on a UAE residence visa; bilingual Spanish/English."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Manage brand growth on the UAE's food-delivery and quick-commerce platforms — Deliveroo, Noon, talabat and Careem — owning listings, promotional mechanics and retail execution to drive orders, conversion and sell-out",
                "Act as the commercial bridge to platform and modern-trade partners, negotiating promotions and joint activations that grow volume and profitability for both sides",
                "Work cross-functionally with Marketing and Operations to launch new projects end-to-end — campaigns, activations and go-to-market across 50+ GCC/MENA and international markets",
                "Own the A&P budget and track partner and channel performance (ROI, ROAS, conversion, sell-out) against targets, using an AI (Claude/GPT) reporting system that cuts manual reporting ~40% and speeds decisions",
                "Manage distributor and key-account relationships across channels, building the trust and cadence that keep partners engaged in a constantly evolving market",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed a portfolio of 42 key accounts, achieving +30% GMV growth QoQ through data-led pricing, assortment and promotional strategy — consulting partners on how to grow, not just servicing them",
                "Owned the Flash Sales channel and reported performance directly to the CEO, translating traffic, conversion, retention and ROI data into clear growth stories and commercial plans",
                "Onboarded 30+ new partner accounts in two months as category lead, using data and trend insight to prioritise the highest-potential relationships",
                "Analysed account and channel performance continuously to sharpen forecasting accuracy and defend profitability across the portfolio",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce & food-delivery leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed a portfolio of strategic restaurant key accounts on a food-delivery platform — KFC, Taco Bell, La Tagliatella, Sushi Shop — the exact restaurant-partner remit this role covers",
                "Acted as a data-driven consultant to partners, using order, performance and marketing data to build bespoke activations and growth plans that lifted order volume, GMV and profitability",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both Glovo and its restaurant partners",
                "Worked cross-functionally with marketing, logistics/operations and customer support to deliver seamless campaigns, while helping build out Glovo's new Retail vertical",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out analysis and promotional-effectiveness reports for the chocolate category — the foundation of using data to tell a commercial story",
                "Identified growth opportunities and contributed to NPD launches (Milka Spread, Mini Suchard), turning category data into action",
            ],
        },
    ],
    "skills_brand": (
        "partner & campaign activation, promotions & joint marketing, go-to-market, "
        "trade & shopper marketing, brand growth, influencer & creator marketing, sampling & seeding"
    ),
    "skills_ecommerce": (
        "quick-commerce & food delivery (Deliveroo, Glovo, Noon, talabat, Careem), marketplaces "
        "(Miravia, AliExpress), listings & promotional mechanics, retail execution, Meta & Google Ads, "
        "CRM & retention, Shopify e-store, marketing automation, generative-AI reporting"
    ),
    "skills_commercial": (
        "account management, key account management, portfolio management, restaurant & retail partner "
        "management, relationship building, negotiation, commercial deal-making, upsell & retention, "
        "distributor management, cross-functional stakeholder management (Marketing, Operations)"
    ),
    "skills_data": (
        "data storytelling, P&L & profitability, KPI tracking & reporting, sell-in/sell-out, "
        "ROI, ROAS, GMV, conversion & retention analysis, forecasting, AI-assisted analysis, "
        "Power BI, Tableau, Looker, Salesforce, Nielsen, Kantar"
    ),
    "skills_tools": (
        "Salesforce, Power BI, Tableau, Looker, Generative AI (Claude / ChatGPT), "
        "Meta Ads Manager, Google Ads, Shopify, SAP, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Deliveroo describes its Account Managers as restaurant consultants — people who use data and industry "
        "know-how to help partners grow, not just support them. That is exactly the job I did at Glovo, where I "
        "managed a portfolio of strategic restaurant chains on a food-delivery platform, and it is the work I love "
        "most. As a commercial marketer already based in Dubai who integrates brands into Deliveroo every week, I "
        "would be thrilled to bring that experience to your most important restaurant partners."
    ),
    "body_paragraph_1": (
        "At Glovo I managed key accounts such as KFC, Taco Bell, La Tagliatella and Sushi Shop — using order and "
        "performance data to build bespoke activations and growth plans that lifted volume, GMV and profitability "
        "for both the partner and the platform. I then ran a 42-account portfolio at Alibaba's Miravia to +30% GMV "
        "QoQ, reporting the Flash Sales channel directly to the CEO and turning traffic, conversion and retention "
        "data into clear growth stories partners acted on. Today at DoFreeze I manage brand growth across "
        "Deliveroo, Noon, talabat and Careem and partner daily with Marketing and Operations to launch new "
        "projects — so I know the quick-commerce mechanics behind this role from the inside."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, food-delivery and quick-commerce account management is genuinely my "
        "background — I don't need to learn the model, I have grown restaurant and brand portfolios on these "
        "platforms for years and I read the data fluently (sell-in/sell-out, ROI, conversion, profitability). "
        "Second, I am already in Dubai on a UAE residence visa, GCC-fluent and bilingual Spanish/English, so there "
        "is no relocation and no ramp-up. I am organised, genuinely energised by fast-moving environments, and I "
        "build the kind of partner relationships that last."
    ),
    "closing_paragraph": (
        "I would love to help Deliveroo's top restaurant partners grow — and grow Deliveroo with them. I am "
        "available to start immediately and would welcome the chance to talk through how I would approach the "
        "portfolio. Thank you for your consideration; I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="deliveroo-mid-market-account-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://jobs.ashbyhq.com/deliveroo/52214163-31dd-4629-b6b2-771836be15e1",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Mid Market Account Manager Deliveroo Dubai restaurants", "via": "LinkedIn / Ashby", "department": "Commercial UAE"},
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
        "ai_score": 93,
        "ai_tier": "Hot",
        "skills_match": [
            "Direct match: was an Account Manager at Glovo (food-delivery platform) managing restaurant chains — KFC, Taco Bell, La Tagliatella, Sushi Shop",
            "42-account portfolio at Miravia to +30% GMV QoQ — proven high-value portfolio management",
            "Very data-conversant: sell-in/sell-out (Mondelez), ROI/ROAS/conversion, reported to CEO — 'uses data to tell a story'",
            "Integrates brands into Deliveroo/Noon/talabat/Careem today (DoFreeze) — knows the platform from inside",
            "Cross-functional with Marketing and Operations (DoFreeze, Glovo)",
            "Growth & profitability focus for partners and platform (Glovo, Miravia)",
            "4+ yrs experience — squarely in the 3–5 band",
            "Already in Dubai on UAE residence visa; relationship-driven; thrives in fast-moving environments",
        ],
        "missing_skills": [
            "Arabic (a plus, not required — Paula is native Spanish, professional English C1)",
            "Restaurant-industry depth is on the F&B/food-delivery side (Glovo, DoFreeze) rather than restaurant operations",
        ],
        "sector_fit": "excellent (food delivery / quick-commerce account management — Glovo is the same model as Deliveroo)",
        "seniority_fit": "on-band (3–5 yrs asked; Paula 4+) — clean fit, no stretch",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "One of Paula's cleanest, most on-the-nose fits. The role is restaurant-partner account management on a "
            "food-delivery platform, and Paula was literally an Account Manager at Glovo doing exactly that — "
            "managing strategic restaurant chains (KFC, Taco Bell, La Tagliatella, Sushi Shop) with data-led growth "
            "plans. She then ran a 42-account portfolio at Alibaba's Miravia to +30% GMV QoQ (portfolio management + "
            "data storytelling, reporting to the CEO), and today integrates brands into Deliveroo itself plus Noon/"
            "talabat/Careem while partnering with Marketing and Operations. She is 4+ yrs (asked 3–5), very "
            "data-conversant (sell-in/sell-out at Mondelez, ROI/ROAS/conversion throughout), relationship-driven and "
            "already in Dubai on a residence visa. Only non-blocking gaps: Arabic (a plus) and depth in restaurant "
            "operations specifically vs. food-delivery/FMCG partner management."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX → PDF with LibreOffice headless (docx2pdf/Word fails on this Mac)."""
    subprocess.run(
        [
            "soffice", "--headless", "--convert-to", "pdf",
            "--outdir", str(docx_path.parent), str(docx_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    pdf_path = docx_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError(f"soffice did not produce {pdf_path}")
    return pdf_path


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

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
