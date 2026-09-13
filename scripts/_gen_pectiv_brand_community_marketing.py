"""One-off: CV for PECTIV (premium feminine care, Dubai) — "Brand & Community Marketing".
Own online brand positioning/voice, monthly IG & TikTok plans, community + influencer collabs,
represent the brand at events/panels/workshops, weekly Lives with doctors. 2-4 yrs. English req, Arabic plus.

Honest angle: DoFreeze Brand & Marketing Manager (leads designer + social media exec, seasonal content
calendar, 103 creator activations, community activations with running/padel/yoga clubs, samplings);
Miravia beauty KAM (Beauty Club + Hot on Social projects) = premium beauty/personal-care credibility.

Guardrails: no Arabic (plus only, not required), no sponsorship claim, no hosting of Lives/panels
claimed (not in record — flagged). CV only, ONE page. Lands under output/2026-09-13/.
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

COMPANY = "PECTIV"
TITLE = "Brand & Community Marketing"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
PECTIV is a premium feminine care brand, founded by pharmacist Dr. Elias Abboud, offering science-backed
sanitary pads, intimate wipes, and masks designed for healthier, more comfortable periods. We're looking
for a confident, creative person to own PECTIV's online brand positioning and represent the brand at
events and community activities. You will: shape PECTIV's digital brand voice and positioning; create
monthly social media plans (IG & TikTok); engage with our community and support influencer
collaborations; represent PECTIV at events, panels, and workshops; participate in weekly Lives with
doctors and experts. You should have: 2-4 years in brand, community, or digital marketing; strong
communication & presentation skills; experience with social media planning; confidence to represent a
premium brand; English required, Arabic is a plus.
"""

ATS = [
    "brand positioning", "brand voice", "digital brand", "premium brand", "feminine care",
    "social media planning", "monthly content plan", "Instagram", "TikTok", "community engagement",
    "community management", "influencer collaborations", "events", "panels", "workshops", "Lives",
    "brand ambassador", "communication", "presentation skills", "digital marketing", "beauty",
    "personal care", "health & wellness", "FMCG", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Premium Brand Voice · Social Planning (IG & TikTok) · Community & Influencers · Events"
    ),
    "professional_summary": (
        "Brand and community marketer with 5 years across FMCG, beauty and e-commerce, now leading brand "
        "and social for UAE consumer brands. I shape brand voice, plan monthly Instagram and TikTok content, "
        "build creator and community programmes and represent brands at activations and partner meetings."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG food group (Befit, Eurocake, Smash) | Health & fitness brand Befit | 50+ markets",
            "bullets": [
                "Own brand positioning and voice for three brands, incl. health-focused Befit; lead a designer and a social media executive on monthly Instagram and TikTok plans tied to seasonal moments (Ramadan, Fitness Month, New Year)",
                "Built influencer marketing from zero: 103 creator activations across 3 campaigns and 4 agencies; SMASH x talabat lifted daily sales +165% (control brand +4.7%)",
                "Represent the brands at samplings and community activations with running, padel and yoga clubs; launched an affiliate programme for inbound creators with multilingual AI content briefs",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Created and led the Beauty Club and Hot on Social projects, positioning Miravia as a beauty and lifestyle destination",
                "Managed 42 beauty, fragrance and fashion brands, growing them +30% GMV QoQ; reported directly to the CEO on Flash Sales",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build the Retail vertical, onboarding fashion, lifestyle and beauty brands; ran activations with XL partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Supported the Milka Spread and Mini Suchard launches with promo and sell-out analysis",
            ],
        },
    ],
    "skills_brand": (  # -> "Brand"
        "brand positioning, brand voice, premium brand, launches, samplings, events & activations"
    ),
    "skills_ecommerce": (  # -> "Social"
        "monthly IG & TikTok plans, content calendar, UGC, trend monitoring, Meta Ads"
    ),
    "skills_commercial": (  # -> "Community"
        "influencers & creators, agencies, communities & clubs, partners (talabat, Noon, Careem)"
    ),
    "skills_data": (  # -> "Insights"
        "content & campaign performance, control-group measurement, engagement, ROI"
    ),
    "skills_tools": (
        "Canva, Adobe Photoshop & Illustrator, Meta Business Suite, Shopify, Generative AI (Claude, ChatGPT)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand",
    "E-Commerce & Digital": "Social",
    "Commercial": "Community",
    "Data & Analytics": "Insights",
}


def make_job() -> Job:
    return Job(
        id="pectiv-brand-community-marketing-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"note": "Premium feminine care brand founded by pharmacist Dr. Elias Abboud. 2-4 yrs."},
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
        "salary_raw": "Not posted (2-4 yrs band — likely below 20k AED/month floor)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 62, "ai_tier": "Good",
        "skills_match": [
            "Brand voice/positioning for 3 UAE brands incl. health-focused Befit",
            "Monthly IG & TikTok plans; leads designer + social media exec",
            "Influencers: 103 creator activations; communities (running, padel, yoga)",
            "Beauty background: Miravia Beauty Club & Hot on Social",
        ],
        "missing_skills": ["Hosting Lives / speaking on panels — not in record", "Feminine care / health category"],
        "sector_fit": "adjacent — beauty & health-focused FMCG, not feminine care",
        "seniority_fit": "slightly above — 2-4 yrs vs ~5 yrs + Manager title",
        "red_flags": ["Small founder-led brand: salary likely below floor", "Arabic is a plus (she has none)"],
        "ats_keywords": ATS,
        "reasoning": "Social planning, community and influencer work match closely; category and on-camera Lives are the gaps.",
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


def _pages(pdf: Path) -> int:
    from pypdf import PdfReader
    return len(PdfReader(str(pdf)).pages)


def main() -> None:
    job = make_job()
    register_in_dashboard(job)

    final_dir = settings.output_dir / DATE_FOLDER / f"{COMPANY} - {TITLE}"
    dest = final_dir / "01_CV"
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
