#!/usr/bin/env python3
"""One-off runner: CV + cover letter for the 5 Indeed jobs found 2026-05-29.

The LLM provider is ``chatqueue`` (no direct API key), so instead of parking
requests on the queue we feed pre-authored content straight into the generators
via ``llm.override(...)``. The author of that content is Claude (this session),
which is exactly the model the generator prompts target. Output is redirected
into ``output/2026-05-29/<Company> - <Role>/`` by overriding ``output_dir``.

All content below is drawn faithfully from profile.yaml — no invented metrics.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops import llm
from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import generate_cover_letter, generate_cv

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger("run_2026_05_29")

# Redirect all generator output into today's dated folder.
settings.output_dir = ROOT / "output" / "2026-05-29"
settings.output_dir.mkdir(parents=True, exist_ok=True)

# Real experience context lines (from profile.yaml), reused verbatim.
CTX = {
    "DoFreeze": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
    "Miravia": "Top 5 global e-commerce | Alibaba Group | 100K+ employees",
    "Glovo": "Quick-commerce leader | EUR 500M+ revenue | 10K+ employees",
    "Mondelez": "Global FMCG | EUR 36B annual revenue | 90K+ employees",
    "Massimo Dutti": "Inditex Group flagship premium fashion brand | Hands-on retail floor",
}

# Reusable experience blocks (bullets reworded/reordered per job below).
def dofreeze(bullets):
    return {"company": "DoFreeze LLC", "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present", "location": "Dubai, UAE",
            "context": CTX["DoFreeze"], "bullets": bullets}

def miravia(role, bullets):
    return {"company": "Miravia / AliExpress (Alibaba Group)", "role": role,
            "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain",
            "context": CTX["Miravia"], "bullets": bullets}

def glovo(bullets):
    return {"company": "Glovo", "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023", "location": "Madrid, Spain",
            "context": CTX["Glovo"], "bullets": bullets}

def mondelez(bullets):
    return {"company": "Mondelez International", "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022", "location": "Madrid, Spain",
            "context": CTX["Mondelez"], "bullets": bullets}

def massimo(bullets):
    return {"company": "Massimo Dutti (Inditex)", "role": "Sales Associate – Las Rozas Village",
            "dates": "Jun 2018 – Jun 2019", "location": "Madrid, Spain",
            "context": CTX["Massimo Dutti"], "bullets": bullets}


# ===================================================================
# JOB DEFINITIONS  (job + my authored CV content + my authored CL)
# ===================================================================

JOBS = []

# ---- 1. Henkel — Trade & Shopper Marketing Manager – GCC ----
JOBS.append({
    "job": Job(
        id="indeed_henkel_trade_shopper",
        title="Trade & Shopper Marketing Manager - GCC",
        company="Henkel",
        location="Dubai, UAE",
        url="https://to.indeed.com/aalbww9d8jcp",
        source="indeed",
        description=(
            "Develop and execute GCC trade and shopper marketing strategies aligned with brand "
            "and commercial objectives. Translate category and shopper insights into channel and "
            "customer plans. Drive Perfect Store execution. Lead annual trade activation-calendar "
            "planning. Work closely with Key Account Managers and Sales. Design shopper activation "
            "programs and promotions. Support NPD launches via go-to-market planning. Manage trade "
            "marketing budgets with focus on ROI. 4-6 years in Trade/Shopper/Category/Sales within "
            "FMCG. Strong understanding of GCC Modern Trade and Traditional Trade channels."
        ),
    ),
    "analysis": JobAnalysis(score=95, tier="Hot",
        skills_match=["trade marketing", "shopper marketing", "category management", "key account management", "NPD", "modern trade", "ROI"],
        missing_skills=[], sector_fit="FMCG", seniority_fit="Manager — strong fit",
        red_flags=[], ats_keywords=["trade marketing", "shopper marketing", "GCC", "modern trade", "Perfect Store", "key account", "NPD", "ROI", "category"],
        reasoning="Near-exact match: trade & shopper marketing FMCG in GCC."),
    "cv": {
        "headline": "Trade & Shopper Marketing Manager · FMCG · GCC · Key Account & Category",
        "professional_summary": (
            "Trade and shopper marketing professional with 4+ years across FMCG, beauty and e-commerce, "
            "currently leading Brand & Marketing for DoFreeze across 50+ GCC, MENA and global markets. "
            "Proven at turning shopper insight into channel and customer plans, driving modern-trade and "
            "quick-commerce execution, and managing A&P budgets to ROI alongside key-account and sales teams."
        ),
        "experience": [
            dofreeze([
                "Develop trade and shopper marketing plans by channel across 50+ markets, supporting key-account strategy and category management with the sales team",
                "Integrated brands into UAE modern trade and quick-commerce (Noon, Careem, Talabat, Deliveroo) — onboarding, listings, promotional mechanics and retail execution",
                "Own A&P budget allocation and commercial planning, analysing ROI and ROAS across channels to maximise efficiency",
                "Lead NPD end-to-end for 6 launches (brief, packaging, pricing, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa",
                "Represent brands at international trade fairs, opening distributor relationships and expanding GCC market coverage",
            ]),
            miravia("Key Account Manager – Beauty, Fragrances & Fashion", [
                "Managed 42 key accounts, achieving +30% GMV growth QoQ via pricing strategy, assortment optimisation and targeted promotions",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months through trend-driven assortment and promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, executing commercial plans aligned to P&L targets",
                "Analysed ROI, ROAS, conversion and retention to optimise channel performance and forecasting accuracy",
            ]),
            glovo([
                "Managed strategic key accounts and drove GMV growth through data-led planning and bespoke marketing activations",
                "Helped build Glovo's retail vertical, onboarding partners and expanding the marketplace beyond food delivery",
                "Negotiated and closed high-impact commercial deals maximising profitability for partners and platform",
            ]),
            mondelez([
                "Conducted sell-in/sell-out analysis and evaluated promotional effectiveness for the chocolate category",
                "Identified growth opportunities and contributed to NPD launches including Milka Spread and Mini Suchard",
                "Built performance reports informing category and trade decisions",
            ]),
        ],
        "skills_brand": "trade marketing, shopper marketing, go-to-market, NPD end-to-end, A&P budget management, brand strategy, omnichannel campaigns",
        "skills_ecommerce": "quick-commerce, Noon, Talabat, Careem, Deliveroo, retail execution, e-store management, process automation",
        "skills_commercial": "key account management, category management, modern trade, general trade, distributor management, pricing strategy, assortment planning, planogram, negotiation, forecasting",
        "skills_data": "sell-in/sell-out, ROI, ROAS, P&L management, KPI tracking, Nielsen, Kantar, Looker",
        "skills_tools": "SAP, Salesforce, Nielsen, Kantar, Looker, Planorama, Microsoft Office (Expert)",
    },
    "cl": {
        "opening_paragraph": (
            "Henkel's strength in Modern Trade and its Perfect Store ambition across the GCC are exactly the "
            "kind of channel and shopper challenges I work on every day. As Brand & Marketing Manager at a "
            "Dubai-based FMCG distributor operating in 50+ markets, I would welcome the chance to bring that "
            "hands-on GCC trade experience to your portfolio."
        ),
        "body_paragraph_1": (
            "I build trade and shopper marketing plans by channel and translate them into customer plans with "
            "the sales team — the core of this role. At Miravia (Alibaba) I managed 42 key accounts and grew "
            "GMV +30% QoQ through pricing, assortment and promotions, and led category expansion as PIC "
            "Fragrances, onboarding 30+ stores in two months. At DoFreeze I run A&P budgets to ROI and lead "
            "NPD go-to-market end-to-end across six launches."
        ),
        "body_paragraph_2": (
            "What sets me apart for the GCC specifically: hands-on integration of brands into UAE modern trade "
            "and quick-commerce (Noon, Talabat, Careem, Deliveroo), a category-planning foundation from "
            "Mondelez (sell-in/sell-out, promo effectiveness), and the fact that I am already based in Dubai on "
            "a UAE residence visa — no relocation or sponsorship needed. I work bilingually in Spanish and English."
        ),
        "closing_paragraph": (
            "I would love to discuss how my GCC trade and shopper experience can support Henkel's category "
            "growth and retailer partnerships. I am available for an interview at your convenience and can start "
            "immediately. Thank you for your consideration."
        ),
    },
})

# ---- 2. Huda Beauty — Assistant Manager, Global Brand Marketing ----
JOBS.append({
    "job": Job(
        id="indeed_hudabeauty_global_brand",
        title="Assistant Manager, Global Brand Marketing",
        company="Huda Beauty",
        location="Dubai, UAE",
        url="https://to.indeed.com/aazlq2j9gpgz",
        source="indeed",
        description=(
            "Support development and execution of 360 marketing campaigns — messaging, paid media assets, "
            "in-store assets, e-commerce content, press materials and influencer activations for hero and "
            "sub-hero product launches. Coordinate cross-functional teams. Collaborate with Creative, Product "
            "and Commercial. Track campaign performance and post-campaign analysis. Support global teams. "
            "5+ years in a similar role; beauty industry an advantage. Passion for beauty and cosmetics a must."
        ),
    ),
    "analysis": JobAnalysis(score=86, tier="Hot",
        skills_match=["360 campaigns", "influencer marketing", "e-commerce content", "NPD launches", "omnichannel", "beauty"],
        missing_skills=[], sector_fit="Beauty & Fragrances", seniority_fit="Assistant Manager — slight step but brand+sector ideal",
        red_flags=[], ats_keywords=["brand marketing", "360 campaign", "influencer", "product launch", "e-commerce content", "beauty", "go-to-market"],
        reasoning="Beauty global brand — her sweet spot; influencer + launches match strongly."),
    "cv": {
        "headline": "Brand & Marketing Manager · Beauty & Fragrances · Influencer & E-Commerce",
        "professional_summary": (
            "Brand and marketing professional with 4+ years across beauty, fragrances, FMCG and e-commerce, "
            "passionate about building brands consumers love. Currently leading Brand & Marketing for DoFreeze, "
            "running 360 launches end-to-end and an influencer programme scaled from zero to 25–50 creators per "
            "campaign. Trained on beauty and fragrance at Alibaba's Miravia, with global, omnichannel reach."
        ),
        "experience": [
            dofreeze([
                "Lead NPD end-to-end for 6 product launches — brief, packaging, messaging, pricing and go-to-market — across 50+ markets",
                "Built and scaled the influencer marketing programme from zero, managing 25–50 influencers per campaign to drive awareness and sell-out",
                "Manage e-commerce content, UX and promotional mechanics across the store and UAE quick-commerce platforms (Noon, Talabat, Careem, Deliveroo)",
                "Develop omnichannel campaigns and analyse KPIs, ROI and ROAS across paid media, social and EDM",
            ]),
            miravia("Key Account Manager – Beauty, Fragrances & Fashion", [
                "Created and led the Beauty Club and Hot on Social projects, boosting brand visibility, loyalty and positioning Miravia as a beauty and lifestyle destination",
                "Managed 42 beauty, fragrance and fashion accounts, achieving +30% GMV growth QoQ through assortment and targeted promotions",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months, including Arabian fragrances",
                "Analysed ROI, ROAS, conversion and retention to optimise campaign and channel performance",
            ]),
            glovo([
                "Onboarded fashion, beauty and lifestyle brands as Glovo built out its retail vertical beyond food delivery",
                "Managed strategic key accounts and drove GMV growth through data-led planning and bespoke marketing activations",
            ]),
            mondelez([
                "Evaluated promotional effectiveness and contributed to NPD launches including Milka Spread and Mini Suchard",
                "Conducted sell-in/sell-out analysis and built performance reports for the chocolate category",
            ]),
        ],
        "skills_brand": "brand strategy, 360 campaigns, influencer marketing, NPD end-to-end, go-to-market, shopper marketing, A&P budget management",
        "skills_ecommerce": "e-store management, e-commerce content, quick-commerce, Noon, Talabat, Careem, Deliveroo, Instagram, TikTok, EDM, UX optimisation",
        "skills_commercial": "key account management, category management, assortment planning, pricing strategy, modern trade, negotiation",
        "skills_data": "ROI, ROAS, KPI tracking, conversion analysis, P&L management, sell-in/sell-out",
        "skills_tools": "Canva, Google Ads, Salesforce, Looker, Kantar, Nielsen, Microsoft Office (Expert)",
    },
    "cl": {
        "opening_paragraph": (
            "Huda Beauty redefined what a beauty brand born in Dubai could become globally, and its purpose-led, "
            "community-first approach is precisely the kind of brand I want to help grow. With four years building "
            "beauty and fragrance brands across e-commerce and FMCG, supporting your Global Brand Marketing team "
            "would be a natural fit."
        ),
        "body_paragraph_1": (
            "This role lives on 360 campaigns, launches and influencer activations — my day-to-day. At DoFreeze I "
            "lead NPD end-to-end for six launches and built an influencer programme from zero to 25–50 creators per "
            "campaign. At Miravia (Alibaba) I created the Beauty Club and Hot on Social projects and grew 42 beauty, "
            "fragrance and fashion accounts +30% GMV QoQ, giving me a sharp sense of what converts in beauty."
        ),
        "body_paragraph_2": (
            "Beyond campaign execution, I bring e-commerce content and UAE quick-commerce fluency (Noon, Talabat, "
            "Careem, Deliveroo), a data-led approach to ROI and ROAS, and genuine passion for the category. I am "
            "already in Dubai on a UAE residence visa and work bilingually in Spanish and English — useful for a brand "
            "operating across global markets."
        ),
        "closing_paragraph": (
            "I would be thrilled to contribute to Huda Beauty's hero and sub-hero launches and global campaign "
            "calendar. I am available to interview whenever suits and can start without notice constraints. Thank you "
            "for considering my application."
        ),
    },
})

# ---- 3. Chic Le Frique — Key Account Manager (Wholesale & E-commerce) ----
JOBS.append({
    "job": Job(
        id="indeed_chiclefrique_kam",
        title="Key Account Manager (Wholesale & E-commerce)",
        company="Chic Le Frique Fashion",
        location="Dubai, UAE",
        url="https://to.indeed.com/aafhvzglgcx7",
        source="indeed",
        description=(
            "Own and grow relationships with key retail partners. Drive sell-through, manage stock performance, "
            "ensure strong brand representation across partner platforms. Track weekly sales, sell-through and "
            "stock levels; drive replenishment and stock optimisation. Align pricing, markdowns and promotional "
            "strategies. Support seasonal drops and product launches. Oversee product uploads (imagery, "
            "descriptions, pricing). Prepare weekly/monthly performance reports. 3-6 years in wholesale, key "
            "account management or e-commerce, fashion preferred."
        ),
    ),
    "analysis": JobAnalysis(score=82, tier="Hot",
        skills_match=["key account management", "e-commerce", "sell-through", "pricing", "assortment", "fashion"],
        missing_skills=[], sector_fit="Fashion / Retail", seniority_fit="Manager — strong fit",
        red_flags=[], ats_keywords=["key account", "wholesale", "e-commerce", "sell-through", "pricing", "markdowns", "product uploads", "fashion"],
        reasoning="KAM + e-commerce + fashion combines three of her pillars (Miravia + Inditex)."),
    "cv": {
        "headline": "Key Account Manager · Fashion & E-Commerce · Wholesale & Retail",
        "professional_summary": (
            "Commercial and key-account professional with 4+ years across fashion, beauty and e-commerce, "
            "Inditex-trained at the start of her career. Grew 42 key accounts +30% GMV QoQ at Alibaba's Miravia "
            "through pricing, assortment and sell-through management, and now owns e-commerce content and "
            "commercial planning at DoFreeze. Analytical, executional and fluent in online retail mechanics."
        ),
        "experience": [
            dofreeze([
                "Manage and optimise the e-commerce store — content, product listings, UX, conversion and promotional mechanics — and own A&P budget and commercial planning",
                "Integrated brands into UAE retail and quick-commerce platforms (Noon, Careem, Talabat, Deliveroo), managing listings, pricing and promotional execution",
                "Develop pricing, assortment and trade plans by channel, supporting key-account strategy across 50+ markets",
            ]),
            miravia("Key Account Manager – Beauty, Fragrances & Fashion", [
                "Owned day-to-day relationships with 42 key accounts, growing GMV +30% QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Managed sell-through and assortment across beauty, fashion and home, identifying bestsellers and acting on underperforming lines",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, aligning markdowns and promotions to P&L targets",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months",
            ]),
            glovo([
                "Part of the team that built Glovo's retail vertical — onboarding fashion and lifestyle brands and expanding the marketplace into apparel and non-food",
                "Managed strategic key accounts and supported fashion-partner integration, driving GMV through data-led planning",
                "Negotiated and closed commercial deals maximising profitability for partners and platform",
            ]),
            massimo([
                "First-hand Inditex retail operations, visual merchandising standards and store cadence at a flagship factory outlet",
                "Customer-facing sales, styling and shop-floor management — foundation in fashion retail and premium brand presentation",
            ]),
        ],
        "skills_brand": "brand presentation, visual merchandising, go-to-market, seasonal launches, promotional planning",
        "skills_ecommerce": "e-store management, product uploads, listings & content, quick-commerce, Noon, Talabat, Careem, Deliveroo, UX optimisation, conversion",
        "skills_commercial": "key account management, wholesale, sell-through management, pricing strategy, markdowns, assortment planning, stock optimisation, distributor management, negotiation, forecasting",
        "skills_data": "sell-in/sell-out, KPI tracking, conversion, inventory turnover, ROI, P&L management",
        "skills_tools": "Salesforce, SAP, Looker, Nielsen, Microsoft Office (Expert), Canva",
    },
    "cl": {
        "opening_paragraph": (
            "Chic Le Frique sits right at the intersection of fashion, wholesale and e-commerce — the exact mix I "
            "have spent my career in, from Inditex on the shop floor to managing fashion and beauty accounts at "
            "Alibaba's Miravia. I would love to help own and grow your key retail partnerships."
        ),
        "body_paragraph_1": (
            "Driving sell-through, stock performance and brand representation across partners is what I do best. At "
            "Miravia I owned 42 key accounts and grew GMV +30% QoQ through pricing, assortment and markdown "
            "strategy, acting weekly on bestsellers and underperformers. I also manage product uploads, listings and "
            "content at DoFreeze, so the e-commerce side of this role is second nature."
        ),
        "body_paragraph_2": (
            "I started my career Inditex-trained at Massimo Dutti, giving me an instinct for premium fashion "
            "presentation and retail cadence, and I helped build Glovo's retail vertical onboarding fashion brands. "
            "I am already based in Dubai on a UAE residence visa — no relocation needed — and work bilingually in "
            "Spanish and English."
        ),
        "closing_paragraph": (
            "I would welcome the chance to discuss how I can drive sell-through and grow Chic Le Frique's wholesale "
            "and e-commerce accounts. I am available to interview at your convenience and can start immediately. "
            "Thank you for your consideration."
        ),
    },
})

# ---- 4. Expert (Rituals) — E-Commerce Manager ----
JOBS.append({
    "job": Job(
        id="indeed_expert_rituals_ecommerce",
        title="E-Commerce Manager",
        company="Expert (Rituals)",
        location="Dubai, UAE",
        url="https://to.indeed.com/aa4ysf24fwph",
        source="indeed",
        description=(
            "Lead and grow the digital presence of Rituals in the region. Develop and execute e-commerce "
            "strategies to drive traffic, conversions and revenue. Oversee end-to-end online customer "
            "experience (UI/UX, site performance, digital merchandising). Manage multi-million USD digital "
            "marketing budgets across paid search, social, affiliate and email. Ensure seamless omni-channel "
            "integration. Analyse performance data and market trends. 8-10 years B2C e-commerce, omni-channel "
            "retail or high-growth digital. Salary up to AED 20,000."
        ),
    ),
    "analysis": JobAnalysis(score=72, tier="Warm",
        skills_match=["e-commerce strategy", "conversion optimisation", "UX", "paid media", "ROAS", "omnichannel"],
        missing_skills=["8-10 years seniority (Paula has 4+)"], sector_fit="Beauty & Fragrances / Omnichannel Retail",
        seniority_fit="Stretch-up — role asks 8-10 yrs senior", red_flags=["seniority gap", "salary ceiling at floor"],
        ats_keywords=["e-commerce", "conversion", "UX", "paid search", "affiliate", "omnichannel", "ROAS", "digital merchandising"],
        reasoning="Rituals is beauty/fragrance (her sweet spot) but seniority ask is above her tenure."),
    "cv": {
        "headline": "E-Commerce Manager · Omnichannel Retail · Beauty & Fragrances",
        "professional_summary": (
            "E-commerce and brand professional with 4+ years scaling online channels across beauty, fragrance and "
            "FMCG. Manages the DoFreeze e-store end-to-end — content, UX, conversion and promotions — and grew 42 "
            "beauty and fragrance accounts +30% GMV QoQ at Alibaba's Miravia. Data-led on paid media ROI/ROAS, with "
            "deep UAE quick-commerce and omnichannel experience."
        ),
        "experience": [
            dofreeze([
                "Manage and optimise the e-commerce store end-to-end — content, UX, conversion rate and promotional mechanics",
                "Analyse e-commerce KPIs, ROI and ROAS across paid media, social and EDM to drive continuous performance improvement",
                "Integrated brands into UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), managing listings, promotions and omnichannel retail execution",
                "Own A&P budget allocation and led digital transformation, automating marketing and commercial workflows for scalable growth",
            ]),
            miravia("Key Account Manager (E-Commerce) – Beauty, Fragrances & Fashion", [
                "Grew 42 beauty, fragrance and fashion accounts +30% GMV QoQ through pricing, assortment and promotion strategy on a top-5 global e-commerce platform",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, executing commercial plans to P&L targets",
                "Continuously analysed conversion, traffic, retention, ROI and ROAS to optimise channel performance",
            ]),
            glovo([
                "Drove GMV growth on a quick-commerce platform through data-led planning and bespoke activations",
                "Helped build the retail vertical, onboarding brands and expanding the marketplace beyond food delivery",
            ]),
            massimo([
                "Inditex retail operations and visual merchandising experience underpinning an omnichannel view of premium retail",
            ]),
        ],
        "skills_brand": "digital merchandising, brand consistency, go-to-market, promotional planning, omnichannel campaigns",
        "skills_ecommerce": "e-store management, conversion optimisation, UX optimisation, paid search, Google Ads, social, affiliate, EDM, quick-commerce, Noon, Talabat, Careem, Deliveroo, process automation",
        "skills_commercial": "pricing strategy, assortment planning, key account management, category management, customer acquisition & retention",
        "skills_data": "ROAS, ROI, conversion analysis, traffic & retention, KPI tracking, P&L management, Looker",
        "skills_tools": "Google Ads, Looker, Salesforce, SAP, Nielsen, Kantar, Microsoft Office (Expert)",
    },
    "cl": {
        "opening_paragraph": (
            "Rituals' blend of premium beauty and home fragrance with a strong omni-channel experience is exactly "
            "the kind of brand I love growing online. Having run e-commerce for beauty and fragrance brands across "
            "the region, I would be excited to help scale Rituals' digital presence."
        ),
        "body_paragraph_1": (
            "I manage the DoFreeze e-store end-to-end — UX, conversion, content and promotions — and analyse ROI "
            "and ROAS across paid media, social and EDM. At Miravia (Alibaba) I grew 42 beauty and fragrance accounts "
            "+30% GMV QoQ on a top-5 global platform, optimising conversion, traffic and retention. I am also fluent "
            "in UAE quick-commerce (Noon, Talabat, Careem, Deliveroo) and omnichannel execution."
        ),
        "body_paragraph_2": (
            "In full honesty, my hands-on tenure is four-plus years rather than the eight to ten listed — but the "
            "depth is there: full P&L exposure, multi-channel budget management and a track record of measurable "
            "online growth. I am Dubai-based on a UAE residence visa, bilingual in Spanish and English, and Google "
            "E-Commerce and Digital Marketing certified."
        ),
        "closing_paragraph": (
            "If you are open to a candidate who combines beauty-category fluency with strong e-commerce execution, I "
            "would welcome a conversation about Rituals' growth plans. I am available to interview at your convenience. "
            "Thank you for considering my application."
        ),
    },
})

# ---- 5. PlaceUp — Category Manager ----
JOBS.append({
    "job": Job(
        id="indeed_placeup_category",
        title="Category Manager",
        company="PlaceUp",
        location="Dubai, UAE",
        url="https://to.indeed.com/aasyg67j4hjg",
        source="indeed",
        description=(
            "Manage and grow assigned product categories across FMCG retail and e-commerce. Develop category "
            "plans for sales, margin and market share across traditional retail and e-commerce. Optimise "
            "assortment, pricing and promotions offline and online (marketplaces, D2C, e-retailers). Coordinate "
            "with e-commerce teams on listings, content and digital merchandising. Ensure brand visibility at POS "
            "via planograms and displays. Negotiate with suppliers. 4-6 years in category management, trade "
            "marketing or product management in FMCG and/or e-commerce."
        ),
    ),
    "analysis": JobAnalysis(score=70, tier="Warm",
        skills_match=["category management", "trade marketing", "assortment", "pricing", "promotions", "FMCG", "e-commerce", "planogram"],
        missing_skills=[], sector_fit="FMCG / Consumer Goods", seniority_fit="4-6 yrs — good fit",
        red_flags=[], ats_keywords=["category management", "assortment", "pricing", "promotions", "planogram", "FMCG", "e-commerce", "market share", "supplier negotiation"],
        reasoning="Direct target title; FMCG + e-commerce category role matching Mondelez + Miravia background."),
    "cv": {
        "headline": "Category Manager · FMCG & E-Commerce · Trade & Shopper Marketing",
        "professional_summary": (
            "Category and commercial professional with 4+ years across FMCG, beauty and e-commerce, blending "
            "category planning at Mondelez with key-account growth at Alibaba's Miravia (+30% GMV QoQ across 42 "
            "accounts). Now leads trade, assortment and channel plans at DoFreeze across 50+ markets, fluent in both "
            "modern trade and online marketplaces."
        ),
        "experience": [
            dofreeze([
                "Develop trade and shopper marketing plans by channel, supporting category management and key-account strategy across 50+ markets",
                "Manage assortment, pricing and promotional mechanics across the e-store and UAE quick-commerce (Noon, Talabat, Careem, Deliveroo)",
                "Lead NPD end-to-end (brief, pricing, go-to-market) and own A&P budget allocation with ROI focus",
            ]),
            miravia("Key Account Manager – Beauty, Fragrances & Fashion", [
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via trend-driven assortment and promotions",
                "Grew 42 accounts +30% GMV QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Analysed conversion, ROI and ROAS to optimise category performance and forecasting on a top-5 e-commerce platform",
            ]),
            mondelez([
                "Conducted sell-in/sell-out analysis and evaluated promotional effectiveness for the chocolate category",
                "Identified growth opportunities and contributed to NPD launches including Milka Spread and Mini Suchard",
                "Built category performance reports informing assortment and trade decisions",
            ]),
            glovo([
                "Managed strategic key accounts and drove GMV growth through data-led planning",
                "Helped expand the retail marketplace beyond food into new categories",
            ]),
        ],
        "skills_brand": "trade marketing, shopper marketing, go-to-market, NPD end-to-end, promotional planning",
        "skills_ecommerce": "online marketplaces, e-store management, listings & content, digital merchandising, quick-commerce, Noon, Talabat, Careem, Deliveroo",
        "skills_commercial": "category management, assortment planning, pricing strategy, planogram, supplier negotiation, key account management, modern trade, distributor management, forecasting",
        "skills_data": "sell-in/sell-out, market share, ROI, ROAS, KPI tracking, P&L management, Nielsen, Kantar",
        "skills_tools": "Nielsen, Kantar, Looker, SAP, Salesforce, Planorama, Microsoft Office (Expert)",
    },
    "cl": {
        "opening_paragraph": (
            "Growing categories across both FMCG retail and e-commerce is precisely where my experience sits — from "
            "category planning at Mondelez to fragrance category expansion at Alibaba's Miravia. PlaceUp's dual "
            "offline-and-online focus is a strong match for how I work."
        ),
        "body_paragraph_1": (
            "I build category and assortment plans, optimise pricing and promotions, and drive market share. At "
            "Miravia I led category expansion as PIC Fragrances, onboarding 30+ stores in two months and growing 42 "
            "accounts +30% GMV QoQ. At Mondelez I owned sell-in/sell-out analysis and promotional effectiveness for "
            "the chocolate category, and at DoFreeze I manage assortment and trade plans across 50+ markets."
        ),
        "body_paragraph_2": (
            "I bring both sides PlaceUp needs: modern-trade and planogram fundamentals plus hands-on online "
            "marketplace and UAE quick-commerce experience (Noon, Talabat, Careem, Deliveroo). I am Dubai-based on a "
            "UAE residence visa, data-led on ROI and market share, and bilingual in Spanish and English."
        ),
        "closing_paragraph": (
            "I would welcome the opportunity to discuss how I can grow PlaceUp's categories across retail and "
            "e-commerce. I am available to interview at your convenience and can start immediately. Thank you for your "
            "consideration."
        ),
    },
})


# ===================================================================
# RUN
# ===================================================================

def run():
    results = []
    for spec in JOBS:
        job = spec["job"]
        analysis = spec["analysis"]
        logger.info("=== %s @ %s ===", job.title, job.company)

        cv_path = None
        cl_path = None
        try:
            with llm.override({"submit_cv_content": spec["cv"]}):
                cv_path = generate_cv(job, analysis)
        except Exception as exc:
            logger.error("CV failed for %s: %s", job.company, exc)
        try:
            with llm.override({"submit_cover_letter": spec["cl"]}):
                cl_path = generate_cover_letter(job, analysis)
        except Exception as exc:
            logger.error("CL failed for %s: %s", job.company, exc)

        results.append((job.company, job.title, cv_path, cl_path))

    print("\n\n========== RESULT ==========")
    for company, title, cv, cl in results:
        print(f"\n{company} — {title}")
        print(f"  CV: {cv}")
        print(f"  CL: {cl}")


if __name__ == "__main__":
    run()
