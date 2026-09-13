"""One-off: CV + cover letter for Amazon "Brand Specialist, AVS — Amazon Now" (quick commerce),
Amazon Middle East and North Africa FZ-LLC, Job ID A10516546. 2026-09-13.

Paula's honest angle: AVS is vendor/account management for brands selling TO Amazon. She has done
both sides: 42 brand accounts at Miravia (Alibaba) and XL accounts at Glovo (platform side), and today
the supplier side of quick commerce at DoFreeze (Careem, talabat, Noon dark-store POs, weekly
stock-risk review, promotions measured vs control). Maps onto the five focus areas: business advice,
selection, availability, traffic, conversion.

Honesty guardrails:
- SQL NOT in profile. JD says "SQL or other analytical tools" -> list Power BI, Looker, Excel (advanced);
  never claim SQL.
- Never "own the forecast" (contributes to monthly sell-in forecast).
- No Amazon Vendor Central experience claimed.
- No Arabic, no sponsorship claim.
- Specialist band: salary possibly under 20k AED/month floor; flagged in the dashboard entry.

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

COMPANY = "Amazon"
TITLE = "Brand Specialist - AVS Amazon Now"
DATE_FOLDER = "2026-09-13"
CONTACT = None

JOB_DESCRIPTION = """\
Brand Specialist, AVS (Amazon Vendor Services) — Amazon Now (quick commerce), Amazon MENA. Job ID A10516546.
Manage end-to-end vendor relationships for strategic brands on Amazon Now. Vendors supply multiple
fulfilment centers; resolve live supply and receiving issues with urgency alongside Ops. Own vendor
relationships as primary point of contact; define and deliver joint business plans across selection,
availability, traffic and conversion; partner with internal teams on priorities, event execution and
operational goals; audit performance metrics and drive continuous improvement across MENA.
Focus areas: Business Advice (financial analysis, opportunity identification); Selection (new product
launches, discoverability); Availability (operational excellence, supply chain problem-solving); Traffic
(marketing and merchandising campaigns); Conversion (promotions, customer journey optimization).
Profile: thrives under daily operational rigor and ambiguity; cross-functional communicator with
ownership mindset; analytical, action-oriented; FMCG, fresh, grocery or quick commerce background a plus.
Basic: Bachelor's degree; English C1+; SQL or other analytical tools for data analysis; 2+ years account
management, project/program management or buying; cross-functional or client-facing environment.
Preferred: process improvement; managing large amounts of data.
"""

ATS = [
    "Brand Specialist", "Amazon Vendor Services", "AVS", "Amazon Now", "quick commerce", "vendor management",
    "vendor relationships", "account management", "key account management", "joint business plans",
    "selection", "availability", "traffic", "conversion", "new product launches", "discoverability",
    "supply chain", "fulfilment centers", "receiving issues", "operations", "promotions", "merchandising",
    "event execution", "customer journey", "financial analysis", "opportunity identification",
    "performance metrics", "continuous improvement", "process improvement", "large data sets",
    "data analysis", "analytical tools", "Power BI", "Looker", "Excel", "FMCG", "grocery",
    "cross-functional", "client-facing", "ownership", "MENA", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Vendor & Key Account Management · Quick Commerce · Availability, Selection & Promotions · FMCG"
    ),
    "professional_summary": (
        "Account manager with 5 years across FMCG, e-commerce and quick commerce, on both sides of the "
        "table: 42 brand accounts at Alibaba's Miravia, XL partners at Glovo, and today the supplier side "
        "of Careem, talabat and Noon dark stores in the UAE, fixing availability, selection and promotions."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG food group (Befit, Eurocake, Smash) | Careem, talabat, Noon, Deliveroo | 50+ markets",
            "bullets": [
                "Run the weekly stock-risk review by dark store for Careem, talabat and Noon: check platform POs against upcoming demand and flag gaps with sales and supply before products go out of stock",
                "Plan promotions and listings with the platforms and measure them against control: SMASH x talabat lifted daily sales +165% (control brand +4.7%)",
                "Launched 6 new products; defined must-stock lists by channel with e-commerce sales and contribute to the monthly sell-in forecast",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Primary point of contact for 42 brand accounts; grew them +30% GMV QoQ through business plans on pricing, selection and promotions",
                "Ran the Flash Sales channel reporting to the CEO; as PIC Fragrances onboarded 30+ new stores in two months",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL partners (KFC, Taco Bell, La Tagliatella) and in-app promotions; helped build the Retail vertical with operations and logistics",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Sell-in/sell-out and promotional-effectiveness analysis on large retail data sets for the chocolate category",
            ],
        },
    ],
    "skills_brand": (  # -> "Vendor Mgmt"
        "joint business plans, key accounts (42 brands), negotiation, business reviews, new launches"
    ),
    "skills_ecommerce": (  # -> "Q-Commerce"
        "Careem, talabat, Noon, Glovo, Miravia: availability, POs, listings, promotions, events"
    ),
    "skills_commercial": (  # -> "Operations"
        "stock-risk reviews, supply issue resolution, cross-functional coordination with Ops & Sales"
    ),
    "skills_data": (  # -> "Data & KPIs"
        "GMV, availability, sell-in/sell-out, promo ROI, conversion, financial analysis, dashboards"
    ),
    "skills_tools": (
        "Excel (advanced), Power BI, Looker, Tableau, SAP, Salesforce, Generative AI (Claude)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Vendor Mgmt",
    "E-Commerce & Digital": "Q-Commerce",
    "Commercial": "Operations",
    "Data & Analytics": "Data & KPIs",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I would like to apply for the Brand Specialist role in the AVS team for Amazon Now. Quick commerce "
        "is my daily environment: as Brand & Marketing Manager at DoFreeze, a UAE food group, I manage how "
        "our brands perform on Careem, talabat and Noon dark stores. Before that I managed brand accounts "
        "from the platform side at Alibaba's Miravia and Glovo. This role joins both sides, and that is "
        "why it appeals to me."
    ),
    "body_paragraph_1": (
        "Your five focus areas are close to my current week. On availability, I run a weekly stock-risk "
        "review by dark store, checking whether platform purchase orders cover upcoming demand and chasing "
        "gaps with sales and supply before products go out of stock. On traffic and conversion, I plan "
        "promotions with the platforms and measure them against a control: a SMASH x talabat campaign "
        "lifted daily sales by 165% while a control brand grew 4.7%. On selection, I launched six new "
        "products and defined must-stock lists by channel with our e-commerce sales team. At Miravia I was "
        "the main contact for 42 brands and grew them 30% GMV quarter on quarter through business plans on "
        "pricing, selection and promotions, and ran the Flash Sales channel reporting to the CEO."
    ),
    "body_paragraph_2": (
        "I do my analysis in Excel, Power BI and Looker, starting with sell-in and sell-out data at "
        "Mondelez. I have not used Amazon Vendor Central or SQL day to day, and I would learn both quickly. "
        "I would bring an FMCG and grocery background, the habit of closing the loop without being chased, "
        "and a clear view of what a vendor needs when a fulfilment center is short."
    ),
    "closing_paragraph": (
        "I am based in Dubai and would welcome the chance to discuss how I could support your vendors on "
        "Amazon Now. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="amazon-brand-specialist-avs-amazon-now-A10516546",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.amazon.jobs/en/jobs/A10516546",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"team": "Amazon Vendor Services (AVS) — Amazon Now", "job_id": "A10516546",
             "entity": "Amazon Middle East and North Africa FZ-LLC",
             "note": "Gaps: no SQL (JD accepts other analytical tools), no Vendor Central."},
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
        "salary_raw": "Not posted (Specialist band — may be near/below 20k AED/month floor)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 72, "ai_tier": "Strong",
        "skills_match": [
            "Key account management: 42 brands at Miravia (+30% GMV QoQ), XL accounts at Glovo",
            "Supplier-side Q-commerce: dark-store POs, weekly stock-risk review (Careem/talabat/Noon)",
            "Promotions measured vs control (SMASH x talabat +165%); 6 launches",
            "FMCG/grocery background (DoFreeze, Mondelez) — explicit plus",
        ],
        "missing_skills": [
            "SQL (JD accepts other analytical tools: Power BI, Looker, Excel)",
            "Amazon Vendor Central / AVS tooling",
        ],
        "sector_fit": "strong — FMCG + quick commerce + marketplace account management",
        "seniority_fit": "slightly below — Specialist vs current Manager title",
        "red_flags": [
            "Specialist band: salary may be under her 20k AED/month floor",
        ],
        "ats_keywords": ATS,
        "reasoning": "Near-exact profile match: account management on platforms + supplier-side quick commerce in the UAE; SQL is the only soft gap.",
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "CV Ready",
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
