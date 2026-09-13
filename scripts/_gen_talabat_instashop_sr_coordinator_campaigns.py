"""One-off: generate Paula's CV for the talabat (instashop)
"Sr. Coordinator Campaigns - instashop" (Dubai) role.

talabat is the leading on-demand delivery platform in MENA and part of the
Delivery Hero family; instashop is its online local marketplace (UAE + Egypt).
This role sits inside the campaigns team and is execution/coordination-heavy:
support planning, implementation and tracking of promotional activations with
retail partners; leverage existing partner discounts/promotions into campaigns;
ensure accurate in-app visualization of deals (swimlanes, classifications,
category icons, banner spaces); regularly audit live campaigns for accuracy;
coordinate creative, CRM, performance and digital marketing teams for seamless
cross-channel execution; track performance, prepare reports and maintain the
campaign calendar. Also upsell campaign features to smaller partners with the
Account Management team.

Qualifications: Bachelor's (Business/Marketing); 2+ years in campaign management
/ marketing; data-driven; Excel & PowerPoint; understanding of SEO, PPC, social
and email marketing; analytics tools.

Paula's fit is very strong and she is comfortably ABOVE the 2+ year floor (4+
years). The standout is that she runs quick-commerce promotional mechanics
hands-on TODAY — she integrates brands into talabat itself (plus Noon, Careem,
Deliveroo) at DoFreeze, owning listings, promotions, deals/discounts and retail
execution: exactly the in-app promotional visualization + campaign auditing this
role coordinates. At Miravia she owned the Flash Sales channel and ran 42 partner
accounts' promotions; at Glovo she ran key-account activations on a q-commerce
marketplace. Cross-functional coordination (creative, CRM, performance, digital)
and reporting in Excel/dashboards map to the JD line by line.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. Fills the real CV template, converts to PDF
via LibreOffice soffice headless (docx2pdf/Word fails silently on this Mac), and
lands the package under output/2026-08-25/talabat - Sr. Coordinator Campaigns - instashop/.
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

COMPANY = "talabat"
TITLE = "Sr. Coordinator Campaigns - instashop"
DATE_FOLDER = "2026-08-25"

JOB_DESCRIPTION = """\
Sr. Coordinator Campaigns — instashop (talabat / Delivery Hero family), Dubai, UAE.

instashop, headquartered in Dubai, is the leading online local marketplace in the
UAE and Egypt, part of the Delivery Hero family (global leader in q-commerce).

As a Sr. Coordinator Campaigns you support the execution of campaigns in
collaboration with partners — assisting in planning, implementation and tracking of
promotional activations to enhance engagement and performance.

Responsibilities:
- Develop and implement innovative campaign strategies in partnership with key
  retail partners.
- Identify opportunities for upselling campaign features to smaller partners and
  work with the Account Management team to execute them.
- Collaborate with partner shops to identify existing discounts and promotions that
  can be leveraged for campaigns.
- Ensure accurate visualization of deals, discounts and promotions in the app —
  swimlanes, classifications, category icons and banner spaces.
- Regularly audit live campaigns to ensure accuracy in discounts, promotions and
  messaging.
- Collaborate with creative, CRM, performance and digital marketing teams to ensure
  seamless execution and consistency across channels, aligned with business objectives.
- Track campaign performance, prepare reports and provide updates to senior team members.
- Assist in analyzing results to refine short-term and long-term campaign goals.
- Maintain a schedule of ongoing and upcoming campaigns.
- Work with internal departments to ensure smooth and effective campaign delivery.

