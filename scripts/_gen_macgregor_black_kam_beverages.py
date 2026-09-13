"""One-off: generate Paula's CV + cover letter for MacGregor Black's
"Key Account Manager" role — a premium Beverage Distributor (On-Trade / luxury
hospitality) in Dubai, recruited by MacGregor Black (contact: Kieron Hall).

HONEST-FIT NOTE — this is a *stretch*, not a direct fit. The role is premium
BEVERAGE (spirits / wine / beer) On-Trade SALES into luxury bars, hotels and
hospitality groups. Paula has:
  - NO beverage-industry experience (spirits/wine/beer) — never claimed.
  - NO existing On-Trade / luxury-hospitality network (bar managers, sommeliers,
    F&B leaders) — never claimed; the letter is candid about this gap.

What IS genuine and used as the bridge:
  - Key Account Management is her explicit track: 42 key accounts at Alibaba's
    Miravia (+30% GMV QoQ) via commercial negotiation, assortment, pricing and
    promotions — including onboarding PREMIUM / LUXURY fragrance houses
    (Arabian Oud, Lattafa, Swiss Arabian, Ajmal).
  - F&B / HOSPITALITY account management at Glovo: strategic accounts KFC, Taco
    Bell, La Tagliatella, Sushi Shop — the closest genuine analogue to On-Trade
    hospitality accounts — plus negotiating and closing high-impact commercial
    deals and building the Retail vertical.
  - Distributor orchestration + UAE modern-trade / quick-commerce execution at
    DoFreeze (listings, promotions, activations, KPI reporting).
  - Graduate education (BBA, CUNEF); fluent English. Arabic (an advantage) NOT
    held — omitted, not faked.

VISA (IMPORTANT): Paula's UAE residence visa is EMPLOYER-sponsored/paid by her
current company. We do NOT claim "no sponsorship needed" anywhere. We state only
that she is already based in Dubai and available immediately with no relocation.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful. Fills the real CV + cover-letter templates, converts to PDF via
LibreOffice (soffice headless — docx2pdf/Word silently fails on this Mac),
registers the job for the dashboard, and lands the package under
output/2026-08-20/.
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

COMPANY = "MacGregor Black"
TITLE = "Key Account Manager"
DATE_FOLDER = "2026-08-20"

# Kieron Hall is the named recruiter / job advertiser at MacGregor Black
# ("Apply now or contact Kieron Hall at MacGregor Black") — address the letter
# to him rather than a generic "Hiring Manager".
CONTACT = "Kieron Hall"

JOB_DESCRIPTION = """\
Key Account Manager — MacGregor Black (recruitment partner for a leading premium
Beverage Distributor), Dubai, UAE. Hybrid, Full-Time. Salary: tax-free up to
21,000 AED/month based on experience; relocation package for international
candidates; performance incentives; private medical insurance; annual flights;
22 days annual leave.

Represent a portfolio of global spirits, wine & beer brands within one of the
world's most influential luxury hospitality hubs.

Key Responsibilities:
- Manage & grow premium On-Trade customer accounts across Dubai
- Drive distribution, visibility, volume & rate-of-sale performance for leading
  global brands
- Build strong relationships with bar managers, sommeliers, F&B leaders &
  hospitality groups
- Execute listing agreements, promotions, and commercial plans in-market
- Deliver brand activations, events & trade engagement across key venues
- Analyse customer performance, track KPIs, and provide reporting to senior
  leadership
- Partner with marketing & trade teams to maximise brand presence & execution

Qualifications & Requirements:
- Proven commercial experience in the beverage industry — spirits, wine, beer or
  premium drinks
