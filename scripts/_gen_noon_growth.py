"""One-off: generate Paula's CV tailored to the noon "Growth Manager" role on
the Noon Business (B2B marketplace) team inside Everyday Labs — noon's 0-to-1
innovation engine — Dubai, UAE.

The role is a hands-on demand-generation / performance-marketing execution seat
("build and execute campaigns yourself, not manage agencies"). Content is
authored directly (no LLM API call), filled into the real template, converted to
PDF (keeping the editable DOCX too), placed under the día → posición → categoría
convention, and the job is registered in scored_jobs.json.

Mirrors the pattern established in scripts/_gen_noon_am.py.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "noon"
TITLE = "Growth Manager"
DATE_FOLDER = "2026-08-12"

JOB_DESCRIPTION = """\
Growth Manager — noon (Noon Business / Everyday Labs), Dubai, UAE (On-site).

About: Everyday Labs is noon's innovation engine — build and test new ideas fast,
from early concepts to real products. High ownership, fast cycles, focus on what
actually works. Noon Business is a B2B marketplace helping companies buy their
recurring business supplies faster, cheaper and with better control — noon's
consumer engine applied to enterprise procurement.

The Growth Manager is the execution engine of the growth team, working closely
with the Senior Manager, Growth to execute demand-generation campaigns, manage
digital channels, create content, generate leads and drive B2B customer
acquisition and retention. Not an agency-management role — you build and execute
campaigns yourself, analyse results and iterate fast.

What you'll do:
- Execute and optimise performance marketing campaigns. Own day-to-day paid
  channels, A/B testing, budget allocation and performance reporting.
- Create ongoing content for B2B engagement: case studies, ROI stories, category
  guides, industry newsletters and LinkedIn content.
- Manage community and partnership outreach: trade events, industry webinars,
  business association partnerships, co-marketing with brand principals.
- Build and manage the email marketing engine: onboarding sequences,
  re-engagement, promotional campaigns and weekly updates.
- Track and report growth metrics: CAC, lead-to-customer conversion rate,
  activation rate, retention rate and channel-level ROI.
- Support the Senior Manager, Growth on strategic initiatives: ABM campaigns for
  enterprise accounts, expansion into new segments, new channel experiments.

What you'll need:
- 5 years in digital marketing, growth or demand generation. B2B preferred.
- Hands-on with LinkedIn Ads, Google Ads, email tools (HubSpot, Mailchimp) and
  CRM systems.
- Strong content creation (LinkedIn posts, product one-pagers, cold outreach).
- Analytical mindset: Google Analytics, campaign dashboards, data-driven
  optimisation.
- Experience with lead generation and nurturing workflows.
- Self-starter who executes independently without detailed briefs.
- GCC/MENA experience a plus. Comfortable in a fast-paced, ambiguous 0-to-1
  environment.
