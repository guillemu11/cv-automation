"""One-off: generate Paula's ONE-PAGE CV for **Ecommerce Assistant Manager** at **SQUATWOLF**
(Dubai gymwear DTC brand, customers in 100+ countries; on-site Dubai).

JD ask: own day-to-day ecommerce ops on a headless Shopify site + app; product setup, pricing (local &
global), categorisation, collections/filters/navigation hygiene; launches and seasonal drops (data,
reviews, imagery, timing); onsite banners/landing pages; QA and bug/checkout monitoring with Engineering;
support UX/CRO; ecommerce calendar; coordinate Digital Marketing, CRM, Content; stock availability with
Merchandising/Ops; backend-frontend alignment (Shopify, logistics, reviews, returns); process improvement;
manage juniors. 4-6+ yrs ecommerce ops, excellent Shopify, "completer finisher", passion for fitness.

Paula's honest angle: owns the DoFreeze Shopify store end-to-end (catalogue, collections, discounts,
checkout, CRO/AOV); AI-built landing page; weekly dark-store stock-risk review + MSL per channel (web
done by her); listings and promo mechanics on talabat/Noon/Careem; 6 NPD launches; Miravia marketplace
catalogue/promotions for 42 brands + Flash Sales channel; Befit = fitness brand (Fitness Month, run/padel/yoga clubs).

Honesty guardrails:
- No headless Shopify, no app, no page-speed/engineering QA claims, no reviews/returns platform named.
- Forecast not owned ("contribute"). ~4 yrs of pure ecommerce vs 4-6+. No personal fitness claim.
- Factual "UAE Residence Visa" only; already in Dubai (no relocation needed).

ONE-PAGE standard. Lands under output/2026-09-13/.
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

COMPANY = "SQUATWOLF"
TITLE = "Ecommerce Assistant Manager"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
Ecommerce Assistant Manager — SQUATWOLF (Dubai gymwear brand founded 2016, customers in 100+ countries).
Relocation to Dubai required. Own the operational execution of the Ecommerce platform so the website and
app run efficiently, accurately and at pace, enabling Trading, Marketing and Merchandising to hit targets.

Responsibilities: own day-to-day ecommerce operations (headless Shopify website and app), functional,
accurate and optimised; operational backbone supporting Trading plans; work with Ecommerce Director and
Ecommerce Merchandiser on trading strategy and campaign/launch readiness; accurate product setup, pricing,
categorisation and onsite visibility; lead product launches and seasonal drops (data, reviews, imagery,
timing); site hygiene across collections, filters, navigation; product uploads and catalogue integrity
incl. local and global pricing, promotions, product data, imagery; onsite content, banners, landing pages
on time; own QA; monitor bugs, errors, page speed, checkout issues; prioritise fixes with Engineering;
support UX and CRO through implementation and testing; manage the Ecommerce calendar; coordinate Digital
Marketing, CRM and Content; stock availability and onsite accuracy with Merchandising and Operations;
align backend systems (Shopify, Operations, Logistics, Reviews, Returns) with frontend; improve processes;
manage and develop junior team members.

About you: passion for fitness, sport or training culture; 4-6+ years in Ecommerce Operations; excellent
Shopify; excellent attention to detail; product catalogues, promotions and onsite content in Shopify;
highly organised, strong project management, Belbin completer finisher; accountable for Ecommerce
performance; cross-functional, multiple priorities; fast problem-solving.
"""

ATS = [
    "ecommerce operations", "Shopify", "headless Shopify", "catalogue management", "product uploads",
    "product data", "pricing", "promotions", "categorisation", "collections", "filters", "navigation",
    "site hygiene", "product launches", "seasonal drops", "landing pages", "banners", "onsite content",
    "QA", "checkout", "UX", "CRO", "conversion rate", "AOV", "ecommerce calendar", "trading",
    "merchandising", "stock availability", "CRM", "digital marketing", "cross-functional",
    "process improvement", "attention to detail", "project management", "fitness", "D2C",
]

