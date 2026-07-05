#!/usr/bin/env python3
"""One-off: CV + cover letter for Deliveroo Hop Vendor/Category Manager (2026-06-15).

Override pattern, content authored from profile.yaml, no invented metrics.
Output into output/2026-06-15/<Company> - <Role>/.
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
    id=job_hash("Vendor / Category Manager - Deliveroo Hop UAE", "Deliveroo", "Dubai, UAE"),
    title="Vendor / Category Manager - Deliveroo Hop UAE",
    company="Deliveroo",
    location="Dubai, UAE",
    url="https://to.indeed.com/aaw8464gnkln",
    source="indeed",
    description=(
        "Vendor / Category Manager for Deliveroo Hop (24/7 digital supermarket). Own the performance of a "
        "category: range selection, sourcing, pricing, cost and contract negotiations, promotions, "
        "merchandising and marketing campaigns, and manage vendors within the category. Set pricing per "
        "principles; nominate SKUs for promotional campaigns; monitor SKU performance and optimise range; "
        "deep-dive category performance vs plan and drive sustainable growth. Develop and manage relationships "
        "with local and international grocery suppliers; negotiate contracts and terms; analyse vendor "
        "performance; drive media spend with vendors. 3+ years in vendor/category management or buying. "
        "Analytical, strong negotiation, Excel/Gsheets. DIFC, hybrid."
    ),
)

analysis = JobAnalysis(
    score=84, tier="Hot",
    skills_match=["category management", "vendor negotiation", "pricing strategy", "assortment / range", "promotions", "quick-commerce", "data analysis"],
    missing_skills=[], sector_fit="Quick-commerce / FMCG grocery", seniority_fit="3+ yrs — exact fit",
    red_flags=[], ats_keywords=["category management", "vendor management", "pricing", "range selection", "SKU", "promotions", "negotiation", "quick-commerce", "FMCG", "merchandising"],
    reasoning="Quick-commerce category + vendor role at her level; maps to Miravia category/assortment, Glovo partner onboarding and DoFreeze quick-commerce integration.",
)

cv = {
    "headline": "Category Manager · Quick-Commerce & FMCG · Vendor, Range & Pricing",
    "professional_summary": (
        "Category and commercial professional with 4+ years across quick-commerce, e-commerce and FMCG. "
        "Grew 42 accounts +30% GMV QoQ at Alibaba's Miravia through range, pricing and promotions, helped "
        "build Glovo's retail vertical onboarding vendors, and integrates brands into UAE quick-commerce "
        "(Noon, Talabat, Careem, Deliveroo) at DoFreeze. Analytical, negotiation-led and fluent in the "
        "category mechanics that drive sustainable growth."
    ),
    "experience": [
        {"company": "Miravia (Alibaba Group)", "role": "Key Account Manager – Beauty, Fragrances & Fashion",
         "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain", "context": CTX["Miravia"], "bullets": [
            "Owned category performance for 42 accounts, growing GMV +30% QoQ through range selection, pricing strategy, assortment optimisation and targeted promotions",
            "Led category expansion as PIC Fragrances, sourcing and onboarding 30+ new stores in two months via trend-driven range and promotional mechanics",
            "Nominated SKUs for promotional campaigns and the Flash Sales channel, monitoring SKU performance and optimising the range to P&L targets",
            "Analysed conversion, ROI and ROAS to deep-dive category performance vs plan and act on underperformers",
        ]},
        {"company": "Glovo", "role": "Account Manager – XL Accounts", "dates": "Sep 2022 – Nov 2023",
         "location": "Madrid, Spain", "context": CTX["Glovo"], "bullets": [
            "Part of the team that built Glovo's retail vertical — sourcing and onboarding vendors and expanding the marketplace range beyond food delivery",
            "Negotiated and closed commercial contracts and terms with partners, maximising profitability for vendor and platform",
            "Managed vendor relationships and resolved day-to-day issues, driving GMV through data-led range and promotional planning",
            "Led cross-functional teams across marketing, logistics and operations to grow order volume on a quick-commerce platform",
        ]},
        {"company": "DoFreeze LLC", "role": "Brand & Marketing Manager", "dates": "Oct 2025 – Present",
         "location": "Dubai, UAE", "context": CTX["DoFreeze"], "bullets": [
            "Integrate brands into UAE quick-commerce (Noon, Talabat, Careem, Deliveroo) — range listing, pricing, promotional mechanics and merchandising",
            "Manage distributor and supplier relationships and coordinate sourcing across 50+ markets",
            "Own assortment, promotion strategy and A&P budget allocation, tracking ROI by channel",
        ]},
        {"company": "Mondelez International", "role": "Trainee – Category Planning", "dates": "Aug 2021 – Aug 2022",
         "location": "Madrid, Spain", "context": CTX["Mondelez"], "bullets": [
            "Conducted sell-in/sell-out and category performance analysis for the chocolate category in a multinational FMCG",
            "Evaluated promotional effectiveness and built reports informing range and trade decisions",
            "Contributed to NPD launches including Milka Spread and Mini Suchard",
        ]},
    ],
    "skills_brand": "promotion strategy, merchandising, marketing campaigns, go-to-market, range storytelling",
    "skills_ecommerce": "quick-commerce, Deliveroo, Talabat, Noon, Careem, digital merchandising, e-store management, online marketplaces",
    "skills_commercial": "category management, vendor & supplier management, range selection, sourcing, contract & price negotiation, pricing strategy, assortment planning, SKU optimisation, distributor management, forecasting",
    "skills_data": "category performance analysis, SKU performance, sell-in/sell-out, ROI, ROAS, P&L management, KPI tracking, Excel / Google Sheets, Power BI, Tableau, Looker, Nielsen, Kantar",
    "skills_tools": "Excel / Google Sheets, Power BI, Tableau, Looker, Salesforce, SAP, Nielsen, Kantar, Microsoft Office (Expert)",
}

cl = {
    "opening_paragraph": (
        "Deliveroo Hop sits exactly where my experience lives — quick-commerce, category management and "
        "vendor relationships. I already integrate brands into Deliveroo, Talabat, Noon and Careem from the "
        "brand side at DoFreeze, and I helped build Glovo's retail vertical, so owning a Hop category would "
        "be a natural fit."
    ),
    "body_paragraph_1": (
        "Range, pricing, promotions and vendor negotiation are my core. At Alibaba's Miravia I owned category "
        "performance across 42 accounts and grew GMV +30% QoQ through range selection, pricing and SKU-led "
        "promotions, deep-diving performance vs plan. At Glovo I sourced and onboarded vendors and negotiated "
        "commercial contracts, and at Mondelez I built a category-planning foundation (sell-in/sell-out, "
        "promo effectiveness)."
    ),
    "body_paragraph_2": (
        "I'm analytical and comfortable living in spreadsheets and category scorecards, with genuine "
        "quick-commerce fluency that is rare in the market. I am already based in Dubai on a UAE residence "
        "visa — no relocation or sponsorship needed — thrive in fast-paced, ambiguous environments, and work "
        "bilingually in Spanish and English."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to discuss how I can grow a Deliveroo Hop category through smart range, pricing "
        "and vendor partnerships. I'm available to interview at your convenience and can start immediately. "
        "Thank you for your consideration."
    ),
}

with llm.override({"submit_cv_content": cv}):
    cv_path = generate_cv(job, analysis)
with llm.override({"submit_cover_letter": cl}):
    cl_path = generate_cover_letter(job, analysis)

print("\n========== DELIVEROO ==========")
print("CV:", cv_path)
print("CL:", cl_path)
