"""One-off: generate Paula's CV (+ cover letter) for Nestlé MENA's
"NesTalent — Marketing Graduate Trainee" (Dubai) — a 24-month rotational
graduate-development programme.

Honest context (IMPORTANT — this is an OFF-PROFILE / reach application):
  - The programme explicitly targets a "fresh graduate with limited work
    experience". Paula is the opposite: 4+ years and already a Brand & Marketing
    Manager. Guille decided to apply anyway (foot-in-the-door at Nestlé), fully
    aware of the overqualification risk.
  - Per the project's #1 rule we do NOT fabricate or hide anything. The CV keeps
    her real titles and real experience. What we adapt is EMPHASIS: it foregrounds
    her marketing craft (brand building, consumer insights, brand experiences, NPD
    — the exact "streams" the JD names), her CUNEF BBA with a strong thesis grade
    (they ask for "very good GPA"), and her Mondelez graduate-trainee stint at a
    global FMCG leader.
  - The COVER LETTER carries the transparency: it openly acknowledges she brings
    more than a typical graduate and explains, honestly and compellingly, why the
    programme still appeals (master big-brand marketing at Nestlé scale, structured
    rotations, learn from senior leaders, long-term career as a future leader).
  - Per standing rule: NO "own visa / no sponsorship" claim anywhere. The CV visa
    field ("UAE Residence Visa") is factual and stays; nothing is asserted about
    sponsorship in the letter.

Application channel: Nestlé careers portal (online form / "Olivia" assistant),
not email — so CONTACT = None and the letter is addressed to "Hiring Manager".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word fails on this Mac), registers the job for the
dashboard (honestly flagged as a reach), and lands the package under
output/2026-08-23/.
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

COMPANY = "Nestlé"
TITLE = "NesTalent Marketing Graduate Trainee"
DATE_FOLDER = "2026-08-23"

CONTACT = None  # Careers-portal application — letter to "Hiring Manager".

JOB_DESCRIPTION = """\
NesTalent Trainee, Marketing — NesTalent Marketing Graduate Trainee (Dubai, AE).

Position Snapshot: NesTalent is a fast-track development program focused on
nurturing future leaders across the key business areas of Nestlé Middle East and
North Africa (MENA). As a young graduate you'll gain opportunities for growth and
work on impactful projects, with a focus on innovation, diversity and
sustainability, in a supportive and inclusive environment.

Position Summary: As a Marketing Graduate Trainee you will embark on an immersive
journey into Nestlé's categories. With guidance from experienced professionals you
will gain exposure to diverse marketing streams and enhance your skillset, making a
significant impact in brand innovation, creating engaging brand experiences,
consumer insights and more.

Which profile are we looking for?
- Ability to work in a multi-functional environment, interacting effectively with
  your team and business partners.
- Able to operate in a fast-moving environment and manage time effectively.
- Curious, enthusiastic, a fast learner with strong interpersonal skills.
- Fresh graduate with limited work experience but a strong passion for Marketing.
- Fluency in English.
- Very good GPA and a bachelor's degree in business administration with a
  concentration in Marketing.

What do we offer?
- A permanent position as a Nestlé employee, starting with a 24-month program of
  several rotations in different teams.
- Access to Nestlé's comprehensive training program (soft and hard skills).
- Responsibilities developing knowledge in Marketing, brand building, consumer
  insights and the core business.
