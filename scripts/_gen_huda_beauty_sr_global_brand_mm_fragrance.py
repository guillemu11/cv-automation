"""One-off: generate Paula's CV for Huda Beauty
"Senior Global Brand Marketing Manager - Fragrance" (Dubai, UAE — prestige beauty / fragrance).

Reach-but-plausible fit. Huda Beauty is a Dubai-born prestige beauty powerhouse;
the role is a SENIOR, GLOBAL, brand-side fragrance marketing lead: own 360°
launch campaigns end-to-end (concept positioning → global commercialization),
fragrance storytelling / olfactive positioning, launch toolkits (messaging,
visual identity, paid, e-com content, retailer assets, PR, influencer guidelines,
education, sampling), experiential/gifting/retail theatre, cross-functional
leadership + project management, partner with Product Development & Creative.

What maps genuinely onto Paula's real track:
  - 360° integrated launch campaigns + end-to-end NPD (6 launches concept→GTM)
    + creative briefing + launch calendars + e-commerce content + paid media —
    all real at DoFreeze across 50+ markets.
  - Influencer programme built from zero (25–50 creators/campaign, influencer
    guidelines) + sampling & seeding + social-first storytelling — real (DoFreeze).
  - Fragrance & prestige-beauty depth: at Alibaba's Miravia she OWNED the Beauty
    & Fragrances category (42 accounts, +30% GMV QoQ) and, as PIC Fragrances,
    onboarded the official distributors of leading Arabian & oud houses (Arabian
    Oud, Lattafa, Swiss Arabian, Ajmal) — genuine premium-fragrance-landscape
    fluency and consumer/positioning work.
  - Consumer/market/competitor/trend analysis + post-launch learnings (Miravia,
    Mondelez category planning).

Kept strictly truthful — honest gaps NOT papered over:
  - She has 4+ years (JD asks "typically 5+"). We state 4+, never inflate.
  - Her fragrance depth is COMMERCIAL / category / e-commerce (Miravia), plus
    brand-side NPD launches in FMCG/F&B (DoFreeze) — NOT proven global *prestige
    fragrance brand* launches on the brand-marketing side. The CV foregrounds the
    genuine adjacency (fragrance category ownership, Arabian oud houses, 360° NPD
    launch execution, influencer/experiential) without claiming prestige-fragrance
    brand-launch tenure she doesn't have.
  - VISA: already in Dubai on a UAE residence visa. Per the standing rule we NEVER
    claim "no sponsorship needed" (the visa is employer-sponsored). We only state
    she is already based in Dubai (zero relocation timeline).

Fills the real CV template, converts to PDF via LibreOffice (soffice headless —
docx2pdf/Word silently fails on this Mac), registers the job for the dashboard
with an honest score, and lands the package under output/2026-08-27/.

CV only (as requested). Cover letter + the existing Huda Beauty "360° Launch"
concept deliverable can be added to the same package on request.
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

COMPANY = "Huda Beauty"
TITLE = "Senior Global Brand Marketing Manager - Fragrance"
DATE_FOLDER = "2026-08-27"

JOB_DESCRIPTION = """\
Senior Global Brand Marketing Manager - Fragrance — Huda Beauty, Dubai, UAE.

Lead the global marketing strategy and execution for the fragrance portfolio,
developing breakthrough 360° launch campaigns that build brand equity, drive
consumer desire and achieve commercial objectives. Own end-to-end marketing
development of new fragrance launches and core franchise support, from concept
positioning through global launch execution. Translate olfactive compositions,
ingredients, craftsmanship, inspiration and emotional storytelling into engaging
consumer narratives across all channels. Define strategic consumer, positioning,
messaging hierarchy, campaign architecture and key selling points per launch.
Lead global launch toolkits (campaign messaging, visual identity, paid media
assets, e-commerce content, retailer assets, PR materials, influencer guidelines,
education materials, sampling strategies). Develop consumer experiences that
elevate fragrance discovery — experiential activations, gifting moments, sampling
programs, influencer events, retail theatre, social-first storytelling.
Collaborate with Creative, Commercial, Education, Digital, PR, Social and Regional
Marketing. Own creative briefing and campaign development. Build annual launch
calendars and integrated marketing plans. Analyse market trends, competitive
activity, consumer behaviour and cultural shifts to identify whitespace. Monitor
campaign performance and post-launch learnings. Lead cross-functional project
management across global stakeholders; partner with regional markets on
localization while maintaining global brand consistency.

