"""One-off: generate Paula's CV for **Sporty Group — general talent community**
("Interested in working for Sporty?"), GLOBAL, remote-first. No specific opening: candidates
pick an area; Paula targets **Marketing & Communications**.

Sporty: sport & gaming consumer products used by millions daily (SportyBet), teams across
Africa, Europe and South America, partners of Real Madrid and LaLiga. Culture: high volume,
high accountability, high speed, real ownership. Contract: B2B or B2C arrangement.

Paula's honest angle: consumer-platform growth at scale (Glovo app, Alibaba's Miravia
marketplace, Noon/talabat activations) + incrementality-measured campaigns + paid social +
influencer built from zero + AI automation (ship fast) + multi-market (50+) + native Spanish
(LaLiga / Real Madrid / LATAM relevance).

Honesty guardrails:
- No iGaming / sports-betting experience, no CRM/retention-marketing platform, no app-install
  (UA) campaigns claimed. No Arabic. Factual "UAE Residence Visa" only.
- Flags: remote B2B/B2C contract would NOT sponsor her UAE visa (currently employer-sponsored);
  sector is sports betting.

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

COMPANY = "Sporty Group"
TITLE = "Marketing & Communications"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
Interested in working for Sporty? GLOBAL talent community (no specific opening). Sporty builds
real sport and gaming products used by millions of people every day. Remote-first, global company
with teams across Africa, Europe and South America: high volume, high accountability, high speed.
Partners of Real Madrid and LaLiga. Real autonomy, genuine ownership, build things that touch
millions of people. Areas include Marketing & Communications, Business Development & Partnerships,
Product, Data & Analytics, Operations. Application asks: LinkedIn, area of interest, English
proficiency, salary expectations, years of experience, B2B or B2C arrangement.
"""

ATS = [
    "marketing", "communications", "growth", "brand", "consumer products", "digital products",
    "millions of users", "performance marketing", "paid social", "Meta Ads", "Google Ads",
    "A/B testing", "influencer marketing", "creators", "partnerships", "sports", "LaLiga",
    "multi-market", "Africa", "Europe", "South America", "LATAM", "remote", "ownership",
    "high speed", "ROAS", "ROI", "conversion", "retention", "incrementality", "agencies",
    "team leadership", "generative AI", "automation", "Spanish", "English",
]

CONTENT = {
    "headline": (
        "Growth & Brand Marketing · Consumer Platforms · Paid Social & Influencer · Multi-market"
    ),
    "professional_summary": (
        "Growth-minded marketer with 5 years at consumer platforms and brands: Glovo's app, Alibaba's "
        "Miravia marketplace (+30% GMV QoQ across 42 accounts) and, today, brand, paid social and "
        "influencer for three FMCG brands across 50+ markets. Measures on incrementality, ships fast "
        "with AI automation. Native Spanish, English C1."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Smash) | 50+ markets | Noon, Talabat, Careem, Deliveroo + Shopify",
            "bullets": [
                "Run campaigns measured on incremental results, not reach: SMASH x talabat lifted daily sales +165% vs +4.7% for a control brand; Befit x Noon 'New Year, New Me' added 4,176 incremental units (+31% vs baseline)",
                "Built the influencer programme from zero: 103 creator activations across 3 campaigns at AED 81 per content piece; plan Meta and Google Ads with creative A/B testing and report ROAS",
                "Lead a team of two (designer, social media executive) and manage 4 agencies (fees negotiated -30%); built a generative-AI system (Claude) for planning, content and KPI reporting, cutting manual work ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew 42 brand accounts +30% GMV QoQ through onsite campaigns, promotions, pricing and content; owned the Flash Sales channel reporting to the CEO",
                "Created the Beauty Club and Hot on Social community projects to drive loyalty; tracked traffic, conversion, ROI, ROAS and retention weekly",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce app leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew XL partners (KFC, Taco Bell, Sushi Shop) with in-app promotions and data-led activation plans; helped build the Retail vertical beyond food delivery",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Category planning & analytics",
            "bullets": [
                "Analysed promotional effectiveness and sell-in/sell-out; supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # label -> "Growth & Brand"
        "brand strategy, campaign planning, launches, influencer & creators, communications"
    ),
    "skills_ecommerce": (  # label -> "Digital & Performance"
        "Meta Ads, Google Ads, creative A/B testing, social (Instagram, TikTok), EDM, CRO, Shopify"
    ),
    "skills_commercial": (  # label -> "Partners & Teams"
        "platform partnerships, agencies (4), team leadership (2), negotiation, cross-functional delivery"
    ),
    "skills_data": (  # label -> "Data & KPIs"
        "incrementality vs control, ROAS, ROI, GMV, conversion, retention, Power BI, Looker"
    ),
    "skills_tools": (  # label -> "Tools"
        "Generative AI (Claude, ChatGPT), Meta Ads Manager, Google Ads, Shopify, Canva, Adobe, Excel"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Growth & Brand",
    "E-Commerce & Digital": "Digital & Performance",
    "Commercial": "Partners & Teams",
    "Data & Analytics": "Data & KPIs",
}


def make_job() -> Job:
    return Job(
        id="sporty-group-talent-community-marketing-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Remote (Global)",
        url="https://job-boards.greenhouse.io/sportygroup",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Sporty Group talent community Marketing & Communications",
            "note": "General talent pool, no opening. Consumer-platform growth fit; gaps: no iGaming, "
                    "no CRM/UA. Remote B2B/B2C = no UAE visa sponsorship.",
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
        "salary_raw": "Not disclosed (talent pool)", "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 58, "ai_tier": "Possible",
        "skills_match": [
            "Consumer-platform growth: Glovo app, Miravia (+30% GMV QoQ, 42 accounts)",
            "Incrementality-measured campaigns (SMASH x talabat +165% vs control) + Meta/Google Ads",
            "Influencer programme from zero (103 creators) + AI automation for speed",
            "Native Spanish — relevant to LaLiga / Real Madrid and LATAM markets",
        ],
        "missing_skills": ["No iGaming / sports-betting experience", "No CRM / user-acquisition (app installs)"],
        "sector_fit": "partial — sport & gaming consumer apps (sports betting)",
        "seniority_fit": "unknown — general talent pool",
        "red_flags": [
            "Remote B2B/B2C contract: no UAE employer visa (hers is employer-sponsored)",
            "Sports-betting sector",
            "No specific opening — passive pipeline",
        ],
        "ats_keywords": ATS,
        "reasoning": "Talent-community application; low effort, positioned as growth/brand marketer for consumer platforms.",
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
