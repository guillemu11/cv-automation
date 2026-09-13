#!/usr/bin/env python3
"""No Borders — Revolut UAE brand & growth pitch deck for Paula's application to
Marketing Manager (Brand), Dubai / UAE.

Adapts the deck-propuesta machinery (concept-led 16:9 deck in the company's real
brand system + a rigorous plan appendix, HTML->PDF via headless Chromium, merged
with pypdf) to a FINTECH BRAND & GROWTH role instead of FMCG Trade & Shopper:

  - Concept locked to "No Borders" (remittance + multi-currency; insight: ~88% of
    the UAE is expat, money here is born to cross borders) so the deck tells the
    SAME story as the campaign-landing already built at output/landing_revolut/.
  - The appendix is a BRAND & GROWTH plan (positioning, full-funnel channel
    architecture acquisition->retention, corridor go-to-market, experimentation,
    funnel economics) — NOT a trade & shopper / Perfect Store plan.

Fully dark, cinematic deck in Revolut's real brand system (cobalt #4F55F1, teal
#00A87E, near-black #0B0C10; Aeonik -> Space Grotesk / Inter). No stock photos —
brand-system typographic/CSS key visuals only; Paula's real photo on "Why Paula".

Outputs into the job folder's 02_Deliverables:
  Deliverable_Paula_Revolut_No-Borders_Deck.pdf   (11 slides, 16:9)
  Deliverable_Paula_Revolut_Brand-Growth-Plan.pdf (2-page A4 appendix)
  Deliverable_Paula_Revolut_No-Borders_FULL.pdf   (deck + plan, headline attach)

Nothing is ever sent — drafts for Paula to review.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings  # noqa: E402

JOB_DIR = ROOT / "output" / "2026-08-20" / "Revolut - Marketing Manager (Brand)"
DELIV_DIR = JOB_DIR / "02_Deliverables"
BUILD_DIR = DELIV_DIR / "no_borders_deck"
BUILD_ASSETS = BUILD_DIR / "assets"
DECK_HTML = BUILD_DIR / "deck.html"
PLAN_HTML = BUILD_DIR / "plan.html"

PAULA_PHOTO = ROOT / "templates" / "paula_photo.jpg"

DECK_PDF = DELIV_DIR / "Deliverable_Paula_Revolut_No-Borders_Deck.pdf"
PLAN_PDF = DELIV_DIR / "Deliverable_Paula_Revolut_Brand-Growth-Plan.pdf"
FULL_PDF = DELIV_DIR / "Deliverable_Paula_Revolut_No-Borders_FULL.pdf"

P = settings.profile["personal"]

# ---------------------------------------------------------------- brand tokens
COBALT = "#4F55F1"
TEAL = "#00A87E"
BG = "#0B0C10"
CARD = "#14161B"
CARD2 = "#1B1E25"
LINE = "rgba(255,255,255,.12)"
DIM = "rgba(255,255,255,.64)"

# ============================================================================
# DECK  (16:9, fully dark, Revolut brand system)
# ============================================================================

DECK_CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
@page{{size:1280px 720px;margin:0}}
html,body{{background:{BG}}}
body{{font-family:'Inter',system-ui,sans-serif;color:#fff}}
.slide{{position:relative;width:1280px;height:720px;overflow:hidden;background:{BG};page-break-after:always}}
.slide:last-child{{page-break-after:auto}}
.pad{{position:absolute;inset:0;padding:74px 88px}}
.cobalt{{color:{COBALT}}}
.teal{{color:{TEAL}}}
.wordmark{{font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-.5px;font-size:20px;color:#fff}}
.eyebrow{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:13px;letter-spacing:2.5px;text-transform:uppercase;color:{COBALT}}}
.kicker{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:12.5px;letter-spacing:2px;text-transform:uppercase;color:{DIM}}}
.h2{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:50px;line-height:.98;letter-spacing:-1.5px;color:#fff}}
.lead{{font-size:18px;line-height:1.5;color:{DIM};max-width:780px}}
.lead b{{color:#fff;font-weight:600}}
.pagenum{{position:absolute;bottom:40px;right:60px;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:34px;color:{COBALT}}}
ul.bullets{{list-style:none;margin-top:10px}}
ul.bullets li{{position:relative;padding-left:26px;margin:14px 0;font-size:16px;line-height:1.45;color:{DIM};max-width:640px}}
ul.bullets li::before{{content:"";position:absolute;left:0;top:8px;width:9px;height:9px;background:{COBALT};border-radius:50%}}
ul.bullets li b{{color:#fff;font-weight:600}}
/* aura backgrounds */
.aura{{position:absolute;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none}}
.aura.c{{width:640px;height:640px;background:{COBALT};opacity:.30}}
.aura.t{{width:520px;height:520px;background:{TEAL};opacity:.20}}
/* table */
table.ps{{width:100%;border-collapse:collapse;margin-top:22px;font-size:14px;position:relative;z-index:2}}
table.ps th{{background:{COBALT};color:#fff;text-align:left;padding:12px 15px;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:12px;letter-spacing:.6px;text-transform:uppercase}}
table.ps td{{border-bottom:1px solid {LINE};padding:12px 15px;vertical-align:top;color:{DIM};line-height:1.4;background:{CARD}}}
table.ps tr td:first-child{{font-weight:600;color:#fff;width:210px}}
table.ps b{{color:{COBALT};font-weight:600}}
/* cover */
.cover-title{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:150px;line-height:.82;letter-spacing:-6px;color:#fff}}
.cover-tag{{font-size:22px;color:#fff;margin-top:28px;max-width:620px;line-height:1.35;font-weight:500}}
.cover-tag span{{color:{COBALT}}}
.cover-lockup{{position:absolute;bottom:48px;left:88px;font-size:12.5px;color:{DIM};letter-spacing:.3px;line-height:1.7}}
.cover-chip{{position:absolute;top:74px;right:88px;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#fff;background:{COBALT};padding:8px 16px;border-radius:999px}}
/* agenda */
.agenda-row{{display:flex;align-items:baseline;gap:24px;padding:15px 0;border-bottom:1px solid {LINE}}}
.agenda-num{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:22px;color:{COBALT};width:44px}}
.agenda-txt{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:25px;color:#fff;letter-spacing:-.4px}}
/* insight */
.bignum{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:230px;line-height:.8;letter-spacing:-8px;color:{COBALT};font-variant-numeric:tabular-nums}}
/* big idea key visual */
.bigidea{{display:flex;gap:56px;align-items:center;height:100%;padding:74px 88px;position:relative;z-index:2}}
.bigidea-left{{flex:1;max-width:560px}}
.bigidea-left .t{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:96px;line-height:.84;letter-spacing:-4px;color:#fff;margin:14px 0 22px}}
.bigidea-left .lockup{{margin-top:26px;color:#fff;font-size:19px;line-height:1.35;font-weight:600}}
.bigidea-left .lockup span{{color:{COBALT}}}
.kv{{position:relative;flex:0 0 430px;height:470px}}
.xfer{{position:absolute;left:0;top:40px;width:400px;background:{CARD};border:1px solid {LINE};border-radius:22px;padding:30px 32px;box-shadow:0 40px 90px rgba(0,0,0,.6);z-index:3}}
.xfer .top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px}}
.xfer .rvl{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:15px;letter-spacing:-.3px;color:#fff}}
.xfer .live{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{TEAL};display:flex;align-items:center;gap:7px}}
.xfer .live::before{{content:"";width:8px;height:8px;border-radius:50%;background:{TEAL}}}
.xfer .rowlbl{{font-size:12px;letter-spacing:1px;text-transform:uppercase;color:{DIM};margin-bottom:5px}}
.xfer .amt{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:44px;line-height:1;color:#fff;letter-spacing:-1px}}
.xfer .amt small{{font-size:20px;color:{DIM};font-weight:500;margin-left:6px}}
.xfer .divider{{height:1px;background:{LINE};margin:20px 0}}
.xfer .get .amt{{color:{TEAL}}}
.xfer .foot{{margin-top:22px;display:flex;justify-content:space-between;align-items:center;font-size:12.5px;color:{DIM}}}
.xfer .foot b{{color:#fff;font-weight:600}}
.kv-badge{{position:absolute;right:6px;bottom:26px;background:{COBALT};color:#fff;border-radius:14px;padding:16px 20px;z-index:4;box-shadow:0 24px 60px rgba(79,85,241,.5)}}
.kv-badge .n{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:15px;letter-spacing:-.2px}}
.kv-badge .s{{font-size:11.5px;opacity:.85;margin-top:2px}}
/* how-it-works funnel */
.flow{{display:flex;align-items:stretch;gap:14px;margin-top:28px;position:relative;z-index:2}}
.flow .node{{flex:1;background:{CARD};border:1px solid {LINE};border-top:4px solid {COBALT};border-radius:12px;padding:18px 18px}}
.flow .node .stg{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{COBALT}}}
.flow .node h4{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:17px;margin:8px 0 6px;color:#fff}}
.flow .node p{{font-size:13px;line-height:1.4;color:{DIM}}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:26px;position:relative;z-index:2}}
.two .col{{background:{CARD};border:1px solid {LINE};border-radius:12px;padding:22px 24px}}
.two .col .tagcol{{font-size:11.5px;color:{COBALT};font-weight:600;letter-spacing:1.2px;text-transform:uppercase;font-family:'Space Grotesk',sans-serif}}
.two .col h4{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:19px;color:#fff;margin:6px 0 4px}}
/* channel cards */
.cards5{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:30px;position:relative;z-index:2}}
.cc{{border-radius:14px;overflow:hidden;background:{CARD};border:1px solid {LINE};min-height:300px;display:flex;flex-direction:column}}
.cc .cap{{height:96px;display:flex;align-items:flex-end;padding:14px;background:linear-gradient(150deg,{CARD2},{CARD})}}
.cc.is-cobalt .cap{{background:linear-gradient(150deg,{COBALT},#3A40C4)}}
.cc.is-teal .cap{{background:linear-gradient(150deg,{TEAL},#00795a)}}
.cc .stg{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;color:#fff;opacity:.9}}
.cc .body{{padding:14px 15px}}
.cc h4{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:15px;margin-bottom:7px;color:#fff}}
.cc p{{font-size:11.5px;line-height:1.4;color:{DIM}}}
/* why paula */
.why-photo{{position:absolute;right:0;top:0;width:470px;height:720px;object-fit:cover;filter:grayscale(.15) contrast(1.02)}}
.why-fade{{position:absolute;right:390px;top:0;width:200px;height:720px;background:linear-gradient(90deg,{BG},transparent);z-index:2}}
.why-quote{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:25px;line-height:1.28;color:#fff;max-width:560px;margin-top:16px}}
.why-quote span{{color:{COBALT}}}
ul.why-bul li{{max-width:490px}}
.skillrow{{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px;max-width:520px}}
.skillrow span{{font-size:12px;font-weight:500;color:#fff;border:1px solid {LINE};border-radius:999px;padding:7px 14px}}
/* contact */
.contact-big{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:180px;line-height:.85;letter-spacing:-7px;color:#fff}}
.contact-line{{font-size:18px;color:#fff;margin-top:8px;letter-spacing:.4px}}
.contact-line b{{color:{COBALT}}}
"""


