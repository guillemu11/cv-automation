"""One-off: generate Paula's CV (+ cover letter) for JTI's
"Consumer Activation Manager" — Global Travel Retail (GTR), Dubai.

Source: JTI careers (Workday) — https://jobs.jti.com/job/DUBAI-Consumer-Activation-Manager-000/1427768033/
Also live on LinkedIn ("Promocionado por un técnico de selección · Respuestas
gestionadas fuera de LinkedIn") — apply via the Workday portal so the ATS captures it.

Honest context (IMPORTANT):
  - STRONG fit on the core brief: the JD wants 4–5 years FMCG brand marketing incl.
    consumer/trade promotions, brand activation execution (new launches, Limited
    Edition Packaging / LEP), merchandising & POSM, a marketing activation calendar,
    A&P budget management + ROI, KPI monitoring, Brand Communication (ATL/BTL), Trade
    Segmentation, Merchandising Management, KAM, SAP, fluent English. Paula matches
    essentially all of it from real experience (DoFreeze activations + 6 NPD launches
    + A&P budgets + trade/shopper plans across 50+ markets; Miravia KAM 42 accounts
    +30% GMV QoQ; Mondelez category-planning trade-promo analysis).
  - TWO honest gaps, NOT hidden:
      1. TRAVEL RETAIL (duty-free / GTR) itself — Paula has run activations in
         domestic + e-commerce/modern-trade channels, not travel retail. The JD lists
         travel-retail experience as "an advantage", NOT a requirement. The cover
         letter states this plainly and bridges it with two genuine adjacencies:
           • Category depth in BEAUTY & FRAGRANCES — the core travel-retail
             categories: at Alibaba's Miravia she managed 42 accounts incl. leading
             fragrance houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal).
           • The role liaises with the AMERICAS travel-retail teams; Paula is a native
             Spanish speaker — a real asset for LATAM markets.
      2. TOBACCO / nicotine sector — JTI is Japan Tobacco International. This is a
         values call for Paula, flagged in the dashboard red_flags; nothing in the
         CV/CL pretends otherwise. No tobacco experience is invented.
  - Per project rules: NOTHING fabricated (real titles/metrics kept; the letter is
    candid about the travel-retail gap). NO "own visa / no sponsorship" claim anywhere
    — the CV visa field ("UAE Residence Visa") is factual and stays; the letter asserts
    nothing about sponsorship (her residence visa is employer-sponsored).

Application channel: JTI Workday portal (recruiter-managed, no named contact) →
CONTACT = None, letter addressed to "Hiring Manager".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word fails on this Mac), registers the job for the
dashboard, and lands the package under output/2026-08-23/.
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

COMPANY = "JTI"
TITLE = "Consumer Activation Manager"
DATE_FOLDER = "2026-08-23"
JOB_URL = "https://jobs.jti.com/job/DUBAI-Consumer-Activation-Manager-000/1427768033/"

CONTACT = None  # Recruiter-managed via Workday/LinkedIn, no named contact → "Hiring Manager".

JOB_DESCRIPTION = """\
Consumer Activation Manager — JTI (Japan Tobacco International), Global Travel
Retail (GTR). Dubai, UAE. Full-time.

Global Travel Retail is a strategic channel following consumers wherever they
travel — present in 160+ markets, JTI's fastest-growing market YTD, ~13bn sticks
planned for 2026, critical to GFB brand-equity building and Ploom Geo expansion.
One of the most diverse teams within JTI: 220 employees, 41 nationalities, 29+
locations, 6 Regional Hubs.

This position is responsible for developing and implementing brand activation
plans and activation initiatives across all product categories — including new
product / line-extension launches and Limited Edition Packaging (LEP) — all
aligned with GTR Marketing strategies & Brand Group guidelines. Liaises and works
very closely with the Americas Travel Retail Sales teams, ensuring competitive
activities for all assigned markets and being responsible for: the activation
calendar coordination; the implementation of consumer & trade marketing programs;
KPI monitoring. Engages and aligns with domestic markets for their strategic
plans, transferring knowledge within GTR to support the Marketing Plan objectives.
Establishes very close links with the Finance Travel Retail team for budget
reporting.

Marketing Strategy — Lead the development of marketing strategies for assigned
markets in collaboration with the Sales team based on GTR directions, synergy
with domestic-market plans and global trends, the regulatory environment and
digital-transformation priorities.

Brand Activation Execution Excellence — Lead planning and implementation of brand
equity building initiatives with Sales and P&S teams: impactful merchandising
solutions & POSM based on GTR Equity guidelines; consumer-centric brand
activations for new launches, LEP and/or brand rejuvenations; a clear marketing
activation calendar with regular status updates; ongoing evaluation of marketing
programs and driving efficiency of campaigns.

