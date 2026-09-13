"""One-off: generate Paula's CV + cover letter for Jobgether
"Digital Marketing & E-Commerce Growth Manager" — a full-time, fully REMOTE role
based in the UAE, listed by Jobgether on behalf of an unnamed partner company.
Commercially-focused digital marketing: turn online visibility into measurable
revenue across SEO/AEO/GEO, paid ads, email, landing pages and e-commerce
optimisation, generating qualified B2B leads and online sales.

Why this is a strong, honest fit (the spine is Paula's exact day-to-day):
  - E-commerce growth IS her core. At DoFreeze she owns the Shopify store
    end-to-end (catalogue, descriptions, imagery, category structure, pricing,
    promotions, checkout), lifting conversion rate (CRO) and average order value
    (AOV) through data-led merchandising — the heart of this brief.
  - Paid media + email + landing pages + analytics: she runs Google Ads and Meta
    Ads, plans email/EDM lifecycle campaigns, builds high-converting landing
    pages, and tracks ROI/ROAS/conversion/traffic in dashboards — all named
    accountabilities here.
  - Large product catalogues / many SKUs across 50+ markets (DoFreeze: Befit,
    Eurocake, Flair) and 42 accounts at Miravia — directly matches "experience
    managing large product catalogues or businesses with multiple SKUs."
  - Genuine B2B commercial angle for "qualified B2B leads, bulk orders, reseller
    and wholesale opportunities, account applications": her Key Account /
    distributor / modern-trade work at Alibaba's Miravia (42 accounts, +30% GMV
    QoQ, onboarded 30+ distributor-run stores) and DoFreeze distributor networks
    is exactly selling to and through businesses, resellers and wholesale.
  - AEO/GEO (Answer Engine & Generative Engine Optimisation) is an emerging edge
    and Paula's generative-AI work (Claude/GPT for content, campaign planning and
    analytics) is a rare, genuine advantage for optimising toward AI-generated
    search results.

Honest positioning (NO fabrication):
  - Experience length: the ad asks for a minimum of 5 years. Paula has ~4+ years
    of professional marketing/commercial experience (Mondelez 2021 → present).
    Framed truthfully as "4+ years" / "nearly five years" — never inflated to 5+.
  - Technical SEO tooling: she does content/organic and is genuinely ahead on
    AEO/GEO via generative AI, but deep technical-SEO tools (SEMrush, Ahrefs,
    Screaming Frog, structured-data/Search Console audits) are a development area,
    not a claimed strength. Positioned as "strong on content/organic + AEO/GEO;
    building depth on technical SEO tooling", never as owned Ahrefs/Screaming Frog.
  - Google Shopping / Performance Max / Google Merchant Center: she runs Google
    Ads genuinely; Shopping/PMax/Merchant Center feeds framed as ready-to-run
    extensions of her paid practice, not overclaimed as owned.
  - Email platforms (Klaviyo, Mailchimp, HubSpot, ActiveCampaign): she has real
    email/EDM + lifecycle-automation and CRM (Salesforce) experience, but not
    those specific platforms. Positioned as "email marketing & automation; quick
    to adopt Klaviyo / HubSpot / Mailchimp", never as Klaviyo/HubSpot experience.
  - E-commerce platforms: she is Shopify-native (not WooCommerce/Magento/
    BigCommerce). Shopify strength stated; other platforms framed as transferable.
  - B2B lead generation: her B2B is COMMERCIAL (key accounts, distributors,
    resellers, wholesale/bulk) — not a classic inbound MQL→SQL demand-gen /
    lead-scoring pipeline. The transferable funnel/paid/CRO/analytics craft and
    real B2B commercial relationships are claimed; an owned inbound-ABM pipeline
    is not.
  - Australian B2B / e-commerce market experience is listed as "an advantage" —
    Paula does not have it; not claimed. The partner may be Australian, so the
    letter notes she is set up for flexible remote collaboration (no permanent
    night-shift commitment baked in).
  - "Excellent written English" — she is C1 professional (stated as such), not
    native, with strong commercial copywriting.
  - NO "no sponsorship needed" claim — the visa is employer-sponsored (standing
    rule); the CV header only states "UAE Residence Visa".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-26/.
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

COMPANY = "Jobgether"
TITLE = "Digital Marketing & E-Commerce Growth Manager"
DATE_FOLDER = "2026-08-26"

# Jobgether posts on behalf of an unnamed partner company — no hiring manager named.
CONTACT = None

JOB_DESCRIPTION = """\
Digital Marketing & E-Commerce Growth Manager — Jobgether (on behalf of a partner
company). United Arab Emirates. Fully remote, full-time.

