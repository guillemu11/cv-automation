"""One-off: generate Paula's CV for Arla
"Market Category Expert" / Category Development Manager (Dubai, MEA — FMCG dairy).

Strong fit on substance. Arla (global dairy FMCG; Puck, Lurpak, Castello, Starbucks
licence) wants a Market Category Expert / Category Development Manager to localise
regional category strategy: define growth drivers + market-level JTBDs, be the
go-to category expert, customise 4P toolkits / trade decks / NPD sell-ins, deep-
dive shopper & consumer understanding and market trends, work with NRM on pricing
& promotions, run Perfect Store, build bottom-up business cases and promo menus,
and report category performance — using Nielsen & EPOS data.

Maps cleanly onto Paula's real track:
  - Category-planning FOUNDATION at Mondelez (global FMCG food): sell-in/sell-out,
    Nielsen, promo effectiveness, planogram compliance, assortment-gap analysis,
    NPD from concept to shelf (Milka Spread, Mini Suchard).
  - Category OWNERSHIP at Alibaba's Miravia: owned Beauty & Fragrances category
    across 42 accounts, +30% GMV QoQ via assortment, pricing, margin and a data-led
    promotional calendar; category expansion + brand onboarding as PIC Fragrances.
  - Category + NPD + pricing/promo + distributor + retail execution at DoFreeze
    across 50+ markets (Shopify + UAE modern trade & quick-commerce).

Kept strictly truthful — honest gaps NOT papered over:
  - JD asks for MORE THAN 6 years (business/commercial dev, category mgmt, sales or
    marketing in FMCG/retailer). Paula has 4+ years. We state 4+, never inflate.
  - No DAIRY-specific category tenure — her FMCG food depth is Mondelez chocolate +
    DoFreeze bakery/F&B; dairy is adjacent, positioned as fast ramp not owned.
  - Named Arla/industry frameworks (NRM, Perfect Store, market-level JTBD) are
    positioned as transferable muscle (pricing/promo, retail execution, consumer
    understanding), NOT as certified methodologies she has personally run at scale.
  - VISA: already in Dubai on a UAE residence visa. NEVER claim "no sponsorship
    needed" (employer-sponsored). Only "already based in Dubai".

Fills the real CV template, converts to PDF via LibreOffice (soffice headless),
registers the job for the dashboard with an honest score, lands under
output/2026-08-27/. CV only (as requested); CL + form answers on request.
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

COMPANY = "Arla"
TITLE = "Market Category Expert"
DATE_FOLDER = "2026-08-27"

JOB_DESCRIPTION = """\
Market Category Expert / Category Development Manager — Arla, Dubai (MEA). Global
dairy FMCG (Puck, Lurpak, The Three Cows, Starbucks licence, Castello; 15bn EUR
turnover, 100+ countries).

Responsibilities: define and localise medium-to-long-term growth drivers for local
customers, consumers and shoppers; develop and own market-level JTBDs shaping the
category; be the go-to market category expert with insightful analysis; customise
4P category toolkits, trade decks and NPD sell-ins; deep-dive shopper behaviour,
consumer understanding and market trends to set strategic direction and propose
innovations; work with the NRM team to optimise pricing and promotions for
profitable, sustainable growth; implement the Perfect Store methodology for market
presence and channel success; monitor and evaluate category initiatives and adjust
strategy to hit targets; track industry, market and competitor activity; report
category performance and insights to stakeholders. Specific tasks: in-depth 4P
category analysis; NPD toolkit localisation; bottom-up business case development;
promo menu creation by category and channel.

