"""One-off: generate Paula's application package for the TikTok
"Client Solutions Manager - Retail & Ecommerce" role.

Source posting (LinkedIn): "Client Solutions Manager - Retail and Ecommerce -
Türkiye & South Asia", TikTok, Dubai (Hybrid). That specific desk hard-requires
Turkish ("Proficient in English and Turkish — will be working with Turkish
speaking clients"), which Paula does NOT have (ES native / EN C1). So this
package is deliberately framed to the *general* TikTok Client Solutions Manager –
Retail & Ecommerce craft — reusable for the same role on non-Turkish desks
(e.g. MENA) — rather than leaning on the Türkiye positioning. No Turkish is
claimed anywhere.

The role is a strong genuine fit on everything except the language gate:
- "Hands-on campaign management (Google Ads, Meta Ads or TikTok Ads) is a must"
  → Paula runs Meta Ads (FB & IG) and Google Ads hands-on on the self-serve
  auction (audiences, A/B creative, ROI/ROAS). REAL.
- "Retail & Ecommerce vertical" → Alibaba/Miravia KAM, Glovo quick-commerce,
  Shopify, UAE quick-commerce onboarding. VERY strong.
- "Post-sale client relationships, business reviews, consultative account growth"
  → 42 key accounts, +30% GMV QoQ, QBRs, Flash Sales P&L to CEO. REAL.
- "Drive adoption of Pixels / TikTok Shop where applicable" → creator-led social
  at scale + pixel-based conversion tracking. Adjacent, REAL.

Two honest gaps (handled in the cover letter, NOT papered over):
- MMP app-tracking (Appsflyer/Adjust) — she has web tracking (Meta Pixel, GA)
  and funnel analysis, not app-install/MMP measurement. Framed as fast ramp.
- Turkish — not claimed; the Türkiye desk specifically is a stretch for that
  reason and is flagged in the dashboard record.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-18/.
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

COMPANY = "TikTok"
TITLE = "Client Solutions Manager - Retail & Ecommerce"
DATE_FOLDER = "2026-08-18"
CONTACT = None

JOB_DESCRIPTION = """\
Client Solutions Manager (CSM) - Retail & Ecommerce — TikTok, Dubai (Hybrid).
(Source posting: Türkiye & South Asia desk.)

The CSM is an expert in TikTok's performance & branding advertisement products
for key clients in marketplaces, fashion, electronics, furniture, beauty, price
comparison sites and quick commerce apps. The CSM acts as a strategic partner to
advertisers across the full funnel, from awareness to conversion, ensuring
scalable campaign execution, robust measurement frameworks and actionable
insights that drive sales and long-term growth. Works with Client Partners to
design end-to-end strategies, manage campaign operations and optimize performance
across web and app channels. Strong understanding of web/app tracking, campaign
optimization, A/B testing and measurement setup is critical.

Responsibilities: Manage and grow post-sale client relationships with Retail &
Ecommerce vertical advertisers; support Client Partners on pre-sale research and
pitch; create and optimize client ad strategies across TikTok for Business
solutions (organic, branding, brandformance, performance, consideration);
increase adoption of the auction platform and auction-based tools with ongoing
technical support and real-time analysis; analyze campaign performance data for
data-driven insights; conduct regular strategic business reviews and take a
consultative long-term approach; keep accurate records of campaign plans and
schedules; act as product champion to drive revenue and adoption; work with
product/engineering to troubleshoot client issues; work with creative teams on
creative solutions and strategy; work with measurement partners on how advertisers
measure success; build trusting relationships with client & agency teams; drive
adoption of Pixels, MMPs and TikTok Shop where applicable; run campaign setup
checks, performance monitoring and optimization; build narratives, workshops and
business reviews to educate and upskill clients; share vertical learnings via case
studies; cooperate with Ad Operations for smooth campaign execution; complement
paid activity with organic presence; deliver post-campaign reporting and account
audits.

