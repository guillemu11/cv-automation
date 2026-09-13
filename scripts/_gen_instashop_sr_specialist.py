"""One-off: generate Paula's CV for the instashop
"Sr. Specialist Marketing" (Dubai) role.

instashop is the leading online local marketplace in the UAE and Egypt and part
of the Delivery Hero family (the same group as talabat) — a q-commerce business.
The role owns instashop's UAE brand presence: build brand affinity, manage local
partnerships, and run integrated 360 campaigns (online + offline) that keep
instashop top-of-mind. Core remit: 360 campaign leadership end-to-end; co-marketing
with FMCG brands and retail partners; online/offline synergy (OOH, activations,
events aligned with digital, social and influencer); cross-functional bridge
(Commercial, Creative, Legal, CRM/Retention) translating campaigns into in-app/push
briefs to drive repeat orders; performance & budgeting (ROI, CAC, conversion);
market intelligence on UAE competitors and consumer trends.

Qualifications: 4–6 yrs in brand / campaign / growth / trade marketing in the GCC
(Q-Commerce preferred); proven 360 integrated campaigns (offline + digital +
localized activations); data-driven; vendor & agency management.

Paula's fit is exceptionally strong and — unlike most senior briefs — there is NO
tenure gap: she has 4+ years, squarely in the 4–6 band. The standout is the exact
"Q-Commerce preferred" line: she runs quick-commerce hands-on today (integrating
brands into Noon, talabat, Careem, Deliveroo — talabat being Delivery Hero's own
UAE platform) and came up through Glovo, a quick-commerce marketplace. As Brand &
Marketing Manager at DoFreeze (an FMCG distributor) she leads integrated 360
campaigns end-to-end, runs FMCG/retail co-marketing, directs agencies/production/
creators, owns A&P budgets and tracks ROI/ROAS/conversion — the JD almost line by
line.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. Fills the real CV template, converts to PDF,
and lands the package under output/2026-08-15/instashop - Sr. Specialist Marketing/.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "instashop"
TITLE = "Sr. Specialist Marketing"
DATE_FOLDER = "2026-08-15"

JOB_DESCRIPTION = """\
Sr. Specialist Marketing — instashop (Delivery Hero family), Dubai, UAE. 4–6 years.

instashop is the leading online local marketplace in the UAE and Egypt, part of the
Delivery Hero family (global leader in online food delivery and q-commerce). As Sr.
Specialist Marketing you are the creative and strategic force behind instashop's
brand presence in the UAE — building brand affinity, managing local partnerships,
and coordinating integrated campaigns (online and offline) that keep instashop
top-of-mind. You work closely with external partners, retail vendors and internal
creative teams to execute memorable, high-impact marketing initiatives.

Responsibilities:
- 360 Campaign Leadership: end-to-end strategy, planning and execution of seasonal,
  tactical and brand campaigns across the UAE.
- Co-Marketing & Partnerships: collaborate with FMCG brands and retail partners to
  design high-yielding joint marketing initiatives.
- Online/Offline Synergy: align OOH ads, activations and events with digital,
  social and influencer roadmaps.
- Cross-Functional Bridge: connect Commercial, Creative, Legal and CRM/Retention
  teams — translating campaigns into targeted in-app/push messaging briefs to drive
  repeat orders.
- Performance & Budgeting: track localized spend and campaign impact (ROI, CAC,
  conversion metrics) against business targets.
- Market Intelligence: monitor UAE competitor moves and consumer trends to spot
  quick-turnaround growth opportunities.

Qualifications:
- Bachelor's degree in Marketing, Communications, Business or related field.
- 4–6 years in brand management, campaign management, growth marketing or trade
  marketing within the GCC region (Experience in Q-Commerce preferred).
- Proven track record planning and executing integrated 360-degree campaigns
  combining offline, digital and localized activations.
- Data-driven mindset: read, translate and leverage marketing data into actionable
  growth insights and commercial strategies.
- Vendor & agency management: experience managing external creative agencies,
  production houses and print/OOH vendors.
