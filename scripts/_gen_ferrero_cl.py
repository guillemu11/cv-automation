"""Follow-up to _gen_ferrero_brand_manager_bfy.py — brief cover letter for Ferrero
"Brand Manager - Better For You, Raffaello & Tablets" (Job ID 77585, Dubai). The posting asks for
the CV plus a *brief* cover letter, so this stays at ~4 short paragraphs, one page.

Honesty guardrails (same as the CV): forecast = "contribute", not own; no Arabic claimed; no ATL/TV
media; team of two stated exactly; Nielsen at Mondelez confirmed by Guille 2026-09-13.
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

COMPANY = "Ferrero"
TITLE = "Brand Manager - Better For You, Raffaello & Tablets"
DATE_FOLDER = "2026-09-13"
CONTACT = None  # No named hiring manager in the posting.

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I am applying for the Brand Manager role for Better For You, Raffaello and Tablets in Dubai. "
        "The portfolio brings together the three things I have worked on: chocolate, better-for-you "
        "snacking, and seasonal moments in the Gulf. I would like to bring that experience to your "
        "regional team."
    ),
    "body_paragraph_1": (
        "Today I run brand and marketing for DoFreeze, a UAE snacking group whose portfolio includes "
        "Befit, a sugar-free, fitness-led better-for-you brand. I have taken six products to market end "
        "to end, from brief and packaging to pricing and go-to-market, working with Sales, Supply Chain "
        "and Finance. I also built a seasonal calendar around Ramadan, Back to School, Fitness Month and "
        "New Year, measured on sell-out rather than reach: Befit x Noon \u201cNew Year, New Me\u201d "
        "added 4,176 incremental units (+31% vs baseline), and a SMASH x talabat creator campaign lifted "
        "daily sales by 165% while a control brand grew 4.7%."
    ),
    "body_paragraph_2": (
        "The rest of the brief is also familiar. I brief and manage four agencies on campaign assets and "
        "content, and negotiated their fees down by 30%. I track A&P spend against results and contribute "
        "promotional input to the monthly sell-in forecast. I lead and coach a team of two, a graphic "
        "designer and a social media executive, so developing an Assistant Brand Manager is part of how I "
        "already work. My grounding in chocolate comes from Mondelez, where I planned the category with "
        "Nielsen data, measured promotional effectiveness and supported the Milka Spread and Mini Suchard "
        "launches. Two years at Alibaba\u2019s Miravia marketplace, growing 42 brand accounts by +30% GMV "
        "QoQ, added the commercial discipline of reading the numbers every week."
    ),
    "closing_paragraph": (
        "I am based in Dubai and would welcome the chance to discuss how I would approach the Better For "
        "You, Raffaello and Tablets plans for the Gulf. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="ferrero-77585-brand-manager-bfy-raffaello-tablets",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (Hybrid)",
        url="https://www.ferrerocareers.com/",
        source="manual",
        description="See _gen_ferrero_brand_manager_bfy.py for the full JD.",
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
        raise SystemExit(f"Package folder missing — run _gen_ferrero_brand_manager_bfy.py first: {final_dir}")

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
