"""One-off: generate Paula's CV + cover letter for Jobgether
"Paid Media Specialist (Meta)" — remote, UAE-based, EST schedule.

Why this is a solid, honest fit:
  - Meta Ads is genuinely part of Paula's current day-to-day: at DoFreeze she
    plans, launches and optimises Facebook & Instagram campaigns end-to-end —
    audience research and targeting (segmentation, retargeting, lookalike
    audiences), creative A/B testing, budget allocation and ROI/ROAS reporting —
    running Google Ads and EDM alongside, and closing the loop into a Shopify
    store she optimises for conversion (CRO) and AOV.
  - The role's spine (Meta Ads Manager / Business Suite, audience strategy,
    A/B testing, budget & spend management, performance reporting, data-driven
    optimisation, fluent English, WFH setup) maps directly onto her explicit
    track. Analytical + ROAS discipline reinforced by 42 accounts / +30% GMV QoQ
    at Alibaba's Miravia.

Honest positioning (NO fabrication):
  - Paula's Meta work sits INSIDE a broader Brand & Marketing / e-commerce
    remit, not a dedicated multi-year "paid media specialist" title. Framed
    truthfully — she owns the hands-on campaign/audience/budget/reporting craft,
    but this is one part of a wider role, stated plainly in the letter.
  - NO Meta Blueprint claim (a "plus"; not held). NO Google Analytics or tools
    absent from profile.yaml.
  - Per standing rule, NO "no sponsorship needed" claim. It's a remote role, so
    visa is not surfaced; the letter states remote-ready home setup only.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-18/.
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

COMPANY = "Jobgether"
TITLE = "Paid Media Specialist (Meta)"
DATE_FOLDER = "2026-08-18"

# AI-matched via Jobgether on behalf of an unnamed partner company; no hiring
# manager named — letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Paid Media Specialist (Meta) — Jobgether (on behalf of a partner company),
United Arab Emirates. Remote, full-time (40h/week), Mon–Fri aligned to Eastern
Standard Time (EST). Permanent work-from-home.

This role is ideal for a performance-focused digital marketer who knows how to
turn Meta advertising into measurable business results. You will own campaigns
across Facebook, Instagram and related Meta platforms, from audience research and
targeting through execution, optimisation and reporting. Your work directly
influences campaign efficiency, customer acquisition and return on advertising
investment.

Accountabilities:
- Develop, launch, manage and optimise Meta advertising campaigns aligned with
  business and marketing objectives.
- Conduct audience research and build effective targeting strategies, including
  segmentation, retargeting and lookalike audiences.
- Collaborate with design and content teams to develop compelling ad creatives,
  messaging and visual assets.
- Monitor campaign performance and analyse key metrics to identify opportunities
  for optimisation and improved return on investment.
- Manage advertising budgets and allocate spend effectively across campaigns,
  audiences, placements and creative variations.
- Design and execute A/B tests across messaging, creative, audience targeting,
  placements and other campaign variables.
- Produce regular performance reports that clearly communicate campaign results,
  trends, insights and recommendations to stakeholders.
- Stay informed about Meta advertising products, platform updates, industry
  trends and emerging paid media best practices.

Requirements:
- 2–3+ years of hands-on experience managing paid advertising campaigns on Meta
  platforms, preferably in a performance marketing environment.
- Strong proficiency with Meta Ads Manager, Meta Business Suite, and relevant
  analytics and reporting tools.
- Demonstrated experience with audience segmentation, retargeting, lookalike
  audiences and campaign optimisation.
- Strong analytical skills and the ability to interpret campaign data, identify
  trends and make informed performance decisions.
- Experience managing advertising budgets with a focus on efficient resource
  allocation and measurable ROI.
- Strong written and verbal communication skills.
- Ability to collaborate with designers, content specialists and other marketing
  stakeholders.
- Comfortable in a fast-paced environment, managing multiple priorities.
- Familiarity with Google Ads or TikTok Ads is an advantage.
- Meta advertising certification (Meta Blueprint) is a plus.
- Reliable home-working setup (dual-monitor computer, 8GB+ RAM, 25Mbps+, 1080p
  camera).
"""

ATS = [
    "Paid Media Specialist", "Meta", "Meta Ads", "Meta Ads Manager",
    "Meta Business Suite", "Facebook", "Instagram", "Facebook Ads",
    "Instagram Ads", "paid media", "paid social", "performance marketing",
    "digital marketer", "campaign optimisation", "campaign optimization",
    "audience research", "targeting", "segmentation", "retargeting",
    "lookalike audiences", "ad creatives", "creative", "messaging",
    "A/B testing", "A/B tests", "campaign performance", "key metrics",
    "ROI", "return on investment", "return on ad spend", "ROAS",
    "advertising budgets", "budget", "spend allocation", "placements",
    "performance reports", "reporting", "stakeholders", "data-driven",
    "analytical", "customer acquisition", "Google Ads", "TikTok Ads",
    "Meta Blueprint", "optimisation", "continuous improvement",
    "fast-paced", "remote", "work-from-home", "fluent English",
]