def deck_doc(slides: str) -> str:
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{DECK_CSS}</style></head><body>{slides}</body></html>"""


def s_cover() -> str:
    return f"""<section class="slide">
  <div class="aura c" style="top:-220px;left:-160px"></div>
  <div class="aura t" style="bottom:-220px;right:-140px"></div>
  <div class="cover-chip">Brand &amp; Growth concept</div>
  <div class="pad">
    <div class="wordmark">Revolut</div>
    <div class="eyebrow" style="margin-top:120px">Brand &amp; Growth · UAE · a full-funnel campaign concept</div>
    <div class="cover-title" style="margin-top:20px">NO<br>BORDERS</div>
    <div class="cover-tag">Make Revolut the way the UAE moves money — <span>send it home before the exchange desk even opens.</span></div>
  </div>
  <div class="cover-lockup">
    Prepared by {P['name']} &nbsp;·&nbsp; {date.today().strftime('%d %B %Y')}<br>
    For: Marketing Manager (Brand) — Dubai / UAE, Revolut
  </div>
</section>"""


def s_agenda() -> str:
    rows = [
        ("01", "The insight — money born to cross borders"),
        ("02", "The big idea — No Borders"),
        ("03", "How it works — full funnel, one story"),
        ("04", "Audience &amp; corridor strategy"),
        ("05", "90-day launch &amp; KPIs"),
        ("06", "Why Paula"),
    ]
    body = "".join(
        f'<div class="agenda-row"><div class="agenda-num">{n}</div><div class="agenda-txt">{t}</div></div>'
        for n, t in rows
    )
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">Agenda</div>
    <div class="h2" style="margin:6px 0 26px">The concept, end&nbsp;to&nbsp;end.</div>
    {body}
  </div>
  <div class="pagenum">01</div>
</section>"""


