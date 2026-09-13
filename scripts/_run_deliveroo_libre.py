"""Runner: build the Deliveroo package DOCX and convert to PDF via LibreOffice.

docx2pdf (Word/AppleScript) is flaky on this Mac ("Mensaje incomprensible"),
so we drive LibreOffice headless instead. Keeps both DOCX (editable) and PDF
(final) in the package, then relocates it under the dated folder.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import _gen_deliveroo_brand_mm as gen  # noqa: E402  (scripts/ is on path)
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"


def to_pdf(docx: Path) -> Path:
    """Convert DOCX -> PDF via LibreOffice headless, keeping the DOCX."""
    subprocess.run(
        [SOFFICE, "--headless",
         "-env:UserInstallation=file:///tmp/lo_deliveroo_profile",
         "--convert-to", "pdf", "--outdir",
         str(docx.parent), str(docx)],
        check=True, capture_output=True, text=True,
    )
    pdf = docx.with_suffix(".pdf")
    if not pdf.exists():
        raise RuntimeError(f"LibreOffice did not produce {pdf}")
    return pdf


def main() -> None:
    job = gen.make_job()
    gen.register_in_dashboard(job)

    cv_docx = cv._fill_template(gen.CONTENT, job)
    cv_pdf = to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    cl_docx = cl._fill_template(gen.CL_PARAGRAPHS, job, contact_name=None)
    cl_pdf = to_pdf(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = gen._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