A commercially focused role for a digital marketing professional who can turn
online visibility into measurable revenue growth. Own strategies across SEO, AEO,
GEO, paid advertising, email marketing, landing pages and e-commerce optimisation.
Focus on generating qualified B2B leads, increasing online sales, and strengthening
customer acquisition and retention across diverse customer segments and extensive
product catalogues, connecting marketing activity directly to commercial outcomes.
Combines strategic ownership with hands-on execution, experimentation, analytics and
continuous optimisation. Work measured by revenue, conversions and sustainable growth.

Accountabilities:
- Develop and execute an inbound marketing strategy generating qualified B2B
  enquiries, quote requests, bulk orders, reseller opportunities, account
  applications and online sales.
- Build targeted campaigns and lead-generation funnels for different industries,
  customer segments, product categories and purchasing needs.
- Partner with sales and management to track leads from enquiry through conversion,
  improve lead quality, and introduce lead scoring, automated follow-up and nurturing.
- Own organic search across SEO, Answer Engine Optimisation and Generative Engine
  Optimisation — keyword research, competitor analysis, technical optimisation,
  structured data, internal linking, content architecture and search-intent analysis.
- Optimise product, category, service and location pages for rankings and visibility
  across traditional and AI-generated search results.
- Develop commercially focused content (pricing, bulk purchasing, product
  comparisons, specifications, delivery, FAQs).
- Create and optimise high-converting landing pages for retail, wholesale, reseller,
  corporate and government audiences.
- Improve CTAs, forms, account applications and checkout journeys through testing
  and behavioural analysis.
- Manage and optimise the e-commerce platform: product information, descriptions,
  specifications, imagery, category structures, pricing, stock, promotions and
  customer journeys.
- Increase average order value, purchase frequency and repeat revenue via bundles,
  volume offers, cross-selling, upselling, promotions and abandoned-cart recovery.
- Plan, launch and optimise paid advertising across Google Search, Shopping,
  Performance Max, remarketing, display and relevant Meta/LinkedIn channels.
- Manage ad budgets and improve cost per qualified lead, CAC and ROAS.
- Build segmented email marketing and automated lifecycle campaigns (enquiries,
  quote follow-ups, abandoned carts, account applications, repeat-order reminders,
  reactivation, launches, promotions).
- Analyse campaign, CRM, website and sales data to identify what generates revenue
  rather than vanity metrics; build weekly/monthly performance dashboards; establish
  clear attribution between digital activity and revenue.

Requirements:
- Minimum 5 years in digital marketing, e-commerce, inbound marketing or lead gen.
- Proven track record of measurable online revenue and/or qualified B2B leads.
- Strong practical SEO, AEO, GEO, content strategy and search-intent optimisation.
- Ability to build and optimise sales-focused landing pages and conversion funnels.
- Hands-on Google Ads, Google Shopping, remarketing and performance paid campaigns.
- Strong e-commerce CRO and customer-journey understanding (acquisition → repeat).
- Email marketing, CRM, segmentation and marketing automation.
- Strong analytics (Google Analytics 4, Search Console, ad platforms, CRM/sales data).
- Experience managing large product catalogues / multiple SKUs highly desirable.
- Excellent written English and strong commercial copywriting.
- Tools valued: Shopify, WooCommerce, Magento, BigCommerce, Google Merchant Center,
  Microsoft Ads, Meta Ads Manager, SEMrush, Ahrefs, Screaming Frog, Klaviyo,
  Mailchimp, HubSpot, ActiveCampaign, Canva, Adobe, heat-mapping / testing tools.
