"""One-off: generate Paula's CV (+ cover letter) for a recruiter-posted
"Marketing Manager" role at a growing pet-supplement D2C brand (part of a larger
human vitamins/supplements group). Remote-first, startup-like, paid-media-led.

Why this is a genuinely strong fit (honest):
  - CORE = paid social + paid search for D2C: "planning, launching and managing
    campaigns across Meta Ads and Google Ads for our D2C sites", owning strategy,
    budget allocation, bidding strategy and performance targets, with a
    test-and-learn analytics mindset and performance reporting. This is precisely
    what Paula runs TODAY at DoFreeze (Meta + Google paid media on a Shopify D2C,
    A/B testing, ROI/ROAS/conversion) — a direct, concrete match.
  - Manage multiple marketing channels + D2C/e-commerce: strong (Shopify/CRO,
    social, influencer, EDM, quick-commerce).
  - Fluent English (C1); remote-first actually SUITS her — Dubai-based, keeps her
    location, works with an international senior-led team.
  - Health/supplements is only "a plus": honest adjacency via a health & fitness
    FMCG brand (Befit) in her DoFreeze portfolio + beauty/personal care (Miravia).

Honest gaps (disclosed, NOT fabricated):
  - Team building / people management: JD wants "build out a team", "comfortable
    managing teams and delegating". Paula has scaled delivery by managing
    creators, agencies and freelancers and led cross-functional teams, and owns
    marketing as a function — but she has NOT built/run a direct-report team at
    scale. Framed as the natural, ready next step; NOT overstated as prior
    people-management tenure.
  - Sector pet/supplements/subscription is not direct (health-adjacent FMCG +
    beauty); disclosed, bridged honestly.
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-21/.
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

COMPANY = "Pet Supplement Brand"
TITLE = "Marketing Manager"
DATE_FOLDER = "2026-08-21"

CONTACT = None  # Recruiter posting, brand confidential — letter to "Hiring Manager".

JOB_DESCRIPTION = """\
Marketing Manager — growing pet-supplement brand (confidential, via recruiter),
part of a larger group with deep roots in human vitamins and supplements. Take
full ownership of the marketing channels in a startup-like, remote-first
environment.

Responsibilities (not limited to):
- Be strategic with hands-on work in planning, launching and managing campaigns
  across Meta Ads and Google Ads for the D2C sites.
- Build out a team as we grow.
- Own strategy, budget allocation, bidding strategy and performance targets.
- Report on performance and translate numbers into clear next steps.

Candidate profile:
- Must be fluent in English, written and spoken.
- Strong knowledge in either Meta or Google.
- Experience managing multiple marketing channels.
- Experience in pet, health, supplements or subscription categories is a plus.
- Hands-on experience running paid social and paid search for DTC or e-commerce
  brands.
- Comfortable managing teams and delegating.
- A test-and-learn analytics mindset.
- Good discipline with the document flow.

