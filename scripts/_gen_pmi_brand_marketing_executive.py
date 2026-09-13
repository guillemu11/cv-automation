"""One-off: generate Paula's CV (+ cover letter) for Philip Morris International
(PMI) — "Brand Marketing Executive" (Brand Executive, Brand Marketing team),
Dubai. Reports to Manager Brand Marketing. Ref 31754.

Why the CRAFT fit is strong:
  - This is a BRAND EXECUTION role: campaign execution & deployment across CRM,
    website, social and offline; translate brand strategy into creative briefs;
    brief & coordinate external agencies; content development & localisation
    (digital + print/POS); project & timeline management with budget tracking;
    QA / brand compliance. That is exactly Paula's brand-manager craft.
  - She runs omnichannel campaigns today (Meta & Google Ads, EDM/CRM, Shopify
    website, social, plus modern-trade/POS retail execution) at DoFreeze; briefs
    and manages 25-50 creators per campaign; leads NPD end-to-end (briefs,
    packaging/print, GTM, timelines, A&P budgets); and localises brand assets
    across 50+ markets — a direct match for content localisation + multi-channel
    toolkits + project management.
  - "2-3 yrs in multinational FMCG or creative agencies": anchored by Mondelez
    (global FMCG) + DoFreeze (FMCG) + Miravia (Alibaba). She has ~4 yrs.
  - HARD requirement MET: "currently based in UAE" — Paula is in Dubai.
  - Digital/CRM/paid media "as a plus" — a genuine strength, not just a plus.

HONEST gaps (NOT fabricated):
  - **ARABIC — the decisive one.** JD requires "Fluent in English AND Arabic,
    strong reading/writing/speaking in both." Paula is Spanish (native) + English
    (C1), NOT an Arabic speaker. NEVER claimed. CV languages stay ES/EN only.
    This is very likely the hard filter — flagged to Paula/Guille. Documents do
    not advertise the gap (don't fabricate the positive), but nothing implies
    Arabic anywhere.
  - Agency management: she is more creator/influencer + in-house led than classic
    external-agency management. Transferable (briefing, coordinating, reviewing
    outputs); framed honestly, not overstated.
  - Seniority: "Executive" (2-3 yrs) sits a touch below her current Brand &
    Marketing Manager level — framed as genuine interest in PMI's transformation
    and a global brand, not a step-down. (Flagged separately.)
  - Sector: tobacco/nicotine (smoke-free transition). A personal call for Paula —
    neutral flag, not a documents issue.
  - Per standing rule, NO "own visa / no sponsorship" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-27/.
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

COMPANY = "Philip Morris International"
TITLE = "Brand Marketing Executive"
DATE_FOLDER = "2026-08-27"

CONTACT = None  # Reports to Manager Brand Marketing; no name in posting — "Hiring Manager".

JOB_DESCRIPTION = """\
Brand Marketing Executive (Brand Executive) — Philip Morris International (PMMS,
Middle East), Dubai. Part of the Brand Marketing team, reporting to the Manager
Brand Marketing. PMI is transforming toward a smoke-free future (IQOS, ZYN).

The Brand Executive supports the execution of brand initiatives, ensuring
high-quality implementation across digital and offline channels — translating
brand strategies into effective campaigns through close coordination with
creative agencies, oversight of content creation, and consistency across all
brand touchpoints.

Campaign Execution & Deployment: support rollout of brand campaigns across CRM,
website, social media and offline channels; translate campaign strategies into
actionable creative briefs and execution plans; ensure consistency and quality
across brand touchpoints.

Agency & Stakeholder Management: brief and coordinate external agencies on
campaign execution; manage day-to-day communications and timely delivery of
creatives; review final outputs and provide feedback before deployment.

Content Management: support development and localisation of brand assets across
digital and print; assist with email creation, website updates and social media
content deployment; organise and maintain campaign toolkits for multi-channel
execution.

Project & Process Management: manage multiple tasks and timelines; prioritise
workload to meet deadlines; support basic budget tracking and project pipeline
visibility.

Quality Control & Optimization: conduct pre-launch testing and QA checks; ensure
accuracy, attention to detail and full brand compliance; identify opportunities
to improve execution processes.

