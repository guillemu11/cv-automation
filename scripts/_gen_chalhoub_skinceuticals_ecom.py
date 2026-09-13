"""One-off: generate Paula's CV for the Chalhoub Group / SkinCeuticals
"Ecommerce Specialist" (Middle East) role.

This is a strong, honest fit: a pure D2C e-commerce ownership role in Beauty
(SkinCeuticals, medical-aesthetic skincare under Chalhoub Group) asking for D2C
e-commerce strategy, e-Commerce P&L management, an e-business animation plan
(search / paid media / CRM), a premium online shopping experience, 1st-party
data & CRM, media planning & KPIs, and data-driven CLV growth — almost all of
which Paula genuinely has: she owns the DoFreeze D2C Shopify store end-to-end
(catalogue, UX, content, CRO, AOV), plans and optimises paid media (Meta,
Google), runs CRM/EDM and loyalty, and led the Beauty & Fragrances category at
Alibaba's Miravia (42 accounts, +30% GMV QoQ) with conversion/traffic/retention
and ROI/ROAS analytics.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented skincare/medical-aesthetic titles, NO invented Arabic,
NO invented standalone CRM-platform ownership. It is re-angled to the JD's
pillars (D2C P&L, animation plan, premium UX, 1st-party data/CRM, media & KPIs).
Genuine gaps (Arabic — the JD lists it as a must — and skincare-specific brand
tenure) are simply not over-claimed and are logged honestly in the dashboard.

Fills the real CV template, converts to PDF, registers the job for the dashboard,
and lands the package under output/2026-08-16/.
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

COMPANY = "Chalhoub Group"
TITLE = "Ecommerce Specialist - SkinCeuticals"
DATE_FOLDER = "2026-08-16"

JOB_DESCRIPTION = """\
Ecommerce Specialist - SkinCeuticals — Chalhoub Group, Middle East (Dubai, UAE).

As the Ecommerce Specialist for SkinCeuticals in the Middle East, you will take
full ownership of the D2C business, working in a highly collaborative role,
partnering closely with brand, media and zone teams.

Key responsibilities:
Develop and execute the D2C strategy, managing the P&L to ensure profitable
growth and setting ambitious goals for the Middle East market.
Create and lead a dynamic e-business animation plan, driving traffic through
search, paid media and CRM to fuel sales and expand the customer base.
Ensure a premium, seamless online shopping experience by implementing unique
content, services and functionalities that reflect SkinCeuticals' medical-aesthetic
positioning.
Analyze D2C data and consumer insights to make data-driven decisions, identifying
opportunities to increase customer lifetime value.

