#!/usr/bin/env python3
"""One-off: CV + cover letter for Colgate-Palmolive E-Commerce Manager (2026-06-15).

Same override pattern as _run_2026_06_15.py — content authored from profile.yaml,
no invented metrics. Output into output/2026-06-15/<Company> - <Role>/.
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
from career_ops.discovery.normalize import Job, job_hash
from career_ops.generators import generate_cover_letter, generate_cv

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(message)s", datefmt="%H:%M:%S")

settings.output_dir = ROOT / "output" / "2026-06-15"
settings.output_dir.mkdir(parents=True, exist_ok=True)

CTX = {
    "DoFreeze": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
    "Miravia": "Top 5 global e-commerce | Alibaba Group | 100K+ employees",
    "Glovo": "Quick-commerce leader | EUR 500M+ revenue | 10K+ employees",
    "Mondelez": "Global FMCG | EUR 36B annual revenue | 90K+ employees",
}

job = Job(
    id=job_hash("Ecommerce Manager", "Colgate-Palmolive", "Dubai, United Arab Emirates"),
    title="Ecommerce Manager",
    company="Colgate-Palmolive",
    location="Dubai, United Arab Emirates",
    url="https://jobs.colgate.com/job/Dubai-Ecommerce-Manager-DU/174114-en_US/",
    source="company_site",
    description=(
        "Develop digital commerce strategies with growth ambition, customer prioritization and key "
        "business capabilities. Ensure continuous improvement in eCapabilities for DAM, Content, "
        "Net Sales, P&L and Analytics reporting. Use data and analytics to drive decision-making. "
        "Develop rich content that converts (higher click & conversion). Define metrics for digital "
        "shelf excellence and review via scorecard. Leverage digital to drive demand with a full-funnel "
        "approach. Drive category growth across sub-channels and develop promotion strategy. 360 "
        "marketing communications across digital platforms. Track sales, traffic, marketing spend and "
        "channel performance for eCommerce retailers. Coordinate with agencies. Work with consumer "
        "marketing, retail marketing, key accounts and supply chain. Min 4 years in eCommerce marketing "
        "or account management, preferably multinational FMCG with leading brands."
    ),
)

analysis = JobAnalysis(
    score=88, tier="Hot",
    skills_match=["e-commerce strategy", "digital shelf", "content & conversion", "P&L", "category growth", "key accounts", "data & analytics", "FMCG"],
    missing_skills=[], sector_fit="FMCG / E-commerce", seniority_fit="Min 4 yrs — exact fit",
    red_flags=[], ats_keywords=["eCommerce", "digital shelf", "conversion", "P&L", "category growth", "full funnel", "key accounts", "promotion strategy", "FMCG", "analytics"],
    reasoning="Multinational FMCG e-commerce role at her exact level; digital-shelf + content + P&L + key accounts map 1:1 to her profile.",
)

cv = {
    "headline": "E-Commerce Manager · Digital Commerce · FMCG · Digital Shelf & Key Accounts",
    "professional_summary": (
        "E-commerce professional with 4+ years scaling digital commerce across FMCG, beauty and "
        "quick-commerce. Owns the DoFreeze e-store and digital-shelf execution across UAE retailers "
        "(Noon, Talabat, Careem, Deliveroo), and grew 42 accounts +30% GMV QoQ on Alibaba's Miravia. "
        "Data-led on conversion, ROI/ROAS and P&L, with a category-growth foundation from Mondelez — "
        "a strong fit for multinational FMCG digital commerce."
    ),
    "experience": [
        {"company": "DoFreeze LLC", "role": "Brand & Marketing Manager", "dates": "Oct 2025 – Present",
         "location": "Dubai, UAE", "context": CTX["DoFreeze"], "bullets": [
            "Own digital-shelf execution across UAE e-commerce retailers (Noon, Talabat, Careem, Deliveroo) — listings, content, imagery, pricing and promotional mechanics that drive click and conversion",
            "Manage the Shopify e-store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
            "Plan and optimise full-funnel digital marketing (Meta Ads, Google Ads, social, EDM), tracking traffic, spend, ROI and ROAS by channel and recommending corrective actions",
            "Drive category growth and promotion strategy across sub-channels, owning A&P budget allocation to P&L and ROI",
            "Coordinate agencies and built AI-powered automation (Claude) for content, campaign planning and KPI reporting, cutting manual workload ~40%",
        ]},
        {"company": "Miravia (Alibaba Group)", "role": "Key Account Manager (E-Commerce) – Beauty, Fragrances & Fashion",
         "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain", "context": CTX["Miravia"], "bullets": [
            "Grew 42 key accounts +30% GMV QoQ on a top-5 global e-commerce platform through pricing, assortment and conversion-led promotions",
            "Owned the digital shelf for Beauty, Fashion & Home — content, assortment and promotional execution — and ran the Flash Sales channel to P&L targets",
            "Continuously analysed conversion, traffic, retention, ROI and ROAS to optimise channel performance and forecasting",
            "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via data-led assortment",
        ]},
        {"company": "Glovo", "role": "Account Manager – XL Accounts", "dates": "Sep 2022 – Nov 2023",
         "location": "Madrid, Spain", "context": CTX["Glovo"], "bullets": [
            "Drove GMV growth on a quick-commerce platform through data-led planning and full-funnel activations",
            "Helped build the retail vertical, onboarding brands and expanding the marketplace beyond food delivery",
            "Led cross-functional teams across marketing, operations and logistics to grow order volume",
        ]},
        {"company": "Mondelez International", "role": "Trainee – Category Planning", "dates": "Aug 2021 – Aug 2022",
         "location": "Madrid, Spain", "context": CTX["Mondelez"], "bullets": [
            "Conducted sell-in/sell-out analysis and evaluated promotional effectiveness for the chocolate category",
            "Built category performance reports informing assortment and trade decisions in a multinational FMCG",
            "Contributed to NPD launches including Milka Spread and Mini Suchard",
        ]},
    ],
    "skills_brand": "digital commerce strategy, digital shelf excellence, content that converts, 360 marketing communications, promotion strategy, go-to-market",
    "skills_ecommerce": "e-store management, Shopify, conversion rate optimisation (CRO), full-funnel, digital merchandising, online marketplaces, quick-commerce, Noon, Talabat, Careem, Deliveroo, Meta Ads, Google Ads, EDM",
    "skills_commercial": "key account management, category growth, assortment planning, pricing strategy, customer prioritization, supply-chain coordination, distributor management",
    "skills_data": "digital-shelf scorecards, conversion & click-through, P&L management, Net Sales, ROI, ROAS, traffic & channel analytics, KPI tracking, Looker",
    "skills_tools": "Shopify, Meta Ads Manager, Google Ads, Looker, Salesforce, SAP, Generative AI (Claude), Microsoft Office / Google Suite (Expert)",
}

cl = {
    "opening_paragraph": (
        "Colgate-Palmolive's focus on digital-shelf excellence and content that converts across "
        "e-commerce retailers is exactly the work I do every day. As Brand & Marketing Manager at a "
        "Dubai-based FMCG distributor, I own digital-shelf execution across Noon, Talabat, Careem and "
        "Deliveroo, so stepping into multinational FMCG e-commerce would be a natural progression."
    ),
    "body_paragraph_1": (
        "This role lives on conversion, the digital shelf and category growth — my core. At Alibaba's "
        "Miravia I grew 42 accounts +30% GMV QoQ on a top-5 platform, owning content, assortment and "
        "promotions to P&L targets while analysing conversion, traffic and ROAS. At DoFreeze I run the "
        "Shopify store end-to-end and full-funnel paid media, tracking spend and channel performance to ROI."
    ),
    "body_paragraph_2": (
        "I bring the FMCG foundation Colgate values: category planning from Mondelez (sell-in/sell-out, "
        "promo effectiveness) plus hands-on UAE quick-commerce digital-shelf experience that is rare in "
        "the market. I'm data-led, build AI automation for content and reporting, already based in Dubai "
        "on a residence visa (no sponsorship needed), and bilingual in Spanish and English."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to discuss how I can drive Colgate-Palmolive's digital-shelf and category "
        "growth across e-commerce retailers. I'm available to interview at your convenience and can start "
        "immediately. Thank you for your consideration."
    ),
}

with llm.override({"submit_cv_content": cv}):
    cv_path = generate_cv(job, analysis)
with llm.override({"submit_cover_letter": cl}):
    cl_path = generate_cover_letter(job, analysis)

print("\n========== COLGATE ==========")
print("CV:", cv_path)
print("CL:", cl_path)