Who we're looking for: 2-3 years in marketing, branding or related in
multinational FMCGs or creative agencies; must be currently based in UAE; good
understanding of brand execution, campaign deployment and marketing fundamentals,
with exposure to digital marketing, CRM and paid media a plus; familiarity with
digital and offline materials (print, POS, multi-channel brand assets); strong
project management and organizational skills; fluent in English and Arabic
(strong reading, writing and speaking in both); highly organized, detail-oriented,
quality-driven with strong ownership; able to manage multiple priorities under
pressure. Ref 31754.
"""

ATS = [
    "brand marketing", "brand execution", "brand executive", "campaign execution",
    "campaign deployment", "brand initiatives", "brand touchpoints", "brand consistency",
    "brand compliance", "creative briefs", "creative briefing", "agency management",
    "agency coordination", "stakeholder management", "content management",
    "localisation", "brand assets", "email", "CRM", "website", "social media",
    "social media content", "offline", "print", "POS", "multi-channel",
    "campaign toolkits", "project management", "timelines", "prioritisation",
    "budget tracking", "project pipeline", "quality control", "QA",
    "pre-launch testing", "attention to detail", "digital marketing", "paid media",
    "Meta Ads", "Google Ads", "go-to-market", "NPD", "FMCG", "multinational",
    "Dubai", "UAE", "ownership", "PowerPoint", "Excel", "generative AI",
]

CV_CONTENT = {
    "headline": (
        "Brand & Marketing Executive · Omnichannel Campaign Execution & Deployment (CRM · Web · Social · Offline) · "
        "Creative Briefing & Agency Coordination · Content & Multi-Market Localisation · Multinational FMCG · Dubai-based"
    ),
    "professional_summary": (
        "Dubai-based brand & marketing professional (4+ yrs, multinational FMCG) who turns brand strategy into "
        "shipped campaigns across CRM, website, social and offline — creative briefs, agency coordination, "
        "multi-market content localisation and end-to-end project & QA ownership. AI-first way of working (Claude/GPT)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-brand FMCG group | Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Execute and deploy brand campaigns across CRM/email, website (Shopify), social and offline/trade — turning brand strategy into creative briefs and consistent, on-brand touchpoints",
                "Brief and coordinate external creatives/agencies and 25–50 creators per campaign, manage timelines and review outputs, and localise brand assets across 50+ markets",
                "Run NPD launches as projects (timelines, A&P budgets, QA & brand compliance); AI-first (Claude/GPT) briefs, content and reporting, cutting ~40% manual work",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees",
            "bullets": [
                "Led brand-building projects (Beauty Club, Hot on Social) and owned the Flash Sales channel — campaign deployment, promotions and merchandising across touchpoints, reporting to the CEO",
                "Managed 42 brand accounts (+30% GMV QoQ) and onboarded 30+ new brands in two months with well-briefed activations",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG multinational | €36B revenue | 90K+ employees",
            "bullets": [
                "Multinational-FMCG grounding — supported the chocolate category and NPD launches (Milka Spread, Mini Suchard) with analysis and reporting in Excel/PowerPoint",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue",
            "bullets": [
                "Delivered bespoke partner activations and campaigns, coordinating cross-functionally across marketing, ops and logistics under tight deadlines",
            ],
        },
    ],
    "skills_brand": (
        "brand execution, campaign deployment, creative briefing, brand consistency & compliance, "
        "omnichannel campaigns, go-to-market, NPD"
    ),
    "skills_ecommerce": (
        "CRM & email (EDM), website (Shopify), social content, paid media (Meta & Google Ads), "
        "digital & print/POS localisation, campaign toolkits"
    ),
    "skills_commercial": (
        "agency & partner coordination, project & timeline management, budget tracking, "
        "offline/trade execution, cross-functional collaboration"
    ),
    "skills_data": (
        "campaign tracking & KPIs, pre-launch QA, ROI/ROAS, attention to detail, Power BI"
    ),
    "skills_tools": (
        "MS Office — Expert (PowerPoint, Excel), Meta Ads, Google Ads, Shopify, Canva, "
        "Generative AI (Claude, ChatGPT)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "PMI's smoke-free transformation is one of the boldest brand journeys in consumer goods, and it runs on "
        "people who can take brand strategy and actually ship it — cleanly, on-brand, across every channel. That's "
        "the work I do. I'm a brand and marketing professional based in Dubai who executes and deploys campaigns "
        "end-to-end across CRM, website, social and offline, and I'd bring an FMCG-trained, detail-obsessed, "
        "ownership-led approach to the Brand Marketing team."
    ),
    "body_paragraph_1": (
        "The day-to-day maps directly onto what I already do at DoFreeze. I translate brand strategy into creative "
        "briefs and execution plans; deploy campaigns across CRM/email, Shopify website, social and modern-trade/POS "
        "channels; brief and coordinate external creatives and agencies, managing timelines and reviewing outputs "
        "before launch; and support the development and localisation of brand assets (digital and print) across "
        "50+ markets, keeping multi-channel toolkits organised. I run launches as projects — juggling multiple "
        "timelines, budgets and pipelines under pressure — and I own quality control, running pre-launch QA and "
        "brand-compliance checks so nothing ships off-brand. My Mondelez grounding gives me the multinational-FMCG "
        "fundamentals, and my paid-media, CRM and AI-first toolkit (a Claude/GPT system that speeds up briefs, "
        "content and reporting) helps me move fast without dropping quality."
    ),
    "body_paragraph_2": (
        "Beyond the checklist, what I bring is genuine multi-market brand execution — I keep dozens of markets "
        "consistent and on-brand at once — plus hands-on digital, CRM and paid media that go past the 'nice to "
        "have', and a rare AI-first way of working that cuts the manual overhead in briefs, content and reporting. "
        "I'm highly organized, detail-oriented and quality-driven, with the ownership to run several campaigns in "
        "parallel and still sweat the details."
    ),
    "closing_paragraph": (
        "I'd be genuinely excited to help the Brand Marketing team execute PMI's brand initiatives to a high "
        "standard, and I can walk through campaign, content and launch case studies from my current work. I'm "
        "already based in Dubai and ready to start fast. Thank you for your consideration — I look forward to "
        "hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="pmi-brand-marketing-executive-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://www.pmi.com/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Brand Marketing Executive brand execution campaign deployment FMCG",
             "function": "Brand marketing execution (Brand Executive — campaign deployment, agency coordination, content)",
             "sector": "Tobacco / nicotine (PMI — smoke-free transition: IQOS, ZYN)",
             "note": "STRONG craft fit (brand execution / campaign deployment / creative briefs / agency coordination "
                     "/ content localisation / project mgmt / QA in a multinational FMCG, Dubai-based — all genuine "
                     "Paula strengths) BUT a HARD requirement she does NOT meet: 'Fluent in English AND Arabic'. "
                     "Paula is Spanish native + English C1, no Arabic — NEVER fabricated; CV languages stay ES/EN. "
                     "This is very likely the decisive filter. Also: agency mgmt is more creator/in-house-led for her "
                     "(transferable); 'Executive'/2-3 yrs sits a touch below her Manager level; sector is tobacco "
                     "(personal call for Paula). No 'own visa / no sponsorship' claim."},
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
        "ai_score": 62,
        "ai_tier": "Warm",
        "skills_match": [
            "Campaign execution & deployment across CRM/email, website (Shopify), social and offline — exactly her DoFreeze brand-execution work; translates brand strategy into briefs and execution plans",
            "Creative briefing & agency/external-partner coordination — briefs and manages creatives/agencies + 25-50 creators per campaign, manages timelines, reviews outputs before launch",
            "Content management & multi-market localisation — brand assets digital + print (packaging/POS/social/EDM), campaign toolkits across 50+ markets",
            "Project & process management — runs NPD launches with timelines, A&P budgets and pipeline visibility; prioritises under pressure",
            "Quality control & brand compliance — pre-launch QA, accuracy, attention to detail, brand consistency across touchpoints",
            "Multinational FMCG grounding (Mondelez) + FMCG now (DoFreeze); digital/CRM/paid media (Meta & Google Ads) well beyond 'a plus'; AI-first working",
            "HARD requirement MET: currently based in UAE (Dubai); ~4 yrs vs 2-3 asked; Business Administration degree",
        ],
        "missing_skills": [
            "ARABIC — HARD requirement ('Fluent in English AND Arabic, strong reading/writing/speaking'). Paula is Spanish native + English C1, NOT an Arabic speaker. NEVER fabricated. Very likely the decisive filter for this role",
            "Agency management is more creator/influencer + in-house-led for her than classic external-agency management (transferable: briefing, coordinating, reviewing)",
            "'Executive'/2-3 yrs sits a touch below her current Brand & Marketing Manager level (slight over-qualification)",
        ],
        "sector_fit": "good on craft (brand execution in multinational FMCG) — but sector is tobacco/nicotine (personal call for Paula)",
        "seniority_fit": "slightly over — 'Executive' (2-3 yrs) vs her Brand & Marketing Manager level (~4 yrs); framed as genuine interest in PMI's transformation",
        "red_flags": [
            "ARABIC fluency is an explicit HARD requirement Paula does not meet — realistically the decisive filter. Documents do not fabricate it; decide whether to apply anyway, add an Arabic-learning line, or skip.",
            "Sector is tobacco/nicotine (smoke-free transition) — a personal/ethical consideration for Paula, not a documents issue.",
            "'Executive' title sits below her Manager level — confirm scope/band/comp if it advances.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "The craft fit is genuinely strong: this is a brand-execution role — campaign deployment across "
            "CRM/website/social/offline, translating strategy into creative briefs, briefing and coordinating "
            "external agencies, content development & localisation (digital + print/POS), project/timeline/budget "
            "management, and QA/brand compliance — inside a multinational FMCG, for a candidate who must be "
            "UAE-based. That is squarely Paula's brand-manager work (DoFreeze omnichannel execution + creator/"
            "agency briefing + 50+ market localisation + NPD project management), anchored by multinational-FMCG "
            "experience (Mondelez) and strong digital/CRM/paid-media chops. The decisive problem is a HARD "
            "requirement she does not meet: fluency in English AND Arabic (she is Spanish native + English C1, no "
            "Arabic) — never fabricated; CV languages stay ES/EN. That likely filters her out regardless of craft. "
            "Secondary notes: agency management is more creator/in-house-led for her; the 'Executive' title sits a "
            "touch below her Manager level; and the sector is tobacco/nicotine (a personal call for Paula). Package "
            "prepared honestly at her request and reusable; recommend deciding on the Arabic gap before applying. "
            "No 'own visa / no sponsorship' claim."
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