CV_CONTENT = {
    "headline": (
        "Performance Marketing · Meta Ads (Facebook & Instagram) · Paid Social & ROAS · "
        "E-Commerce Growth · Google Ads"
    ),
    "professional_summary": (
        "Performance-focused digital marketer with 4+ years across E-Commerce, Beauty and FMCG who turns "
        "Meta advertising into measurable business results. At DoFreeze I own paid media on Meta Ads "
        "(Facebook & Instagram) end-to-end — audience research and targeting (segmentation, retargeting, "
        "lookalike audiences), creative A/B testing, budget and spend allocation, and ROI/ROAS reporting — "
        "running Google Ads and EDM alongside, and closing the loop into a Shopify store I optimise for "
        "conversion rate (CRO) and average order value. Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, "
        "conversion and retention across 42 accounts to optimise channel performance (+30% GMV QoQ). "
        "Analytical and comfortable with data and fast test-and-learn cycles, and an early adopter of "
        "generative AI (Claude/GPT) to scale campaign planning, creative and reporting. Business "
        "Administration graduate, fluent English, with a fully equipped dual-monitor home-working setup."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Plan, launch, manage and optimise Meta advertising campaigns (Facebook & Instagram) end-to-end — from audience research and targeting through execution, optimisation and reporting — aligned to acquisition and return-on-ad-spend objectives",
                "Build targeting strategies with audience segmentation, retargeting and lookalike audiences, and run continuous A/B tests across creative, messaging, placements and audiences to improve campaign efficiency and lower cost per acquisition",
                "Manage advertising budgets across campaigns, audiences, placements and creative variations — allocating spend to the best-performing combinations and monitoring key metrics (CTR, CPA, ROAS) to maximise return on investment",
                "Collaborate with design and content teams to develop compelling ad creatives, messaging and visual assets for paid social, and run Google Ads and EDM alongside Meta for a full-funnel paid + owned mix",
                "Produce regular performance reports communicating results, trends, insights and recommendations to stakeholders, and built AI-powered automation (Claude/GPT) that scales campaign planning, creative and reporting",
                "Own the brand's Shopify store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate (CRO) and average order value — closing the loop from paid click to purchase",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Continuously analysed ROI, ROAS, conversion, traffic and retention across 42 accounts to optimise channel performance and forecasting accuracy — sharpening data-led decisions on spend and promotion",
                "Created and led the Beauty Club and Hot on Social projects, boosting brand visibility, engagement and customer loyalty across social channels",
                "Managed 42 key accounts across beauty, fragrances and fashion, achieving +30% GMV growth QoQ through pricing strategy, assortment optimisation and targeted promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO and executing performance-driven commercial plans aligned to P&L targets",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew strategic accounts through data-led joint planning and bespoke marketing activations, tracking performance to optimise campaigns and order volume",
                "Supported building Glovo's Retail vertical — onboarding fashion and lifestyle brands with tailored launch campaigns and promotions",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, building performance reports that informed spend and commercial planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) with data-driven analysis in advanced Excel, turning category data into actionable recommendations",
            ],
        },
    ],
    "skills_ecommerce": (
        "Meta Ads Manager, Meta Business Suite, Facebook & Instagram Ads, paid social, Google Ads, TikTok Ads, "
        "audience segmentation / retargeting / lookalike audiences, A/B testing, Shopify, conversion rate "
        "optimisation (CRO), EDM, marketing automation"
    ),
    "skills_data": (
        "ROI & ROAS optimisation, campaign performance & data analysis, advertising budget & spend management, "
        "KPI tracking (CTR, CPA, CPM, ROAS), A/B test analysis, forecasting, Meta Ads reporting, Power BI, "
        "Tableau, Looker"
    ),
    "skills_brand": (
        "paid media strategy, performance marketing, full-funnel campaigns, audience & creative testing, "
        "go-to-market, influencer & UGC, omnichannel campaigns, generative-AI content & campaign automation"
    ),
    "skills_commercial": (
        "customer acquisition, growth, pricing & promotion strategy, stakeholder communication, "
        "key account management, negotiation"
    ),
    "skills_tools": (
        "Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, Generative AI (Claude, ChatGPT), "
        "Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Paid media is where marketing has to prove itself in numbers, which is exactly why the Paid Media "
        "Specialist (Meta) role caught my attention. Meta Ads is something I run hands-on every week: at "
        "DoFreeze I own our Facebook and Instagram campaigns end-to-end — from audience research and targeting "
        "through creative testing, budget allocation and ROAS reporting — so turning Meta advertising into "
        "measurable business results is already my day-to-day."
    ),
    "body_paragraph_1": (
        "In my current role as Brand & Marketing Manager at DoFreeze, I plan, launch and optimise Meta "
        "campaigns built on segmentation, retargeting and lookalike audiences, running continuous A/B tests "
        "across creative, messaging and placements to lower cost per acquisition and lift ROAS. I manage the "
        "ad budget across campaigns and placements, produce the performance reports that decide where spend "
        "goes next, and run Google Ads and EDM alongside Meta. Because I also own our Shopify store and its "
        "conversion rate (CRO), I optimise the full journey from paid click to purchase — not just the ad. "
        "Earlier, at Alibaba's Miravia, I analysed ROI, ROAS, conversion and retention across 42 accounts to "
        "grow GMV +30% QoQ, so data-led decision-making is second nature."
    ),
    "body_paragraph_2": (
        "A few things I'd bring beyond the checklist: I'm an early adopter of generative AI (Claude/GPT) and "
        "have built automation that scales campaign planning, creative and reporting — genuinely useful in a "
        "fast-paced, test-and-learn environment. I collaborate naturally with design and content teams on ad "
        "creative, I'm comfortable owning budgets against ROI, and I'm fully set up to work remotely with a "
        "dedicated dual-monitor home office. I'll be straightforward: my Meta work sits inside a broader brand "
        "and e-commerce remit rather than a pure paid-media title — but the hands-on campaign, audience, "
        "budget and reporting craft this role runs on is exactly what I do every week, and I ramp fast."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd build, test and scale Meta campaigns for your partner's "
        "business — from audience strategy through creative and budget optimisation to the reporting that "
        "keeps ROAS climbing. I'm fluent in English, available to start quickly, and set up for remote work. "
        "Thank you for considering my application — I'd be glad to walk through how I'd approach a first 90 "
        "days of campaigns."
    ),
}