- Strong On-Trade network & understanding of luxury hospitality channels
- Confident communicator & relationship-builder with commercial mindset
- Experience executing trade activations & premium brand programmes
- Comfortable working in a fast-paced, high-growth environment
- Passion for premium drinks & hospitality culture
- Graduate level education
- Fluent in English; Arabic an advantage
"""

ATS = [
    "Key Account Manager", "Key Account Management", "On-Trade", "premium",
    "luxury hospitality", "beverage", "spirits", "wine", "beer", "premium drinks",
    "distribution", "visibility", "volume", "rate-of-sale", "customer accounts",
    "listing agreements", "promotions", "commercial plans", "commercial mindset",
    "relationship-building", "brand activations", "events", "trade engagement",
    "trade activations", "premium brand programmes", "customer performance",
    "KPIs", "reporting", "senior leadership", "trade marketing", "brand presence",
    "commercial negotiation", "account growth", "distributor management",
    "fast-paced", "high-growth", "graduate", "Dubai", "UAE", "GCC", "hospitality",
    "F&B", "profitability", "GMV", "P&L",
]

CV_CONTENT = {
    "headline": (
        "Key Account Manager · Premium & Luxury Accounts · F&B / Hospitality · "
        "Commercial Negotiation · Trade Activation & Distribution"
    ),
    "professional_summary": (
        "Commercial and key account professional with 4+ years growing premium accounts, distributors and "
        "category performance across FMCG, Beauty, Fragrances, Fashion and F&B. At Alibaba's Miravia owned 42 "
        "key accounts and delivered +30% GMV growth QoQ through commercial negotiation, assortment, pricing and "
        "targeted promotions — including onboarding premium and luxury fragrance houses (Arabian Oud, Lattafa, "
        "Swiss Arabian, Ajmal). At Glovo managed strategic F&B and hospitality accounts (KFC, Taco Bell, La "
        "Tagliatella, Sushi Shop) and helped build the Retail vertical, negotiating and closing high-impact "
        "commercial deals. Now orchestrate distributor networks and modern-trade + quick-commerce execution for "
        "DoFreeze across the UAE and 50+ markets — driving distribution, visibility, listings, promotions and "
        "brand activations, with KPI reporting to senior leadership. Confident relationship-builder with a "
        "commercial mindset, comfortable in fast-paced, high-growth environments. Graduate education (BBA), "
        "fluent English, and already based in Dubai on a UAE residence visa — available immediately, no relocation."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Drive account and distributor execution across the UAE and 50+ markets — growing distribution, visibility, volume and rate-of-sale against agreed commercial plans with listings, promo mechanics and on-shelf availability",
                "Negotiate and manage listing agreements, promotions and commercial plans with accounts and distributors, building relationships that grow volume and profitability",
                "Deliver brand activations, sampling and trade engagement across modern trade and UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), integrating brands from onboarding to retail execution",
                "Manage A&P and trade budgets end-to-end, track account KPIs and provide performance reporting to senior leadership",
                "Partner with marketing and trade teams to maximise brand presence and execution, turning sell-out and competitor data into account actions",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned 42 key accounts, delivering +30% GMV growth QoQ (ahead of category) through commercial negotiation, assortment optimisation, pricing strategy and targeted promotions",
                "Built relationships across premium and luxury houses — onboarding 30+ accounts including the official distributors of leading Arabian & oud fragrance brands (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) in two months via trend-driven, value-creating assortment",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing commercial plans aligned with P&L targets",
                "Analysed customer performance — ROI, ROAS, conversion, traffic and retention — turning data into corrective actions and clear reporting to senior leadership",
                "Led the Beauty Club and Hot on Social projects, boosting brand visibility, loyalty and premium positioning",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic F&B and hospitality key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV through data-led joint planning and bespoke marketing activations",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both platform and partners",
                "Helped build Glovo's Retail vertical — onboarding premium fashion and lifestyle brands and expanding the marketplace into new categories",
                "Led cross-functional squads across marketing, logistics and operations to deliver flawless campaign execution and grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category (Nielsen), feeding commercial and demand planning",
                "Identified growth opportunities and supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
                "Built management-ready analyses in advanced Excel, translating market data into actionable commercial recommendations",
            ],
        },
    ],
    "skills_commercial": (
        "key account management, premium & luxury accounts, F&B / hospitality accounts, distributor "
        "management, commercial negotiation, listing agreements, pricing strategy, assortment planning, "
        "promotions, trade activation, forecasting"
    ),
    "skills_data": (
        "P&L management, KPI tracking & reporting, sell-in/sell-out, rate-of-sale, volume & distribution "
        "tracking, ROI/ROAS, Nielsen, Power BI, Salesforce, SAP"
    ),
    "skills_brand": (
        "trade marketing, shopper marketing, brand activations & events, sampling & seeding, visibility & "
        "merchandising, A&P & trade budget management, promotional planning, go-to-market"
    ),
    "skills_ecommerce": (
        "modern trade + quick-commerce (Noon, Talabat, Careem, Deliveroo), omnichannel retail execution, "
        "listings & promo mechanics, e-store management, conversion rate optimisation (CRO)"
    ),
    "skills_tools": (
        "SAP, Salesforce, Nielsen, Microsoft Excel (Advanced), PowerPoint (Advanced), Power BI, "
        "Generative AI (Claude, ChatGPT), Kantar, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm writing about the Key Account Manager role you're leading for a premium beverage distributor in "
        "Dubai. Representing a portfolio of global spirits, wine and beer brands across the city's luxury "
        "hospitality scene is exactly the kind of premium, relationship-led commercial challenge I look for — "
        "growing accounts through distribution, visibility, listings and standout activation. I'd welcome the "
        "chance to bring my key account and premium-brand track record to your client's On-Trade team."
    ),
    "body_paragraph_1": (
        "Key account management is the spine of my career. At Alibaba's Miravia I owned 42 key accounts and "
        "grew GMV +30% QoQ through commercial negotiation, assortment, pricing and targeted promotions — "
        "including onboarding premium and luxury fragrance houses such as Arabian Oud, Lattafa, Swiss Arabian "
        "and Ajmal, and reporting channel P&L directly to the CEO. At Glovo I managed strategic F&B and "
        "hospitality accounts — KFC, Taco Bell, La Tagliatella, Sushi Shop — negotiating and closing "
        "high-impact commercial deals and building bespoke activations. Today, as Brand & Marketing Manager at "
        "DoFreeze, I orchestrate distributor execution across the UAE and 50+ markets: listing agreements, "
        "promotions, brand activations and on-shelf visibility, with KPI reporting to senior leadership."
    ),
    "body_paragraph_2": (
        "I'll be candid: my accounts have been in premium beauty, fragrance, fashion and F&B rather than "
        "spirits, wine and beer specifically, and I'm building — not inheriting — an On-Trade network in Dubai. "
        "But the commercial muscle is the same: I grow premium accounts through distribution, rate-of-sale, "
        "listings and activation, I'm a confident relationship-builder with buyers and partners, and I thrive "
        "in fast-paced, high-growth environments. I already work inside the UAE market and its distributor and "
        "trade landscape, I learn categories fast, and I'm genuinely drawn to premium hospitality culture — the "
        "kind of passion this portfolio deserves."
    ),
    "closing_paragraph": (
        "I'd be excited to represent your client's premium beverage portfolio and grow its presence across "
        "Dubai's luxury On-Trade. I'm already based in Dubai on a UAE residence visa and available to start "
        "immediately, with no relocation required. Thank you for considering my application, Kieron — I'd "
        "welcome a conversation about how I'd approach building and growing these accounts. I look forward to "
        "hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="macgregor-black-kam-premium-beverages-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/macgregor-black/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Key Account Manager premium beverage On-Trade Dubai",
             "recruiter": "Kieron Hall (MacGregor Black, job advertiser)",
             "end_client": "Confidential — leading premium beverage distributor",
             "function": "Sales", "work_mode": "Hybrid",
             "salary_note": "Up to 21,000 AED/month (tax-free) + relocation, incentives, medical, flights"},
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
        "salary_raw": "Up to 21,000 AED/month (tax-free)",
        "salary_aed_min": None,
        "salary_aed_max": 21000,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 60,
        "ai_tier": "Warm",
        "skills_match": [
            "Key Account Management (explicit — Miravia 42 accounts, +30% GMV QoQ)",
            "Premium / luxury account onboarding (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "F&B / hospitality account management (Glovo — KFC, Taco Bell, La Tagliatella, Sushi Shop)",
            "Commercial negotiation & closing high-impact deals",
            "Distribution, visibility, listings & promotions (DoFreeze, UAE)",
            "Trade activations & brand programmes",
            "KPI tracking & reporting to senior leadership",
            "Fast-paced, high-growth environments (Alibaba, Glovo, DoFreeze)",
            "Graduate education (BBA, CUNEF) + fluent English",
            "Already in Dubai (residence visa), available immediately",
        ],
        "missing_skills": [
            "Beverage-industry experience (spirits/wine/beer) — NOT held; core JD requirement",
            "Existing On-Trade / luxury-hospitality network (bar managers, sommeliers, F&B leaders) — building, not inherited",
            "Arabic (JD lists as an advantage) — not held",
        ],
        "sector_fit": "weak/adjacent (premium beverage On-Trade sales; Paula's premium exposure is beauty/fragrance/fashion + F&B accounts)",
        "seniority_fit": "on-band (4+ yrs KAM; graduate-level asked)",
        "red_flags": [
            "Role is a SALES role in a specific industry (premium drinks) Paula has never worked in",
            "'Strong On-Trade network' is a stated requirement Paula does not yet have",
            "Salary caps at 21k AED/month — only just above the 20k floor",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "STRETCH / reach application, generated at Guille's explicit request. This is a premium-beverage "
            "(spirits/wine/beer) On-Trade SALES role into Dubai's luxury hospitality channel — an industry and "
            "a ready-made network Paula does not have, so it is scored Warm (60), not Hot. The honest bridge is "
            "Key Account Management, which IS her explicit track: 42 key accounts +30% GMV QoQ at Miravia via "
            "commercial negotiation/assortment/pricing/promotions (incl. onboarding premium/luxury fragrance "
            "houses), F&B & hospitality account management at Glovo (KFC, Taco Bell, La Tagliatella, Sushi "
            "Shop) with high-impact deal negotiation, and distributor + UAE modern-trade/quick-commerce "
            "execution at DoFreeze (distribution, visibility, listings, promotions, activations, KPI "
            "reporting). Positioned truthfully as a premium key-account manager who is candid about the "
            "beverage/On-Trade-network gap; NO invented drinks experience, NO faked hospitality network, "
            "Arabic omitted (not held). Visa framed only as 'already in Dubai, available immediately, no "
            "relocation' — no 'sponsorship not required' claim (her visa is employer-sponsored)."
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
