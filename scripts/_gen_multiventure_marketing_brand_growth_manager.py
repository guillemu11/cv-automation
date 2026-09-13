"""One-off: generate Paula's CV (+ cover letter) for a Dubai "Marketing & Brand
Growth Manager" role working directly with the CEO across multiple business
ventures (technology, AI, blockchain, IT infrastructure, e-commerce, SaaS).

Why the WORK is a strong fit (honest):
  - AI-first generalist growth marketer is exactly Paula: the JD's headline ask is
    "implement AI tools, automations and modern marketing technologies to improve
    efficiency and results" — she BUILT an AI-powered marketing-automation system
    (Claude / generative AI) for research, content, campaign planning, KPI
    reporting and decks/landing pages. On-the-nose, rare edge.
  - Works directly with the CEO: real precedent — at Miravia she owned the Flash
    Sales channel reporting DIRECTLY to the CEO.
  - Develop & execute brand/marketing strategy, multi-channel campaigns for
    profitable sales, own digital presence, content strategy with agencies/AI/
    freelancers, analyse ROI/conversion/customer behaviour, coordinate agencies/
    vendors, manage MULTIPLE projects/brands simultaneously, present to leadership
    — all things she does now across Befit/Eurocake/Flair and 50+ markets.
  - "High value startup, digital agency, or reputed brand a MUST": Alibaba's
    Miravia + Glovo (hyper-growth startup) + Mondelez (reputed brand) all qualify.
  - "UK / EU market experience preferred": Paula is Spanish (EU) and built her
    career in Madrid (Glovo, Miravia, Mondelez) — genuine EU-market experience.
  - Independent, ownership, minimal supervision, storytelling/presentation in
    English (C1): all real. "Female Applicants preferred" — Paula qualifies.

Honest gaps (disclosed, NOT fabricated):
  - Sector: she is e-commerce / FMCG / beauty / fashion — NOT tech / SaaS /
    blockchain / IT infrastructure. Bridged honestly via AI-first tooling and
    Shopify/e-commerce (SaaS-adjacent); disclosed in the cover letter.
  - Tenure: JD requires "5 years (Required)". Paula's marketing & commercial
    career runs from Mondelez (Aug 2021) through today — ~5 years by Aug 2026 —
    across Mondelez, Glovo, Miravia and DoFreeze. Framed as "five years of
    marketing and commercial experience since 2021", which is defensible; NOT
    inflated beyond that.
  - German preferred — she does NOT have German; not claimed.
  - Per standing rule, NO "own visa / no sponsorship needed" claim — her UAE
    residence visa is employer-sponsored. CV states the factual "UAE Residence
    Visa" only (already in profile). The application's "Do you have your own
    visa?" question needs a human decision — flagged to Paula/Guille, not answered
    here.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-21/.
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

COMPANY = "Multi-Venture Group"
TITLE = "Marketing & Brand Growth Manager"
DATE_FOLDER = "2026-08-21"

# No company or hiring manager named (CEO office, multiple ventures) — letter
# stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Marketing & Brand Growth Manager — Dubai (in person). Base AED 5,000 + incentives
AED 10,000–25,000 tied to direct sales revenue.

Work directly with the CEO and take ownership of marketing, branding, lead
generation and growth initiatives across multiple business ventures in technology,
AI, blockchain, IT infrastructure, e-commerce and SaaS. This is NOT a social media
management role. Think strategically, execute independently, identify
opportunities, build brands, generate leads and drive measurable business results.
Shape the public image, market positioning and growth strategy of multiple
companies. Commercially minded, resourceful, proactive, confident, turning ideas
into execution without constant supervision.

Key responsibilities:
- Develop and execute marketing and brand strategies.
- Do market research and implement data-gathering methods.
- Design and manage multi-channel campaigns to generate profitable sales.
- Take ownership of digital presence across all channels.
- Develop content strategies and work with agencies, AI and freelancers to produce
  high-quality content: presentations, videos, graphics, articles, campaigns and
  promotional materials.
- Analyse, improve and report campaign performance, customer behaviour, conversion
  metrics and marketing ROI.
- Implement AI tools, automations and modern marketing technologies to improve
  efficiency and results.
- Coordinate external agencies, designers, content creators, media partners and
  vendors when required.
- Manage multiple projects across the companies simultaneously.
- Present marketing plans, growth initiatives and performance reports directly to
  company leadership.

What success looks like (first 12 months): increased qualified lead generation;
improved brand visibility and market positioning; growth in audience engagement
and digital reach; stronger executive and company branding; successful launch and
execution of campaigns; measurable contribution to business growth and revenue.

Required: 5+ years in marketing, branding, growth marketing, digital strategy,
business development or related. Past experience in a high-value startup, digital
agency or reputed brand is a must. University-qualified (degree desirable, not
mandatory). Demonstrated track record of measurable business results — share
achievements and your role clearly. Ability to work independently with minimal
supervision. UK / EU market experience preferred. Female applicants preferred.

Required skills: managing multiple marketing projects concept-to-execution; strong
analytical, strategic and creative problem-solving; excellent communication,
storytelling and presentation in English; experience with AI tools, marketing
automation platforms, analytics tools, CRM and modern content-creation technology.

Added advantages: UAE driving licence; German/Dutch/French; existing UAE residence
visa; experience building personal brands or executive thought-leadership
programmes.

Application requirements: updated CV, portfolio / work samples, campaign examples
or case studies, and examples of measurable results. Applications without
supporting work samples may not be considered.
"""

