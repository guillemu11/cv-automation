"""One-off: generate Paula's ONE-PAGE CV for **Marketing Specialist (Remote)** hired via a recruiter
for an unnamed "global leader in Technology, Information and Internet" (full-time, work from anywhere).

JD ask: "Marketing Domain Expert" — vertical-specific marketing strategy; market-trend and competitor
analysis; cross-functional alignment with business goals; create/optimise campaign assets (content,
messaging, targeting); monitor metrics and adjust on data. 3+ yrs, analytics tools, digital channels,
customer segmentation, campaigns concept-to-execution. Influences product adoption.

Paula's honest angle: 5 yrs marketing/eCommerce in tech (Alibaba, Glovo) + FMCG; in Dubai owns brand
strategy + campaigns end-to-end for 3 brands (Meta/Google Ads, creators, Shopify, quick-commerce);
competitor/category analysis from Mondelez + KAM; control-group measurement.

Honesty guardrails: no spend figures; forecast not owned; factual "UAE Residence Visa" only.
Wording "Domain Expert" + vague client often = AI-training contract gig — flagged in dashboard.

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

COMPANY = "Remote Tech Client"
TITLE = "Marketing Specialist"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
Marketing Specialist (Remote) — Work from Anywhere, full-time, via recruiter for a global leader in the
Technology, Information and Internet industry. Marketing Domain Expert with deep knowledge of marketing
strategies and execution to drive measurable outcomes; domain-specific marketing frameworks and hands-on
execution.

Responsibilities: develop and refine marketing strategies tailored to specific industry verticals; analyse
market trends and competitor activities to identify opportunities; collaborate with cross-functional teams
to align marketing initiatives with business goals; create and optimise campaign assets including content,
messaging and targeting; monitor performance metrics and adjust strategies based on data-driven insights.

Requirements: Bachelor's in Marketing, Business or related (or equivalent experience); 3+ years in marketing
strategy or domain-specific marketing roles; proficiency in marketing analytics tools and platforms; strong
understanding of digital marketing channels and customer segmentation; experience creating and managing
marketing campaigns from concept to execution. High-impact projects that influence product adoption.
"""

ATS = [
    "marketing strategy", "industry verticals", "market trends", "competitor analysis",
    "cross-functional", "business goals", "campaign assets", "content", "messaging", "targeting",
    "performance metrics", "data-driven insights", "marketing analytics", "digital marketing channels",
    "customer segmentation", "campaigns from concept to execution", "product adoption",
    "Meta Ads", "Google Ads", "eCommerce", "A/B testing", "KPI", "Looker", "Power BI", "remote",
]

CONTENT = {
    "headline": "Marketing Strategy · Digital Campaigns · eCommerce & FMCG",
    "professional_summary": (
        "Marketing manager with 5 years across tech eCommerce (Alibaba, Glovo) and FMCG, building vertical-specific "
        "strategies and running digital campaigns from concept to execution, steered by data and segmentation."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG snacking group (Befit, Eurocake, Smash) | DTC Shopify + quick-commerce | GCC",
            "bullets": [
                "Set marketing strategy for 3 brands by segment and channel (DTC, quick-commerce, retail), aligned with sales and e-commerce on business goals",
                "Run campaigns concept to execution: messaging, content and targeting across Meta Ads, Google Ads and creators; 103 creator activations at AED 81 per content piece",
                "Track KPIs and reallocate on data: SMASH x talabat +165% daily sales vs +4.7% for a control brand; audited agency reports and caught inflated reach",
                "Lead a designer and social media executive producing campaign assets; own the Shopify store, lifting conversion rate and AOV",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's eCommerce marketplace | 100K+ employees",
            "bullets": [
                "Built vertical strategies for 42 beauty and fashion brands using competitor and trend analysis, driving +30% GMV QoQ",
                "Owned the Flash Sales channel, reporting performance and recommendations directly to the CEO",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Delivery & quick-commerce tech leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew XL partners (KFC, Taco Bell, Sushi Shop) with data-led in-app campaigns and promotions, working with product and ops teams",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Analysed market share, competitors and promo effectiveness with Nielsen for the chocolate category",
            ],
        },
    ],
    "skills_brand": (  # label -> "Strategy"
        "marketing strategy, positioning & messaging, customer segmentation, competitor & trend analysis"
    ),
    "skills_ecommerce": (  # label -> "Digital"
        "Meta Ads, Google Ads, creators & UGC, content, Shopify, marketplaces & quick-commerce"
    ),
    "skills_commercial": (  # label -> "Execution"
        "campaigns concept to launch, cross-functional alignment, agency management, team leadership"
    ),
    "skills_data": (  # label -> "Analytics"
        "KPI dashboards, A/B tests, control groups, funnel & conversion analysis, Looker, Power BI"
    ),
    "skills_tools": (  # label -> "Tools"
        "Meta Ads Manager, Google Ads, Shopify, Nielsen, Excel, Canva, Claude (AI agents)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Strategy",
    "E-Commerce & Digital": "Digital",
    "Commercial": "Execution",
    "Data & Analytics": "Analytics",
}


def make_job() -> Job:
    return Job(
        id="remote-tech-client-marketing-specialist-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Remote (Work from Anywhere)",
        url="",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Marketing Specialist (Remote) — recruiter, unnamed tech client",
            "note": "Generalist marketing strategy role; good fit on paper. Vague recruiter post "
                    "('Domain Expert', unnamed client) — possibly AI-training contract; verify before investing time.",
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
        "salary_raw": "Not disclosed (competitive)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 62, "ai_tier": "Warm",
        "skills_match": [
            "5 yrs marketing/eCommerce (3+ required) across tech and FMCG",
            "Campaigns concept to execution: messaging, content, targeting on Meta/Google/creators",
            "Vertical strategy + competitor analysis (Miravia beauty/fashion, Mondelez Nielsen)",
            "Data-driven optimisation: control groups, KPI dashboards, Looker/Power BI",
        ],
        "missing_skills": [
            "Unknown 'domain' vertical — not specified",
            "B2B tech / product-adoption marketing",
        ],
        "sector_fit": "adjacent — tech eCommerce background, current role FMCG",
        "seniority_fit": "good — mid-level specialist, she is over the 3-yr bar",
        "red_flags": [
            "Unnamed client + 'Marketing Domain Expert' wording: often AI-training/annotation contract",
            "Remote/work-from-anywhere — check it's compatible with her employer-sponsored UAE visa",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Requirements are generic and Paula clears all of them. The risk is the posting itself: vague recruiter "
            "listing that may be a freelance AI-training gig rather than a real in-house marketing role."
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
