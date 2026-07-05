"""One-off generator for VAULT & Vyonic (DALVE) — Marketing Executive.

LLM auto-gen is dead (no API key). This injects hand-authored, role-adapted
content straight into the DOCX templates via the generators' internal
_fill_template, then converts to PDF — bypassing the Claude call entirely.

Run by the developer (Claude), not Paula.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from career_ops.config import settings

# Write into the dated folder: output/2026-06-23/<position>/01_CV_y_Carta/
settings.output_dir = settings.root / "output" / "2026-06-23"
settings.output_dir.mkdir(parents=True, exist_ok=True)

from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator, cover_letter

JOB = Job.build(
    title="Marketing Executive",
    company="VAULT & Vyonic (DALVE)",
    location="Dubai, UAE",
    url="",
    source="indeed",
    description=(
        "Own the full marketing function across two brands DALVE is building "
        "from the ground up — VAULT, the flagship fitness performance centre "
        "launching Q3 2026, and Vyonic, a performance optimisation ecosystem. "
        "Strategy, paid campaigns, content, community building, influencer "
        "partnerships and pre-launch activation. Work directly with the founding "
        "team with genuine creative ownership. For someone who thinks in "
        "campaigns, moves fast on data, and wants to put two ambitious brands "
        "on the map in Dubai and beyond."
    ),
)

# ── Hand-authored CV content (matches cv_generator._CV_TOOL schema) ──────────
CV_CONTENT = {
    "headline": "Marketing Executive · Brand Builder (0→1) · Paid Campaigns · Content, Influencer & Community · Go-to-Market",
    "professional_summary": (
        "Brand and marketing professional with 4+ years building and launching brands across FMCG, "
        "Beauty, Fashion and E-Commerce. I currently own the full marketing function for DoFreeze's "
        "brand portfolio in Dubai — strategy, paid media, content, influencer and go-to-market — and "
        "I thrive in zero-to-one, founder-led environments where I own the campaign end to end. Track "
        "record: 6 product launches taken from concept to market, an influencer programme scaled from "
        "zero to 25–50 creators per campaign, +30% GMV growth QoQ across 42 accounts, and AI-powered "
        "workflows that turn a brief into a live campaign fast. Already based in Dubai with a UAE "
        "residence visa — ready to drive pre-launch activation from day one."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the full marketing function for the brand portfolio — brand strategy, content, paid media, influencer and go-to-market — operating with end-to-end creative and commercial ownership across 50+ markets",
                "Lead go-to-market for 6 product launches end-to-end (brief, positioning, packaging, pricing, pre-launch activation), taking brands from concept to shelf and online across GCC and MENA",
                "Built and scaled the influencer marketing programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign plus sampling and seeding — driving brand awareness, UGC and community growth",
                "Plan and optimise paid media on Meta Ads (Facebook & Instagram) and Google Ads — audience building, creative A/B testing, social and EDM — managing ROAS and scaling what works fast on data",
                "Own the Shopify e-commerce store end-to-end (catalogue, UX, CRO, collections, checkout), lifting conversion rate and average order value through data-led merchandising",
                "Built an AI-powered marketing system (Claude / generative AI) automating content, campaign planning, market research and KPI reporting — moving from brief to live campaign in a fraction of the time",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions — moving fast on data to hit commercial targets",
                "Created and led the Beauty Club and Hot on Social projects, building community, customer loyalty and brand visibility on the platform",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via strategic, trend-driven promotions",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team that built Glovo's Retail vertical from the ground up — onboarding new brands and launching categories beyond food delivery, a direct parallel to standing brands up pre-launch",
                "Managed strategic key accounts and drove GMV growth through data-led planning and bespoke marketing activations",
                "Led cross-functional teams across marketing, logistics and support to deliver seamless campaigns and grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out analysis and promotional-effectiveness reporting for the chocolate category",
                "Contributed to successful NPD launches including Milka Spread and Mini Suchard",
            ],
        },
    ],
    "skills_brand": "brand strategy, go-to-market, pre-launch activation, influencer marketing, community building, content, NPD end-to-end, sampling & seeding, generative AI campaigns, omnichannel campaigns",
    "skills_ecommerce": "Meta Ads (Facebook & Instagram), Google Ads, paid social, Instagram, TikTok, Pinterest, Shopify, conversion rate optimisation (CRO), marketing automation, EDM, UX optimisation",
    "skills_commercial": "key account management, negotiation, pricing strategy, assortment planning, category management, distributor management, modern trade, forecasting",
    "skills_data": "KPI tracking, ROI, ROAS, P&L management, sell-in/sell-out, AI-assisted analysis & forecasting, Power BI, Tableau, Looker, Salesforce",
    "skills_tools": "Generative AI (Claude, ChatGPT), Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, Canva, Power BI, Salesforce, Microsoft Office (Expert)",
}

# ── Hand-authored cover letter (matches cover_letter._CL_TOOL schema) ────────
CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm writing to apply for the Marketing Executive role building VAULT and Vyonic. Launching a "
        "flagship fitness performance centre and a performance-optimisation ecosystem from the ground "
        "up — and owning how both show up in Dubai — is exactly the kind of zero-to-one, full-ownership "
        "brief I look for. I think in campaigns, I move fast on data, and I'd relish the chance to put "
        "two ambitious brands on the map alongside the founding team."
    ),
    "body_paragraph_1": (
        "In my current role I own the full marketing function for DoFreeze's brand portfolio — strategy, "
        "paid media, content, influencer and go-to-market — so the breadth this role demands is my "
        "day-to-day, not a stretch. I've led 6 product launches end to end, from brief and positioning "
        "through pricing and pre-launch activation; built an influencer programme from zero to 25–50 "
        "creators per campaign with the UGC and community to match; and run Meta and Google paid media "
        "where I scale what the data rewards. Earlier, managing 42 key accounts at Alibaba's Miravia, I "
        "drove +30% GMV growth QoQ — I'm comfortable carrying a number, not just a brand."
    ),
    "body_paragraph_2": (
        "Two things set me apart for a pre-launch build. First, I'm an AI-first marketer: I've built "
        "generative-AI workflows (Claude/GPT) that take a campaign from brief to live in a fraction of "
        "the usual time — invaluable when a small founding team needs to move fast and punch above its "
        "weight. Second, I helped build Glovo's Retail vertical from scratch, onboarding brands and "
        "launching new categories, so standing something up before it exists is familiar ground. I'm "
        "already in Dubai on a UAE residence visa — no sponsorship, no relocation, ready to drive "
        "activation from day one of the Q3 2026 runway."
    ),
    "closing_paragraph": (
        "I'd love to walk the founding team through how I'd approach the pre-launch and first 90 days "
        "for VAULT and Vyonic. I'm available to start quickly and can share campaign work and launch "
        "examples on request. Thank you for your consideration — I'd be excited to help these two "
        "brands make a mark in Dubai and beyond."
    ),
}


def main() -> None:
    cv_docx = cv_generator._fill_template(CV_CONTENT, JOB)
    cv_pdf = cv_generator._to_pdf(cv_docx)
    print("CV:", cv_pdf)

    cl_docx = cover_letter._fill_template(CL_PARAGRAPHS, JOB, contact_name="Founding Team")
    cl_pdf = cover_letter._to_pdf(cl_docx)
    print("CL:", cl_pdf)


if __name__ == "__main__":
    main()
