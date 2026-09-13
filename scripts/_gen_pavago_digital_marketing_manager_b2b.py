"""One-off: generate Paula's CV + cover letter for Pavago
"Digital Marketing Manager (B2B)" — a full-time, REMOTE role working US Eastern
(EST) hours, hiring on behalf of an unnamed US B2B/SaaS/professional-services
client. Owns the full B2B marketing funnel: demand generation, paid media, SEO,
outbound, content and brand, with analytics/reporting and team/agency leadership.

Why this is an honest, warm fit (craft matches; sector + setup have friction):
  - The spine of the role is Paula's day-to-day craft: own the marketing funnel
    end-to-end (awareness → demand gen → nurture → conversion); run multi-channel
    campaigns across paid media (Google Ads, Meta Ads), SEO, email/EDM, social,
    content and partnerships; manage budgets to maximise ROI/ROAS; track CAC/CPL,
    conversion, traffic and revenue; build dashboards and reports; run A/B tests;
    guide content/design teams and external agencies/contractors; and lead
    brand positioning and messaging. She does all of this today at DoFreeze.
  - Cross-functional work with sales + direct commercial/B2B relationships map
    honestly to her Key Account / Account Manager years at Alibaba's Miravia
    (42 accounts, +30% GMV QoQ, 30+ stores onboarded) and Glovo — she sells TO
    businesses, manages distributor networks and aligns marketing with revenue.
  - Generative-AI automation (Claude/GPT) for content, campaign planning and
    reporting — a rare edge for a fast, experiment-driven growth function.

Honest positioning (NO fabrication):
  - Sector: her background is B2C — FMCG / Beauty / Fashion / E-Commerce /
    quick-commerce — NOT B2B SaaS / professional services. Her genuine B2B angle
    is commercial: key account management, distributor/modern-trade management and
    trade marketing (selling to and through businesses). ABM / SaaS demand-gen
    pipeline (MQL→SQL) motion is NOT claimed as owned; the transferable funnel,
    paid, SEO, content and analytics craft is.
  - HubSpot / Marketo: named as required/preferred. Paula uses Salesforce (CRM)
    plus Meta/Google — she does NOT have HubSpot experience. Positioned as
    "CRM & marketing automation (Salesforce); quick to adopt HubSpot/Marketo",
    never as HubSpot experience.
  - LinkedIn Ads: JD lists it alongside Google/Meta. Paula runs Google + Meta
    genuinely; LinkedIn Ads is framed as a channel she's ready to run, not owned.
  - "Excellent English" — she is C1 professional (stated as such), not native.
  - Remote + US Eastern (EST) hours ≈ 18:00–02:00 Dubai time — a real practical
    consideration (profile is remote_ok:false). Flagged to Paula; the letter only
    notes she is set up for remote work with distributed/US teams — no permanent
    night-shift commitment is baked in for her.
  - NO "no sponsorship needed" claim — the visa is employer-sponsored (standing
    rule); the CV header only states "UAE Residence Visa".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-25/.
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

COMPANY = "Pavago"
TITLE = "Digital Marketing Manager (B2B)"
DATE_FOLDER = "2026-08-25"

# Recruiter posting on behalf of an unnamed client — no hiring manager named.
CONTACT = None

JOB_DESCRIPTION = """\
Digital Marketing Manager (B2B) — Pavago (on behalf of client). Full-Time, Remote.
Working Hours: U.S. Eastern Time (EST).

Our client is seeking a results-driven Digital Marketing Manager (B2B) to lead and
scale the company's marketing strategy across paid, organic, outbound, and brand
channels. Combines strategic leadership with hands-on execution; owns the full
marketing funnel from demand generation and lead nurturing to brand positioning
and performance optimisation.

Responsibilities:
- Develop and execute a comprehensive B2B marketing strategy aligned with growth goals.
- Own the marketing funnel end-to-end: awareness, demand gen, nurturing, conversion.
- Partner with leadership and sales to align marketing with revenue objectives.
- Build, manage and mentor marketing resources, agencies or contractors.
- Lead and optimise multi-channel campaigns across paid media, SEO, outbound,
  email marketing, social media, partnerships and content.
- Manage budgets and allocate spend to maximise ROI and efficiency.
- Track CAC, CPL, ROAS, conversion rates, traffic, MQLs, SQLs and revenue attribution.
- Build dashboards and reports (HubSpot, Google Analytics, Looker Studio).
- Continuously optimise via A/B testing and experimentation.
- Guide messaging strategy and brand positioning; support blogs, landing pages,
  outbound messaging and campaign assets.