- Mentoring from senior leaders; exposure and career growth.
- Attractive package, flexible hours, hybrid/remote options.
- Post-program assignment based on opportunities and business needs.
"""

ATS = [
    "Marketing", "Graduate Trainee", "brand building", "brand innovation",
    "engaging brand experiences", "consumer insights", "consumer understanding",
    "FMCG", "fast-moving consumer goods", "multi-functional", "cross-functional",
    "business partners", "fast learner", "curiosity", "enthusiasm",
    "interpersonal skills", "time management", "fast-moving environment",
    "passion for marketing", "fluency in English", "business administration",
    "BBA", "GPA", "future leader", "leadership development", "rotational program",
    "NPD", "new product development", "go-to-market", "product launch",
    "influencer marketing", "UGC", "social media", "digital marketing",
    "campaign management", "market research", "category", "Nestlé", "MENA",
    "GCC", "Dubai", "UAE", "sustainability", "innovation",
]

CV_CONTENT = {
    "headline": (
        "Marketing & Brand Professional · Brand Building · Consumer Insights · "
        "NPD & Go-to-Market · FMCG / E-Commerce · CUNEF BBA (Marketing & E-Commerce)"
    ),
    "professional_summary": (
        "Marketing professional with a Business Administration degree (CUNEF, "
        "e-commerce & marketing focus, 9.5/10 thesis) and hands-on brand experience "
        "across FMCG, beauty and e-commerce. Genuinely passionate about brand "
        "building, consumer insights and creating engaging brand experiences — from "
        "NPD and go-to-market to influencer and digital campaigns. Curious, a fast "
        "learner and at home in fast-moving, multi-functional teams, having trained "
        "at a global FMCG leader (Mondelez) and worked with Alibaba's Miravia and "
        "Glovo, and today across 50+ markets. Fluent English (C1), Dubai-based, and "
        "eager to grow into a future marketing leader inside a world-class FMCG "
        "organisation."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Drive brand building and go-to-market for an FMCG portfolio (Befit, Eurocake, Flair) across 50+ markets — brand strategy, NPD briefs, packaging, pricing and launch",
                "Create engaging, consumer-facing brand experiences: influencer/UGC programmes (25–50 creators per campaign), sampling & seeding, and social/digital content that build awareness and engagement",
                "Turn consumer and market insights into campaign and product decisions, collaborating across sales, trade, design and supply in a fast-moving, multi-functional environment",
                "Built an AI-powered marketing system (Claude / generative AI) that accelerates market research, content and reporting — reflecting genuine curiosity and fast learning with new tools",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Used consumer insight, assortment and promotions to grow 42 accounts +30% GMV QoQ across beauty, fragrances and fashion",
                "Created and led the 'Beauty Club' and 'Hot on Social' brand-building programmes, boosting brand visibility, engagement and customer loyalty",
                "Analysed conversion, traffic and retention continuously to sharpen commercial and marketing decisions",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's retail vertical (0→1), taking new brands to market on a quick-commerce super-app",
                "Ran cross-functional campaigns end-to-end, coordinating marketing, operations and logistics teams",
                "Negotiated and managed strategic partners, driving GMV growth through data-led activations",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG leader | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Completed a structured graduate-style trainee programme at a global FMCG leader — sell-in/sell-out, promotional-effectiveness and category analysis for the chocolate category",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from consumer insight to shelf",
                "Learned FMCG brand, category and consumer fundamentals inside a large, matrixed, multi-functional organisation",
            ],
        },
    ],
    "skills_brand": (
        "brand building, brand strategy, consumer insights, engaging brand experiences, "
        "NPD end-to-end, go-to-market, influencer & UGC marketing, sampling & seeding, "
        "omnichannel campaigns, storytelling"
    ),
    "skills_ecommerce": (
        "digital & social marketing (Instagram, TikTok, Pinterest), Meta Ads, Google Ads, "
        "Shopify / e-commerce, content creation, EDM, marketing automation, "
        "generative-AI content & research"
    ),
    "skills_commercial": (
        "cross-functional collaboration, working with business partners, project & time "
        "management, category understanding, key account management, negotiation, "
        "pricing & assortment"
    ),
    "skills_data": (
        "consumer & market research, KPI tracking, sell-in/sell-out, ROI / ROAS, "
        "performance reporting, Power BI, Nielsen, forecasting"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Canva, Meta Business Suite, Google Ads, Shopify, "
        "Power BI, Nielsen, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "NesTalent's mission — developing Nestlé MENA's future marketing leaders through "
        "real work on brand innovation, engaging brand experiences and consumer insights — "
        "speaks directly to what I love most about this craft. I'm applying with genuine "
        "intent and full transparency: I already have a few years in marketing rather than "
        "coming straight out of university, and I've thought hard about why a structured "
        "graduate programme at Nestlé is exactly where I want to build the next decade of "
        "my career."
    ),
    "body_paragraph_1": (
        "My foundation is squarely in marketing. I hold a Business Administration degree "
        "from CUNEF with an e-commerce and marketing focus and a 9.5/10 thesis, and I began "
        "my career on a graduate-style trainee programme at a global FMCG leader (Mondelez), "
        "where I learned brand, category and consumer fundamentals inside a large "
        "multi-functional organisation and supported NPD launches such as Milka Spread. "
        "Since then I've stayed close to the streams NesTalent names: brand building and "
        "go-to-market, creating engaging brand experiences (influencer and social "
        "campaigns), and turning consumer insights into product and campaign decisions — "
        "always collaborating across functions and thriving in fast-moving environments. "
        "I'm fluent in English, deeply curious, and a genuinely fast learner (I even built "
        "an AI system to speed up my own research and reporting)."
    ),
    "body_paragraph_2": (
        "Let me be candid about the obvious: I bring more hands-on experience than a typical "
        "fresh graduate, and I want to be upfront about that rather than pretend otherwise. "
        "What draws me to NesTalent specifically is the chance to master big-brand marketing "
        "at Nestlé's scale and rigour — world-class categories, structured rotations, and "
        "mentoring from senior leaders — inside a company where I can grow long-term as a "
        "future leader. I'd bring real commercial hustle and launch experience to the cohort "
        "from day one while learning the Nestlé way properly. I'm based in Dubai and would "
        "relish the breadth and pace the rotations offer across MENA."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to talk through how I'd contribute to a rotation team and why "
        "I'm choosing to invest in Nestlé's development path deliberately. Thank you for "
        "considering an application that doesn't fit the usual mould — I'm confident my "
        "passion for marketing, curiosity and drive make me a strong fit for what NesTalent "
        "is really trying to build. I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="nestle-nestalent-marketing-trainee-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="",  # Nestlé careers portal posting (Dubai, AE, 52185)
        source="careers_portal",
        description=JOB_DESCRIPTION,
        raw={"query": "Nestlé NesTalent Marketing Graduate Trainee Dubai",
             "function": "Marketing graduate-development programme (brand building, consumer insights, NPD)",
             "sector": "FMCG (Nestlé MENA)",
             "note": "OFF-PROFILE / REACH APPLICATION. Programme targets a 'fresh graduate with "
                     "limited work experience'; Paula is a Brand & Marketing Manager with 4+ years, "
                     "so high overqualification-rejection risk. Applied anyway by explicit decision "
                     "(foot-in-the-door at Nestlé). NOTHING fabricated or hidden: real titles kept; "
                     "CV emphasises marketing craft + CUNEF BBA (9.5/10 thesis) + Mondelez trainee "
                     "stint; the cover letter transparently addresses the seniority gap and the "
                     "genuine motivation. No 'own visa / no sponsorship' claim."},
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
        "salary_raw": "'Attractive package' (graduate programme — not disclosed; typically below manager band)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 38,
        "ai_tier": "Reach (off-profile)",
        "skills_match": [
            "Strong marketing foundation: CUNEF BBA (e-commerce & marketing focus, 9.5/10 thesis) — maps to 'very good GPA + BBA' requirement",
            "Began career on a graduate-style trainee programme at a global FMCG leader (Mondelez) — brand/category/consumer fundamentals + NPD",
            "Direct experience in the streams the JD names: brand building, engaging brand experiences (influencer/social), consumer insights, NPD & go-to-market",
            "Curious, fast learner (built an AI system for research/reporting), strong cross-functional collaboration in fast-moving environments",
            "Fluent English (C1); already Dubai-based for a MENA rotational programme",
        ],
        "missing_skills": [
            "SENIORITY MISMATCH (the core issue): programme wants a 'fresh graduate with limited work experience'; Paula is a Manager with 4+ years — high overqualification-rejection risk and likely below her current salary band",
            "Not a recent graduate (CUNEF 2020) — outside the usual graduate-intake window",
        ],
        "sector_fit": "excellent (Nestlé = top-tier FMCG, directly on-sector)",
        "seniority_fit": "OFF-BAND — this is a graduate/trainee programme; Paula is mid/senior. Applied deliberately as a reach; risk disclosed",
        "red_flags": [
            "Overqualification is the headline risk: graduate programmes routinely auto-reject experienced managers. Handled by a transparent cover letter, but the risk remains real.",
            "Compensation ('attractive package' for a graduate) likely lands below Paula's 20k AED/month floor — confirm before accepting any offer.",
            "Nothing fabricated: real Manager titles kept on the CV; the letter is candid about the experience gap rather than hiding it.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa).",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Deliberate off-profile / reach application to Nestlé MENA's NesTalent Marketing "
            "Graduate Trainee programme. Sector fit is excellent (Nestlé is a premier FMCG target) "
            "but seniority fit is off-band: the programme explicitly wants a fresh graduate with "
            "limited experience, and Paula is a Brand & Marketing Manager with 4+ years. Guille chose "
            "to apply anyway for the foot-in-the-door value. Per project rules nothing is fabricated "
            "or concealed — the CV keeps her real titles and foregrounds her genuine marketing "
            "foundation (CUNEF BBA with 9.5/10 thesis, Mondelez graduate-trainee stint, brand "
            "building / consumer insights / NPD), and the cover letter transparently acknowledges she "
            "brings more than a typical graduate while making an honest case for why the structured "
            "Nestlé path still appeals. Main risk: overqualification auto-rejection; secondary risk: "
            "graduate-level pay below her 20k AED floor. No 'own visa / no sponsorship' claim."
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
