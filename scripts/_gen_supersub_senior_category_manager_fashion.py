"""One-off: CV for "Senior Category Manager – Fashion (UAE)", Supersub, Dubai, remote (found via Jack &
Jill, 2026-10-13; Teamtailor job 8442315). CV only for now.

The first livestream-shopping platform in the Middle East. The role scales pre-owned luxury, hypewear and
off-price apparel in the UAE: seller acquisition and onboarding, seller success (coaching sellers to run
livestreams, drops, bundling, pricing), marketplace operations with product/authentication/marketing,
creator collaborations and community events, full category KPIs and P&L. 3+ yrs in fashion (buyer,
category manager, reseller, consignment, or creator/affiliate); UAE network; Arabic preferred.

Paula's honest angle:
- Miravia & AliExpress: seller acquisition on a marketplace (30+ stores in two months, the Arabian-perfume
  push), 42 fashion/beauty/fragrance brands, Flash Sales (off-price, time-limited) against P&L, on-site
  visibility, work with marketing/product/ops (memory miravia-scope-all-cvs).
- DoFreeze: creators from zero (103 activations), Befit Crew affiliates, community events, bundles.
- Glovo: partner success on a delivery app, incl. visiting kitchens to cut prep times (memory glovo-real-role).
- Massimo Dutti at the Las Rozas Village factory store: off-price fashion retail floor.

Honesty guardrails:
- No pre-owned luxury, authentication, hypewear/sneaker or UAE consignment-network claims: she has none.
- Hot on Social was a monthly trend showcase, NOT livestream. She did NOT manage fashion brands at Miravia
  (2026-10-13). Fashion evidence: Flash Sales covered Fashion (confirmed), her thesis on e-commerce in fashion,
  Massimo Dutti, and Vinted (she buys and sells a lot). Official title includes "Fashion".
- No Arabic. Glovo is NOT the Retail vertical. NIVEA left out (needs "three months").
- Massimo Dutti / Mondelez dates are from her original CV; she remembers them longer — to confirm on LinkedIn.

ONE-PAGE standard. Lands under output/2026-10-13/Supersub - Senior Category Manager - Fashion (UAE)/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from docx import Document

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Supersub"
TITLE = "Senior Category Manager - Fashion (UAE)"
DATE_FOLDER = "2026-10-13"

JOB_DESCRIPTION = """\
Senior Category Manager – Fashion (UAE), Supersub — the first livestream shopping platform in the Middle
East. Dubai, remote. Scale pre-owned luxury, hypewear and off-price apparel verticals across the UAE.
Subject-matter expert on authenticated pre-owned luxury, streetwear/hypewear drops, premium apparel,
accessories and off-price retail. Seller acquisition and onboarding (luxury consignment boutiques, vintage
dealers, off-price distributors, hypewear resellers, independent fashion brands). Seller success: coach
sellers and creators to run high-converting livestreams (styling, authentication walkthroughs, drops,
bundling, pricing, hosting). Day-to-day marketplace operations with product, authentication and marketing.
Category growth and community: sneaker/hype drop shows, luxury vintage auctions, creator collaborations,
fashion marketing campaigns; presence at regional fashion activations and pop-ups. Own category KPIs and P&L.
English fluency, Arabic preferred. 3+ years in fashion as buyer, category manager, luxury reseller,
consignment manager or creator/affiliate. Luxury authentication, hypewear release cycles, off-price supply
chains; warm UAE relationships with consignment stores, sneaker boutiques, off-price distributors, retailers.
Differentiators: fashion e-commerce marketplace, luxury resale or creator platform experience; UAE luxury
retail; personal history trading luxury/streetwear on live-commerce apps. Package + equity, remote.
"""

ATS = [
    "category management", "marketplace", "seller acquisition", "seller onboarding", "seller success",
    "fashion", "off-price", "luxury", "pre-owned", "streetwear", "drops", "livestream shopping",
    "live commerce", "creator collaborations", "affiliates", "community building", "events", "pricing",
    "bundling", "assortment", "category KPIs", "P&L", "GMV", "marketplace operations", "UAE",
]

CV_CONTENT = {
    "headline": "Marketplace Category · Seller Growth · Trend Curation",
    "professional_summary": (
        "Marketplace category and key account manager with 5 years across beauty, fashion retail and "
        "e-commerce. At Alibaba's Miravia & AliExpress, grew 42 beauty and fragrance brands +30% GMV QoQ, "
        "onboarded 30+ sellers in two months and owned the Flash Sales channel against P&L targets. Now "
        "building creator and community programmes at DoFreeze; an active Vinted buyer and seller."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | 7 brands incl. Befit, Eurocake, SMASH | sold on talabat, Noon, Careem",
            "bullets": [
                "Lead marketing for 7 brands across 50+ markets with a team of two (designer, social media exec), incl. 6 product launches and listings and promotions on talabat, Noon and Careem",
                "Built the creator programme from zero (103 creator activations over 3 waves at AED 81 per content piece) and designed the Befit Crew affiliate programme with personal codes and tiered commissions",
                "Run community activations and events: running, padel and yoga club sessions, Saudi Food Show 2026, and a Sun & Sand Sports x Fabletics session that led to a listing proposal",
                "Judge everything on sell-out: SMASH x talabat lifted daily sales +165% vs +4.7% for a control brand; web orders +86% after adding reviews and basket-based bundles",
            ],
        },
        {
            "company": "Miravia & AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Marketplace | Beauty & Health department",
            "bullets": [
                "Managed 42 beauty and fragrance brands (incl. L'Oréal Paris, Maybelline, NYX, Redken, KIKO Milano) to +30% GMV QoQ through pricing, assortment, promotions and on-site visibility",
                "Seller acquisition: spotted the Arabian-perfume trend and onboarded 30+ stores in two months, incl. the distributors of Lattafa, Arabian Oud, Swiss Arabian and Ajmal, making it a top-growing sub-category",
                "Owned the Flash Sales channel for Beauty, Fashion & Home (up to ~30% of B&H sales): off-price, time-limited deals and pricing, reporting to the CEO",
                "Created Hot on Social, a monthly trend-led showcase of seasonal products and brand promotions, and the Beauty Club; worked with marketing, product and ops",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Food & quick-commerce delivery app | 10K+ employees",
            "bullets": [
                "Co-managed 5 XL restaurant partners (KFC, Taco Bell, Vicio): promotions, in-app visibility, fraud reviews, kitchen visits",
            ],
        },
        {
            "company": "Mondelez International · Massimo Dutti (Inditex)",
            "role": "Early Career",
            "dates": "2018 – 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Premium fashion retail",
            "bullets": [
                "Category Planning Trainee, Mondelez (Aug 2021 – Aug 2022): sell-in/sell-out and promo-effectiveness analysis, NPD support",
                "Sales Associate, Massimo Dutti (Jun 2018 – Jun 2019): Las Rozas Village factory store, premium off-price fashion retail",
            ],
        },
    ],
    "skills_brand": (
        "seller acquisition & onboarding, trend curation, key account management, pricing, flash sales"
    ),
    "skills_ecommerce": (
        "Miravia, AliExpress, Noon, talabat, Careem, Amazon, Glovo, Shopify, on-site visibility, bundling"
    ),
    "skills_commercial": (
        "creator & influencer programmes, affiliates, community events, sampling, UGC, product launches"
    ),
    "skills_data": (
        "P&L targets, GMV, sell-in/sell-out, promo uplift vs control, Excel (Expert), Looker, Power BI"
    ),
    "skills_tools": (
        "Claude (AI automation), ChatGPT, Canva, Photoshop, Meta Ads, Shopify"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Category",
    "E-Commerce & Digital": "Marketplaces",
    "Commercial": "Creators & Community",
    "Tools": "Tools & AI",
}


def make_job() -> Job:
    return Job(
        id="supersub-senior-category-manager-fashion-uae-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://supersub.teamtailor.com/jobs/8442315-senior-category-manager-fashion-english-uae",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"via": "Jack & Jill AI (tracked job, 2026-10-13)",
             "workplace": "Dubai, remote",
             "sector": "Live-commerce marketplace (fashion resale)"},
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id, "title": job.title, "company": job.company, "location": job.location,
        "url": job.url, "source": job.source, "description": job.description,
        "salary_raw": "Not posted (Jack & Jill estimate AED 240–360K/yr + equity ≈ 20–30K/month)",
        "salary_aed_min": 20000, "salary_aed_max": 30000,
        "posted_date": None, "raw": job.raw,
        "ai_score": 60, "ai_tier": "Possible",
        "skills_match": [
            "Marketplace seller acquisition: 30+ stores onboarded in two months at Miravia (Arabian-perfume push)",
            "42 fashion/beauty/fragrance brands, +30% GMV QoQ; Flash Sales (off-price) against P&L, reporting to the CEO",
            "Creators from zero (103 activations), Befit Crew affiliates, community events",
            "Partner success on Glovo (5 XL accounts); off-price fashion retail at Massimo Dutti's factory store",
        ],
        "missing_skills": [
            "Pre-owned luxury, authentication, hypewear/sneaker release cycles",
            "Warm UAE network of consignment stores, sneaker boutiques, off-price distributors",
            "Livestream commerce (unconfirmed); Arabic (preferred)",
        ],
        "sector_fit": "good (marketplace category management) but not luxury resale",
        "seniority_fit": "good (3+ yrs asked; Paula 5, 2 on a marketplace)",
        "red_flags": [
            "Core asks are luxury-resale expertise and a UAE fashion network she doesn't have",
            "Arabic preferred",
        ],
        "ats_keywords": ATS,
        "reasoning": "Marketplace seller acquisition, P&L and creator/community work fit; luxury resale, hypewear and UAE network are gaps.",
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relabel_for_role(docx_path: Path) -> None:
    doc = Document(str(docx_path))
    for table in doc.tables:
        for row in table.rows:
            first = row.cells[0]
            new = ROLE_LABELS.get(first.text.strip())
            if not new:
                continue
            para = first.paragraphs[0]
            if para.runs:
                para.runs[0].text = new
                for r in para.runs[1:]:
                    r.text = ""
            else:
                para.add_run(new)
    doc.save(str(docx_path))


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
                return pdf_path
        except Exception as exc:  # noqa: BLE001
            print("soffice conversion failed, falling back to docx2pdf:", exc)
    return cv._to_pdf(docx_path)


def _pages(pdf: Path) -> int:
    from pypdf import PdfReader
    return len(PdfReader(str(pdf)).pages)


def main() -> None:
    job = make_job()
    register_in_dashboard(job)

    final_dir = settings.output_dir / DATE_FOLDER / f"{COMPANY} - {TITLE}"
    dest = final_dir / "01_CV_y_Carta"
    dest.mkdir(parents=True, exist_ok=True)

    cv_docx = cv._fill_template(CV_CONTENT, job)
    _relabel_for_role(cv_docx)
    stray = cv_docx.parent.parent

    clean_docx = dest / "Paula De Francisco - CV.docx"
    shutil.move(str(cv_docx), str(clean_docx))
    # The template writes to output/<Company> - <Role>/ at the root; only ever remove that.
    if stray.exists() and stray.parent.resolve() == settings.output_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)

    cv_pdf = _to_pdf_soffice(clean_docx)
    # The dashboard only indexes CV_Paula_<Company>_<Title>.pdf; the clean name is the one to send.
    dashboard_pdf = dest / f"CV_Paula_{cv._sanitize_filename(COMPANY)}_{cv._sanitize_filename(TITLE)}.pdf"
    shutil.copy(str(cv_pdf), str(dashboard_pdf))
    print("OK", cv_pdf, "PAGES", _pages(cv_pdf), "| dashboard copy:", dashboard_pdf.name)


if __name__ == "__main__":
    main()