What makes you successful: strategic thinking to shape dairy categories in-store;
MORE THAN 6 years in business/commercial development, category management, sales
or marketing within an FMCG company or retailer; business-development mindset;
market, channel and shopper insight; creative problem solving; analytical
expertise with data retrieval and insight generation using tools like Nielsen &
EPOS data. Closing date 4 September 2026.
"""

ATS = [
    "Category Development Manager", "Market Category Expert", "category management",
    "category development", "category strategy", "category growth", "4P", "4Ps",
    "4P framework", "category toolkit", "trade decks", "NPD sell-in", "NPD",
    "new product development", "JTBD", "jobs to be done", "shopper behaviour",
    "shopper marketing", "consumer understanding", "consumer insight",
    "market trends", "competitor analysis", "strategic direction", "innovation",
    "NRM", "net revenue management", "pricing", "promotions", "promotional menu",
    "Perfect Store", "retail execution", "channel", "market presence",
    "business case", "bottom-up business case", "assortment", "assortment planning",
    "planogram", "sell-in", "sell-out", "EPOS", "Nielsen", "category KPIs",
    "performance", "P&L", "modern trade", "FMCG", "dairy", "GCC", "MENA", "MEA",
    "UAE", "Dubai", "stakeholder management", "forecasting",
]

CV_CONTENT = {
    "headline": (
        "Category Development & Management · FMCG · 4P Category Strategy · NPD & Trade Sell-Ins · "
        "Shopper & Consumer Insight · Pricing & Promo (NRM) · Nielsen-Driven"
    ),
    "professional_summary": (
        "Category, commercial and brand professional with 4+ years across FMCG, Beauty and E-Commerce — turning "
        "shopper, consumer and market data into category growth. I built my category-planning foundation at "
        "Mondelez (sell-in/sell-out, Nielsen, promotional effectiveness, planogram compliance and assortment-gap "
        "analysis for the chocolate category); at Alibaba's Miravia I owned the Beauty & Fragrances category across "
        "42 accounts, growing GMV +30% QoQ through assortment, pricing, margin and a data-led promotional calendar; "
        "and at DoFreeze I run category, assortment, distributor negotiation, pricing and NPD end-to-end (6 "
        "launches) across 50+ markets. I work fluently with the 4P framework, NPD toolkits and trade sell-ins, "
        "Nielsen and EPOS/sell-out data, and bottom-up business cases — pragmatic, analytical and already based in "
        "Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own category development and assortment across the FMCG portfolio — building the range, 4P plans, pricing and a promotional menu by channel, and negotiating listings and terms with distributors and modern-trade partners to hit revenue and margin targets across 50+ markets",
                "Lead NPD end-to-end for 6 launches (brief, pricing, sell-in toolkit, go-to-market), localising toolkits and trade decks to local market/channel dynamics and building bottom-up business cases for each opportunity",
                "Translate shopper behaviour, consumer understanding and market trends into strategic direction and innovation proposals — analysing sell-out, competitors and category KPIs to steer assortment and close range gaps",
                "Drive retail execution and channel presence across modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo) — listings, availability and promo mechanics with a Perfect-Store-style approach to on-shelf and online presence",
                "Optimise pricing and promotions with a net-revenue mindset, using data to balance profitable, sustainable growth against volume",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned the Beauty & Fragrances category across 42 accounts, growing GMV +30% QoQ through assortment optimisation, pricing strategy, margin management and a data-led promotional calendar",
                "Led category expansion as PIC Fragrances — onboarding and negotiating terms with 30+ new brands/stores in two months, building the range and unlocking category growth",
                "Analysed market trends, competitors, shopper behaviour, ROI and conversion to set strategic direction, refine assortment and improve forecasting accuracy",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO against P&L, revenue and margin targets",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Built bottom-up commercial cases and negotiated high-impact deals as Glovo expanded its Retail vertical, growing GMV through data-led category and assortment planning",
                "Managed strategic key accounts and led cross-functional teams across marketing, logistics and operations to deliver activations and grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built my category-management foundation at a global FMCG leader — running sell-in/sell-out and Nielsen performance analysis and evaluating promotional effectiveness for the chocolate category",
                "Assessed shelf share, planogram compliance and assortment gaps versus potential to inform range and category recommendations",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf, turning category and shopper data into commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "category development & management, 4P category strategy, assortment planning, NPD sell-in toolkits & trade "
        "decks, pricing & promotions (net revenue management), bottom-up business cases, promo menu design, "
        "distributor & key account management, negotiation, channel & retail execution, stakeholder management"
    ),
    "skills_data": (
        "Nielsen, EPOS / sell-in–sell-out data, shopper & consumer insight, market & competitor analysis, "
        "category KPIs & performance tracking, P&L, ROI / ROAS, forecasting, AI-assisted analysis, Power BI, Kantar"
    ),
    "skills_brand": (
        "category growth strategy, shopper & trade marketing, NPD end-to-end, consumer understanding & JTBD framing, "
        "promotional planning, go-to-market, A&P & trade budget management, brand activation"
    ),
    "skills_ecommerce": (
        "modern trade, quick-commerce (Noon, Talabat, Careem, Deliveroo), e-commerce & Shopify, online "
        "merchandising & assortment, promo mechanics, conversion rate optimisation (CRO), marketing automation "
        "(generative AI)"
    ),
    "skills_tools": (
        "Nielsen, Kantar, SAP, Salesforce, Power BI, Tableau, Planorama, Foxy, Shopify, Microsoft Office (Expert), "
        "Generative AI (Claude, ChatGPT)"
    ),
}


def make_job() -> Job:
    return Job(
        id="arla-market-category-expert-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.arla.com/careers/market-category-expert",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Market Category Expert / Category Development Manager",
             "function": "Category Development / Category Management",
             "sector": "FMCG dairy", "closing_date": "2026-09-04"},
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
        "ai_score": 78,
        "ai_tier": "Warm",
        "skills_match": [
            "Category-planning foundation: sell-in/sell-out, Nielsen, promo effectiveness, planogram, assortment gap (Mondelez, FMCG food)",
            "Category ownership: Beauty & Fragrances across 42 accounts, +30% GMV QoQ (Miravia)",
            "4P plans, assortment, pricing & promo menu by channel (DoFreeze, Miravia)",
            "NPD end-to-end + sell-in toolkits + trade decks localisation (DoFreeze, 6 launches)",
            "Bottom-up business cases + commercial negotiation (DoFreeze, Glovo)",
            "Shopper behaviour, consumer understanding, market & competitor analysis",
            "Pricing & promotions with net-revenue mindset (NRM-adjacent)",
            "Retail execution / channel presence (modern trade + quick-commerce), Perfect-Store-style",
            "Analytical tooling: Nielsen, EPOS/sell-out, Power BI, Kantar",
            "Already in Dubai (UAE residence visa); FMCG core",
        ],
        "missing_skills": [
            "MORE THAN 6 years required — Paula has 4+ years (not inflated)",
            "Dairy-specific category tenure — has FMCG food (Mondelez chocolate, DoFreeze bakery/F&B), adjacent not identical",
            "Named Arla/industry frameworks (NRM, Perfect Store, market-level JTBD) — has the transferable muscle, not certified methodology tenure",
        ],
        "sector_fit": "very strong (FMCG category development is Paula's core — Mondelez category planning + Miravia category ownership + DoFreeze)",
        "seniority_fit": "reach on tenure (JD wants 6+ yrs; Paula 4+), on-band on substance (category dev/mgmt)",
        "red_flags": [
            "JD explicitly asks '>6 years' — Paula is at 4+; real tenure gap",
            "Dairy-specific category knowledge is implied — Paula's FMCG food is chocolate/bakery, adjacent",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong-on-substance, reach-on-tenure. Arla (global dairy FMCG) wants a Market Category Expert / "
            "Category Development Manager to localise category strategy: growth drivers + market-level JTBDs, 4P "
            "toolkits, trade decks, NPD sell-ins, shopper/consumer deep-dives, NRM pricing & promo, Perfect Store, "
            "business cases, promo menus, reporting — using Nielsen & EPOS. This is squarely Paula's wheelhouse: "
            "category-planning foundation at Mondelez (sell-in/sell-out, Nielsen, promo effectiveness, planogram, "
            "assortment gap, NPD), category ownership at Miravia (42 accounts, +30% GMV QoQ via assortment/pricing/"
            "margin/promo), and category + NPD + pricing/promo + distributor + retail execution at DoFreeze across "
            "50+ markets. Honest gaps: JD asks >6 years (Paula 4+, not inflated), no dairy-specific tenure (FMCG "
            "food is adjacent), and Arla's named frameworks (NRM/Perfect Store/JTBD) are transferable muscle rather "
            "than certified methodology. No 'no sponsorship needed' claim (employer-sponsored UAE residence visa). "
            "Worth a strong application built on the category/4P/Nielsen/NPD narrative. Closing date 4 Sep 2026."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
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
    job = make_job()
    register_in_dashboard(job)

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    final_dir = _relocate_to_dated_folder(cv_pdf.parent.parent)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
