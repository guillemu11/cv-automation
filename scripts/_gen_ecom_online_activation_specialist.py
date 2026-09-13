"""One-off: generate Paula's CV for the "E-Commerce & Online Activation
Specialist (English & Arabic speaking)" role — Marketing, Dubai, Hybrid.

The role: drive online sales performance and flawless campaign activation across
e-commerce platforms and digital retail partners for an FMCG/beauty/personal-care
business. Own day-to-day e-commerce execution (online shelf: content, imagery, A+
content, SEO, pricing, availability, ratings & reviews), lead digital activation of
brand campaigns across e-commerce and retailer-media platforms, manage promotions/
launches/seasonal events, act as the primary e-commerce contact for distributors/
retailers/agencies, optimise product pages & brand stores for conversion, and turn
e-commerce KPIs (traffic, conversion, sell-out, share, ROI) into actionable insight.
Asks 2–3 years in e-commerce / digital activation, FMCG/beauty a strong advantage,
regional/multi-market exposure preferred.

Paula's fit is excellent and on-the-nose:
- At **DoFreeze** she owns day-to-day e-commerce execution across Noon, Talabat,
  Careem and Deliveroo (listings, content, pricing, availability, promo mechanics)
  AND runs the Shopify brand store end-to-end (PDP/CRO) — the exact "online shelf +
  activation" remit — while briefing agencies and coordinating 50+ markets.
- At **Alibaba's Miravia** she ran online-shelf execution across 42 beauty/fragrance/
  fashion accounts to +30% GMV QoQ, owned the Flash Sales channel (end-to-end
  promotions, launches, seasonal events; calendars reporting to the CEO) and, as PIC
  Fragrances, onboarded the official distributors of the leading Arabian & oud houses
  (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — deep GCC/Arabic beauty-market
  relevance and localisation.
- **Glovo** = quick-commerce activations & promotions; **Mondelez** = sell-in/
  sell-out data reporting — the "translate KPIs into insight" muscle.

Content is authored directly (no LLM API key needed) and kept strictly truthful —
NO invented experience. **Arabic is NOT claimed** (the JD requires it; Paula is
native Spanish / English C1). Her real Arabian/oud-market and Dubai-based experience
is surfaced honestly to address "local relevance" without overclaiming language.

Fills the real CV template, converts to PDF with LibreOffice soffice (docx2pdf/Word
is unreliable headless on this Mac), and lands the CV under
output/2026-08-16/FMCG Beauty Distributor (Dubai) - E-Commerce & Online Activation Specialist/.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "FMCG Beauty Distributor (Dubai)"  # placeholder — no company named in the posting
TITLE = "E-Commerce & Online Activation Specialist"
DATE_FOLDER = "2026-08-16"

JOB_DESCRIPTION = """\
E-Commerce & Online Activation Specialist (English & Arabic speaking) — Marketing,
Dubai, UAE (Hybrid).

Responsible for driving online sales performance, digital execution excellence and
flawless campaign activation across e-commerce platforms and digital retail
partners. Key link between brand and commercial teams so online touchpoints are
optimised, locally relevant and conversion-focused. Strong coordination with
distributors, retailers, agencies and internal stakeholders to execute always-on and
campaign-based activations that accelerate growth across priority markets.

E-Commerce Execution & Performance
- Own day-to-day execution of e-commerce activities across key online retailers and
  marketplaces.
- Ensure best-in-class online shelf execution (content, imagery, A+ content, SEO,
  pricing, availability, ratings & reviews).
- Track and analyse e-commerce KPIs (traffic, conversion, sell-out, share, ROI) and
  recommend optimisation actions.
- Support commercial teams with online forecasting, promotions and performance
  tracking.

Online Activation & Campaign Management
- Lead digital activation of brand campaigns across e-commerce and retailer-media
  platforms.
- Coordinate end-to-end execution of promotions, launches, seasonal events and
  always-on activations.
- Ensure timely, accurate rollout of assets, messaging and mechanics across markets
  and customers.
- Manage campaign calendars and alignment with brand, trade and media plans.

Stakeholder & Distributor Management
- Primary point of contact for e-commerce topics with distributors, retailers and
  local partners.
