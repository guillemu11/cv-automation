"""One-off: generate Paula's COVER LETTER for Arla
"Market Category Expert" / Category Development Manager (Dubai, MEA — FMCG dairy).

Pairs with _gen_arla_market_category_expert.py (the CV). Same Job, same honest
positioning. Addressed to "Hiring Team" (no named contact). Authored directly,
strictly truthful:
  - foregrounds real category-planning foundation (Mondelez: Nielsen, sell-in/
    sell-out, promo effectiveness, planogram, assortment gap, NPD) + category
    ownership (Miravia) + 4P/NPD/promo-menu/business-cases (DoFreeze);
  - candid about the two real gaps — no dairy-specific tenure (FMCG food/beauty,
    adjacent) and 4+ vs the JD's 6 years — while showing the 4P/NRM/Nielsen muscle
    transfers directly;
  - NO "no sponsorship needed" claim (employer-sponsored UAE residence visa) — only
    "already based in Dubai, no relocation timeline".

Converts to PDF via LibreOffice (soffice headless) and lands next to the CV under
output/2026-08-27/Arla - Market Category Expert/01_CV_y_Carta/.
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

COMPANY = "Arla"
TITLE = "Market Category Expert"
DATE_FOLDER = "2026-08-27"
CONTACT = "Hiring Team"  # -> "Dear Hiring Team,"

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "There's something I admire about a business that stays farmer-owned while building brands the whole region "
        "reaches for — Puck and Lurpak are fixtures of the Middle Eastern kitchen, and Arla's invitation to 'shape "
        "the future of dairy' is exactly the kind of category challenge I want. As a category and commercial "
        "manager based in Dubai, working across FMCG in this market every day, the Market Category Expert role "
        "reads like the brief I've been building toward: turning regional strategy into local category growth that "
        "resonates with our customers, consumers and shoppers."
    ),
    "body_paragraph_1": (
        "Category work is the spine of my career. I built the foundation at Mondelez, a global FMCG leader — "
        "running sell-in/sell-out and Nielsen analysis, evaluating promotional effectiveness and assessing "
        "planogram compliance and assortment gaps for the chocolate category, then supporting NPD from concept to "
        "shelf (Milka Spread, Mini Suchard). At Alibaba's Miravia I owned a category across 42 accounts and grew "
        "GMV +30% QoQ through assortment, pricing, margin and a data-led promotional calendar. Today at DoFreeze I "
        "own category and the 4P across 50+ markets — localising toolkits and trade decks, designing promo menus by "
        "channel, leading NPD end-to-end and building bottom-up business cases to unlock growth."
    ),
    "body_paragraph_2": (
        "The way this role works is the way I work: shopper and consumer understanding turned into strategic "
        "direction, pricing and promotions optimised with a net-revenue mindset, and market presence driven "
        "through disciplined retail execution — all evidenced with Nielsen and EPOS/sell-out data. I'll be candid "
        "that my category depth has been in FMCG food and beauty rather than dairy specifically, and I'm at 4+ "
        "years against your six — but the 4P, NRM and Nielsen muscle transfers directly, I ramp fast on a new "
        "category, and I'm AI-first in how I pull insight and build decks. I'm also already based in Dubai on a UAE "
        "residence visa, so there's no relocation timeline."
    ),
    "closing_paragraph": (
        "I'd love to bring this blend of category-planning rigour, NPD and commercial execution to Arla's growth in "
        "the region. I'm in Dubai, available to start quickly, and happy to talk ahead of the 4 September close "
        "about how I'd localise the strategy, sharpen the 4P and turn shopper insight into category wins. Thank you "
        "for your consideration — I hope we get to speak."
    ),
}


def make_job() -> Job:
    return Job(
        id="arla-market-category-expert-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.arla.com/careers/market-category-expert",
        source="linkedin",
        description="Market Category Expert / Category Development Manager (Arla, Dubai, MEA).",
        raw={"function": "Category Development / Category Management", "sector": "FMCG dairy"},
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
