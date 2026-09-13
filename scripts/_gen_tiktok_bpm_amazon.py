"""One-off: generate Paula's application package for the TikTok
"Brand Partnerships Manager, Amazon" (Global Agency & Accounts + Amazon team) role.

This is a *pivot / stretch* application. The JD is a platform-side media-sales /
brand-partnerships role: a revenue-carrying BPM who builds long-term trusted
client relationships across multiple brands under one parent (Amazon), sells
TikTok's ad products consultatively, builds compelling sales presentations,
and drives/exceeds revenue goals — partnering cross-functionally with Client
Solutions Managers.

Paula has never been a *platform* media seller (selling ad inventory). But she
is a revenue-carrying **key account manager** (Miravia: 42 accounts, +30% GMV
QoQ, Flash Sales P&L reporting to the CEO; Glovo XL Accounts: strategic KAs,
negotiated and closed commercial deals) and a hands-on **biddable / self-serve
digital-media practitioner** (Meta Ads — Facebook & Instagram — and Google Ads,
auction buying, creative A/B testing, ROI/ROAS) who also runs **creator-led
social** at scale (25–50 creators per campaign) and builds **client-ready sales
decks**. Those are the genuine bridges the JD asks for.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented media-sales/CTV/OTT/Amazon-Ads experience. The two real
gaps (never sold platform ad inventory; 4+ yrs vs 5+ ask) are addressed head-on
in the cover letter rather than papered over.

Fills the real CV + cover-letter templates, converts to PDF, and lands the
package under output/2026-08-12/TikTok - Brand Partnerships Manager, Amazon/.
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
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "TikTok"
TITLE = "Brand Partnerships Manager, Amazon"
DATE_FOLDER = "2026-08-12"

JOB_DESCRIPTION = """\
Brand Partnerships Manager (BPM), Global Agency & Accounts (GA&A) + Amazon team — TikTok.

The GA&A + Amazon team partners with some of the world's most influential
advertisers to accelerate growth and deepen engagement across TikTok, building
long-term, trusted relationships with global clients. The BPM on the Amazon team
is a key growth driver responsible for developing long-term, trusted client
relationships across multiple brands under a single parent company. This is a
strategic, revenue-generating role combining consultative selling with deep
cross-functional collaboration. The ideal candidate is a proactive, persuasive
storyteller, skilled in navigating complex client organizations, aligning
solutions to business objectives, and driving measurable results through TikTok's
suite of advertising products. BPMs partner closely with Client Solutions Managers
(CSMs).

Responsibilities: Act as a strategic advisor by demonstrating deep product
knowledge and delivering tailored solutions to unique business goals. Lead the
account planning process and align cross-functional resources to client
priorities and long-term growth. Elevate TikTok's brand narrative. Drive revenue
growth, foster strategic conversations, and build relationships across client
organizations. Grow global client relationships and scale product adoption across
brands and markets. Deepen penetration across brands and markets, identifying
whitespace opportunities and unlocking incremental investment. Create compelling
sales presentations and proposals leveraging internal insights and market
intelligence to influence and persuade. Educate clients on best practices, product
updates and new solutions to drive adoption. Manage the full sales lifecycle,
including proactive issue resolution, campaign troubleshooting and optimization in
collaboration with CSM. Collaborate cross-functionally with product, measurement,
creative and operations teams. Analyze campaign performance, deliver actionable
insights, and iterate to improve results.

Minimum qualifications: 5+ years of media sales, digital marketing, brand
advertising and/or online advertising experience. Experience with digital media
(i.e., Digital TV / CTV, OTT, social media, etc.). Track record of building
compelling presentations leveraging industry and internal proof points. Knowledge
of the self-serve platform, auction, and biddable form of digital advertising
buying.