CONTENT = {
    "headline": "Ecommerce Operations · Shopify · Catalogue, Promotions & Launches",
    "professional_summary": (
        "Ecommerce professional with 5 years across marketplaces (Alibaba, Glovo) and FMCG, now running a Shopify D2C store "
        "end-to-end in Dubai for a fitness snacking brand: catalogue, promotions, launches, QA and stock accuracy."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG snacking group (Befit fitness, Eurocake, Smash) | Shopify D2C + quick-commerce | GCC",
            "bullets": [
                "Own the Shopify store end-to-end: product uploads, pricing, collections, navigation, discounts and checkout, lifting conversion rate and AOV; built the affiliate landing page with AI agents",
                "Run launches and seasonal moments to the calendar (6 NPD launches, Fitness Month, New Year, Ramadan): product data, imagery, banners and promotions live on time across web, talabat, Noon and Careem",
                "Run a weekly stock-risk review by dark store with an AI-built dashboard and set the must-stock list for the web; contribute to the monthly sell-in forecast with Sales and Finance",
                "Coordinate digital marketing, CRM/EDM and content with 4 agencies so campaigns land correctly onsite; lead a team of two (designer + social media executive)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's eCommerce marketplace | 100K+ employees",
            "bullets": [
                "Managed catalogue, pricing, assortment and promotions for 42 brands (+30% GMV QoQ); onboarded 30+ fragrance stores in two months",
                "Owned the Flash Sales channel end-to-end (selection, pricing, timing, performance), reporting to the CEO",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Delivery & quick-commerce app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL partners (KFC, Taco Bell, Sushi Shop) on menus, promotions and ops issues; helped build the Retail vertical",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Built promotional-effectiveness and sell-in/sell-out reports with Nielsen for the chocolate category",
            ],
        },
    ],
    "skills_brand": (  # label -> "Ecommerce Ops"
        "catalogue & product data, pricing, promotions, collections & navigation, QA, launches"
    ),
    "skills_ecommerce": (  # label -> "Shopify & Onsite"
        "Shopify admin, landing pages, banners, discounts, checkout, CRO & AOV, marketplaces"
    ),
    "skills_commercial": (  # label -> "Coordination"
        "ecommerce calendar, trading & merchandising, CRM, content, agencies, team of two"
    ),
    "skills_data": (  # label -> "Stock & Data"
        "stock-risk review, must-stock lists, conversion funnel, KPI dashboards, sell-out"
    ),
    "skills_tools": (  # label -> "Tools"
        "Shopify, Excel, Looker, Power BI, Meta & Google Ads, Canva, Claude (AI agents)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Ecommerce Ops",
    "E-Commerce & Digital": "Shopify & Onsite",
    "Commercial": "Coordination",
    "Data & Analytics": "Stock & Data",
}


def make_job() -> Job:
    return Job(
        id="squatwolf-ecommerce-assistant-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=SQUATWOLF%20Ecommerce%20Assistant%20Manager",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "SQUATWOLF Ecommerce Assistant Manager",
            "note": "Good fit: owns Shopify D2C store end-to-end, launches, promotions, stock review, fitness brand (Befit). "
                    "Gaps: headless Shopify + app, engineering QA/page speed, ~4 yrs pure ecommerce ops; step down in title.",
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
        "id": job.id, "title": job.title, "company": job.company, "location": job.location,
        "url": job.url, "source": job.source, "description": job.description,
        "salary_raw": "Not disclosed",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 70, "ai_tier": "Hot",
        "skills_match": [
            "Owns a Shopify D2C store end-to-end (catalogue, pricing, collections, discounts, checkout, CRO/AOV)",
            "Launches and seasonal moments across web + talabat/Noon/Careem (6 NPD launches)",
            "Weekly dark-store stock-risk review and web must-stock list",
            "Marketplace catalogue & promotions ops at Miravia (42 brands, Flash Sales channel)",
            "Fitness-adjacent: Befit brand, Fitness Month, running/padel/yoga club partnerships",
        ],
        "missing_skills": [
            "Headless Shopify and app operations",
            "Engineering-side QA (bugs, page speed) and reviews/returns systems",
            "Dedicated ecommerce-ops title (hers is brand & marketing)",
        ],
        "sector_fit": "adjacent — D2C Shopify in FMCG fitness snacking vs gymwear D2C",
        "seniority_fit": "slight step down — Assistant Manager vs her Manager title",
        "red_flags": ["Assistant Manager level (salary may sit low)", "Ops-heavy role, less brand/marketing"],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong Shopify ownership, launches, promotions and stock accuracy with a fitness brand in Dubai; no Arabic "
            "required. Gaps are headless/app and engineering QA. Title is a step down; check salary vs AED 20k floor early."
        ),
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

    cv_docx = cv._fill_template(CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