ATS = [
    "Marketing & Brand Growth Manager", "brand growth", "growth marketing",
    "marketing strategy", "brand strategy", "branding", "market positioning",
    "lead generation", "qualified leads", "business development", "digital strategy",
    "multi-channel campaigns", "profitable sales", "revenue growth",
    "measurable results", "business results", "digital presence",
    "content strategy", "content creation", "storytelling", "presentations",
    "campaign performance", "conversion metrics", "customer behaviour",
    "marketing ROI", "ROAS", "market research", "data gathering",
    "AI tools", "marketing automation", "automations", "marketing technology",
    "martech", "analytics", "CRM", "Salesforce",
    "agencies", "freelancers", "vendors", "designers", "content creators",
    "multiple projects", "concept to execution", "work independently",
    "minimal supervision", "present to leadership", "executive branding",
    "personal brand", "thought leadership", "startup", "reputed brand",
    "digital agency", "EU market", "UK market", "e-commerce", "Shopify",
    "Meta Ads", "Google Ads", "paid media", "CRO", "GMV", "P&L", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Marketing & Brand Growth Manager · AI-First Marketing & Automation · Multi-Venture / Multi-Brand "
        "Growth · Brand Strategy, Lead Gen & Multi-Channel Campaigns · Direct-to-CEO Reporting"
    ),
    "professional_summary": (
        "Commercially minded brand & growth marketer with five years of marketing and commercial experience "
        "(since 2021), now leading Brand & Marketing across multiple brands and 50+ markets from Dubai. I develop "
        "and execute brand and marketing strategy end-to-end, design multi-channel campaigns engineered to drive "
        "profitable sales and qualified leads, and I own the AI side of modern marketing — I built an AI-powered "
        "marketing-automation system (Claude / generative AI) that turns market research, content, campaign "
        "planning, KPI reporting and pitch decks/landing pages into repeatable workflows, cutting manual "
        "workload ~40%. I work independently with minimal supervision, coordinate agencies, freelancers and "
        "vendors, manage several projects at once, and present plans and performance to leadership — I reported "
        "directly to the CEO at Alibaba's Miravia, where I grew 42 accounts +30% GMV QoQ. EU-market native "
        "(Spanish; career built in Madrid across Glovo, Miravia and Mondelez), fluent English (C1), based in "
        "Dubai. Business Administration graduate (CUNEF)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-market group | Multiple brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Develop and execute brand & marketing strategy across multiple brands and 50+ markets — owning positioning, go-to-market and growth end-to-end with minimal supervision",
                "Implement AI tools, automations and modern marketing technologies — built an AI-powered marketing-automation system (Claude / generative AI) that turns market research, content, campaign planning, KPI reporting and decks/landing pages into repeatable workflows, cutting manual workload ~40%",
                "Design and manage multi-channel campaigns engineered to drive profitable sales and leads — Meta & Google paid media, influencer/UGC, social, EDM and e-commerce — then analyse ROI, ROAS, conversion and customer behaviour to improve results",
                "Take ownership of the digital presence across all channels — running the Shopify e-store end-to-end (CRO, UX, merchandising) to lift conversion and average order value",
                "Develop content strategies and produce high-quality content with agencies, AI and freelancers — presentations/decks, landing pages, video, graphics and campaign assets",
                "Coordinate external agencies, designers, content creators and vendors and manage multiple projects and launches simultaneously across markets",
                "Run market research and data-gathering, then present marketing plans, growth initiatives and performance reports to company leadership",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce | Reputed global brand (Alibaba) | 100K+ employees",
            "bullets": [
                "Reported directly to the CEO owning the Flash Sales channel for Beauty, Fashion & Home — planning and executing commercial campaigns tied to P&L targets",
                "Grew 42 key accounts +30% GMV growth QoQ through pricing, assortment and data-led multi-channel promotions — measurable revenue impact",
                "Created and led the 'Beauty Club' and 'Hot on Social' brand programmes end-to-end, boosting brand visibility, audience engagement and digital reach",
                "Continuously analysed conversion, traffic, retention, ROI and ROAS to optimise campaign performance and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Hyper-growth startup / quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Worked inside a hyper-growth startup, driving GMV growth for strategic accounts through data-led campaigns and bespoke activations",
                "Negotiated and closed high-impact commercial deals — hands-on business development and lead-to-revenue ownership",
                "Ran complex cross-functional campaigns from concept to execution across marketing, logistics and support",
                "Helped build Glovo's Retail vertical, taking new fashion and lifestyle brands to market on the platform",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Reputed brand | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness analysis and performance reports for the chocolate category, distilling data into actionable insight",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to execution",
                "Identified growth opportunities across the category through consumer and market analysis",
            ],
        },
    ],
    "skills_brand": (
        "brand strategy & market positioning, growth marketing, brand building, go-to-market, multi-channel "
        "campaigns, content strategy, storytelling & presentations, executive/brand content (decks, landing "
        "pages), product launches / NPD, influencer & UGC"
    ),
    "skills_ecommerce": (
        "AI marketing tools & automation (Claude / generative AI), modern marketing technology (martech), "
        "paid media (Meta / Google Ads), lead generation, conversion rate optimisation (CRO), Shopify e-store, "
        "digital presence across channels, social & EDM, landing pages"
    ),
    "skills_commercial": (
        "multi-venture / multi-brand management, managing multiple projects concept-to-execution, "
        "business development & deal closing, independent ownership (minimal supervision), agency / freelancer / "
        "vendor coordination, CEO-level reporting & presentation, negotiation, key account management"
    ),
    "skills_data": (
        "campaign performance & marketing ROI analysis, customer behaviour & conversion metrics, market "
        "research & data gathering, KPI reporting, ROAS, P&L, Salesforce (CRM), Power BI, forecasting"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), marketing automation, Meta Ads Manager, Google Ads, Shopify, "
        "Salesforce (CRM), Power BI, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "A role working directly with the CEO to build brands, generate leads and drive measurable growth "
        "across multiple ventures — where the brief is explicitly to implement AI tools, automations and modern "
        "marketing technology, not to manage social feeds — is exactly the kind of ownership I'm looking for. "
        "I'm a commercially minded brand and growth marketer who already runs marketing across multiple brands "
        "and 50+ markets from Dubai, and being AI-first isn't a buzzword for me: I built the automation that "
        "makes a lean marketing function move like a much bigger one."
    ),
    "body_paragraph_1": (
        "Your responsibilities map onto what I do every day. At DoFreeze I develop and execute brand and "
        "marketing strategy across several brands, design multi-channel campaigns (Meta and Google paid media, "
        "e-commerce, influencer, social, EDM) built to drive profitable sales, own the digital presence "
        "end-to-end, and analyse ROI, conversion and customer behaviour to improve results — coordinating "
        "agencies, freelancers and vendors and running multiple projects at once. The AI ask is my sharpest "
        "edge: I built a marketing-automation system on Claude / generative AI that turns research, content, "
        "campaign planning, reporting and decks/landing pages into repeatable workflows and cut manual workload "
        "~40%. And I'm comfortable at the top table — at Alibaba's Miravia I owned the Flash Sales channel "
        "reporting directly to the CEO and grew 42 accounts +30% GMV QoQ, presenting plans and performance to "
        "leadership."
    ),
    "body_paragraph_2": (
        "A few honest notes so you can calibrate. My sector background is e-commerce, FMCG, beauty and fashion "
        "rather than SaaS, blockchain or IT infrastructure — but I'm AI-native and own e-commerce/Shopify and "
        "martech day to day, so the digital and software-adjacent terrain is familiar, and I ramp fast on new "
        "categories. My marketing and commercial career runs from 2021 across Mondelez, Glovo, Miravia and "
        "DoFreeze — around five years, inside a hyper-growth startup (Glovo) and reputed global brands "
        "(Alibaba's Miravia, Mondelez), which is the pedigree your brief asks for. I'm EU-market native "
        "(Spanish, career built in Madrid), work independently with minimal supervision, and turn ideas into "
        "execution — exactly the resourceful, self-directed operator this role needs."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show, not just tell: I can share campaign case studies, the AI-automation "
        "system I built and examples of measurable results (from +30% GMV QoQ to launch and content work). I'm "
        "based in Dubai and available to talk through how I'd approach brand and growth across your ventures in "
        "the first 90 days. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="multiventure-marketing-brand-growth-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="",
        source="job board",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing & Brand Growth Manager",
             "function": "Brand / Growth Marketing (AI-first, multi-venture, reports to CEO)",
             "sector": "Technology / AI / Blockchain / IT infrastructure / E-commerce / SaaS",
             "compensation": "Base AED 5,000 + incentives AED 10,000–25,000 (tied to direct sales revenue)",
             "note": "No company named (CEO office, multiple ventures). WORK fit is strong (AI-first growth "
                     "generalist), but OFFER quality is a concern: base AED 5,000 is far below Paula's 20k floor "
                     "and the upside is sales-commission. Sector (tech/SaaS/blockchain) is a real gap, disclosed "
                     "honestly. 'Do you have your own visa?' application question needs a human decision — visa "
                     "is employer-sponsored; do NOT answer 'own visa / no sponsorship'."},
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
        "salary_raw": "AED 5,000 base + AED 10,000–25,000 incentives (tied to direct sales revenue)",
        "salary_aed_min": 5000,
        "salary_aed_max": 25000,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 66,
        "ai_tier": "Warm",
        "skills_match": [
            "AI tools / automation / marketing technology — Paula's rarest edge (BUILT an AI marketing-automation system on Claude); the JD's headline ask",
            "Works directly with the CEO — real precedent: owned Flash Sales channel reporting DIRECTLY to the CEO at Miravia",
            "Develop & execute brand/marketing strategy; multi-channel campaigns for profitable sales & leads",
            "Own digital presence across all channels (Shopify e-store, paid, social, EDM); CRO/AOV",
            "Analyse campaign performance, ROI, conversion, customer behaviour; market research & data gathering",
            "Coordinate agencies/designers/content creators/vendors; content strategy with agencies/AI/freelancers",
            "Manage MULTIPLE projects/brands simultaneously (Befit/Eurocake/Flair, 50+ markets)",
            "Present plans & performance to leadership; +30% GMV QoQ, 42 accounts (measurable results)",
            "'High-value startup / reputed brand a MUST' — Alibaba's Miravia + Glovo (hyper-growth startup) + Mondelez",
            "UK/EU market experience preferred — EU-native (Spanish; career in Madrid); independent, minimal-supervision operator; English C1; female applicant preferred (qualifies)",
        ],
        "missing_skills": [
            "Sector: tech / SaaS / blockchain / IT infrastructure (real gap — she is e-commerce/FMCG/beauty/fashion). Bridged honestly via AI-first tooling + Shopify/e-commerce (SaaS-adjacent); disclosed in cover letter, not claimed as tech tenure",
            "Tenure: JD requires 5 years. Paula's marketing/commercial career runs 2021→now (~5 yrs by Aug 2026 across Mondelez/Glovo/Miravia/DoFreeze); framed as 'five years since 2021', defensible, not inflated further",
            "German preferred — not held, not claimed",
        ],
        "sector_fit": "adjacent (AI-first + e-commerce/Shopify are SaaS-adjacent; tech/blockchain/SaaS is new — disclosed honestly)",
        "seniority_fit": "on-band for the work (manager-level, independent owner); 5-yr bar met by counting from 2021",
        "red_flags": [
            "COMPENSATION: base AED 5,000 is far below Paula's 20k/month floor; upside (AED 10k–25k) is sales-commission tied to direct revenue. Effectively a commission-heavy growth/sales role. Fails the pipeline's own salary floor on base — flag for a human go/no-go before applying.",
            "Low-quality/risk signals: unnamed company, 'multiple ventures' incl. blockchain, 'Female Applicants preferred', heavy commission, in-person Dubai — typical of small owner-run setups. Verify legitimacy before investing.",
            "'Do you have your own visa?' + 'existing UAE residence visa' as advantage — Paula's visa is EMPLOYER-SPONSORED; do NOT answer 'own visa / no sponsorship'. Human decision required.",
            "Application requires portfolio / work samples / case studies — CV+CL alone 'may not be considered'. Recommend attaching a landing/deck as the work sample.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "The WORK is a strong, on-profile fit: an AI-first, commercially minded generalist growth marketer "
            "who develops and executes brand/marketing strategy, runs multi-channel campaigns for profitable "
            "sales and leads, owns digital presence, analyses ROI/conversion, implements AI tools & automation "
            "(her rarest edge — she built one on Claude), coordinates agencies/vendors, manages multiple "
            "projects across ventures, and presents to the CEO (real precedent at Miravia). Startup/reputed-"
            "brand pedigree (Alibaba, Glovo, Mondelez) and EU-market background match the brief. Honest gaps: "
            "sector is e-commerce/FMCG/beauty not tech/SaaS/blockchain (bridged via AI + Shopify, disclosed); "
            "tenure meets the 5-yr bar by counting from 2021; no German. The real caution is the OFFER, not the "
            "fit: base AED 5,000 sits far below the 20k floor with commission-based upside, plus several small-"
            "owner/risk signals — a human go/no-go is warranted before applying. No 'own visa / no sponsorship' "
            "claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only."
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
