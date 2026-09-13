"""One-off: generate Paula's CV for the **E-commerce Specialist (Remote)** role at
**Quik Hire Staffing** (staffing agency; remote, UAE-based; $60-95k USD; LinkedIn
Easy Apply, 100+ applicants, hidden end-client).

Pure e-commerce operations role — day-to-day online store: manage listings,
merchandising & storefront content; optimise on-site search/navigation/category
structure; run on-site promotions/bundles/conversion campaigns; monitor
conversion / AOV / traffic and report weekly; coordinate with marketing, ops &
customer service; run experiments to grow revenue. Asks 2+ yrs on Shopify/Magento/
BigCommerce, e-commerce KPIs & CRO, hands-on GA4, email/SMS/on-site personalisation,
attention to detail + test-and-learn, cross-functional collaboration, async.

Paula's fit is strong and honest — it's her e-commerce wheelhouse:
- Owns DoFreeze's D2C **Shopify** store end-to-end (listings, merchandising,
  storefront content, category/nav, collections, discounts, checkout, UX, CRO/AOV).
- Runs on-site **promotions/bundles/conversion campaigns**; A/B / test-and-learn.
- Monitors **conversion / AOV / traffic** in **GA4** + BI, reports weekly.
- Coordinates **marketing, ops & customer service** on order issues.
- Marketplace depth: **Miravia (Alibaba)** — 42 accounts, +30% GMV QoQ — plus
  quick-commerce (Noon, Talabat, Careem, Deliveroo, Glovo).

Honesty guardrails: NO Magento/BigCommerce hands-on claimed (Shopify + marketplaces
are the real ground); email/EDM & on-site personalisation framed honestly (no
specific SMS platform claimed); NO Arabic (not required here anyway); factual
"UAE Residence Visa" only — never the "no-sponsorship" claim.

ONE-PAGE standard (since 2026-08-27): tight summary (~2 lines), 3 bullets current
role / 1-2 older, ~6 skills per row. Fills the real CV template, relabels the
skills rows for an e-commerce specialist (template stays pristine), converts to PDF
via LibreOffice, registers the job for the dashboard, verifies 1 page, and lands
the package under output/2026-08-30/. Also drops a short-named 'Paula De Francisco -
CV.pdf' copy for portals that reject long filenames.
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

COMPANY = "Quik Hire Staffing"
TITLE = "E-commerce Specialist"
DATE_FOLDER = "2026-08-30"

JOB_DESCRIPTION = """\
E-commerce Specialist — Quik Hire Staffing (Remote, UAE; full-time; ~$60-95k USD).

We are hiring an E-commerce Specialist to manage the day-to-day operations of our
online store. The role spans merchandising, conversion, and the operational details
that decide whether revenue grows month over month.

Key Responsibilities:
- Manage product listings, merchandising, and storefront content.
- Optimise on-site search, navigation, and category structure.
- Run on-site promotions, bundles, and conversion campaigns.
- Monitor performance metrics (conversion rate, AOV, traffic) and report weekly.
- Coordinate with marketing, ops, and customer service on order issues.
- Run experiments to improve site performance and revenue.

Required Skills:
- 2+ years managing e-commerce stores (Shopify, Magento, BigCommerce, or similar).
- Strong understanding of e-commerce KPIs and conversion optimisation.
- Hands-on with GA4 and e-commerce analytics.
- Familiarity with email, SMS, and on-site personalisation tools.
- Excellent attention to detail and bias for testing.
- Comfort with cross-functional collaboration.

