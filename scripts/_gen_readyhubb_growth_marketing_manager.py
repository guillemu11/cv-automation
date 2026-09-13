"""One-off: generate Paula's CV for **Growth Marketing Manager** at **Readyhubb**
(SaaS / beauty-tech platform for beauty professionals; Dubai, remote — LinkedIn, 403 applicants).

JD ask: data-driven, customer-obsessed growth marketer to drive acquisition, activation,
retention and revenue for a SaaS platform used by beauty professionals. Paid acquisition
(especially Meta), reactivation of an existing database, creator/affiliate/partnership/referral
programmes, landing pages and funnels, email/CRM/lifecycle, full-funnel analysis
(CAC, conversion, activation, churn, MRR), constant experimentation, and the ability to execute
without a big team or agency. 4+ years growth/performance/digital. Marketing to beauty
professionals, SMBs, creators or service businesses is a "strong advantage".

Paula's honest angle:
- PAID ACQUISITION: runs Meta (FB/IG) and Google Ads end-to-end at DoFreeze — audiences,
  creative A/B testing, ROI/ROAS optimisation.
- CREATORS AT VOLUME: built the influencer/creator programme from zero, 25–50 creators per
  campaign (sourcing, briefing, negotiating) — the JD's creator/partnership lever.
- FUNNEL OWNERSHIP: owns the Shopify store end-to-end — landing pages, offers, checkout, CRO,
  AOV — plus EDM/lifecycle campaigns.
- BEAUTY PROFESSIONALS & SMBs (the "strong advantage"): at Miravia she managed 42 beauty,
  fragrance and fashion accounts and, as PIC Fragrances, acquired and activated 30+ new stores
  in two months — i.e. selling to and activating small beauty businesses and distributors.
- MARKETPLACE / PLATFORM GROWTH: Miravia (Alibaba) and Glovo's retail vertical build-out —
  acquiring partners onto a platform and getting them to transact.
- RESOURCEFUL / NO BIG TEAM: built an AI automation system (Claude/GPT) that cuts manual
  workload ~40%, so she ships experiments fast solo.

Honesty guardrails: she has NOT worked in SaaS and has NOT owned subscription metrics
(MRR, churn, CAC payback) — the CV claims platform/marketplace and e-commerce funnel work,
never SaaS subscription ownership. No affiliate-programme claim (she has creator and
partnership work, not affiliate). No Arabic. Factual "UAE Residence Visa" only — never
"no sponsorship needed". Remote-from-Dubai role.

ONE-PAGE standard: tight summary, 3/2/1/1 bullets, ~6-9 short skills per row.
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

COMPANY = "Readyhubb"
TITLE = "Growth Marketing Manager"
DATE_FOLDER = "2026-09-03"

JOB_DESCRIPTION = """\
Growth Marketing Manager — Readyhubb. Full-Time | Remote | SaaS / Beauty Tech. Dubai, UAE.
Readyhubb is a SaaS platform helping beauty professionals manage and grow their businesses.
We are looking for a data-driven and customer-obsessed Growth Marketer to drive acquisition,
activation, retention and revenue growth. This role sits at the intersection of Growth,
Marketing and Product, turning beauty professionals into active, paying customers.
What you'll do: develop and execute strategies to acquire new users and paid subscribers;
launch, manage and optimise paid acquisition campaigns across Meta, Google and other channels;
build campaigns to reactivate and convert the existing database of beauty professionals;
develop and test creator, affiliate, partnership and referral programmes; build and optimise
landing pages, funnels and offers to improve conversion; create email, CRM and lifecycle
campaigns across the customer journey; analyse the full funnel from acquisition → signup →
activation → paid subscription → retention; run continuous experiments across messaging,
creative, channels, onboarding, pricing and offers; identify drop-off points and work with
Product and Customer Success; track CAC, conversion, activation, retention, churn, subscriber
growth and MRR; scale the channels and experiments that perform; report weekly on growth
performance, experiments, learnings and next actions.
Who we're looking for: 4+ years hands-on growth, performance or digital marketing; experience
growing a SaaS, app, marketplace, subscription product or digital business; strong understanding
of acquisition, conversion, lifecycle marketing and retention; hands-on paid acquisition,
particularly Meta; experience with social media and influencer marketing; strong analytical
skills; strong copywriting and creative instincts; highly experimental; resourceful and able to
execute without relying on a large team or agency; comfortable in a fast-moving entrepreneurial
environment. Experience marketing to beauty professionals, SMBs, creators or service-based
businesses is a strong advantage.
"""

ATS = [
    "growth marketing", "growth marketer", "performance marketing", "digital marketing",
    "paid acquisition", "paid social", "Meta Ads", "Facebook Ads", "Instagram Ads",
    "Google Ads", "user acquisition", "activation", "retention", "lifecycle marketing",
    "CRM", "email marketing", "EDM", "reactivation", "referral programme",
    "partnership marketing", "creator marketing", "influencer marketing", "UGC",
    "landing pages", "funnels", "offers", "conversion rate optimisation", "CRO",
    "A/B testing", "experimentation", "growth experiments", "full-funnel analysis",
    "signup", "onboarding", "churn", "subscriber growth", "CAC", "ROAS", "ROI", "CPA",
    "conversion rate", "AOV", "GMV", "KPI reporting", "cohort", "marketplace",
    "SaaS", "subscription", "digital business", "SMB", "beauty professionals",
    "beauty", "copywriting", "Shopify", "social media", "TikTok", "Instagram",
    "Dubai", "UAE", "remote",
]

CONTENT = {
    "headline": (
        "Growth Marketing Manager · Paid Acquisition (Meta & Google) · Activation, Lifecycle & Retention · "
        "Beauty, Marketplace & E-Commerce"
    ),
    "professional_summary": (
        "Growth marketer with 5 years across marketplaces, e-commerce and consumer brands. Runs Meta and "
        "Google acquisition end-to-end, owns the Shopify funnel (landing pages, offers, CRO) and lifecycle "
        "email, and spent two years acquiring and activating beauty businesses. Dubai-based, available remote."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Consumer brands (Befit, Eurocake, Flair) | Shopify D2C + marketplaces | 50+ countries",
            "bullets": [
                "Run paid acquisition on Meta (Facebook & Instagram) and Google Ads end-to-end — audiences, creative and messaging A/B tests, budget reallocated on ROI/ROAS, weekly readout on what to kill, iterate or scale",
                "Own the Shopify funnel from ad to checkout — landing pages, offers, merchandising, UX and EDM/lifecycle campaigns — lifting conversion rate (CRO) and average order value through continuous testing",
                "Built the creator programme from zero (25–50 creators briefed and negotiated per campaign, plus seeding) and an AI automation system cutting manual work ~40%, so experiments ship fast with no agency and no big team",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Acquired and activated small beauty businesses on the platform: onboarded 30+ new stores in two months as PIC Fragrances, taking them from signup to actively selling via tailored offers and promo mechanics",
                "Grew 42 beauty, fragrance and fashion accounts +30% GMV QoQ, testing pricing, offers and campaigns against traffic, conversion, ROI/ROAS and retention data",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce marketplace | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Part of the team that built Glovo's retail vertical from scratch — acquiring and onboarding new brand partners onto the marketplace and growing order volume and GMV through data-led activations",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Category planning & analytics",
            "bullets": [
                "Measured promotional effectiveness and sell-in/sell-out performance — the discipline behind deciding which experiments deserve budget",
            ],
        },
    ],
    "skills_brand": (  # label -> "Growth & Acquisition"
        "full-funnel growth (acquisition → activation → retention), paid acquisition, offers & promo mechanics, "
        "reactivation, creator & partnership programmes, experimentation, copywriting"
    ),
    "skills_ecommerce": (  # label -> "Performance & Lifecycle"
        "Meta Ads (Facebook & Instagram), Google Ads, audience building, creative A/B testing, "
        "landing pages & funnels, CRO, EDM / CRM lifecycle, Shopify"
    ),
    "skills_commercial": (  # label -> "Customers & Partners"
        "SMB & merchant acquisition, onboarding & activation, influencer programmes (25–50 creators/campaign), "
        "creator negotiation, sampling & seeding, beauty & fragrance category"
    ),
    "skills_data": (  # label -> "Analytics & Reporting"
        "conversion & funnel analysis, retention, ROAS, ROI, CPA, AOV, GMV, drop-off diagnosis, "
        "A/B test readouts, weekly KPI reporting"
    ),
    "skills_tools": (  # label -> "Tools"
        "Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, Power BI, Tableau, Looker, "
        "Salesforce, Canva, Adobe, Generative AI (Claude, ChatGPT)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Growth & Acquisition",
    "E-Commerce & Digital": "Performance & Lifecycle",
    "Commercial": "Customers & Partners",
    "Data & Analytics": "Analytics & Reporting",
}


def make_job() -> Job:
    return Job(
        id="readyhubb-growth-marketing-manager-dubai-remote-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (Remote)",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Readyhubb Growth Marketing Manager Dubai remote SaaS beauty tech",
            "note": "SaaS platform for beauty professionals. Posted ~1 week ago, promoted by recruiter, "
                    "responses handled OUTSIDE LinkedIn. 403 applicants (49 in the last day) — heavy "
                    "competition. LinkedIn flags Paula as a top-match on the must-haves. Real gap: no SaaS "
                    "/ subscription ownership (MRR, churn, CAC payback) — do NOT imply it. Remote role, "
                    "which sits outside her stated preference.",
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
        "ai_score": 72, "ai_tier": "Warm",
        "skills_match": [
            "Hands-on paid acquisition on Meta (FB/IG) and Google Ads — audiences, creative A/B testing, ROI/ROAS optimisation (the JD's 'particularly Meta')",
            "Marketing to beauty professionals and SMBs — the JD's 'strong advantage': 42 beauty/fragrance/fashion accounts and 30+ new stores acquired and activated in two months at Miravia",
            "Creator/influencer programme built from zero, 25–50 creators briefed and negotiated per campaign — covers the creator/partnership lever",
            "Funnel ownership: Shopify store end-to-end (landing pages, offers, CRO, AOV) plus EDM/lifecycle campaigns",
            "Marketplace/platform growth: Miravia (Alibaba) and Glovo's retail vertical build-out — acquiring partners and getting them transacting",
            "Resourceful solo operator: AI automation system cutting manual workload ~40%, so she ships experiments without an agency",
            "5 years experience vs the 4+ asked",
        ],
        "missing_skills": [
            "No SaaS experience and no subscription-metric ownership — never ran MRR, churn, CAC payback or paid-subscriber growth",
            "Her funnel is transactional e-commerce (GMV, AOV, repeat purchase), not signup → activation → paid subscription",
            "No affiliate-programme experience specifically (creator and partnership work, yes; affiliate, no)",
            "No formal Growth title — growth work sits inside brand/e-commerce and KAM roles",
        ],
        "sector_fit": "adjacent — beauty vertical is a direct hit, SaaS/beauty-tech product model is new to her",
        "seniority_fit": "good — 5 years hands-on vs 4+ asked, and the role is an execution-heavy IC/manager hybrid",
        "red_flags": [
            "403 applicants (49 in a single day) — very crowded",
            "Applications handled outside LinkedIn by a recruiter — limited process visibility",
            "No salary published — confirm against the AED 20K/month floor",
            "Remote role, outside Paula's stated preference (remote_ok: false in profile.yaml)",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong-adjacent fit. Readyhubb sells software to beauty professionals, and the one line in the "
            "JD marked 'strong advantage' — experience marketing to beauty professionals, SMBs, creators or "
            "service businesses — is precisely what Paula did for two years at Miravia, where she acquired "
            "and activated small beauty and fragrance merchants and grew 42 accounts +30% GMV QoQ. On top of "
            "that she runs Meta and Google acquisition hands-on, owns a Shopify funnel with landing pages, "
            "offers and CRO, runs EDM/lifecycle, and briefs 25–50 creators per campaign — four of the five "
            "levers this job pulls. The honest gap is the product model: she has never owned subscription "
            "metrics (MRR, churn, CAC payback, paid-subscriber growth) or worked in SaaS, so the CV leads on "
            "acquisition, activation and the beauty-SMB customer, and claims no SaaS or subscription "
            "ownership. With 403 applicants, the differentiator to push in outreach is the beauty-professional "
            "customer knowledge plus the fact that she can build the whole funnel alone."
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