Preferred qualifications: Proven ability to establish relationships with
advertisers, agencies and C-level executives. Track record of delivering and
exceeding revenue goals. Experience working with global and regional accounts with
an understanding of market-specific dynamics, media landscapes and regulatory
environments. Deep experience across the full marketing funnel, with a nuanced
understanding of advertiser challenges, measurement and KPIs. Collaborative and
team-oriented, with a solution-first mindset.
"""

ATS = [
    "media sales", "brand partnerships", "digital marketing", "brand advertising",
    "online advertising", "digital media", "social media", "self-serve platform",
    "auction", "biddable", "advertising products", "consultative selling",
    "revenue growth", "exceeding revenue goals", "account planning",
    "client relationships", "trusted relationships", "C-level executives",
    "agencies", "advertisers", "compelling sales presentations", "proposals",
    "market intelligence", "product adoption", "whitespace", "incremental investment",
    "full marketing funnel", "campaign performance", "measurement", "KPIs",
    "actionable insights", "cross-functional", "storyteller", "brand narrative",
    "Meta Ads", "Facebook Ads", "Instagram Ads", "Google Ads", "ROI", "ROAS",
    "creator marketing", "TikTok", "e-commerce", "marketplace", "Amazon", "GCC", "MENA",
]

CONTENT = {
    "headline": "Brand Partnerships & Key Account Manager · Consultative Selling & Revenue Growth · Biddable Digital Media (Meta / Google) · Creator-Led Social",
    "professional_summary": (
        "Revenue-carrying commercial and marketing manager who builds long-term, trusted client relationships and "
        "grows them through consultative selling. Managed 42 key accounts to +30% GMV QoQ at Alibaba's Miravia — "
        "owning the Flash Sales channel P&L and reporting to the CEO — and closed strategic commercial deals across "
        "multi-brand clients at Glovo. Hands-on, biddable/self-serve digital-media practitioner: I plan and optimise "
        "Meta Ads (Facebook & Instagram) and Google Ads on the auction, run creative A/B tests, and read ROI/ROAS to "
        "grow performance — and I run creator-led social at scale (25–50 creators per campaign), TikTok's own world. "
        "A persuasive storyteller who builds client-ready sales decks and proposals, fluent across the full marketing "
        "funnel and in e-commerce/marketplace dynamics. Bilingual (ES/EN C1), AI-native, based in Dubai covering 50+ "
        "GCC/MENA markets."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Plan and optimise paid media on the self-serve auction — Meta Ads (Facebook & Instagram) and Google Ads — building audiences, running creative A/B tests and reading ROI/ROAS to drive continuous performance improvement across 50+ GCC/MENA markets",
                "Build and scale a creator-led social programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign plus UGC and seeding — the same creator-and-social storytelling that powers TikTok advertising",
                "Build client-ready sales decks, proposals and campaign landing pages (AI-assisted) that leverage market intelligence and insights to influence and persuade — cutting turnaround while raising quality",
                "Own trusted relationships across distributors, modern-trade partners and quick-commerce platforms — account planning, joint business plans and A&P budgets that identify whitespace and unlock incremental investment",
                "Analyse campaign and channel performance, translate it into actionable insights, and iterate — partnering cross-functionally with commercial, creative and trade teams to improve results",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew a book of 42 key accounts +30% GMV QoQ as a strategic advisor — aligning pricing, assortment and promotional solutions to each client's business goals and consistently delivering against revenue targets",
                "Owned the Flash Sales channel P&L for Beauty, Fashion & Home, reporting directly to the CEO and executing commercial plans aligned to revenue and margin goals",
                "Led category expansion as PIC Fragrances — deepening penetration by onboarding 30+ new brand stores in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Analysed ROI, ROAS, conversion, traffic and retention across the funnel to sharpen account plans, forecasting and adoption of new commercial mechanics",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts across multiple brands (KFC, Taco Bell, La Tagliatella, Sushi Shop), building long-term relationships and driving GMV growth through data-led planning and bespoke marketing activations",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both partners and platform — a consultative, revenue-generating sale",
                "Led cross-functional teams across marketing, logistics and customer support to troubleshoot, optimise and deliver seamless campaigns — the same CSM-style partnership this role runs on",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness analysis and performance reports for the chocolate category — early grounding in measurement, KPIs and the proof points that make a persuasive pitch",
                "Identified growth opportunities feeding NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": "consultative selling & client partnerships, revenue growth & account planning, compelling sales presentations & proposals, persuasive storytelling & brand narrative, creator & influencer marketing (TikTok / social), full-funnel marketing, go-to-market, integrated campaigns",
    "skills_ecommerce": "biddable / self-serve digital advertising — Meta Ads (Facebook & Instagram) & Google Ads, auction buying, creative A/B testing, social media advertising, TikTok & Instagram, e-commerce & marketplaces (Alibaba), quick-commerce, marketing automation",
    "skills_commercial": "key account management, strategic account planning, negotiation & deal closing, advertiser / agency / C-level relationships, multi-brand client management, pricing & assortment strategy, category management, cross-functional collaboration (CSM / product / creative)",
    "skills_data": "revenue & P&L management, campaign performance analysis, ROI / ROAS, conversion / traffic / retention, measurement & KPIs, forecasting, AI-assisted analysis, Looker, Power BI, Tableau, Salesforce, Nielsen, Kantar",
    "skills_tools": "Meta Ads Manager, Google Ads, Salesforce, Generative AI (Claude / ChatGPT), Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "TikTok has turned advertising into storytelling — creator-led, culture-first, measured on real business "
        "outcomes — and that is exactly the kind of selling I want to do next. The Brand Partnerships Manager role on "
        "the Amazon team sits at an intersection I know well from three angles: growing revenue by managing large, "
        "multi-brand accounts as a trusted advisor; running biddable, self-serve digital media on the auction every "
        "week; and building the creator and social programmes that make TikTok work. I'd bring all three."
    ),
    "body_paragraph_1": (
        "My core is revenue-carrying account management. At Alibaba's Miravia I grew a book of 42 key accounts +30% "
        "GMV QoQ as a strategic advisor — aligning pricing, assortment and promotional solutions to each client's "
        "goals — while owning the Flash Sales channel P&L and reporting to the CEO. At Glovo I managed strategic "
        "accounts spanning multiple brands (KFC, Taco Bell, Sushi Shop), and negotiated and closed high-impact "
        "commercial deals. Alongside that I'm a hands-on digital-media practitioner: I plan and optimise Meta Ads "
        "(Facebook & Instagram) and Google Ads on the self-serve auction, run creative A/B tests, and read ROI/ROAS "
        "to grow performance — so I speak the language of biddable buying, the full funnel, measurement and KPIs, and "
        "I build the sales decks and proposals that turn insight into investment."
    ),
    "body_paragraph_2": (
        "What makes me different for the Amazon team specifically: I've lived inside e-commerce and marketplaces at "
        "scale (Alibaba/Miravia, plus UAE quick-commerce), so I understand how a giant retail-and-advertising "
        "advertiser actually thinks about growth, penetration and whitespace across many brands. I run creator-led "
        "social — 25–50 creators per campaign — which is TikTok's native craft, and I'm AI-native, building tooling "
        "that makes account planning, market intelligence and reporting faster. I'll be candid about two things: I've "
        "sold *as* an advertiser and marketplace partner, not yet *for* an ad platform's inventory, and I have 4+ "
        "years rather than 5+. But the muscles this role needs — consultative selling, exceeding revenue targets, "
        "C-level and agency relationships, biddable media fluency and persuasive storytelling — are exactly the ones "
        "I've been building, and I'd back that portfolio against the gap."
    ),
    "closing_paragraph": (
        "I'd love to walk the team through how I'd approach an account plan for a multi-brand advertiser on TikTok — "
        "from the whitespace thesis to the pitch. I'm bilingual (Spanish/English C1), based in Dubai covering GCC/MENA, "
        "and available immediately. Thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="tiktok-bpm-amazon-gaa-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.tiktok.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "TikTok Brand Partnerships Manager Amazon", "via": "LinkedIn / TikTok Careers"},
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
        "ai_score": 68,
        "ai_tier": "Warm",
        "skills_match": [
            "Revenue-carrying key account management (+30% GMV QoQ, 42 accounts — Miravia)",
            "Consultative selling & closing commercial deals (Glovo XL Accounts)",
            "Biddable / self-serve digital media — Meta & Google Ads, auction, A/B, ROI/ROAS",
            "Creator-led social at scale (25–50 creators/campaign) — TikTok's native craft",
            "Client-ready sales decks & proposals; persuasive storytelling",
            "Full-funnel measurement & KPIs; cross-functional (CSM-style) delivery",
            "E-commerce / marketplace depth (Alibaba) — how a big advertiser thinks",
            "C-level & multi-brand client relationships; Dubai-based, ES/EN bilingual",
        ],
        "missing_skills": [
            "Never sold *for* an ad platform's inventory (advertiser/marketplace-side, not platform media sales)",
            "No CTV/OTT experience (has social media)",
            "No direct Amazon Ads / AMS experience",
            "4+ yrs vs 5+ ask",
        ],
        "sector_fit": "adjacent (media sales pivot from KAM + biddable-media practitioner + creator/social)",
        "seniority_fit": "stretch (revenue-carrying KAM maps to BPM; slight tenure gap)",
        "red_flags": [
            "Platform media-sales experience is the core ask and is the genuine gap — addressed head-on in the cover letter",
            "Role may be US-based (Amazon account team) — confirm location vs Dubai / no-relocation preference",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Pivot application. TikTok BPM (Amazon team) is a platform-side media-sales / brand-partnerships role: a "
            "revenue-carrying advisor to a multi-brand advertiser, selling TikTok's ad products consultatively, "
            "building compelling decks and exceeding revenue goals. Paula has not sold platform ad inventory, but her "
            "core is revenue-carrying key account management (Miravia: 42 accounts, +30% GMV QoQ, Flash Sales P&L to "
            "CEO; Glovo: strategic multi-brand KAs, closed deals) plus hands-on biddable/self-serve media (Meta, "
            "Google — auction, A/B, ROI/ROAS), creator-led social at scale (TikTok's craft), and client-ready sales "
            "decks. Real gaps: no platform media-sales tenure, no CTV/OTT, no Amazon-Ads, 4+ vs 5+ yrs — all handled "
            "honestly in the cover letter. Confirm the role's location: an Amazon-account team can be US-based, which "
            "would conflict with Paula's Dubai / no-relocation preference."
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

    # --- CV ---
    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    # --- Cover letter ---
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, contact_name=None)
    cl_pdf = cl._to_pdf(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
