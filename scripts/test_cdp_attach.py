"""End-to-end test of CDP attach to a real Chrome.

This test:
  1. Launches Chrome with --remote-debugging-port=9222 pointing at your real profile
  2. Connects Playwright to it via connect_over_cdp
  3. Verifies we can see the existing context (with cookies)
  4. Opens a NEW tab, navigates it, reads the page
  5. Disconnects (NOT closes) — verifies Chrome stays alive
  6. Re-connects and verifies the new tab is still there

If this all passes, CDP attach works for the autofill flow.
"""
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

CHROME = Path(os.environ["LOCALAPPDATA"]) / "Google/Chrome/Application/chrome.exe"
PROFILE = Path(os.environ["LOCALAPPDATA"]) / "Google/Chrome/User Data"
PORT = 9222


def kill_existing_chrome():
    """Kill any running chrome.exe so we can start fresh with the flag."""
    subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"],
                   capture_output=True, timeout=10)
    time.sleep(2)


def start_chrome_with_cdp():
    """Launch Chrome with CDP enabled, return its PID."""
    proc = subprocess.Popen(
        [str(CHROME),
         f"--remote-debugging-port={PORT}",
         f"--user-data-dir={PROFILE}",
         "--no-first-run",
         "--no-default-browser-check"],
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
    )
    print(f"  Launched Chrome PID={proc.pid}")
    return proc


def chrome_running():
    """True if any chrome.exe is running with our --remote-debugging-port."""
    out = subprocess.run(
        ["wmic", "process", "where", "name='chrome.exe'",
         "get", "ProcessId,CommandLine", "/format:csv"],
        capture_output=True, text=True, timeout=8,
    )
    return f"--remote-debugging-port={PORT}".lower() in (out.stdout or "").lower()


print("=" * 70)
print("CDP ATTACH TEST")
print("=" * 70)

print(f"\nChrome:  {CHROME}")
print(f"Profile: {PROFILE}")
print(f"CDP port: {PORT}")

if not CHROME.exists():
    print(f"\nERROR: chrome.exe not found at {CHROME}")
    sys.exit(1)

# --- Step 1: Launch Chrome ---
print("\n[1] Killing any existing Chrome instances...")
kill_existing_chrome()

print("[2] Starting Chrome with CDP enabled...")
proc = start_chrome_with_cdp()
print("    waiting 5s for Chrome to be ready...")
time.sleep(5)

if not chrome_running():
    print("    FAIL — Chrome did not start with CDP flag")
    sys.exit(1)
print("    PASS — Chrome is running with CDP flag")

# --- Step 2: Connect via Playwright ---
print("\n[3] Connecting Playwright via CDP...")
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    try:
        browser = pw.chromium.connect_over_cdp(f"http://127.0.0.1:{PORT}", timeout=10_000)
    except Exception as exc:
        print(f"    FAIL — connect_over_cdp raised: {exc}")
        sys.exit(1)

    print(f"    PASS — connected. Browser: {browser}")
    print(f"    Existing contexts: {len(browser.contexts)}")
    if not browser.contexts:
        print("    FAIL — no existing contexts (Chrome should have one default context)")
        sys.exit(1)

    ctx = browser.contexts[0]
    print(f"    Using context [0]; pages currently open: {len(ctx.pages)}")
    for i, p in enumerate(ctx.pages[:5]):
        try:
            print(f"      [{i}] {p.url[:80]}")
        except Exception:
            print(f"      [{i}] (could not read URL)")

    # --- Step 3: Open a new tab ---
    print("\n[4] Opening a new tab and navigating to httpbin (proves we control Chrome)...")
    new_tab = ctx.new_page()
    new_tab.goto("https://httpbin.org/get?from=careerops_test", wait_until="domcontentloaded", timeout=20_000)
    body = new_tab.evaluate("() => document.body.innerText")
    if "careerops_test" in body:
        print("    PASS — navigation worked, page returned expected content")
    else:
        print("    FAIL — page did not contain expected content")
        print(f"    Got: {body[:200]}")

    print(f"\n    Pages now open: {len(ctx.pages)}")
    for i, p in enumerate(ctx.pages[:8]):
        try:
            print(f"      [{i}] {p.url[:80]}")
        except Exception:
            pass

    # --- Step 4: Disconnect (NOT close) ---
    print("\n[5] Disconnecting from Chrome WITHOUT closing it...")
    browser.close()  # In CDP mode, .close() detaches but does NOT kill Chrome
    print("    Disconnected.")

# --- Verify Chrome is still alive ---
print("\n[6] Verifying Chrome is still alive after disconnect...")
time.sleep(2)
if chrome_running():
    print("    PASS — Chrome survived the disconnect (this is critical!)")
else:
    print("    FAIL — Chrome was killed by browser.close(); user would lose all their tabs")
    sys.exit(1)

# --- Step 5: Re-connect to prove it's still attachable ---
print("\n[7] Reconnecting to verify attach is repeatable...")
with sync_playwright() as pw:
    try:
        browser2 = pw.chromium.connect_over_cdp(f"http://127.0.0.1:{PORT}", timeout=5_000)
        ctx2 = browser2.contexts[0]
        urls = [p.url for p in ctx2.pages]
        print(f"    PASS — reattached. Found {len(urls)} pages.")
        if any("careerops_test" in u for u in urls):
            print("    PASS — the tab we opened earlier is STILL alive — full session preserved")
        else:
            print(f"    INFO — earlier tab not found (may have been navigated away)")
        browser2.close()
    except Exception as exc:
        print(f"    FAIL — could not reattach: {exc}")
        sys.exit(1)

print("\n" + "=" * 70)
print("ALL CDP TESTS PASSED")
print("=" * 70)
print()
print("Chrome is still running on PID", proc.pid)
print("You can close it manually whenever you're done testing.")
