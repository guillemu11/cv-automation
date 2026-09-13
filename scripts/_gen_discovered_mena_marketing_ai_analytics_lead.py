"""One-off: generate Paula's application package for the Discovered MENA
"Marketing AI & Analytics Lead" (Dubai) role.

Discovered MENA is a Dubai tech/e-commerce recruitment partner; this role is
for one of their client platforms. The JD has a DUAL mandate:
  (1) own the marketing data & analytics ecosystem (dashboards, attribution,
      funnel, single-source-of-truth reporting), and
  (2) embed practical AI, automation and agentic workflows into everyday
      marketing operations to cut manual work and speed teams up.

Half (2) is Paula's single strongest, rarest differentiator: at DoFreeze she
built an AI-powered marketing automation system (Claude/GPT) that automates
campaign planning, content, market research and KPI reporting — cutting manual
workload ~40%. Half (1) she covers via her hands-on KPI/ROI/ROAS reporting,
dashboards (Power BI, Tableau, Looker) and P&L fluency.

Honest gaps (JD-specific, addressed in the cover letter, NOT papered over):
  - formal attribution modelling / incrementality testing terminology
  - mobile measurement partners (MMPs) — not in her stack
  - she is a marketing-analytics *hybrid*, not a pure BI analyst

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. Fills the real CV + cover-letter templates,
converts DOCX->PDF via LibreOffice (docx2pdf/Word is unreliable on this Mac),
and lands the package under
output/2026-08-18/Discovered MENA - Marketing AI & Analytics Lead/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "Discovered MENA"
TITLE = "Marketing AI & Analytics Lead"
DATE_FOLDER = "2026-08-18"

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

JOB_DESCRIPTION = """\
Marketing AI & Analytics Lead — Discovered MENA (client: fast-growing technology
platform), Dubai. Competitive Salary + Benefits. On-site, full-time.

The Opportunity: We are looking for a Marketing AI & Analytics Lead to join a fast
growing technology platform based in Dubai. This is a high impact opportunity for
someone who sits at the intersection of marketing analytics, business intelligence,
automation, and AI. You will play a key role in building the data infrastructure
that powers marketing performance while identifying and implementing AI driven
solutions that make the wider marketing function faster, smarter, and more efficient.

The Role: As the Marketing AI & Analytics Lead, you will have a dual mandate. You
will own and develop the marketing data and analytics ecosystem, ensuring that
performance is measurable across the full customer journey and that marketing
investment can be directly linked to commercial outcomes. Alongside this, you will
identify opportunities to embed practical AI, automation, and agentic workflows into
everyday marketing operations, developing tools that reduce manual work and enable
teams to move faster. You will work closely with Growth, Product, Customer, and
Technology teams to establish robust attribution, improve funnel visibility, and
translate complex data into clear commercial recommendations.

Key Responsibilities:
- Design and manage multi channel marketing data frameworks across web and mobile
  applications.
- Establish a single source of truth for marketing performance across business units.
- Build centralised dashboards covering acquisition, retention, CPA, LTV, conversion,
  and funnel performance.
- Develop and optimise attribution models across web and mobile channels.
- Ensure data quality, tagging, tracking, and measurement infrastructure remain
  accurate and reliable.
- Automate recurring analytics and leadership reporting, reducing manual processes and
  increasing the speed of insight.
- Identify high impact opportunities to apply AI and automation across marketing
  functions.
- Build practical AI tools, automations, and agentic workflows that solve real
  business problems.
- Partner with marketing teams to turn time intensive, multi day processes into
  efficient automated workflows.
- Develop reusable tools and systems that reduce repetitive work and improve team
  productivity.
- Translate complex datasets and performance trends into actionable commercial
  recommendations.

What We're Looking For:
- 4 to 7 years' experience across marketing analytics, business intelligence,
  performance analytics, or a related discipline.
- Proven experience building and implementing practical AI tools, agents, or automated
  workflows that deliver tangible business value.
- Strong proficiency in reporting and visualisation platforms such as Looker Studio,
  Power BI, or Tableau.
- Advanced spreadsheet and data manipulation skills, including pivot tables and complex
  formulas.
- Strong understanding of mobile measurement partners, CRM platforms, and major
  advertising platforms.
- Hands on experience with attribution modelling, funnel analysis, and campaign
  incrementality testing.
- Strong commercial understanding and the ability to turn complex or messy datasets into
  clear, actionable insights.
- A highly analytical and hands on mindset, with the ability to move from identifying a
  problem to building a practical solution.
