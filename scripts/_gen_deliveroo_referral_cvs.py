"""One-off: generate Paula's TWO referral CVs for her Deliveroo contact (2026-08-27).

A Deliveroo insider offered to refer Paula internally and asked for two CVs:
  1. A MARKETING-angled CV   -> reuse _gen_deliveroo_brand_mm.CONTENT (brand /
     integrated campaigns end-to-end)
  2. A KEY-ACCOUNT-angled CV -> reuse _gen_deliveroo_account_manager.CONTENT
     (account / key account management, quick-commerce & food delivery)

These are REFERRAL CVs, not tied to one specific job req — the contact circulates
them internally — so we reuse the already-authored, strictly-truthful content
(NO invented experience, Arabic never claimed) and give the PDFs clean,
human-readable filenames Paula can forward as-is.

Fills the real CV template, converts DOCX -> PDF with LibreOffice headless
(docx2pdf/Word is unreliable on this Mac), and lands both under
output/2026-08-27/Deliveroo - Referral (Marketing + Key Account)/01_CV_y_Carta/.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))  # import sibling _gen_* modules

from career_ops.config import settings
from career_ops.discovery.normalize import Job

# Land everything under today's dated folder (generators write to settings.output_dir)
settings.output_dir = ROOT / "output" / "2026-08-27"
settings.output_dir.mkdir(parents=True, exist_ok=True)

from career_ops.generators import cv_generator as cv  # noqa: E402

import _gen_deliveroo_brand_mm as brand           # noqa: E402  (reuse CONTENT)
import _gen_deliveroo_account_manager as am        # noqa: E402  (reuse CONTENT)

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

# Referral folder — one package holding both CVs
FOLDER = "Deliveroo - Referral (Marketing + Key Account)"

# Slightly de-JD'd headlines so each CV reads as a general track CV, not a single
# req. Content bodies stay exactly as authored (truthful, ATS-strong).
MARKETING = dict(brand.CONTENT)
MARKETING["headline"] = (
    "Brand & Marketing Manager · Integrated Campaigns End-to-End · "
    "Quick-Commerce & Delivery · Dubai / UAE / MENA"
)

KEY_ACCOUNT = dict(am.CONTENT)
KEY_ACCOUNT["headline"] = (
    "Key Account & Partner Management · Quick-Commerce & Food Delivery · "
    "Data-Driven Growth · Dubai / UAE"
)

# (content, clean filename stem)
CVS = [
    (MARKETING, "Marketing Profile (Brand & Campaigns)"),
    (KEY_ACCOUNT, "Key Account Profile"),
]


def make_job(role_label: str) -> Job:
    """A referral 'job' just carries the label used for the template + filename."""
    return Job(
        id=f"deliveroo-referral-{role_label.lower().replace(' ', '-')}-2026-08-27",
        title=role_label,
        company="Deliveroo",
        location="Dubai, United Arab Emirates",
        url="https://careers.deliveroo.co.uk/locations/united-arab-emirates/",
        source="referral",
        description="Referral CV — internal circulation by a Deliveroo contact.",
        raw={"via": "Deliveroo employee referral"},
    )


def to_pdf(docx: Path) -> Path:
    subprocess.run(
        [SOFFICE, "--headless",
         "-env:UserInstallation=file:///tmp/lo_deliveroo_referral_profile",
         "--convert-to", "pdf", "--outdir", str(docx.parent), str(docx)],
        check=True, capture_output=True, text=True,
    )
    pdf = docx.with_suffix(".pdf")
    if not pdf.exists():
        raise RuntimeError(f"LibreOffice did not produce {pdf}")
    return pdf


def strip_trailing_blank_pages(pdf: Path) -> int:
    """Drop trailing pages with no extractable text (overflow artifacts).

    The AM-track content slightly overflows the template, leaving an empty final
    page — fine to ship on a job application, sloppy on a CV a contact forwards.
    Only removes trailing pages whose extracted text is empty; content pages
    always carry experience/skills text, so this never cuts real content.
    """
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(str(pdf))
    keep = list(range(len(reader.pages)))
    while len(keep) > 1 and not (reader.pages[keep[-1]].extract_text() or "").strip():
        keep.pop()
    removed = len(reader.pages) - len(keep)
    if removed:
        writer = PdfWriter()
        for i in keep:
            writer.add_page(reader.pages[i])
        with pdf.open("wb") as fh:
            writer.write(fh)
    return removed


def main() -> None:
    for content, stem in CVS:
        job = make_job(stem)
        docx = cv._fill_template(content, job)
        pdf = to_pdf(docx)
        removed = strip_trailing_blank_pages(pdf)
        # Rename to a clean, forwardable filename
        clean = pdf.parent / f"Paula De Francisco - CV - {stem}.pdf"
        pdf.replace(clean)
        # Drop the intermediate DOCX so the folder only holds the shareable PDFs
        docx.unlink(missing_ok=True)
        print("OK_CV", stem, f"(-{removed} blank pg)" if removed else "", "->", clean)


if __name__ == "__main__":
    main()