What You'll Bring: curiosity about audiences; strong written communication &
storytelling; a test-and-learn mindset (ship fast, iterate on data); comfort
working asynchronously across time zones.
"""

ATS = [
    "e-commerce", "eCommerce", "E-commerce Specialist", "online store",
    "Shopify", "store management", "product listings", "listings", "catalogue",
    "merchandising", "storefront content", "on-site search", "site navigation",
    "category structure", "on-site promotions", "bundles", "conversion campaigns",
    "conversion rate", "CRO", "conversion optimisation", "AOV", "average order value",
    "traffic", "performance metrics", "KPIs", "weekly reporting", "GA4",
    "Google Analytics", "e-commerce analytics", "email", "EDM", "SMS",
    "on-site personalisation", "A/B testing", "test-and-learn", "experimentation",
    "attention to detail", "cross-functional", "marketing", "operations",
    "customer service", "revenue growth", "async", "remote", "UAE",
    "marketplaces", "Miravia", "Alibaba", "Noon", "Talabat", "Careem", "Deliveroo",
    "Glovo", "quick-commerce", "Meta Ads", "Google Ads", "ROI", "ROAS", "GMV",
]

CONTENT = {
    "headline": (
        "E-Commerce Specialist · Shopify Store Management · "
        "Merchandising, CRO & Conversion · GA4 Analytics"
    ),
    "professional_summary": (
        "E-commerce specialist with 4+ years running online stores end-to-end — Shopify D2C plus "
        "marketplaces (Miravia / Alibaba) and UAE quick-commerce. Owns product listings, merchandising, "
        "storefront content, on-site promotions and CRO — lifting conversion and AOV through GA4-tracked "
        "test-and-learn. Data-led, AI-first and Dubai-based; cross-functional with marketing, ops and CS, "
        "and comfortable working async across time zones."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (E-Commerce — Shopify, End-to-End)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG / D2C group | Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the D2C Shopify store day-to-day, end-to-end — product listings, merchandising, storefront content, category structure and on-site search/navigation, collections, discounts and checkout — the operational detail that grows revenue",
                "Run on-site promotions, bundles and conversion campaigns and lift conversion rate and AOV through data-led merchandising, funnel/UX optimisation and A/B / test-and-learn experiments",
                "Monitor e-commerce KPIs (conversion, AOV, traffic) in GA4 and BI dashboards, report weekly, and coordinate with marketing, ops and customer service on order issues — with an AI (Claude/GPT) layer automating reporting",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Miravia — Alibaba's marketplace | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 marketplace stores/accounts — listings, catalogue, assortment, pricing and promotions — driving +30% GMV QoQ, and onboarded 30+ new stores in two months",
                "Owned the Flash Sales channel (reporting to the CEO) and continuously analysed conversion, traffic, retention and ROI/ROAS to optimise storefront and channel performance",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts (Quick-Commerce / Retail E-Commerce)",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | Retail vertical build-out",
            "bullets": [
                "Helped build Glovo's Retail vertical — onboarding brands and their catalogues onto the platform — and ran bespoke, data-led activations that lifted order volume and GMV across strategic accounts",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Commercial Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG multinational | €36B revenue | 90K+ employees",
            "bullets": [
                "Sell-in/sell-out and promo-effectiveness analysis and performance reporting — the analytical, detail-oriented foundation behind e-commerce measurement and test-and-learn",
            ],
        },
    ],
    # Skills-block ROW LABELS are relabelled for an e-commerce specialist in
    # _relabel_for_role(); values below are authored to sit under those labels.
    "skills_brand": (  # label -> "E-Commerce & Merchandising"
        "Shopify store management (end-to-end), product listings & catalogue, merchandising & storefront "
        "content, category structure & on-site search/navigation, collections, discounts & checkout"
    ),
    "skills_ecommerce": (  # label -> "Conversion & Growth"
        "CRO & funnel optimisation, on-site promotions & bundles, A/B testing & test-and-learn, "
        "UX optimisation, email/EDM & lifecycle, on-site personalisation, Paid Media (Meta & Google Ads)"
    ),
    "skills_commercial": (  # label -> "Operations & Cross-Functional"
        "day-to-day store operations, order-issue resolution, marketplaces & quick-commerce (Miravia, Noon, "
        "Talabat, Careem, Deliveroo, Glovo), catalogue onboarding, pricing & assortment, marketing/ops/CS coordination"
    ),
    "skills_data": (  # label -> "Analytics & Tracking (GA4)"
        "GA4 & e-commerce analytics, conversion / AOV / traffic KPIs, weekly reporting & dashboards, "
        "ROI, ROAS, GMV, forecasting, AI-assisted analysis, Power BI, Tableau, Looker"
    ),
    "skills_tools": (  # label -> "Tools" (unchanged)
        "Shopify, Google Analytics (GA4), Meta Ads Manager, Google Ads, Power BI, Tableau, Looker, "
        "Salesforce, Generative AI (Claude, ChatGPT), Canva, Microsoft Office (Expert)"
    ),
}

# Skills-block row-label overrides for this e-commerce CV (template kept pristine).
# Keep labels SHORT (≤ ~20 chars) so they fit the narrow ~1.55" label column on ONE
# line — longer labels wrap to 2 lines and push the CV onto a 2nd page.
ROLE_LABELS = {
    "Brand & Marketing": "Merchandising",
    "E-Commerce & Digital": "Conversion & Growth",
    "Commercial": "Operations",
    "Data & Analytics": "Analytics & GA4",
}


def make_job() -> Job:
    return Job(
        id="quikhire-ecommerce-specialist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Remote (UAE)",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "E-commerce Specialist Remote UAE Quik Hire Staffing Shopify GA4 CRO",
            "note": "Staffing-agency Easy Apply, remote, hidden end-client, 100+ applicants. Strong honest "
                    "e-commerce fit (Shopify end-to-end + Miravia marketplace + quick-commerce; CRO, GA4, "
                    "test-and-learn). No Arabic required. Factual UAE Residence Visa only.",
        },
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
        "salary_raw": "$60,000 – $95,000 USD + benefits",
        "salary_aed_min": 18000,
        "salary_aed_max": 29000,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 84,
        "ai_tier": "Warm-Hot",
        "skills_match": [
            "Owns a Shopify store end-to-end — listings, merchandising, storefront content, category/nav, collections, discounts, checkout, UX (the JD's core)",
            "Runs on-site promotions, bundles & conversion campaigns; A/B / test-and-learn",
            "Monitors conversion / AOV / traffic in GA4 + BI dashboards and reports weekly",
            "Coordinates with marketing, ops & customer service on order issues",
            "Marketplace depth: 42 accounts at Miravia (Alibaba), +30% GMV QoQ; quick-commerce (Noon, Talabat, Careem, Deliveroo, Glovo)",
            "2+ yrs managing e-commerce stores — she has 4+; Google E-Commerce certified; CUNEF BBA (E-Commerce & Fashion specialisation)",
            "Dubai-based on UAE residence visa; comfortable working async; AI-first",
        ],
        "missing_skills": [
            "No hands-on Magento/BigCommerce — Shopify + marketplaces are the real ground (JD says 'or similar', so covered)",
            "Email/EDM & on-site personalisation are genuine; no specific SMS platform claimed",
        ],
        "sector_fit": "excellent (day-to-day e-commerce store ops — Shopify, merchandising, CRO, GA4, test-and-learn — her exact wheelhouse)",
        "seniority_fit": "over-qualified-friendly (JD asks 2+ yrs; Paula 4+ with marketplace + quick-commerce depth)",
        "red_flags": [
            "Staffing-agency Easy Apply, remote, hidden end-client, 100+ applicants — low signal; a strong tailored CV + any warm angle matters more than the application itself",
            "Remote role (Paula prefers hybrid) and salary bottom (~$60k ≈ AED 18k/mo) sits just under her AED 20k/mo floor; top of band clears it comfortably",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit squarely in Paula's e-commerce wheelhouse. The role is day-to-day online-store "
            "management — listings, merchandising, storefront content, on-site search/nav/category, on-site "
            "promotions/bundles/conversion campaigns, GA4 KPI monitoring (conversion/AOV/traffic) with weekly "
            "reporting, cross-functional coordination with marketing/ops/CS, and test-and-learn experimentation. "
            "Paula owns DoFreeze's D2C Shopify store end-to-end (all of the above), monitors GA4 + BI and reports, "
            "and brings marketplace depth (42 accounts at Miravia/Alibaba, +30% GMV QoQ) plus quick-commerce. She "
            "has 4+ yrs vs the 2+ asked and is Google E-Commerce certified. Caveats are about the posting, not the "
            "fit: staffing-agency Easy Apply with a hidden client and 100+ applicants (low signal), remote (she "
            "prefers hybrid), and the salary floor sits just under her AED 20k/mo at ~$60k (top of band clears it). "
            "No Arabic required. Documents keep the factual UAE Residence Visa line only."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relabel_for_role(docx_path: Path) -> None:
    """Relabel skills rows for this e-commerce specialist CV (template stays pristine)."""
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

    cv_docx = cv._fill_template(CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    # Short-named copy for portals that reject long/special-char filenames.
    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    # Verify ONE page (one-page standard since 2026-08-27).
    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS — trim a bullet/skills")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
