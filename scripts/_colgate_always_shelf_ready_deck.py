#!/usr/bin/env python3
"""Always Shelf-Ready — Colgate UAE e-commerce pitch deck for Paula's
Colgate Ecommerce Manager application.

A 16:9 visual deck (11 slides) rendered HTML -> PDF via headless Chromium.
Reuses the landing_colgate brand system + assets. One-off build script
(mirrors scripts/_henkel_frizz_forecast_deck.py). Nothing is sent.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings  # noqa: E402

COLGATE_DIR = ROOT / "output" / "2026-06-11" / "Colgate-Palmolive - Ecommerce Manager"
DELIV = COLGATE_DIR / "02_Deliverables"
LANDING_ASSETS = DELIV / "landing_colgate" / "assets"
PAULA_PHOTO = ROOT / "templates" / "paula_photo.jpg"

BUILD_DIR = DELIV / "always_shelf_ready_deck"
BUILD_ASSETS = BUILD_DIR / "assets"
HTML_PATH = BUILD_DIR / "deck.html"

DECK_PDF = DELIV / "Deliverable_Paula_Colgate_Always-Shelf-Ready_Deck.pdf"

P = settings.profile["personal"]
CHANNEL_IMAGES = ["hero", "digitalshelf", "marketplace", "qcommerce", "retailmedia"]

CSS = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:1280px 720px;margin:0}
html,body{background:#fff}
body{font-family:'Inter',system-ui,sans-serif;color:#0e1726}
.slide{position:relative;width:1280px;height:720px;overflow:hidden;background:#fff;page-break-after:always}
.slide:last-child{page-break-after:auto}
.dark{background:#0e1726;color:#fff}
.redbg{background:linear-gradient(135deg,#fb0007,#c4161c);color:#fff}
.pad{position:absolute;inset:0;padding:74px 88px}
.red{color:#c4161c}
.eyebrow{font-family:'Poppins',sans-serif;font-weight:800;font-size:14px;letter-spacing:3px;text-transform:uppercase;color:#c4161c}
.wordmark{font-family:'Poppins',sans-serif;font-weight:900;letter-spacing:2px;font-size:18px}
.kicker{font-family:'Poppins',sans-serif;font-weight:800;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:#9aa3b0}
.h2{font-family:'Poppins',sans-serif;font-weight:900;font-size:50px;line-height:.98;letter-spacing:-1.5px;color:#0e1726}
.h2.on-dark{color:#fff}
.lead{font-size:18px;line-height:1.5;color:#41495a;max-width:760px}
.lead.on-dark{color:#cfd5de}
.pagenum{position:absolute;bottom:38px;right:60px;font-family:'Poppins',sans-serif;font-weight:900;font-size:40px;color:#fb0007}
ul.bullets{list-style:none;margin-top:8px}
ul.bullets li{position:relative;padding-left:24px;margin:14px 0;font-size:16px;line-height:1.45;color:#333d4d;max-width:600px}
ul.bullets li::before{content:"";position:absolute;left:0;top:8px;width:9px;height:9px;background:#fb0007;border-radius:50%}
ul.bullets li b{color:#0e1726}
table.ps{width:100%;border-collapse:collapse;margin-top:22px;font-size:14px}
table.ps th{background:#0e1726;color:#fff;text-align:left;padding:13px 16px;font-family:'Poppins',sans-serif;font-weight:800;font-size:12.5px;letter-spacing:.6px;text-transform:uppercase}
table.ps td{border-bottom:1px solid #eadede;padding:13px 16px;vertical-align:top;color:#222;line-height:1.4}
table.ps tr td:first-child{font-weight:700;color:#0e1726;width:250px}
table.ps b{color:#c4161c}
/* cover */
.cover-img{position:absolute;right:0;top:0;width:560px;height:720px;object-fit:cover}
.cover-fade{position:absolute;right:440px;top:0;width:320px;height:720px;background:linear-gradient(90deg,#c4161c,transparent)}
.cover-title{font-family:'Poppins',sans-serif;font-weight:900;font-size:104px;line-height:.86;letter-spacing:-3px;color:#fff}
.cover-tag{font-size:21px;color:#fff;margin-top:24px;max-width:540px;line-height:1.35;font-weight:500}
.cover-lockup{position:absolute;bottom:48px;left:88px;font-size:12px;color:rgba(255,255,255,.85);letter-spacing:.4px;line-height:1.6;z-index:3}
/* agenda */
.agenda-row{display:flex;align-items:baseline;gap:22px;padding:15px 0;border-bottom:1px solid #f0e3e3}
.agenda-num{font-family:'Poppins',sans-serif;font-weight:900;font-size:24px;color:#fb0007;width:48px}
.agenda-txt{font-family:'Poppins',sans-serif;font-weight:800;font-size:25px;color:#0e1726;letter-spacing:-.5px}
/* big idea key visual */
.bigidea{display:flex;gap:54px;align-items:center;height:100%;padding:74px 88px}
.bigidea-left{flex:1;max-width:560px}
.bigidea-left .t{font-family:'Poppins',sans-serif;font-weight:900;font-size:70px;line-height:.88;letter-spacing:-2px;color:#fff;margin:14px 0 22px}
.bigidea-left .lockup{margin-top:26px;color:#fff;font-size:19px;line-height:1.35;font-weight:600;opacity:.95}
.kv{position:relative;flex:0 0 420px;height:470px}
.kv-card{position:absolute;left:40px;top:60px;width:330px;background:#fff;border-radius:18px;padding:28px 30px;box-shadow:0 28px 70px rgba(0,0,0,.45)}
.kv-card .lbl{font-family:'Poppins',sans-serif;font-weight:800;font-size:13px;letter-spacing:2px;color:#5a6473}
.kv-card .val{font-family:'Poppins',sans-serif;font-weight:900;font-size:104px;line-height:.9;color:#fb0007}
.kv-card .state{font-family:'Poppins',sans-serif;font-weight:900;font-size:20px;letter-spacing:3px;color:#0e1726}
.kv-card .track{margin-top:16px;height:10px;border-radius:6px;background:#f0dada;overflow:hidden}
.kv-card .fill{height:100%;width:100%;background:linear-gradient(90deg,#00b5e2,#fb0007)}
.kv-card .rows{margin-top:18px}
.kv-card .r{display:flex;justify-content:space-between;font-size:13px;color:#41495a;padding:5px 0;border-top:1px solid #f3eaea}
.kv-card .r b{color:#0e1726}
/* how-it-works flow */
.flow{display:flex;align-items:stretch;gap:18px;margin-top:28px}
.flow .node{flex:1;background:#fff5f5;border-left:5px solid #fb0007;border-radius:8px;padding:18px}
.flow .node h4{font-family:'Poppins',sans-serif;font-weight:800;font-size:16px;margin-bottom:8px}
.flow .node p{font-size:13px;line-height:1.4;color:#41495a}
.two{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:24px}
.two .col h4{font-family:'Poppins',sans-serif;font-weight:800;font-size:19px;color:#0e1726;margin-bottom:6px}
.two .col .tagcol{font-size:12px;color:#c4161c;font-weight:700;letter-spacing:1px;text-transform:uppercase}
/* channel cards */
.cards5{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:28px}
.cc{border-radius:12px;overflow:hidden;background:#fff;border:1px solid #f0e3e3;box-shadow:0 8px 20px rgba(14,23,38,.06)}
.cc img{width:100%;height:118px;object-fit:cover;display:block}
.cc .body{padding:12px 13px}
.cc h4{font-family:'Poppins',sans-serif;font-weight:800;font-size:14px;margin-bottom:6px;color:#0e1726}
.cc p{font-size:11.5px;line-height:1.35;color:#41495a}
/* why paula */
.why-photo{position:absolute;right:0;top:0;width:470px;height:720px;object-fit:cover}
.why-quote{font-family:'Poppins',sans-serif;font-weight:800;font-size:24px;line-height:1.25;color:#0e1726;max-width:600px;margin-top:18px}
.skillrow{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}
.skillrow span{font-size:12px;font-weight:600;color:#0e1726;border:1px solid #e0c9c9;border-radius:999px;padding:7px 14px}
/* contact */
.contact-big{font-family:'Poppins',sans-serif;font-weight:900;font-size:170px;line-height:.85;letter-spacing:-5px;color:#fff}
.contact-line{font-size:18px;color:#fff;margin-top:8px;letter-spacing:.5px;opacity:.95}
"""


