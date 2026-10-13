"""One-off: CV for Wahed "Marketing Manager", Sharjah, hybrid (found via Jack & Jill, 2026-10-12;
Lever posting dfa51897). CV only for now; cover letter pending Paula's figures.

Wahed is a Shariah-compliant (interest-free) investing fintech. The role is a hands-on generalist:
integrated plans and calendar, paid search/social against CAC/conversion/ROI, social and content,
email/push/lifecycle, referral and loyalty, influencers/affiliates/community partners/agencies,
events, PR support, reporting. 4–7 yrs; fintech or financial services preferred, not required.

Paula's honest angle:
- DoFreeze is the same hands-on mix: paid social/search, content with her designer + social exec,
  influencer programme from zero (103 creator activations, AED 81 per piece, -30% negotiated, agency
  report audited), affiliate programme with an AI-built landing page, talabat cashback giveaway,
  community activations (running/padel/yoga clubs), incremental-sales measurement vs control.
- Miravia: Beauty Club (loyalty) and Hot on Social programmes; Flash Sales reporting to the CEO.
- Línea Directa Aseguradora: her only financial-services experience (accounting intern, 2019).

Honesty guardrails:
- Glovo told in Paula's own words (2026-10-12): co-managed big restaurant-chain accounts in the XL
  team (KFC, Taco Bell, La Tagliatella, Vicio): promotions, promo budgets, cancellations and
  refunds. Not the Retail vertical, no deal negotiation (confirmed false 2026-10-13). 5 XL accounts; weekly
  review of KFC refunds with the fraud team (no recovered amount — never invent one).
- DoFreeze figures from Paula's own notes (2026-10-13): paid (3.7x first-week ROAS), web (+86% orders),
  email (16K base segmented), events (Saudi Food Show 2026), Befit Crew affiliates. Still no push,
  CAC, webinars or PR claims: those are the gaps.
- SMASH x talabat stays at +165% vs +4.7% control (as in earlier CVs); her notes also give x4.6 during
  the campaign on a different baseline — don't mix the two.
- NIVEA always goes with "three months", so for a non-beauty role it is left out; the L'Oréal brands
  and KIKO are named instead (brands confirmed by Paula 2026-10-13).
- No Arabic; never "own the forecast"; DoFreeze is NOT on Deliveroo.
- 103 creators are activations over 3 campaigns, never "one campaign".

ONE-PAGE standard. Lands under output/2026-10-12/Wahed - Marketing Manager/.
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

COMPANY = "Wahed"
TITLE = "Marketing Manager"
DATE_FOLDER = "2026-10-12"

JOB_DESCRIPTION = """\
Marketing Manager — Wahed (global Shariah-compliant, interest-free investing fintech). Sharjah, hybrid.
Hands-on Marketing Manager to plan, execute and optimise marketing across the full customer journey:
performance marketing, social media, content creation, email marketing, referral programmes,
partnerships, events and communications.
Develop integrated marketing plans; manage the marketing calendar (campaigns, content, launches,
partnerships, events); plan, launch and optimise paid search and social; manage budgets and performance
against CAC, conversion, ROI; manage social media and create content (posts, copy, graphics, short-form
video, articles); email, push and lifecycle campaigns (onboarding, engagement, retention, reactivation);
referral and loyalty initiatives; influencers, affiliates, community partners, agencies; webinars,
seminars, conferences, community activations; support PR and corporate comms; market and competitor
research; regular performance reports; work with Country Management, Product, Compliance, Legal,
Operations, Customer Support and global Marketing; internal approvals for financial promotions.
4–7 years of broad marketing experience, preferably FinTech, financial services, technology or another
fast-growth environment; hands-on content and copywriting; paid media budgets, agencies, influencers,
vendors; strong analytics; Bachelor's in Marketing, Communications, Business or related. Financial
services marketing or understanding of Shariah-compliant finance is an advantage.
"""

ATS = [
    "integrated marketing", "full customer journey", "performance marketing", "paid search", "paid social",
    "Meta Ads", "Google Ads", "social media", "content creation", "copywriting", "short-form video",
    "email marketing", "referral", "loyalty", "partnerships", "influencer marketing", "affiliates",
    "community", "agencies", "events", "budget management", "CAC", "conversion", "ROI", "reporting",
    "market research", "stakeholder management", "financial services",
]

CV_CONTENT = {
    "headline": "Marketing Manager · Performance, Social & Partnerships",
    "professional_summary": (
        "Hands-on marketing manager with 5 years across consumer brands and digital marketplaces. "
        "Brand & Marketing Manager at DoFreeze in Dubai, running paid, social, email, influencer, "
        "affiliate and event marketing with a team of two, and judging campaigns on incremental sales, "
        "not reach. Previously grew 42 brands +30% GMV QoQ at Alibaba's Miravia."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | 7 brands incl. Befit, Eurocake, SMASH | sold in 50+ countries",
            "bullets": [
                "Lead marketing for 7 brands across 50+ markets with a team of two (designer, social media exec): seasonal campaign calendar, 6 product launches, 4 social accounts with weekly creative-hook tests",
                "Paid social and search on Meta and Google Ads: built a dynamic-catalogue retargeting campaign at 3.7x ROAS and AED 34.5 per purchase in week one; shift budget between channels on break-even ROAS",
                "Built the influencer programme from zero: 103 creator activations over 3 waves on ~AED 25K (AED 81 per content piece); compared 4 agencies, negotiated −30% and audited the agency's reach reporting",
                "Measure on incremental sales: the SMASH x talabat purchase-to-enter giveaway lifted daily sales +165% vs +4.7% for a control brand; Befit x Noon added 4,176 incremental units (+31% vs baseline)",
                "Web orders +86% and revenue +57% (Q1 vs Jun–Aug 2026) after adding Judge.me reviews, basket-based bundles and a 30-day replenishment flow; segmented a 16K email base for deliverability",
                "Designed the Befit Crew affiliate programme (BixGrow, personal codes, tiered commissions); ran sampling and events incl. Saudi Food Show 2026 and a Sun & Sand Sports x Fabletics yoga session that led to a listing proposal",
            ],
        },
        {
            "company": "Miravia & AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Beauty & Health department",
            "bullets": [
                "Grew 42 beauty and fragrance brands (incl. L'Oréal Paris, Maybelline, NYX, Redken, KIKO Milano) +30% GMV QoQ through pricing, assortment, promotions and on-site visibility; worked with marketing, product and ops",
                "Spotted the Arabian-perfume trend and grew it into one of Beauty & Health's fastest-growing sub-categories, onboarding 30+ stores in two months (incl. Lattafa and Arabian Oud distributors)",
                "Owned the Flash Sales channel (up to ~30% of B&H sales), reporting to the CEO; created the Beauty Club loyalty programme",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Food & quick-commerce delivery app | 10K+ employees",
            "bullets": [
                "Co-managed 5 XL restaurant accounts (KFC, Taco Bell, Vicio): promotions, in-app visibility, weekly refund-fraud reviews",
            ],
        },
        {
            "company": "Mondelez International · Línea Directa Aseguradora",
            "role": "Early Career",
            "dates": "2019 – 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Spanish direct insurer",
            "bullets": [
                "Category Planning Trainee, Mondelez (Aug 2021 – Aug 2022): sell-in/sell-out and promo analysis, NPD support",
                "Accounting Intern, Línea Directa (Jan – Dec 2019): accounting department of an insurer, working in SAP and Looker",
            ],
        },
    ],
    "skills_brand": (
        "campaign planning, content & copy, social media, influencer & affiliate, events & sampling"
    ),
    "skills_ecommerce": (
        "Meta Ads, Google Ads, Shopify, CRO, email & segmentation, Instagram, TikTok, Noon, talabat"
    ),
    "skills_commercial": (
        "budget management, agency & vendor negotiation, platform partnerships, key account management"
    ),
    "skills_data": (
        "ROI, ROAS, break-even ROAS, incremental uplift vs control, KPI reporting, Looker, Power BI, SAP"
    ),
    "skills_tools": (
        "Claude (AI automation), ChatGPT, Canva, Photoshop, Illustrator, Notion, Excel (Expert)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Marketing",
    "E-Commerce & Digital": "Digital & Performance",
    "Commercial": "Budgets & Partners",
    "Tools": "Tools & AI",
}


def make_job() -> Job:
    return Job(
        id="wahed-marketing-manager-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Sharjah, United Arab Emirates",
        url="https://jobs.lever.co/wahed.com/dfa51897-5e43-4dff-b591-5f8d0c3ce7cb",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"via": "Jack & Jill AI (tracked job, 2026-10-12)",
             "workplace": "Sharjah, hybrid",
             "sector": "FinTech (Shariah-compliant investing)"},
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
        "salary_raw": "Not posted (Jack & Jill estimate AED 180–260K/yr ≈ 15–21.7K/month)",
        "salary_aed_min": 15000, "salary_aed_max": 21700,
        "posted_date": None, "raw": job.raw,
        "ai_score": 72, "ai_tier": "Warm",
        "skills_match": [
            "Hands-on generalist marketing today (DoFreeze): paid social/search, content, influencer, affiliates, partnerships",
            "Influencer programme from zero: 103 creator activations, AED 81 per piece, −30% negotiated, agency report audited",
            "Measured ROI: SMASH x talabat +165% vs +4.7% control (~AED 32K incremental on ~AED 8.7K)",
            "Affiliate programme, talabat cashback giveaway, community activations (running/padel/yoga clubs)",
            "Loyalty: Beauty Club at Miravia; manages a designer + social media exec",
        ],
        "missing_skills": [
            "Fintech / financial-services marketing (only an accounting internship at Línea Directa, 2019)",
            "Email, push and lifecycle CRM (onboarding, retention, reactivation)",
            "App-funnel metrics (CAC, activation); events such as webinars and conferences; PR",
        ],
        "sector_fit": "partial (consumer brands → fintech; preferred, not required)",
        "seniority_fit": "good (4–7 yrs asked; Paula 5)",
        "red_flags": [
            "Salary not posted; the estimate straddles her 20K AED/month floor",
            "Sharjah office (hybrid) — commute from Dubai",
        ],
        "ats_keywords": ATS,
        "reasoning": "Same hands-on marketing mix she runs at DoFreeze, with measured results; gaps are fintech domain and lifecycle CRM.",
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
