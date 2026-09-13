"""One-off: generate Paula's CV + cover letter for Binance
"Creator Partnerships Manager, Binance Square" (Dubai, UAE — remote).

Why the SKILL fit is strong but it's still a domain STRETCH:
  - The core of the role is Paula's single strongest, most genuine skill: recruit,
    onboard, engage, RETAIN and manage a PORTFOLIO of creators, plus community
    growth programmes and creator marketing initiatives. She built DoFreeze's
    influencer/creator programme from zero — sourcing, briefing, negotiating and
    managing 25-50 creators per campaign (incl. paid collabs) — and led community
    projects (Hot on Social, Beauty Club) at Miravia. That maps almost 1:1 onto the
    JD's responsibilities.
  - Requirement bar is only "minimum 3 years in partnerships, affiliate management,
    or cross-channel marketing" — she has 5+.
  - SPANISH is explicitly listed as an advantage ("Proficiency in Spanish,
    Vietnamese and Ukrainian would be an advantage") — she is a native Spanish
    speaker. Genuine plus, surfaced.
  - Remote, global, self-motivated, analytical, trend-aware — all real.

The honest GAP (not fabricated):
  - CRYPTO / Web3 domain. The JD prefers "a strong understanding of the crypto
    industry" and requires "demonstrated involvement or experience in the crypto
    creator community or a resourceful network within the crypto industry." Paula
    does NOT have crypto tenure or a crypto creator network. We DO NOT invent any.
    Positioning leans on transferable creator-partnerships expertise + fast-ramp,
    tech-forward learner mindset + genuine interest in the Web3 creator economy —
    and the cover letter names the gap plainly. If Paula turns out to have real
    crypto involvement (personal investing, following/knowing crypto creators, a
    network), that can be added truthfully later.
  - Visa: remote role; already in Dubai on a UAE residence visa. Per standing rule,
    NO "no sponsorship needed" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-30/.
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

COMPANY = "Binance"
TITLE = "Creator Partnerships Manager, Binance Square"
DATE_FOLDER = "2026-08-30"

# Recruiter-promoted LinkedIn Easy Apply; no named hiring manager — letter stays
# addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Creator Partnerships Manager, Binance Square — Binance, Dubai, UAE (Remote,
full-time). Binance is the world's largest crypto exchange; Binance Square is its
one-stop social platform for Web3 & crypto, bridging content creators and their
followers.

Responsibilities:
- Identify and recruit global crypto creators, overseeing the onboarding process.
- Develop and implement creator engagement and retention strategies, acting as a
  liaison between creators and internal teams.
- Manage a portfolio of high-impact global crypto creators, tracking community
  growth metrics for engagement, retention and satisfaction.
- Build community growth programs and execute creator marketing initiatives to
  enhance brand awareness and community interaction through collaborations with
  creators.
- Collaborate with creators to facilitate AMA sessions, interviews and
  community-driven initiatives.
- Stay updated with the latest trends, news and developments in the crypto
  industry, identifying emerging crypto creators and tracking competitor activities.

Requirements:
- Minimum of 3 years of experience in partnerships, affiliate management or
  cross-channel marketing, preferably with a strong understanding of the crypto
  industry.
- Demonstrated involvement or experience in the crypto creator community or a
  resourceful network within the crypto industry.
- Strong interpersonal skills to build relationships with multiple stakeholders.
- Fluency in English is required to coordinate with overseas partners and
  stakeholders. Proficiency in Spanish, Vietnamese and Ukrainian would be an
  advantage.
- Strong analytical skills to interpret data and derive effective strategies.
- Ambitious, goal-oriented and self-motivated; able to work independently and
  collaborate with remote global team members.
- Up-to-date knowledge of the latest trends and best practices in relevant
  marketing fields, particularly within the crypto space.
"""

