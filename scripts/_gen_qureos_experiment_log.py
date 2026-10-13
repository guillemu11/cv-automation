"""One-off: one-page "Growth experiment log" PDF for the Qureos Senior Growth Marketer application ("additional
files"). Qureos describes its experiment engine as bets with a hypothesis, a budget, a time box and a bar to clear,
documented so nobody retests them; this page shows Paula already works that way, with five real DoFreeze tests.

Sources: memory paula-influencer-real-work (SMASH x talabat vs Befit control, agency audit, micro-creators),
profile.yaml DoFreeze highlights (break-even ROAS, Advantage+, giveaway follower cost, web store, bundles).

Guardrails: percentages and unit costs only — no absolute DoFreeze sales, budgets or campaign costs leave the
company. Where the outcome is a first read or changes shipped together, the page says so instead of over-claiming.

Rendered HTML -> PDF with headless Chrome (A4). Lands in 02_Deliverables/ as Deliverable_Paula_Qureos_* (the name
the dashboard indexes) plus a clean-named copy to upload.
"""
from __future__ import annotations

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings

DATE_FOLDER = "2026-10-13"
FOLDER = "Qureos - Senior Growth Marketer"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# (experiment, bet, setup & bar, result, call / learning)
EXPERIMENTS = [
    ("Creators + purchase-to-enter giveaway (SMASH x talabat), May–Jul 2026",
     "Creators plus a cashback draw tied to purchase move sell-out, not just reach.",
     "Control: Befit, same platform and weeks, no campaign. Bar: lift well above control.",
     "Daily sales +165% (units +170%) vs +4.7% for the control. Still about 2x baseline after the campaign.",
     "Report incremental sales against a control, never reach."),
    ("Google Ads vs Meta budget",
     "Search earns its share of the paid budget.",
     "Break-even ROAS per brand and channel, net of marketplace commissions. Bar: above break-even.",
     "Google's return did not cover the cost.",
     "Stopped Google; moved the budget to Meta."),
    ("Influencer agency report audit (3 waves, 103 creators)",
     "The agency's reach and 'unique accounts' figures are reliable enough to plan on.",
     "Read the agency's report line by line, creator by creator, across the three waves.",
     "Reach estimated from followers, not measured; one creator 5x apart between waves; unique accounts double-counted. "
     "Micro-creators (<20K) at 10–40x the campaign average.",
     "Negotiated −30% with the agency; 103 creators delivered vs 75 contracted."),
    ("Giveaway vs promoted reel for follower growth (@eurocake.ae)",
     "A giveaway grows a brand account more cheaply than paid promotion.",
     "Cost per net new follower, compared with a promoted reel.",
     "AED 0.73 per net follower, 8x cheaper than the promoted reel.",
     "For follower growth, the giveaway beat paid promotion 8x on cost."),
    ("Web store conversion (Shopify)",
     "Reviews, bundles built from real baskets and a replenishment reminder lift orders.",
     "Basket analysis first: 73% of orders already had 2+ products. Read: Q1 vs Jun–Aug 2026.",
     "Retail web orders +86%, revenue +57%.",
     "Not isolated: three changes shipped together, so the lift is shared between them."),
]

CSS = """
@page { size: A4; margin: 14mm 13mm; }
* { box-sizing: border-box; }
body { font-family: 'Lato', 'Helvetica Neue', Arial, sans-serif; color: #1e1e1e; font-size: 9.6pt; line-height: 1.35; margin: 0; }
h1 { font-size: 17pt; color: #2b3a4a; margin: 0 0 2px; }
.sub { color: #555; margin: 0 0 4px; }
.meta { color: #777; font-size: 8.6pt; margin: 0 0 12px; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; }
th { text-align: left; font-size: 8.4pt; text-transform: uppercase; letter-spacing: .04em; color: #2b3a4a;
     border-bottom: 1.5px solid #2b3a4a; padding: 5px 6px; }
td { vertical-align: top; padding: 7px 6px; border-bottom: 1px solid #d9dde2; }
td.exp { font-weight: 700; color: #2b3a4a; }
td.res { font-weight: 600; }
col.c1 { width: 19%; } col.c2 { width: 19%; } col.c3 { width: 22%; } col.c4 { width: 21%; } col.c5 { width: 19%; }
.foot { margin-top: 12px; color: #666; font-size: 8.4pt; }
"""


def build_html() -> str:
    rows = "\n".join(
        "<tr>" + "".join(
            f'<td class="{cls}">{html.escape(text)}</td>'
            for cls, text in zip(("exp", "", "", "res", ""), exp)
        ) + "</tr>"
        for exp in EXPERIMENTS
    )
    p = settings.profile["personal"]
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Growth experiment log</title>
<style>{CSS}</style></head><body>
<h1>Growth experiment log</h1>
<p class="sub">Paula De Francisco Pérez · Brand &amp; Marketing Manager, DoFreeze (Dubai)</p>
<p class="meta">Five real tests from 2026. Each one: the bet, how it was judged, what happened and the call.<br>
{html.escape(p["email"])} · {html.escape(p["phone"])}</p>
<table><colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"><col class="c5"></colgroup>
<thead><tr><th>Experiment</th><th>Bet</th><th>Setup &amp; bar</th><th>Result</th><th>Call / learning</th></tr></thead>
<tbody>
{rows}
</tbody></table>
<p class="foot">Figures from DoFreeze's sales data (talabat, Noon, Shopify) and Meta Ads Manager, shown as percentages
and unit costs. Happy to walk through how each one was measured.</p>
</body></html>"""


def main() -> None:
    dest = settings.output_dir / DATE_FOLDER / FOLDER / "02_Deliverables"
    dest.mkdir(parents=True, exist_ok=True)
    html_path = dest / "experiment_log.html"
    html_path.write_text(build_html(), encoding="utf-8")

    pdf_path = dest / "Deliverable_Paula_Qureos_Growth-Experiment-Log.pdf"
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, capture_output=True, timeout=120,
    )
    html_path.unlink(missing_ok=True)
    shutil.copy(str(pdf_path), str(dest / "Paula De Francisco - Growth Experiment Log.pdf"))

    from pypdf import PdfReader
    print("OK", pdf_path.name, "PAGES", len(PdfReader(str(pdf_path)).pages))


if __name__ == "__main__":
    main()