def s_insight() -> str:
    return f"""<section class="slide">
  <div class="aura c" style="top:-260px;right:-200px"></div>
  <div class="pad">
    <div class="kicker">01 · The insight — UAE</div>
    <div style="display:flex;gap:56px;align-items:center;height:520px">
      <div style="flex:0 0 auto">
        <div class="bignum">88%</div>
        <div class="kicker" style="margin-top:14px;max-width:300px">of UAE residents are expats — one of the world's largest remittance hubs</div>
      </div>
      <div style="flex:1">
        <div class="h2" style="margin-bottom:18px">Here, money is<br>born to cross<br>a border.</div>
        <ul class="bullets">
          <li>For millions of people, "money" isn't local — it's a <b>monthly journey</b> to Kerala, Manila, Cairo, Lahore or London.</li>
          <li>Yet the world's average remittance still costs around <b>6%</b> and can take days — much of it still sent in cash, in a queue.</li>
          <li>Revolut already <b>solves</b> this. The brand opportunity isn't a feature — it's to own the cultural truth that <b>your money was never meant to stop at the border.</b></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="pagenum">02</div>
</section>"""


def s_big_idea() -> str:
    return f"""<section class="slide">
  <div class="aura c" style="bottom:-260px;left:-180px"></div>
  <div class="bigidea">
    <div class="bigidea-left">
      <div class="eyebrow">02 · The big idea</div>
      <div class="t">NO<br>BORDERS</div>
      <div class="lead" style="max-width:520px;color:#cfd2da">
        One ownable idea for the UAE: with Revolut, the border was <b style="color:#fff">never there</b>.
        The same platform truth — instant, real-rate, multi-currency — dramatised as the way this
        country actually lives and sends money.
      </div>
      <div class="lockup">"Send it home <span>before the exchange<br>desk even opens.</span>"</div>
    </div>
    <div class="kv">
      <div class="xfer">
        <div class="top">
          <div class="rvl">Revolut · Transfer</div>
          <div class="live">Live rate</div>
        </div>
        <div class="send">
          <div class="rowlbl">You send</div>
          <div class="amt">1,000<small>AED</small></div>
        </div>
        <div class="divider"></div>
        <div class="get">
          <div class="rowlbl">They receive · Kochi</div>
          <div class="amt">₹23,120<small>INR</small></div>
        </div>
        <div class="foot"><span>Arrives <b>in seconds</b></span><span><b>0</b> hidden fees</span></div>
      </div>
      <div class="kv-badge">
        <div class="n">Dubai → home</div>
        <div class="s">no border · no queue · no spread</div>
      </div>
    </div>
  </div>
</section>"""


