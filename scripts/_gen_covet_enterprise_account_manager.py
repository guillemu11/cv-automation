"""One-off: Paula's CV for CoVet — "Enterprise Account Manager" (remote-first,
EUR 50-85K/year, hiring regions Spain / France / Germany).

CoVet is an AI copilot for veterinary professionals. The role is enterprise
account management + rollout/implementation coordination: onboarding enterprise
clients onto the platform, tracking milestones, driving adoption, running
check-ins and QBR prep, and keeping everything organised in HubSpot.

Why this is a genuinely strong fit (no stretching required):
  - Account management IS her core track, not an adjacent skill: 42 key accounts
    at Alibaba's Miravia (+30% GMV QoQ, reporting to the CEO) and XL strategic
    accounts at Glovo (KFC, Taco Bell, La Tagliatella, Sushi Shop).
  - Onboarding clients onto a tech platform is something she has actually done
    twice: onboarded 30+ new stores onto Miravia in two months as PIC Fragrances,
    and onboarded fashion/lifestyle brands onto Glovo's new Retail vertical —
    that is implementation + adoption work, in the JD's own terms.
  - Proven track record of hitting KPIs and targets: +30% GMV QoQ against P&L
    targets, forecasting accuracy, ROI/conversion/retention ownership.
  - Execution and project coordination: 6 NPD launches end-to-end (brief,
    packaging, pricing, go-to-market) across 50+ markets — timelines, checklists,
    cross-functional alignment, blockers flagged. Plus quick-commerce platform
    integrations (Noon, Talabat, Careem, Deliveroo): onboarding, listings,
    promotional mechanics — rollout work by another name.
  - Stakeholder management and communication: CEO-level reporting, distributor
    and retail partner management, cross-functional work with marketing,
    logistics and support.
  - AI product empathy: CoVet sells an AI copilot; Paula built a working
    generative-AI (Claude/GPT) automation system into her own workflow, so she
    can speak credibly about adoption of AI tooling by non-technical users.

Honest gaps — stated plainly, never disguised:
  - Veterinary industry ("preferably") — none. Her sectors are FMCG, beauty,
    fashion, e-commerce and quick-commerce.
  - HubSpot specifically — she uses Salesforce. Framed as "CRM (Salesforce;
    HubSpot-equivalent)", no HubSpot claim.
  - B2B SaaS customer success motion (QBRs by that name, usage summaries,
    adoption tracking inside a software product) — adjacent, not owned. Her
    account work is commercial/marketplace, not software CS.
  - French / German ("strong asset") — neither. Spanish native, English C1.
  - Location: the posting's hiring regions are Spain, France and Germany and
    Paula is based in Dubai (Spanish national). This is a real logistical
    question for the employer, surfaced honestly in the dashboard notes rather
    than hidden; the CV states Dubai as-is.
  - NO "no sponsorship needed" claim (standing rule). NO Arabic claim.

Fills the real CV template, converts DOCX -> PDF via LibreOffice (docx2pdf/Word
silently fails on this Mac), registers the job for the dashboard, and lands the
package under output/2026-09-16/.
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
from career_ops.generators import cv_generator as cv

COMPANY = "CoVet"
TITLE = "Enterprise Account Manager"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Enterprise Account Manager — CoVet. Remote-first, full-time.
EUR 50,000-85,000 per year (hiring regions: Remote Spain / France / Germany).

CoVet is an AI copilot application built to assist veterinary professionals by
saving them time so they can focus on animal care. Small, passionate, agile team
with a mission to improve the veterinary industry through technology.

About the role: a highly organised and customer-focused Enterprise Account
Manager to support the success of enterprise rollouts within the veterinary
industry, working closely with the Enterprise Accounts Lead to ensure smooth
implementation, customer adoption and long-term account success. Coordinate
rollout activities, support client communication and track milestones. Ideal for
someone with account management or project coordination experience who thrives in
a fast-paced environment.

What you'll do:
- Support enterprise rollouts by coordinating tasks, tracking progress and
  assisting with client communications.
- Drive customer engagement: check-in emails, scheduling QBRs, preparing usage
  summaries.
- Assist the Enterprise Accounts Lead in maintaining strong relationships with
  enterprise clients — follow-ups, documentation, day-to-day tasks.
- Prepare materials and insights for strategic account planning sessions and
  customer check-ins.
- Support implementation: track milestones, gather customer information, ensure
  internal alignment.
- Create and maintain implementation timelines and checklists for on-time delivery.
- Facilitate customer onboarding: schedule training sessions, send welcome
  materials, ensure completion of early adoption tasks.
- Assist with onboarding and adoption tracking so enterprise clients get the most
  from the platform.
- Identify opportunities to increase adoption within your accounts using strategy,
  creativity and practical insight.
- Manage and organise account activity within HubSpot.
- Monitor implementation tasks and flag risks or blockers to the right team members.
- Serve as a helpful point of contact for enterprise customers, escalating
  questions and issues appropriately.
- May involve attending in-person meetings, trainings or industry events.

Qualifications:
- Account executive / management experience, preferably in the veterinary
  industry or a related field.
- Proven track record of hitting KPIs and monthly targets.
- Strong organisational and execution skills, able to manage complex deployments.
- Demonstrated ability to guide clients through implementation and adoption.
- Excellent communication and stakeholder management skills.
- Fluency in English required; French and/or German a strong asset.
- Proficiency in CRM tools (e.g. HubSpot) and project management platforms.

Why join: remote-first culture with flexible working arrangements; shape the
future of a fast-growing company.
"""

