"""One-off: CV + application email for The Giving Movement "Head of Ecommerce", Dubai (LinkedIn
network post + hiring flyer, seen 2026-10-12). Apply by email to careers@thegivingmovement.com with
the role in the subject line; the post author also asks for a DM (author's name not provided).

The brief: own the digital P&L, lead e-commerce trading, drive profitable customer growth; someone
who has scaled an e-commerce business before and connects trading, acquisition, conversion and
retention into one growth engine. Ideally fashion, lifestyle or premium DTC. TGM is a Dubai-born
sustainable activewear / streetwear DTC brand (founded 2020, US$15M Series A, GCC-led).

Paula's honest angle, built around the four levers the post names:
- Trading: Miravia (Alibaba) 42 fashion / beauty / fragrance accounts, +30% GMV QoQ; Flash Sales
  channel against P&L targets, reporting to the CEO.
- Acquisition + conversion: DoFreeze Shopify D2C store end-to-end (CRO, AOV), Meta / Google Ads,
  influencer programme from zero to 25–50 creators per campaign.
- Retention: Miravia Beauty Club (customer loyalty); retention tracked with conversion and ROAS.
- Measurement: promos read against control (SMASH x talabat +165% vs +4.7%); Claude reporting system.
- Fashion grounding: Glovo Retail vertical (fashion brands), Inditex, CUNEF e-commerce / fashion.

Honesty guardrails:
- STRETCH: she has never held a Head title nor owned a full D2C digital P&L. The CV never claims
  either; it shows channel-level P&L targets (Flash Sales) and store ownership only.
- No Shopify CRO / AOV figures (none on record). No agencies count. DoFreeze is NOT on Deliveroo.
- Never "own the forecast". No visa / sponsorship claim in the email; visa line in CV from profile.

Nothing is sent: the email and the LinkedIn DM land in 03_Outreach and in the dashboard outreach store
for Paula to send from her hotmail. ONE-PAGE CV. Lands under output/2026-10-12/.
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

from career_ops import outreach_store
from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "The Giving Movement"
TITLE = "Head of Ecommerce"
DATE_FOLDER = "2026-10-12"
JOB_ID = "the-giving-movement-head-of-ecommerce-2026-10"
CAREERS_EMAIL = "careers@thegivingmovement.com"

JOB_DESCRIPTION = """\
Head of Ecommerce — The Giving Movement (TGM), Dubai, UAE. Shared via a LinkedIn network post and a
hiring flyer (2026-10-12). Apply: careers@thegivingmovement.com with the role in the subject line, or
DM the post author.
"Build the digital growth engine behind The Giving Movement": own the digital P&L; lead Ecommerce
trading; drive profitable customer growth.
Looking for someone who has done this before: scaled an e-commerce business profitably, owns the
numbers, and connects trading, acquisition, conversion and retention into one growth engine. Not just
someone who manages campaigns or agencies, but someone who takes real ownership of the digital P&L.
Ideally a strong track record in fashion, lifestyle or premium DTC brands.
Context: Dubai-born sustainable activewear / streetwear DTC brand (founded 2020), US$15M Series A,
growing across the GCC and internationally.
"""

ATS = [
    "Head of Ecommerce", "e-commerce", "ecommerce", "digital P&L", "P&L", "ecommerce trading",
    "trading", "profitable growth", "customer growth", "growth engine", "acquisition", "conversion",
    "retention", "CRO", "AOV", "D2C", "DTC", "Shopify", "merchandising", "UX", "checkout",
    "performance marketing", "Meta Ads", "Google Ads", "influencer", "EDM", "loyalty", "ROAS",
    "GMV", "promotions", "pricing", "assortment", "fashion", "lifestyle", "beauty", "marketplace",
    "Alibaba", "team leadership", "dashboards", "AI", "automation", "Dubai", "UAE", "GCC",
]

CV_CONTENT = {
    "headline": (
        "E-Commerce Growth · Trading, Acquisition, Conversion & Retention · "
        "Fashion, Beauty & D2C · AI Automation"
    ),
    "professional_summary": (
        "E-commerce professional with 5 years across fashion, beauty and consumer brands. At Alibaba's "
        "Miravia I grew 42 fashion and beauty accounts +30% GMV QoQ and ran the Flash Sales channel to P&L "
        "targets; in Dubai I run a Shopify D2C store, paid media and marketplaces, leading a team of two."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Befit, Eurocake, Flair | Shopify D2C + Careem, talabat, Noon",
            "bullets": [
                "Conversion: own the Shopify D2C store end-to-end (catalogue, collections, UX, discounts, checkout), lifting conversion rate and AOV through data-led merchandising",
                "Acquisition: plan and optimise Meta and Google Ads (audiences, creative A/B tests, social, EDM) on ROAS; built the influencer programme from zero to 25–50 creators per campaign",
                "Trading: run promotions on Careem, talabat and Noon and read them against control: SMASH x talabat lifted daily sales +165% (control brand +4.7%)",
                "Lead a team of two (designer, social media exec); built a Claude-based system that automates campaign planning and KPI reporting, cutting manual work ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace in Spain | 100K+ employees",
            "bullets": [
                "Managed 42 fashion, beauty and fragrance brand accounts to +30% GMV QoQ through assortment, pricing and promotions, reading traffic, conversion and retention data",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and running commercial plans against P&L targets",
                "Created the Beauty Club and Hot on Social programmes to build customer loyalty and visibility; onboarded 30+ new stores in two months as PIC Fragrances",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build the Retail vertical, onboarding fashion and lifestyle brands, and grew XL partner GMV (KFC, Taco Bell, Sushi Shop) through promotions and bespoke activations",
            ],
        },
        {
            "company": "Mondelez International · Massimo Dutti (Inditex)",
            "role": "Category Planning Trainee · Sales Associate",
            "dates": "Jun 2018 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG category planning | Premium fashion retail floor",
            "bullets": [
                "Sell-in/sell-out and promo-effectiveness analysis at Mondelez; Inditex grounding in fashion retail, visual merchandising and premium customer experience",
            ],
        },
    ],
    "skills_brand": (  # -> "Trading & P&L"
        "trading calendars, assortment, pricing & promotions, promo uplift vs control, P&L-aligned plans"
    ),
    "skills_ecommerce": (  # -> "D2C & Conversion"
        "Shopify, collections & merchandising, UX, CRO, AOV, checkout; Noon, talabat, Careem"
    ),
    "skills_commercial": (  # -> "Acquisition & Retention"
        "Meta Ads, Google Ads, influencer & UGC, EDM, community & loyalty programmes"
    ),
    "skills_data": (  # -> "Data & Team"
        "GMV, ROAS, conversion, retention, dashboards; team of two; reporting to the CEO"
    ),
    "skills_tools": (
        "Shopify, Meta Ads Manager, Google Ads, Power BI, Looker, Excel (Expert), Claude / Claude Code"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Trading & P&L",
    "E-Commerce & Digital": "D2C & Conversion",
    "Commercial": "Acquisition & Retention",
    "Data & Analytics": "Data & Team",
    "Tools": "Tools & AI",
}

EMAIL_SUBJECT = "Head of Ecommerce – Paula De Francisco"
EMAIL_BODY = (
    "Dear Hiring Team,\n\n"
    "I'd like to apply for the Head of Ecommerce role at The Giving Movement.\n\n"
    "You're looking for someone who connects trading, acquisition, conversion and retention into one "
    "growth engine and owns the numbers. That is the work I've done across marketplace and D2C over the "
    "last five years:\n\n"
    "- Trading: at Alibaba's Miravia I managed 42 fashion, beauty and fragrance brands to +30% GMV "
    "quarter on quarter, and owned the Flash Sales channel against P&L targets, reporting directly to "
    "the CEO.\n"
    "- Acquisition and conversion: in Dubai I run a Shopify D2C store end to end (merchandising, UX, "
    "checkout) and its Meta and Google Ads, and built an influencer programme from zero to 25–50 "
    "creators per campaign.\n"
    "- Retention: at Miravia I created the Beauty Club to build customer loyalty, and tracked retention "
    "alongside conversion and ROAS.\n"
    "- Measurement: I read every promotion against a control (SMASH x talabat: +165% daily sales vs "
    "+4.7% for the control brand) and built a Claude-based system that automates our KPI reporting.\n\n"
    "I'm based in Dubai and lead a team of two. My fashion grounding comes from Inditex, Glovo's Retail "
    "vertical and a CUNEF degree specialised in e-commerce and the fashion industry.\n\n"
    "My CV is attached. I'd welcome the chance to talk about TGM's next phase of growth.\n\n"
    "Best regards,\n"
    "Paula De Francisco\n"
    "+971 50 386 3656 · paulich98@hotmail.com\n"
    "linkedin.com/in/paula-de-francisco-perez-92a13119a"
)

LINKEDIN_DM = (
    "Hi [first name], I saw your post about the Head of Ecommerce role at The Giving Movement. I'm in "
    "Dubai, with 5 years in e-commerce across fashion, beauty and D2C: at Alibaba's Miravia I grew 42 "
    "brand accounts +30% GMV QoQ and ran the Flash Sales channel against P&L targets, and today I run a "
    "Shopify store, paid media and marketplaces. I've just applied via careers@ and would be glad to "
    "send you my CV here too. Paula"
)


def make_job() -> Job:
    return Job(
        id=JOB_ID,
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url=f"mailto:{CAREERS_EMAIL}?subject=Head%20of%20Ecommerce",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"via": "LinkedIn network post + hiring flyer (2026-10-12)",
             "apply": f"{CAREERS_EMAIL}, role in the subject line; or DM the post author",
             "level": "Head of"},
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
        "salary_raw": "Not posted (Head-level: likely above her 20k AED/month floor)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 55, "ai_tier": "Stretch",
        "skills_match": [
            "Miravia (Alibaba): 42 fashion / beauty / fragrance accounts, +30% GMV QoQ; Flash Sales channel vs P&L targets, CEO reporting",
            "DoFreeze: Shopify D2C store end-to-end (CRO, AOV), Meta / Google Ads, influencer programme 25–50 creators",
            "Promo measurement vs control (SMASH x talabat +165%); Claude reporting automation",
            "Fashion grounding: Glovo Retail vertical, Inditex, CUNEF e-commerce / fashion specialisation",
            "Already in Dubai; leads a team of two",
        ],
        "missing_skills": [
            "Never held a Head of Ecommerce title or owned a full D2C digital P&L",
            "No record of scaling a fashion DTC site herself (her D2C store is F&B)",
            "No quantified CRO / AOV / retention results on record",
        ],
        "sector_fit": "good (fashion / lifestyle e-commerce via Miravia, Glovo Retail, Inditex)",
        "seniority_fit": "stretch (Head-level; 5 yrs, Manager / KAM roles so far)",
        "red_flags": [
            "Post asks for 'someone who has done this before' and owns the digital P&L",
        ],
        "ats_keywords": ATS,
        "reasoning": "Strong fashion / beauty e-commerce trading and D2C hands-on work, but a Head-level brief that wants prior ownership of a digital P&L she has not had.",
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "CV Ready",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def register_outreach() -> None:
    cpath = settings.data_dir / "contacts" / f"{JOB_ID}.json"
    cpath.parent.mkdir(parents=True, exist_ok=True)
    if not cpath.exists():
        cpath.write_text(json.dumps([{
            "name": "The Giving Movement Careers",
            "title": "Careers inbox (apply with the role in the subject line)",
            "company": COMPANY,
            "email": CAREERS_EMAIL,
            "linkedin_url": None,
            "role_type": "Careers inbox",
            "source": "Hiring flyer shared in a LinkedIn network post (2026-10-12)",
        }], indent=2, ensure_ascii=False), encoding="utf-8")

    cid = outreach_store.contact_id("The Giving Movement Careers", None)
    if cid not in outreach_store.load(JOB_ID):
        outreach_store.add_version(JOB_ID, cid, "email", f"Subject: {EMAIL_SUBJECT}\n\n{EMAIL_BODY}")


def write_outreach_file(final_dir: Path, cv_name: str) -> Path:
    out_dir = final_dir / "03_Outreach"
    out_dir.mkdir(parents=True, exist_ok=True)
    md = (
        "# The Giving Movement — Head of Ecommerce: email + LinkedIn DM\n\n"
        "Send both from Paula's own accounts. Nothing has been sent.\n\n"
        "## 1. Email (from paulich98@hotmail.com)\n\n"
        f"**To:** {CAREERS_EMAIL}\n"
        f"**Subject:** {EMAIL_SUBJECT}\n"
        f"**Attach:** `../01_CV_y_Carta/{cv_name}`\n\n"
        "---\n\n"
        f"{EMAIL_BODY}\n\n"
        "---\n\n"
        "## 2. LinkedIn DM to the post author\n\n"
        "> The post says \"send me a DM directly\". Replace [first name] before sending.\n\n"
        f"{LINKEDIN_DM}\n"
    )
    p = out_dir / "Email_y_DM_The_Giving_Movement.md"
    p.write_text(md, encoding="utf-8")
    return p


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

    register_outreach()
    print("OK_OUTREACH", write_outreach_file(final_dir, "Paula De Francisco - CV.pdf"))
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
