"""One-off: generate Paula's CV + cover letter for four Dubai/remote roles
discovered 2026-08-20 (the ones she picked after liking the Jobgether opening).

Roles:
  1. SMS Realty        — Digital Marketing Manager – AI & Performance Marketing (Dubai)
  2. METABOLIC         — Performance & Growth Manager (Dubai, healthcare)   [STRETCH]
  3. STARTRADER        — Social Media Performance Specialist (Remote)
  4. Unique Wholesale  — Marketing Manager – Skincare Brand (Dubai, EU market) [PAY BELOW FLOOR]

Honest-positioning rules applied throughout (NO fabrication):
  - Only facts present in profile.yaml. Real metrics only (+30% GMV QoQ, 42
    accounts, 6 NPD launches, 25–50 creators, ~40% workload cut via AI).
  - SMS Realty: lead with genuine AI-first + paid performance (Meta/Google Ads)
    craft; state plainly that deep technical SEO/AEO/GEO tooling is a growth
    area, with her daily LLM fluency a real head-start on GEO/AI-search.
  - METABOLIC: 5–8 yr + team-management + healthcare role — the letter is
    transparent that she has neither formal team management nor healthcare
    acquisition; sells the transferable growth craft honestly.
  - STARTRADER: closest analog to Jobgether (remote paid-social specialist);
    letter is honest that her sector is e-commerce/beauty/FMCG, not trading.
  - Unique Wholesale: her Miravia beauty/fragrance work IS the European-market
    experience they require; brand + performance balance mapped truthfully.
  - Per standing rule, NO "no sponsorship needed" claim anywhere. Dubai presence
    + UAE residence visa surfaced only as availability, never as a sponsorship
    statement. Remote role (STARTRADER) surfaces the equipped home setup only.
  - She is currently employed, so letters say "move quickly / short notice",
    never "available immediately".

Fills the real CV + cover-letter templates, converts DOCX->PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers each
job for the dashboard as "CV Ready", and lands packages under output/2026-08-20/.
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

DATE_FOLDER = "2026-08-20"
CONTACT = None  # no named hiring manager on any of the four postings


# ---------------------------------------------------------------------------
# Shared experience scaffold (real dates/context from profile.yaml). Each role
# overrides the bullets to reorder/emphasise by relevance — never inventing.
# ---------------------------------------------------------------------------
def exp(company, role, dates, location, context, bullets):
    return {"company": company, "role": role, "dates": dates,
            "location": location, "context": context, "bullets": bullets}


DOFREEZE = dict(company="DoFreeze LLC", role="Brand & Marketing Manager",
                dates="Oct 2025 – Present", location="Dubai, UAE",
                context="Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries")
MIRAVIA = dict(company="Miravia (Alibaba Group)",
               role="Key Account Manager – Beauty, Fragrances & Fashion",
               dates="Nov 2023 – Oct 2025", location="Madrid, Spain",
               context="Top 5 global e-commerce | 100K+ employees")
GLOVO = dict(company="Glovo", role="Account Manager – XL Accounts",
             dates="Sep 2022 – Nov 2023", location="Madrid, Spain",
             context="Quick-commerce leader | €500M+ revenue | 10K+ employees")
MONDELEZ = dict(company="Mondelez International", role="Trainee – Category Planning",
                dates="Aug 2021 – Aug 2022", location="Madrid, Spain",
                context="Global FMCG | €36B annual revenue | 90K+ employees")


def E(base, bullets):
    return exp(base["company"], base["role"], base["dates"], base["location"],
               base["context"], bullets)


# ===========================================================================
# ROLE 1 — SMS Realty · Digital Marketing Manager – AI & Performance Marketing
# ===========================================================================
SMS = {
    "id": "sms-realty-digital-marketing-manager-ai-performance-2026-08",
    "title": "Digital Marketing Manager – AI & Performance Marketing",
    "company": "SMS Realty",
    "location": "Dubai, UAE",
    "url": "https://to.indeed.com/aa4wcnyyrl7d",
    "source": "indeed",
    "posted_date": "2026-08-13",
    "score": 73, "tier": "Warm",
    "description": (
        "Digital Marketing Manager – AI, Performance Marketing, SEO/AEO/GEO (Dubai, 2–3 yrs). "
        "Explicitly AI-focused: actively use ChatGPT/Claude/Gemini for strategy, content, ads and "
        "optimisation; build AI prompts/workflows/automations. Performance marketing across Google "
        "Ads, Meta Ads, LinkedIn Ads, PMax; plan/optimise on CPL/CPA/CAC/ROAS with structured A/B "
        "testing. SEO (technical/on-page/off-page, SEMrush/Ahrefs, GA4, Search Console), AEO "
        "(featured snippets, schema) and GEO (visibility across ChatGPT, AI Overviews, Perplexity). "
        "Analytics/reporting via GA4 + dashboards. Not suitable for social-posting-only or "
        "traditional-SEO-only profiles."
    ),
    "skills_match": [
        "AI-first marketing — builds Claude/GPT automation for campaign planning, content, research & reporting (their headline requirement)",
        "Daily hands-on use of ChatGPT/Claude/Gemini + reusable prompts, workflows & SOPs",
        "Performance marketing on Meta Ads & Google Ads — audiences, A/B testing, budget & ROAS",
        "Conversion rate optimisation (CRO) on a live Shopify store",
        "KPI/dashboard reporting (CTR, CPA, ROAS) with Power BI / Tableau / Looker",
        "Google Digital Marketing & E-Commerce certified",
    ],
    "missing_skills": [
        "Deep technical SEO tooling (SEMrush/Ahrefs, Core Web Vitals, schema) — growth area, not core",
        "AEO/GEO monitoring platforms (Profound, Otterly.AI) — conceptually strong via LLM fluency, no tool time",
        "GA4 depth (uses Power BI/Tableau/Looker; Google-certified but GA4 not the daily tool)",
    ],
    "sector_fit": "adjacent (real estate — new sector; B2C acquisition + AI craft transfer)",
    "seniority_fit": "on-band (Manager title; 2–3 yr ask, she has 4+)",
    "red_flags": [
        "Heavy SEO/AEO/GEO weighting she'd have to ramp into; posting warns off traditional-SEO-only or social-only profiles (she is neither, but SEO tooling is a genuine gap)",
        "In-person Dubai; real-estate lead-gen sector new to her",
    ],
    "reasoning": (
        "Strong on the two axes the posting weights most — genuine AI-first marketing (her rare "
        "differentiator: real Claude/GPT automation cutting ~40% workload) and hands-on paid "
        "performance (Meta + Google Ads, A/B, ROAS, CRO). Honest gap is the SEO/AEO/GEO half: no "
        "SEMrush/Ahrefs/schema tool time, though daily LLM fluency gives a real head-start on "
        "generative-engine/AI-search visibility. Positioned truthfully — lead with AI + performance, "
        "frame SEO/AEO/GEO as fast-ramp territory."
    ),
    "cv": {
        "headline": ("AI-First Digital Marketing · Performance Marketing (Meta & Google Ads) · "
                     "Generative-AI Automation · CRO, ROAS & Analytics"),
        "professional_summary": (
            "Digital marketer and early adopter of generative AI (Claude, ChatGPT, Gemini) who uses AI "
            "hands-on every day to plan campaigns, build content and automate reporting — exactly the "
            "AI-first profile this role calls for. At DoFreeze I run performance marketing on Meta Ads "
            "(Facebook & Instagram) and Google Ads end-to-end — audience building, creative A/B testing, "
            "budget and spend allocation, ROI/ROAS optimisation — and own a Shopify store I optimise for "
            "conversion rate (CRO). I built an AI-powered marketing automation system (Claude/generative "
            "AI) that automates campaign planning, content, market research and KPI reporting, cutting "
            "manual workload ~40%. Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, conversion and "
            "retention across 42 accounts (+30% GMV QoQ). Business Administration graduate, Google Digital "
            "Marketing & E-Commerce certified, fluent English — keen to extend a data-driven, test-and-"
            "learn approach into SEO, AEO and generative-engine (GEO) search."
        ),
        "experience": [
            E(DOFREEZE, [
                "Built an AI-powered marketing automation system (Claude / generative AI) that automates campaign planning, content creation, market research and KPI reporting — cutting manual workload ~40% and accelerating go-to-market across 50+ markets",
                "Plan and optimise performance campaigns on Meta Ads (Facebook & Instagram) and Google Ads — audience building, creative A/B testing, budget and spend allocation — analysing ROI and ROAS for continuous improvement",
                "Use ChatGPT, Claude and Gemini daily for marketing strategy, ad copy, creative and research, building reusable prompts, workflows and SOPs that scale output",
                "Own and optimise the brand's Shopify store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
                "Produce performance reports and dashboards on CTR, CPA and ROAS, turning campaign data into clear, actionable recommendations for stakeholders",
            ]),
            E(MIRAVIA, [
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across 42 accounts to optimise channel performance and forecasting accuracy",
                "Managed 42 key accounts, achieving +30% GMV growth QoQ through pricing, assortment optimisation and targeted, data-led promotions",
                "Created and led the Beauty Club and Hot on Social projects, boosting brand visibility and engagement across social channels",
            ]),
            E(GLOVO, [
                "Grew strategic accounts through data-led joint planning and bespoke marketing activations, tracking performance to optimise campaigns and order volume",
                "Negotiated and closed high-impact commercial deals, maximising profitability for platform and partners",
            ]),
            E(MONDELEZ, [
                "Ran sell-in/sell-out and promotional-effectiveness analysis, building performance reports that informed spend and commercial planning",
            ]),
        ],
        "skills_brand": ("AI-powered marketing, generative-AI content & campaign automation, prompt "
                         "engineering & AI workflows, full-funnel campaigns, audience & creative testing, "
                         "go-to-market, lead generation"),
        "skills_ecommerce": ("Meta Ads Manager, Google Ads, Facebook & Instagram Ads, LinkedIn Ads, paid "
                             "media, performance marketing, Shopify, conversion rate optimisation (CRO), "
                             "marketing automation, EDM"),
        "skills_commercial": ("customer acquisition, growth, pricing & promotion strategy, stakeholder "
                              "reporting, agency/freelancer management, negotiation"),
        "skills_data": ("ROI & ROAS optimisation, campaign performance & data analysis, KPI tracking (CTR, "
                        "CPA, CPM, ROAS), A/B testing, advertising budget management, dashboards, "
                        "forecasting, Power BI, Tableau, Looker"),
        "skills_tools": ("Generative AI (Claude, ChatGPT, Gemini), Meta Ads Manager, Google Ads, Shopify, "
                         "Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)"),
    },
    "cl": {
        "opening_paragraph": (
            "Your posting is refreshingly specific: you want a marketer who actively uses AI to drive "
            "performance, not a traditional digital or SEO hire. That is exactly how I work. At DoFreeze I "
            "built an AI-powered automation system on Claude and generative AI that runs campaign planning, "
            "content, market research and KPI reporting — cutting manual workload by around 40% — while I "
            "manage paid performance on Meta and Google Ads day to day."
        ),
        "body_paragraph_1": (
            "On the performance side, I plan and optimise Meta Ads (Facebook & Instagram) and Google Ads "
            "end-to-end — audience building and retargeting, structured A/B testing across creative and "
            "copy, budget and spend allocation, and ROI/ROAS optimisation — and I own a Shopify store I "
            "improve for conversion rate (CRO), so I'm accountable for leads and revenue, not impressions. "
            "Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, conversion and retention across 42 "
            "accounts to grow GMV +30% QoQ, so data-led decision-making and dashboard reporting (CTR, CPA, "
            "ROAS) are second nature."
        ),
        "body_paragraph_2": (
            "I'll be straightforward about scope: my deepest craft is AI-powered marketing and paid "
            "performance rather than years of technical SEO tooling (SEMrush/Ahrefs, schema, Core Web "
            "Vitals). But because I work inside LLMs every day, the GEO and AEO shift — structuring content "
            "so a brand surfaces in ChatGPT, Perplexity and Google's AI Overviews — is intuitive territory "
            "for me, and I ramp fast on new tools. I'm Google Digital Marketing & E-Commerce certified, "
            "already based in Dubai on a UAE residence visa, and can move quickly."
        ),
        "closing_paragraph": (
            "I'd welcome the chance to show how I'd combine AI workflows with paid performance to generate "
            "qualified leads for SMS Realty — and how I'd approach the SEO/AEO/GEO build-out with an AI-"
            "first lens. Thank you for considering my application; I'd be glad to walk through a first-90-"
            "days plan."
        ),
    },
}


# ===========================================================================
# ROLE 2 — METABOLIC · Performance & Growth Manager  [STRETCH: 5-8y + team + healthcare]
# ===========================================================================
METABOLIC = {
    "id": "metabolic-performance-growth-manager-2026-08",
    "title": "Performance & Growth Manager",
    "company": "METABOLIC",
    "location": "Dubai, UAE",
    "url": "https://to.indeed.com/aaj9bhtrsdby",
    "source": "indeed",
    "posted_date": "2026-06-03",
    "score": 60, "tier": "Cool",
    "description": (
        "Performance & Growth Manager (Dubai, healthcare/clinic). Hands-on leadership role owning the "
        "patient-acquisition growth engine: full-funnel paid + organic across Meta (CAPI), Google Ads "
        "(PMax), TikTok and SEO; CAC/LTV/ROAS ownership; structured A/B testing; lead nurture across "
        "SMS/WhatsApp/email; CRM (Salesforce/HubSpot); GA4 + Tableau/Mixpanel; AI tools for creative & "
        "research. Requires 5–8 yrs growth/performance with 2+ yrs team management and a track record in "
        "healthcare/clinics/HealthTech patient acquisition, ideally UAE/GCC."
    ),
    "skills_match": [
        "Full-funnel paid media on Meta & Google Ads with ROI/ROAS ownership",
        "Conversion-rate optimisation & click-to-purchase funnel ownership (Shopify)",
        "Structured A/B testing across creative, copy, audiences & placements",
        "AI-driven efficiency — Claude/GPT automation for creative, research & reporting",
        "Commercial reporting to senior leadership (Miravia, CEO-facing; +30% GMV QoQ across 42 accounts)",
        "CRM exposure (Salesforce)",
    ],
    "missing_skills": [
        "5–8 yrs seniority (she has 4+) and no formal people/team-management track record",
        "Healthcare / clinic / patient-acquisition sector experience (hers is e-commerce/beauty/FMCG)",
        "Deep multi-channel attribution stack (GA4/CAPI/Mixpanel) at the level implied",
    ],
    "sector_fit": "weak sector match (healthcare), strong craft match (paid performance/growth)",
    "seniority_fit": "below-band on years + no team management (role wants 5–8 yrs + 2 yrs managing)",
    "red_flags": [
        "Explicit 5–8 yr + 2-yr team-management requirement she doesn't yet meet — genuine stretch",
        "Healthcare patient-acquisition track record required; hers is consumer/e-commerce",
        "Posted 2026-06-03 — may be older / partially filled",
    ],
    "reasoning": (
        "A stretch, applied honestly on her request. The growth craft is a real match — full-funnel "
        "Meta/Google paid media, CAC/ROAS discipline, A/B testing, CRO and AI-driven efficiency, plus "
        "leadership-facing commercial reporting. But the role explicitly wants 5–8 years with 2+ in team "
        "management and a healthcare patient-acquisition record; she has 4+ years, no formal team "
        "management, and an e-commerce/beauty/FMCG background. The letter states both gaps plainly and "
        "sells the transferable engine-building skill and fast category ramp."
    ),
    "cv": {
        "headline": ("Performance & Growth Marketing · Paid Media (Meta & Google Ads) · Full-Funnel CAC & "
                     "ROAS · Generative-AI Automation"),
        "professional_summary": (
            "Performance-focused marketer with 4+ years across E-Commerce, Beauty and FMCG who builds and "
            "optimises paid-media growth engines. At DoFreeze I run full-funnel performance marketing on "
            "Meta Ads (Facebook & Instagram) and Google Ads — audience building, retargeting, creative A/B "
            "testing, budget and spend allocation, ROI/ROAS optimisation — and own a Shopify store I "
            "optimise for conversion (CRO), closing the loop from click to purchase. I built an AI-powered "
            "automation system (Claude/generative AI) that scales campaign planning, creative and "
            "reporting. At Alibaba's Miravia I analysed ROI, ROAS, conversion and retention across 42 "
            "accounts to grow GMV +30% QoQ, reporting commercial narratives to senior leadership. "
            "Commercially grounded, analytical and fast in test-and-learn cycles, comfortable owning "
            "budgets against measurable outcomes."
        ),
        "experience": [
            E(DOFREEZE, [
                "Run full-funnel performance marketing across Meta Ads (Facebook & Instagram) and Google Ads — audience building, retargeting, creative A/B testing and budget allocation — optimising against ROI and ROAS to drive acquisition",
                "Own the Shopify store and its conversion rate (CRO) end-to-end, optimising the journey from paid click to purchase and lifting average order value through data-led merchandising",
                "Built an AI-powered automation system (Claude / generative AI) that streamlines campaign planning, ad-creative variations, market research and KPI reporting — cutting manual workload ~40%",
                "Run continuous A/B tests across creative, messaging, placements and audiences to lower cost per acquisition and sharpen every channel",
                "Produce performance reports on CTR, CPA and ROAS, turning granular campaign data into clear commercial recommendations for stakeholders",
            ]),
            E(MIRAVIA, [
                "Analysed ROI, ROAS, conversion, traffic and retention across 42 accounts to optimise channel performance and forecasting; grew GMV +30% QoQ",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing performance-driven commercial plans aligned to P&L targets",
                "Created and led the Beauty Club and Hot on Social projects, boosting engagement, loyalty and re-engagement across social channels",
            ]),
            E(GLOVO, [
                "Grew strategic accounts through data-led joint planning and bespoke activations, tracking performance to optimise campaigns and order volume",
                "Led cross-functional work across marketing, logistics and support to deliver campaigns and increase order volume",
            ]),
            E(MONDELEZ, [
                "Built sell-in/sell-out and promotional-effectiveness reporting that informed spend and commercial planning",
            ]),
        ],
        "skills_brand": ("growth strategy, full-funnel campaigns, audience & creative testing, generative-AI "
                         "automation, go-to-market, lead generation & qualification, re-engagement & retention"),
        "skills_ecommerce": ("Meta Ads Manager, Google Ads, TikTok Ads, paid media, performance marketing, "
                             "full-funnel acquisition, Shopify, conversion rate optimisation (CRO), "
                             "retargeting, marketing automation"),
        "skills_commercial": ("customer acquisition, growth, unit economics, pricing & promotion, "
                              "stakeholder & leadership reporting, CRM (Salesforce), cross-functional "
                              "collaboration"),
        "skills_data": ("CAC, LTV, ROAS & ROI optimisation, campaign performance analysis, KPI tracking "
                        "(CTR, CPA, CPM), A/B testing, attribution & measurement, budget management, "
                        "forecasting, Power BI, Tableau, Looker"),
        "skills_tools": ("Generative AI (Claude, ChatGPT), Meta Business Suite, Google Ads, Shopify, "
                         "Salesforce, Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)"),
    },
    "cl": {
        "opening_paragraph": (
            "Building an acquisition engine where every dirham is tied to a booked, attended appointment — "
            "not an impression — is exactly the kind of growth problem I find energising. I run full-funnel "
            "performance marketing hands-on: at DoFreeze I own paid media across Meta and Google Ads, "
            "optimise a Shopify funnel for conversion, and hold myself to ROI and ROAS rather than reach."
        ),
        "body_paragraph_1": (
            "Day to day I plan, launch and optimise campaigns with structured A/B testing across creative, "
            "copy, audiences and placements to lower cost per acquisition, and I manage the budget and "
            "spend allocation behind them. I built an AI-powered automation system (Claude/GPT) that "
            "speeds up campaign planning, creative variations and reporting — useful in a fast, high-"
            "expectation environment. At Alibaba's Miravia I analysed ROI, ROAS, conversion and retention "
            "across 42 accounts to grow GMV +30% QoQ and reported the commercial story directly to the "
            "CEO, so translating campaign data into a leadership-ready narrative is familiar ground."
        ),
        "body_paragraph_2": (
            "In fairness, two things sit outside my track record and I'd rather be upfront: I haven't yet "
            "formally managed a team, and my acquisition work has been in e-commerce, beauty and FMCG "
            "rather than healthcare. What I bring instead is the core growth craft — full-funnel paid "
            "media, CAC/ROAS discipline, A/B testing and AI-driven efficiency — a genuinely commercial, "
            "unit-economics mindset, and a fast ramp into new categories. I'm based in Dubai on a UAE "
            "residence visa and can move quickly."
        ),
        "closing_paragraph": (
            "If you're open to a candidate who is strong on the growth engine and ready to grow into the "
            "leadership and healthcare specifics, I'd love to talk through how I'd approach the first "
            "quarter of patient acquisition. Thank you for considering my application."
        ),
    },
}


# ===========================================================================
# ROLE 3 — STARTRADER · Social Media Performance Specialist (REMOTE)
# ===========================================================================
STARTRADER = {
    "id": "startrader-social-media-performance-specialist-2026-08",
    "title": "Social Media Performance Specialist (REMOTE)",
    "company": "STARTRADER",
    "location": "Remote",
    "url": "https://to.indeed.com/aahj9ldcqt92",
    "source": "indeed",
    "posted_date": "2026-08-10",
    "score": 70, "tier": "Warm",
    "description": (
        "Social Media Performance Specialist (Remote, full-time). Lead paid acquisition globally focused "
        "on Meta, TikTok, Instagram and LinkedIn (Google Ads/DSPs/programmatic/affiliate a plus). "
        "High-autonomy hands-on role: develop paid strategies/budgets/KPIs and scaling/kill decisions, "
        "write/adapt ad copy and guide creative, run A/B tests, audience segmentation and optimisation, "
        "own tracking/attribution/GTM/dashboards, integrate AI-driven optimisation. 3+ yrs social paid "
        "acquisition; preferred sectors trading/brokerage/crypto/fintech/iGaming. Application asks "
        "current + expected monthly salary and notice period."
    ),
    "skills_match": [
        "Hands-on paid social on Meta (Facebook & Instagram); TikTok & Instagram in the mix",
        "Audience segmentation, retargeting & lookalike audiences",
        "Ad copywriting & creative concepting for paid social",
        "A/B testing & full-funnel optimisation; budget/scaling decisions on ROAS",
        "AI-driven optimisation — Claude/GPT automation for planning, creative & reporting",
        "Remote-ready: equipped dual-monitor home office; fluent English; high autonomy",
    ],
    "missing_skills": [
        "Trading/brokerage/crypto/fintech sector background (preferred) — hers is e-commerce/beauty/FMCG",
        "LinkedIn Ads (strong on Meta/TikTok/Instagram, lighter on LinkedIn)",
        "Deep GTM/attribution/DSP-programmatic tooling",
    ],
    "sector_fit": "strong craft (paid social/performance), sector preference (finance) not met",
    "seniority_fit": "specialist level — below her Manager seniority (same nuance as the Jobgether role)",
    "red_flags": [
        "Preferred industries are trading/brokerage/crypto/fintech/iGaming — none in her background",
        "Application form asks current & expected salary — keep her AED 20k/month floor in mind",
        "Specialist (not manager) title",
    ],
    "reasoning": (
        "The closest analog to the Jobgether opening she liked: remote, paid-social specialist. Skills "
        "match is strong — Meta/Instagram/TikTok paid acquisition, segmentation/retargeting, ad copy and "
        "creative guidance, A/B testing, budget/scaling decisions and AI-driven optimisation, all hands-"
        "on at DoFreeze. Honest gaps: her sector is e-commerce/beauty/FMCG rather than the preferred "
        "trading/fintech, and LinkedIn Ads/DSP-programmatic are lighter. Title sits below her seniority. "
        "Letter is transparent on sector and leans on remote-readiness and transferable acquisition craft."
    ),
    "cv": {
        "headline": ("Paid Social Performance · Meta, Instagram & TikTok Ads · Creative & A/B Testing · "
                     "ROAS & Analytics"),
        "professional_summary": (
            "Performance marketer who runs paid social acquisition hands-on. At DoFreeze I plan, launch and "
            "optimise paid campaigns across Meta (Facebook & Instagram) and Google Ads — audience research "
            "and segmentation, retargeting, creative concepting and A/B testing, budget and spend "
            "allocation, and ROI/ROAS reporting — with TikTok and Instagram in the mix. I write and adapt "
            "ad copy, guide creative, and make data-led scaling and kill decisions, and I built AI-powered "
            "automation (Claude/GPT) that speeds up campaign planning, creative variations and reporting. "
            "At Alibaba's Miravia I analysed ROI, ROAS, conversion and retention across 42 accounts (+30% "
            "GMV QoQ). Fully set up to work remotely with a dual-monitor home office; fluent English, "
            "comfortable with high autonomy and fast test-and-learn cycles."
        ),
        "experience": [
            E(DOFREEZE, [
                "Plan, launch and optimise paid social campaigns on Meta (Facebook & Instagram) — audience research, segmentation, retargeting and lookalike audiences — with continuous A/B tests across creative, copy and placements to lower CPA and lift ROAS",
                "Write and adapt ad copy and guide creative for paid social, collaborating with design and content to produce scroll-stopping assets",
                "Manage advertising budgets across campaigns, audiences and placements, making data-led scaling and kill decisions on ROI/ROAS",
                "Run Google Ads alongside Meta, with TikTok and Instagram in the content mix, for a full-funnel paid + organic approach",
                "Built AI-powered automation (Claude/GPT) that scales campaign planning, creative variations and performance reporting",
            ]),
            E(MIRAVIA, [
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across 42 accounts to optimise channel performance (+30% GMV QoQ)",
                "Created and led the Hot on Social and Beauty Club projects, growing visibility and engagement across social channels",
            ]),
            E(GLOVO, [
                "Grew strategic accounts via data-led planning and bespoke marketing activations, optimising campaigns and order volume",
            ]),
            E(MONDELEZ, [
                "Built promotional-effectiveness and sell-in/sell-out reporting to inform spend and planning",
            ]),
        ],
        "skills_brand": ("paid social strategy, ad copywriting & creative concepting, full-funnel campaigns, "
                         "audience & creative testing, generative-AI campaign automation, influencer & UGC"),
        "skills_ecommerce": ("Meta Ads Manager, Meta Business Suite, Facebook & Instagram Ads, paid social, "
                             "TikTok Ads, Google Ads, paid acquisition, audience segmentation / retargeting "
                             "/ lookalikes, A/B testing, marketing automation"),
        "skills_commercial": ("customer acquisition, growth, budget ownership, stakeholder reporting, "
                              "cross-team coordination, negotiation"),
        "skills_data": ("ROI & ROAS optimisation, paid-social performance analysis, KPI tracking (CTR, CPA, "
                        "CPM, ROAS), attribution & dashboards, A/B test analysis, budget & scaling "
                        "decisions, Power BI, Tableau, Looker"),
        "skills_tools": ("Meta Ads Manager, Meta Business Suite, Google Ads, Generative AI (Claude, "
                         "ChatGPT), Shopify, Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)"),
    },
    "cl": {
        "opening_paragraph": (
            "A hands-on, high-autonomy role where paid-social strategy meets execution is exactly where I "
            "do my best work. At DoFreeze I run Meta, Instagram and TikTok acquisition end-to-end every "
            "week — from audience research and creative through A/B testing, budget scaling and ROAS "
            "reporting — so shaping campaign performance and driving ROI across markets is my day-to-day."
        ),
        "body_paragraph_1": (
            "I develop the paid-media strategy, budgets and KPIs, then make the scaling and kill decisions "
            "the numbers point to. I write and adapt ad copy and guide creative, run structured A/B tests "
            "across audiences, creative and placements, and keep a close eye on tracking and dashboards so "
            "attribution stays honest. I've also integrated AI-driven optimisation into the workflow — "
            "Claude/GPT automation that speeds up planning, creative variations and reporting. At Alibaba's "
            "Miravia I analysed ROI, ROAS, conversion and retention across 42 accounts to grow GMV +30% "
            "QoQ, so I'm comfortable owning performance with minimal oversight."
        ),
        "body_paragraph_2": (
            "One honest note: my paid-social experience is in e-commerce, beauty and FMCG rather than "
            "trading, brokerage or fintech — so I'd be learning your product and audience, though the "
            "acquisition mechanics, creative testing and attribution discipline transfer directly. I'm "
            "fully equipped for remote, full-time work with a dedicated dual-monitor home office, fluent "
            "in English, and used to coordinating across design and content teams asynchronously."
        ),
        "closing_paragraph": (
            "I'd welcome the chance to show how I'd build, test and scale global paid-social campaigns for "
            "STARTRADER — and I'm happy to share detail on channels, budgets and the results I've driven. "
            "Thank you for considering my application."
        ),
    },
}


# ===========================================================================
# ROLE 4 — Unique Wholesale · Marketing Manager – Skincare  [PAY UP TO AED 11k — below floor]
# ===========================================================================
UNIQUE = {
    "id": "unique-wholesale-marketing-manager-skincare-2026-08",
    "title": "Marketing Manager - Skincare brand",
    "company": "Unique Wholesale and Distributions Limited",
    "location": "Dubai, UAE",
    "url": "https://to.indeed.com/aatszkb4z296",
    "source": "indeed",
    "posted_date": "2026-07-22",
    "score": 68, "tier": "Warm",
    "description": (
        "Marketing Manager – Skincare Brand (Dubai, in-person). Lead brand development, positioning and "
        "identity for a skincare brand across the EUROPEAN market at a fast-growing start-up. Brand "
        "strategy, guidelines, tone of voice, new-product launches; integrated marketing across paid "
        "media, email, SEO, social, influencer, PR and e-commerce; acquisition/retention/loyalty; budget "
        "& ROI; go-to-market; agency/retailer/distributor relationships. Requires 5+ yrs in brand + "
        "marketing (ideally skincare/beauty/premium) AND European skincare/beauty market experience "
        "(explicitly essential). Pay: up to AED 11,000/month. Urgent / immediate start."
    ),
    "skills_match": [
        "European beauty-market experience — 2 yrs managing beauty/fragrance/fashion accounts in Spain (Miravia)",
        "Brand strategy, positioning, identity & tone of voice",
        "NPD end-to-end — 6 launches (brief, packaging, pricing, go-to-market)",
        "Influencer marketing built from zero to 25–50 creators/campaign, plus sampling & seeding",
        "E-commerce & Shopify (CRO), paid media (Meta & Google), EDM/CRM",
        "Beauty & Fragrances specialisation; +30% GMV QoQ across 42 accounts",
    ],
    "missing_skills": [
        "Pure skincare-specific brand-building (hers spans beauty/fragrance categories + NPD — adjacent)",
        "5+ yrs brand+marketing (she has 4+, weighted to beauty/e-commerce)",
    ],
    "sector_fit": "strong (Beauty & Fragrances, European market) — direct on their essential requirement",
    "seniority_fit": "on-band (Manager); slightly under the 5-yr ask but strong beauty/brand depth",
    "red_flags": [
        "Pay up to AED 11,000/month — roughly HALF Paula's AED 20,000/month floor (major flag)",
        "In-person Dubai for a brand targeting the European market; urgent/immediate-start expectation while she is employed",
        "Start-up: scope and stability to verify",
    ],
    "reasoning": (
        "Genuinely strong sector/skills fit: the posting makes European skincare/beauty market experience "
        "an explicit must-have, and Paula's two years at Alibaba's Miravia managing beauty and fragrance "
        "brands for European consumers answers it directly — alongside end-to-end NPD, brand identity, "
        "an influencer programme built from zero, and Shopify/e-commerce. The blocker is money: the "
        "posting caps pay at AED 11k/month, about half her AED 20k floor, so this is materially below "
        "band and worth a deliberate decision before submitting. CV/letter map the beauty + brand + "
        "performance blend truthfully; salary is a conversation for the form/screen, not the letter."
    ),
    "cv": {
        "headline": ("Brand & Marketing Manager · Beauty & Fragrances · European Market · NPD, Influencer "
                     "& E-Commerce Growth"),
        "professional_summary": (
            "Brand and marketing manager with 4+ years across Beauty, Fragrances, Fashion and FMCG, "
            "including hands-on experience in the European beauty market. At Alibaba's Miravia (Madrid) I "
            "managed 42 key accounts across beauty, fragrances and fashion — growing GMV +30% QoQ and "
            "creating the Beauty Club and Hot on Social brand projects — so I know European beauty "
            "consumers, trends and buying behaviour first-hand. At DoFreeze I now lead brand and marketing "
            "end-to-end: 6 NPD launches (brief, packaging, pricing, go-to-market), a Shopify store I "
            "optimise for conversion, an influencer programme I built from zero to 25–50 creators per "
            "campaign, and paid media on Meta and Google Ads. I balance brand-building — strategy, identity "
            "and tone of voice — with performance: acquisition, retention and ROI. Business Administration "
            "graduate (E-Commerce & Fashion specialisation), native Spanish and fluent English, based in "
            "Dubai."
        ),
        "experience": [
            E(DOFREEZE, [
                "Lead NPD end-to-end for 6 product launches — brief, packaging, pricing and go-to-market — across GCC, MENA, Asia, Europe, USA and Africa",
                "Own the brand work end-to-end: strategy, positioning, identity and tone of voice, keeping consistency across packaging, campaigns and communications",
                "Built and scaled an influencer marketing programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign — plus sampling and seeding to drive awareness, UGC and sell-out",
                "Own and optimise the brand's Shopify e-commerce store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate and average order value",
                "Plan and optimise paid media on Meta and Google Ads (audience building, creative A/B testing, EDM), analysing ROI/ROAS for continuous improvement",
                "Manage A&P budgets and go-to-market across 50+ markets, working with creative teams, designers and content creators on brand assets",
            ]),
            E(MIRAVIA, [
                "Managed 42 key accounts across beauty, fragrances and fashion in the European (Spanish) market, achieving +30% GMV growth QoQ through pricing, assortment and targeted promotions",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months, including official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Created and led the Beauty Club and Hot on Social projects, boosting brand visibility, engagement and loyalty and positioning Miravia as a beauty and lifestyle destination",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO on commercial plans aligned to P&L",
            ]),
            E(GLOVO, [
                "Onboarded fashion and lifestyle brands as Glovo built its Retail vertical, with tailored launch campaigns and promotions",
                "Negotiated and closed high-impact commercial deals maximising profitability for platform and partners",
            ]),
            E(MONDELEZ, [
                "Supported NPD launches (Milka Spread, Mini Suchard) with sell-in/sell-out and promotional analysis",
            ]),
        ],
        "skills_brand": ("brand strategy, brand positioning & identity, tone of voice, NPD end-to-end, "
                         "product launches, go-to-market, influencer marketing, sampling & seeding, PR, "
                         "omnichannel campaigns, A&P budget management"),
        "skills_ecommerce": ("Shopify, e-store management, conversion rate optimisation (CRO), Meta Ads "
                             "(Facebook & Instagram), Google Ads, social media, EDM/CRM, influencer & UGC, "
                             "marketing automation"),
        "skills_commercial": ("customer acquisition, retention & loyalty, pricing & promotion, key account "
                              "management, distributor & retailer relationships, market & competitor "
                              "research, go-to-market"),
        "skills_data": ("ROI & ROAS, KPI tracking, campaign & consumer-behaviour analysis, P&L awareness, "
                        "forecasting, Power BI, Tableau, Looker"),
        "skills_tools": ("Shopify, Meta Ads Manager, Google Ads, Generative AI (Claude, ChatGPT), Canva, "
                         "Power BI, Tableau, Looker, Salesforce, Microsoft Office (Expert)"),
    },
    "cl": {
        "opening_paragraph": (
            "Building a skincare brand for the European market is a brief I can speak to from both sides. "
            "For two years at Alibaba's Miravia I managed beauty and fragrance brands for European "
            "consumers — learning the market's trends and buying behaviour first-hand — and I now build "
            "brands end-to-end at DoFreeze, from identity through go-to-market. Your start-up's ambition "
            "to grow a skincare brand across Europe is exactly the kind of build I want to lead."
        ),
        "body_paragraph_1": (
            "At DoFreeze I own brand strategy, positioning, identity and tone of voice, and I run NPD "
            "end-to-end — six launches through brief, packaging, pricing and go-to-market across 50+ "
            "markets. I built our influencer programme from zero to 25–50 creators per campaign with "
            "sampling and seeding, and I own the Shopify store and its conversion rate. At Miravia I "
            "managed 42 beauty, fragrance and fashion accounts to +30% GMV QoQ and created the Beauty Club "
            "and Hot on Social brand projects — so I balance brand-building with the performance and "
            "commercial results a scaling business needs."
        ),
        "body_paragraph_2": (
            "What I'd bring to a fast-moving start-up is exactly that blend: a marketer who builds the "
            "brand — identity, packaging, tone — and is equally comfortable owning paid media, e-commerce, "
            "influencer and the ROI behind them, with generative-AI automation (Claude/GPT) to move faster "
            "on content and campaigns. My hands-on beauty and fragrance work is adjacent to pure skincare, "
            "but the brand-building, European-market and launch craft transfer directly. I'm based in Dubai "
            "on a UAE residence visa and able to move quickly."
        ),
        "closing_paragraph": (
            "I'd love to talk through how I'd shape the brand's positioning and a first go-to-market for "
            "the European market. Thank you for considering my application — I'm keen to help build this "
            "from the ground up."
        ),
    },
}


ROLES = [SMS, METABOLIC, STARTRADER, UNIQUE]


# ---------------------------------------------------------------------------
# Plumbing (mirrors scripts/_gen_jobgether_paid_media_meta.py)
# ---------------------------------------------------------------------------
def make_job(role: dict) -> Job:
    return Job(
        id=role["id"], title=role["title"], company=role["company"],
        location=role["location"], url=role["url"], source=role["source"],
        description=role["description"],
        raw={"note": f"Prepared 2026-08-20 from Indeed listing ({role['url']})"},
    )


def register_in_dashboard(role: dict, job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id, "title": job.title, "company": job.company,
        "location": job.location, "url": job.url, "source": job.source,
        "description": job.description,
        "salary_raw": None, "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": role["posted_date"], "raw": job.raw,
        "ai_score": role["score"], "ai_tier": role["tier"],
        "skills_match": role["skills_match"], "missing_skills": role["missing_skills"],
        "sector_fit": role["sector_fit"], "seniority_fit": role["seniority_fit"],
        "red_flags": role["red_flags"],
        "ats_keywords": [], "reasoning": role["reasoning"],
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "CV Ready",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
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
    for role in ROLES:
        job = make_job(role)
        register_in_dashboard(role, job)

        cv_docx = cv._fill_template(role["cv"], job)
        cv_pdf = _to_pdf_soffice(cv_docx)
        print("OK_CV", cv_pdf)

        cl_docx = cl._fill_template(role["cl"], job, CONTACT)
        cl_pdf = _to_pdf_soffice(cl_docx)
        print("OK_CL", cl_pdf)

        final_dir = _relocate_to_dated_folder(cv_pdf.parent.parent)
        print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
