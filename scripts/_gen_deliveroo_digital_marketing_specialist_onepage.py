"""One-off: generate Paula's ONE-PAGE CV for **Digital Marketing Specialist** at **Deliveroo**,
Dubai (hybrid), Brand & Experience team.

Replaces the 2-page 2026-08-30 version (_gen_deliveroo_digital_marketing_specialist.py) with the
current facts: control-group sell-out results, 103 creator activations / AED 81 per piece,
4 agencies + reporting audit, micro-creator insight, team of two (designer reviews = visual detail).

JD ask: full-funnel digital campaigns (YouTube, Meta, Snapchat, TikTok, programmatic, local
publishers); media planning & scheduling; collaboration with brand + platform teams on social;
ROI/KPI reports and post-campaign analysis; trend monitoring; 3-5 yrs digital/media; local media
landscape; agency experience a plus; test-and-learn; detail in copy and visual design.

Honesty guardrails:
- Paid media documented = Meta + Google. TikTok/Instagram = creator/organic content.
  NO Snapchat, YouTube ads or programmatic claimed.
- Agencies = influencer/UGC agencies she manages, not media-agency tenure.
- Forecast not owned. Factual "UAE Residence Visa" only.

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

COMPANY = "Deliveroo"
TITLE = "Digital Marketing Specialist"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
Digital Marketing Specialist — Deliveroo (part of DoorDash), Dubai Main Office, hybrid. Brand &
Experience team. Manage and execute full-funnel digital marketing campaigns driven by data insights;
collaborate daily with multiple teams and stakeholders; in-depth knowledge of digital tools, platforms
and analytics stacks incl. Meta, Google, TikTok, Snapchat and local publishers; post-campaign analysis
and insight-sharing with stakeholders.

Campaign Management: day-to-day management of digital campaigns, brand consistency across YouTube, Meta,
Snapchat, TikTok and programmatic. Media Planning & Scheduling: develop and execute media plans for
creative and performance efficiency. Collaboration & Innovation: work with brand and platform teams on
new social media ideas and best practices. Performance Reporting: comprehensive ROI and KPI reports.
Trend Monitoring: emerging digital tools, platforms and trends.

Needs: 3-5 years in Digital Marketing or Media; Bachelor's in Marketing or related; strong understanding
of the local media landscape; media planning, media management and campaign implementation; agency
experience good to have; consumer-centric and data-driven; market trends and competition; test-and-learn;
fast-paced; meticulous attention to detail in copywriting and visual design; quick to adopt new tools.
"""

ATS = [
    "digital marketing", "full-funnel", "campaign management", "media planning", "scheduling",
    "Meta", "Google", "TikTok", "social media", "paid social", "performance reporting", "ROI",
    "KPI", "post-campaign analysis", "test-and-learn", "A/B testing", "consumer-centric",
    "data-driven", "agency", "brand consistency", "copywriting", "visual design", "trends",
    "stakeholders", "local media landscape", "UAE", "Dubai", "creators", "UGC",
]

CONTENT = {
    "headline": "Digital Marketing · Paid Social & Creators · Performance Reporting",
    "professional_summary": (
        "Digital marketer with 5 years across FMCG and delivery/e-commerce tech (Glovo, Alibaba), now running full-funnel "
        "Meta, Google and creator campaigns in Dubai, measured with control groups and ROI reporting; Google Digital Marketing certified."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG snacking group (Befit, Eurocake, Smash) | GCC + 50+ markets",
            "bullets": [
                "Plan, schedule and optimise full-funnel paid media on Meta (Facebook & Instagram) and Google Ads: audience building, creative A/B tests, managing spend against ROI and ROAS",
                "Run creator campaigns on Instagram and TikTok built on the UAE calendar (Ramadan, Fitness Month, New Year): 103 creator activations at AED 81 per content piece; found micro-creators (<20K) beat the campaign engagement average 10-40x",
                "Measure sell-out, not just reach: SMASH x talabat lifted daily sales +165% vs +4.7% for a control brand; Befit x Noon added 4,176 incremental units (+31% vs baseline)",
                "Brief 4 agencies (negotiated -30%) and audited their reports, catching reach estimated from followers; lead a designer and social media executive, reviewing all copy and creative",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | 100K+ employees",
            "bullets": [
                "Created the Hot on Social and Beauty Club projects; analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance",
                "Grew 42 brand accounts +30% GMV QoQ; owned the Flash Sales channel, reporting to the CEO",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Delivery & quick-commerce tech leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Delivered data-led marketing activations for XL partners (KFC, Taco Bell, Sushi Shop) with marketing, ops and CX teams",
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
    "skills_brand": (  # label -> "Digital Campaigns"
        "full-funnel campaigns, media planning & scheduling, paid social, creators & UGC, copy review"
    ),
    "skills_ecommerce": (  # label -> "Platforms"
        "Meta (Facebook, Instagram), Google Ads, TikTok & Instagram creators, EDM, talabat & Noon"
    ),
    "skills_commercial": (  # label -> "Collaboration"
        "4 agencies, brand & design teams, platform partners, team of two, stakeholder insight decks"
    ),
    "skills_data": (  # label -> "Performance"
        "ROI / ROAS, KPI reports, post-campaign analysis, A/B tests, control groups, Power BI"
    ),
    "skills_tools": (  # label -> "Tools"
        "Meta Ads Manager, Google Ads, Meta Business Suite, Looker, Excel, Adobe & Canva, Claude"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Digital Campaigns",
    "E-Commerce & Digital": "Platforms",
    "Commercial": "Collaboration",
    "Data & Analytics": "Performance",
}


def make_job() -> Job:
    return Job(
        id="deliveroo-digital-marketing-specialist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (Hybrid)",
        url="https://careers.deliveroo.co.uk/",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={"query": "Deliveroo Digital Marketing Specialist Dubai"},
    )


def register_in_dashboard(job: Job) -> None:
    # Already tracked in data/scored_jobs.json since 2026-08 (same id) — nothing to add.
    return


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