def make_job() -> Job:
    return Job(
        id="jobgether-paid-media-specialist-meta-2026-08",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (Remote)",
        url="https://www.linkedin.com/jobs/view/paid-media-specialist-meta-jobgether",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Paid Media Specialist Meta remote",
             "function": "Marketing / Performance",
             "workplace": "Remote (WFH, EST schedule)",
             "note": "Listed by Jobgether (AI-matching intermediary) on behalf of an unnamed partner company; LinkedIn Easy Apply"},
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
        "ai_score": 74,
        "ai_tier": "Warm",
        "skills_match": [
            "Hands-on Meta Ads (Facebook & Instagram) — plan/launch/optimise end-to-end at DoFreeze",
            "Meta Ads Manager & Meta Business Suite",
            "Audience segmentation, retargeting & lookalike audiences",
            "A/B testing across creative, messaging, placements & audiences",
            "Advertising budget & spend allocation",
            "ROI / ROAS optimisation & performance reporting to stakeholders",
            "Google Ads (and TikTok) alongside Meta",
            "Shopify + conversion rate optimisation (CRO) — full paid-to-purchase loop",
            "Collaboration with design & content teams on ad creative",
            "Generative-AI automation for campaign planning, creative & reporting",
            "Strong analytical / data-driven decision-making (42 accounts, +30% GMV QoQ)",
            "Fluent English; equipped dual-monitor home-working setup",
        ],
        "missing_skills": [
            "Dedicated 2–3 yr paid-media-specialist TITLE (her Meta Ads is hands-on but within a broader brand/e-commerce role)",
            "Meta Blueprint certification (listed as 'a plus'; not held)",
        ],
        "sector_fit": "strong (E-Commerce / performance marketing — direct)",
        "seniority_fit": "above-band on breadth (Brand & Marketing Manager vs a specialist 2–3 yr role)",
        "red_flags": [
            "Remote role on an EST schedule (Mon–Fri, 8h/day aligned to US Eastern) — from Dubai that lands in the evening/late-night hours",
            "Listed via Jobgether, an AI-matching intermediary for an unnamed partner company; 'competitive base salary' is unspecified and may fall below Paula's AED 20k/month floor for a WFH specialist role",
            "Specialist level (2–3 yrs) sits below Paula's current Manager seniority; her Meta Ads work is one part of a wider remit, not a dedicated paid-media title — positioned truthfully",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Solid, honest fit on the skills axis. The role is a Meta-focused paid-media specialist: plan/"
            "launch/optimise Facebook & Instagram campaigns, audience segmentation/retargeting/lookalikes, "
            "A/B testing, budget & spend management, ROI/ROAS reporting and data-driven optimisation — all of "
            "which Paula does hands-on today at DoFreeze (plus Google Ads, EDM and a Shopify/CRO loop), "
            "reinforced by ROAS/ROI analysis across 42 accounts and +30% GMV QoQ at Alibaba's Miravia. Honest "
            "gaps: her Meta work lives inside a broader Brand & Marketing / e-commerce remit rather than a "
            "dedicated multi-year paid-media title, and she doesn't hold Meta Blueprint (a 'plus'). Practical "
            "caveats worth weighing before applying: it's a remote WFH role on an EST schedule (tough hours "
            "from Dubai), routed through Jobgether's AI matching for an unnamed partner, with an unspecified "
            "'competitive base' that may sit below her salary floor and a specialist level below her current "
            "seniority. CV + letter lead with the genuine Meta/performance craft and state the title nuance "
            "plainly; no Blueprint or fabricated-tool claims."
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