ATS = [
    "Enterprise Account Manager", "account management", "account executive",
    "key account management", "strategic accounts", "enterprise accounts",
    "enterprise rollouts", "rollout coordination", "implementation",
    "implementation timelines", "milestones", "checklists", "deployment",
    "onboarding", "customer onboarding", "adoption", "adoption tracking",
    "customer engagement", "customer success", "QBR", "quarterly business review",
    "account planning", "check-ins", "usage summaries", "client communication",
    "stakeholder management", "escalation", "risks and blockers",
    "cross-functional alignment", "project coordination", "project management",
    "KPIs", "monthly targets", "quota", "revenue growth", "GMV", "P&L",
    "forecasting", "retention", "upsell", "relationship management",
    "negotiation", "CRM", "HubSpot", "Salesforce", "reporting", "data-driven",
    "Power BI", "Tableau", "Looker", "AI", "generative AI", "Claude",
    "AI tool adoption", "SaaS", "platform", "marketplace", "remote", "English",
    "Spanish", "organisational skills", "fast-paced",
]

CV_CONTENT = {
    "headline": (
        "Enterprise & Key Account Management · Client Onboarding and Adoption · "
        "Rollout Coordination · CRM and KPI Ownership"
    ),
    "professional_summary": (
        "Account manager with 4+ years owning enterprise and key-account portfolios — 42 accounts at Alibaba's "
        "Miravia (+30% GMV QoQ) and XL strategic accounts at Glovo. I onboard clients onto platforms, run the "
        "implementation timeline, drive adoption and hit monthly targets."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE (remote across 50+ markets)",
            "context": "FMCG / e-commerce group | Brands: Befit, Eurocake, Flair | 50+ markets",
            "bullets": [
                "Own partner relationships and integrations with major platforms (Noon, Talabat, Careem, Deliveroo) — onboarding, listings, promotional mechanics and account performance",
                "Run 6 product launches end-to-end across 50+ markets, owning timelines, checklists and cross-functional alignment, flagging blockers early to protect go-live dates",
                "Lead a two-person team and drove adoption of a generative-AI (Claude/GPT) workflow across the function — real experience getting non-technical users to adopt new tooling (~40% less manual work)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce platform | 100K+ employees",
            "bullets": [
                "Owned a 42-account enterprise portfolio — relationships, joint planning, business reviews and escalations — delivering +30% GMV growth QoQ against monthly KPIs and P&L targets",
                "Onboarded 30+ new partner stores onto the platform in two months as category lead, guiding each through implementation, catalogue setup and early adoption until trading independently",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce platform | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL strategic accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) as their day-to-day point of contact, growing orders through data-led joint planning",
                "Coordinated the rollout of Glovo's new Retail vertical — onboarding fashion and lifestyle partners, tracking milestones and aligning marketing, logistics and support on go-live dates",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional reporting for the chocolate category, turning account data into commercial recommendations",
            ],
        },
    ],
    "skills_brand": (
        "enterprise & key account management, client onboarding and adoption, rollout & implementation "
        "coordination, account planning, stakeholder management, escalation handling"
    ),
    "skills_ecommerce": (
        "platform onboarding & integrations (marketplace, quick-commerce), catalogue and listing setup, "
        "promotional mechanics, adoption tracking, Shopify, AI tool rollout"
    ),
    "skills_commercial": (
        "KPI & monthly target delivery, negotiation, pricing & promotion strategy, P&L awareness, "
        "forecasting, team leadership (2 reports)"
    ),
    "skills_data": (
        "GMV, ROI, conversion and retention analysis, performance reporting & usage summaries, "
        "Salesforce (CRM), Power BI, Looker, advanced Excel"
    ),
    "skills_tools": (
        "Salesforce (CRM; HubSpot-equivalent), Power BI, Looker, Generative AI (Claude, ChatGPT), "
        "Microsoft Office — Expert, Canva"
    ),
}


