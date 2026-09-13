"""One-off: generate Paula's CV for the District (by Zomato)
"Brand Marketing Manager" (Dubai) role — inbound via a TRJ recruiter on LinkedIn.

District by Zomato is a fast-growing consumer-tech platform for discovering
dining, events, movies and experiences across the UAE — an early-stage lifestyle
brand. The role is brand marketing end-to-end: strategy/insight → positioning,
messaging & tone → integrated campaigns → on-ground activations, launches and
experiential — working with agencies, creators, photographers, production teams
and hospitality/venue/media/event partners, owning budgets, production and
timelines, all tuned to UAE consumer behaviour and cultural moments.

Paula's fit is genuinely strong on the substance: as Brand & Marketing Manager at
DoFreeze she owns brand positioning and integrated campaigns end-to-end, directs
creators/agencies/production, runs on-ground activations tied to cultural moments,
and owns budgets. Her platform/marketplace DNA is the standout — Glovo (a consumer-
tech platform where she helped launch the Retail vertical and ran DINING/hospitality
accounts: KFC, Taco Bell, La Tagliatella, Sushi Shop) and Miravia/Alibaba (a top-5
marketplace where she built integrated brand campaigns and positioned it as a
lifestyle destination). The one honest gap — JD asks 6–8 yrs, Paula has 4+ — is
NOT papered over on the CV; it's flagged for the cover letter / recruiter reply.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. Fills the real CV template, converts to PDF,
and lands the package under output/2026-08-12/District - Brand Marketing Manager/.
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

COMPANY = "District"
TITLE = "Brand Marketing Manager"
DATE_FOLDER = "2026-08-12"

JOB_DESCRIPTION = """\
Marketing / Brand Marketing Manager — District (by Zomato), Dubai, UAE. 6–8 years.

We're hiring for a fast-growing consumer technology platform redefining how people
discover dining, events, movies and experiences across the UAE. Join early and help
build one of the region's most exciting lifestyle brands. Ideal for someone who
thrives in high-growth environments, enjoys building impactful campaigns, and
understands the UAE consumer landscape.

Key responsibilities: Lead end-to-end brand campaigns from strategy and insights
through execution. Plan and execute integrated marketing campaigns to drive user
growth and engagement. Define brand positioning, messaging, tone of voice and the
campaign calendar. Collaborate with designers, agencies, creators, photographers and
production teams to deliver high-quality campaigns. Execute on-ground activations,
venue partnerships, launches and experiential marketing initiatives. Build
relationships with agencies, hospitality brands, media partners, creators,
influencers and event organizers. Manage campaign budgets, production, timelines and
vendor partnerships. Identify cultural moments and marketing opportunities to
strengthen brand awareness and customer engagement.

Requirements: 6–8 years of marketing experience in the UAE. Background in Brand,
Consumer, Integrated, Growth Marketing or Marketing Strategy. Experience with
consumer brands, marketplaces, hospitality, dining, entertainment, events or
lifestyle businesses. Proven success leading integrated campaigns from strategy to
execution. Strong creative judgment and experience working with agencies and creative
teams. Deep understanding of UAE consumer behaviour and cultural trends. Ability to
thrive in a fast-paced, high-ownership environment.

