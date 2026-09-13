"""One-off: generate Paula's cover letter for Club L London "E-commerce Specialist".

Reuses the job defined in _gen_clubl_ecom_specialist.py. Paragraphs are authored
directly (no LLM API key in this repo) and kept strictly truthful — no invented
Arabic fluency, no invented platform tenure. Fills the real cover-letter template,
saves the DOCX and converts to PDF via LibreOffice (docx2pdf/Word is unreliable
headless in this environment), then relocates into the dated package.
"""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_clubl_cv", ROOT / "scripts" / "_gen_clubl_ecom_specialist.py"
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # no named contact yet → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Club L London has done something genuinely hard: turned accessible-luxury womenswear into a brand a "
        "global community of trend-setters actually waits on, with fresh collections dropping every week. Running "
        "the day-to-day trading behind that cadence — in the GCC, where I already live and work — is exactly the "
        "role I want. As an e-commerce and digital-trading marketer based in Dubai, with a career that started on "
        "the Inditex (Massimo Dutti) shop floor and runs through fashion e-commerce ever since, the E-commerce "
        "Specialist opening reads like it was written around what I do daily."
    ),
    "body_paragraph_1": (
        "At DoFreeze I own the D2C Shopify store end-to-end — catalogue, onsite merchandising, search, navigation, "
        "collections, promotions and checkout — running weekly trading plans, launches and promotions and lifting "
        "conversion (CRO) and average order value through data-led merchandising. Shopify is one of the exact "
        "platforms this role names. I also own localisation of content, campaigns and promotions across 50+ "
        "GCC/MENA and global markets, and I grow wholesale, distributor and marketplace partners across Noon, "
        "talabat, Careem and Deliveroo. Earlier, at Alibaba's Miravia marketplace, I ran the Beauty, Fragrances & "
        "Fashion category across 42 accounts and brand/wholesale partners, growing GMV +30% QoQ through weekly "
        "promotions and constant conversion, traffic and retention analysis — the trading rhythm this role lives on."
    ),
    "body_paragraph_2": (
        "Two things make me a natural fit. First, real fashion depth — Massimo Dutti (Inditex), Miravia's Fashion "
        "category, Glovo's fashion Retail vertical and a CUNEF thesis specialised in the Fashion Industry — so the "
        "product, the merchandising standards and the trend-led weekly drop are second nature. Second, I am already "
        "in Dubai on a UAE residence visa and fluent in the GCC market, so there is no relocation and no ramp-up on "
        "the local consumer. In full honesty, I am not an Arabic speaker (I am a native Spanish speaker with C1 "
        "English), which I know the role prefers — but I localise the GCC customer experience daily and would "
        "partner closely with native Arabic colleagues to keep the Arabic storefront to the standard the brand "
        "deserves. I am also AI-native: I built a generative-AI system that cut trading and reporting workload ~40%, "
        "meaning sharper, faster trading insights."
    ),
    "closing_paragraph": (
        "I would love to bring this blend of fashion instinct and D2C trading rigour to Club L London's GCC and "
        "Australia growth story. I am based in Dubai, available to start immediately, and would welcome the chance "
        "to talk through how I would approach your weekly trading calendar and wholesale partners. Thank you for "
        "your consideration — I look forward to hearing from you."
    ),
}


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


def main() -> None:
    job = cvmod.make_job()
    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    # Relocate into the dated package (same helper as the CV script)
    pos_dir = cl_pdf.parent.parent
    final_dir = cvmod._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
