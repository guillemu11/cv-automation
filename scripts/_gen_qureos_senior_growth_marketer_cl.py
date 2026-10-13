"""One-off: cover letter for Qureos "Senior Growth Marketer" — reuses the job from
`_gen_qureos_senior_growth_marketer.py`. Addressed to the Qureos team (the role works directly with the founders;
no named contact).

The posting says "campaigns launched is not a result" and "we hire on what you have proven", so the letter opens
with a controlled test (SMASH x talabat vs the Befit control), then channels built from zero and a stop decision
(Google moved to Meta on break-even ROAS), then hands-on building with Claude. It names the B2B SaaS gap once,
plainly, and closes on the candidate side of their marketplace (Paula is job-hunting now).

Honesty guardrails (same as the CV): percentages and unit costs only — no absolute DoFreeze sales or campaign
costs in material sent outside. "From zero" only for the influencer channel and affiliates. Glovo is co-managed XL
accounts, not the Retail vertical. Miravia: 30+ sellers onboarded in two months.
"""
from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_qureos_senior_growth_marketer_cv",
    ROOT / "scripts" / "_gen_qureos_senior_growth_marketer.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.config import settings
from career_ops.generators import cover_letter as cl

CONTACT = "Qureos team"

PARAGRAPHS = {
    "opening_paragraph": (
        "Your posting says campaigns launched is not a result, so I will start with a test. This year we ran a "
        "purchase-to-enter cashback giveaway with talabat for SMASH, a new snack brand at DoFreeze in Dubai. Daily "
        "sales rose 165% during the campaign. Befit, our other brand on the same platform in the same weeks, without "
        "the campaign, moved 4.7%. That gap, not the reach, is what I reported, and it is the kind of work I want to "
        "do as your Senior Growth Marketer."
    ),
    "body_paragraph_1": (
        "Most of what I have built started from nothing. I took our influencer channel from zero to 103 creator "
        "activations at AED 81 per content piece, then audited the agency's own report and found reach that had been "
        "estimated rather than measured, and micro-creators performing 10 to 40 times the campaign average. I "
        "designed the Befit Crew affiliate programme with personal codes and tiered commissions. I also stop things: "
        "when break-even ROAS, net of marketplace commissions, showed Google could not clear the bar, I moved that "
        "budget to Meta, where an Advantage+ retargeting campaign returned 3.7x in its first week."
    ),
    "body_paragraph_2": (
        "I build it myself. My team is one designer and one social media executive, so I built a Claude-based system "
        "that runs our campaign planning, content and KPI reporting with about 40% less manual work, and our "
        "affiliate landing page with AI agents. On conversion, web orders grew 86% after I added reviews, rebuilt "
        "bundles from basket analysis and set up a replenishment flow. I have worked the supply side of two "
        "marketplaces: I onboarded 30+ sellers in two months at Alibaba's Miravia and co-managed XL restaurant "
        "accounts at Glovo. I have not run B2B SaaS demand generation, and I will not pretend I have. What I bring is "
        "the habit of setting the bar before the test and writing down why something stopped."
    ),
    "closing_paragraph": (
        "Hiring is a two-sided problem I would like to work on, and right now I know your candidate side first-hand. "
        "I have attached a one-page log of the experiments behind these numbers. I am based in Dubai and would be "
        "glad to talk."
    ),
}


def main() -> None:
    job = cvmod.make_job()
    final_dir = settings.output_dir / cvmod.DATE_FOLDER / f"{cvmod.COMPANY} - {cvmod.TITLE}"
    dest = final_dir / "01_CV_y_Carta"
    dest.mkdir(parents=True, exist_ok=True)

    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    stray = cl_docx.parent.parent
    cl_pdf = cvmod._to_pdf_soffice(cl_docx)

    # CL_Paula_* is the name the dashboard indexes; the clean name is the one to upload.
    moved = dest / cl_pdf.name
    shutil.move(str(cl_pdf), str(moved))
    shutil.copy(str(moved), str(dest / "Paula De Francisco - Cover Letter.pdf"))
    cl_docx.unlink(missing_ok=True)
    print("OK", moved.name, "PAGES", cvmod._pages(moved))

    # The template writes to output/<Company> - <Role>/ at the root; only ever remove that.
    if stray.exists() and stray.parent.resolve() == settings.output_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)


if __name__ == "__main__":
    main()
