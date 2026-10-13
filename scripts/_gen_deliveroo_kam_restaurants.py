"""One-off: CV for Deliveroo "Key Account Manager - Restaurants", Dubai (LinkedIn, posted ~2026-10-06).
Paula has an interview for this one. CV only.

Restaurant key-account management on a food-delivery platform: own a portfolio of top-tier restaurant
partners, grow their business on the platform, run commercial and marketing plans, work with
Operations/Marketing, review performance with data.

Paula's honest angle:
- Glovo XL Accounts: the same job, same model, large restaurant chains in Madrid (2022-23).
- Miravia KAM: 42 accounts, +30% GMV QoQ, 30+ stores onboarded in two months.
- DoFreeze: sits on the partner side of talabat, Careem and Noon today — she knows what a brand
  wants from its platform account manager, which is the exact empathy this role needs.

Honesty guardrails (differences vs the Careem CV of 2026-10-12):
- Glovo rewritten per Paula's own account (memory: glovo-real-role, 2026-10-12): XL team, "basically
  as a junior", co-managed the accounts. NO "negotiated commercial deals", NO "helped build the
  Retail vertical", NO "led cross-functional teams" — she did not recognise those framings.
- The XL portfolio was FIVE accounts: KFC, Taco Bell, La Tagliatella, Sushi Shop, Vicio. Few accounts
  because XL demanded depth; a separate regional team handled the many small restaurants by zone.
- DoFreeze is NOT live on Deliveroo. It DID pitch Deliveroo and sent a product proposal, which went
  unanswered (the war intervened); DoFreeze wants to reopen that conversation. So: never list Deliveroo
  as a platform of hers, but she can honestly say she has pitched Deliveroo from the supplier side.
  Live platforms: talabat, Careem, Noon, Amazon, Kibsons, Medex (pharmacy).
- Never "own the forecast"; the AI stock-risk dashboard was built as a team ("we built").
- No Arabic. Visa line comes from profile.yaml.

ONE-PAGE standard. Lands under output/2026-10-13/.
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

COMPANY = "Deliveroo"
TITLE = "Key Account Manager - Restaurants"
DATE_FOLDER = "2026-10-13"

JOB_DESCRIPTION = """\
Key Account Manager - Restaurants, Deliveroo, Dubai, UAE. Full-time. (Real posting text, captured
2026-10-13; the ad has since closed.)

Deliveroo is now part of DoorDash, alongside Wolt.

The team: as Deliveroo scales, it becomes a major revenue channel for restaurants. Beyond best-in-class
support, the Account Management team are "restaurant consultants that use data-driven insight and
industry knowledge to help our partner restaurants grow". They own and manage restaurant relationships.

What you will be doing:
- Manage a portfolio of Deliveroo's most important restaurants, including high-sales volume drivers and
  global restaurant brands
- Own relationships with key restaurant industry stakeholders
- Analyze data to drive growth and profitability, both for your partners and for Deliveroo
- Work cross-functionally with other departments (Marketing, Operations) to drive new initiatives

What skills you'll need:
- Minimum of 3-5 years of experience in a relevant industry
- Strong analytical and problem-solving skills
- Well-organized with excellent team-player qualities
- Strong interpersonal skills to build and maintain relationships
- Agile and highly adaptable to a fast-paced work environment
- Strong knowledge of the restaurant industry is a plus
- Fluency in both English and Arabic is a strong advantage