What our client offers: competitive base salary; high-impact role with exposure to
senior stakeholders and strategic decision-making; remote-first setup with
flexibility and autonomy; senior-led international team combining startup agility
with established expertise; fast-paced, ownership-driven environment with clear
growth opportunities.
"""

ATS = [
    "Marketing Manager", "paid social", "paid search", "Meta Ads", "Facebook Ads",
    "Instagram Ads", "Google Ads", "PPC", "performance marketing",
    "growth marketing", "D2C", "DTC", "e-commerce", "campaign management",
    "budget allocation", "bidding strategy", "performance targets",
    "test-and-learn", "A/B testing", "experimentation", "conversion rate",
    "CRO", "ROI", "ROAS", "CPA", "cost per acquisition", "audience building",
    "multiple marketing channels", "multi-channel", "performance reporting",
    "translate numbers into next steps", "analytics", "customer behaviour",
    "team management", "build a team", "delegating", "managing teams",
    "creators", "agencies", "freelancers", "Shopify", "EDM", "CRM",
    "subscription", "health", "supplements", "pet", "FMCG",
    "senior stakeholders", "remote-first", "startup", "ownership", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Marketing Manager · Paid Social & Paid Search (Meta + Google Ads) · D2C / E-Commerce Growth · "
        "Budget, Bidding & Performance Targets · Test-and-Learn Analytics"
    ),
    "professional_summary": (
        "Performance and growth marketer who runs paid social and paid search (Meta Ads + Google Ads) for a "
        "D2C/e-commerce business today, with five years across e-commerce, FMCG, beauty and health-adjacent "
        "consumer goods. I own the full paid-media loop end-to-end — strategy, budget allocation, audience "
        "building, creative A/B testing, bidding and optimisation — and hold it to hard performance targets "
        "(ROI, ROAS, CPA, conversion), translating the numbers into clear next steps with a genuine "
        "test-and-learn mindset. I manage multiple channels around paid (Shopify D2C store / CRO, social, "
        "influencer, EDM) and scale delivery by coordinating creators, agencies and freelancers — so building "
        "and leading an in-house team as the function grows is the next step I'm ready for. Remote-capable from "
        "Dubai, fluent English (C1). Business Administration graduate (CUNEF)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Portfolio incl. a health & fitness brand (Befit), Eurocake, Flair",
            "bullets": [
                "Plan, launch and manage paid media end-to-end across Meta Ads (Facebook & Instagram) and Google Ads for the D2C business — audience building, creative A/B testing, budget allocation and bidding — optimising to ROI, ROAS, CPA and conversion targets",
                "Own the paid-media budget and performance targets, running a continuous test-and-learn loop and translating results into clear next-step recommendations for leadership",
                "Run the D2C / Shopify e-store end-to-end (CRO, UX, merchandising, checkout), turning paid traffic into conversion and higher average order value",
                "Manage multiple channels around paid — social, influencer/UGC, EDM and e-commerce — coordinating and delegating to creators, agencies and freelancers across campaigns",
                "Built an AI-powered analytics & automation system (Claude / generative AI) that speeds up performance reporting, creative iteration and campaign planning",
                "Market a portfolio that includes a health & fitness brand (Befit) — directly relevant to health / supplement consumer categories",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Grew 42 accounts +30% GMV QoQ through data-led promotions, assortment and pricing — hard commercial targets, measurable results",
                "Analysed conversion, traffic, retention, ROI and ROAS continuously to optimise channel performance and forecasting — a test-and-learn operating rhythm",
                "Created and led the 'Beauty Club' loyalty programme and 'Hot on Social' content programme in beauty & personal care (health/wellness-adjacent), across multiple channels",
                "Owned the Flash Sales channel reporting directly to the CEO, executing performance-driven commercial plans against P&L targets",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Drove GMV growth for strategic accounts through data-led campaigns and paid activations on a quick-commerce super-app",
                "Ran complex cross-functional campaigns from concept to execution, coordinating marketing, operations and logistics teams",
                "Helped build Glovo's Retail vertical — 0-to-1 launches taking new brands to market on the platform",
                "Negotiated and closed commercial deals and managed external partners and vendors",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out, promotional-effectiveness and performance analysis for the chocolate category",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
                "Distilled data into actionable insight and clear next steps for leadership",
            ],
        },
    ],
    "skills_brand": (
        "growth & performance marketing, multi-channel campaign management, D2C / e-commerce marketing, "
        "brand & content, influencer & UGC, go-to-market, product launches"
    ),
    "skills_ecommerce": (
        "paid social (Meta / Facebook / Instagram Ads), paid search (Google Ads), budget allocation & bidding "
        "strategy, A/B testing & experimentation, conversion rate optimisation (CRO), Shopify D2C e-store, "
        "EDM / CRM, marketing automation, quick-commerce"
    ),
    "skills_commercial": (
        "budget ownership & performance targets, team coordination & delegation (creators, agencies, "
        "freelancers), ready to build & lead a growing function, senior-stakeholder reporting, project "
        "management, key account management, negotiation"
    ),
    "skills_data": (
        "test-and-learn analytics, ROI / ROAS / CPA / conversion analysis, performance reporting & next-step "
        "recommendations, KPI tracking, customer-behaviour analysis, Power BI, forecasting, P&L"
    ),
    "skills_tools": (
        "Meta Ads Manager, Google Ads, Meta Business Suite, Generative AI (Claude, ChatGPT), Shopify, "
        "Power BI, Salesforce (CRM), Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "A growing pet-supplement D2C brand looking for someone to take full ownership of paid media — "
        "strategic and hands-on across Meta and Google, owning budget, bidding and performance targets in a "
        "startup-like, remote-first setup — describes what I do every day. I'm a performance and growth "
        "marketer who runs paid social and paid search for a D2C/e-commerce business now, and I love the "
        "combination this role offers: real ownership of the numbers, plus the chance to build the channel — "
        "and the team — as the brand scales."
    ),
    "body_paragraph_1": (
        "On the core of the role I'm a direct match. At DoFreeze I plan, launch and manage paid campaigns "
        "across Meta Ads (Facebook & Instagram) and Google Ads for the D2C business — audience building, "
        "creative A/B testing, budget allocation and bidding — and I hold everything to hard targets (ROI, "
        "ROAS, CPA, conversion), running a continuous test-and-learn loop and translating results into clear "
        "next steps for leadership. I run the Shopify store end-to-end (CRO, UX, checkout) so I optimise the "
        "whole funnel, not just the click, and I manage multiple channels around paid (social, influencer, "
        "EDM). Before Dubai I built the same performance rhythm inside two data-led businesses: at Alibaba's "
        "Miravia I grew 42 accounts +30% GMV QoQ analysing conversion, ROI and ROAS daily; at Glovo I ran "
        "complex campaigns on a quick-commerce super-app. I've also built an AI-powered system (Claude) that "
        "speeds up my reporting, creative iteration and planning."
    ),
    "body_paragraph_2": (
        "Two honest notes. First, on team-building: I've scaled delivery by coordinating and delegating to "
        "creators, agencies and freelancers and by leading cross-functional teams, and I own marketing as a "
        "function today — but I haven't yet run a large direct-report team, so building and leading the "
        "in-house team as you grow is a step I'm genuinely ready for rather than one I've done at scale. "
        "Second, on category: my background is e-commerce, FMCG and beauty rather than pet supplements "
        "specifically, though I market a health & fitness brand (Befit) and beauty/personal-care lines today, "
        "so health-and-wellness consumer goods and D2C subscription-style retention are familiar, and I ramp "
        "fast. A remote-first, senior-led international team suits me well — I'm Dubai-based and used to working "
        "across markets and time zones."
    ),
    "closing_paragraph": (
        "I'd love to own and grow this brand's paid media and prove it in the numbers — I can share paid-media "
        "case studies and performance results, from +30% GMV QoQ to funnel and creative optimisation. I'm "
        "Dubai-based, comfortable remote-first, and available to talk through how I'd approach strategy, budget "
        "and the first performance targets. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="petsupplement-marketing-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Remote-first (Dubai-based)",
        url="",
        source="recruiter",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing Manager paid media D2C",
             "function": "Performance / paid-media marketing (Meta + Google) for D2C",
             "sector": "Pet supplements / health & vitamins (D2C, subscription-adjacent)",
             "note": "Strong CORE fit (paid social + paid search for D2C — exactly her DoFreeze work). "
                     "Soft spots disclosed honestly: formal team-building/people-management (she's coordinated "
                     "creators/agencies/cross-functional but not run a direct-report team at scale) and exact "
                     "sector (pet/supplements is only 'a plus'; health-adjacent via Befit + beauty). Remote-first "
                     "suits her Dubai base. No 'own visa / no sponsorship' claim."},
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
        "salary_raw": "Competitive base salary (not disclosed)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 80,
        "ai_tier": "Hot",
        "skills_match": [
            "CORE MATCH: runs paid social (Meta Ads) + paid search (Google Ads) for a D2C/Shopify business TODAY — planning, launching, managing campaigns",
            "Owns strategy, budget allocation, bidding and performance targets (ROI/ROAS/CPA/conversion)",
            "Test-and-learn analytics mindset — continuous A/B testing, performance reporting, translating numbers into next steps",
            "Manages multiple marketing channels around paid (Shopify/CRO, social, influencer/UGC, EDM)",
            "Coordinates & delegates to creators, agencies and freelancers; leads cross-functional teams",
            "Health/supplement adjacency (only 'a plus'): markets a health & fitness brand (Befit) + beauty/personal care (Miravia)",
            "Fluent English (C1); remote-first suits her (Dubai-based, international-team ready)",
            "AI-powered analytics/automation (Claude) that speeds reporting, creative iteration & planning — extra edge for a lean startup team",
        ],
        "missing_skills": [
            "Team building / people management at scale — JD wants 'build out a team' + 'managing teams and delegating'. She's managed creators/agencies/freelancers and cross-functional teams and owns a function, but has NOT run a large direct-report team. Framed as a ready next step, not overstated",
            "Exact sector (pet / supplements / subscription) — only 'a plus'; she is health-adjacent FMCG + beauty, disclosed honestly",
        ],
        "sector_fit": "adjacent+ (health-adjacent FMCG via Befit + beauty; pet/supplements only a 'plus', not required)",
        "seniority_fit": "on-band (Marketing Manager; paid-media ownership is a direct match; team-building is the step-up)",
        "red_flags": [
            "Only real soft spot is formal team-building/people-management — disclosed candidly in the cover letter as a ready next step, not fabricated.",
            "'Competitive base salary' not disclosed — remote-first international role; confirm the number lands at/above Paula's 20k AED floor before advancing.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); remote-first so visa is likely a non-issue, but not asserted either way.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit. The role's core is exactly Paula's day job: strategic + hands-on paid social "
            "and paid search (Meta + Google) for D2C sites, owning strategy, budget allocation, bidding and "
            "performance targets, with a test-and-learn analytics mindset and performance reporting that "
            "translates numbers into next steps. She runs precisely this on a Shopify D2C at DoFreeze (Meta + "
            "Google, A/B testing, ROI/ROAS/CPA/conversion) and built the same rhythm at Alibaba's Miravia and "
            "Glovo. Multiple-channel management and D2C/CRO are strong. Honest soft spots: (1) formal team-"
            "building/people-management — she coordinates creators/agencies/freelancers and leads cross-"
            "functional teams and owns a function, but hasn't run a large direct-report team, framed as a ready "
            "next step; (2) exact sector (pet/supplements/subscription) is only 'a plus' and bridged honestly "
            "via a health & fitness brand (Befit) and beauty/personal care. Remote-first suits her Dubai base "
            "and fluent English. Confirm the undisclosed 'competitive base' meets the 20k AED floor. No 'own "
            "visa / no sponsorship' claim."
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

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
