"""One-off: generate Paula's CV for **Digital Marketing Manager** at **Jobgether**
(United Arab Emirates · fully remote · LinkedIn Easy Apply · posted 2026-09-02).

IMPORTANT — the full JD text was NOT retrievable: LinkedIn sits behind login and
jobgether.com could not be fetched from this environment. The brief below is
reconstructed from the LinkedIn listing metadata (title, UAE remote, Easy Apply)
plus Jobgether's standard model (it posts on behalf of an unnamed partner company
and runs an AI-powered match against the role's core requirements before a
shortlist reaches the hiring team). The CV is therefore built as a broad-spine
**Digital Marketing Manager** CV: paid media, e-commerce/CRO, content & social,
influencer, email/CRM and revenue-led analytics — every claim drawn from Paula's
real profile.yaml. If the actual JD is pasted later, re-tune the emphasis.

Because Jobgether screens with AI keyword/requirement matching, breadth of
genuine digital-marketing surface area matters more here than a narrow angle.

Paula's honest fit:
- PAID MEDIA: plans and optimises Meta (FB/IG) and Google Ads at DoFreeze —
  audiences, creative A/B testing, budget management to ROI/ROAS.
- E-COMMERCE: owns the Shopify store end-to-end (catalogue, UX, collections,
  pricing, promotions, checkout) lifting CRO and AOV.
- CONTENT / SOCIAL / INFLUENCER: built the influencer & UGC programme from zero,
  25–50 creators per campaign; social-first programmes at Miravia.
- LIFECYCLE / EMAIL: email & EDM campaigns, promotions, cart recovery.
- ANALYTICS: conversion, traffic, AOV, ROAS and marketing-attributed revenue in
  dashboards (GA4, Looker, Power BI, Tableau).
- AI: generative-AI marketing automation (Claude/GPT) — a genuine differentiator
  and increasingly a named requirement in digital roles.

Honesty guardrails:
- Experience length stated as 4+ years (Mondelez 2021 → present); never inflated.
- Technical-SEO tooling (SEMrush, Ahrefs, Screaming Frog) is a development area —
  positioned as content/organic strength + AEO/GEO edge, never as owned tooling.
- Klaviyo / HubSpot / Mailchimp: real email/EDM + Salesforce CRM experience only;
  those platforms framed as "quick to adopt", never claimed.
- Shopify-native; WooCommerce/Magento transferable, not claimed.
- No Arabic claimed (many UAE marketing JDs require it — flag if the real JD does).
- Visa line is the factual "UAE Residence Visa" — never "no sponsorship needed".

ONE-PAGE standard: tight summary, 3/2/1/1 bullets, ~6-8 skills per row.
Fills the real CV template, relabels the skills rows for this role, converts to
PDF via LibreOffice (docx2pdf/Word fails silently on this Mac), registers the job
for the dashboard, verifies the page count, and lands the package under
output/2026-09-03/. Also drops a short-named 'Paula De Francisco - CV.pdf' copy
for Easy Apply / portal uploads.
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

COMPANY = "Jobgether"
TITLE = "Digital Marketing Manager"
DATE_FOLDER = "2026-09-03"

JOB_DESCRIPTION = """\
Digital Marketing Manager — Jobgether (on behalf of an unnamed partner company).
United Arab Emirates · Fully remote · Full-time · LinkedIn Easy Apply · posted 2026-09-02.

NOTE: the full job description was not retrievable (LinkedIn login wall; jobgether.com
not fetchable from this environment). The following is the expected scope of a
Digital Marketing Manager brief of this type, used to target the CV:

- Own the digital marketing plan end-to-end and connect activity to commercial
  outcomes (traffic, conversion, revenue, retention) rather than vanity metrics.
- Plan, launch and optimise paid media across Meta (Facebook/Instagram) and Google
  Ads — audience building, creative testing, remarketing — managing budgets to
  ROAS, CPA and CAC.
- Grow e-commerce performance: catalogue and product content, merchandising,
  promotions, landing pages, checkout journey, conversion rate (CRO) and average
  order value (AOV).
- Run content, organic/SEO and social programmes, plus influencer and creator
  partnerships that generate UGC and measurable sell-out.
- Build segmented email/EDM and lifecycle automation (launches, promotions,
  abandoned cart, reactivation, repeat purchase).
- Report performance in dashboards — conversion, traffic, AOV, ROI/ROAS,
  marketing-attributed revenue — and run continuous experimentation.
- Work autonomously in a distributed, fully remote setup; professional English.