"""

ATS = [
    "marketing analytics", "business intelligence", "performance analytics",
    "AI tools", "AI agents", "agentic workflows", "automation",
    "marketing automation", "generative AI", "Looker Studio", "Power BI",
    "Tableau", "dashboards", "single source of truth", "attribution",
    "funnel analysis", "conversion", "retention", "CPA", "LTV", "ROI", "ROAS",
    "CRM", "advertising platforms", "Meta Ads", "Google Ads", "data quality",
    "tagging", "tracking", "measurement", "reporting automation",
    "commercial recommendations", "customer journey", "P&L", "pivot tables",
    "data manipulation", "e-commerce", "growth", "Dubai", "UAE",
]

CONTENT = {
    "headline": "Marketing Analytics & AI Automation · Performance Dashboards (Power BI · Tableau · Looker) · Attribution, Funnel & ROI/ROAS · P&L-Linked Reporting",
    "professional_summary": (
        "Marketing professional at the intersection of analytics and applied AI. I build the reporting that links "
        "marketing spend to commercial outcomes — KPI dashboards across the funnel (conversion, retention, ROI/ROAS, "
        "sell-out) in Power BI, Tableau and Looker — and I build the AI/automation on top of it: at DoFreeze I created "
        "a generative-AI system (Claude/GPT) that automates campaign planning, market research, content and KPI "
        "reporting, cutting manual workload ~40% and turning multi-day processes into same-day ones. Four+ years across "
        "FMCG and top-5 e-commerce (DoFreeze, Alibaba's Miravia, Glovo), fluent in P&L and translating messy data into "
        "clear commercial recommendations. Already in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Built a practical AI + automation system (Claude / generative AI) that embeds agentic workflows into everyday marketing — automating campaign planning, market research, content and KPI reporting — cutting manual workload ~40% and turning time-intensive, multi-day processes into same-day ones across 50+ markets",
                "Own end-to-end marketing performance reporting: KPI dashboards across the funnel (traffic, conversion/CRO, retention, ROI, ROAS, sell-out) that link A&P investment to commercial outcomes and feed leadership decisions",
                "Automate recurring analytics and leadership reporting with AI-assisted tooling, increasing speed of insight and freeing the team from repetitive manual reporting",
                "Run paid media on Meta Ads (Facebook & Instagram) and Google Ads plus CRM/EDM — audience building, creative A/B testing and funnel analysis to improve ROAS and cost efficiency",
                "Build reusable tools and templates (reporting, briefs, pitch decks, landing pages) that reduce repetitive work and improve team productivity — measurement and tracking discipline built in",
                "Translate messy multi-market data into clear commercial recommendations for NPD, pricing and channel investment across GCC, MENA, Asia, Europe, USA and Africa",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Continuously analysed conversion, traffic, retention, ROI and ROAS to optimise channel performance and improve forecasting accuracy — a data-led operating rhythm across a top-5 e-commerce platform",
                "Grew 42 key accounts +30% GMV QoQ through data-driven pricing, assortment and promotion decisions — reporting the Flash Sales channel P&L directly to the CEO",
                "Turned platform performance data into commercial recommendations that shaped assortment and promo calendars, onboarding 30+ stores in two months as PIC Fragrances",
                "Built recurring performance reports and read-outs that made channel and category performance measurable and comparable across teams",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Drove GMV growth for strategic accounts through data-led planning on a web + mobile quick-commerce platform — reading funnel and order data to prioritise actions",
                "Partnered cross-functionally with marketing, logistics and CX — the Growth/Product/Customer/Tech collaboration this role requires — to deliver campaigns and measure results",
                "Negotiated and closed commercial deals with profitability tracked on both sides",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Insights Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Conducted sell-in/sell-out analysis and evaluated promotional effectiveness for the chocolate category — building the performance reports leadership used to steer the category",
                "Identified data-backed growth opportunities that contributed to NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": "AI & automation for marketing (agentic workflows), generative-AI tooling (Claude / GPT), marketing automation, campaign planning & optimisation, go-to-market, reusable tools & templates, team productivity",
    "skills_ecommerce": "performance marketing (Meta Ads, Google Ads), funnel analysis & CRO, CRM & EDM, retention & acquisition, e-commerce growth (Shopify, quick-commerce), web + mobile marketing, tagging & tracking discipline",
    "skills_commercial": "commercial acumen & P&L, translating data into recommendations, pricing & assortment analytics, key account & category performance, cross-functional partnership (Growth · Product · Customer · Tech)",
    "skills_data": "marketing analytics & BI, KPI dashboards & single-source-of-truth reporting, Power BI, Tableau, Looker, reporting automation, ROI / ROAS / CPA / conversion / retention, funnel & performance analysis, forecasting, AI-assisted analysis, advanced Excel (pivot tables, complex formulas), Nielsen, Kantar",
    "skills_tools": "Generative AI (Claude, ChatGPT), Power BI, Tableau, Looker, Meta Ads Manager, Google Ads, Excel (Expert), Salesforce, SAP, Shopify, Canva",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "The Marketing AI & Analytics Lead role reads like the job I've been quietly building for myself. Its dual "
        "mandate — own the marketing data and analytics ecosystem, and embed practical AI and automation into everyday "
        "marketing — is exactly the intersection I work at today. At DoFreeze in Dubai I don't just report on marketing "
        "performance; I've built the AI system that generates the reporting, and I'd love to do that at platform scale "
        "for a fast-growing Dubai tech business."
    ),
    "body_paragraph_1": (
        "On the AI-and-automation half, I have the rare, tangible track record you're asking for: I built a generative-AI "
        "system (Claude/GPT) that embeds agentic workflows into our marketing operations — automating campaign planning, "
        "market research, content and KPI reporting — which cut manual workload roughly 40% and collapsed multi-day "
        "processes into same-day ones. On the analytics half, I own end-to-end performance reporting: funnel dashboards "
        "(traffic, conversion/CRO, retention, ROI, ROAS, sell-out) in Power BI, Tableau and Looker that link marketing "
        "spend to commercial outcomes. At Alibaba's Miravia I ran this discipline daily — analysing conversion, traffic, "
        "retention and ROI to grow 42 accounts +30% GMV QoQ, reporting the channel P&L to the CEO — and at Glovo and "
        "Mondelez I built the sell-out and performance analysis leadership steered by."
    ),
    "body_paragraph_2": (
        "I want to be straight about fit rather than oversell. My core strength is the applied-AI and commercial-analytics "
        "side — building tools, dashboards and recommendations that move the business — plus performance marketing across "
        "Meta and Google and CRM/EDM. Where I'd be learning fast is the most specialised BI vocabulary in the posting: "
        "formal attribution modelling, incrementality testing and mobile measurement partners are adjacent to what I do "
        "(funnel analysis, ROI/ROAS, conversion) rather than my day-to-day today. Given my analytical, build-a-solution "
        "mindset — and that I'm the kind of marketer who automates her own reporting — I close that gap quickly. I'm also "
        "already in Dubai on a residence visa, so I can start on-site immediately with zero relocation."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to walk your team through the AI reporting system I built and how I'd stand up a "
        "single source of truth and an automation roadmap for this platform. I'm based in Dubai and available "
        "immediately. Thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="discovered-mena-marketing-ai-analytics-lead-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/company/discovered-mena/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing AI & Analytics Lead", "via": "LinkedIn / Discovered MENA (recruiter)"},
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
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
        "ai_score": 80,
        "ai_tier": "Hot",
        "skills_match": [
            "Built practical AI tools / agentic workflows for marketing (DoFreeze, -40% manual work)",
            "Marketing performance reporting & KPI dashboards (Power BI / Tableau / Looker)",
            "Funnel analysis, conversion/CRO, retention, ROI/ROAS",
            "Performance marketing (Meta Ads, Google Ads) + CRM/EDM",
            "Commercial acumen & P&L; translating data into recommendations",
            "Cross-functional with Growth / Product / Customer / Tech",
            "AI-native builder; already in Dubai (residence visa)",
        ],
        "missing_skills": [
            "Formal attribution modelling / incrementality testing terminology",
            "Mobile measurement partners (MMPs) not in her stack",
            "Marketing-analytics hybrid rather than a pure BI analyst",
        ],
        "sector_fit": "strong (marketing analytics + applied AI · e-commerce / tech platform)",
        "seniority_fit": "on-band (JD asks 4-7 yrs; Paula has 4+)",
        "red_flags": [
            "Recruiter-listed role (Discovered MENA) — client is an undisclosed Dubai tech platform",
            "Salary not disclosed — cannot confirm AED 20k/mo floor",
            "High competition (500+ applicants on LinkedIn within 24h)",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit on the differentiating half of a dual-mandate role. Discovered MENA's 'Marketing AI & "
            "Analytics Lead' wants (1) marketing analytics/BI ownership and (2) building practical AI/automation/"
            "agentic workflows for marketing. Half (2) is Paula's signature — the DoFreeze generative-AI marketing "
            "automation system (Claude/GPT, -40% manual workload). Half (1) she covers via hands-on KPI/ROI/ROAS "
            "reporting, funnel/conversion analysis and dashboards (Power BI, Tableau, Looker) plus P&L fluency. "
            "Genuine gaps — formal attribution modelling, incrementality testing and MMPs — are adjacent, not core, "
            "and handled honestly in the cover letter. Tenure is on-band (4-7 yrs asked, 4+ held). Recruiter role, "
            "undisclosed client and salary; competition is high, so the AI-automation angle is the wedge."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX->PDF with LibreOffice headless (docx2pdf/Word is unreliable
    on this Mac). Removes the intermediate DOCX on success."""
    outdir = docx_path.parent
    subprocess.run(
        [SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(docx_path)],
        check=True,
        capture_output=True,
    )
    pdf_path = docx_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError(f"LibreOffice did not produce {pdf_path}")
    docx_path.unlink(missing_ok=True)
    return pdf_path


def _relocate_to_dated_folder(pos_dir: Path) -> Path:
    """Move output/<Company> - <Role>/ under output/<DATE_FOLDER>/."""
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

    # --- CV ---
    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    # --- Cover letter ---
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, contact_name=None)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