Minimum qualifications: Proven experience in performance-based campaign management
(in-house, agency, platform or media side); hands-on campaign management (Google
Ads, Meta Ads or TikTok Ads) is a must; hands-on experience in optimization,
tracking, attribution, measurement using app tracking (MMPs such as Adjust,
Appsflyer) and web tracking (Google Analytics, Omniture); knowledge of app/web
tracking (MMP, GA) is a must; deep understanding of user acquisition &
performance marketing with a passion for social/content platforms and Retail &
Ecommerce; proactive, consultative, strong project management and analytical
skills; self-starter with a start-up spirit; proficient in English and Turkish
(will be working with Turkish speaking clients); ability to travel.

Preferred: diagnosing/solving technical problems with product & engineering;
sales-oriented mindset with strong account management; good technical
understanding of digital marketing tech, integrations and infrastructure;
hands-on experience with App, CPAS, Shopping Ads and broader e-commerce
marketing; proven ability to manage revenue-bearing targets and strategic program
development to drive product adoption.
"""

ATS = [
    "client solutions manager", "performance campaign management", "campaign optimization",
    "Google Ads", "Meta Ads", "Facebook Ads", "Instagram Ads", "TikTok Ads", "auction",
    "self-serve platform", "biddable", "A/B testing", "measurement", "attribution",
    "tracking", "pixel", "conversion tracking", "Google Analytics", "web tracking",
    "user acquisition", "performance marketing", "full funnel", "Retail & Ecommerce",
    "e-commerce", "marketplace", "quick commerce", "TikTok Shop", "CPAS", "Shopping Ads",
    "post-sale", "account management", "consultative selling", "business reviews", "QBR",
    "client relationships", "agency", "product adoption", "revenue growth", "ROI", "ROAS",
    "conversion", "retention", "actionable insights", "cross-functional", "ad operations",
    "creator marketing", "influencer marketing", "social media", "Shopify", "CRO",
    "Noon", "Talabat", "Careem", "Deliveroo", "GCC", "MENA", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Client Solutions Manager · Retail & E-Commerce · Performance Campaign Management "
        "(Meta & Google Ads) · Measurement & Optimisation · Consultative Account Growth"
    ),
    "professional_summary": (
        "Performance-and-e-commerce marketer who runs paid campaigns hands-on and grows advertisers as a "
        "consultative partner — exactly the Client Solutions craft this role needs. I plan, launch and optimise "
        "campaigns on the self-serve auction (Meta Ads — Facebook & Instagram — and Google Ads), building audiences, "
        "A/B-testing creative and reading ROI/ROAS against sales goals, with pixel-based conversion tracking and "
        "Google Analytics on the web side. My home turf is Retail & E-commerce: I managed 42 key accounts to +30% "
        "GMV QoQ at Alibaba's Miravia, run a Shopify store end-to-end (CRO), and onboarded brands across UAE "
        "quick-commerce (Noon, Talabat, Careem, Deliveroo). I grow post-sale relationships through regular business "
        "reviews, optimisation and product adoption, and I pair paid with creator-led social at scale (25–50 creators "
        "per campaign) — TikTok's native, TikTok-Shop-adjacent world. Bilingual (ES native / EN C1), AI-native, "
        "based in Dubai covering 50+ GCC/MENA markets."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Plan, launch and optimise performance campaigns on the self-serve auction — Meta Ads (Facebook & Instagram) and Google Ads — building audiences, running A/B creative tests and pixel-based conversion tracking, and reading ROI/ROAS against efficiency and sales goals across 50+ GCC/MENA markets",
                "Own the full-funnel Retail & E-commerce engine advertisers here live in: Shopify store end-to-end (catalogue, UX, CRO, checkout) plus onboarding and growth across UAE quick-commerce — Noon, Talabat, Careem, Deliveroo — with listings, promo mechanics and retail execution",
                "Build and scale creator-led social from zero (25–50 creators per campaign) with UGC, seeding and TikTok/Instagram content — the organic + creator-commerce that complements paid and maps to TikTok Shop",
                "Turn campaign and channel data into strategic business reviews with clear next steps — partnering cross-functionally with commercial, trade and creative teams to optimise performance and unlock incremental growth",
                "Build client-ready decks, plans and campaign landing pages (AI-assisted) that translate insight into strategy and drive adoption — cutting turnaround while raising quality",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed a book of 42 key accounts as a consultative advisor, growing them +30% GMV QoQ through data-led planning, promotional strategy and regular business reviews — the post-sale account-growth motion this role runs on",
                "Owned the Flash Sales channel P&L for Beauty, Fashion & Home, reporting directly to the CEO and aligning commercial plans to revenue and margin goals",
                "Drove category adoption as PIC Fragrances — onboarding 30+ new brand stores in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Analysed ROI, ROAS, conversion, traffic and retention across the funnel to sharpen forecasts, account plans and the adoption of new commercial mechanics",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic multi-brand key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) end-to-end, driving GMV growth through data-led planning and bespoke marketing activations, and negotiating and closing commercial deals",
                "Led cross-functional teams across marketing, logistics and customer support to troubleshoot, optimise and deliver live campaigns — the ad-operations-style partnership CSMs depend on",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness analysis and performance reports for the chocolate category — early grounding in measurement, KPIs and optimisation",
                "Identified growth opportunities feeding NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (
        "consultative account management & client solutions, strategic business reviews (QBRs) & optimisation, "
        "performance campaign strategy (full funnel), creator & influencer marketing (TikTok / social), "
        "go-to-market, retail media & shopper marketing, product adoption"
    ),
    "skills_ecommerce": (
        "performance / auction media — Meta Ads (Facebook & Instagram) & Google Ads, creative A/B testing, "
        "pixel-based conversion tracking, Google Analytics (web tracking), e-commerce & marketplaces "
        "(Alibaba / Miravia), quick-commerce (Noon, Talabat, Careem, Deliveroo), Shopify & CRO, "
        "TikTok & Instagram, TikTok-Shop-adjacent creator commerce, marketing automation"
    ),
    "skills_commercial": (
        "key account management, post-sale relationship growth, consultative selling & negotiation, "
        "multi-brand client & agency management, pricing & assortment strategy, category management, "
        "cross-functional collaboration (ad-ops / product / creative)"
    ),
    "skills_data": (
        "campaign performance analysis, ROI / ROAS, conversion / traffic / retention, measurement & KPIs, "
        "A/B testing, P&L, forecasting, AI-assisted analysis, Looker, Power BI, Tableau, Salesforce"
    ),
    "skills_tools": (
        "Meta Ads Manager, Google Ads, Google Analytics, Shopify, Salesforce, "
        "Generative AI (Claude / ChatGPT), Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "TikTok turned Retail & E-commerce advertising into full-funnel performance — creator-led, measured on real "
        "sales — and that is precisely where I work every week. The Client Solutions Manager role sits at an "
        "intersection I know from three sides: running performance campaigns hands-on on the self-serve auction, "
        "growing e-commerce advertisers as a consultative partner through business reviews and optimisation, and "
        "pairing paid with the creator-led social that is TikTok's native craft. I'd bring all three."
    ),
    "body_paragraph_1": (
        "I'm a hands-on performance practitioner. At DoFreeze I plan, launch and optimise campaigns on Meta Ads "
        "(Facebook & Instagram) and Google Ads — building audiences, A/B-testing creative, setting up pixel-based "
        "conversion tracking and Google Analytics, and reading ROI/ROAS against sales goals across 50+ GCC/MENA "
        "markets. And my home turf is Retail & E-commerce: at Alibaba's Miravia I managed 42 key accounts to +30% "
        "GMV QoQ as a consultative advisor while owning the Flash Sales P&L reporting to the CEO; I run a Shopify "
        "store end-to-end (CRO); and I onboard brands across UAE quick-commerce (Noon, Talabat, Careem, Deliveroo). "
        "That is exactly the advertiser world — marketplaces, beauty, fashion, quick commerce — this vertical serves."
    ),
    "body_paragraph_2": (
        "On the post-sale motion the role is built on, I grow client relationships through regular strategic business "
        "reviews, optimisation and product adoption, and I run creator-led social at scale (25–50 creators per "
        "campaign) — TikTok-Shop-adjacent commerce. I'm also AI-native, building tooling that makes campaign "
        "planning, analysis and reporting faster. I'll be candid about one genuine gap: my measurement depth is on "
        "the web side (Meta Pixel, Google Analytics, funnel and conversion analysis) rather than app MMPs like "
        "Appsflyer or Adjust — but tracking logic is tracking logic, I ramp fast on new tooling, and I'd close that "
        "gap quickly. The core this role rewards — hands-on campaign management, optimisation and A/B testing, "
        "consultative account growth and Retail & E-commerce fluency — is exactly what I do."
    ),
    "closing_paragraph": (
        "I'd love to walk the team through how I'd build and optimise a full-funnel plan for a Retail & E-commerce "
        "advertiser on TikTok — from measurement setup to the business review. I'm bilingual (Spanish native / "
        "English C1), based in Dubai and available immediately. Thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="tiktok-csm-retail-ecom-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.tiktok.com/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "TikTok Client Solutions Manager Retail Ecommerce",
             "via": "LinkedIn / TikTok Careers",
             "source_posting": "Client Solutions Manager - Retail and Ecommerce - Türkiye & South Asia"},
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
        "ai_score": 72,
        "ai_tier": "Warm",
        "skills_match": [
            "Hands-on performance campaign management — Meta Ads (FB & IG) & Google Ads, auction, A/B, ROI/ROAS",
            "Deep Retail & E-commerce: Alibaba/Miravia KAM (42 accounts, +30% GMV QoQ), Shopify CRO, UAE quick-commerce",
            "Post-sale consultative account growth + strategic business reviews / QBRs",
            "Web tracking & measurement — Meta Pixel, Google Analytics, funnel/conversion analysis",
            "Creator-led social at scale (25–50 creators/campaign) — TikTok-Shop-adjacent commerce",
            "Cross-functional / ad-ops-style delivery; client & agency relationships",
            "Dubai-based, ES native / EN C1, AI-native",
        ],
        "missing_skills": [
            "Turkish — the source posting (Türkiye & South Asia desk) hard-requires English + Turkish; Paula has ES/EN only",
            "MMP app-tracking (Appsflyer / Adjust) — has web tracking (Pixel, GA), not app-install/MMP measurement",
            "Never sold *for* an ad platform's inventory (advertiser / marketplace-side, not platform ad sales)",
        ],
        "sector_fit": "strong (Retail & E-commerce + performance media + account management all map directly)",
        "seniority_fit": "on-target (revenue-carrying KAM + hands-on performance media maps to CSM)",
        "red_flags": [
            "HARD GATE for the Türkiye desk specifically: Turkish is a stated must ('will be working with Turkish speaking clients'). This package is framed for the general CSM – Retail & Ecommerce role; best used for non-Turkish desks (e.g. MENA).",
            "MMP measurement is a stated must and is a genuine gap — addressed honestly in the cover letter (web tracking strong, ramps fast on MMPs).",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong genuine fit on the Client Solutions Manager – Retail & Ecommerce craft: hands-on performance "
            "campaign management (Meta & Google on the auction, A/B, ROI/ROAS), deep Retail & E-commerce (Alibaba/"
            "Miravia 42 accounts +30% GMV QoQ, Shopify CRO, UAE quick-commerce), consultative post-sale account "
            "growth with business reviews, and creator-led social (TikTok-Shop-adjacent). Two honest gaps: MMP "
            "app-tracking (has web tracking/GA/Pixel) and — for the source Türkiye & South Asia posting only — "
            "Turkish, which Paula does not speak. Package deliberately framed to the general role so it is reusable "
            "for the same CSM Retail & Ecommerce opening on non-Turkish desks."
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

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