ATS = [
    "Creator Partnerships", "creator partnerships manager", "partnerships",
    "affiliate management", "cross-channel marketing", "creator recruitment",
    "creator onboarding", "creator engagement", "creator retention",
    "portfolio of creators", "influencer", "influencer marketing", "KOL",
    "community growth", "community programs", "community management",
    "creator marketing", "brand awareness", "collaborations", "UGC", "AMA",
    "interviews", "community-driven initiatives", "engagement", "retention",
    "satisfaction", "community growth metrics", "stakeholder management",
    "interpersonal skills", "relationship building", "analytical", "data-driven",
    "trends", "emerging creators", "competitor tracking", "remote", "global",
    "self-motivated", "goal-oriented", "English", "Spanish", "Web3", "crypto",
    "creator economy", "social platform", "content creators", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Creator & Influencer Partnerships · Community Growth, Engagement & Retention · "
        "Cross-Channel Marketing · Global Creator Programs (Remote) · Spanish-Native / English C1"
    ),
    "professional_summary": (
        "Creator-partnerships and community-growth marketer with 5+ years across consumer internet, "
        "marketplaces and FMCG. My core strength is exactly this role: I built a creator/influencer partnership "
        "programme from zero — identifying, recruiting, onboarding, negotiating with and retaining a portfolio "
        "of 25–50 creators per campaign (including paid collaborations) — and led community programmes that grew "
        "engagement, brand awareness and loyalty. I manage relationships with multiple stakeholders, track "
        "engagement/retention metrics, and turn data into creator and channel strategy. Native Spanish speaker "
        "and English C1 (a listed advantage for coordinating global creators), ambitious and self-motivated in "
        "remote, globally distributed teams, and a fast, tech-forward learner (early adopter of generative AI "
        "and new platforms) genuinely excited to bring proven creator expertise into the Web3 and crypto "
        "creator economy. Already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Built and run a creator/influencer partnership programme from zero — identifying and recruiting global creators, owning onboarding, briefing, negotiation and ongoing relationship management for a portfolio of 25–50 creators per campaign, including paid collaborations",
                "Develop creator engagement and retention strategies as the liaison between creators and internal teams, tracking reach, engagement and content-performance metrics to grow the community",
                "Execute creator marketing initiatives and community/UGC programmes that build brand awareness and community interaction through creator collaborations — co-created content, campaign activations, sampling and seeding",
                "Stay on top of platform and content trends and competitor activity to spot and onboard emerging creators, and coordinate creator-led campaigns and social activations across channels",
                "Run cross-channel marketing (social, paid on Meta/Google, CRM/EDM, e-commerce), using data to optimise engagement and ROI, and built AI-powered automation for research and reporting — self-motivated and hands-on in a lean, fast-paced setup",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Created and led the Hot on Social and Beauty Club community programmes — creator/KOL collaborations and community-driven initiatives that boosted engagement, brand visibility and customer loyalty",
                "Managed a portfolio of 42 brand and partner accounts, building relationships with multiple stakeholders and running collaborations and campaigns to grow engagement and GMV +30% QoQ",
                "Recruited and onboarded 30+ new partners in two months as PIC Fragrances — sourcing, onboarding and activating new partners at speed",
                "Analysed engagement, conversion and retention data to shape creator, channel and campaign strategy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "High-growth consumer-internet / quick-commerce | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic partner accounts and cross-functional campaigns at a high-growth consumer-internet platform, coordinating partners, agencies and stakeholders",
                "Negotiated and closed high-impact partnership deals — goal-oriented, self-motivated and bias-for-action",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Analysed performance and promotional effectiveness, turning data into clear insights and strategy recommendations",
                "Supported brand campaigns and NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": (
        "creator & influencer partnerships, creator recruitment & onboarding, creator engagement & retention "
        "strategy, community growth programmes, creator marketing & collaborations, AMAs / interviews / "
        "community initiatives, brand awareness, UGC, campaign activation"
    ),
    "skills_ecommerce": (
        "cross-channel marketing (social, paid, CRM, EDM), Instagram / TikTok / YouTube / Pinterest, social "
        "platform management, content collaborations, quick-commerce & marketplaces, marketing automation"
    ),
    "skills_commercial": (
        "partnerships management, portfolio & account management, stakeholder relationship building, "
        "negotiation, affiliate-style creator collaborations, cross-functional coordination"
    ),
    "skills_data": (
        "engagement / retention / community-growth metrics, data-driven strategy, funnel & conversion analysis, "
        "ROI/ROAS, competitor & trend tracking, performance reporting, AI-assisted analysis"
    ),
    "skills_tools": (
        "social platforms & analytics, Meta Ads Manager, Google Ads, Generative AI (Claude, ChatGPT), Notion, "
        "Power BI, Tableau, Canva, Adobe Creative Suite, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Binance Square is, at its heart, a bridge between creators and their communities — and building that "
        "bridge is the work I love and do best. The Creator Partnerships Manager role reads like my day-to-day: "
        "identify and recruit creators, own onboarding, and grow a portfolio through engagement and retention. "
        "I'm also a native Spanish speaker with C1 English, which I noticed is a listed advantage for "
        "coordinating creators across regions."
    ),
    "body_paragraph_1": (
        "Creator partnerships is genuinely my strongest muscle. At DoFreeze I built the creator/influencer "
        "programme from zero — sourcing and recruiting creators, owning onboarding, briefing, negotiation and "
        "ongoing relationship management for a portfolio of 25–50 creators per campaign, including paid "
        "collaborations — and I develop engagement and retention strategies while tracking reach, engagement "
        "and content performance. Earlier, at Alibaba's Miravia, I created and led the Hot on Social and Beauty "
        "Club community programmes (creator/KOL collaborations and community-driven initiatives) and managed a "
        "portfolio of 42 partner relationships, growing engagement and GMV +30% QoQ. I'm analytical, "
        "self-motivated and used to remote, globally distributed teams."
    ),
    "body_paragraph_2": (
        "I'll be upfront, in the interest of a good match: I'm coming into crypto from consumer, creator and "
        "marketplace marketing rather than from years inside the Web3 space, so I'd be building my crypto "
        "creator network from a strong base rather than an existing one. What I bring is that the core of this "
        "role — recruiting, growing and retaining a global creator portfolio and running community programmes — "
        "is exactly what I do best, I'm a fast, tech-forward learner (an early adopter of generative AI and new "
        "platforms) who's genuinely excited by the creator economy Binance Square is building, and I ramp "
        "quickly. I'm already based in Dubai and set up to work fully remotely."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd approach the first 90 days — mapping and recruiting high-impact "
        "creators, standing up an onboarding and engagement cadence, and building community growth programmes "
        "that turn creator collaborations into real community interaction. Thank you for considering my "
        "application — I'd love to bring proven creator-partnerships expertise to Binance Square."
    ),
}