Benefits: 25 days annual leave, medical insurance, annual flight allowance, free Deliveroo Plus,
maternity/paternity benefits.
"""

ATS = [
    "Key Account Manager", "key account management", "account management", "restaurant partners",
    "portfolio management", "restaurant industry", "restaurant consultant", "data-driven insight",
    "data analysis", "analytical", "problem-solving", "growth", "profitability", "food delivery",
    "quick-commerce", "marketplace", "F&B", "e-commerce", "partner performance",
    "stakeholder relationships", "promotions", "marketing activations", "onboarding", "cross-functional",
    "Operations", "Marketing", "GMV", "orders", "Excel", "Dubai", "UAE", "Deliveroo",
    "talabat", "Careem", "Noon", "Glovo",
]

CV_CONTENT = {
    "headline": (
        "Key Account Management · Restaurant & Brand Partners · Food Delivery & Q-Commerce · "
        "Data-Led Partner Growth"
    ),
    "professional_summary": (
        "Account manager with 5 years growing partners on delivery and e-commerce platforms. At Glovo I "
        "worked on Glovo's five XL restaurant chains (KFC, Taco Bell, Vicio); at Alibaba's Miravia I "
        "took 42 accounts to +30% GMV QoQ. Today I sit on the partner side of every major UAE platform: "
        "talabat, Careem, Noon, Amazon and Kibsons."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Befit, Eurocake, Flair | talabat, Careem, Noon, Amazon, Kibsons | 50+ markets",
            "bullets": [
                "The partner side of the table across every UAE platform — talabat, Careem, Noon, Amazon, Kibsons and Medex: onboarded our SKUs, manage listings and in-app promotions, and measure every activation against a control brand (SMASH x talabat lifted daily sales +165%, control +4.7%)",
                "Run the weekly stock-risk review by dark store across the delivery platforms, using an AI dashboard we built with Claude to flag where platform POs will not cover demand",
                "Built a Claude-based system that automates campaign planning, market research and KPI reporting, cutting manual work ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 partner accounts to +30% GMV QoQ, turning sales, traffic and conversion data into pricing, assortment and promotion recommendations; reported the Flash Sales channel to the CEO",
                "Onboarded 30+ new stores in two months as PIC Fragrances, using launch promotions and trend-driven products",
                "Created and led the Beauty Club and Hot on Social programmes, giving partner brands extra visibility and positioning Miravia as a beauty destination",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Food-delivery & quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Co-managed Glovo's five XL restaurant chains (KFC, Taco Bell, La Tagliatella, Sushi Shop, Vicio): promotions and promo budgets, in-app visibility campaigns and their return, prep and rider pick-up times, and refund and cancellation disputes",
                "Worked day to day with marketing, logistics and customer support to get campaigns live and keep partner operations running",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Sell-in/sell-out and promotional-effectiveness analysis and performance reports for the chocolate category",
            ],
        },
    ],
    "skills_brand": (  # -> "Partners"
        "portfolio & relationship management, restaurant-chain accounts, promotions & promo budgets, onboarding"
    ),
    "skills_ecommerce": (  # -> "Platforms"
        "talabat, Careem, Noon, Amazon, Kibsons, Medex, Glovo, Miravia: listings, promotions, dark-store availability"
    ),
    "skills_commercial": (  # -> "Cross-functional"
        "Operations, Marketing, Logistics, Customer Support, Finance; reporting to C-level"
    ),
    "skills_data": (  # -> "Data & KPIs"
        "GMV, orders, conversion, promo uplift vs control, ROI, sell-in/sell-out, dashboards"
    ),
    "skills_tools": (
        "Excel (advanced), Google Sheets, Power BI, Looker, Salesforce, Claude / Claude Code, ChatGPT"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Partners",
    "E-Commerce & Digital": "Platforms",
    "Commercial": "Cross-functional",
    "Data & Analytics": "Data & KPIs",
    "Tools": "Tools & AI",
}


def make_job() -> Job:
    return Job(
        id="deliveroo-key-account-manager-restaurants-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"team": "Deliveroo UAE — Restaurants / Account Management",
             "via": "LinkedIn (verified job, posted ~2026-10-06)",
             "note": "Paula has an interview scheduled",
             "group": "Deliveroo is part of DoorDash (with Wolt)"},
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
        "salary_raw": None, "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": "2026-10-06", "raw": job.raw,
        "ai_score": 86, "ai_tier": "Hot",
        "skills_match": [
            "Glovo XL Accounts: restaurant chains on a food-delivery platform — the same model",
            "Miravia: 42 key accounts, +30% GMV QoQ; 30+ stores onboarded in two months",
            "Partner side of talabat, Careem and Noon today (DoFreeze) — knows what partners want from a platform KAM",
            "Promo measurement against control (SMASH x talabat +165% vs +4.7%)",
            "Excel / Sheets, dashboards, Business Administration degree",
        ],
        "missing_skills": [
            "Restaurant-partner work is from 2022-23 (Glovo) and was team-shared, not solo-owned",
            "No Arabic",
        ],
        "sector_fit": "excellent (food delivery key account management; Glovo is the same model)",
        "seniority_fit": "good — KAM title matches her level",
        "red_flags": [
            "DoFreeze is NOT on Deliveroo (talabat, Careem, Noon only) — expect the question",
        ],
        "ats_keywords": ATS,
        "reasoning": "Interview scheduled. Glovo restaurant AM plus current partner-side platform work on the UAE competitors.",
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Interviewing",
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
    cv_pdf = _to_pdf_soffice(cv_docx)

    moved = dest / cv_pdf.name
    shutil.move(str(cv_pdf), str(moved))
    shutil.copy(str(moved), str(dest / "Paula De Francisco - CV.pdf"))
    print("OK", moved.name, "PAGES", _pages(moved))

    stray = cv_pdf.parent.parent
    if stray.exists() and stray.resolve() != final_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