"""

ATS = [
    "Growth Manager", "growth marketing", "demand generation", "performance marketing",
    "paid channels", "A/B testing", "budget allocation", "performance reporting",
    "Google Ads", "LinkedIn Ads", "email marketing", "onboarding sequences",
    "re-engagement", "lead generation", "lead nurturing", "content creation",
    "LinkedIn content", "case studies", "newsletters", "community", "partnerships",
    "co-marketing", "webinars", "CAC", "lead-to-customer conversion", "activation rate",
    "retention", "channel-level ROI", "ROAS", "ABM", "account-based marketing",
    "B2B customer acquisition", "CRM", "Google Analytics", "campaign dashboards",
    "GCC", "MENA", "0-to-1", "marketing automation", "generative AI", "noon",
]

# --------------------------------------------------------------------------
# CV content — authored for this JD (no invented experience or tools)
# --------------------------------------------------------------------------
CV_CONTENT = {
    "headline": (
        "Growth & Digital Marketing · Performance Media (Meta & Google Ads) · "
        "Demand Generation · Email/CRM & AI Automation"
    ),
    "professional_summary": (
        "Hands-on growth and digital marketing manager with 4+ years across FMCG, "
        "e-commerce and GCC quick-commerce — I build and execute campaigns end-to-end "
        "myself, not brief agencies. I own performance media (Meta & Google Ads), the "
        "email/EDM engine, content and A/B testing, powered by a generative-AI automation "
        "stack (Claude) that cut campaign turnaround ~40%. Track record of +30% GMV growth "
        "QoQ across 42 key accounts and full-funnel optimisation on CAC, conversion, "
        "activation and retention. Deep GCC/MENA experience (Noon, Talabat, Careem, "
        "Deliveroo); thrives in fast, ambiguous 0-to-1 environments. Based in Dubai on a "
        "residence visa — no sponsorship needed."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own day-to-day performance marketing across paid channels (Meta & Google Ads) — audience building, creative A/B testing, budget allocation and weekly performance reporting on ROI, ROAS, CAC and conversion",
                "Build and run the email/EDM engine end-to-end — onboarding sequences, re-engagement, promotional campaigns and weekly updates — with segmentation and nurturing workflows through marketing automation and CRM",
                "Built a generative-AI automation stack (Claude) for campaign planning, content, market research and KPI reporting — cutting turnaround ~40% and letting me test and iterate fast across 50+ markets",
                "Create ongoing content myself — LinkedIn and social copy, product one-pagers, category guides and brand storytelling — and scaled UGC via an influencer programme (25–50 creators per campaign)",
                "Track and report growth metrics — CAC, conversion, activation, retention and channel-level ROI — reallocating budget to the best-performing channels",
                "Run partnership and channel outreach across UAE quick-commerce (Noon, Talabat, Careem, Deliveroo) and modern trade — co-marketing with brand principals, promotional mechanics and retail execution",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Grew 42 key (high-value) brand accounts to +30% GMV QoQ through account-based promotions, pricing and assortment — effectively ABM for enterprise accounts",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across channels to optimise performance and forecasting accuracy",
                "Drove acquisition of 30+ new brand accounts in two months via demand-generation promotions and trend-led products (incl. Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Owned the Flash Sales channel (Beauty, Fashion & Home), reporting to the CEO and executing commercial plans aligned with P&L targets",
                "Created the Beauty Club and Hot on Social content projects, lifting engagement, retention and brand visibility",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the 0-to-1 team that built Glovo's Retail vertical from scratch — acquiring and onboarding fashion and lifestyle brand partners onto the platform",
                "Managed strategic B2B accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning and bespoke marketing activations",
                "Negotiated and closed high-impact commercial partnerships and ran cross-functional campaigns across marketing, logistics and support",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis and built performance reports for the chocolate category",
                "Contributed to NPD launches including Milka Spread and Mini Suchard",
            ],
        },
    ],
    "skills_brand": (
        "demand generation, performance marketing, growth marketing, content creation "
        "(LinkedIn, case studies, newsletters, one-pagers), email marketing, ABM / "
        "account-based marketing, partnerships & co-marketing, influencer marketing & UGC, "
        "go-to-market, generative-AI campaigns"
    ),
    "skills_ecommerce": (
        "Meta Ads (Facebook & Instagram), Google Ads, paid social & search, A/B testing, "
        "email/EDM automation & nurturing, landing pages & CRO, Shopify, quick-commerce "
        "(Noon, Talabat, Careem, Deliveroo), organic social & LinkedIn content"
    ),
    "skills_commercial": (
        "B2B customer acquisition & retention, lead generation & nurturing workflows, "
        "key & enterprise account management, funnel optimisation, pricing & promotions, "
        "negotiation, distributor & partner management"
    ),
    "skills_data": (
        "CAC, lead-to-customer conversion, activation & retention, channel-level ROI, ROAS, "
        "KPI dashboards & reporting, web & campaign analytics (Google Analytics, Looker, "
        "Power BI, Tableau), AI-assisted analysis, forecasting"
    ),
    "skills_tools": (
        "Meta Ads Manager, Google Ads, Google Analytics, Salesforce (CRM), Shopify, Looker, "
        "Power BI, Tableau, Generative AI (Claude, ChatGPT), Canva, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="noon-growth-manager-noonbusiness",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/noon/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Growth Manager", "via": "LinkedIn",
             "team": "Noon Business / Everyday Labs",
             "reports_to": "Senior Manager, Growth"},
    )


def _convert_pdf(docx_path: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice headless. Keeps the editable DOCX."""
    import subprocess

    pdf_path = docx_path.with_suffix(".pdf")
    try:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", "--outdir",
             str(docx_path.parent), str(docx_path)],
            check=True, capture_output=True, timeout=120,
        )
    except Exception as exc:  # noqa: BLE001
        print("WARN pdf conversion failed:", type(exc).__name__, exc)
    return pdf_path


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "url": job.url,
        "source": job.source,
        "description": job.description,
        "salary_raw": None,
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 90,
        "ai_tier": "Hot",
        "skills_match": [
            "Performance marketing (Meta & Google Ads)", "Demand generation",
            "Email/EDM engine", "A/B testing & budget allocation",
            "CAC / conversion / retention analytics", "Content creation (LinkedIn)",
            "Partnerships & co-marketing", "GCC/MENA quick-commerce (hands-on)",
            "Generative-AI automation", "0-to-1 self-starter",
        ],
        "missing_skills": [
            "LinkedIn Ads (has Meta & Google Ads — transferable)",
            "HubSpot/Mailchimp by name (has EDM + marketing automation + CRM)",
            "5 yrs (has 4+)",
        ],
        "sector_fit": "strong",
        "seniority_fit": "exact",
        "red_flags": [],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit for a hands-on B2B growth execution seat: Paula builds and runs "
            "performance campaigns herself (Meta + Google Ads), owns an email/EDM engine, "
            "created a Claude automation stack that cut turnaround ~40%, and reports CAC, "
            "conversion, activation, retention and channel ROI. +30% GMV QoQ across 42 "
            "accounts (ABM-style) and lives inside the noon ecosystem daily. Gaps are name-"
            "brand tools (LinkedIn Ads, HubSpot) and one year of tenure — all transferable."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _move_into_dated_folder() -> Path:
    """Move output/<Company> - <Role>/ under output/<DATE_FOLDER>/."""
    from career_ops.generators._paths import job_output_dir
    src = job_output_dir(make_job())            # output/noon - Growth Manager
    dated_parent = settings.output_dir / DATE_FOLDER
    dated_parent.mkdir(parents=True, exist_ok=True)
    dest = dated_parent / src.name
    if src.resolve() == dest.resolve():
        return dest
    if dest.exists():
        for item in src.iterdir():
            shutil.move(str(item), str(dest / item.name))
        shutil.rmtree(src, ignore_errors=True)
    else:
        shutil.move(str(src), str(dest))
    return dest


def main() -> None:
    job = make_job()
    register_in_dashboard(job)
    print("STEP registered in dashboard")

    cv_docx = cv._fill_template(CV_CONTENT, job)
    print("STEP CV docx built:", cv_docx.name)

    final_dir = _move_into_dated_folder()
    print("STEP moved to:", final_dir)

    cvd = final_dir / "01_CV_y_Carta" / cv_docx.name
    cv_pdf = _convert_pdf(cvd)

    print("OK_CV_DOCX", cvd.name, "(exists)" if cvd.exists() else "(MISSING)")
    print("OK_CV_PDF", cv_pdf.name, "(exists)" if cv_pdf.exists() else "(MISSING)")
    print("FINAL_DIR", final_dir)


if __name__ == "__main__":
    main()
