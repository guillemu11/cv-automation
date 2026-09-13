"""One-off: CV + cover letter for PAX (Hayati®) "Field Marketing Executive", UAE.
Consumer electronics / vaping brand; role visits independent retail (IR) stores, POSM, in-store
displays, trade marketing, offline launches/seasonal promos, retail outlet database, partners/suppliers.

Paula's honest angle: FMCG brand & trade marketing in the UAE at DoFreeze — trade & shopper plans by
channel, retail execution in modern trade, 6 launches, seasonal campaigns (Ramadan, Back to School,
Fitness Month, New Year) with samplings, community activations (running/padel/yoga clubs), agencies
and suppliers, works with the social team she leads (designer + social media exec). Measured results
(SMASH x talabat +165% vs control +4.7%). Retail floor grounding at Massimo Dutti. Account management
at Miravia (42 accounts) and Glovo (retail vertical) = relationship-building with retail partners.

Honesty guardrails:
- NO claim of daily IR store-visit routes, POSM deployment ownership or an outlet database: not in her
  record. The letter frames these as what she would build.
- NO consumer electronics / vaping experience (preferred, not required) — not claimed.
- UAE driving licence + own work vehicle: UNKNOWN — not claimed anywhere; flagged for Guille.
- No Arabic, no sponsorship claim. Executive band: likely below 20k AED/month floor (flagged).

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
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "PAX (Hayati)"
TITLE = "Field Marketing Executive"
DATE_FOLDER = "2026-09-13"
CONTACT = None

JOB_DESCRIPTION = """\
Field Marketing Executive — PAX (Hayati®), UAE. Consumer electronics (Hayati, Quokka, Moxy, Liora,
Finebar, Philia); offices UK, Germany, UAE; pre-IPO (NASDAQ).
Visit independent retail (IR) stores to strengthen retailer relationships, improve brand visibility,
secure premium in-store display and execute trade marketing. Execute regional field marketing across
retail stores, manage POSM deployment, develop local retail partnerships, build and update a regional
retail outlet database, expand visibility and retail coverage. Plan and deliver offline campaigns
(product launches, seasonal promotions, regional events) from planning to completion. Monitor market
trends, consumer insights and competitors; provide market analysis for localized strategies. Manage
local partners and suppliers; support materials, logistics and operations. Work with Brand, GTM and
Social Media teams on integrated campaigns.
Needs: Bachelor's; 3+ yrs field / regional / offline marketing (consumer electronics or vaping
preferred); communication, stakeholder management, project coordination; UAE market and local retail
landscape; independently execute regional campaigns and offline events; execution, channel development,
problem-solving; results-driven, data-oriented, frequent field travel; valid UAE driving licence and
own work vehicle.
"""

ATS = [
    "Field Marketing", "field marketing executive", "trade marketing", "retail execution",
    "independent retail", "point of sale", "POSM", "in-store visibility", "display", "merchandising",
    "retail partnerships", "retailer relationships", "retail coverage", "outlet database",
    "offline marketing", "product launches", "seasonal promotions", "events", "activations",
    "sampling", "market trends", "consumer insights", "competitor analysis", "suppliers", "agencies",
    "logistics", "Brand", "GTM", "social media", "integrated campaigns", "stakeholder management",
    "project coordination", "channel development", "data-driven", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Trade & Field Marketing · Retail Execution & Visibility · Launches, Promotions & Events · "
        "Retail Partnerships"
    ),
    "professional_summary": (
        "Brand and trade marketer with 5 years in FMCG, retail and quick-commerce, now in the UAE. "
        "I plan and deliver launches, seasonal promotions, samplings and community events, and manage "
        "retail partners, agencies and suppliers, measuring every activation on sales."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG food group (Befit, Eurocake, Smash) | Modern trade & quick-commerce | 50+ markets",
            "bullets": [
                "Develop trade and shopper marketing plans by channel and support retail execution in UAE modern trade; launched 6 new products from brief and packaging to go-to-market",
                "Run offline and seasonal campaigns (Ramadan, Back to School, Fitness Month) with product samplings and community activations with running, padel and yoga clubs",
                "Manage agencies and suppliers and lead a designer and a social media executive to deliver integrated campaigns; SMASH x talabat lifted daily sales +165% (control brand +4.7%)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 brand partners and grew them +30% GMV QoQ through promotions, visibility and campaign calendars",
                "Expanded coverage as PIC Fragrances: onboarded 30+ new stores in two months, incl. Arabian Oud, Lattafa and Ajmal distributors",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Ran marketing activations with XL partners (KFC, Taco Bell, Sushi Shop) and helped build the Retail vertical",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Sell-in/sell-out and promotional-effectiveness analysis; supported the Milka Spread and Mini Suchard launches",
            ],
        },
    ],
    "skills_brand": (  # -> "Field & Trade"
        "trade & shopper marketing, retail execution, in-store visibility, sampling, launches & seasonal promotions"
    ),
    "skills_ecommerce": (  # -> "Events & Campaigns"
        "offline activations, community events, integrated campaigns with brand & social teams, influencers"
    ),
    "skills_commercial": (  # -> "Partners"
        "retail partner & account management (42), agencies & suppliers, negotiation, logistics coordination"
    ),
    "skills_data": (  # -> "Insights & KPIs"
        "market & competitor analysis, sell-in/sell-out, promo ROI, control-group measurement, dashboards"
    ),
    "skills_tools": (
        "Excel (advanced), Google Sheets, Power BI, Looker, SAP, Salesforce, Canva, Generative AI (Claude)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Field & Trade",
    "E-Commerce & Digital": "Events",
    "Commercial": "Partners",
    "Data & Analytics": "Insights",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I would like to apply for the Field Marketing Executive role at PAX. I am a brand and trade "
        "marketer based in Dubai, currently Brand & Marketing Manager at DoFreeze, a UAE food group, where "
        "I take our brands to market through modern trade and quick-commerce. Hayati's growth in the UAE, "
        "built one retailer at a time, is the kind of hands-on marketing I want to do more of."
    ),
    "body_paragraph_1": (
        "Most of what this role delivers is already part of my work. I build trade and shopper marketing "
        "plans by channel, and I have launched six products from brief to go-to-market. I plan and run "
        "offline campaigns around seasonal moments such as Ramadan, Back to School and Fitness Month, with "
        "product samplings and activations with running, padel and yoga communities. I coordinate agencies "
        "and suppliers and lead a designer and a social media executive, so campaigns land consistently "
        "in store and online. And I measure results on sales: our SMASH x talabat campaign lifted daily "
        "sales by 165% while a control brand grew 4.7%. Before Dubai I managed 42 brand partners at "
        "Alibaba's Miravia and ran partner activations at Glovo, which taught me how to earn a partner's "
        "trust and turn it into visibility."
    ),
    "body_paragraph_2": (
        "To be transparent: I have not worked in consumer electronics or vaping, and my retail work so far "
        "has been with larger chains and platforms rather than daily visits to independent stores. That "
        "is the part I would build first: a clear outlet database, a visit plan, and a simple way to track "
        "display wins and POSM compliance, so the team can see which stores and placements actually "
        "move sales."
    ),
    "closing_paragraph": (
        "I would welcome the chance to discuss how I could grow Hayati's presence at the point of sale "
        "across the UAE. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="pax-hayati-field-marketing-executive-2026-09",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates",
        url="",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"brand": "Hayati® (PAX Group) — consumer electronics / vaping",
             "note": "Field role: IR store visits; requires UAE driving licence + own vehicle (unconfirmed)."},
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
        "salary_raw": "Not posted (Executive band — likely below 20k AED/month floor)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 50, "ai_tier": "Possible",
        "skills_match": [
            "Trade & shopper marketing plans by channel; retail execution in UAE modern trade",
            "6 product launches; seasonal campaigns with samplings and community events",
            "Agencies, suppliers and integrated campaigns with social team (leads 2)",
            "Partner management: 42 accounts at Miravia, XL partners at Glovo",
        ],
        "missing_skills": [
            "Hands-on IR store visits, POSM deployment, outlet database",
            "Consumer electronics / vaping (preferred)",
            "UAE driving licence + own work vehicle (unconfirmed)",
        ],
        "sector_fit": "adjacent — FMCG trade marketing, not electronics/vaping",
        "seniority_fit": "below level — Executive field role vs Manager title",
        "red_flags": [
            "Requires UAE driving licence and own vehicle",
            "Executive band: salary likely under 20k AED/month floor",
            "Vaping category",
        ],
        "ats_keywords": ATS,
        "reasoning": "Trade/offline marketing transfers; field-sales-style IR visits and car requirement are the blockers.",
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
    dest = final_dir / "01_CV_y_Carta"
    dest.mkdir(parents=True, exist_ok=True)

    cv_docx = cv._fill_template(CV_CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)

    for src, short in ((cv_pdf, "Paula De Francisco - CV.pdf"),
                       (cl_pdf, "Paula De Francisco - Cover Letter.pdf")):
        moved = dest / src.name
        shutil.move(str(src), str(moved))
        shutil.copy(str(moved), str(dest / short))
        print("OK", moved.name, "PAGES", _pages(moved))

    stray = cv_pdf.parent.parent
    if stray.exists() and stray.resolve() != final_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