def html_doc(slides: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{slides}
</body>
</html>"""


def stage_assets() -> None:
    if not LANDING_ASSETS.is_dir():
        raise FileNotFoundError(f"Landing assets not found: {LANDING_ASSETS}")
    if not PAULA_PHOTO.exists():
        raise FileNotFoundError(f"Paula's photo not found: {PAULA_PHOTO}")
    BUILD_ASSETS.mkdir(parents=True, exist_ok=True)
    for name in CHANNEL_IMAGES:
        src = LANDING_ASSETS / f"{name}.jpg"
        if src.exists():
            shutil.copyfile(src, BUILD_ASSETS / f"{name}.jpg")
        else:
            print(f"WARNING: missing asset {src}")
    shutil.copyfile(PAULA_PHOTO, BUILD_ASSETS / "paula.jpg")


def slide_cover() -> str:
    return f"""<section class="slide redbg">
  <img class="cover-img" src="assets/hero.jpg" loading="eager" alt="">
  <div class="cover-fade"></div>
  <div class="pad">
    <div class="wordmark">COLGATE-PALMOLIVE</div>
    <div class="eyebrow" style="color:#fff;opacity:.85;margin-top:54px">Digital Commerce Concept · UAE E-Commerce</div>
    <div class="cover-title" style="margin-top:16px">ALWAYS<br>SHELF-READY</div>
    <div class="cover-tag">Win the click before the cart.</div>
  </div>
  <div class="cover-lockup">
    Prepared by {P['name']} &nbsp;·&nbsp; June 2026<br>
    For: Ecommerce Manager (174114), Colgate-Palmolive — Dubai
  </div>
</section>"""


def slide_agenda() -> str:
    rows = [
        ("01", "The digital-shelf truth — UAE"),
        ("02", "The big idea — Always Shelf-Ready"),
        ("03", "The Perfect Page by channel"),
        ("04", "90-day digital-commerce plan"),
        ("05", "KPIs, ROI &amp; cadence"),
        ("06", "Why Paula"),
    ]
    body = "".join(
        f'<div class="agenda-row"><div class="agenda-num">{n}</div><div class="agenda-txt">{t}</div></div>'
        for n, t in rows
    )
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">Agenda</div>
    <div class="h2" style="margin:6px 0 26px">The plan, end&nbsp;to&nbsp;end.</div>
    {body}
  </div>
  <div class="pagenum">01</div>
</section>"""


def slide_insight() -> str:
    return f"""<section class="slide">
  <img src="assets/marketplace.jpg" loading="eager" alt=""
       style="position:absolute;right:0;top:0;width:440px;height:720px;object-fit:cover">
  <div class="pad" style="padding-right:490px">
    <div class="kicker">01 · The digital-shelf truth — UAE</div>
    <div class="h2" style="margin:6px 0 18px">The category is won<br>on the first screen.</div>
    <ul class="bullets">
      <li><b>Decided at search:</b> ~7 in 10 e-commerce purchases are won at the title, image, rating and price the shopper sees first — long before checkout.</li>
      <li><b>A crowded shelf:</b> on Noon &amp; Amazon.ae, oral &amp; personal care is a search-share battle won by content, ratings and availability.</li>
      <li><b>Two missions:</b> planned replenishment on marketplaces vs. 10-minute impulse on quick-commerce (Noon Minutes, Talabat, Careem).</li>
      <li><b>Retail media is the new profit pool:</b> the fastest-growing FMCG lever — but only with ROAS discipline.</li>
      <li><b>So the job is clear:</b> make every hero SKU perfect on the digital shelf, every day, and prove it in the P&amp;L.</li>
    </ul>
  </div>
  <div class="pagenum">02</div>
</section>"""


def slide_big_idea() -> str:
    return f"""<section class="slide dark">
  <div class="bigidea">
    <div class="bigidea-left">
      <div class="eyebrow" style="color:#ff5a5f">02 · The big idea</div>
      <div class="t">ALWAYS<br>SHELF-READY</div>
      <div class="lead on-dark" style="max-width:520px">
        Turn digital-shelf excellence into one shared operating system: a weekly
        <b style="color:#fff">Digital Shelf Scorecard (0–100)</b> per hero SKU. Content, search share,
        availability, conversion and ROAS — one number the whole team drives toward
        <b style="color:#fff">100 = PERFECT</b>, with clear corrective actions.
      </div>
      <div class="lockup">"Perfect on the shelf,<br>proven in the P&amp;L."</div>
    </div>
    <div class="kv">
      <div class="kv-card">
        <div class="lbl">DIGITAL SHELF SCORE</div>
        <div class="val">100</div>
        <div class="state">PERFECT</div>
        <div class="track"><div class="fill"></div></div>
        <div class="rows">
          <div class="r"><span>Content &amp; A+</span><b>100%</b></div>
          <div class="r"><span>Search share</span><b>#1</b></div>
          <div class="r"><span>Availability</span><b>100%</b></div>
          <div class="r"><span>Conversion · ROAS</span><b>▲</b></div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def slide_how() -> str:
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">02 · How it works</div>
    <div class="h2" style="margin:6px 0 4px">One scorecard. Two layers.</div>
    <div class="flow">
      <div class="node"><h4>Measure</h4><p>A weekly Digital Shelf Score per hero SKU across every retailer.</p></div>
      <div class="node"><h4>Act</h4><p>Clear corrective actions where the score drops — content, price, stock, bid.</p></div>
      <div class="node"><h4>Prove</h4><p>Conversion, search share &amp; ROAS tracked against the P&amp;L.</p></div>
    </div>
    <div class="two">
      <div class="col">
        <div class="tagcol">Owned · content that converts</div>
        <h4>The Perfect Page</h4>
        <ul class="bullets">
          <li>Search-optimised titles, A+ rich content, hero imagery and review health on every priority SKU.</li>
          <li>Availability &amp; buy-box protection so demand never leaks to a competitor.</li>
          <li>One audit line: <b>"Perfect Page compliance"</b> — content + rating + in-stock.</li>
        </ul>
      </div>
      <div class="col">
        <div class="tagcol">Paid &amp; live · drive demand</div>
        <h4>Full-funnel pull</h4>
        <ul class="bullets">
          <li>Retail-media sponsored search &amp; banners tuned to ROAS on Noon, Amazon.ae &amp; Carrefour.</li>
          <li>Quick-commerce impulse bundles + 10-minute delivery deals on Noon Minutes, Talabat, Careem.</li>
          <li>360 social &amp; creator content feeding the funnel, measured to conversion.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="pagenum">03</div>
</section>"""


def slide_channels() -> str:
    cards = [
        ("digitalshelf", "Marketplace PDP", "A+ content, hero imagery, review health and search-optimised titles on every priority SKU."),
        ("marketplace", "Search &amp; share", "Own page-one for category keywords on Noon &amp; Amazon.ae via ranking, ratings &amp; availability."),
        ("retailmedia", "Retail media", "Always-on sponsored search + banners, bid &amp; budget tuned to ROAS and net-sales contribution."),
        ("qcommerce", "Quick-commerce", "Impulse bundles, 10-minute delivery deals and replenishment tiles on Noon Minutes, Talabat, Careem."),
        ("hero", "Full-funnel &amp; data", "360 social/creator pull into the funnel, all unified on one weekly Digital Shelf Scorecard."),
    ]
    cc = "".join(
        f'<div class="cc"><img src="assets/{img}.jpg" loading="eager" alt=""><div class="body"><h4>{title}</h4><p>{desc}</p></div></div>'
        for img, title, desc in cards
    )
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">02 · Across the digital shelf</div>
    <div class="h2" style="margin:6px 0 0">One scorecard, every channel.</div>
    <div class="cards5">{cc}</div>
  </div>
  <div class="pagenum">04</div>
</section>"""


def _table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="ps"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def slide_perfect_store() -> str:
    rows = [
        ["Marketplace (Noon / Amazon.ae)", 'A+ content on hero SKUs · 4.3★+ review health · search-optimised titles · <b>page-one search share</b> on category keywords · buy-box &amp; availability'],
        ["Carrefour / MAF online", "Hero-SKU availability · banner &amp; sponsored placement · price-pack compliance · click-and-collect readiness"],
        ["Quick-commerce (Talabat / Noon Minutes / Careem)", '<b>Impulse bundles</b> · hero-SKU availability · 10-minute delivery deal · replenishment tiles'],
        ["Retail media (cross-platform)", 'Always-on sponsored search + display · <b>ROAS &amp; net-sales</b> targets · weekly bid &amp; budget optimisation'],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">03 · The Perfect Page by channel</div>
    <div class="h2" style="margin:6px 0 2px">One measurable picture per channel.</div>
    <div class="lead" style="font-size:15px;margin-top:8px">Content, availability, pricing and activation — scored weekly and tied to the digital-shelf scorecard.</div>
    {_table(["Channel", "Perfect Page priorities"], rows)}
  </div>
  <div class="pagenum">05</div>
</section>"""


def slide_calendar() -> str:
    rows = [
        ["Wk 1–2", "Onboarding &amp; digital-shelf audit", "All", "Baseline scorecard per hero SKU + retailer 1:1s", "Diagnose gaps"],
        ["Wk 3–4", "Perfect Page fix", "Marketplaces", "A+ refresh, titles, imagery, review seeding", "Content score ▲"],
        ["Month 2", "Retail-media engine on", "Noon/Amazon/Carrefour", "Always-on sponsored + ROAS targets", "Search share &amp; ROAS"],
        ["Month 2", "Quick-commerce push", "Talabat/Noon Min./Careem", "Impulse bundles + 10-min delivery deal", "Trial &amp; basket size"],
        ["Month 3", "Peak &amp; gifting pre-build", "All", "Ramadan/DSF bundles + hero stock secured", "Net sales ▲"],
        ["Month 3", "Business review &amp; scale", "All", "Scorecard + ROAS readout, scale winners", "Lock next-Q plan"],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">04 · 90-day digital-commerce plan</div>
    <div class="h2" style="margin:6px 0 2px">From audit to scale in 90 days.</div>
    {_table(["Window", "Workstream", "Channel", "Mechanic", "Objective"], rows)}
  </div>
  <div class="pagenum">06</div>
</section>"""


def slide_kpis() -> str:
    rows = [
        ['<b>Digital Shelf Score (toward 100)</b>', "Execution quality — the hero KPI", "Weekly"],
        ["Click &amp; conversion rate (CVR)", "Proof that content converts", "Weekly"],
        ["Search share (priority keywords)", "Digital-shelf strength (leading indicator)", "Bi-weekly"],
        ["Retail-media ROAS", "Spend efficiency", "Per activity + monthly"],
        ["Availability / buy-box %", "Demand-capture foundation", "Weekly"],
        ["Net sales &amp; channel P&amp;L contribution", "Growth that reaches the bottom line", "Monthly"],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">05 · KPIs, ROI &amp; cadence</div>
    <div class="h2" style="margin:6px 0 2px">Prove it moves the number.</div>
    {_table(["KPI", "What it proves", "Cadence"], rows)}
    <div class="lead" style="font-size:14px;margin-top:18px"><b class="red">Cadence:</b> weekly scorecard review with the e-commerce &amp; key-account teams; monthly business reviews with Marketing, Supply Chain &amp; Finance; spend managed to ROAS throughout.</div>
  </div>
  <div class="pagenum">07</div>
</section>"""


def slide_why_paula() -> str:
    return f"""<section class="slide">
  <img class="why-photo" src="assets/paula.jpg" loading="eager" alt="">
  <div class="pad" style="padding-right:500px">
    <div class="kicker">06 · Why Paula</div>
    <div class="why-quote">"Always Shelf-Ready is exactly how I work — make every product perfect on the digital shelf, drive the full funnel, and prove it in the P&amp;L."</div>
    <ul class="bullets" style="margin-top:20px">
      <li>Owns the digital shelf end-to-end at DoFreeze — Shopify + Noon, Talabat, Careem, Deliveroo across <b>50+ markets</b>.</li>
      <li>Ran <b>42 key accounts to +30% GMV QoQ</b> at Alibaba's Miravia, with Flash Sales <b>P&amp;L</b> ownership.</li>
      <li>Fluent in content-that-converts, retail media, ROI/ROAS analytics — and already in Dubai on a residence visa.</li>
    </ul>
    <div class="skillrow">
      <span>Digital shelf excellence</span><span>Content that converts</span>
      <span>Retail media &amp; ROAS</span><span>Key accounts &amp; P&amp;L</span>
    </div>
  </div>
  <div class="pagenum">08</div>
</section>"""


def slide_contact() -> str:
    raw = P.get("linkedin", "")
    linkedin = raw.replace("https://", "").replace("http://", "")
    linkedin_line = f'<div class="contact-line">{linkedin}</div>' if linkedin else ""
    return f"""<section class="slide redbg">
  <div class="pad">
    <div class="wordmark">ALWAYS SHELF-READY</div>
    <div class="contact-big" style="margin-top:150px">CONTACT</div>
    <div class="contact-line" style="margin-top:30px">{P['email']}</div>
    <div class="contact-line">{P['phone']}</div>
    {linkedin_line}
  </div>
</section>"""


def build_html() -> str:
    slides = "\n".join([
        slide_cover(),
        slide_agenda(),
        slide_insight(),
        slide_big_idea(),
        slide_how(),
        slide_channels(),
        slide_perfect_store(),
        slide_calendar(),
        slide_kpis(),
        slide_why_paula(),
        slide_contact(),
    ])
    return html_doc(slides)


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    url = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(400)
            page.emulate_media(media="print")
            page.pdf(
                path=str(pdf_path),
                width="1280px",
                height="720px",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
        finally:
            browser.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
    args = ap.parse_args()

    stage_assets()
    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    HTML_PATH.write_text(build_html(), encoding="utf-8")
    print(f"HTML: {HTML_PATH}")
    if args.html_only:
        return
    render_pdf(HTML_PATH, DECK_PDF)
    print(f"DECK PDF: {DECK_PDF}")


if __name__ == "__main__":
    main()
