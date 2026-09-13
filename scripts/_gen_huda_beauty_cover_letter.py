"""One-off: generate Paula's COVER LETTER for Huda Beauty
"Senior Global Brand Marketing Manager - Fragrance" (Dubai).

Pairs with _gen_huda_beauty_sr_global_brand_mm_fragrance.py (the CV). Same Job,
same honest positioning. Addressed to "Hiring Team" (no named contact known).
Authored directly (no LLM key in repo), strictly truthful:
  - foregrounds real 360°/NPD/influencer/experiential craft (DoFreeze) + genuine
    fragrance/prestige-beauty grounding (Miravia: Beauty & Fragrances category,
    Arabian oud houses);
  - is candid that fragrance depth is commercial/e-commerce + brand-side launches
    in beauty/FMCG, not prestige-fragrance brand-launch tenure;
  - references her self-built Huda Beauty "360° Launch" concept as a genuine asset;
  - NO "no sponsorship needed" claim (employer-sponsored UAE residence visa) — only
    "already based in Dubai, no relocation timeline".

Converts to PDF via LibreOffice (soffice headless) and lands next to the CV under
output/2026-08-27/Huda Beauty - .../01_CV_y_Carta/.
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

COMPANY = "Huda Beauty"
TITLE = "Senior Global Brand Marketing Manager - Fragrance"
DATE_FOLDER = "2026-08-27"
CONTACT = "Hiring Team"  # -> "Dear Hiring Team,"

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Huda Beauty has always felt different — a Dubai-born brand that Huda Kattan built in 2013 into one of the "
        "world's fastest-growing beauty powerhouses by leading with purpose over profit and an unwavering belief in "
        "kindness. Bringing that same instinct to fragrance — where a scent has to carry a story people fall in love "
        "with — is exactly the challenge I want. As a Brand & Marketing Manager based here in Dubai, building 360° "
        "launches across beauty and FMCG, the Senior Global Brand Marketing Manager – Fragrance role reads like the "
        "brief I have been working toward."
    ),
    "body_paragraph_1": (
        "Taking products from concept to market is what I do day to day. At DoFreeze I lead 360° launch campaigns "
        "end-to-end across 50+ markets — owning NPD for six launches from concept positioning and creative brief "
        "through global go-to-market, defining the messaging hierarchy and key selling points, and building the "
        "launch toolkit (campaign messaging, retailer and e-commerce assets, paid media, education and sampling). I "
        "built our influencer programme from zero to 25–50 creators per campaign, with influencer guidelines, "
        "product seeding and sampling that turn a launch into social-first storytelling and measurable sell-out — "
        "the experiential, PR and creator muscle this role runs on."
    ),
    "body_paragraph_2": (
        "My grounding in fragrance and prestige beauty comes from Alibaba's Miravia, where I owned the Beauty & "
        "Fragrances category across 42 accounts and grew GMV +30% QoQ, and — as PIC Fragrances — onboarded the "
        "official distributors of leading Arabian and oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal), "
        "building real fluency in the premium fragrance landscape and how these consumers buy. I'll be candid that "
        "this depth has been on the commercial and e-commerce side of fragrance rather than leading prestige-"
        "fragrance brand launches, and my brand-side launch record is in beauty and FMCG — but the 360° craft, the "
        "olfactive-to-narrative storytelling and the cross-functional project management transfer directly, and I "
        "ramp fast. I'm AI-first in how I plan campaigns and content, and already based in Dubai on a UAE residence "
        "visa, so there's no relocation timeline. I was excited enough by the brand to build a 360° launch concept "
        "for a Huda Beauty hero product — I'd love to share it."
    ),
    "closing_paragraph": (
        "I would love to bring this blend of 360° launch execution, fragrance-category fluency and creator-led "
        "storytelling to Huda Beauty's fragrance ambitions. I'm in Dubai, available to start quickly, and would "
        "welcome the chance to talk through how I'd take a fragrance from concept to a launch people remember. Thank "
        "you for reading — I hope we get to speak."
    ),
}


def make_job() -> Job:
    return Job(
        id="huda-beauty-sr-global-brand-mm-fragrance-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/view/huda-beauty-senior-global-brand-marketing-manager-fragrance",
        source="linkedin",
        description="Senior Global Brand Marketing Manager - Fragrance (Huda Beauty, Dubai).",
        raw={"function": "Brand Marketing", "category": "Fragrance / Prestige beauty"},
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
    return cl._to_pdf(docx_path)


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
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)
    final_dir = _relocate_to_dated_folder(cl_pdf.parent.parent)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