We are looking for a strategic and data-driven individual with strong D2C
e-commerce experience, ideally in the beauty sector; a natural collaborator with
a clear vision for creating exceptional online consumer experiences.
A relevant degree and proven experience building and executing e-commerce / D2C
strategies. Fluency in English; Arabic is a must. e-Commerce Management: proven
ability to manage an e-commerce P&L and drive business performance. Data-Driven
Business & P&L Steering: strong analytical skills to monitor KPIs, derive insights
and steer business decisions. Audience Strategy & 1st Party Data Management:
expertise in CRM and using first-party data to acquire and retain customers.
Digital technology expertise and trend knowledge. Media planning & KPIs. CRM
strategy and execution.
"""

ATS = [
    "Ecommerce Specialist", "e-Commerce Management", "D2C", "DTC", "direct-to-consumer",
    "e-commerce strategy", "e-commerce P&L", "P&L steering", "profitable growth",
    "e-business animation plan", "trading calendar", "traffic", "search", "paid media",
    "media planning", "CRM", "CRM strategy and execution", "first-party data",
    "1st party data", "audience strategy", "customer acquisition", "retention",
    "customer lifetime value", "CLV", "premium online experience", "online shopping experience",
    "content", "merchandising", "conversion rate optimisation", "CRO", "AOV",
    "consumer insights", "data-driven decisions", "KPIs", "ROI", "ROAS", "GMV",
    "Beauty", "skincare", "Shopify", "Meta Ads", "Google Ads", "EDM", "loyalty",
    "digital technology", "trend knowledge", "GCC", "MENA", "Middle East",
]

CONTENT = {
    "headline": "E-Commerce & D2C Manager · Beauty & FMCG · P&L Ownership · Paid Media, CRM & 1st-Party Data · Data-Driven Growth",
    "professional_summary": (
        "Data-driven e-commerce and D2C professional with 4+ years across Beauty, FMCG and marketplace commerce, "
        "scoped exactly like this role: full ownership of a direct-to-consumer business — strategy, P&L and profitable "
        "growth — with a trading/animation calendar that drives traffic through search, paid media and CRM. Currently "
        "own DoFreeze's D2C Shopify store end-to-end (catalogue, UX, content, merchandising, checkout), lifting "
        "conversion (CRO) and average order value, while planning and optimising Meta and Google paid media against "
        "ROI/ROAS. Previously owned the Beauty & Fragrances category at Alibaba's Miravia (42 accounts, +30% GMV QoQ), "
        "steering conversion, traffic, retention and loyalty. Fluent in commercial KPIs, first-party data and CRM/EDM "
        "to acquire, retain and grow customer lifetime value. Business Administration graduate (CUNEF, 9.5/10 thesis, "
        "E-Commerce specialisation), already based in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (E-Commerce & D2C)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the brand's D2C Shopify store end-to-end — strategy, catalogue, UX, content, collections, discounts and checkout — delivering a premium, seamless online shopping experience and steering it against commercial KPIs and A&P budget",
                "Build and run the e-business animation plan (always-on trading calendar), driving traffic through search, paid media and CRM/EDM to fuel sales and expand the customer base",
                "Plan and optimise paid media on Meta (Facebook & Instagram) and Google Ads — audience building, first-party audiences, creative A/B testing — analysing ROI and ROAS to steer spend toward profitable growth",
                "Lift conversion rate (CRO) and average order value through data-led merchandising, content and consumer insight, and use CRM, EDM and loyalty/sampling to improve retention and customer lifetime value",
                "Turn D2C data and consumer insights into data-driven decisions, reporting KPIs and building an AI-powered (Claude/GPT) analytics and content system that cut manual workload ~40% and sped go-to-market across 50+ markets",
                "Integrate the D2C business with UAE quick-commerce and modern trade (Noon, Talabat, Careem, Deliveroo), partnering with brand, media and channel teams on omnichannel visibility and execution",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned the Beauty & Fragrances online business across 42 accounts, growing GMV +30% QoQ through assortment, pricing, promotions and best-in-class digital activation — a premium, content- and discovery-led beauty category adjacent to skincare",
                "Ran the commercial P&L for the Flash Sales channel (Beauty, Fashion & Home) reporting to the CEO, executing trading plans aligned with profitability targets",
                "Drove traffic and conversion through on-platform search, promotions and the Beauty Club and Hot on Social programmes — lifting brand visibility, consumer loyalty and repeat purchase (customer lifetime value)",
                "Led category expansion as PIC Fragrances, onboarding 30+ beauty & fragrance houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) in two months via trend-driven assortment",
                "Continuously analysed conversion, traffic, retention, ROI and ROAS to steer performance, forecasting accuracy and data-driven decisions",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts and helped build Glovo's Retail vertical, growing GMV through data-led planning and bespoke digital marketing activations",
                "Led cross-functional squads across marketing, media, logistics and CX to ship campaigns and grow order volume",
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
                "Ran category deep dives — sell-in/sell-out, promotional effectiveness and Nielsen-based performance reporting — surfacing growth opportunities and corrective actions",
                "Built management-ready analyses in advanced Excel and PowerPoint, translating data into actionable commercial recommendations",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": "D2C strategy & ownership, e-business animation / trading calendar, premium online experience design, content & merchandising, loyalty & sampling, influencer marketing, go-to-market, brand activation, A&P budget management",
    "skills_ecommerce": "e-Commerce & D2C management, Shopify e-store (end-to-end), conversion rate optimisation (CRO), AOV growth, media planning & paid media (Meta Ads, Google Ads), search / traffic acquisition, CRM & EDM, quick-commerce (Noon, Talabat, Careem, Deliveroo), marketing automation, UX optimisation",
    "skills_commercial": "e-commerce P&L management, P&L steering, profitable growth, pricing strategy, assortment planning, category management, key account management, negotiation, forecasting",
    "skills_data": "KPI monitoring & business steering, first-party / 1st-party data, audience strategy, customer acquisition & retention, customer lifetime value (CLV), consumer insight, conversion / traffic / cohort analysis, ROI, ROAS, GMV, AI-assisted analysis, Power BI, Tableau, Salesforce",
    "skills_tools": "Shopify, Meta Ads Manager, Google Ads, Salesforce (CRM), Power BI, Tableau, Looker, Generative AI (Claude, ChatGPT), Microsoft Excel (Advanced), PowerPoint (Advanced), Canva, Microsoft Office (Expert)",
}


def make_job() -> Job:
    return Job(
        id="chalhoub-skinceuticals-ecom-specialist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.chalhoubgroup.com/en/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Ecommerce Specialist SkinCeuticals", "brand": "SkinCeuticals",
             "division": "Chalhoub Group — Beauty / L'Oréal Dermatological Beauty"},
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
            "D2C / e-commerce ownership (Shopify end-to-end)",
            "e-commerce P&L & KPI steering",
            "e-business animation plan (search / paid media / CRM)",
            "Media planning & paid media (Meta, Google) with ROAS",
            "Premium online shopping experience (CRO, AOV, content)",
            "Beauty sector depth (Miravia Beauty & Fragrances, +30% GMV QoQ)",
            "First-party data, CRM/EDM, loyalty & retention (CLV)",
            "Data-driven decisions (conversion / traffic / retention analytics)",
            "Already in Dubai (residence visa, no sponsorship)",
        ],
        "missing_skills": [
            "Arabic language (JD lists Arabic as a MUST — Paula is ES native / EN C1)",
            "Skincare / medical-aesthetic-specific brand tenure (has adjacent beauty & fragrance + FMCG)",
            "Standalone enterprise CRM-platform ownership (has CRM/EDM + Salesforce exposure, not a dedicated CRM-lead role)",
        ],
        "sector_fit": "strong (Beauty D2C e-commerce; skincare-adjacent)",
        "seniority_fit": "strong (4+ yrs of D2C/e-commerce + beauty; Specialist level fits, arguably a step below her range)",
        "red_flags": [
            "Arabic listed as a must-have — genuine gap",
            "Medical-aesthetic skincare positioning is specific; Paula's beauty depth is fragrance/beauty + FMCG",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit. The SkinCeuticals Ecommerce Specialist is a pure D2C e-commerce ownership role "
            "(D2C strategy + P&L, e-business animation plan across search/paid media/CRM, premium online experience, "
            "first-party data & CRM, media planning & KPIs, CLV growth) — nearly all of which Paula genuinely has: she "
            "owns the DoFreeze D2C Shopify store end-to-end (catalogue, UX, content, CRO, AOV), plans and optimises "
            "Meta/Google paid media against ROAS, runs CRM/EDM and loyalty, and owned the Beauty & Fragrances online "
            "category at Alibaba's Miravia (42 accounts, +30% GMV QoQ) with conversion/traffic/retention analytics. "
            "Genuine gaps: Arabic (JD says it is a must; Paula is ES native / EN C1) and skincare/medical-aesthetic-"
            "specific brand tenure (she has adjacent beauty/fragrance + FMCG). Positioned truthfully as a Beauty/FMCG "
            "D2C e-commerce owner; no invented skincare, Arabic or CRM-platform claims."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (no Word automation prompts).

    Falls back to cv._to_pdf (docx2pdf/Word) if soffice is unavailable or fails.
    Removes the intermediate DOCX on success, mirroring cv._to_pdf.
    """
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