def s_how() -> str:
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">03 · How it works</div>
    <div class="h2" style="margin:6px 0 2px">One story, the whole funnel.</div>
    <div class="flow">
      <div class="node"><div class="stg">Awareness</div><h4>Own the corridor</h4><p>Community-true OOH &amp; creators make Revolut the name attached to "sending home".</p></div>
      <div class="node"><div class="stg">Consideration</div><h4>Expose the rate</h4><p>Data-driven stories show the real cost of the old way vs. Revolut.</p></div>
      <div class="node"><div class="stg">Conversion</div><h4>First transfer</h4><p>Localised onboarding + a payday-week offer engineered for one activation metric.</p></div>
      <div class="node"><div class="stg">Retention</div><h4>Everyday money</h4><p>From one transfer to multi-currency spend, savings and travel — a daily habit.</p></div>
    </div>
    <div class="two">
      <div class="col">
        <div class="tagcol">Brand layer · earns attention</div>
        <h4>A cultural truth, not an ad</h4>
        <ul class="bullets">
          <li>One line — <b>"send it home before the exchange desk opens"</b> — carried across OOH, social and creators, adapted per corridor.</li>
          <li>Tone of voice &amp; style guide owned locally; global assets adapted to real UAE nuance.</li>
        </ul>
      </div>
      <div class="col">
        <div class="tagcol">Growth layer · drives results</div>
        <h4>Engineered for the metric</h4>
        <ul class="bullets">
          <li>Paid social &amp; app-install campaigns A/B-tested on creative &amp; offer; scaled on ROAS.</li>
          <li>Winners operationalised into a <b>regional playbook</b> so the idea scales without re-inventing it.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="pagenum">03</div>
</section>"""


def s_channels() -> str:
    cards = [
        ("is-cobalt", "Awareness", "OOH · corridor-cut", "Sheikh Zayed Rd &amp; Metro", "Billboards &amp; wraps with a different destination city per line, timed to payday week."),
        ("", "Awareness", "Corridor creators", "The people who send it home", "Micro-creators per community (Malayali, Filipino, Egyptian, Pakistani) — real UGC, not gloss."),
        ("is-teal", "Consideration", "Content · the rate exposed", "\"See what the desk didn't tell you\"", "Data-driven cost comparisons — the conversion engine of the campaign."),
        ("", "Conversion", "In-app · first-transfer GTM", "Zero-fee first send", "Localised onboarding + payday-week offer built to drive the first transfer."),
        ("", "Retention", "CRM + referral loop", "One sender, a community", "Lifecycle nudges to multi-currency &amp; savings, plus a compounding referral loop."),
    ]
    cc = "".join(
        f'<div class="cc {cls}"><div class="cap"><div class="stg">{stg}</div></div>'
        f'<div class="body"><div class="kicker" style="font-size:10px;margin-bottom:6px;color:{COBALT}">{lbl}</div>'
        f'<h4>{title}</h4><p>{desc}</p></div></div>'
        for cls, stg, lbl, title, desc in cards
    )
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">03 · Across the funnel</div>
    <div class="h2" style="margin:6px 0 0">The same idea, every stage.</div>
    <div class="cards5">{cc}</div>
  </div>
  <div class="pagenum">04</div>
</section>"""


