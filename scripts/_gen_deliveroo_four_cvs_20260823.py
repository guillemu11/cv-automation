"""One-off: generate Paula's CVs for FOUR live Deliveroo Dubai roles (2026-08-23).

The four roles Paula chose to apply to, all Dubai - Main Office, none restricted
to UAE Nationals:
  1. Marketing Manager, Brand              -> reuse _gen_deliveroo_brand_mm content
  2. Marketing Manager, Promotions & Incentives  -> new content (authored below)
  3. Mid Market Account Manager            -> reuse _gen_deliveroo_account_manager content
  4. Senior Catalogue Specialist           -> new content (authored below)

All content is authored directly from profile.yaml and kept strictly truthful —
NO invented experience, metrics or languages (Arabic is never claimed). Fills the
real CV template, converts DOCX -> PDF with LibreOffice headless (docx2pdf/Word is
unreliable on this Mac), and lands each CV under
output/2026-08-23/Deliveroo - <Role>/01_CV_y_Carta/.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))  # so we can import the sibling _gen_* modules

from career_ops.config import settings
from career_ops.discovery.normalize import Job

# Land everything under today's dated folder (generators write to settings.output_dir)
settings.output_dir = ROOT / "output" / "2026-08-23"
settings.output_dir.mkdir(parents=True, exist_ok=True)

from career_ops.generators import cv_generator as cv  # noqa: E402

import _gen_deliveroo_brand_mm as brand          # noqa: E402  (reuse CONTENT)
import _gen_deliveroo_account_manager as am       # noqa: E402  (reuse CONTENT)

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

CTX = {
    "DoFreeze": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
    "Miravia": "Top 5 global e-commerce marketplace | Alibaba Group | 100K+ employees",
    "Glovo": "Quick-commerce & food-delivery leader | €500M+ revenue | 10K+ employees",
    "Mondelez": "Global FMCG | €36B annual revenue | 90K+ employees",
}

# -------------------------------------------------------------------
# 2. Marketing Manager, Promotions & Incentives  (new content)
# JD: own ME promotional calendar, in-app & lifecycle campaigns by segment,
# quarterly/annual promo roadmaps vs commercial priorities, track campaign
# budgets/ROI/margin, structured tests for minimum effective discount,
# test-and-learn, business cases w/ financials, data -> senior stakeholders.
# 5-8 yrs Growth Mktg / Data Analytics / Segmentation / Promotions in a
# high-growth tech/marketplace/e-commerce platform; Excel/Sheets/Looker; A/B.
# -------------------------------------------------------------------
PROMO_CONTENT = {
    "headline": (
        "Promotions, Value & Pricing · Commercial Marketing · Test-and-Learn & ROI · "
        "Quick-Commerce · UAE / GCC"
    ),
    "professional_summary": (
        "Commercial marketer with 4+ years running promotions, pricing and value campaigns on "
        "quick-commerce, e-commerce and FMCG platforms across the GCC and Europe. At Alibaba's Miravia I "
        "owned the Flash Sales channel — the platform's core value/promotions engine — reporting to the CEO "
        "and growing 42 accounts +30% GMV QoQ through segment-led promotions and pricing. Today at DoFreeze I "
        "plan the promotional calendar across the UAE and 50+ markets on Deliveroo, talabat, Noon and Careem, "
        "owning A&P budgets and tracking ROI and margin, with an AI-built reporting system. I live in the data "
        "— test-and-learn, Looker/Sheets, conversion and margin analysis — and turn it into clear "
        "recommendations for leadership. Already in Dubai on a UAE residence visa; bilingual Spanish/English."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC", "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present", "location": "Dubai, UAE", "context": CTX["DoFreeze"],
            "bullets": [
                "Plan and run the promotional calendar across the UAE and 50+ GCC/MENA markets — translating quarterly commercial priorities into targeted promotions and in-app/quick-commerce activations on Deliveroo, talabat, Noon and Careem",
                "Own promotional mechanics and pricing across channels, building offers by channel/customer segment and timing them to cultural moments (Ramadan, Eid, National Days) to hit both volume and margin targets",
                "Own the A&P budget and track campaign-level ROI, ROAS and margin impact — flagging early when a promotion runs off plan — with an AI (Claude/GPT) system that automates reporting and cuts manual work ~40%",
                "Run test-and-learn on offers and creative (A/B testing on Meta and Google Ads) to find what genuinely drives conversion, feeding results back into the next promotional cycle",
                "Translate complex performance data into clear recommendations for leadership on where to scale, hold or cut promotional spend",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain", "context": CTX["Miravia"],
            "bullets": [
                "Owned the Flash Sales channel for Beauty, Fashion & Home — Miravia's core value and promotions engine — reporting performance directly to the CEO and executing promotional plans against P&L targets",
                "Grew 42 key accounts +30% GMV QoQ through pricing strategy, assortment and targeted, segment-led promotions",
                "Made structured pricing and promo decisions that protected margin while driving volume — nominating the SKUs and offers with the strongest return",
                "Analysed conversion, traffic, retention and ROI continuously to sharpen promotional effectiveness and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo", "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023", "location": "Madrid, Spain", "context": CTX["Glovo"],
            "bullets": [
                "Built bespoke, data-led promotional activations for strategic partners on a quick-commerce platform, lifting order volume and GMV",
                "Worked cross-functionally with marketing, operations and CX to launch and measure campaigns end-to-end",
                "Negotiated commercial deals balancing partner growth with platform profitability",
            ],
        },
        {
            "company": "Mondelez International", "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022", "location": "Madrid, Spain", "context": CTX["Mondelez"],
            "bullets": [
                "Evaluated promotional effectiveness and built sell-in/sell-out performance reports for the chocolate category — early grounding in the test-measure-learn discipline this role runs on",
                "Contributed to NPD launches (Milka Spread, Mini Suchard), turning category data into commercial action",
            ],
        },
    ],
    "skills_brand": (
        "promotional strategy & calendar, value & pricing promotions, in-app & lifecycle campaigns, "
        "customer segmentation, go-to-market, campaign management, cultural-moment activations (Ramadan / Eid)"
    ),
    "skills_ecommerce": (
        "quick-commerce & delivery (Deliveroo, talabat, Noon, Careem), in-app promotions, Meta & Google Ads, "
        "CRM / lifecycle & EDM, A/B testing, Shopify, marketing automation, generative-AI reporting"
    ),
    "skills_commercial": (
        "commercial strategy, pricing strategy, margin & P&L management, promotional ROI, "
        "key account management, cross-functional & senior-stakeholder management"
    ),
    "skills_data": (
        "test-and-learn / A/B testing, promotional ROI & margin analysis, Looker, Power BI, Tableau, "
        "Excel / Google Sheets, sell-in/sell-out, conversion & retention analysis, forecasting, AI-assisted analysis"
    ),
    "skills_tools": (
        "Looker, Power BI, Tableau, Excel / Google Sheets, Meta Ads Manager, Google Ads, "
        "Generative AI (Claude / ChatGPT), Salesforce, SAP, Microsoft Office (Expert)"
    ),
}

# -------------------------------------------------------------------
# 4. Senior Catalogue Specialist  (new content)
# JD: build/maintain high-quality product catalogue across partners; curate item
# names, categories, images, descriptions to brand standards; content clean-up,
# sprints, large-scale partner onboarding; create/update/manage SKUs via internal
# tools across grocery/retail; standardise names/categories/tags for
# discoverability; enrich pages w/ images & descriptions leveraging AI tools;
# collaborate w/ Category, Account Management, content, design. 1-2 yrs content
# ops/e-commerce/retail/data; Excel/Sheets large data sets; detail + process;
# English required, Arabic preferred.
# -------------------------------------------------------------------
CATALOGUE_CONTENT = {
    "headline": (
        "E-Commerce & Catalogue Specialist · Product Content & SKU Management · "
        "Quick-Commerce Merchandising · AI-Enriched"
    ),
    "professional_summary": (
        "E-commerce and content-operations specialist who builds and maintains conversion-ready product "
        "catalogues across marketplaces and quick-commerce platforms. At DoFreeze I own a Shopify store "
        "end-to-end — catalogue, categories, images, descriptions and collections — and manage brand listings "
        "(SKUs) on Deliveroo, Noon, talabat and Careem, enriching product pages with generative-AI tools. At "
        "Alibaba's Miravia I optimised assortment across 42 accounts and onboarded 30+ stores. I work fast and "
        "accurately in Excel/Google Sheets across large data sets, with sharp attention to detail and a "
        "structured, process-driven approach to content clean-up, standardisation and large-scale partner "
        "onboarding. Fluent English, native Spanish; already in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC", "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present", "location": "Dubai, UAE", "context": CTX["DoFreeze"],
            "bullets": [
                "Own a Shopify e-commerce catalogue end-to-end — creating and maintaining product listings, categories, tags, images and descriptions to brand standards, optimised for discoverability and conversion",
                "Create, update and manage brand SKUs across UAE quick-commerce and grocery/retail platforms — Deliveroo, Noon, talabat, Careem — keeping catalogues complete, accurate and conversion-ready",
                "Enrich product pages with high-quality images and compelling descriptions, leveraging generative-AI tools (Claude/GPT) and creative inputs to scale content quality",
                "Run content clean-up and standardisation across large catalogues — normalising item names, categories and tags for a consistent customer experience",
                "Collaborate with commercial, content and design teams to launch fully merchandised catalogues for key campaigns and promotions",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain", "context": CTX["Miravia"],
            "bullets": [
                "Optimised assortment and product content across a 42-account portfolio, standardising listings to improve discoverability and conversion",
                "Onboarded 30+ new stores in two months — large-scale partner and catalogue onboarding under tight timelines",
                "Managed SKUs, pricing and performance daily in large data sets (Excel / Google Sheets and BI tools) with a high accuracy bar",
                "Curated category and campaign pages, coordinating content and merchandising for promotional moments",
            ],
        },
        {
            "company": "Glovo", "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023", "location": "Madrid, Spain", "context": CTX["Glovo"],
            "bullets": [
                "Set up and merchandised partner catalogues/menus while helping build Glovo's retail vertical — onboarding new partners and their product ranges onto the platform",
                "Coordinated cross-functionally with content, marketing and operations to launch listings accurately and on time",
                "Maintained catalogue accuracy across a portfolio of high-volume partners in a fast-moving environment",
            ],
        },
        {
            "company": "Mondelez International", "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022", "location": "Madrid, Spain", "context": CTX["Mondelez"],
            "bullets": [
                "Built structured data reports and sell-in/sell-out analysis for the chocolate category — a detail-oriented, process-driven grounding in managing large data sets",
                "Contributed to NPD launches (Milka Spread, Mini Suchard), maintaining product and category data end-to-end",
            ],
        },
    ],
    "skills_brand": (
        "product merchandising, catalogue curation, content standardisation, campaign & promotion merchandising, "
        "brand-standard compliance, AI-enriched content"
    ),
    "skills_ecommerce": (
        "catalogue & SKU management, product listings, quick-commerce & grocery catalogues (Deliveroo, Noon, "
        "talabat, Careem), Shopify catalogue & collections, marketplace content (Miravia / AliExpress), "
        "image & description enrichment, generative-AI content tools, discoverability & tagging"
    ),
    "skills_commercial": (
        "large-scale partner onboarding, assortment & range management, category management, "
        "cross-functional coordination (Category, Account Management, Design)"
    ),
    "skills_data": (
        "large data-set management (Excel / Google Sheets), data accuracy & QA, SKU & performance tracking, "
        "BI tools (Looker, Power BI, Tableau), sell-in/sell-out, structured process & attention to detail"
    ),
    "skills_tools": (
        "Excel / Google Sheets (Expert), Shopify, Generative AI (Claude / ChatGPT), Looker, Power BI, "
        "Tableau, Salesforce, SAP, Canva, Microsoft Office (Expert)"
    ),
}


def make_job(title: str, url: str, description: str, department: str) -> Job:
    return Job(
        id=f"deliveroo-{title.lower().replace(',', '').replace(' ', '-')}-2026-08-23",
        title=title,
        company="Deliveroo",
        location="Dubai, United Arab Emirates",
        url=url,
        source="linkedin",
        description=description,
        raw={"via": "Deliveroo Careers", "department": department},
    )


ROLES = [
    ("Marketing Manager, Brand", brand.CONTENT,
     "https://careers.deliveroo.co.uk/role/marketing-manager-brand-69a7ec15cdb7/",
     brand.JOB_DESCRIPTION, "Marketing UAE"),
    ("Marketing Manager, Promotions and Incentives", PROMO_CONTENT,
     "https://careers.deliveroo.co.uk/role/marketing-manager-promotions-and-incentives-3ff893d2a9a3/",
     "Own the Middle East promotional calendar, in-app & lifecycle campaigns, ROI/margin, test-and-learn. 5-8 yrs growth marketing/promotions.",
     "Marketing UAE"),
    ("Mid Market Account Manager", am.CONTENT,
     "https://careers.deliveroo.co.uk/",
     am.JOB_DESCRIPTION, "Commercial UAE"),
    ("Senior Catalogue Specialist", CATALOGUE_CONTENT,
     "https://careers.deliveroo.co.uk/",
     "Build and maintain a high-quality product catalogue across partners; SKU/content ops; large-scale onboarding. 1-2 yrs content ops/e-commerce.",
     "New Verticals UAE"),
]


def to_pdf(docx: Path) -> Path:
    subprocess.run(
        [SOFFICE, "--headless",
         "-env:UserInstallation=file:///tmp/lo_deliveroo_4cvs_profile",
         "--convert-to", "pdf", "--outdir", str(docx.parent), str(docx)],
        check=True, capture_output=True, text=True,
    )
    pdf = docx.with_suffix(".pdf")
    if not pdf.exists():
        raise RuntimeError(f"LibreOffice did not produce {pdf}")
    return pdf


def main() -> None:
    for title, content, url, desc, dept in ROLES:
        job = make_job(title, url, desc, dept)
        docx = cv._fill_template(content, job)
        pdf = to_pdf(docx)
        print("OK_CV", title, "->", pdf)


if __name__ == "__main__":
    main()