- Australian B2B or e-commerce market experience is an advantage.
- Strong portfolio of measurable results (e-commerce revenue, B2B lead gen, SEO,
  landing-page performance, ad management, customer-acquisition optimisation).

Benefits: fully remote work-from-home; significant ownership over digital growth and
e-commerce performance; broad ownership across SEO/AEO/GEO, paid media, e-commerce,
CRO, email, automation and analytics; high autonomy; data-driven marketing systems.

How Jobgether works: AI-powered matching reviews applications against core
requirements and shares a shortlist with the hiring company; interviews and final
decisions are managed by the partner's internal team.
"""

ATS = [
    "Digital Marketing", "E-Commerce Growth", "e-commerce", "growth marketing",
    "online revenue", "revenue growth", "conversion rate optimisation", "CRO",
    "average order value", "AOV", "customer acquisition", "retention",
    "customer journey", "checkout optimisation", "abandoned cart",
    "cross-sell", "upsell", "bundles", "promotions", "repeat purchase",
    "SEO", "AEO", "Answer Engine Optimisation", "GEO",
    "Generative Engine Optimisation", "organic search", "search intent",
    "content strategy", "landing pages", "conversion funnels", "A/B testing",
    "experimentation", "heat-mapping",
    "paid advertising", "Google Ads", "Google Shopping", "Performance Max",
    "remarketing", "display", "Meta Ads", "Facebook Ads", "Instagram Ads",
    "LinkedIn Ads", "ROAS", "cost per lead", "CPL", "CAC", "budget management",
    "email marketing", "EDM", "lifecycle campaigns", "marketing automation",
    "segmentation", "CRM", "lead generation", "lead nurturing", "lead scoring",
    "B2B", "wholesale", "reseller", "bulk orders", "quote requests",
    "Google Analytics 4", "GA4", "Google Search Console", "dashboards",
    "reporting", "revenue attribution", "data-driven",
    "Shopify", "WooCommerce", "Magento", "BigCommerce", "Google Merchant Center",
    "Klaviyo", "Mailchimp", "HubSpot", "ActiveCampaign", "SEMrush", "Ahrefs",
    "Screaming Frog", "Canva", "product catalogue", "SKUs", "merchandising",
    "generative AI", "AI automation", "commercial copywriting", "remote",
]

CV_CONTENT = {
    "headline": (
        "Digital Marketing & E-Commerce Growth Manager · Shopify, CRO & AOV · "
        "Paid Media (Google & Meta Ads), SEO/AEO/GEO & Email · Revenue-Led Analytics"
    ),
    "professional_summary": (
        "Commercially-driven digital marketing and e-commerce growth manager with 4+ years turning online "
        "visibility into measurable revenue across E-Commerce, FMCG, Beauty and Fashion. At DoFreeze I own the "
        "Shopify store end-to-end — catalogue, product content, category structure, pricing, promotions, UX and "
        "checkout — lifting conversion rate (CRO) and average order value through data-led merchandising, and "
        "grow demand across paid media (Google Ads, Meta Ads), SEO/organic, email/EDM lifecycle campaigns, "
        "landing pages and partnerships while managing budgets to maximise ROI and ROAS. I manage large product "
        "catalogues across 50+ markets and track conversion, traffic, AOV and revenue in dashboards, tying every "
        "activity to commercial outcomes rather than vanity metrics. Earlier, as a Key Account Manager at "
        "Alibaba's Miravia and Glovo I sold to and through businesses, resellers and distributors — growing GMV "
        "+30% QoQ across 42 accounts — a genuine B2B commercial angle for qualified-lead, wholesale and reseller "
        "growth. Early adopter of generative AI (Claude/GPT), a rare edge for AEO/GEO and AI-generated search. "
        "Excellent written English (C1), fully set up for remote work."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "FMCG e-commerce & distribution | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the Shopify e-commerce store end-to-end — product information, descriptions, imagery, category structures, pricing, stock, promotions and checkout journey — lifting conversion rate (CRO) and average order value through data-led merchandising across a large multi-brand catalogue",
                "Grow online revenue through segmented promotions, bundles, cross-sell/upsell and abandoned-cart recovery, and build high-converting landing pages for retail, wholesale and reseller audiences, improving CTAs, forms and checkout via continuous A/B testing",
                "Plan and optimise paid advertising across Google Ads and Meta Ads (Facebook & Instagram) — audience building, creative testing, remarketing — managing budgets to improve cost per lead, CAC and ROAS (Google Shopping / Performance Max / Merchant Center feeds ready to extend)",
                "Build segmented email marketing and automated lifecycle campaigns (EDM) — launches, promotions, repeat-order reminders, cart recovery and reactivation — to grow purchase frequency and repeat revenue",
                "Own organic and content strategy (search-intent-led product, category and FAQ content) and apply generative AI (Claude/GPT) to optimise toward AI-generated search results (AEO/GEO) — cutting content and campaign-planning workload ~40%",
                "Analyse campaign, sales and website data to identify what drives revenue, building weekly/monthly dashboards on conversion, traffic, AOV, ROAS and marketing-attributed revenue with clear attribution to commercial outcomes",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts across a large multi-SKU catalogue, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions — a direct B2B commercial angle (selling to and through business partners and resellers)",
                "Led category expansion as PIC Fragrances, onboarding 30+ new distributor- and reseller-run stores in two months via performance-driven promotions and trend-led products",
                "Owned the Flash Sales channel (Beauty, Fashion & Home) and continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Generated and converted B2B enquiries into partnerships — prospecting, qualifying and closing high-impact commercial deals — and grew order volume through data-led joint planning and bespoke activations",
                "Supported building Glovo's Retail vertical, onboarding new brand and reseller partners with tailored launch campaigns and promotions across marketing, logistics and support",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, building performance reports that informed pricing, assortment and commercial planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) with data-driven analysis, turning category and sales data into actionable recommendations",
            ],
        },
    ],
    "skills_brand": (
        "e-commerce growth strategy, conversion rate optimisation (CRO), average order value (AOV) growth, "
        "landing-page & funnel optimisation, content & search-intent strategy, AEO / GEO (generative-AI search), "
        "promotions, bundles, cross-sell & upsell, campaign management, generative-AI content"
    ),
    "skills_ecommerce": (
        "Shopify (end-to-end store, catalogue, checkout), paid media (Google Ads, Meta Ads), remarketing, "
        "email marketing / EDM & lifecycle automation, abandoned-cart recovery, SEO / organic, landing pages, "
        "A/B testing & experimentation, Google Shopping / Performance Max / Merchant Center (ready to run), "
        "quick to adopt Klaviyo / HubSpot / Mailchimp; WooCommerce / Magento transferable"
    ),
    "skills_commercial": (
        "B2B commercial & lead generation, key account management, distributor / reseller / wholesale management, "
        "modern trade, sales alignment & cross-functional collaboration, pricing & promotion strategy, "
        "negotiation, budget management, large multi-SKU catalogue management"
    ),
    "skills_data": (
        "revenue attribution, conversion & funnel analysis, AOV & repeat-purchase analysis, ROI, ROAS, "
        "cost per lead (CPL), CAC, dashboards & performance reporting, KPI tracking, Google Analytics 4 (GA4), "
        "Google Search Console, Looker, Tableau, Power BI"
    ),
    "skills_tools": (
        "Shopify, Google Ads, Meta Ads Manager, Meta Business Suite, Google Analytics 4, Google Search Console, "
        "Salesforce (CRM), Looker, Tableau, Power BI, Generative AI (Claude, ChatGPT), Canva, "
        "Microsoft Office — Expert (Excel, PowerPoint, Word); quick to adopt Klaviyo / HubSpot / SEMrush / Ahrefs"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "The Digital Marketing & E-Commerce Growth Manager brief — turn online visibility into measurable "
        "revenue by owning the store, paid, organic, email and landing pages, and connecting every activity to "
        "conversions and sales rather than vanity metrics — describes how I already work. I run e-commerce growth "
        "end-to-end today, I'm analytical and hands-on in equal measure, and I'm fully set up for focused remote work."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze I own the Shopify store end-to-end — catalogue, product content, "
        "category structure, pricing, promotions, UX and checkout — lifting conversion rate (CRO) and average "
        "order value through data-led merchandising, bundles, cross-sell and abandoned-cart recovery. I plan and "
        "optimise paid media (Google Ads, Meta Ads) with remarketing and budgets managed to ROAS and cost per "
        "lead; run segmented email/EDM lifecycle campaigns; build high-converting landing pages for retail, "
        "wholesale and reseller audiences; and track conversion, traffic, AOV and revenue in dashboards with clear "
        "attribution. I manage large product catalogues across 50+ markets, and my generative-AI work (Claude/GPT) "
        "gives me a genuine head start on AEO and GEO — optimising content toward AI-generated search results."
    ),
    "body_paragraph_2": (
        "I'll be straightforward about fit. My B2B experience is commercial rather than a classic inbound "
        "MQL-to-SQL pipeline: as a Key Account Manager at Alibaba's Miravia and Glovo I sold to and through "
        "businesses, distributors and resellers — managing 42 accounts, growing GMV +30% QoQ and onboarding 30+ "
        "reseller-run stores in two months — which maps directly to generating qualified B2B enquiries, bulk and "
        "wholesale orders and reseller opportunities. On tooling, I'm Shopify-native and strong on content, paid "
        "and analytics; I use Salesforce for CRM and run email automation, and I'm quick to pick up Klaviyo, "
        "HubSpot and the technical-SEO stack (SEMrush, Ahrefs, Screaming Frog) — I'd rather be honest about where "
        "I'm deepening than overclaim it. I have close to five years across e-commerce and commercial roles, "
        "excellent written English (C1) and strong commercial copywriting."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to walk through how I'd approach the first 90 days — auditing the store and funnel "
        "for the quickest CRO and AOV wins, prioritising the paid, organic and email bets with the best return, "
        "and standing up the dashboards and experimentation cadence to prove revenue impact fast. I'm set up for "
        "flexible remote collaboration across time zones. Thank you for considering my application — I'd be glad "
        "to share specifics and portfolio examples of the e-commerce growth I've driven."
    ),
}


def make_job() -> Job:
    return Job(
        id="jobgether-digital-marketing-ecommerce-growth-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates · Fully remote",
        url="https://www.linkedin.com/jobs/search/?keywords=Jobgether%20Digital%20Marketing%20E-Commerce%20Growth%20Manager",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Jobgether Digital Marketing & E-Commerce Growth Manager UAE remote",
             "function": "Digital Marketing & E-Commerce Growth (revenue-led, SEO/AEO/GEO + paid + email + CRO)",
             "workplace": "Fully remote (UAE-based)",
             "note": "Jobgether = platform posting on behalf of an unnamed partner company; AI-powered shortlist shared with the hiring company; no hiring manager named; salary not disclosed. 'Australian B2B/e-commerce market experience an advantage' hints the partner may be Australian."},
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
        "salary_raw": "Not disclosed (fully remote, UAE)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 78,
        "ai_tier": "Hot",
        "skills_match": [
            "Owns the Shopify e-commerce store end-to-end today (catalogue, content, pricing, promotions, UX, checkout) — CRO & AOV via data-led merchandising",
            "Grows online revenue with bundles, cross-sell/upsell, abandoned-cart recovery and segmented promotions",
            "Builds high-converting landing pages and conversion funnels; improves CTAs/forms/checkout via A/B testing",
            "Paid media: Google Ads + Meta Ads with remarketing; budgets managed to ROAS / cost per lead / CAC",
            "Email marketing / EDM lifecycle & automation (launches, cart recovery, reactivation, repeat-order)",
            "Organic & content strategy + genuine AEO/GEO edge via generative AI (Claude/GPT) — rare and on-trend",
            "Manages large multi-SKU catalogues across 50+ markets (DoFreeze) and 42 accounts (Miravia)",
            "Revenue-led analytics: conversion, traffic, AOV, ROAS, attribution in dashboards (GA4, Looker)",
            "Genuine B2B commercial angle for qualified leads / wholesale / reseller: KAM + distributor management (+30% GMV QoQ, 30+ reseller stores onboarded)",
            "Excellent written English (C1) + commercial copywriting; fully set up for remote work",
        ],
        "missing_skills": [
            "Minimum 5 years required — Paula has ~4+ years (Mondelez 2021 → present); framed honestly as '4+ years / nearly five', never inflated",
            "Technical-SEO tooling (SEMrush, Ahrefs, Screaming Frog, structured data, Search Console audits) — a development area; she's strong on content/organic + AEO/GEO, quick to deepen (not overclaimed)",
            "Google Shopping / Performance Max / Merchant Center — runs Google Ads genuinely; these framed as ready-to-run extensions, not owned",
            "Email platforms Klaviyo / Mailchimp / HubSpot / ActiveCampaign — has email/EDM + Salesforce CRM; positioned as 'quick to adopt', never as Klaviyo/HubSpot experience",
            "E-commerce platforms WooCommerce / Magento / BigCommerce — she is Shopify-native (transferable, not claimed as owned)",
            "Classic inbound MQL→SQL / lead-scoring demand-gen pipeline — her B2B is commercial (KAM/distributor/reseller/wholesale), not an owned inbound-ABM funnel",
            "Australian B2B / e-commerce market experience ('an advantage') — she does not have it; not claimed",
        ],
        "sector_fit": "strong — e-commerce growth is Paula's exact core (Shopify, CRO, AOV, paid, email, landing pages, large catalogues); the softer edge is B2B inbound lead-gen framing and technical-SEO tooling",
        "seniority_fit": "on-band — Manager-level role matches Paula's current Brand & Marketing Manager seniority (lateral); 5-yr minimum is the one stretch, handled honestly",
        "red_flags": [
            "Minimum 5 years of experience vs Paula's ~4+ — the clearest stated gap; positioned truthfully, not inflated",
            "Heavy SEO/AEO/GEO + technical-SEO tooling emphasis — content/organic and AEO/GEO are genuine strengths, but deep Ahrefs/Screaming Frog/structured-data work is a development area",
            "B2B *inbound* lead-generation focus (quote requests, account applications, lead scoring) vs her B2B *commercial* (KAM/distributor/reseller) background — adjacent, framed honestly",
            "Salary not disclosed — cannot confirm against her 20,000 AED/month floor",
            "Jobgether posts for an unnamed partner (AI-shortlist model); 'Australian market an advantage' hints the partner may be Australian — potential timezone consideration, though role is UAE-based remote",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit — one of the closest matches to Paula's actual day-to-day. The role is a "
            "commercially-focused digital marketing & e-commerce growth manager: own the store and turn visibility "
            "into revenue across SEO/AEO/GEO, paid ads, email, landing pages and CRO, generating qualified B2B "
            "leads and online sales, all measured by conversions and revenue. Paula does the spine of this today at "
            "DoFreeze — owns the Shopify store end-to-end (CRO, AOV, catalogue, pricing, promotions, checkout), runs "
            "Google + Meta Ads with remarketing to ROAS/cost-per-lead, builds email/EDM lifecycle campaigns and "
            "landing pages, and reports revenue-led analytics — over a large multi-SKU catalogue across 50+ markets. "
            "Her generative-AI work is a rare, genuine edge for AEO/GEO (AI-generated search). Her B2B is commercial "
            "(KAM, distributor, reseller, wholesale at Alibaba's Miravia and Glovo: 42 accounts, +30% GMV QoQ, 30+ "
            "reseller stores), which maps to the ad's wholesale/reseller/bulk-order lead generation. Honest gaps: "
            "she has ~4+ years vs the stated 5-year minimum; technical-SEO tooling (SEMrush/Ahrefs/Screaming Frog) "
            "is a development area; Google Shopping/PMax/Merchant Center and Klaviyo/HubSpot are 'ready to adopt' "
            "not owned; she is Shopify-native (not WooCommerce/Magento); classic inbound MQL→SQL lead-scoring is not "
            "owned; and she lacks Australian-market experience. CV + letter lead with the genuine e-commerce growth, "
            "Shopify/CRO/AOV, paid, email and analytics craft plus real B2B commercial relationships, and state the "
            "experience-length, SEO-tooling, platform and inbound-pipeline nuances plainly — no fabricated tooling "
            "or seniority, no native-English or 'no sponsorship needed' claim."
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