def _table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="ps"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def s_corridors() -> str:
    rows = [
        ["India", "Largest corridor; value-conscious, mobile-first, family remitters", 'Real rate, arrives in seconds — <b>"before the desk opens"</b>', "Malayali/Tamil creators · Meta &amp; YouTube · Metro"],
        ["Philippines", "High trust in community word-of-mouth; frequent smaller sends", "No hidden spread; every dirham counts back home", "Filipino creators · Facebook groups · referral"],
        ["Egypt / Levant", "FX-savvy, rate-sensitive; growing young professional base", "Beat the parallel-rate anxiety with a transparent live rate", "TikTok &amp; short-form · rate-exposed content"],
        ["UK / EU", "Premium expats; travel &amp; multi-currency daily use", "One card, every currency — spend like a local, everywhere", "Premium OOH · lifestyle creators · Metal/Ultra"],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">04 · Audience &amp; corridor strategy</div>
    <div class="h2" style="margin:6px 0 2px">Prioritised by corridor, not by channel.</div>
    <div class="lead" style="font-size:15px;margin-top:8px;color:{DIM}">Same idea, tuned per community — audience truth &#8594; lead message &#8594; channel &amp; creator mix.</div>
    {_table(["Corridor", "Audience truth", "Lead message", "Channel &amp; creator"], rows)}
  </div>
  <div class="pagenum">05</div>
</section>"""


def s_calendar_kpis() -> str:
    cal = [
        ["Wk 1–2", "Launch — \"No Borders\"", "OOH + social + PR", "Awareness"],
        ["Wk 3–6", "Corridor creators + rate-exposed content", "Meta / TikTok / YouTube", "Consideration"],
        ["Payday wks", "Zero-fee first-transfer push", "In-app + paid social", "Conversion"],
        ["Month 3", "Lifecycle + referral loop; scale winners", "CRM + referral", "Retention"],
    ]
    kpi = [
        ['<b>Install &#8594; first-transfer activation</b>', "The hero metric — the idea works or it doesn't", "Weekly"],
        ["Blended CAC in target corridors", "Efficient, corridor-led acquisition", "Weekly"],
        ["Multi-currency MAU / retention", "One transfer &#8594; everyday habit", "Monthly"],
        ["Referral K-factor", "The corridor loop compounding", "Monthly"],
        ["Creative ROAS &amp; test win-rate", "Experimentation discipline", "Per flight"],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">05 · 90-day launch &amp; measurement</div>
    <div class="h2" style="margin:6px 0 2px">Launch it. Then prove it.</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:start">
      <div>
        <div class="eyebrow" style="margin-top:20px;margin-bottom:-6px">90-day plan</div>
        {_table(["Window", "Activation", "Channels", "Stage"], cal)}
      </div>
      <div>
        <div class="eyebrow" style="margin-top:20px;margin-bottom:-6px">Full-funnel KPIs</div>
        {_table(["KPI", "What it proves", "Cadence"], kpi)}
      </div>
    </div>
  </div>
  <div class="pagenum">06</div>
</section>"""


def s_why_paula() -> str:
    return f"""<section class="slide">
  <img class="why-photo" src="assets/paula.jpg" loading="eager" alt="">
  <div class="why-fade"></div>
  <div class="pad" style="padding-right:500px">
    <div class="kicker">06 · Why Paula</div>
    <div class="why-quote">"No Borders is exactly how I work — take a real local truth, build one idea across the whole funnel, and <span>engineer it to move the metric.</span>"</div>
    <ul class="bullets why-bul" style="margin-top:22px">
      <li>Leads <b>brand &amp; growth in the UAE today</b> — GTM launches, full-funnel campaigns and paid media, in-market.</li>
      <li>Came up inside <b>hyper-growth global tech</b> — Alibaba's Miravia (42 accounts, <b>+30% GMV QoQ</b>) &amp; Glovo.</li>
      <li>Built an <b>AI marketing-automation system</b> (Claude) that scaled repeatable playbooks across <b>50+ markets</b>.</li>
    </ul>
    <div class="skillrow">
      <span>Brand strategy &amp; positioning</span><span>Go-to-market</span>
      <span>Full-funnel growth</span><span>Experimentation &amp; ROAS</span><span>UAE market</span>
    </div>
  </div>
  <div class="pagenum">07</div>
</section>"""


def s_contact() -> str:
    raw = P.get("linkedin", "")
    linkedin = raw.replace("https://", "").replace("http://", "")
    linkedin_line = f'<div class="contact-line">{linkedin}</div>' if linkedin else ""
    return f"""<section class="slide">
  <div class="aura c" style="bottom:-260px;right:-160px"></div>
  <div class="pad">
    <div class="wordmark">Revolut · No Borders</div>
    <div class="contact-big" style="margin-top:150px">LET'S<br>TALK.</div>
    <div class="contact-line" style="margin-top:30px"><b>{P['name']}</b> — for Marketing Manager (Brand), UAE</div>
    <div class="contact-line" style="margin-top:14px">{P['email']}</div>
    <div class="contact-line">{P['phone']}</div>
    {linkedin_line}
  </div>
</section>"""


def build_deck_html() -> str:
    return deck_doc("\n".join([
        s_cover(), s_agenda(), s_insight(), s_big_idea(), s_how(),
        s_channels(), s_corridors(), s_calendar_kpis(), s_why_paula(), s_contact(),
    ]))


# ============================================================================
# PLAN  (A4 portrait, light, readable brand & growth appendix)
# ============================================================================

PLAN_CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
@page{{size:A4;margin:0}}
html,body{{background:#fff}}
body{{font-family:'Inter',system-ui,sans-serif;color:#1a1a1a}}
.page{{position:relative;width:794px;min-height:1123px;padding:54px 60px 64px;page-break-after:always}}
.page:last-child{{page-break-after:auto}}
.badge{{display:inline-block;background:{COBALT};color:#fff;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:10px;letter-spacing:2px;text-transform:uppercase;padding:6px 12px;border-radius:4px}}
h1.title{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:31px;letter-spacing:-1px;color:#0a0a0a;margin-top:12px}}
.sub{{font-size:13px;color:#555;font-style:italic;margin-top:5px}}
.meta{{font-size:10.5px;color:#8a8a8a;margin-top:6px}}
.rule{{height:1px;background:#e6e6e6;margin:14px 0 12px}}
.purpose{{font-size:12px;line-height:1.55;color:#222}}
.purpose b{{color:{COBALT}}}
h2.sec{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:15px;color:#0a0a0a;margin:16px 0 6px;padding-left:11px;border-left:4px solid {COBALT}}}
p.b{{font-size:11.3px;line-height:1.5;color:#222;margin:3px 0 3px 4px}}
p.b b{{color:#0a0a0a}}
ul.pl{{list-style:none;margin:4px 0 4px 4px}}
ul.pl li{{position:relative;padding-left:16px;font-size:11.3px;line-height:1.48;color:#222;margin:4px 0}}
ul.pl li::before{{content:"";position:absolute;left:0;top:7px;width:6px;height:6px;border-radius:50%;background:{COBALT}}}
ul.pl li b{{color:#0a0a0a}}
table.t{{width:100%;border-collapse:collapse;margin:8px 0;font-size:10.3px}}
table.t th{{background:#0a0a0a;color:#fff;text-align:left;padding:8px 10px;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:9.5px;letter-spacing:.4px;text-transform:uppercase}}
table.t td{{border-bottom:1px solid #e6e6e6;padding:8px 10px;vertical-align:top;color:#333;line-height:1.4}}
table.t tr td:first-child{{font-weight:700;color:#0a0a0a}}
table.t b{{color:{COBALT}}}
.close{{margin-top:14px;font-size:11px;line-height:1.5;color:#444;font-style:italic;border-top:1px solid #ddd;padding-top:10px}}
.close b{{color:#0a0a0a;font-style:normal}}
.foot{{position:absolute;bottom:26px;left:60px;right:60px;text-align:center;font-size:8.5px;color:#9a9a9a}}
"""


def plan_doc(pages: str) -> str:
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{PLAN_CSS}</style></head><body>{pages}</body></html>"""


def _t(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="t"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def build_plan_html() -> str:
    li = P.get("linkedin", "").replace("https://", "").replace("http://", "")
    foot = f"{P['name']} · {P['email']} · {li} · {P['phone']}"

    page1 = f"""<section class="page">
  <div class="badge">Brand &amp; Growth Plan · Appendix to “No Borders”</div>
  <h1 class="title">Revolut — UAE Brand &amp; Growth</h1>
  <div class="sub">A full-funnel launch blueprint to make Revolut the way the UAE moves money</div>
  <div class="meta">Prepared by {P['name']} · {date.today().strftime('%d %B %Y')} · For: Marketing Manager (Brand) — Dubai / UAE, Revolut</div>
  <div class="rule"></div>
  <p class="purpose"><b>Purpose.</b> This is how I would land in the role: a fast read of the UAE customer and
  competitive set, one ownable brand idea (“No Borders”), a full-funnel channel architecture from acquisition
  to retention, and the experimentation and KPI discipline to prove it — built to run with global Growth and
  regional leadership from week one.</p>

  <h2 class="sec">1 · Market &amp; customer insight (UAE)</h2>
  <ul class="pl">
    <li><b>Expat-first market:</b> ~88% of residents are expats and the UAE is one of the world's largest remittance hubs — money here is inherently cross-border, high-frequency and emotionally loaded (it's family, not just FX).</li>
    <li><b>The pain is real:</b> the world's average remittance still costs ~6% and can take days; much is still sent as cash through exchange houses. Revolut's instant, real-rate, multi-currency product is the answer — the job is brand salience and trust at the moment of sending.</li>
    <li><b>Competitive set:</b> exchange houses (Al Ansari, LuLu), money-transfer apps (Wise, Remitly), neobanks (Wio, Mashreq Neo) and traditional banks. Revolut wins on rate transparency, speed and everyday multi-currency utility — that must be the story.</li>
    <li><b>Two jobs, one brand:</b> the value-conscious remitter (India, Philippines, Egypt, Pakistan) and the premium multi-currency traveller (UK/EU expats) — one idea, tuned by corridor and life-stage.</li>
  </ul>

  <h2 class="sec">2 · Positioning &amp; brand platform</h2>
  <p class="b"><b>Positioning:</b> Revolut = money with <b>no borders</b>. The one defensible, locally-true idea — instant, real-rate, multi-currency money that never stops at the border — dramatised as how the UAE actually lives and sends.</p>
  <p class="b"><b>Tone of voice:</b> clear, confident, human; never preachy about money. Own a local tone-of-voice and style guide, and adapt global campaigns to genuine UAE nuance (language, corridors, cultural moments) rather than lifting them wholesale.</p>

  <h2 class="sec">3 · Full-funnel channel architecture</h2>
  {_t(["Funnel stage", "Objective", "Channels &amp; mechanics"],
      [["Awareness", "Own the corridor &amp; the idea", "Corridor-cut OOH (Sheikh Zayed Rd, Metro), community micro-creators, PR &amp; earned around the “No Borders” idea"],
       ["Consideration", "Build trust, expose the rate", "Data-driven “real cost” content, comparison stories, ASO &amp; organic social, always-on search"],
       ["Conversion", "Drive the first transfer", "Paid social (Meta/TikTok), app-install (ASA/UAC), payday-week zero-fee first-send offer, localised onboarding"],
       ["Retention", "One transfer &#8594; everyday money", "Lifecycle CRM/EDM &amp; push to multi-currency spend, savings vaults &amp; travel; community referral loop"]])}
  <div class="foot">{foot}</div>
</section>"""

    page2 = f"""<section class="page">
  <h2 class="sec">4 · 90-day launch calendar</h2>
  {_t(["Window", "Activation", "Channel", "Objective"],
      [["Wk 1–2", "Launch “No Borders” — idea &amp; hero assets", "OOH + social + PR", "Salience &amp; corridor awareness"],
       ["Wk 3–6", "Corridor creators + rate-exposed content", "Meta / TikTok / YouTube", "Consideration &amp; trust"],
       ["Payday weeks", "Zero-fee first-transfer push", "In-app + paid social", "First-transfer activation"],
       ["Month 3", "Lifecycle + referral loop; scale winners", "CRM + referral", "Retention &amp; compounding growth"]])}
  <p class="b" style="margin-top:6px">Anchored to real UAE moments: monthly payday cadence (salaries land ~25th), Ramadan &amp; Eid (family &amp; giving), summer travel (multi-currency), and DSF/DSS retail peaks.</p>

  <h2 class="sec">5 · Experimentation &amp; growth mechanics</h2>
  <ul class="pl">
    <li><b>First-transfer offer:</b> the single activation metric; test offer type, threshold and payday timing to find the most efficient trigger.</li>
    <li><b>Creative testing:</b> structured A/B on hook, corridor message and creator format; scale on ROAS and cost-per-first-transfer, kill the rest fast.</li>
    <li><b>Referral loop:</b> engineered around how these communities actually share — a low-CAC, compounding growth engine measured by K-factor.</li>
    <li><b>Playbook operationalisation:</b> winning creative, audiences and mechanics packaged into a regional playbook so the idea scales to other markets without re-inventing it — my AI-automation background makes this fast and repeatable.</li>
  </ul>

  <h2 class="sec">6 · KPIs, funnel economics &amp; cadence</h2>
  {_t(["KPI", "What it proves", "Cadence"],
      [["<b>Install &#8594; first-transfer activation rate</b>", "Hero KPI — the concept works", "Weekly"],
       ["Blended CAC in target corridors", "Efficient, corridor-led acquisition", "Weekly"],
       ["Multi-currency MAU &amp; retention", "One transfer becomes an everyday habit", "Monthly"],
       ["Referral K-factor", "The corridor loop compounding", "Monthly"],
       ["Creative ROAS &amp; test win-rate", "Experimentation discipline &amp; spend efficiency", "Per flight"],
       ["Brand salience / prompted awareness (UAE)", "Brand-building, not just performance", "Quarterly"]])}
  <p class="b"><b>Cadence:</b> weekly growth stand-ups on activation &amp; CAC with the global Growth team; monthly brand &amp; funnel review with regional leadership; quarterly brand-tracking and playbook updates.</p>

  <div class="close"><b>Why I can land this fast:</b> I lead brand &amp; growth in the UAE today, came up inside hyper-growth global tech (Alibaba's Miravia — 42 accounts, +30% GMV QoQ; Glovo), run go-to-market launches and full-funnel paid media end-to-end, and built an AI marketing-automation system that scales repeatable playbooks across 50+ markets. “No Borders” is the way I'd put that to work for Revolut in the UAE.</div>
  <div class="foot">{foot}</div>
</section>"""

    return plan_doc(page1 + page2)


# ============================================================================
# Render + merge + QA
# ============================================================================

def stage_assets() -> None:
    BUILD_ASSETS.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PAULA_PHOTO, BUILD_ASSETS / "paula.jpg")


def render_pdf(html_path: Path, pdf_path: Path, size=("1280px", "720px")) -> None:
    from playwright.sync_api import sync_playwright
    url = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(350)
            page.emulate_media(media="print")
            kw = dict(path=str(pdf_path), print_background=True,
                      prefer_css_page_size=True,
                      margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            if size:
                kw.update(width=size[0], height=size[1])
            page.pdf(**kw)
        finally:
            browser.close()


def merge_pdfs(deck_pdf: Path, appendix_pdf: Path, out_pdf: Path) -> None:
    from pypdf import PdfWriter
    writer = PdfWriter()
    writer.append(str(deck_pdf))
    if appendix_pdf.exists():
        writer.append(str(appendix_pdf))
    else:
        print(f"WARNING: appendix not found: {appendix_pdf}")
    with open(out_pdf, "wb") as f:
        writer.write(f)


def screenshot_slides(html_path: Path, out_dir: Path, sel: str, w=1280, h=720) -> None:
    from playwright.sync_api import sync_playwright
    out_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": w, "height": h})
            page.goto(html_path.resolve().as_uri(), wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(350)
            for i, el in enumerate(page.query_selector_all(sel), 1):
                el.screenshot(path=str(out_dir / f"slide_{i:02d}.png"))
        finally:
            browser.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--qa", action="store_true", help="also write per-slide PNGs")
    args = ap.parse_args()

    stage_assets()
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    DECK_HTML.write_text(build_deck_html(), encoding="utf-8")
    PLAN_HTML.write_text(build_plan_html(), encoding="utf-8")
    print(f"DECK HTML: {DECK_HTML}")
    print(f"PLAN HTML: {PLAN_HTML}")
    if args.html_only and not args.qa:
        return

    if args.qa:
        screenshot_slides(DECK_HTML, BUILD_DIR / "qa", ".slide", 1280, 720)
        screenshot_slides(PLAN_HTML, BUILD_DIR / "qa_plan", ".page", 794, 1123)
        print(f"QA PNGs: {BUILD_DIR/'qa'} and {BUILD_DIR/'qa_plan'}")
        if args.html_only:
            return

    render_pdf(DECK_HTML, DECK_PDF, size=("1280px", "720px"))
    print(f"DECK PDF: {DECK_PDF}")
    render_pdf(PLAN_HTML, PLAN_PDF, size=None)  # A4 from CSS @page
    print(f"PLAN PDF: {PLAN_PDF}")
    merge_pdfs(DECK_PDF, PLAN_PDF, FULL_PDF)
    print(f"FULL PDF: {FULL_PDF}")


if __name__ == "__main__":
    main()