- Brief, coordinate and follow up with agencies on content creation, media
  activation and optimisation.
- Support cross-market alignment while ensuring local relevance and compliance.

Content & Consumer Experience
- Ensure brand consistency and high-quality consumer experience across all online
  touchpoints.
- Optimise product pages and brand stores to improve discoverability and conversion.
- Coordinate localisation of content where required (language, cultural relevance,
  regulatory needs).

Reporting & Insights
- Prepare regular performance reports and post-campaign evaluations.
- Translate data into actionable insights and recommendations.

Qualifications: Bachelor's in Business/Marketing/E-Commerce/Digital Marketing. 2–3
years in e-commerce, digital marketing or online activation. Hands-on with online
retailers, marketplaces or DTC. FMCG/beauty/personal care a strong advantage.
Regional/multi-market exposure preferred. Strong e-commerce fundamentals (online
shelf, conversion levers, retail media, promotions), analytics/reporting tools
(Excel, dashboards, retailer platforms, Google Analytics), project management.
Fluent English and Arabic required.
"""

ATS = [
    "e-commerce", "ecommerce", "online activation", "digital execution",
    "campaign activation", "online sales performance", "conversion",
    "online shelf", "content", "A+ content", "imagery", "SEO", "pricing",
    "availability", "ratings and reviews", "product pages", "PDP",
    "brand store", "discoverability", "conversion rate optimisation", "CRO",
    "online retailers", "marketplaces", "DTC", "retail media",
    "retailer media", "always-on", "seasonal events", "promotions", "launches",
    "campaign calendar", "go-to-market", "asset rollout",
    "distributor management", "retailer management", "agency management",
    "stakeholder management", "cross-functional", "cross-market", "local relevance",
    "localisation", "compliance",
    "e-commerce KPIs", "traffic", "conversion", "sell-out", "share", "ROI", "ROAS",
    "GMV", "forecasting", "performance tracking", "post-campaign evaluation",
    "reporting", "insights", "Google Analytics", "Excel", "dashboards",
    "retailer platforms", "analytics", "project management",
    "FMCG", "beauty", "personal care", "consumer goods", "fragrances",
    "Noon", "talabat", "Careem", "Deliveroo", "Shopify", "Amazon",
    "Miravia", "AliExpress", "GCC", "MENA", "UAE", "Dubai", "multi-market",
    "Meta Ads", "Google Ads", "English",
]

CONTENT = {
    "headline": (
        "E-Commerce Execution & Online Activation · Online Shelf, Retail Media & "
        "PDP / Conversion · Marketplaces & Quick-Commerce · FMCG & Beauty · Dubai / UAE"
    ),
    "professional_summary": (
        "E-commerce and online-activation specialist with 4+ years driving online sales performance and "
        "flawless campaign execution across marketplaces, quick-commerce and DTC in the GCC and Europe. "
        "Today at DoFreeze I own day-to-day e-commerce execution across Noon, talabat, Careem and Deliveroo "
        "— online shelf, listings, pricing, availability and promo mechanics — and run the brand's Shopify "
        "store end-to-end (PDP and conversion). Before that, at Alibaba's Miravia I ran online-shelf execution "
        "across 42 beauty and fragrance accounts to +30% GMV QoQ and owned the Flash Sales channel end-to-end "
        "(promotions, launches, seasonal events), including onboarding the official distributors of the leading "
        "Arabian & oud houses — so I know the GCC beauty market and its localisation needs first-hand. I brief "
        "agencies, coordinate distributors and retailers across 50+ markets, and turn e-commerce KPIs (traffic, "
        "conversion, sell-out, ROI) into optimisation actions. Already in Dubai on a UAE residence visa; "
        "bilingual Spanish/English."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (E-Commerce & Online Activation)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own day-to-day e-commerce execution across key online retailers, marketplaces and quick-commerce platforms — Noon, talabat, Careem and Deliveroo — managing online shelf (listings, content, imagery, pricing, availability, ratings & reviews) and promotional mechanics to drive traffic, conversion and sell-out",
                "Lead digital activation of brand campaigns across e-commerce and retailer-media platforms — coordinating end-to-end rollout of promotions, launches, seasonal events (incl. Ramadan) and always-on activations, and managing campaign calendars aligned to brand, trade and media plans",
                "Own and optimise the brand's Shopify e-store end-to-end (catalogue, product pages, collections, checkout), lifting discoverability, conversion (CRO) and average order value through data-led merchandising and UX",
                "Act as the primary e-commerce contact for distributors, retailers and local partners, and brief/follow up with agencies on content creation, media activation and optimisation — ensuring cross-market alignment, local relevance and compliance across 50+ GCC, MENA and international markets",
                "Track e-commerce KPIs (traffic, conversion, sell-out, share, ROI, ROAS) and produce post-campaign evaluations via an AI (Claude/GPT) reporting system that cuts manual reporting ~40% and turns data into optimisation actions",
                "Plan and optimise retail media and paid social (Meta & Google Ads) — audience building, creative A/B testing and ROAS analysis — to accelerate online sales across priority markets",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion (E-Commerce)",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Owned best-in-class online shelf execution across 42 beauty, fragrance and fashion accounts — content, imagery, pricing, assortment, availability and ratings & reviews — achieving +30% GMV growth QoQ",
                "Owned the Flash Sales channel end-to-end for Beauty, Fashion & Home — activating promotions, launches and seasonal events, managing the campaign calendar and reporting performance directly to the CEO",
                "Led category expansion as PIC Fragrances, onboarding 30+ stores in two months including the official distributors of the leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — deep GCC/Arabic beauty-market relevance and content localisation",
                "Continuously analysed traffic, conversion, retention, ROI and ROAS to optimise online performance and forecasting accuracy, translating data into clear optimisation recommendations",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce & food-delivery leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Executed data-led activations and promotions for strategic key accounts on a quick-commerce marketplace, growing order volume and GMV through bespoke online campaigns",
                "Worked cross-functionally with marketing, operations and customer support to deliver seamless campaign rollout, while helping build out Glovo's new Retail vertical (fashion, beauty, non-food)",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out analysis, promotional-effectiveness evaluations and performance reports for the chocolate category — turning data into actionable commercial insight",
                "Identified growth opportunities and supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_ecommerce": (
        "online shelf execution (content, A+ content, imagery, SEO, pricing, availability, ratings & reviews), "
        "product-page (PDP) & brand-store optimisation, conversion rate optimisation (CRO), marketplaces "
        "(Miravia, AliExpress), quick-commerce (Noon, talabat, Careem, Deliveroo), Shopify DTC, retail media, "
        "Meta Ads (Facebook & Instagram), Google Ads, Google Analytics, marketing automation"
    ),
    "skills_brand": (
        "online activation, always-on & campaign activation, promotions, launches & seasonal events, "
        "campaign calendar management, go-to-market, asset & content briefing, retail-media activation, "
        "content localisation, omnichannel campaigns"
    ),
    "skills_commercial": (
        "distributor management, retailer & marketplace management, agency management, "
        "cross-functional stakeholder management, cross-market coordination, key account management, "
        "negotiation, pricing strategy, assortment planning, online forecasting"
    ),
    "skills_data": (
        "e-commerce KPIs (traffic, conversion, sell-out, share), ROI, ROAS, GMV, Google Analytics, "
        "dashboards & retailer platforms, Excel, performance tracking & reporting, post-campaign evaluation, "
        "forecasting, sell-in/sell-out, AI-assisted analysis, Power BI, Tableau, Looker"
    ),
    "skills_tools": (
        "Google Analytics, Microsoft Excel (Expert), Shopify, Meta Ads Manager, Google Ads, "
        "Power BI, Tableau, Looker, Salesforce, SAP, Generative AI (Claude / ChatGPT), Canva"
    ),
}


def make_job() -> Job:
    return Job(
        id="ecom-online-activation-specialist-dubai-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, DU, AE (Hybrid)",
        url="",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"query": "E-Commerce & Online Activation Specialist Dubai FMCG beauty", "function": "Marketing", "work_arrangement": "Hybrid"},
    )


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

    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
