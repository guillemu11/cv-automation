"""One-off: generate Paula's ENGLISH CV tuned for the micro1 "Marketing Domain
Expert" (remote AI-training contractor) role.

Unlike the rest of the pipeline (Dubai Brand/Marketing-Manager roles), this is a
remote contractor gig producing AI *training data* from real marketing expertise.
The JD's required skills are: Enterprise Marketing, Business Writing, Prompt
Engineering, Analytical Reasoning, Microsoft 365, Content Strategy, and AI
Response Evaluation.

Paula is an unusually strong *honest* fit because her stand-out differentiator —
being an AI-first marketer who actually builds and operates a generative-AI
(Claude/GPT) marketing system — maps almost 1:1 onto "prompt engineering" and "AI
response evaluation", while her 4+ years of enterprise marketing across FMCG,
beauty, fashion and e-commerce cover the domain, business-writing and
content-strategy pillars. Microsoft Office is already "Expert" on her profile.

Nothing is invented:
- "Prompt engineering" / "AI response evaluation" = she genuinely designs, tests
  and iterates prompts and reviews/QA-s AI outputs before use (profile: DoFreeze
  AI automation system on Claude/generative AI).
- "Enterprise marketing" = FMCG (DoFreeze, Mondelez), top-5 e-commerce (Miravia/
  Alibaba, 100K+ employees), quick-commerce (Glovo).
- "Business writing / content strategy" = campaign plans, stakeholder comms,
  reports, decks, landing pages, project documentation she already produces.
- "Microsoft 365" = profile lists Microsoft Office (Expert).

Fills the real CV template, converts to PDF via LibreOffice, and lands the
package under output/2026-08-16/. No dashboard registration (off-target gig, not
part of the Dubai pipeline).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "micro1"
TITLE = "Marketing Domain Expert"
DATE_FOLDER = "2026-08-16"

JOB_DESCRIPTION = """\
Marketing Domain Expert — micro1 (AI data lab). Contractor, Remote. $10-40/hour.

Required skills: Enterprise Marketing, Business Writing, Prompt Engineering,
Analytical Reasoning, Microsoft 365, Content Strategy, AI Response Evaluation.

