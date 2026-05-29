"""End-to-end test of the autofill navigator against a real aggregator URL.

Run from the project root:
    python scripts/test_navigator.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from playwright.sync_api import sync_playwright

from career_ops.autofill.extractor import extract_form_fields
from career_ops.autofill.navigator import (
    click_best_apply,
    dismiss_cookie_banner,
    find_apply_candidates,
    is_aggregator,
    is_ats,
)

import json as _json
_jobs = _json.loads((ROOT / "data" / "scored_jobs.json").read_text(encoding="utf-8"))
_target_id = sys.argv[1] if len(sys.argv) > 1 else "0a11bd5cf12e36a2"  # Galderma Workday by default
_job = next(j for j in _jobs if j["id"] == _target_id)
URL = _job["url"]
print(f"\nJob: {_job['title']} @ {_job['company']}")

print(f"\n{'='*70}\nTesting navigator against: {URL[:80]}\n{'='*70}\n")

with sync_playwright() as pw:
    # Match production: visible browser. Cloudflare is much more permissive
    # to non-headless Chromium, so this matches what the real autofill does.
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()

    print("[1] Navigating to URL...")
    page.goto(URL, wait_until="domcontentloaded", timeout=45_000)
    try:
        page.wait_for_load_state("networkidle", timeout=10_000)
    except Exception as e:
        print(f"    networkidle timed out (ok): {e.__class__.__name__}")

    print(f"[2] Landed on: {page.url}")
    print(f"    is_aggregator: {is_aggregator(page.url)}")
    print(f"    is_ats:        {is_ats(page.url)}")

    print("[2.5] Dismissing cookie banner if present...")
    dismissed = dismiss_cookie_banner(page)
    print(f"    cookie banner dismissed: {dismissed}")

    print("[3] Extracting fields on landing page...")
    fields = extract_form_fields(page)
    print(f"    fields found: {len(fields)}")
    for f in fields[:5]:
        print(f"      - {f.field_type}: {f.label!r} (selector={f.selector[:60]})")

    print("[4] Looking for apply CTA candidates...")
    candidates = find_apply_candidates(page)
    print(f"    candidates found: {len(candidates)}")
    for c in candidates[:8]:
        text = c.get("text", "")[:60]
        href = c.get("href", "")[:80]
        print(f"      score={c['score']:3d} tag={c['tag']:6s} text={text!r} href={href!r}")

    if not candidates:
        # Dump *all* visible buttons/links to see what's actually there
        print("\n    [DEBUG] No candidates passed the score threshold. Dumping all clickables:")
        all_items = page.evaluate("""
            () => {
              const items = [];
              document.querySelectorAll('a, button, [role="button"]').forEach(el => {
                const r = el.getBoundingClientRect();
                if (r.width === 0 && r.height === 0) return;
                items.push({
                  tag: el.tagName.toLowerCase(),
                  text: (el.innerText || el.value || el.getAttribute('aria-label') || '').trim().slice(0,80),
                  href: el.getAttribute('href') || '',
                });
              });
              return items.filter(i => i.text);
            }
        """)
        for i in all_items[:30]:
            print(f"      {i['tag']:6s} text={i['text']!r}  href={i['href'][:60]!r}")

    print("\n[5] Attempting click_best_apply()...")
    print(f"    pages in context BEFORE click: {len(context.pages)}")
    for i, p in enumerate(context.pages):
        print(f"      [{i}] {p.url[:90]}")

    next_page = click_best_apply(page, context)
    print(f"    pages in context AFTER click: {len(context.pages)}")
    for i, p in enumerate(context.pages):
        print(f"      [{i}] {p.url[:90]}")

    if next_page is None:
        print("    -> click_best_apply returned None (no clickable CTA)")
    elif next_page is page:
        print(f"    -> same-tab navigation, now at: {page.url}")
    else:
        print(f"    -> popup tab opened, now at: {next_page.url}")
        page = next_page

    # Wait extra time in case the redirect is slow (JS-driven)
    print("\n[5.5] Waiting 10s for any slow redirect...")
    page.wait_for_timeout(10_000)
    print(f"    pages in context after wait: {len(context.pages)}")
    for i, p in enumerate(context.pages):
        print(f"      [{i}] {p.url[:90]}")
    # Switch to the most-recently-opened page if popup arrived late
    if len(context.pages) > 1:
        page = context.pages[-1]
        try:
            page.wait_for_load_state("domcontentloaded", timeout=15_000)
            page.wait_for_load_state("networkidle", timeout=10_000)
        except Exception:
            pass

    print(f"\n[6] After hop 1: URL = {page.url}")
    fields_after = extract_form_fields(page)
    print(f"    fields found after hop: {len(fields_after)}")
    for f in fields_after[:10]:
        print(f"      - {f.field_type}: label={f.label!r} name={f.name!r} sel={f.selector[:60]}")

    # Inspect whether jobsora is asking us to log in / showing a modal
    print("\n[7] Page title + first 300 chars of body text:")
    print(f"    title: {page.title()!r}")
    body_text = page.evaluate("() => document.body.innerText.slice(0, 500)")
    print(f"    body: {body_text!r}")

    # Look for modals or overlays that might have appeared after the click
    print("\n[8] Modals / overlays / login prompts visible:")
    modals = page.evaluate("""
        () => {
          const modals = [];
          document.querySelectorAll('[role="dialog"], .modal, [class*="modal"], [class*="popup"], [class*="overlay"]').forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.width === 0 && r.height === 0) return;
            const s = window.getComputedStyle(el);
            if (s.display === 'none' || s.visibility === 'hidden') return;
            modals.push({
              tag: el.tagName.toLowerCase(),
              cls: (el.className || '').toString().slice(0, 80),
              text: (el.innerText || '').trim().slice(0, 200),
            });
          });
          return modals;
        }
    """)
    for m in modals[:5]:
        print(f"      {m['tag']} class={m['cls']!r} text={m['text']!r}")

    browser.close()

print("\nTest complete.\n")
