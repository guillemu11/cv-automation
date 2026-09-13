"""Follow-up to _gen_sporty_talent_community_marketing.py — cover letter for Sporty Group's
general talent community (Marketing & Communications, remote-first, global). Short, one page.

Honesty guardrails (same as the CV): no iGaming/betting, CRM or app-install (UA) experience
claimed; team of two stated exactly; no visa/sponsorship claims; no Arabic.
"""
from __future__ import annotations

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

COMPANY = "Sporty Group"
TITLE = "Marketing & Communications"
DATE_FOLDER = "2026-09-13"
CONTACT = None  # Talent community — no named hiring manager.

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I would like to join Sporty's talent community for Marketing & Communications. I have spent "
        "my career marketing consumer platforms and brands where results are counted in orders and "
        "users, not impressions, and Sporty's mix of scale, speed and ownership is the environment "
        "where I do my best work."
    ),
    "body_paragraph_1": (
        "Today I run brand and marketing for DoFreeze, a UAE FMCG group selling in more than 50 markets. "
        "I measure campaigns against a control, not on reach: a SMASH x talabat creator campaign lifted "
        "daily sales by 165% while a control brand grew 4.7%, and Befit x Noon \u201cNew Year, New Me\u201d "
        "added 4,176 incremental units (+31% vs baseline). I built the influencer programme from zero, "
        "with 103 creator activations at AED 81 per content piece, and I run Meta and Google Ads with "
        "creative A/B testing. I lead a team of two, a designer and a social media executive, and manage "
        "four agencies. To move faster, I built a generative-AI system with Claude for planning, content "
        "and reporting that cut our manual work by around 40%."
    ),
    "body_paragraph_2": (
        "Before that I worked inside two high-growth consumer platforms. At Glovo I grew XL partners "
        "such as KFC and Taco Bell with in-app promotions and helped build the Retail vertical. At "
        "Alibaba's Miravia marketplace I grew 42 brand accounts by +30% GMV quarter on quarter, owned "
        "the Flash Sales channel reporting to the CEO and created community projects to drive loyalty. "
        "Both taught me to read the numbers weekly and adjust quickly. I am a native Spanish speaker with "
        "professional English, which could add value alongside your Real Madrid and LaLiga partnerships "
        "and your teams in South America."
    ),
    "closing_paragraph": (
        "I am happy to work remote-first with teams across time zones and would welcome a conversation when a "
        "marketing, growth or partnerships role opens up. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="sporty-group-talent-community-marketing-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Remote (Global)",
        url="https://job-boards.greenhouse.io/sportygroup",
        source="manual",
        description="See _gen_sporty_talent_community_marketing.py for the full posting.",
        raw={},
    )


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



def main() -> None:
    job = make_job()
    final_dir = settings.output_dir / DATE_FOLDER / f"{COMPANY} - {TITLE}"
    if not final_dir.exists():
        raise SystemExit(f"Package folder missing — run _gen_sporty_talent_community_marketing.py first: {final_dir}")

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)

    dest_dir = final_dir / "01_CV_y_Carta"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_cl = dest_dir / cl_pdf.name
    shutil.move(str(cl_pdf), str(dest_cl))
    short = dest_dir / "Paula De Francisco - Cover Letter.pdf"
    shutil.copy(str(dest_cl), str(short))
    print("OK_CL", short)

    stray = cl_pdf.parent.parent
    if stray.exists() and stray.resolve() != final_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(dest_cl)).pages)
        print(f"CL_PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)


if __name__ == "__main__":
    main()