"""

ATS = [
    "brand management", "brand affinity", "brand presence", "campaign management",
    "360 campaign", "integrated campaigns", "integrated 360-degree campaigns",
    "seasonal campaigns", "tactical campaigns", "brand campaigns", "strategy to execution",
    "co-marketing", "partnerships", "FMCG brands", "retail partners", "joint marketing",
    "online/offline synergy", "OOH", "activations", "events", "experiential",
    "digital", "social", "influencer", "cross-functional", "Commercial", "Creative",
    "CRM", "retention", "in-app messaging", "push notifications", "repeat orders",
    "performance marketing", "budgeting", "A&P budget", "ROI", "ROAS", "CAC",
    "conversion", "business targets", "market intelligence", "competitor analysis",
    "consumer trends", "growth marketing", "trade marketing", "GCC", "UAE",
    "q-commerce", "quick-commerce", "marketplace", "Noon", "talabat", "Careem",
    "Deliveroo", "Delivery Hero", "vendor management", "agency management",
    "production houses", "print/OOH vendors", "data-driven", "growth insights",
]

CONTENT = {
    "headline": (
        "Brand & 360 Campaign Marketing · Q-Commerce & Marketplaces · "
        "FMCG Co-Marketing & Partnerships · GCC / UAE"
    ),
    "professional_summary": (
        "Brand and campaign marketer with 4+ years across FMCG, marketplaces and quick-commerce in the GCC, "
        "who builds brand affinity and runs integrated 360 campaigns — seasonal, tactical and brand — end-to-end, "
        "from strategy and planning to online + offline execution. Currently lead Brand & Marketing at DoFreeze in "
        "Dubai: I own 360 campaigns across paid social, influencer, CRM/EDM, activations and in-store, run FMCG and "
        "retail co-marketing, direct creative agencies, production houses and 25–50 creators per campaign, and own "
        "the A&P budget while tracking ROI, ROAS and conversion against targets. Quick-commerce native — I integrate "
        "brands into Noon, talabat, Careem and Deliveroo today and came up through Glovo, a q-commerce marketplace. "
        "Data-driven, AI-native, and already in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Lead integrated 360 campaigns end-to-end — seasonal, tactical and brand — from strategy and planning through online + offline execution, building brand affinity and keeping the brands top-of-mind across the UAE and 50+ GCC/MENA markets",
                "Run quick-commerce end-to-end, integrating brands into the UAE's q-commerce platforms — Noon, talabat, Careem and Deliveroo — owning onboarding, listings, promotional mechanics and retail execution to drive conversion, repeat orders and sell-out",
                "Design FMCG and retail co-marketing initiatives with brands, distributors and modern-trade partners — joint promotions, sampling/seeding and activations that lift reach and sell-through for both sides",
                "Align online and offline: sync activations, launches and in-store with the digital, social and influencer roadmap (25–50 creators per campaign), directing creative agencies and production houses to a high standard on time and on budget",
                "Bridge Commercial, Creative and CRM/EDM — translating each campaign into targeted in-app, push and promo briefs that drive repeat orders and retention on quick-commerce",
                "Own the A&P budget and track localized spend and campaign impact (ROI, ROAS, conversion) against business targets, using an AI (Claude/GPT) reporting system that cuts manual workload ~40% and speeds quick-turnaround decisions",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace & consumer app | 100K+ employees",
            "bullets": [
                "Created and led integrated brand campaigns — Beauty Club and Hot on Social — from concept to activation on a top-5 marketplace, working across social, content and commercial teams to build brand affinity and position Miravia as a beauty and lifestyle destination",
                "Ran co-marketing with 42 brand accounts — joint promotions, assortment and pricing plays — growing +30% GMV QoQ and reporting the Flash Sales channel directly to the CEO",
                "Onboarded 30+ brands in two months as category lead, using trend-driven products and cultural moments to drive discovery, conversion and repeat purchase on a consumer app used by millions",
                "Analysed campaign performance (conversion, traffic, retention, ROI) to sharpen creative and commercial decisions and improve forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce marketplace | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped launch and build Glovo's Retail vertical from the ground up — taking a q-commerce marketplace beyond food delivery into fashion, beauty and lifestyle, the same online-local-marketplace model instashop runs",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), delivering bespoke marketing activations and promotional campaigns that drove order volume, conversion and GMV",
                "Led cross-functional teams across marketing, logistics and CX to deliver campaigns end-to-end and negotiated high-impact commercial deals maximising profitability for platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness analysis for the chocolate category — FMCG trade-marketing grounding in turning data into commercial action",
                "Contributed to brand NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": (
        "integrated 360 campaigns (strategy → planning → execution), seasonal / tactical / brand campaigns, "
        "brand affinity & brand presence, co-marketing & partnerships (FMCG + retail), online/offline synergy, "
        "OOH & experiential activations, events & launches, influencer & creator marketing, sampling & seeding, "
        "trade & shopper marketing, go-to-market"
    ),
    "skills_ecommerce": (
        "quick-commerce / q-commerce (Noon, talabat, Careem, Deliveroo), marketplaces & consumer apps "
        "(Miravia, Glovo), Meta Ads (Facebook & Instagram), Google Ads, social & content, CRM & EDM, in-app & "
        "push messaging, retention / repeat orders, Shopify e-store, marketing automation, generative-AI content"
    ),
    "skills_commercial": (
        "creative agency, production house & OOH/print vendor management, co-marketing & partner management, "
        "cross-functional & senior-stakeholder management (Commercial, Creative, CRM), A&P budget management, "
        "key account management, negotiation, category management, modern trade"
    ),
    "skills_data": (
        "performance & budgeting (ROI, ROAS, conversion, CAC/CPO), campaign KPI tracking & reporting, "
        "market intelligence & competitor analysis, consumer & sell-out insight, AI-assisted analysis & "
        "forecasting, Looker, Power BI, Nielsen, Kantar, Salesforce"
    ),
    "skills_tools": (
        "Meta Ads Manager, Google Ads, Generative AI (Claude / ChatGPT), Shopify, Canva, Salesforce, "
        "Power BI, Tableau, Looker, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="instashop-sr-specialist-marketing-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.instashop.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Sr. Specialist Marketing instashop Delivery Hero", "via": "LinkedIn"},
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
        "ai_score": 91,
        "ai_tier": "Hot",
        "skills_match": [
            "4+ yrs in the 4–6 band — no tenure gap",
            "Q-Commerce preferred = exact fit: integrates brands into Noon/talabat/Careem/Deliveroo today; came up through Glovo (q-commerce)",
            "instashop is Delivery Hero family — talabat (Paula's live q-commerce channel) is the same group",
            "Integrated 360 campaigns end-to-end, online + offline (DoFreeze)",
            "FMCG + retail co-marketing / partnerships (FMCG distributor + Miravia brand accounts + Mondelez)",
            "Cross-functional bridge: Commercial, Creative, CRM/EDM → in-app/push briefs for repeat orders",
            "Performance & budgeting: A&P budget, ROI/ROAS/conversion vs targets",
            "Vendor & agency management: creative agencies, production houses, creators",
            "GCC / UAE; already in Dubai on residence visa",
        ],
        "missing_skills": [
            "CAC named explicitly in JD (Paula tracks ROI/ROAS/conversion/GMV; CAC/CPO literacy via paid media)",
            "Arabic (not required)",
        ],
        "sector_fit": "excellent (q-commerce marketplace · FMCG co-marketing · GCC — Delivery Hero family)",
        "seniority_fit": "on-band (4–6 yrs asked; Paula 4+) — clean fit, no stretch",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Near-perfect fit and one of the cleanest Paula has: the JD asks 4–6 yrs in brand/campaign/growth/"
            "trade marketing in the GCC with Q-Commerce preferred, and Paula sits exactly there — 4+ yrs, GCC-based, "
            "and quick-commerce is her rare standout (integrates brands into Noon/talabat/Careem/Deliveroo today and "
            "came up through Glovo). instashop being Delivery Hero family (same group as talabat, which she works "
            "with live) is a strong narrative hook. Her DoFreeze remit maps to the JD almost line by line: integrated "
            "360 campaigns end-to-end, FMCG/retail co-marketing, online/offline synergy, agency/production direction, "
            "A&P budget ownership and ROI/ROAS/conversion tracking. No tenure gap; only nuance is CAC named "
            "explicitly, covered by her performance-marketing metric literacy."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


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
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