Preferred: Experience launching a brand, product or new business vertical in the UAE.
Strong network across agencies, creators, hospitality groups, venues, media owners or
event partners. Experience with consumer apps, marketplaces or platform businesses.
Arabic proficiency is a plus.
"""

ATS = [
    "brand marketing", "brand campaigns end-to-end", "strategy to execution",
    "brand positioning", "messaging", "tone of voice", "campaign calendar",
    "integrated marketing", "integrated campaigns", "user growth", "engagement",
    "brand awareness", "creative brief", "briefing", "agencies", "creative teams",
    "designers", "photographers", "production", "creators", "influencers",
    "on-ground activations", "experiential marketing", "launches", "venue partnerships",
    "hospitality", "dining", "events", "entertainment", "lifestyle",
    "media partners", "event organizers", "budget management", "vendor partnerships",
    "timelines", "cultural moments", "Ramadan", "Eid", "UAE consumer",
    "consumer apps", "marketplaces", "platform business", "new vertical launch",
    "consumer tech", "high-growth", "high-ownership", "fast-paced",
]

CONTENT = {
    "headline": (
        "Brand Marketing Manager · Integrated Campaigns Strategy → Execution · "
        "Consumer-Tech, Marketplaces & Lifestyle · UAE"
    ),
    "professional_summary": (
        "Brand marketer who builds and runs integrated campaigns end-to-end — from consumer insight and brand "
        "positioning to messaging, creative and full execution — for consumer-tech platforms, marketplaces and "
        "lifestyle brands. Currently lead Brand & Marketing at DoFreeze in Dubai: I define positioning, tone and "
        "the campaign calendar, direct designers, agencies, photographers, production teams and 25–50 creators per "
        "campaign, run on-ground activations and launches timed to UAE cultural moments, and own the budget, "
        "production and timelines. Platform-native — I helped launch Glovo's Retail vertical and ran its dining/"
        "hospitality accounts, and built brand campaigns on Alibaba's Miravia marketplace. Deep read on the UAE "
        "consumer, AI-native, and already in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Lead brand campaigns end-to-end for DoFreeze's consumer brands — from strategy and consumer insight through creative, messaging and tone of voice to full execution — building awareness and engagement across the UAE and 50+ GCC/MENA markets",
                "Define brand positioning, messaging and the campaign calendar, then bring it to life with designers, creative agencies, photographers, production teams and 25–50 creators/influencers per campaign — directing the work to a high creative standard",
                "Plan and run integrated campaigns across paid social (Meta, Google), influencer, CRM/EDM, content and in-store to drive brand awareness, growth and engagement — tracking KPIs (ROI, ROAS, sell-out) with an AI (Claude/GPT) system that cuts reporting workload ~40%",
                "Execute on-ground activations, product launches and sampling/seeding across modern trade and quick-commerce — timing them to UAE cultural moments (Ramadan, Eid, National Days) to maximise reach and relevance",
                "Own campaign budgets, production and timelines end-to-end, managing vendor and agency partnerships so every campaign lands on time, on budget and on brand",
                "Lead go-to-market for 6 new-product launches (brief → packaging → pricing → launch), crafting each brand's story for the UAE consumer",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace & consumer app | 100K+ employees",
            "bullets": [
                "Created and led integrated brand campaigns — Beauty Club and Hot on Social — from concept to activation on a top-5 marketplace, working across social, content and commercial teams to build brand love and position Miravia as a beauty and lifestyle destination",
                "Grew 42 key accounts +30% GMV QoQ through campaign-led promotions, assortment and pricing, reporting the Flash Sales channel directly to the CEO",
                "Onboarded 30+ brands in two months as category lead, using trend-driven products and cultural moments to drive discovery and engagement on a consumer app used by millions",
                "Analysed campaign performance (conversion, traffic, retention, ROI) to sharpen creative and commercial decisions and improve forecasting",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Consumer-tech quick-commerce platform | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped launch and build Glovo's Retail vertical from the ground up — taking a consumer-tech platform beyond food delivery into fashion, beauty and lifestyle: the same multi-category discovery play District is building for the UAE",
                "Managed strategic dining and hospitality accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), delivering bespoke marketing activations and campaigns that drove order volume and GMV",
                "Led cross-functional teams across marketing, logistics and CX to deliver campaigns end-to-end in a fast-paced, high-ownership environment",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built promotional-effectiveness and performance analysis for the chocolate category — early grounding in the insight-to-action mindset brand campaigns depend on",
                "Contributed to brand NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": (
        "brand campaigns end-to-end (strategy → execution), brand positioning, messaging & tone of voice, "
        "integrated marketing, campaign calendar, go-to-market & brand launches, influencer & creator marketing, "
        "experiential & on-ground activations, cultural-moment activations (Ramadan / Eid / National Days), "
        "sampling & seeding, shopper & trade marketing"
    ),
    "skills_ecommerce": (
        "consumer apps & marketplaces (Miravia, Glovo, Noon, talabat, Careem, Deliveroo), Meta Ads "
        "(Facebook & Instagram), Google Ads, social & content, CRM & EDM, Shopify e-store, marketing "
        "automation, generative-AI content"
    ),
    "skills_commercial": (
        "agency, creator & vendor management, cross-functional & senior-stakeholder management, budget & "
        "production management, key account management, negotiation, category management, modern trade"
    ),
    "skills_data": (
        "campaign KPI tracking & reporting, ROI / ROAS / GMV, budget & timeline management, consumer & "
        "performance insight, AI-assisted analysis & forecasting, Looker, Power BI, Nielsen, Kantar, Salesforce"
    ),
    "skills_tools": (
        "Meta Ads Manager, Google Ads, Generative AI (Claude / ChatGPT), Shopify, Canva, Salesforce, "
        "Power BI, Tableau, Looker, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="district-brand-marketing-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.district.ae/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Brand Marketing Manager District Zomato", "via": "LinkedIn / TRJ recruiter"},
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
        "ai_score": 83,
        "ai_tier": "Hot",
        "skills_match": [
            "Brand campaigns end-to-end, strategy → execution (DoFreeze)",
            "Brand positioning, messaging, tone of voice & campaign calendar",
            "Creator/agency/photographer/production direction (25–50 creators/campaign)",
            "On-ground activations, launches & cultural-moment marketing (Ramadan, Eid)",
            "Budget, production & timeline ownership + vendor partnerships",
            "Platform/marketplace native — Glovo (launched Retail vertical, ran dining/hospitality accounts) + Miravia/Alibaba",
            "Deep UAE consumer read; already in Dubai (residence visa)",
        ],
        "missing_skills": [
            "6–8 yrs UAE tenure (Paula has 4+, ~1 yr in-market)",
            "Arabic (plus, not required)",
        ],
        "sector_fit": "strong (consumer-tech · marketplaces · lifestyle · dining/hospitality via Glovo)",
        "seniority_fit": "good on substance; tenure below the 6–8 yr band",
        "red_flags": ["Tenure below 6–8 yrs and limited time in-UAE — address head-on in the recruiter reply / cover letter"],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong substance fit for a brand-marketing role at an early-stage UAE consumer-tech/lifestyle "
            "platform. Paula's DoFreeze remit is exactly this: brand positioning + integrated campaigns "
            "end-to-end, creator/agency/production direction, on-ground activations tied to cultural moments, "
            "budget & timeline ownership. Standout differentiator is platform/marketplace DNA — Glovo (helped "
            "launch the Retail vertical, ran dining/hospitality accounts) and Miravia/Alibaba (integrated brand "
            "campaigns, lifestyle-destination positioning) — which maps directly to District's dining/events/"
            "lifestyle discovery play. Real gap is tenure (JD 6–8 yrs vs 4+) and limited months in-market; "
            "handled honestly in outreach, not on the CV."
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

    # --- CV only (recruiter asked for the resume) ---
    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
