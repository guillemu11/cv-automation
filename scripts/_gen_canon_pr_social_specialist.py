"""One-off: generate Paula's CV for Canon Middle East "CME - PR & Social Media
Specialist - Dubai" (Job Id 876, Communications, Specialist, Dubai Internet City,
Hybrid).

Honest-fit rationale. This is a Communications role split in two halves:

  - SOCIAL MEDIA (strong, genuine match): create & execute the social media
    strategy — campaign development, content planning, content calendars,
    performance tracking against KPIs, briefing creative & media agencies,
    producing/managing social assets, governance & consistency across channels.
    Paula genuinely owns brand social end-to-end at DoFreeze (Instagram, TikTok,
    Facebook, Pinterest), runs content calendars, briefs agencies, tracks KPIs
    and built an influencer/UGC programme from zero — a direct, truthful match.

  - PUBLIC RELATIONS (transferable, honest stretch): plan/implement/measure PR
    campaigns tied to business objectives; coordinate with external media &
    social platforms; manage the local approval process for launch content and
    editorial materials with stakeholders across product categories. Paula does
    develop and publish organizational/brand communications, runs the
    stakeholder approval process for NPD launch content/packaging across product
    categories, and coordinates external partners & platforms — transferable.
    The genuine gaps (formal press-release / media-relations tenure, an EMEA PR
    spokesperson network, crisis-communications experience) are NOT invented and
    are logged honestly in the dashboard.

Sector note: Canon is imaging / tech hardware (cameras, printers); Paula's
background is FMCG / Beauty / Fashion / E-commerce — a sector gap. But this is a
comms/social specialist role where transferable communications & social skills
matter more than sector, and "Specialist" is a comfortable level for a current
Brand & Marketing Manager (no seniority stretch).

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — re-angled to the JD's two pillars (PR campaigns + Social Media), with
no invented press/media-relations, spokesperson or crisis-comms experience.

Fills the real CV template, converts to PDF via LibreOffice, registers the job
for the dashboard, and lands the package under output/2026-08-16/.
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

COMPANY = "Canon Middle East"
TITLE = "PR & Social Media Specialist"
DATE_FOLDER = "2026-08-16"
JOB_ID_REF = "876"

JOB_DESCRIPTION = """\
CME - PR & Social Media Specialist - Dubai — Canon Middle East FZ LLC (a subsidiary
of Canon Europe), Job Id 876. Category: Communications. Function: Specialist.
Location: Dubai Internet City, Dubai, UAE (Hybrid).

Develop and publish organizational communications for the general public, customers,
government agencies, communities, suppliers, and media. Create and execute the
company's social media strategy, including campaign development, content planning,
and performance tracking against defined KPIs.

Responsibilities

Public Relations
- Plan, implement, and measure PR campaigns that directly support business objectives,
  ensuring all initiatives are fully integrated and deliver measurable value.
- Lead public relations activities and coordinate with external media and social
  platforms to ensure smooth execution across all stages of exposure.
- Define, develop, execute, and evaluate PR campaigns aligned with immediate business
  needs. Manage the local approval process for press releases, supporting documents,
  and editorial materials with key stakeholders across product categories, ensuring
  accuracy, factual integrity, and timely delivery.
- Liaise with EMEA PR spokespeople as required and support crisis communication
  efforts when necessary.

Social Media
- Develop and guide the creation of best-practice social media campaigns, content and
  guidelines that support the marketing strategy, business goals and local market
  integration.
- Support the execution of social media campaigns by developing and delivering content
  in alignment with campaign toolkits.
- Produce and manage social media assets, including maintaining content calendars,
  briefing creative & media agencies and tracking campaign performance against KPIs.
- Collaborate with the central Social Communications team to ensure governance and
  consistency across all social media channels.

