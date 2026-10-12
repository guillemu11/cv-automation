"""One-off: CV + application email for "Key Account Manager – Noon", Dubai, AED 20,000/month. LinkedIn
hiring post by Mubaraka (Genetic Callnet, recruitment agency), seen 2026-10-12. The client is not named:
"a growing Food & Non-Food business" with two openings, KAM – Amazon and KAM – Noon. Apply by DM with
"AMAZON" or "NOON", or by email to mubaraka@geneticcallnet.com.

The brief: UAE marketplace experience; strong Amazon OR Noon expertise; GMV / revenue ownership; account
growth, campaigns and promotions; pricing, assortment and inventory management; FMCG, Retail, Food or
Non-Food background preferred.

Why Noon, not Amazon: Paula has zero hands-on Amazon (DoFreeze is NOT on Amazon.ae; no Seller / Vendor
Central, no Amazon Ads). Her UAE marketplace work is Noon, talabat and Careem, so she applies to the Noon
seat only and the email says so plainly.

Paula's honest angle:
- Noon from the brand side (DoFreeze, since Oct 2025): listings, pricing, promotional mechanics; Befit x
  Noon "New Year, New Me" +4,176 incremental units, +31% over baseline. SMASH x talabat +165% vs +4.7%
  for a control brand.
- Inventory: she runs the weekly stock-risk review by dark store (PO coverage vs demand) on Noon, talabat
  and Careem; the AI dashboard was built as a team. Channel MSL on platforms reviewed with e-commerce sales.
- GMV ownership: Miravia (Alibaba) 42 accounts +30% GMV QoQ; Flash Sales channel vs P&L targets, CEO
  reporting. Glovo XL chains, deals profitable for both sides.
- Food and non-food: DoFreeze, Mondelez and Glovo (food); Miravia beauty, fragrances, fashion (non-food).

Honesty guardrails:
- No Amazon anywhere in the CV. Never "own the forecast" (contribute). DoFreeze is NOT on Deliveroo.
- Title stays "Brand & Marketing Manager". No visa line in the email; CV header comes from profile.yaml.

Nothing is sent: the email and the LinkedIn DM land in 03_Outreach and in the dashboard outreach store for
Paula to send from her hotmail. ONE-PAGE CV. Lands under output/2026-10-12/.
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

COMPANY = "Genetic Callnet"
TITLE = "Key Account Manager – Noon"
DATE_FOLDER = "2026-10-12"
JOB_ID = "genetic-callnet-kam-noon-2026-10"
CONTACT_NAME = "Mubaraka"
CONTACT_EMAIL = "mubaraka@geneticcallnet.com"

JOB_DESCRIPTION = """\
Key Account Manager – Noon — confidential client of Genetic Callnet (recruitment agency), Dubai, UAE.
AED 20,000/month. LinkedIn hiring post by Mubaraka (2026-10-12).
Two openings with a growing Food & Non-Food business: KAM – Amazon and KAM – Noon.
Looking for: UAE marketplace experience; strong Amazon or Noon expertise; GMV/revenue ownership; account
growth, campaigns & promotions; pricing, assortment and inventory management; FMCG, Retail, Food or
Non-Food background preferred.
Apply: DM the CV with "AMAZON" or "NOON", or email mubaraka@geneticcallnet.com.
"""

ATS = [
    "Key Account Manager", "KAM", "Noon", "UAE marketplace", "marketplace", "e-commerce", "GMV",
    "revenue", "account growth", "campaigns", "promotions", "pricing", "assortment", "inventory management",
    "stock availability", "purchase orders", "dark stores", "listings", "FMCG", "Food", "Non-Food",
    "Retail", "talabat", "Careem", "quick-commerce", "Alibaba", "P&L", "negotiation", "onboarding",
    "sell-in", "sell-out", "promo ROI", "forecast", "Excel", "Power BI", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Key Account Management · Noon & UAE Marketplaces · GMV Growth · Promotions, Pricing & Stock"
    ),
    "professional_summary": (
        "Marketplace key account professional in Dubai, across food and non-food. Today I grow DoFreeze's "
        "FMCG food brands on Noon, talabat and Careem from the brand side; before that, on the platform side, "
        "42 accounts at Alibaba's Miravia (+30% GMV QoQ) and XL chains at Glovo."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Befit, Eurocake, Flair | Noon, talabat & Careem | 50+ markets",
            "bullets": [
                "Grow Befit, Eurocake and Flair on Noon, talabat and Careem: listings, pricing, promotional mechanics and joint campaigns with the platforms; Befit × Noon \"New Year, New Me\" added +4,176 incremental units, +31% over baseline",
                "Run the weekly stock-risk review by dark store on Noon, talabat and Careem, checking platform POs against current and upcoming demand; set channel must-stock lists with e-commerce sales and contribute to the monthly sell-in forecast",
                "Launched SMASH, a new Eurocake brand, on talabat: daily sales +165% vs +4.7% for a control brand; 6 product launches end-to-end (brief, packaging, pricing, go-to-market)",
                "Lead a team of two (designer, social media exec); built a Claude system that automates market research and KPI reporting, cutting manual work ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees | platform side",
            "bullets": [
                "Managed 42 non-food brand accounts (incl. KIKO Milano, NIVEA) to +30% GMV QoQ, turning sales, traffic and conversion data into pricing, assortment and promotion plans",
                "Owned the Flash Sales channel for Beauty, Fashion & Home against P&L targets, reporting directly to the CEO; onboarded 30+ new stores in two months as PIC Fragrances",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Food-delivery & quick-commerce platform | €500M+ revenue | platform side",
            "bullets": [
                "Managed XL food chains (KFC, Taco Bell, La Tagliatella, Sushi Shop) with GMV growth plans and in-app campaigns, negotiating commercial deals profitable for both Glovo and the partner; helped build the non-food Retail vertical",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Sell-in/sell-out and promotional-effectiveness analysis for the chocolate category; contributed to NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # -> "Marketplaces"
        "Noon, talabat, Careem (brand side) · Miravia / Alibaba, Glovo (platform side)"
    ),
    "skills_ecommerce": (  # -> "Account Growth"
        "GMV & sales growth, P&L targets, campaigns & promotions, onboarding, negotiation"
    ),
    "skills_commercial": (  # -> "Pricing & Stock"
        "pricing, assortment & MSL, listings, PO coverage, dark-store availability, forecast input"
    ),
    "skills_data": (  # -> "Data & Insight"
        "sell-in/sell-out, promo uplift vs control, traffic & conversion, KPI dashboards"
    ),
    "skills_tools": (
        "Excel (advanced), Power BI, Looker, Salesforce, SAP, Shopify, Claude / Claude Code (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Marketplaces",
    "E-Commerce & Digital": "Account Growth",
    "Commercial": "Pricing & Stock",
    "Data & Analytics": "Data & Insight",
    "Tools": "Tools & AI",
}

EMAIL_SUBJECT = "NOON – Key Account Manager | Paula De Francisco"
EMAIL_BODY = (
    "Hi Mubaraka,\n\n"
    "I'd like to apply for the Key Account Manager – Noon role from your post. My CV is attached.\n\n"
    "How my experience lines up with the brief:\n\n"
    "- Noon and UAE marketplaces: I'm based in Dubai and manage DoFreeze's food brands (Befit, Eurocake, "
    "Flair) on Noon, talabat and Careem from the brand side: listings, pricing and promotions. Our Befit × "
    "Noon \"New Year, New Me\" campaign added 4,176 incremental units, 31% over baseline.\n"
    "- GMV ownership: at Alibaba's Miravia marketplace I managed 42 brand accounts and grew GMV 30% "
    "quarter on quarter. I also owned the Flash Sales channel against P&L targets, reporting to the CEO.\n"
    "- Inventory: every week I check, dark store by dark store, whether each platform's purchase orders "
    "cover demand, so we catch stock-outs before they happen.\n"
    "- Food and non-food: food at DoFreeze, Mondelez and Glovo; beauty, fragrances and fashion at "
    "Miravia.\n\n"
    "To be upfront, my marketplace experience is on Noon rather than Amazon, which is why I'm applying for "
    "the Noon opening.\n\n"
    "I'd be glad to talk whenever suits you.\n\n"
    "Best regards,\n"
    "Paula De Francisco\n"
    "+971 50 386 3656 · paulich98@hotmail.com\n"
    "linkedin.com/in/paula-de-francisco-perez-92a13119a"
)

LINKEDIN_DM = (
    "NOON. Hi Mubaraka, I'd like to apply for the KAM – Noon role. I'm in Dubai and manage food brands on "
    "Noon, talabat and Careem (Befit × Noon: +31% over baseline); before that, 42 accounts and +30% GMV "
    "QoQ at Alibaba's Miravia. I've emailed you my CV and attached it here too. Paula"
)


def make_job() -> Job:
    return Job(
        id=JOB_ID,
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url=f"mailto:{CONTACT_EMAIL}?subject=NOON%20-%20Key%20Account%20Manager",
        source="manual",
        description=JOB_DESCRIPTION,
        raw={"via": "LinkedIn hiring post by Mubaraka, Genetic Callnet (2026-10-12)",
             "client": "Confidential: growing Food & Non-Food business",
             "apply": f"DM with \"NOON\" or email {CONTACT_EMAIL}",
             "level": "Manager"},
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
        "salary_raw": "AED 20,000/month",
        "salary_aed_min": 20000, "salary_aed_max": 20000,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 72, "ai_tier": "Warm",
        "skills_match": [
            "Noon from the brand side: listings, pricing, promotions; Befit × Noon +31% over baseline",
            "GMV ownership: Miravia (Alibaba) 42 accounts +30% GMV QoQ; Flash Sales vs P&L, CEO reporting",
            "Inventory: weekly dark-store stock-risk review (PO coverage vs demand) on Noon, talabat, Careem",
            "Campaigns with measured uplift: SMASH × talabat +165% vs +4.7% control",
            "Food (DoFreeze, Mondelez, Glovo) and non-food (Miravia beauty / fashion) background",
        ],
        "missing_skills": [
            "Zero hands-on Amazon (rules out the KAM – Amazon seat)",
            "UAE marketplace experience is ~1 year (since Oct 2025), as Brand & Marketing Manager, not a KAM title",
            "No Noon Seller Center / vendor-side ownership of the full account P&L evidenced",
        ],
        "sector_fit": "strong (FMCG food and non-food on UAE marketplaces)",
        "seniority_fit": "good (Manager-level KAM)",
        "red_flags": [
            "AED 20K/month is exactly her floor: no room below it",
            "Agency post with an unnamed client",
        ],
        "ats_keywords": ATS,
        "reasoning": "Real Noon work from the brand side plus marketplace GMV ownership at Alibaba and a food / non-food mix match the brief; UAE tenure is short and she has no Amazon, so only the Noon seat fits.",
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "CV Ready",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def register_outreach() -> None:
    cpath = settings.data_dir / "contacts" / f"{JOB_ID}.json"
    cpath.parent.mkdir(parents=True, exist_ok=True)
    if not cpath.exists():
        cpath.write_text(json.dumps([{
            "name": CONTACT_NAME,
            "title": "Recruiter, Genetic Callnet (posted the hiring post)",
            "company": COMPANY,
            "email": CONTACT_EMAIL,
            "linkedin_url": None,
            "role_type": "Recruiter",
            "source": "LinkedIn hiring post (2026-10-12)",
        }], indent=2, ensure_ascii=False), encoding="utf-8")

    cid = outreach_store.contact_id(CONTACT_NAME, None)
    if cid not in outreach_store.load(JOB_ID):
        outreach_store.add_version(JOB_ID, cid, "email", f"Subject: {EMAIL_SUBJECT}\n\n{EMAIL_BODY}")


def write_outreach_file(final_dir: Path, cv_name: str) -> Path:
    out_dir = final_dir / "03_Outreach"
    out_dir.mkdir(parents=True, exist_ok=True)
    md = (
        "# Genetic Callnet — Key Account Manager – Noon: email + LinkedIn DM\n\n"
        "Send both from Paula's own accounts. Nothing has been sent.\n\n"
        "## 1. Email (from paulich98@hotmail.com)\n\n"
        f"**To:** {CONTACT_EMAIL}\n"
        f"**Subject:** {EMAIL_SUBJECT}\n"
        f"**Attach:** `../01_CV_y_Carta/{cv_name}`\n\n"
        "---\n\n"
        f"{EMAIL_BODY}\n\n"
        "---\n\n"
        "## 2. LinkedIn DM to Mubaraka\n\n"
        "> The post asks for a DM with \"NOON\". Send after the email, with the CV attached.\n\n"
        f"{LINKEDIN_DM}\n"
    )
    p = out_dir / "Email_y_DM_Genetic_Callnet_Noon.md"
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

    final_dir = settings.output_dir / DATE_FOLDER / f"{COMPANY} - KAM Noon"
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