Required: proven B2B marketing leadership (Head of Marketing / Growth Lead / Senior
Marketing Manager); measurable growth via paid ads, outbound, SEO and organic;
strong grasp of LinkedIn Ads, Google Ads, Meta Ads, HubSpot, analytics tools and
outbound systems; balancing strategy with hands-on execution; strong analytics.
Preferred: B2B service / SaaS / professional industries; ABM or performance-driven
demand gen; CRM/automation (HubSpot, Salesforce, Marketo); managing cross-functional
teams / external agencies; strong branding, storytelling and positioning; scaling
marketing systems in high-growth environments.
KPIs: MQLs/SQLs, CAC & marketing ROI, traffic & conversion growth, lead-to-opp and
opp-to-customer conversion, paid performance & ROAS, brand visibility & engagement.
"""

ATS = [
    "Digital Marketing Manager", "B2B marketing", "growth marketing",
    "demand generation", "performance marketing", "marketing strategy",
    "marketing funnel", "full funnel", "lead nurturing", "lead generation",
    "paid media", "paid ads", "Google Ads", "Meta Ads", "LinkedIn Ads",
    "Facebook Ads", "Instagram Ads", "SEO", "organic", "outbound marketing",
    "email marketing", "EDM", "social media", "content marketing", "partnerships",
    "budget management", "ROI", "ROAS", "CAC", "CPL", "cost per lead",
    "conversion rate", "conversion optimisation", "CRO", "A/B testing",
    "experimentation", "MQL", "SQL", "revenue attribution", "pipeline",
    "dashboards", "reporting", "Google Analytics", "Looker Studio", "analytics",
    "HubSpot", "Salesforce", "CRM", "marketing automation", "ABM",
    "brand positioning", "messaging", "storytelling", "landing pages",
    "campaign management", "go-to-market", "cross-functional", "sales alignment",
    "team leadership", "agency management", "remote", "SaaS",
]

CV_CONTENT = {
    "headline": (
        "Digital & Growth Marketing Manager · Full-Funnel Demand Generation · "
        "Paid Media (Google & Meta Ads), SEO & Content · Analytics, CRO & Reporting"
    ),
    "professional_summary": (
        "Results-driven digital & growth marketing manager with 4+ years owning the marketing funnel "
        "end-to-end — from awareness and demand generation through nurturing and conversion — across "
        "E-Commerce, FMCG, Beauty and Fashion. At DoFreeze I run multi-channel campaigns across paid media "
        "(Google Ads, Meta Ads), SEO/organic, email/EDM, social, content and partnerships; manage budgets to "
        "maximise ROI and ROAS; track CAC, cost per lead, conversion, traffic and revenue; build dashboards "
        "and performance reports; run continuous A/B testing; and guide content, design and creator teams "
        "while leading brand positioning and messaging. Earlier, as a Key Account / Account Manager at "
        "Alibaba's Miravia and Glovo, I partnered directly with sales and commercial teams — aligning "
        "marketing with revenue and growing GMV +30% QoQ across 42 accounts. Early adopter of generative AI "
        "(Claude/GPT) to scale content, campaign planning and analytics. Excellent English (C1), fully set up "
        "for remote work with distributed teams."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "FMCG e-commerce & distribution | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own the marketing funnel end-to-end — awareness, demand generation, nurturing and conversion — developing and executing multi-market strategy aligned with growth goals across 50+ markets",
                "Lead and optimise multi-channel campaigns across paid media (Google Ads, Meta Ads — Facebook & Instagram), SEO/organic, email/EDM, social, content and influencer partnerships — managing budgets and allocating spend to maximise ROI and ROAS",
                "Track and report performance — CAC, cost per lead, conversion rate, traffic, ROAS and revenue — building dashboards and clear reports, and running continuous A/B testing to refine targeting, messaging and budget allocation",
                "Improve landing pages and store UX from a conversion perspective (CRO) — own the Shopify e-store end-to-end (catalogue, UX, checkout) — lifting conversion rate and average order value through data-led testing",
                "Guide messaging and brand positioning and direct content, design and creator teams — briefing agencies/contractors and scaling an influencer/UGC programme from zero (25–50 creators per campaign) to strengthen brand visibility and engagement",
                "Built AI-powered automation (Claude/GPT) that scales campaign planning, content and KPI reporting — cutting manual workload ~40% and accelerating go-to-market",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Partnered directly with sales and commercial teams to align marketing and promotions with revenue targets — managing 42 key accounts and achieving +30% GMV growth QoQ through pricing, assortment and targeted campaigns",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via performance-driven promotions and trend-led products",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting, and created the Beauty Club and Hot on Social projects to lift brand visibility and engagement",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Worked cross-functionally across marketing, sales, logistics and support to launch campaigns and grow order volume — prospecting, qualifying and closing high-impact commercial deals",
                "Supported building Glovo's Retail vertical — onboarding new brand partners with tailored launch campaigns, promotions and data-led joint business planning",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, building performance reports in advanced Excel that informed spend and commercial planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) with data-driven analysis, turning category data into actionable recommendations",
            ],
        },
    ],
    "skills_brand": (
        "full-funnel demand generation, growth & digital marketing strategy, brand positioning & messaging, "
        "content marketing, storytelling, influencer & partnership marketing, go-to-market, campaign management, "
        "team & agency leadership, generative-AI campaigns"
    ),
    "skills_ecommerce": (
        "paid media (Google Ads, Meta Ads), SEO / organic, email marketing / EDM, social media, landing-page "
        "& website CRO, A/B testing & experimentation, Shopify, marketing automation, ready to run LinkedIn Ads"
    ),
    "skills_commercial": (
        "sales alignment & cross-functional collaboration, key account management, distributor & modern-trade "
        "management, lead generation & qualification, CRM & pipeline management, negotiation, "
        "pricing & promotion strategy, budget management"
    ),
    "skills_data": (
        "CAC, cost per lead (CPL), ROI, ROAS, conversion-rate & funnel analysis, traffic & revenue attribution, "
        "dashboards & performance reporting, KPI tracking, Google Analytics, Looker, Tableau, Power BI"
    ),
    "skills_tools": (
        "Google Ads, Meta Ads Manager, Meta Business Suite, Google Analytics, Looker, Tableau, Power BI, "
        "Salesforce (CRM) — quick to adopt HubSpot / Marketo, Shopify, Generative AI (Claude, ChatGPT), "
        "Canva, Microsoft Office — Expert (Excel, PowerPoint, Word)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "The Digital Marketing Manager (B2B) brief — a hands-on operator who can own the full marketing funnel, "
        "scale demand generation across paid, organic, outbound and brand, and connect every campaign to "
        "measurable pipeline and revenue — describes how I already work. I run multi-channel growth marketing "
        "end-to-end today, I'm analytical and execution-focused in equal measure, and I'm fully set up to work "
        "remotely with a distributed, US-based team."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze I own the funnel from awareness through conversion: I plan and "
        "optimise campaigns across paid media (Google Ads, Meta Ads), SEO/organic, email/EDM, social, content and "
        "partnerships; manage budgets to maximise ROI and ROAS; and track CAC, cost per lead, conversion, traffic "
        "and revenue in dashboards and clear performance reports, refining targeting and spend through continuous "
        "A/B testing. I also improve landing pages and store UX for conversion (CRO), lead brand positioning and "
        "messaging, and guide content, design and creator teams plus external contractors — so strategy and "
        "day-to-day execution sit in the same pair of hands."
    ),
    "body_paragraph_2": (
        "I'll be straightforward about where I'm coming from: my sector background is B2C — e-commerce, FMCG, "
        "beauty and fashion — rather than B2B SaaS, so I wouldn't overclaim an ABM or MQL-to-SQL playbook I "
        "haven't owned. What does transfer cleanly is the craft (paid, SEO, content, funnel ownership, analytics "
        "and reporting) and genuine B2B commercial experience: as a Key Account / Account Manager at Alibaba's "
        "Miravia and Glovo I partnered directly with sales, managed 42 accounts and distributor relationships, "
        "and aligned marketing with revenue — growing GMV +30% QoQ and onboarding 30+ new stores in two months. "
        "I work in Salesforce and am quick to pick up HubSpot, and I bring generative-AI automation (Claude/GPT) "
        "that lets a lean team test, produce and report at real speed."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to walk through how I'd approach the first 90 days — auditing the funnel, "
        "prioritising the paid, SEO and content bets with the best ROI, and standing up the dashboards and "
        "experimentation cadence to prove pipeline impact quickly. I have excellent English (C1) and I'm set up "
        "for focused remote work. Thank you for considering my application — I'd be glad to share specifics on "
        "how I'd scale this client's demand generation."
    ),
}


def make_job() -> Job:
    return Job(
        id="pavago-digital-marketing-manager-b2b-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Remote (Dubai) · US Eastern (EST) hours",
        url="https://ae.indeed.com/jobs?q=Pavago+Digital+Marketing+Manager+B2B&l=Dubai",
        source="indeed",
        description=JOB_DESCRIPTION,
        raw={"query": "Pavago Digital Marketing Manager B2B Dubai remote",
             "function": "B2B Digital / Growth Marketing (full-funnel demand gen)",
             "workplace": "Remote, US Eastern (EST) working hours",
             "note": "Pavago = recruiter hiring remote talent for a US B2B/SaaS/professional-services client; no hiring manager named; salary not disclosed"},
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
        "salary_raw": "Not disclosed (remote, US Eastern hours)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 62,
        "ai_tier": "Warm",
        "skills_match": [
            "Owns the marketing funnel end-to-end (awareness → demand gen → nurture → conversion) today at DoFreeze",
            "Multi-channel campaigns: paid media (Google Ads, Meta Ads), SEO/organic, email/EDM, social, content, partnerships",
            "Budget management to maximise ROI/ROAS; tracks CAC, CPL, conversion, traffic, revenue",
            "Dashboards & performance reporting + continuous A/B testing / experimentation (Google Analytics, Looker)",
            "Landing-page & website CRO; owns Shopify store end-to-end",
            "Brand positioning, messaging & content; guides content/design/creator teams and external agencies/contractors",
            "Cross-functional sales alignment + genuine B2B commercial experience (KAM, distributor/modern-trade management)",
            "+30% GMV QoQ across 42 accounts; onboarded 30+ new stores in two months (Alibaba's Miravia)",
            "Generative-AI automation (Claude/GPT) for content, campaign planning and reporting",
            "Excellent English (C1); fully set up for remote work with distributed teams",
        ],
        "missing_skills": [
            "B2B SaaS / professional-services sector experience — her background is B2C (FMCG/Beauty/Fashion/E-commerce); B2B angle is commercial (KAM/distributors), not SaaS demand-gen",
            "ABM and classic MQL→SQL demand-gen pipeline motion — not owned; transferable funnel/paid/SEO/analytics craft is (framed honestly, not overclaimed)",
            "HubSpot / Marketo — she uses Salesforce (CRM); positioned as 'quick to adopt HubSpot', never as HubSpot experience",
            "LinkedIn Ads — runs Google + Meta genuinely; LinkedIn Ads framed as a channel she's ready to run, not owned",
            "'Excellent English' required — she is C1 professional (stated as such), not native",
        ],
        "sector_fit": "adjacent (full-funnel growth-marketing craft is a direct match; B2B SaaS sector is new — her B2B is commercial via KAM/distributors, positioned honestly)",
        "seniority_fit": "on-band — Manager-level role matches Paula's current Brand & Marketing Manager seniority (lateral)",
        "red_flags": [
            "REMOTE + US Eastern (EST) working hours ≈ 18:00–02:00 Dubai time — profile is remote_ok:false; real lifestyle/timezone consideration Paula must weigh",
            "B2B SaaS / professional-services demand-gen focus vs her B2C e-commerce/FMCG/beauty/fashion background — soft sector gap, framed truthfully",
            "HubSpot/Marketo named as required/preferred — she has Salesforce, not HubSpot (transferable, but a stated gap)",
            "Salary not disclosed — cannot confirm against her 20,000 AED/month floor; remote-via-staffing roles vary widely",
            "Recruiter (Pavago) posting for an unnamed end client — company, product and comp opaque until first call",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Warm, honest fit on craft with real practical friction. The role is a hands-on B2B digital/growth "
            "marketing manager: own the full funnel (demand gen → nurture → conversion), run multi-channel "
            "campaigns across paid media (Google/Meta/LinkedIn Ads), SEO, outbound, email, social and content, "
            "manage budgets for ROI/ROAS, track CAC/CPL/MQL/SQL/conversion/revenue, build dashboards, A/B test, "
            "and lead brand positioning plus content/design teams and agencies — most of which Paula does today "
            "at DoFreeze (paid, SEO, content, CRO, analytics, reporting, team leadership, AI automation). Her "
            "cross-functional sales alignment and B2B commercial relationships (KAM at Alibaba's Miravia: 42 "
            "accounts, +30% GMV QoQ, 30+ stores; distributor/modern-trade management) give a genuine B2B angle. "
            "Honest gaps: her sector is B2C not SaaS; she hasn't owned ABM / MQL-to-SQL pipeline; HubSpot/Marteo "
            "vs her Salesforce (transferable); LinkedIn Ads not owned; English is C1 not native. The biggest "
            "practical flag is the remote US-Eastern schedule (~18:00–02:00 Dubai) against a remote_ok:false "
            "profile. CV + letter lead with the genuine full-funnel/paid/SEO/analytics craft and B2B commercial "
            "experience, and state the SaaS-sector, HubSpot and timezone nuances plainly; no fabricated SaaS/ABM "
            "or HubSpot experience, no native-English or 'no sponsorship needed' claim."
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