Qualifications:
- Bachelor's degree in Business, Marketing or a related field.
- Minimum 2+ years of experience in campaign management, marketing or similar roles.
- Basic analytical skills and a data-driven approach to support campaign performance.
- Proficiency in Excel and PowerPoint for organizing and presenting campaign data.
- Strong understanding of SEO, PPC, social media and email marketing strategies.
- Knowledge of analytics tools.
"""

ATS = [
    "campaign management", "campaign coordination", "campaign strategy",
    "promotional activations", "promotions", "deals", "discounts",
    "campaign execution", "campaign planning", "campaign tracking",
    "retail partners", "partner shops", "key accounts", "account management",
    "upselling", "co-marketing", "partnerships",
    "in-app merchandising", "swimlanes", "banners", "category icons",
    "app visualization", "merchandising", "campaign audit", "quality assurance",
    "cross-functional", "creative", "CRM", "performance marketing", "digital marketing",
    "email marketing", "EDM", "social media", "SEO", "PPC", "paid media",
    "Meta Ads", "Google Ads", "reporting", "performance reporting", "dashboards",
    "data-driven", "analytics", "KPI tracking", "ROI", "ROAS", "conversion",
    "Excel", "PowerPoint", "campaign calendar", "scheduling",
    "quick-commerce", "q-commerce", "marketplace", "Noon", "talabat", "Careem",
    "Deliveroo", "Delivery Hero", "instashop", "FMCG", "trade marketing",
    "shopper marketing", "GCC", "UAE", "modern trade", "sell-out",
]

CONTENT = {
    "headline": (
        "Campaign Management & Promotions · Q-Commerce & Marketplaces · "
        "Retail Partnerships & Trade Marketing · GCC / UAE"
    ),
    "professional_summary": (
        "Campaign and commercial marketer with 4+ years across FMCG, marketplaces and quick-commerce in the GCC, "
        "who plans, executes and tracks promotional activations with retail partners end-to-end. Currently lead "
        "Brand & Marketing at DoFreeze in Dubai, where I run promotions on the UAE's q-commerce platforms — talabat, "
        "Noon, Careem and Deliveroo — owning deals, discounts, in-app merchandising (banners, placements, category "
        "visibility), campaign auditing and cross-functional delivery with creative, CRM, performance and digital "
        "teams. Data-driven and hands-on in Excel, PowerPoint and reporting dashboards, tracking ROI, ROAS and "
        "conversion to refine campaign goals. Marketplace-native — I owned Flash Sales and 42 partner accounts at "
        "Miravia and ran key-account activations at Glovo. Already in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Plan, execute and track promotional campaigns and activations with retail and modern-trade partners end-to-end — from strategy and mechanics to go-live and post-campaign analysis — to enhance engagement and sell-out",
                "Run quick-commerce promotions hands-on across the UAE's platforms — talabat, Noon, Careem and Deliveroo — owning deals, discounts and promotional mechanics, plus in-app visibility (banners, placements, category merchandising) to accurately surface offers to shoppers",
                "Audit live campaigns for accuracy of discounts, promotions and messaging, fixing listing, pricing and merchandising errors before and during activation to protect the customer experience",
                "Leverage existing partner discounts and promotions into joint campaigns, working with distributors and retail partners to design high-yield activations and upsell added campaign features",
                "Coordinate creative, CRM/EDM, performance and digital marketing teams for seamless, on-brand execution across channels — translating each campaign into in-app, push, social and email briefs aligned to business objectives",
                "Track performance and prepare reports in Excel and dashboards (ROI, ROAS, conversion), and maintain the campaign calendar of ongoing and upcoming activations — using an AI (Claude/GPT) reporting system that cuts manual workload ~40%",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace & consumer app | 100K+ employees",
            "bullets": [
                "Owned the Flash Sales channel for Beauty, Fashion & Home on a top-5 marketplace — planning promotional calendars, deals and discounts and ensuring accurate in-app placement (banners, swimlanes, category visibility) to maximise conversion",
                "Managed campaigns and promotions across 42 partner accounts — joint activations, pricing and assortment plays — driving +30% GMV growth QoQ and reporting the channel directly to the CEO",
                "Onboarded 30+ partners in two months as category lead, coordinating promotions and campaign features to accelerate discovery, conversion and repeat purchase",
                "Tracked campaign performance (conversion, traffic, retention, ROI) in reporting tools to refine short- and long-term goals and improve forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce marketplace | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Ran promotional campaigns and marketing activations with strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) on a q-commerce marketplace — the same online-local-marketplace model instashop runs",
                "Coordinated cross-functional teams across marketing, logistics and CX to deliver campaigns end-to-end, driving order volume, conversion and GMV",
                "Negotiated and closed high-impact commercial deals and campaign features, maximising profitability for platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness analysis for the chocolate category in Excel — turning campaign and trade data into clear, data-driven recommendations",
                "Prepared performance reports and presentations for the category team, grounding in FMCG trade marketing and promo evaluation",
            ],
        },
    ],
    "skills_brand": (
        "campaign management & coordination, promotional activations, promo mechanics (deals & discounts), "
        "integrated 360 campaigns (strategy → execution), retail & FMCG partnerships / co-marketing, "
        "trade & shopper marketing, in-app merchandising & placement, activations & launches, "
        "influencer & creator marketing, go-to-market"
    ),
    "skills_ecommerce": (
        "quick-commerce / q-commerce (talabat, Noon, Careem, Deliveroo), marketplaces & consumer apps "
        "(Miravia, Glovo), in-app visualization (banners, swimlanes, category icons), SEO, PPC, "
        "Meta Ads (Facebook & Instagram), Google Ads, social media, CRM & email marketing (EDM), "
        "push / in-app messaging, Shopify e-store, marketing automation"
    ),
    "skills_commercial": (
        "key account & partner management, upselling campaign features, account management collaboration, "
        "cross-functional coordination (creative, CRM, performance, digital), campaign calendar & scheduling, "
        "negotiation, category management, modern trade, distributor management"
    ),
    "skills_data": (
        "campaign performance tracking & reporting, live-campaign auditing / QA, KPI dashboards, "
        "ROI, ROAS, conversion, sell-in / sell-out analysis, data-driven insight, "
        "AI-assisted analysis & forecasting, Looker, Power BI, Nielsen, Kantar, Salesforce"
    ),
    "skills_tools": (
        "Excel (Expert), PowerPoint, Microsoft Office (Expert), Meta Ads Manager, Google Ads, "
        "Generative AI (Claude / ChatGPT), Shopify, Canva, Salesforce, Power BI, Tableau, Looker"
    ),
}


def make_job() -> Job:
    return Job(
        id="talabat-instashop-sr-coordinator-campaigns-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.talabat.com/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Sr. Coordinator Campaigns instashop talabat Delivery Hero", "via": "LinkedIn"},
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
        "ai_score": 88,
        "ai_tier": "Hot",
        "skills_match": [
            "4+ yrs — comfortably above the 2+ year floor",
            "Runs q-commerce promotions on talabat itself today (plus Noon/Careem/Deliveroo) — exact in-app promo/merchandising fit",
            "instashop is Delivery Hero family; talabat is Paula's live q-commerce channel — strong narrative hook",
            "Owned Flash Sales channel + 42 partner accounts' promotions at Miravia (in-app placement, banners, discounts)",
            "Live-campaign auditing / QA of discounts, promotions and messaging (DoFreeze)",
            "Cross-functional coordination: creative, CRM/EDM, performance, digital",
            "Reporting in Excel/PowerPoint/dashboards; data-driven (ROI/ROAS/conversion)",
            "SEO/PPC/social/email marketing literacy via paid media + CRM ownership",
            "Already in Dubai on residence visa",
        ],
        "missing_skills": [
            "Role is a coordinator/execution level (2+ yrs) — Paula is slightly senior for it (position as strength, not stretch)",
            "Arabic (not required)",
        ],
        "sector_fit": "excellent (q-commerce marketplace · FMCG promotions · GCC — Delivery Hero / talabat family)",
        "seniority_fit": "above-band (2+ yrs asked; Paula 4+) — over-qualified but clean, coordinator remit she already owns",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Very strong fit: the JD wants 2+ yrs coordinating promotional campaigns with retail partners on the "
            "instashop marketplace — in-app deal/discount visualization (swimlanes, banners, category icons), live-"
            "campaign auditing, cross-functional execution (creative/CRM/performance/digital) and reporting. Paula "
            "does exactly this hands-on today at DoFreeze on talabat, Noon, Careem and Deliveroo, and owned Flash "
            "Sales + 42 partner accounts' promotions at Miravia. She is above the tenure floor (4+ vs 2+), so the "
            "only nuance is slight over-qualification, which we frame as depth rather than stretch."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX→PDF via LibreOffice headless (docx2pdf/Word fails silently on this Mac)."""
    soffice = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    subprocess.run(
        [soffice, "--headless", "--convert-to", "pdf", "--outdir",
         str(docx_path.parent), str(docx_path)],
        check=True, capture_output=True, text=True,
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
    cv_docx.unlink(missing_ok=True)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