Retail Excellence (1-2-1) Program — Collaborate with RSC (Retail Sales
Consultants) SPOC: support brand-communication training materials, adapt to
market specificities, deliver brand-communication training to RSC, and with Sales
and Global Indirect Procurement source the best, most cost-efficient agencies.

Marketing Budget Management — Develop and manage assigned markets' marketing
budget process to ensure timely, consistent, integrated delivery of marketing
plans; deliver clear plans during Annual Plans and quarterly revisions with
variance explanations; ensure marketing-investment efficiency & ROI via the right
resource allocation based on location prioritisation; ensure accuracy and full
compliance with internal Policies & Procedures.

Requirements:
- University degree or equivalent (required).
- 4–5 years in FMCG brand marketing incl. consumer/trade promotions management (an advantage).
- Cross functional / cross cultural experience (an advantage).
- Travel retail experience (an advantage).
- Computer literate: Microsoft Office and SAP.
- Brand Communication (ATL / BTL), Trade Segmentation, Merchandising Management, Key Account Management.
- Fluent English (required). Other languages a plus.
"""

ATS = [
    "consumer activation", "brand activation", "activation initiatives",
    "activation calendar", "brand equity", "brand equity building",
    "new product launch", "line extension", "Limited Edition Packaging", "LEP",
    "merchandising", "merchandising management", "POSM", "brand communication",
    "ATL", "BTL", "trade segmentation", "consumer marketing", "trade marketing",
    "consumer & trade promotions", "shopper marketing", "key account management",
    "KAM", "marketing budget", "A&P budget", "budget management", "ROI",
    "investment efficiency", "KPI monitoring", "campaign efficiency",
    "go-to-market", "NPD", "brand rejuvenation", "cross functional",
    "cross cultural", "SAP", "Microsoft Office", "FMCG", "travel retail",
    "GTR", "Global Travel Retail", "duty free", "beauty", "fragrances",
    "Americas", "LATAM", "Dubai", "GCC", "MENA", "P&L", "forecasting",
    "compliance", "stakeholder management",
]

CV_CONTENT = {
    "headline": (
        "Brand & Consumer Activation Manager · Consumer & Trade Promotions · Brand "
        "Communication (ATL/BTL) · Merchandising & POSM · NPD & LEP Launches · A&P "
        "Budget & ROI · Beauty & Fragrances · Dubai, UAE"
    ),
    "professional_summary": (
        "FMCG brand and consumer-activation professional with 4+ years across FMCG, "
        "beauty & fragrances, fashion and e-commerce. Currently leads Brand & "
        "Marketing for DoFreeze across 50+ markets (GCC, MENA, Asia, Europe, USA, "
        "Africa) — planning and executing brand activations and NPD/LEP launches, "
        "owning the marketing activation calendar, A&P budgets and ROI, and building "
        "trade & shopper marketing programmes by channel. Category depth in beauty "
        "and fragrances (managed leading fragrance houses at Alibaba's Miravia, +30% "
        "GMV QoQ across 42 accounts). Cross-functional and cross-cultural, computer "
        "literate in SAP and MS Office, native Spanish (an asset for the Americas), "
        "fluent English (C1)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Develop and implement brand activation plans and initiatives across all product categories — new product / line-extension launches and seasonal/limited-edition executions — aligned to brand guidelines, maintaining a clear marketing activation calendar with regular status updates across 50+ markets",
                "Lead NPD end-to-end for 6 launches (brief, packaging, pricing, go-to-market), coordinating consumer-centric activations, merchandising and POSM with sales teams to build brand equity at the point of purchase",
                "Develop and manage A&P budgets — ensuring marketing-investment efficiency and ROI via location-based prioritisation, delivering clear annual and quarterly plans with variance explanations, in full compliance with internal policies",
                "Build trade and shopper marketing plans by channel (modern trade and quick-commerce), supporting key account strategy and category management across GCC, MENA, Asia, Europe, USA and Africa",
                "Run consumer-centric activations — influencer & UGC programmes (25–50 creators/campaign), sampling & seeding — and continuously evaluate campaign efficiency, driving awareness and measurable sell-out",
                "Coordinate cross-functional, cross-cultural teams (sales, finance, supply, creative) to deliver activations on time, on budget and in full",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts across beauty and fragrances — including the official distributors of leading Arabian & oud fragrance houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal), core travel-retail categories — achieving +30% GMV QoQ through pricing, assortment and targeted promotions",
                "Created and led the 'Beauty Club' and 'Hot on Social' consumer activations, boosting brand visibility, engagement and customer loyalty",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via strategic promotions and trend-led activation",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise campaign efficiency and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), delivering bespoke marketing activations and leading cross-functional teams (marketing, logistics, support) to execute campaigns seamlessly",
                "Part of the team building Glovo's retail vertical — onboarding fashion and lifestyle brands and expanding the marketplace beyond food",
                "Negotiated and closed high-impact commercial deals, managing budgets to maximise profitability for partners and platform",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG leader | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Conducted sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, evaluating consumer & trade promotions at a global FMCG leader",
                "Contributed to NPD launches (Milka Spread, Mini Suchard), sharpening trade-marketing and category judgement inside a large, matrixed organisation",
            ],
        },
    ],
    "skills_brand": (
        "brand activation & consumer activation, consumer & trade promotions, brand "
        "communication (ATL/BTL), merchandising & POSM, NPD & LEP launches, marketing "
        "activation calendar, shopper marketing, go-to-market, brand equity building, "
        "A&P budget management, omnichannel campaigns"
    ),
    "skills_ecommerce": (
        "quick-commerce (Noon, Talabat, Careem, Deliveroo), Shopify / e-store, Meta "
        "Ads, Google Ads, social (Instagram, TikTok, Pinterest), influencer & UGC, "
        "EDM, generative-AI content"
    ),
    "skills_commercial": (
        "key account management, trade segmentation, modern-trade & distributor "
        "management, category management, negotiation, pricing & assortment, "
        "cross-functional & cross-cultural coordination"
    ),
    "skills_data": (
        "A&P budget & ROI, P&L, KPI monitoring, sell-in/sell-out, ROAS, forecasting, "
        "SAP, Power BI, Nielsen, Kantar"
    ),
    "skills_tools": (
        "SAP, Microsoft Office (Expert), Generative AI (Claude, ChatGPT), Meta "
        "Business Suite, Google Ads, Power BI, Salesforce, Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Building brand equity across a global travel-retail portfolio — activating "
        "new launches and Limited Edition Packaging across many markets at once, from "
        "activation calendar to POSM to ROI — is exactly the kind of work I do today, "
        "so JTI's Consumer Activation Manager role in Global Travel Retail immediately "
        "drew me in. I currently lead brand and activation for an FMCG portfolio "
        "across 50+ markets from Dubai, owning the activation calendar, NPD and "
        "limited-edition launches, A&P budgets and trade & shopper programmes "
        "end-to-end."
    ),
    "body_paragraph_1": (
        "The core of the role maps directly onto what I deliver. At DoFreeze I develop "
        "and implement brand activation plans across all product categories — "
        "translating brand guidelines into launches, line extensions and seasonal "
        "executions — and I keep a clear activation calendar with regular status "
        "updates across GCC, MENA, Asia, Europe, the USA and Africa. I lead six NPD "
        "launches end-to-end (brief, packaging, pricing, go-to-market) with the "
        "merchandising and POSM to build equity at the point of purchase; I develop "
        "and manage A&P budgets, protecting investment efficiency and ROI through "
        "location-based prioritisation with clear annual and quarterly plans; and I "
        "monitor KPIs and campaign efficiency working cross-functionally with sales, "
        "finance and supply. Brand communication (ATL/BTL), trade segmentation, "
        "merchandising and key account management are day-to-day tools for me, and I "
        "work in SAP and MS Office."
    ),
    "body_paragraph_2": (
        "Two things make me a natural fit for this specific brief. First, my category "
        "depth is in beauty and fragrances — the heart of travel retail: at Alibaba's "
        "Miravia I managed 42 accounts including leading fragrance houses (Arabian "
        "Oud, Lattafa, Swiss Arabian, Ajmal), growing them +30% GMV quarter-on-"
        "quarter. Second, this role liaises closely with the Americas travel-retail "
        "teams, and as a native Spanish speaker I can work naturally across LATAM "
        "markets. I'll be candid on one point: my activation experience has been in "
        "domestic and e-commerce / modern-trade channels rather than travel retail "
        "itself — but the discipline is identical, and I would bring it to GTR from "
        "day one, already based in Dubai."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to discuss how my activation, budget and category "
        "experience would translate into JTI's Global Travel Retail team, and I'm "
        "ready to move quickly. Thank you for considering my application — I look "
        "forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="jti-consumer-activation-manager-gtr-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url=JOB_URL,
        source="jti_careers",
        description=JOB_DESCRIPTION,
        raw={"query": "JTI Consumer Activation Manager Global Travel Retail Dubai",
             "function": "Consumer/brand activation — Global Travel Retail (duty free)",
             "sector": "Tobacco / nicotine (FMCG) — Japan Tobacco International, GTR channel",
             "note": "STRONG core fit (FMCG brand activation, consumer/trade promotions, LEP/NPD "
                     "launches, merchandising & POSM, activation calendar, A&P budget & ROI, "
                     "ATL/BTL, trade segmentation, KAM, SAP, fluent English). TWO honest gaps, not "
                     "hidden: (1) no travel-retail experience — JD lists it as 'an advantage', not a "
                     "requirement; bridged via real beauty/fragrance category depth (Miravia: Arabian "
                     "Oud, Lattafa, Swiss Arabian, Ajmal) + native Spanish for the Americas TR teams; "
                     "(2) tobacco/nicotine SECTOR — values call for Paula (flagged). Nothing "
                     "fabricated; cover letter is candid about the TR gap. No 'own visa / no "
                     "sponsorship' claim (employer-sponsored residence visa)."},
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
        "salary_raw": "Not disclosed (big-tobacco FMCG band; GTR — typically above FMCG average)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 82,
        "ai_tier": "Strong (sector caveat: tobacco)",
        "skills_match": [
            "Direct brand-activation execution: develops/implements activation plans across product categories, NPD & seasonal/LEP launches, activation calendar with status updates (DoFreeze, 50+ markets)",
            "Consumer & trade promotions + shopper/trade marketing by channel; brand communication (ATL/BTL), trade segmentation, merchandising & POSM, KAM — all real",
            "A&P budget management + ROI + KPI monitoring; annual/quarterly plans with variance explanations; cross-functional with sales & finance",
            "Beauty & fragrances category depth = core travel-retail categories: Miravia 42 accounts incl. Arabian Oud, Lattafa, Swiss Arabian, Ajmal, +30% GMV QoQ",
            "Cross-functional & cross-cultural (50+ markets); SAP + MS Office; native Spanish (asset for the Americas TR teams the role liaises with); fluent English C1",
        ],
        "missing_skills": [
            "No TRAVEL RETAIL / duty-free (GTR) experience — JD lists it as 'an advantage', NOT a requirement; bridged honestly via beauty/fragrance depth + Spanish/Americas, and the cover letter states the gap plainly",
            "No prior tobacco/nicotine-sector experience (activation skills transfer; not fabricated)",
            "No RSC (Retail Sales Consultant) 1-2-1 training-programme background specifically (adjacent brand-communication/training work only)",
        ],
        "sector_fit": "FMCG brand activation — YES; but tobacco/nicotine sector (values decision for Paula) and travel-retail channel is new",
        "seniority_fit": "on-band — Manager role, 4–5 years FMCG brand marketing; Paula is 4+ years at manager level",
        "red_flags": [
            "TOBACCO SECTOR: JTI = Japan Tobacco International (Winston, Camel, Ploom, Nakhla shisha, etc.). This is a personal/values decision for Paula — the biggest gate, not a skills gap.",
            "Travel-retail experience gap: real, but JD lists TR as 'an advantage' not a requirement; handled with an honest cover letter.",
            "Competitive: LinkedIn showed 175 applicants (24 in last day, 100+ clicked apply). Warm intro via the 2 CUNEF alumni at JTI strongly recommended over cold apply.",
            "Salary not disclosed — confirm it clears the 20k AED/month floor (big-tobacco GTR typically well above).",
            "Nothing fabricated; no 'own visa / no sponsorship' claim (employer-sponsored residence visa).",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong core fit to JTI's Consumer Activation Manager (Global Travel Retail, Dubai). "
            "The JD's core — FMCG brand activation across categories, NPD & LEP launches, "
            "merchandising & POSM, a marketing activation calendar, consumer/trade promotions, A&P "
            "budget management + ROI, KPI monitoring, ATL/BTL, trade segmentation, KAM, SAP, fluent "
            "English — maps almost point-for-point onto Paula's real experience (DoFreeze activations "
            "+ 6 NPD launches + A&P budgets + trade/shopper plans across 50+ markets; Miravia KAM 42 "
            "accounts +30% GMV QoQ in beauty & fragrances; Mondelez category-planning trade-promo "
            "analysis). Two honest gaps, both surfaced not hidden: (1) no travel-retail/duty-free "
            "experience — but the JD lists it only as 'an advantage', and it's bridged with genuine "
            "beauty/fragrance category depth (the core TR categories) plus native Spanish for the "
            "Americas TR teams the role supports; (2) the tobacco/nicotine sector, which is a values "
            "decision for Paula rather than a competence gap. Per project rules nothing is fabricated: "
            "real titles/metrics kept, and the cover letter is candid about the travel-retail gap "
            "while arguing the adjacencies. No 'own visa / no sponsorship' claim. Recommended path: "
            "tailored CV+CL → apply via the JTI Workday portal → warm intro through the 2 CUNEF alumni "
            "at JTI rather than competing cold against 175 applicants."
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
