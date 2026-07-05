#!/usr/bin/env python3
"""One-off: CV + cover letter for Puig — Marketing Graduate Programme (2026-06-17).

Honest positioning: Paula is OVER-qualified (this targets recent grads with ~6
months experience). We do NOT pretend she is a fresh grad — we keep her real
titles, lead on her degree + genuine fragrance passion (Arabian/oud houses), and
the cover letter addresses the over-experience head-on. Every grad-programme task
maps to something she already does at a higher level.
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

settings.output_dir = ROOT / "output" / "2026-06-17"
settings.output_dir.mkdir(parents=True, exist_ok=True)

CTX = {
    "DoFreeze": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
    "Miravia": "Top 5 global e-commerce | Alibaba Group | 100K+ employees",
    "Mondelez": "Global FMCG | EUR 36B annual revenue | 90K+ employees",
    "Massimo Dutti": "Inditex Group flagship premium fashion brand | Hands-on retail floor",
}

job = Job(
    id=job_hash("Marketing Graduate", "Puig", "Dubai, UAE"),
    title="Marketing Graduate",
    company="Puig",
    location="Dubai, UAE",
    url="https://careers.puig.com/opportunities?country=9898",
    source="company_site",
    description=(
        "Marketing Graduate Programme — a structured two-year journey within Puig's Middle East Marketing "
        "team, working across Carolina Herrera, Byredo, Penhaligon's, Christian Louboutin Beauty, "
        "L'Artisan Parfumeur, Rabanne and Jean Paul Gaultier. Support the definition and execution of "
        "marketing plans and local adaptation of global brand strategies. Launch support: planning and "
        "execution of launches and category projects on the marketing calendar; 360 launch plans with "
        "internal teams and external partners; adaptation of assets and copy for retailers and media "
        "agencies. Product marketing: maintain marketing calendars, assortments and price lists; manage "
        "non-saleable items; support forecasting; monitor stock with Demand Planning. Budget & pricing: PO "
        "processes; support retail teams with GWPs and samples. Presentations & analysis: brand reviews and "
        "campaign performance analysis; retailer-meeting and leadership presentations; competitor and media "
        "monitoring; monthly competitor reports. Requirements: recently graduated (Bachelor/Master in "
        "Business, Marketing, Digital or Communication); at least 6 months in marketing support; advanced "
        "English (Arabic an asset). Start September 2026."
    ),
)

analysis = JobAnalysis(
    score=72, tier="Warm",
    skills_match=["launch support", "marketing calendars", "assortment & price lists", "competitor analysis", "presentations & brand reviews", "forecasting", "sampling / GWP", "fragrance"],
    missing_skills=["'recently graduated' profile — Paula is over-experienced for a graduate programme"],
    sector_fit="Luxury Beauty & Fragrances (Puig fragrance houses) — exact",
    seniority_fit="Over-qualified (grad programme targets fresh grads); positioned as a foot-in-the-door to Puig",
    red_flags=["graduate programme may screen for recent graduates only"],
    ats_keywords=["marketing", "launch", "brand", "fragrance", "competitor analysis", "assortment", "price list", "forecasting", "presentations", "GWP", "samples"],
    reasoning="Dream fragrance-house portfolio; every grad task maps to Paula's real work at a higher level. Main risk is over-qualification, applied transparently per Puig's open invite.",
)

cv = {
    "headline": "Marketing · Beauty & Fragrances · Brand Launches, Calendars & Competitor Insight",
    "professional_summary": (
        "Marketing professional with a Business Administration degree from CUNEF (E-Commerce & Fashion "
        "specialisation, 9.5/10 thesis) and hands-on experience across brand launches, marketing calendars, "
        "competitor analysis and trade activation in beauty, fragrances and FMCG. A genuine fragrance "
        "enthusiast — managed leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) as "
        "PIC Fragrances — eager to bring that energy and rigour to Puig's fragrance houses through the "
        "Marketing Graduate Programme."
    ),
    "experience": [
        {"company": "DoFreeze LLC", "role": "Brand & Marketing Manager", "dates": "Oct 2025 – Present",
         "location": "Dubai, UAE", "context": CTX["DoFreeze"], "bullets": [
            "Support and execute 360 launch plans across the marketing calendar, coordinating internal teams and external partners on assets and copy",
            "Maintain marketing calendars, assortments and price lists, and support quarterly forecasting and stock planning",
            "Run sampling, seeding and GWP programmes across modern trade and quick-commerce to drive trial and conversion",
            "Prepare brand reviews and campaign performance analysis, and monitor competitor and media activity, sharing insights with the team",
        ]},
        {"company": "Miravia (Alibaba Group)", "role": "Key Account Manager & PIC Fragrances – Beauty, Fragrances & Fashion",
         "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain", "context": CTX["Miravia"], "bullets": [
            "Led the fragrance category as PIC Fragrances, working with the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "Created the Beauty Club and Hot on Social brand projects, supporting local adaptation of brand initiatives and campaign storytelling",
            "Analysed competitor activity, trends, conversion and ROI, building reports that informed assortment, pricing and promotions",
            "Managed assortment and price positioning across 42 beauty and fragrance accounts",
        ]},
        {"company": "Mondelez International", "role": "Trainee – Category Planning", "dates": "Aug 2021 – Aug 2022",
         "location": "Madrid, Spain", "context": CTX["Mondelez"], "bullets": [
            "Conducted sell-in/sell-out analysis and evaluated promotional effectiveness, preparing performance reports for the category",
            "Supported NPD launches including Milka Spread and Mini Suchard within a global marketing organisation",
            "Built competitor and category insight to support planning cycles — classic marketing-support foundations",
        ]},
        {"company": "Massimo Dutti (Inditex)", "role": "Sales Associate – Las Rozas Village", "dates": "Jun 2018 – Jun 2019",
         "location": "Madrid, Spain", "context": CTX["Massimo Dutti"], "bullets": [
            "Premium beauty-and-fashion retail foundation at a flagship Inditex outlet — visual merchandising and elevated client experience",
            "First-hand passion for beauty and retail that has shaped my marketing career since",
        ]},
    ],
    "skills_brand": "brand launch support, 360 launch plans, marketing calendars, local brand adaptation, campaign storytelling, sampling & GWP, fragrance category",
    "skills_ecommerce": "e-commerce content, social (Instagram, TikTok), digital campaigns, retailer & media-agency coordination",
    "skills_commercial": "assortment planning, price lists, PO support, forecasting, competitor & market analysis, key account support",
    "skills_data": "campaign performance analysis, competitor reporting, sell-in/sell-out, KPI tracking, Power BI, Tableau, Looker, Excel",
    "skills_tools": "Canva, Meta Business Suite, Power BI, Tableau, Looker, Salesforce, SAP, Microsoft Office (Expert)",
}

cl = {
    "opening_paragraph": (
        "Puig's fragrance houses — Byredo, Jean Paul Gaultier, Rabanne, Penhaligon's, Carolina Herrera — are "
        "the brands I admire most, so the Marketing Graduate Programme in the Middle East is genuinely exciting "
        "to me. Fragrance is my passion and my specialism, and I'd throw myself into a two-year journey across "
        "these houses."
    ),
    "body_paragraph_1": (
        "Every part of the programme maps to work I already do hands-on: supporting 360 launches on the "
        "marketing calendar, maintaining assortments and price lists, forecasting, running sampling and GWP "
        "activations, and preparing brand reviews and competitor reports. As PIC Fragrances at Miravia I worked "
        "with the official distributors of leading Arabian and oud houses (Arabian Oud, Lattafa, Swiss Arabian, "
        "Ajmal), so I understand the Gulf fragrance consumer your niche houses speak to."
    ),
    "body_paragraph_2": (
        "In full honesty, I bring more hands-on experience than a typical graduate — but I'm applying with open "
        "eyes and real enthusiasm: I want to learn the Puig way across this portfolio and grow with the brands. "
        "I'm a CUNEF Business graduate (E-Commerce & Fashion specialisation, 9.5/10 thesis), Dubai-based on a UAE "
        "residence visa, fluent in Spanish and English, and ready to contribute from day one."
    ),
    "closing_paragraph": (
        "Given Puig's openness to candidates with transferable skills, I'd love the chance to discuss how my "
        "fragrance passion and marketing experience fit the Graduate Programme. I'm available to interview at "
        "your convenience and based in Dubai. Thank you for your consideration."
    ),
}

with llm.override({"submit_cv_content": cv}):
    cv_path = generate_cv(job, analysis)
with llm.override({"submit_cover_letter": cl}):
    cl_path = generate_cover_letter(job, analysis)

print("\n========== PUIG MARKETING GRADUATE ==========")
print("CV:", cv_path)
print("CL:", cl_path)
