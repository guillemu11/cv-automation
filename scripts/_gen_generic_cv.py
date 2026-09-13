"""One-off: generate a GENERIC, role-agnostic CV of Paula's full profile.

Purpose: Paula's manager will forward this into a Dubai WhatsApp/LinkedIn group
to see where she might fit — so it is NOT tailored to any single posting. It
presents her whole profile in a balanced way (Brand & Marketing + E-Commerce +
Key Account Management + Trade Marketing, across FMCG / Beauty / Fashion), using
the real CV template. Content is drawn straight from profile.yaml — nothing
invented.

Output: a clean, forward-ready file name (CV_Paula_De_Francisco_Perez.pdf) under
output/2026-08-28/CV_Generico/. No cover letter, no dashboard registration.
Converted to PDF via LibreOffice (soffice headless — docx2pdf/Word fails on this
Mac).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

DATE_FOLDER = "2026-08-28"
TARGET_SUBDIR = "CV_Generico"
CLEAN_STEM = "CV_Paula_De_Francisco_Perez"

CV_CONTENT = {
    "headline": (
        "Brand & Marketing · E-Commerce · Key Account Management · Trade Marketing "
        "| FMCG · Beauty · Fashion"
    ),
    "professional_summary": (
        "Brand, e-commerce and commercial professional with 4+ years across FMCG, Beauty, Fashion and "
        "E-Commerce. Currently Brand & Marketing Manager at DoFreeze (Befit, Eurocake, Flair) in Dubai, running "
        "multi-market strategy across 50+ countries. Track record: +30% GMV growth QoQ, 42 key accounts "
        "managed, 6 NPD launches end-to-end and influencer programmes scaled from zero to 25–50 creators per "
        "campaign. Hands-on with UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), modern trade, Shopify "
        "and Meta/Google Ads, and an early adopter of generative-AI automation. Business Administration graduate "
        "(CUNEF); already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Brands: Befit, Eurocake, Flair | sold across 50+ countries",
            "bullets": [
                "Lead Brand & Marketing for the portfolio across GCC, MENA, Asia, Europe, USA and Africa — owning multi-market strategy, go-to-market and A&P budgets across 50+ markets",
                "Lead NPD end-to-end for 6 product launches (brief, packaging, pricing, go-to-market)",
                "Built and scaled the influencer programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign, plus sampling and seeding across modern trade and quick-commerce to drive UGC and measurable sell-out",
                "Own and optimise the brand's Shopify e-store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
                "Integrated brands into UAE quick-commerce (Noon, Careem, Talabat, Deliveroo) — onboarding, listings, promo mechanics and retail execution — and run paid media on Meta and Google Ads",
                "Built an AI-powered marketing automation system (Claude / generative AI) for campaign planning, content, market research, KPI reporting and pitch decks — cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts across beauty, fragrances and fashion, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and executing commercial plans aligned with P&L targets",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months — including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Created and led the Beauty Club and Hot on Social projects, boosting brand visibility, customer loyalty and positioning Miravia as a beauty and lifestyle destination",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical — onboarding fashion and lifestyle brands and expanding the marketplace beyond food delivery into apparel, beauty and non-food",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) and integrated new partners, driving GMV growth through data-led planning and bespoke activations",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both Glovo and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Conducted sell-in/sell-out analysis, evaluated promotional effectiveness and built performance reports for the chocolate category",
                "Identified growth opportunities and contributed to NPD launches including Milka Spread and Mini Suchard",
            ],
        },
    ],
    "skills_brand": (
        "brand strategy, NPD end-to-end, influencer marketing, sampling & seeding, shopper marketing, "
        "trade marketing, A&P budget management, omnichannel campaigns, go-to-market, generative-AI campaigns"
    ),
    "skills_ecommerce": (
        "Shopify & e-store management, conversion rate optimisation (CRO), quick-commerce (Noon, Talabat, "
        "Careem, Deliveroo), Meta Ads, Google Ads, Instagram / TikTok / Pinterest, EDM, marketing automation"
    ),
    "skills_commercial": (
        "key account management, distributor management, modern trade, negotiation, pricing strategy, "
        "assortment planning, category management, forecasting"
    ),
    "skills_data": (
        "P&L management, KPI tracking, sell-in/sell-out, ROI, ROAS, GMV, Nielsen, Power BI, Tableau, Kantar, "
        "Salesforce, SAP"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Shopify, Meta Ads Manager, Google Ads, Salesforce, SAP, Power BI, "
        "Tableau, Nielsen, Adobe Creative Suite, Canva, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    # Synthetic "job" only drives the template's output path; renamed afterwards.
    return Job(
        id="generic-profile-cv-2026-08",
        title="Perfil General",
        company="Paula",
        location="Dubai, United Arab Emirates",
        url="",
        source="manual",
        description="Generic profile CV for circulation.",
        raw={},
    )


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


def main() -> None:
    job = make_job()

    # Fill the real template, then relocate/rename to a clean, forward-ready file.
    tmp_docx = cv._fill_template(CV_CONTENT, job)

    dest_dir = settings.output_dir / DATE_FOLDER / TARGET_SUBDIR
    dest_dir.mkdir(parents=True, exist_ok=True)
    clean_docx = dest_dir / f"{CLEAN_STEM}.docx"
    shutil.move(str(tmp_docx), str(clean_docx))

    # Clean up the synthetic job folder the template created at the output root.
    tmp_job_dir = tmp_docx.parent.parent
    if tmp_job_dir.exists() and tmp_job_dir.name.startswith("Paula - "):
        shutil.rmtree(tmp_job_dir, ignore_errors=True)

    pdf = _to_pdf_soffice(clean_docx)
    print("OK_CV", pdf)


if __name__ == "__main__":
    main()
