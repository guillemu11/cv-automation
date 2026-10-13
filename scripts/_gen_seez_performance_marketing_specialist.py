"""One-off: CV for Seez "Performance Marketing Specialist" (SeezBoost), Dubai, hybrid (found via Jack & Jill,
2026-10-13; Workable hNaEVfAQyXen3bMPQoXf9A). Paula asked for it after being told the fit and pay are weak.

Automotive tech. Runs SeezBoost campaigns for dealer clients: paid social, search, display and email on Google,
Meta, Snapchat, TikTok; account manager for those clients owning CPL/CPA/CAC; design feedback to client teams;
keyword research, media plans, analytics, AI-assisted reporting, SEO. 3–5 yrs on high-budget accounts; Google
Ads depth (Search, Display, PMax, Demand Gen, YouTube); Meta, TikTok, Snapchat, LinkedIn, X. Nice: agency,
automotive.

Paula's honest angle: account management against targets (Glovo XL restaurant accounts with in-app ads;
Miravia 42 brand accounts with on-site visibility), Meta Advantage+ (3.7x first-week ROAS, AED 34.5 per
purchase), budget moved on break-even ROAS, creative feedback to her designer, email segmentation, Claude
reporting automation, AEO/schema markup from profile.yaml.

Honesty guardrails: NO PMax, Demand Gen, YouTube, Snapchat, TikTok/LinkedIn/X Ads, keyword-research, lead-gen
(CPL) or high-budget claims. TikTok is organic only. Glovo is NOT the Retail vertical. Miravia accounts were
beauty and fragrance. Salary estimate AED 10–15K/month, half her current 20K — flagged.

ONE-PAGE standard. Lands under output/2026-10-13/Seez - Performance Marketing Specialist/.
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

COMPANY = "Seez"
TITLE = "Performance Marketing Specialist"
DATE_FOLDER = "2026-10-13"

JOB_DESCRIPTION = """\
Performance Marketing Specialist — Seez (automotive tech: car buying and selling, dealers and importers), Dubai,
hybrid. Drive the SeezBoost product: develop and deploy campaigns across paid social, paid search, display and
email on Google Ads, Meta Ads, Snapchat, TikTok and more. Account manager for SeezBoost clients, owning CPL/CPA
and CAC targets. Design feedback to client teams; analytics and optimisation; keyword research for paid search;
media plans for paid social; campaigns, collaterals and social content for Seez's own channels.
Must: Bachelor's; 3–5 years in performance marketing managing high-budget accounts; Google Ads (Search, Display,
Performance Max, Demand Gen, YouTube); Meta, TikTok, Snapchat, LinkedIn, X; performance reports using AI and
analytics platforms; SEO; communication and presentation of results. Nice: agency multi-client experience,
automotive dealerships, commercial mindset tied to ROI.
"""

ATS = [
    "performance marketing", "Google Ads", "Performance Max", "Meta Ads", "Advantage+", "TikTok", "Snapchat",
    "paid social", "paid search", "display", "email marketing", "account management", "CPL", "CPA", "CAC",
    "ROAS", "media plans", "keyword research", "creative feedback", "reporting", "AI", "analytics", "SEO",
]

CV_CONTENT = {
    "headline": "Performance Marketing · Account Management · AI-First",
    "professional_summary": (
        "Performance marketer and account manager with 5 years across e-commerce and marketplaces. At DoFreeze, "
        "runs Meta and Google Ads against cost-per-purchase and break-even ROAS targets, plus email, creative "
        "testing and AI reporting. Before that, managed brand accounts on the platform side at Alibaba's Miravia "
        "(42 brands, +30% GMV QoQ) and Glovo (KFC, Taco Bell, Vicio)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | 7 brands incl. Befit, Eurocake, SMASH | sold on talabat, Noon, Careem",
            "bullets": [
                "Run paid social and search on Meta and Google Ads: built an Advantage+ catalogue retargeting campaign at 3.7x ROAS and AED 34.5 per purchase in week one; August account at 829K impressions, 2.01% CTR, AED 4.64 CPM",
                "Allocate budget across brands and channels on break-even ROAS net of marketplace commissions; moved Google spend to Meta when its return did not cover the cost",
                "Brief a designer and a social media exec and run weekly creative-hook tests across 4 social accounts; a SMASH giveaway added followers at AED 0.73 each, 8x cheaper than a promoted reel",
                "Measure incrementality, not last touch: SMASH x talabat lifted daily sales +165% vs +4.7% for a control brand; Befit x Noon added 4,176 incremental units (+31% vs baseline)",
                "Email and web: segmented a 16K email base for deliverability and built a 30-day replenishment flow; web orders +86%",
                "Built a Claude-based system that automates campaign planning, content and KPI reporting (~40% less manual work), plus landing pages built with AI agents",
            ],
        },
        {
            "company": "Miravia & AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Marketplace | Beauty & Health department",
            "bullets": [
                "Managed 42 beauty and fragrance brand accounts (incl. L'Oréal Paris, Maybelline, NYX, Redken, KIKO Milano) to +30% GMV QoQ through pricing, promotions and on-site visibility; worked with marketing, product and ops",
                "Owned Flash Sales (up to ~30% of B&H sales), reporting to the CEO; grew Arabian perfume into a top-growing sub-category",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Food & quick-commerce delivery app | 10K+ employees",
            "bullets": [
                "Co-managed 5 XL restaurant accounts (KFC, Taco Bell, Vicio) on GMV, orders, promo spend and in-app ads; read campaign returns to pick activation days",
            ],
        },
        {
            "company": "Mondelez International · Línea Directa Aseguradora",
            "role": "Early Career",
            "dates": "2019 – 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Spanish direct insurer",
            "bullets": [
                "Category Planning Trainee, Mondelez (Aug 2021 – Aug 2022): sell-in/sell-out and promo-effectiveness analysis, NPD support",
                "Accounting Intern, Línea Directa (Jan – Dec 2019): accounting department of an insurer, working in SAP and Looker",
            ],
        },
    ],
    "skills_brand": (
        "Meta Ads (Advantage+, catalogue retargeting), Google Ads, budget allocation, creative testing"
    ),
    "skills_ecommerce": (
        "email & segmentation, Shopify, landing pages, SEO & AEO (schema markup), organic social"
    ),
    "skills_commercial": (
        "brand & partner accounts, promotions, on-site and in-app visibility, KPI targets, client reporting"
    ),
    "skills_data": (
        "ROAS, CPA, CPM, CTR, break-even ROAS, incrementality vs control, Looker, Power BI, Excel (Expert)"
    ),
    "skills_tools": (
        "Claude / Claude Code (AI reporting & automation), ChatGPT, Canva, Photoshop"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Paid Media",
    "E-Commerce & Digital": "Digital & CRM",
    "Commercial": "Account Mgmt",
    "Tools": "AI & Tools",
}


def make_job() -> Job:
    return Job(
        id="seez-performance-marketing-specialist-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://jobs.workable.com/view/hNaEVfAQyXen3bMPQoXf9A/hybrid-performance-marketing-specialist-in-dubai-at-seez",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"via": "Jack & Jill AI (tracked job, 2026-10-13)",
             "workplace": "Dubai, hybrid",
             "sector": "Automotive tech (SeezBoost, dealer clients)"},
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
        "salary_raw": "Not posted (Jack & Jill estimate AED 120–180K/yr ≈ 10–15K/month)",
        "salary_aed_min": 10000, "salary_aed_max": 15000,
        "posted_date": None, "raw": job.raw,
        "ai_score": 45, "ai_tier": "Stretch",
        "skills_match": [
            "Account management against targets: Glovo XL accounts (in-app ads), Miravia 42 brand accounts",
            "Meta Advantage+ retargeting 3.7x first-week ROAS, AED 34.5 per purchase; break-even ROAS budgeting",
            "Creative feedback to her designer; weekly hook tests; email segmentation; Claude reporting automation",
        ],
        "missing_skills": [
            "High-budget Google Ads depth (PMax, Demand Gen, YouTube, Display)",
            "Snapchat, TikTok, LinkedIn and X Ads; lead generation (CPL)",
            "~1 year of hands-on paid media (3–5 asked); no agency or automotive experience",
        ],
        "sector_fit": "weak (automotive lead gen)",
        "seniority_fit": "step down (Specialist; she is a Manager today)",
        "red_flags": [
            "Salary estimate AED 10–15K/month, about half her current 20K",
            "Core asks (Google Ads depth, multi-platform, high budgets) are gaps",
        ],
        "ats_keywords": ATS,
        "reasoning": "Account-management and Meta strengths, but Google Ads depth, multi-platform and lead gen are core gaps; low pay.",
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