def make_job() -> Job:
    return Job(
        id="covet-enterprise-account-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Remote — Spain / France / Germany",
        url="https://es.indeed.com/",
        source="indeed",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Enterprise Account Manager CoVet remote",
            "function": "Enterprise Account Management / Customer Success (B2B SaaS)",
            "workplace": "Remote-first; hiring regions Spain, France, Germany",
            "salary": "EUR 50,000-85,000 / year",
            "note": (
                "AI copilot for veterinary professionals. Strong account-management fit; "
                "main frictions are the veterinary vertical, HubSpot vs Salesforce, and that "
                "Paula is based in Dubai while the hiring regions are Spain/France/Germany."
            ),
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
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "url": job.url,
        "source": job.source,
        "description": job.description,
        "salary_raw": "EUR 50,000-85,000 / year",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 72,
        "ai_tier": "Warm",
        "skills_match": [
            "Account management is her core track, not an adjacent skill: 42 key accounts at Alibaba's Miravia (+30% GMV QoQ, CEO-level reporting) and XL strategic accounts at Glovo (KFC, Taco Bell, La Tagliatella, Sushi Shop)",
            "Has genuinely onboarded clients onto platforms twice: 30+ partner stores onto Miravia in two months, and fashion/lifestyle brands onto Glovo's new Retail vertical — implementation + adoption in the JD's own terms",
            "Proven KPI and monthly-target delivery against P&L: +30% GMV QoQ, forecasting accuracy, ROI/conversion/retention ownership",
            "Rollout/project coordination: 6 NPD launches end-to-end across 50+ markets with timelines, checklists, cross-functional alignment and early blocker flagging; plus Noon/Talabat/Careem/Deliveroo platform integrations",
            "Stakeholder management and communication at CEO level, plus distributor, retail-partner and cross-functional (marketing, logistics, support) coordination",
            "CRM and reporting fluency: Salesforce, Power BI, Tableau, Looker, advanced Excel — usage summaries and account-planning materials are routine output",
            "AI product empathy: CoVet sells an AI copilot; Paula built and drove adoption of a Claude/GPT workflow among non-technical colleagues — directly relevant to selling and embedding an AI tool",
            "Remote-first: already works remotely across 50+ markets; Spanish native, English C1",
        ],
        "missing_skills": [
            "Veterinary industry ('preferably') — none; her sectors are FMCG, beauty, fashion, e-commerce and quick-commerce",
            "HubSpot specifically — she uses Salesforce; CV says 'CRM (Salesforce; HubSpot-equivalent)', no HubSpot claim",
            "B2B SaaS customer-success motion — QBRs by that name, in-product usage summaries and software adoption tracking are adjacent, not owned; her account work is commercial/marketplace",
            "French and/or German ('strong asset') — neither",
            "Dedicated project-management platforms (Asana/Monday/Jira) not named in her stack",
        ],
        "sector_fit": "adjacent (marketplace / quick-commerce / FMCG account management vs veterinary B2B SaaS) — the account-management craft transfers cleanly, the vertical does not",
        "seniority_fit": "on-band — the JD explicitly targets someone continuing to grow their enterprise skillset, which matches 4+ years of key/strategic account ownership",
        "red_flags": [
            "Location: hiring regions are Spain, France and Germany; Paula is a Spanish national but based in Dubai (GMT+4). Needs clarifying up front — it is the most likely reason for an early rejection",
            "Veterinary vertical is 'preferred' and she has none",
            "French/German listed as a strong asset; she has neither",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Genuinely good fit on the axis the role is built around. Enterprise/key account management is "
            "Paula's actual career track — 42 accounts at Alibaba's Miravia with +30% GMV QoQ against monthly "
            "KPIs and CEO-level reporting, and XL strategic accounts at Glovo. Crucially, she has really done "
            "the implementation-and-adoption half of this job: onboarding 30+ partner stores onto Miravia in "
            "two months and rolling out Glovo's new Retail vertical by onboarding fashion partners, tracking "
            "launch milestones and aligning marketing/logistics/support. Add 6 end-to-end launches across 50+ "
            "markets (timelines, checklists, blockers) and platform integrations with Noon/Talabat/Careem/"
            "Deliveroo, and the rollout-coordination requirement is covered by real work. Her AI-adoption "
            "experience is a bonus for a company selling an AI copilot. Honest gaps: no veterinary exposure, "
            "no HubSpot (Salesforce instead), no French or German, and the B2B SaaS customer-success layer "
            "(QBRs, in-product usage data) is adjacent rather than owned. The biggest practical risk is "
            "geographic: the posting hires in Spain/France/Germany and she is in Dubai."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (docx2pdf/Word fails on this Mac)."""
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

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