Qualifications — Canon Core Behaviours: Drive for results; Focus on the Customer;
Take ownership and accountability; Act as a team player; Shows courage and conviction;
People orientated; Caring for self and others.
"""

ATS = [
    "PR", "Public Relations", "Social Media", "Social Media Specialist",
    "Communications", "organizational communications", "PR campaigns",
    "press releases", "editorial materials", "supporting documents",
    "external media", "social platforms", "media relations", "crisis communication",
    "EMEA", "spokespeople", "campaign development", "content planning",
    "content calendar", "content calendars", "social media strategy",
    "social media campaigns", "social media assets", "KPIs",
    "performance tracking", "performance measurement", "creative agencies",
    "media agencies", "agency briefing", "governance", "brand consistency",
    "business objectives", "measurable value", "marketing strategy",
    "local market integration", "stakeholder management", "product categories",
    "approval process", "content", "UGC", "influencer marketing", "creators",
    "engagement", "reach", "brand awareness", "Instagram", "TikTok", "Facebook",
    "Meta", "Pinterest", "Meta Business Suite", "generative AI", "storytelling",
    "integrated campaigns", "go-to-market", "GCC", "MENA",
]

CONTENT = {
    "headline": "PR & Social Media Specialist · Brand Communications · Social Media Strategy · Content & Campaign Planning · KPI-Driven",
    "professional_summary": (
        "Communications and social media professional with 4+ years developing brand communications "
        "and owning social media strategy end-to-end across FMCG, Beauty, Fashion and E-Commerce. "
        "Currently lead brand & marketing for DoFreeze across 50+ markets — creating and executing the "
        "social media strategy (campaign development, content planning, content calendars and performance "
        "tracking against KPIs), publishing organizational communications for the public, customers, trade "
        "partners and media, and briefing creative & media agencies while safeguarding governance and "
        "consistency across all channels. Plans, executes and measures integrated PR-style launch campaigns "
        "tied to business objectives, and runs the local approval process for launch content and editorial "
        "materials with stakeholders across product categories. Built an AI-enabled content system "
        "(Claude / GPT) that scales content creation, campaign planning and reporting. Spanish national "
        "based in Dubai on a residence visa; Business Administration graduate (CUNEF, 9.5/10 thesis); "
        "fluent English (C1)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries (GCC, MENA, Europe, Asia)",
            "bullets": [
                "Create and execute the social media strategy end-to-end across brand channels (Instagram, TikTok, Facebook, Pinterest) — campaign development, content planning, content calendars and performance tracking against defined KPIs",
                "Develop and publish organizational and brand communications for the general public, customers, trade partners and media across 50+ markets — aligning messaging to business objectives, the marketing strategy and local market integration",
                "Brief and manage creative & media agencies — producing and managing social media assets and campaign content in alignment with campaign toolkits and brand guidelines, ensuring governance and consistency across all channels",
                "Plan, implement and measure integrated launch and always-on campaigns (organic social, PR-style product launches and paid media on Meta & Google) that support business objectives and deliver measurable value against KPIs",
                "Manage the local approval process for launch content, packaging and editorial materials with key stakeholders across product categories — ensuring accuracy, factual integrity and timely delivery",
                "Built and scaled the influencer & creator programme from zero — sourcing, briefing and managing 25–50 creators per campaign — driving brand awareness, UGC and earned social reach",
                "Built an AI-enabled content system (Claude / GPT) that scales content creation, campaign planning and KPI reporting, cutting manual workload ~40% and accelerating go-to-market",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Created and led social-first brand programmes (Beauty Club, Hot on Social) — content, social activation and community — that boosted brand visibility and engagement and positioned Miravia as a beauty & lifestyle destination",
                "Coordinated with external brands, partners and social platforms to execute integrated campaigns and promotions across all stages of exposure",
                "Managed 42 key accounts and campaign calendars across beauty, fragrances and fashion, growing GMV +30% QoQ through content-led promotions, assortment and pricing",
                "Continuously analysed engagement, conversion, traffic, retention, ROI and ROAS to optimise campaign performance and reporting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Delivered bespoke marketing activations and co-branded campaigns with strategic partners, coordinating across marketing, media and communications to grow visibility and order volume",
                "Led cross-functional teams (marketing, media, logistics, CX) to deliver integrated campaigns seamlessly across stages of execution",
                "Negotiated and closed high-impact commercial deals maximising profitability for platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built campaign and category performance reports (sell-in/sell-out, promotional effectiveness, Nielsen) for the chocolate category, translating data into clear recommendations",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf, supporting go-to-market content and stakeholder sign-off",
            ],
        },
    ],
    "skills_brand": "social media strategy, content strategy & planning, content calendars, campaign development & execution, brand communications & PR campaigns, storytelling, influencer & creator marketing, UGC, community management, agency briefing & management, brand governance & consistency, AI-enabled content",
    "skills_ecommerce": "social media (Instagram, TikTok, Facebook, Pinterest), Meta Business Suite, paid social (Meta Ads), content production, campaign toolkits, EDM, marketing automation, Shopify / e-commerce, go-to-market",
    "skills_commercial": "stakeholder management & content approvals across product categories, cross-functional coordination, external media & partner liaison, key account management, negotiation, pricing",
    "skills_data": "KPI tracking & campaign performance measurement, social analytics, engagement & reach, ROI, ROAS, GMV, reporting & insights, AI-assisted analysis, Power BI, Tableau, Looker, Nielsen",
    "skills_tools": "Generative AI (Claude, ChatGPT), Meta Business Suite, Meta Ads Manager, Canva, Google Ads, Microsoft Office (Expert), Power BI, Tableau, Looker",
}


def make_job() -> Job:
    return Job(
        id="canon-cme-pr-social-media-specialist-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.canon-me.com/about-us/careers/",
        source="company_site",
        description=JOB_DESCRIPTION,
        raw={
            "query": "PR & Social Media Specialist",
            "job_id": JOB_ID_REF,
            "posting_title": "CME - PR & Social Media Specialist - Dubai",
            "category": "Communications",
            "function": "Specialist",
            "site_location": "Dubai Internet City, Dubai, AE (Hybrid)",
            "posting_date": "2026-07-30",
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
        "salary_raw": None,
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 74,
        "ai_tier": "Warm",
        "skills_match": [
            "Owns social media strategy end-to-end — campaign development, content planning, content calendars, KPI performance tracking (direct JD match)",
            "Develops & publishes organizational / brand communications for public, customers, trade & media",
            "Briefs & manages creative & media agencies; produces & manages social media assets",
            "Governance & consistency across all social channels (brand guidelines / toolkits)",
            "Plans, executes & measures integrated PR-style launch campaigns tied to business objectives",
            "Runs local approval process for launch content & editorial materials with stakeholders across product categories",
            "Influencer / creator & UGC programme built from zero (brand awareness & earned reach)",
            "AI-enabled content system (Claude/GPT) that scales content, campaign planning & reporting",
            "Specialist level is comfortable for a current Brand & Marketing Manager — no seniority stretch",
            "Spanish national already in Dubai (residence visa) — hybrid Dubai Internet City, no relocation",
            "Fluent English (C1); Business Administration graduate (CUNEF, 9.5/10 thesis)",
        ],
        "missing_skills": [
            "Formal press-release / media-relations tenure — genuine gap; experience is brand & organizational comms + social, not a dedicated PR/newsroom desk",
            "EMEA PR spokesperson network — not held; adjacent via external partner/platform liaison",
            "Crisis-communication experience — not held; the JD lists it as 'support when necessary'",
            "Imaging / tech-hardware (cameras, printers) sector — background is FMCG / Beauty / Fashion / E-commerce",
        ],
        "sector_fit": "weak (imaging / tech hardware) — but role SHAPE (PR + social communications) is a strong transferable fit",
        "seniority_fit": "strong (Specialist level; current Brand & Marketing Manager — lateral, no stretch up)",
        "red_flags": [
            "PR half leans on formal press-release / media-relations / crisis-comms — Paula's PR is transferable (brand & organizational comms, stakeholder approvals, launch campaigns), not newsroom PR; positioned honestly, not over-claimed",
            "Sector is imaging / tech hardware (Canon) — no direct experience; transferable comms & social skills carry the fit",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit on the Social Media half and a transferable, honest fit on the PR half. Paula "
            "genuinely creates and executes social media strategy end-to-end — campaign development, "
            "content planning, content calendars, agency briefing, social assets and KPI performance "
            "tracking — plus develops and publishes organizational/brand communications and runs the "
            "local stakeholder approval process for launch content across product categories, which maps "
            "directly to the JD's press-release/editorial approval line. The genuine gaps are formal "
            "press-release/media-relations tenure, an EMEA PR spokesperson network and crisis-comms — none "
            "invented; her PR is brand & organizational communications plus integrated launch campaigns, "
            "not a newsroom desk. Sector is imaging/tech hardware (Canon) vs her FMCG/Beauty/Fashion/"
            "E-commerce background, but 'Specialist' is a comfortable level for a current Brand & Marketing "
            "Manager and she is already in Dubai on a residence visa for the hybrid Dubai Internet City "
            "role. Positioned truthfully on transferable communications + social strengths; PR-desk and "
            "sector gaps logged honestly."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (no Word automation prompts).

    Falls back to cv._to_pdf (docx2pdf/Word) if soffice is unavailable or fails.
    Removes the intermediate DOCX on success, mirroring cv._to_pdf.
    """
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

    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