Apply your marketing expertise to train next-generation AI systems; no prior AI
experience required. Responsibilities: develop realistic AI training data centred
on marketing workflows and business-productivity scenarios; produce high-quality
marketing content (campaign plans, stakeholder communications, reports,
presentations, project documentation) reflecting best practice; review fictional
company contexts to write authentic user prompts and ideal AI responses; generate
follow-up recommendations and assess the quality of AI responses; apply structured
thinking and analytical reasoning to guide training data; use Microsoft 365 (Word,
Excel, PowerPoint, Outlook, Teams, OneNote, SharePoint). Preferred: product
marketing / project / knowledge management; familiarity with AI training, data
annotation or evaluating AI-generated content; enterprise-team support.
"""

CONTENT = {
    "headline": (
        "Enterprise Marketing Expert · Generative-AI (Claude/GPT) Prompt Engineering & "
        "AI Response Evaluation · Content Strategy & Business Writing · Analytical Reasoning · Microsoft 365"
    ),
    "professional_summary": (
        "Enterprise marketing professional with 4+ years across FMCG, beauty, fashion and e-commerce, and an "
        "early, hands-on adopter of generative AI at work. Builds and operates a production AI marketing system "
        "on Claude and GPT — designing, testing and iterating prompts (prompt engineering) and reviewing, scoring "
        "and QA-ing AI-generated outputs for accuracy, relevance and best-practice quality (AI response "
        "evaluation) — to automate campaign planning, content, market research, KPI reporting and client-ready "
        "decks. Produces high-quality enterprise marketing content end-to-end: campaign plans, stakeholder "
        "communications, performance reports, presentations and project documentation reflecting genuine category "
        "best practice. Applies structured, analytical reasoning to marketing decisions and is an expert Microsoft "
        "365 user (Word, Excel, PowerPoint, Outlook, Teams, OneNote, SharePoint). Works independently and to a "
        "high standard in a fully remote, multi-market setting across 50+ countries."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (AI-First Marketing)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE (remote, multi-market)",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Built and operate a production AI marketing system on generative AI (Claude / GPT) — designing, "
                "testing and iterating prompts (prompt engineering) and reviewing, scoring and QA-ing the AI's "
                "outputs for accuracy, relevance and best-practice quality (AI response evaluation) before use — "
                "automating campaign planning, content, market research, KPI reporting and client-ready decks and "
                "landing pages, cutting manual workload ~40%",
                "Produce high-quality enterprise marketing content end-to-end — campaign plans, go-to-market "
                "briefs, stakeholder communications, performance reports, presentations and project documentation "
                "— reflecting real category best practice across 50+ GCC/MENA/global markets",
                "Lead NPD end-to-end for 6 product launches (brief, packaging, pricing, go-to-market), running "
                "the structured, cross-functional marketing workflows an enterprise team relies on",
                "Apply structured, analytical reasoning to marketing decisions — translating sell-out, ROI/ROAS "
                "and market data into clear, prioritised recommendations and follow-up actions",
                "Run the day-to-day on Microsoft 365 (Word, Excel, PowerPoint, Outlook, Teams, SharePoint) for "
                "content development, reporting and documentation — working independently in a fully remote setup",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce | 100K+ employees (enterprise environment)",
            "bullets": [
                "Operated inside a large enterprise (100K+ employees), managing 42 key accounts and growing GMV "
                "+30% QoQ — realistic enterprise marketing and commercial workflows at scale",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting directly to the CEO — writing "
                "the strategic commercial plans, business cases and executive-ready reports the role documents",
                "Created and led the Beauty Club and Hot on Social content programmes, defining content strategy "
                "that boosted visibility, loyalty and positioned Miravia as a beauty and lifestyle destination",
                "Continuously analysed conversion, traffic, retention, ROI and ROAS, turning performance data into "
                "structured recommendations and forecasting — the analytical reasoning this role centres on",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Led cross-functional teams across marketing, logistics and customer support to deliver campaigns "
                "and activations — coordinating the multi-stakeholder workflows enterprise scenarios simulate",
                "Managed strategic key accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) with data-led planning "
                "and bespoke marketing activations, driving GMV growth",
                "Negotiated and closed high-impact commercial deals, producing the proposals and stakeholder "
                "communications that underpinned each agreement",
            ],
        },
        {
            "company": "Mondelez International · earlier: Massimo Dutti (Inditex)",
            "role": "Category Planning Trainee (FMCG) & Premium Fashion Retail",
            "dates": "2018 – 2022",
            "location": "Madrid, Spain",
            "context": "Mondelez global FMCG (€36B) + Inditex premium fashion retail",
            "bullets": [
                "Mondelez: ran sell-in/sell-out analysis, evaluated promotional effectiveness and built performance "
                "reports for the chocolate category — structured analytical reasoning and business writing turning "
                "data into recommendations, contributing to NPD launches (Milka Spread, Mini Suchard)",
                "Inditex / Massimo Dutti: hands-on premium fashion retail — visual merchandising, product flow and "
                "customer experience — grounding her enterprise brand and content work in real retail practice",
            ],
        },
    ],
    "skills_brand": (
        "Enterprise marketing operations, content strategy, business writing, campaign planning & go-to-market, "
        "stakeholder communications, marketing reports & presentations, project documentation, NPD workflows "
        "end-to-end, brand strategy, trade & shopper marketing"
    ),
    "skills_ecommerce": (
        "Generative-AI marketing workflows, prompt engineering, AI response evaluation & QA, AI-assisted content "
        "production, marketing automation, Shopify e-store, conversion rate optimisation (CRO), Meta Ads, Google "
        "Ads, quick-commerce (Noon, Talabat, Careem, Deliveroo)"
    ),
    "skills_commercial": (
        "Key account management, pricing strategy, assortment & category planning, negotiation, forecasting, "
        "P&L awareness, distributor & partner management, modern trade"
    ),
    "skills_data": (
        "Structured analytical reasoning, evaluating content for clarity / accuracy / impact, sell-in/sell-out "
        "analysis, KPI tracking, ROI, ROAS, GMV, forecasting, AI-assisted analysis, Power BI, Tableau, Looker, "
        "Nielsen"
    ),
    "skills_tools": (
        "Microsoft 365 — Word, Excel, PowerPoint, Outlook, Teams, OneNote, SharePoint (Expert); Generative AI "
        "(Claude, ChatGPT); Shopify; Meta Ads Manager; Google Ads; Salesforce; Power BI; Tableau; Canva"
    ),
}


def make_job() -> Job:
    return Job(
        id="micro1-marketing-domain-expert-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Remote",
        url="https://micro1.ai",
        source="direct",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing Domain Expert micro1",
             "type": "Contractor · Remote · AI training data",
             "note": "Off-target vs Dubai pipeline — supplemental remote gig"},
    )


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (docx2pdf/Word is unreliable here)."""
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


def _relocate_to_dated_folder(pos_dir: Path):
    from career_ops.config import settings
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
    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
