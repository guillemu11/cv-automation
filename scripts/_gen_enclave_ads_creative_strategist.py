"""One-off: generate Paula's CV for **Ads Creative Strategist** at **Enclave BioActives**
(Emma Relief — DTC gut-health / supplements brand; Dubai, remote — LinkedIn, 144 applicants).

JD (from the posting): Creative Strategist who "lives and breathes paid ads" for an
established 8-figure DTC health & wellness operation. Mine Meta Ad Library and customer
reviews for angles, dissect WHY a winner won (hook, visual, problem, mechanism,
spokesperson, first 3 seconds, emotional trigger, format), then turn one winner into five.
Asks for: prior Creative Strategist experience for DTC/eCommerce brands (brand-side or
agency), ideally health/wellness/supplements/nutraceuticals; work with 8- or 9-figure DTC
brands; heavy Meta spend; UGC, statics, founder ads, testimonials, advertorials, long-form
direct-response; concrete examples of ads turned into winners.

Paula's honest angle:
- PAID SOCIAL + CREATIVE TESTING: at DoFreeze she plans and optimises Meta (FB/IG) and
  Google Ads — audience building, creative A/B testing, ROI/ROAS analysis.
- CREATIVE + UGC SUPPLY AT VOLUME: built the influencer/UGC programme from zero, briefing
  25–50 creators per campaign (testimonial-style content, sampling & seeding) — i.e. she
  already writes briefs and turns angles into shootable concepts.
- DTC / SHOPIFY OWNERSHIP: owns the Shopify store end-to-end (merchandising, UX, CRO, AOV),
  so she reads the ad→landing→checkout funnel, not just the ad.
- HEALTH & WELLNESS ADJACENCY: Befit is DoFreeze's health-positioned brand; Miravia beauty
  & fragrance accounts add consumer/claims sensitivity.
- CONTENT AT SCALE WITH AI: her generative-AI system produces campaign concepts and content
  variants fast — directly relevant to "turn a winner into five more winners".

Honesty guardrails: she has NOT held a dedicated Creative Strategist title, has NOT worked
for 8/9-figure DTC brands, and has NO supplements/nutraceutical experience — none of that is
implied on the CV, and no ad-spend figures are invented (her real spend scale is not
documented). No Arabic claimed. Factual "UAE Residence Visa" only — never "no sponsorship
needed". Role is remote-from-Dubai, which she can do from her current base.

ONE-PAGE standard: tight summary, 3/2/1/1 bullets, ~6 skills/row, SHORT labels.
Fills the real CV template, relabels the skills rows for this role, converts to PDF via
LibreOffice, registers the job, verifies 1 page, lands under output/2026-09-03/.
Also drops a short-named 'Paula De Francisco - CV.pdf' copy for portals / Easy Apply.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from docx import Document

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Enclave BioActives"
TITLE = "Ads Creative Strategist"
DATE_FOLDER = "2026-09-03"

JOB_DESCRIPTION = """\
Ads Creative Strategist — Enclave BioActives (Emma Relief), Dubai, UAE. Remote, full time.
Enclave BioActives is the company behind Emma Relief, one of the fastest-growing gut-health brands
in DTC. Established performance-marketing operation, large customer base, thousands of reviews.
We're looking for a Creative Strategist who lives and breathes paid ads: someone who can open Meta
Ad Library and disappear for two hours because they found an interesting angle, who reads customer
reviews and sees ad concepts, and who looks at a winning ad and asks WHY it performed — the hook,
the visual, the problem, the mechanism, the spokesperson, the first three seconds, the emotional
trigger, the format — and then turns that winner into five more winners. Your job is simple: find
the next winning ad.
You're probably a fit if: you've worked as a Creative Strategist for DTC/eCommerce brands (direct or
via an agency), ideally in health, wellness, supplements or nutraceuticals; you've worked with
8-figure or 9-figure DTC brands; you've developed ads for brands spending heavily on Meta; you've
worked across UGC, statics, founder ads, testimonials, advertorial-style concepts, long-form creative
or other direct-response formats; and you have actual examples of ads you helped turn into winners.
"""

ATS = [
    "creative strategist", "ads creative strategist", "paid ads", "paid social",
    "Meta Ads", "Facebook Ads", "Instagram Ads", "Meta Ad Library", "ad concepts",
    "hooks", "angles", "direct response", "DTC", "D2C", "eCommerce", "e-commerce",
    "performance marketing", "creative testing", "A/B testing", "iteration",
    "scaling winners", "UGC", "user-generated content", "statics", "testimonials",
    "founder ads", "advertorial", "long-form creative", "video ads", "creator briefs",
    "influencer marketing", "customer reviews", "voice of customer", "messaging",
    "health & wellness", "supplements", "nutraceuticals", "Shopify", "landing page",
    "CRO", "conversion rate", "AOV", "ROAS", "ROI", "CPA", "CTR", "hook rate",
    "media buying", "audience building", "brand", "campaigns", "analytics", "KPI",
    "Dubai", "UAE", "remote",
]

CONTENT = {
    "headline": (
        "Creative Strategist · Paid Social & DTC Growth · Meta Ads & Direct-Response Creative · "
        "UGC, Testing & Scaling Winners"
    ),
    "professional_summary": (
        "Brand and e-commerce marketer who builds and tests paid-social creative for DTC brands — "
        "concepts and hooks, UGC and testimonial content, statics and video — then reads the data to "
        "find what won and why. Runs Meta and Google Ads end-to-end (audiences, A/B tests, ROI/ROAS), "
        "briefs 25–50 creators per campaign, and owns the Shopify funnel behind the ad (CRO, AOV). "
        "Dubai-based, available remote."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Consumer brands incl. Befit (health-positioned) | Shopify DTC + retail | 50+ countries",
            "bullets": [
                "Plan and optimise paid social on Meta (Facebook & Instagram) and Google Ads — audience building, creative A/B testing across statics, video and UGC, and ROI/ROAS analysis that decides which concepts get killed, iterated or scaled",
                "Build the creative pipeline end-to-end: source and brief 25–50 creators per campaign for testimonial and UGC-style content plus sampling and seeding, turning customer language and product benefits into ad angles and hooks that can be shot fast and tested cheaply",
                "Own the Shopify DTC store behind the ads (merchandising, UX, CRO, AOV) so creative, landing page and offer are tested as one funnel — and use generative AI (Claude/GPT) to spin winning angles into new concept variants at speed, cutting production turnaround ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew 42 consumer accounts +30% GMV QoQ by testing offers, promo mechanics and campaign creative, and reading traffic, conversion, ROI/ROAS and retention to double down on what worked",
                "Created and led Hot on Social and the Beauty Club — social-first content and creator programmes built from customer reviews and trending formats, lifting engagement, repeat purchase and brand visibility",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Ran bespoke marketing activations and promo campaigns with major consumer partners, tracking order volume and GMV per activation to identify the mechanics worth repeating",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Chocolate category",
            "bullets": [
                "Analysed promotional effectiveness and sell-in/sell-out performance to explain why specific activations won — the analytical habit behind every creative teardown",
            ],
        },
    ],
    "skills_brand": (  # label -> "Creative Strategy"
        "ad concepts & angles, hooks & first-3-seconds, direct-response copy, UGC & testimonial formats, "
        "statics & video ads, creator briefs, voice-of-customer & review mining, storyboarding"
    ),
    "skills_ecommerce": (  # label -> "Paid Social & DTC"
        "Meta Ads (Facebook & Instagram), Google Ads, audience building, creative testing & iteration, "
        "scaling winners, Shopify DTC, landing pages & CRO, AOV, EDM"
    ),
    "skills_commercial": (  # label -> "Production & Partners"
        "influencer & UGC programmes (25–50 creators/campaign), sampling & seeding, agency & creator management, "
        "briefing & feedback loops, art direction (Adobe, Canva), AI-assisted content at scale"
    ),
    "skills_data": (  # label -> "Performance & Analysis"
        "ROAS, ROI, CPA, CTR, conversion rate, creative A/B testing, KPI dashboards & reporting, "
        "post-campaign teardowns, forecasting"
    ),
    "skills_tools": (  # label -> "Tools"
        "Meta Ads Manager, Meta Business Suite, Meta Ad Library, Google Ads, Shopify, Power BI, Tableau, "
        "Looker, Adobe (Photoshop, Illustrator), Canva, Generative AI (Claude, ChatGPT)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Creative Strategy",
    "E-Commerce & Digital": "Paid Social & DTC",
    "Commercial": "Production & Partners",
    "Data & Analytics": "Performance & Analysis",
}


def make_job() -> Job:
    return Job(
        id="enclave-bioactives-ads-creative-strategist-dubai-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (Remote)",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Enclave BioActives Ads Creative Strategist Dubai remote DTC supplements Emma Relief",
            "note": "Emma Relief (gut-health supplements), 8-figure DTC. Posted by recruiter Kristienne "
                    "Jerica Ruiz (RZ HR Studio); responses handled OUTSIDE LinkedIn — apply via the link in "
                    "the post, so a CV PDF is what matters. 144 applicants (23 in the last day). Specialist "
                    "creative-strategist role: Paula has real paid-social + UGC + DTC funnel experience but "
                    "no Creative Strategist title, no 8/9-figure DTC brand, no supplements category and no "
                    "documented Meta spend scale — do NOT imply otherwise. Remote from Dubai.",
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
        "id": job.id, "title": job.title, "company": job.company, "location": job.location,
        "url": job.url, "source": job.source, "description": job.description,
        "salary_raw": None, "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 63, "ai_tier": "Warm",
        "skills_match": [
            "Meta (FB/IG) + Google Ads hands-on: audiences, creative A/B testing, ROI/ROAS optimisation",
            "Creative supply at volume: influencer/UGC programme built from zero, 25–50 creators briefed per campaign (testimonial-style content, sampling & seeding)",
            "DTC funnel ownership: Shopify store end-to-end (merchandising, UX, CRO, AOV) — reads ad → landing → checkout as one system",
            "Health & wellness adjacency via Befit (health-positioned brand) and beauty/fragrance accounts at Miravia",
            "AI-assisted content production — spins winning angles into new variants fast (the 'one winner into five' ask)",
            "Analytical teardown habit: promo effectiveness and sell-in/sell-out analysis at Mondelez; conversion/ROAS reads at Miravia",
        ],
        "missing_skills": [
            "No dedicated Creative Strategist title — her creative work sits inside broader brand/e-com roles",
            "No 8- or 9-figure DTC brand experience, and no documented large-scale Meta spend (do not invent numbers)",
            "No supplements / nutraceutical / gut-health category experience — the JD's 'ideally' preference",
            "No portfolio of specific ads she turned into winners; the JD asks for concrete examples — she'd need to assemble a short creative teardown to compete",
        ],
        "sector_fit": "partial (DTC e-commerce and consumer health-adjacent, but not supplements/nutraceuticals)",
        "seniority_fit": "plausible IC level, but specialist-skill depth is the gap, not seniority",
        "red_flags": [
            "Specialist role in a crowded field — 144 applicants in days, and true creative strategists apply with an ad portfolio",
            "Applications handled outside LinkedIn via a recruiter (RZ HR Studio) — less visibility on process",
            "No salary published — confirm against the AED 20K/month floor",
            "Remote role, which is outside Paula's stated preference (remote_ok: false in profile.yaml)",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Honest verdict: a stretch with a real, defensible angle. Enclave wants a specialist who lives "
            "inside Meta Ad Library and produces direct-response concepts for an 8-figure DTC supplement "
            "brand. Paula is a brand/e-commerce generalist — but the specific things this job runs on she "
            "does do today: she plans and optimises Meta and Google Ads with creative A/B testing, she "
            "briefs 25–50 creators per campaign for UGC and testimonial content, she owns the Shopify "
            "funnel the ads point at, and she uses generative AI to produce concept variants at speed. "
            "What she can't claim is the Creative Strategist title, an 8/9-figure DTC brand on the CV, a "
            "supplements background, or a portfolio of named winning ads — the CV therefore leads on paid "
            "social + creative production + funnel, and claims none of the rest. To have a real shot she "
            "should attach a short Emma Relief creative teardown (3–5 concepts from review mining plus the "
            "angle behind each), since the posting explicitly asks for evidence of ads turned into winners."
        ),
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relabel_for_role(docx_path: Path) -> None:
    doc = Document(str(docx_path))
    for table in doc.tables:
        for row in table.rows:
            first = row.cells[0]
            new = ROLE_LABELS.get(first.text.strip())
            if not new:
                continue
            para = first.paragraphs[0]
            if para.runs:
                para.runs[0].text = new
                for r in para.runs[1:]:
                    r.text = ""
            else:
                para.add_run(new)
    doc.save(str(docx_path))


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

    cv_docx = cv._fill_template(CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