How Jobgether works: an AI-powered matching process reviews each application
against the role's core requirements and shares a shortlist with the hiring
company; interviews and the final decision are run by their internal team.
"""

ATS = [
    "Digital Marketing Manager", "digital marketing", "growth marketing",
    "e-commerce", "ecommerce", "online revenue", "revenue growth",
    "performance marketing", "paid media", "paid social", "Meta Ads",
    "Facebook Ads", "Instagram Ads", "Google Ads", "remarketing",
    "audience targeting", "creative testing", "A/B testing", "experimentation",
    "media budget management", "ROAS", "ROI", "CPA", "CAC", "cost per lead",
    "conversion rate optimisation", "CRO", "average order value", "AOV",
    "landing pages", "checkout optimisation", "abandoned cart", "cross-sell",
    "upsell", "bundles", "promotions", "merchandising", "product catalogue",
    "Shopify", "quick commerce", "marketplace",
    "content strategy", "social media", "organic search", "SEO", "AEO", "GEO",
    "influencer marketing", "creator partnerships", "UGC", "brand awareness",
    "email marketing", "EDM", "lifecycle campaigns", "marketing automation",
    "segmentation", "CRM", "Salesforce", "retention", "customer acquisition",
    "Google Analytics 4", "GA4", "dashboards", "reporting", "KPI tracking",
    "revenue attribution", "data-driven", "Looker", "Power BI", "Tableau",
    "campaign management", "go-to-market", "product launch", "NPD",
    "generative AI", "AI automation", "stakeholder management",
    "remote", "distributed team", "English C1", "Dubai", "UAE", "MENA", "GCC",
]

CONTENT = {
    "headline": (
        "Digital Marketing Manager · Paid Media (Meta & Google) · "
        "E-Commerce, CRO & AOV · Content, Social & Influencer"
    ),
    "professional_summary": (
        "Digital marketing manager with 4+ years across e-commerce, FMCG, beauty and fashion, running "
        "paid media, Shopify e-commerce, content, influencer and email programmes end-to-end across 50+ "
        "markets. Measures everything against conversion, AOV, ROAS and revenue. Dubai-based, fluent "
        "remote operator, English C1."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Brands: Befit, Eurocake, Flair | Shopify DTC + retail & quick-commerce | 50+ countries",
            "bullets": [
                "Plan and optimise paid media on Meta (Facebook & Instagram) and Google Ads — audience building, creative A/B testing and budget management — analysing ROI and ROAS to reallocate spend toward what converts",
                "Own the Shopify store end-to-end (catalogue, product content, collections, pricing, promotions, UX, checkout) and grow conversion rate and average order value through data-led merchandising, bundles and EDM campaigns; integrated the brands into Noon, Talabat, Careem and Deliveroo",
                "Run content, social and influencer marketing built from zero — 25–50 creators per campaign plus sampling and seeding — and built a generative-AI system (Claude/GPT) for campaign planning, content and KPI reporting that cut manual workload ~40% across 6 product launches",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew 42 accounts +30% GMV QoQ through pricing, assortment and promotional strategy across a large multi-SKU catalogue, reading traffic, conversion, ROI/ROAS and retention to decide where to invest",
                "Created and led Hot on Social and the Beauty Club — social-first content and creator programmes — and owned the Flash Sales channel across Beauty, Fashion & Home",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew order volume with major partners through bespoke digital activations and promo campaigns, and supported building the Retail vertical with tailored launch campaigns",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Analysed promotional effectiveness and sell-in/sell-out data to inform pricing, assortment and launch planning (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # label -> "Digital Marketing"
        "digital marketing strategy, campaign planning & go-to-market, performance marketing, "
        "product launches (NPD), promotional strategy, budget management"
    ),
    "skills_ecommerce": (  # label -> "Paid Media & E-Commerce"
        "Meta Ads (Facebook & Instagram), Google Ads, remarketing, creative A/B testing, Shopify end-to-end, "
        "CRO & AOV, quick-commerce (Noon, Talabat, Careem, Deliveroo)"
    ),
    "skills_commercial": (  # label -> "Content, Social & CRM"
        "content strategy, social media, influencer & UGC programmes, email marketing & EDM, "
        "lifecycle automation & segmentation, CRM (Salesforce), organic/SEO & AEO/GEO"
    ),
    "skills_data": (  # label -> "Analytics & Performance"
        "ROAS, ROI, CPA/CAC, conversion & funnel analysis, AOV & repeat purchase, revenue attribution, "
        "KPI dashboards & reporting, Google Analytics 4"
    ),
    "skills_tools": (  # label -> "Tools"
        "Shopify, Meta Ads Manager, Google Ads, Google Analytics 4, Salesforce, Power BI, Tableau, Looker, "
        "Canva, Generative AI (Claude, ChatGPT), MS Office — Expert"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Digital Marketing",
    "E-Commerce & Digital": "Paid Media & E-Commerce",
    "Commercial": "Content, Social & CRM",
    "Data & Analytics": "Analytics & Performance",
}


def make_job() -> Job:
    return Job(
        id="jobgether-digital-marketing-manager-uae-remote-2026-09",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (Fully remote)",
        url="https://www.linkedin.com/jobs/search/?keywords=Jobgether%20Digital%20Marketing%20Manager&location=United%20Arab%20Emirates",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Jobgether Digital Marketing Manager United Arab Emirates remote",
            "workplace": "Fully remote (UAE-based)",
            "note": "Found in Paula's LinkedIn 'ecommerce en remoto' search, posted 2026-09-02, Easy Apply. "
                    "Jobgether posts on behalf of an unnamed partner company and pre-screens with AI matching "
                    "against the role's core requirements. FULL JD NOT RETRIEVED (LinkedIn login wall, "
                    "jobgether.com unfetchable) — the CV targets the standard broad Digital Marketing Manager "
                    "spine from Paula's real experience. Re-tune if the JD is supplied. Salary not disclosed. "
                    "Paula has already applied to three other Jobgether-listed roles (Paid Media Specialist, "
                    "eCom Operations Manager, Digital Marketing & E-Commerce Growth Manager).",
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
        "salary_raw": "Not disclosed (fully remote, UAE)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 76, "ai_tier": "Hot",
        "skills_match": [
            "Title-level match: she is a Brand & Marketing Manager running the full digital spine today (lateral move, not a stretch)",
            "Paid media hands-on: Meta (FB/IG) + Google Ads — audiences, creative A/B testing, budgets managed to ROI/ROAS",
            "E-commerce ownership: Shopify end-to-end (catalogue, merchandising, pricing, promotions, UX, checkout) lifting CRO and AOV",
            "Marketplace & quick-commerce integration (Noon, Talabat, Careem, Deliveroo) — rare, UAE-specific digital retail experience",
            "Content, social and influencer/UGC programmes built from zero: 25–50 creators per campaign plus sampling and seeding",
            "Email/EDM and lifecycle campaigns; CRM on Salesforce",
            "Revenue-led analytics: conversion, traffic, AOV, ROAS and attribution in dashboards (GA4, Looker, Power BI, Tableau)",
            "Generative-AI marketing automation (Claude/GPT) — a genuine differentiator for an AI-screened, remote-first employer",
            "Fully set up for remote/distributed work from Dubai; English C1",
        ],
        "missing_skills": [
            "Full JD not available — requirements unverified; the CV targets the standard Digital Marketing Manager spine and may need re-tuning",
            "Technical-SEO tooling (SEMrush, Ahrefs, Screaming Frog, structured data) is a development area — content/organic + AEO/GEO claimed, tooling not",
            "Email platforms Klaviyo / HubSpot / Mailchimp not used (real email/EDM + Salesforce CRM instead) — framed as 'quick to adopt'",
            "Shopify-native; WooCommerce / Magento / BigCommerce transferable but not claimed",
            "No Arabic — a hard filter on many UAE marketing JDs; unknown here until the JD is seen",
            "If the role expects 5+ years, Paula has 4+ (Mondelez 2021 → present) — stated honestly, never inflated",
        ],
        "sector_fit": "strong — digital marketing across e-commerce/FMCG/beauty is Paula's exact core; partner company and sector unknown (Jobgether anonymises)",
        "seniority_fit": "on-band — Manager-level title matches her current Brand & Marketing Manager role",
        "red_flags": [
            "Jobgether posts for an unnamed partner and pre-screens with AI matching — no hiring manager to approach, so the CV alone carries the application",
            "Salary not disclosed — cannot check against the AED 20,000/month floor",
            "Fully remote, which sits outside Paula's stated preference (remote_ok: false in profile.yaml)",
            "Full JD not retrievable — fit assessment is based on title and listing metadata only",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Clean, honest title-level match. The role is a Digital Marketing Manager, fully remote from the "
            "UAE, listed by Jobgether for an unnamed partner and screened by AI matching before a human sees "
            "it — which means keyword breadth and evidence of the full digital spine decide whether she gets "
            "shortlisted. Paula runs that spine today at DoFreeze: paid media on Meta and Google with creative "
            "testing and ROAS-managed budgets, the Shopify store end-to-end with CRO and AOV ownership, "
            "content/social/influencer programmes built from zero, email and EDM, and revenue-led dashboards, "
            "all across 50+ markets — plus UAE quick-commerce integrations (Noon, Talabat, Careem, Deliveroo) "
            "that a UAE-based employer will read as directly relevant. Her generative-AI automation work is a "
            "real differentiator. The caveat is that the full JD could not be retrieved, so the CV is built "
            "broad rather than surgically targeted; technical-SEO tooling, Klaviyo/HubSpot and non-Shopify "
            "platforms are not claimed, no Arabic is implied, and experience length is stated as 4+ years."
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

    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
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