def make_job() -> Job:
    return Job(
        id="binance-creator-partnerships-square-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (Remote)",
        url="https://www.binance.com/en/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Creator Partnerships Manager Binance Square Dubai remote",
             "function": "Partnerships / Creator & Community Marketing",
             "workplace": "Remote (work-from-home), Dubai UAE",
             "note": "Binance Square (Web3/crypto social platform). LinkedIn Easy Apply; recruiter-promoted. "
                     "Spanish listed as an advantage. Crypto-domain knowledge is the key gap."},
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
        "ai_score": 68,
        "ai_tier": "Warm",
        "skills_match": [
            "Creator/influencer partnerships end-to-end — recruit, onboard, negotiate, retain a portfolio of 25-50 creators (DoFreeze) — near 1:1 with the JD",
            "Community growth programmes + creator collaborations (Hot on Social, Beauty Club at Miravia)",
            "Portfolio/relationship management across 42 partner accounts; multi-stakeholder relationship building",
            "Engagement/retention metrics tracking + data-driven strategy",
            "Cross-channel marketing (social, paid, CRM/EDM)",
            "5+ yrs vs 'minimum 3 years' in partnerships / cross-channel marketing",
            "SPANISH native (English C1) — explicitly a listed advantage",
            "Remote, global, self-motivated, goal-oriented",
            "Fast, tech-forward learner (AI-first) — trend/competitor awareness",
            "Already based in Dubai",
        ],
        "missing_skills": [
            "Crypto / Web3 industry knowledge — 'preferably a strong understanding of the crypto industry' — NOT held (the key gap)",
            "Crypto creator community involvement / resourceful crypto network — a listed requirement — NOT held; NOT fabricated",
            "Affiliate management specifically — has influencer/creator partnerships + cross-channel marketing (JD accepts these as alternatives)",
        ],
        "sector_fit": "skills: strong (creator partnerships/community); domain: weak (no crypto/Web3 tenure)",
        "seniority_fit": "on/above band (5+ yrs vs minimum 3)",
        "red_flags": [
            "Crypto-domain knowledge and a crypto creator NETWORK are core to this specific role — Paula has neither; strong transferable skills but a real domain gap",
            "'Demonstrated involvement in the crypto creator community' is listed as a requirement, not just a plus",
            "Very high applicant volume (450+); crypto-native candidates likely compete on network",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Split verdict: the SKILL fit is one of the strongest in the pipeline, but the DOMAIN is a genuine "
            "stretch. The role's responsibilities — identify/recruit creators, own onboarding, build engagement "
            "& retention strategies, manage a portfolio of high-impact creators, run community growth programmes "
            "and creator marketing collaborations — map almost 1:1 onto Paula's single strongest, most genuine "
            "skill: she built DoFreeze's creator/influencer programme from zero (recruit, onboard, brief, "
            "negotiate, retain 25-50 creators per campaign incl. paid collabs) and led community programmes "
            "(Hot on Social, Beauty Club) at Miravia across a 42-partner portfolio. She clears the 3-year bar "
            "(5+ yrs) and Spanish-native is an explicitly listed advantage. The real gap is crypto/Web3: the JD "
            "prefers strong crypto-industry understanding and REQUIRES demonstrated involvement in the crypto "
            "creator community or a resourceful crypto network — Paula has neither, and none is fabricated. "
            "Positioned honestly on transferable creator expertise + fast, tech-forward ramp + genuine interest "
            "in the Web3 creator economy; the cover letter names the crypto gap plainly. Scored Warm to reflect "
            "the domain gap despite the excellent skills match. If Paula actually has crypto involvement "
            "(personal investing, following/knowing crypto creators, a network), it should be added truthfully "
            "to move this toward Hot. No 'no sponsorship needed' claim (remote; UAE residence visa)."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


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