Requirements: proven track record building & launching successful fragrance
brands/campaigns within prestige beauty or luxury fragrance (typically 5+ years);
proven global fragrance launches concept→commercialization; strong fragrance
storytelling, olfactive positioning, consumer behaviour and premium fragrance
landscape knowledge; integrated 360° campaigns across digital, retail, PR,
influencer, social, experiential and e-commerce; influence cross-functional teams
and manage multiple global projects; strong strategic thinking + execution + PM;
partnering with Product Development and Creative; excellent communication,
presentation and stakeholder management.
"""

ATS = [
    "Global Brand Marketing Manager", "fragrance", "prestige beauty",
    "luxury fragrance", "360 campaign", "360 marketing", "integrated marketing",
    "brand equity", "consumer desire", "commercial growth", "brand strategy",
    "fragrance storytelling", "olfactive positioning", "consumer positioning",
    "messaging hierarchy", "campaign architecture", "key selling points",
    "launch campaign", "global launch", "concept to commercialization",
    "new product development", "NPD", "go-to-market", "launch toolkit",
    "visual identity", "paid media", "e-commerce content", "retailer assets",
    "PR", "influencer", "influencer guidelines", "education", "sampling",
    "sampling programs", "experiential", "gifting", "retail theatre",
    "social-first", "UGC", "creative briefing", "creative brief",
    "launch calendar", "integrated marketing plan", "market trends",
    "competitive activity", "consumer behaviour", "cultural shifts",
    "whitespace", "post-launch", "campaign performance", "ROI",
    "cross-functional", "project management", "stakeholder management",
    "Product Development", "Creative", "localization", "global brand consistency",
    "beauty", "fragrances", "GCC", "MENA", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Brand & Marketing Manager · Beauty & Fragrance · 360° Launch Campaigns · "
        "NPD Concept-to-Market · Influencer, Social & Experiential · Global (50+ Markets)"
    ),
    "professional_summary": (
        "Brand & marketing manager with 4+ years building and launching brands across Beauty, Fragrances, "
        "Fashion and FMCG — now leading Brand & Marketing for DoFreeze across 50+ markets from Dubai. I take "
        "products from concept to market: end-to-end NPD for 6 launches, breakthrough 360° campaigns spanning "
        "digital, social, PR, influencer, experiential and e-commerce, and an influencer programme I built from "
        "zero to 25–50 creators per campaign with sampling & seeding. My commercial grounding is in fragrance and "
        "prestige beauty — at Alibaba's Miravia I owned the Beauty & Fragrances category across 42 accounts "
        "(+30% GMV QoQ) and onboarded the official distributors of leading Arabian & oud houses (Arabian Oud, "
        "Lattafa, Swiss Arabian, Ajmal), building genuine fluency in the premium fragrance landscape and consumer "
        "behaviour. Strategic and hands-on in equal measure, AI-first and data-led, and already based in Dubai on "
        "a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Lead 360° marketing strategy and execution across the brand portfolio — building integrated launch campaigns that span digital, social, PR, influencer, experiential and e-commerce to build brand equity, drive consumer desire and achieve commercial objectives",
                "Own end-to-end NPD for 6 product launches from concept positioning and creative brief through global go-to-market — defining messaging hierarchy and key selling points and building the launch toolkit (packaging, campaign messaging, retailer and e-commerce assets) across GCC, MENA, Asia, Europe, USA and Africa",
                "Built the influencer programme from zero — sourcing, briefing and managing 25–50 creators per campaign with influencer guidelines, product seeding and sampling programmes across modern trade and quick-commerce, driving UGC, social-first storytelling and measurable sell-out",
                "Own creative briefing and campaign development end-to-end, partnering with creative and product teams so every asset reflects the brand vision — paid media, e-commerce content, retailer assets and education/sampling materials",
                "Build annual launch calendars and integrated marketing plans and run the brand's Shopify store end-to-end; analyse market trends, competitors, cultural shifts and post-launch performance to sharpen future launches and marketing investment",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned the Beauty & Fragrances category across 42 accounts, growing GMV +30% QoQ through consumer positioning, assortment, pricing and a data-led promotional calendar — building deep fluency in the premium fragrance landscape and consumer behaviour",
                "As PIC Fragrances, led category expansion — onboarding and negotiating with 30+ new brands/stores in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Created and led the Beauty Club and Hot on Social projects — social-first storytelling and brand moments that lifted visibility, desire and loyalty and positioned Miravia as a beauty and fragrance destination",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO against P&L targets; analysed market trends, competitors and new launches to identify whitespace and strengthen go-to-market",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Onboarded fashion, beauty and lifestyle brands as Glovo built out its Retail vertical, delivering bespoke marketing activations that grew GMV beyond food delivery",
                "Led cross-functional teams across marketing, logistics and operations to ship campaigns on time, on scope and grow order volume",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept toward shelf within a global FMCG brand",
                "Ran sell-in/sell-out, Nielsen performance and promotional-effectiveness analysis, translating consumer and market data into brand and category recommendations",
            ],
        },
    ],
    "skills_brand": (
        "360° integrated campaigns, brand strategy & equity, fragrance & beauty storytelling, consumer positioning, "
        "messaging hierarchy, NPD concept-to-market, global launch toolkits, creative briefing, influencer marketing "
        "& guidelines, experiential activations & sampling, PR & social-first storytelling, launch calendars, "
        "A&P budget management, go-to-market"
    ),
    "skills_ecommerce": (
        "e-commerce content, Shopify & e-store management, quick-commerce (Noon, Talabat, Careem, Deliveroo), "
        "Meta & Google Ads, Instagram, TikTok, Pinterest, EDM, conversion rate optimisation (CRO), "
        "marketing automation (generative AI)"
    ),
    "skills_commercial": (
        "premium fragrance & beauty category, brand & retailer partnerships, distributor & supplier onboarding, "
        "key account management, negotiation, pricing & assortment, category management, cross-functional "
        "project management, stakeholder management"
    ),
    "skills_data": (
        "market, competitor & trend analysis, consumer behaviour insight, campaign performance & post-launch "
        "learnings, P&L & KPI tracking, ROI / ROAS, sell-in/sell-out, AI-assisted analysis, Nielsen, Kantar, Power BI"
    ),
    "skills_tools": (
        "Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, Generative AI (Claude, ChatGPT), Canva, "
        "Salesforce, SAP, Power BI, Tableau, Nielsen, Kantar, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="huda-beauty-sr-global-brand-mm-fragrance-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/view/huda-beauty-senior-global-brand-marketing-manager-fragrance",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Senior Global Brand Marketing Manager Fragrance",
             "function": "Brand Marketing", "category": "Fragrance / Prestige beauty",
             "channel": "Global 360° (digital, retail, PR, influencer, social, experiential, e-com)"},
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
        "ai_score": 70,
        "ai_tier": "Warm",
        "skills_match": [
            "360° integrated launch campaigns end-to-end (DoFreeze, across 50+ markets)",
            "End-to-end NPD concept→go-to-market, 6 launches (DoFreeze)",
            "Influencer programme from zero + guidelines + sampling & seeding (DoFreeze)",
            "Fragrance & prestige-beauty category ownership (Miravia, 42 accounts, +30% GMV QoQ)",
            "Premium/Arabian fragrance landscape: onboarded Arabian Oud, Lattafa, Swiss Arabian, Ajmal (Miravia PIC Fragrances)",
            "Creative briefing + launch toolkits + e-commerce content + retailer/PR assets (DoFreeze)",
            "Market/competitor/trend analysis + post-launch learnings (Miravia, Mondelez)",
            "Cross-functional project management + stakeholder management (DoFreeze, Glovo)",
            "Based in Dubai (UAE residence visa); Huda Beauty is Dubai-HQ",
        ],
        "missing_skills": [
            "Proven GLOBAL PRESTIGE-FRAGRANCE *brand* launches concept→commercialization — Paula's fragrance depth is commercial/category/e-commerce (Miravia) + FMCG/F&B NPD launches (DoFreeze), adjacent not identical",
            "5+ years in prestige beauty / luxury fragrance — Paula has 4+ years across beauty/fragrances/FMCG, not claimed as 5+",
            "Deep olfactive-composition storytelling as a brand marketer — adjacent (fragrance category + brand storytelling), not owned tenure",
        ],
        "sector_fit": "strong (Dubai-HQ prestige beauty; fragrance is within Paula's core beauty/fragrances category)",
        "seniority_fit": "reach (Senior, Global, brand-side fragrance lead; Paula 4+ yrs, fragrance mostly commercial-side)",
        "red_flags": [
            "Headline requirement is proven prestige-fragrance BRAND launches — Paula's fragrance experience is category/commercial + FMCG NPD, a genuine adjacency but not brand-side prestige-fragrance launch tenure",
            "JD asks 'typically 5+ years' in prestige beauty/luxury fragrance — Paula is at 4+",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Reach-but-plausible. Huda Beauty (Dubai-HQ prestige beauty) wants a SENIOR, GLOBAL, brand-side "
            "fragrance marketing lead: own 360° launch campaigns concept→commercialization, fragrance/olfactive "
            "storytelling, launch toolkits, experiential/sampling, cross-functional PM, partner with Product Dev & "
            "Creative. Genuine overlap on Paula's real track: 360° integrated launches + end-to-end NPD (6, "
            "concept→GTM) + influencer programme from zero + sampling/seeding + creative briefing + e-commerce "
            "content at DoFreeze across 50+ markets; and real fragrance/prestige-beauty grounding at Alibaba's "
            "Miravia (owned the Beauty & Fragrances category, 42 accounts, +30% GMV QoQ; as PIC Fragrances "
            "onboarded the official distributors of Arabian Oud, Lattafa, Swiss Arabian, Ajmal). Honest gaps: no "
            "proven GLOBAL PRESTIGE-FRAGRANCE *brand* launches on the brand-marketing side (her fragrance depth is "
            "commercial/category/e-commerce), 4+ vs 'typically 5+' years, and olfactive brand storytelling is "
            "adjacent not owned. Positioned truthfully — no invented prestige-fragrance launch tenure, no inflated "
            "tenure, no 'no sponsorship needed' claim (employer-sponsored UAE residence visa). Worth applying with "
            "a strong 360°/NPD + fragrance-category narrative; her portfolio already includes a Huda Beauty '360° "
            "Launch' concept."
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

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
