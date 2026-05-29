"""End-to-end test of BrowserWorker — dashboard tab + autofill tab share one Chromium.

Spins up a tiny HTTP server with a fake "dashboard" page and a fake "form" page,
starts a BrowserWorker pointing at the dashboard, submits an autofill task,
verifies that:
  1. The worker opens ONE Chromium with the dashboard in tab 1
  2. The autofill opens a SECOND tab in the same context (not a new browser)
  3. Both tabs are alive simultaneously
  4. Closing the autofill tab does not kill the dashboard tab
"""
import http.server
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# A "dashboard" and a "form" page on the same local server
HTML_DASHBOARD = b"""<html><head><title>Career Ops Dashboard</title></head>
<body><h1>DASHBOARD</h1><p>This is the dashboard tab.</p></body></html>"""

HTML_FORM = b"""<html><head><title>Apply</title></head><body>
<h1>Application form</h1>
<form>
  <label>Name<input name=name></label>
  <label>Email<input name=email type=email></label>
  <label>Phone<input name=phone type=tel></label>
  <label>Why<textarea name=why></textarea></label>
  <button type=submit>Submit</button>
</form></body></html>"""


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        if "/form" in self.path:
            self.wfile.write(HTML_FORM)
        else:
            self.wfile.write(HTML_DASHBOARD)

    def log_message(self, *a, **k):
        pass


srv = http.server.HTTPServer(("127.0.0.1", 9913), TestHandler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
time.sleep(0.3)
print("Mock server up at http://127.0.0.1:9913 (/=dashboard /form=form)")

# A fake Job pointing at /form so the runner navigates there
from dataclasses import dataclass


@dataclass
class FakeJob:
    id: str
    url: str
    company: str
    title: str
    location: str
    description: str = ""


@dataclass
class FakeAnalysis:
    score: int = 80
    tier: str = "Hot"
    skills_match: list = None
    missing_skills: list = None
    sector_fit: str = ""
    seniority_fit: str = ""
    red_flags: list = None
    ats_keywords: list = None
    reasoning: str = ""


# Patch _ensure_form_responses so the test doesn't need the LLM
from career_ops.autofill import runner as runner_mod
runner_mod._ensure_form_responses = lambda j, a, jid: {
    "responses": {
        "full_name": "Paula De Francisco",
        "email": "paula@example.com",
        "phone": "+971 50 000 0000",
        "why_interested": "Aligned with my passion for the sector",
        "why_good_fit": "I scaled influencer programmes to 50+ creators",
    }
}
# Patch map_fields too — no LLM in tests; produce trivial fill actions
from career_ops.autofill import mapper as mapper_mod


def fake_map_fields(fields, responses):
    from career_ops.autofill.mapper import FieldAction
    out = []
    for f in fields:
        if "name" in (f.label or "").lower() or "name" in (f.name or "").lower():
            out.append(FieldAction(selector=f.selector, action="fill", value="Paula De Francisco"))
        elif "email" in (f.label or "").lower() or "email" in (f.name or "").lower():
            out.append(FieldAction(selector=f.selector, action="fill", value="paula@example.com"))
        elif "phone" in (f.label or "").lower() or "phone" in (f.name or "").lower():
            out.append(FieldAction(selector=f.selector, action="fill", value="+971 50 000 0000"))
        elif "why" in (f.label or "").lower() or "why" in (f.name or "").lower():
            out.append(FieldAction(selector=f.selector, action="fill", value="My answer."))
        else:
            out.append(FieldAction(selector=f.selector, action="skip"))
    return out


mapper_mod.map_fields = fake_map_fields


# Build a worker — but force headless for testing by monkey-patching the run loop
from career_ops.autofill.browser_worker import BrowserWorker
from playwright.sync_api import sync_playwright


def headless_run(self):
    """Replacement for BrowserWorker._run that uses headless=True for testing."""
    profile_dir = ROOT / "data" / "playwright_profile_test"
    profile_dir.mkdir(parents=True, exist_ok=True)
    # Clean any previous test profile lockfile
    lockfile = profile_dir / "lockfile"
    if lockfile.exists():
        try:
            lockfile.unlink()
        except Exception:
            pass

    import queue as _q
    from career_ops.autofill.runner import run_autofill_in_tab

    with sync_playwright() as pw:
        context = None
        while not self._stopping.is_set():
            if context is None or self._context_dead(context):
                if context is not None:
                    try:
                        context.close()
                    except Exception:
                        pass
                context = pw.chromium.launch_persistent_context(
                    user_data_dir=str(profile_dir),
                    headless=True,    # TEST ONLY
                    viewport={"width": 1280, "height": 900},
                )
                # Open dashboard in tab 1
                p = context.pages[0] if context.pages else context.new_page()
                p.goto(self.dashboard_url, wait_until="domcontentloaded", timeout=15_000)
                self._ready.set()
                # Expose for assertions
                self._test_context = context

            try:
                task = self._queue.get(timeout=1.0)
            except _q.Empty:
                continue
            if task is None:
                break

            try:
                run_autofill_in_tab(context, task.job, task.analysis)
            except Exception as exc:
                print(f"  [worker error] {type(exc).__name__}: {exc}")

        if context is not None:
            try:
                context.close()
            except Exception:
                pass


BrowserWorker._run = headless_run

# Run the actual end-to-end test
print("\n=== Test ===")
worker = BrowserWorker(dashboard_url="http://127.0.0.1:9913/")
worker.start()

# Wait for browser ready
print("Waiting for worker to launch Chromium + dashboard tab...")
worker._ready.wait(timeout=30)
print(f"  Worker ready at t={time.time():.1f}")
ctx = worker._test_context
print(f"  Tabs open: {len(ctx.pages)}")
for i, p in enumerate(ctx.pages):
    print(f"    [{i}] {p.url}")
assert len(ctx.pages) == 1, f"Expected 1 tab (dashboard), got {len(ctx.pages)}"
assert "9913" in ctx.pages[0].url, f"Dashboard tab URL wrong: {ctx.pages[0].url}"
print("  PASS — dashboard tab open")

# Submit an autofill task
print("\nSubmitting autofill task...")
fake_job = FakeJob(
    id="testjob01",
    url="http://127.0.0.1:9913/form",
    company="TestCo",
    title="Senior Brand Manager",
    location="Dubai",
)
worker.submit_autofill(fake_job, FakeAnalysis())

# Wait for the autofill to open a 2nd tab
print("Waiting for autofill tab to appear...")
deadline = time.time() + 20
while time.time() < deadline:
    if len(ctx.pages) >= 2:
        break
    time.sleep(0.5)

print(f"  Tabs open: {len(ctx.pages)}")
for i, p in enumerate(ctx.pages):
    print(f"    [{i}] {p.url}")
assert len(ctx.pages) >= 2, f"Expected >=2 tabs (dashboard + autofill), got {len(ctx.pages)}"
print("  PASS — autofill opened in a SECOND tab of the SAME browser")

# Wait until the autofill reaches awaiting_human, then close its tab
print("\nWaiting for autofill to reach awaiting_human...")
from career_ops.autofill.runner import get_status

deadline = time.time() + 20
while time.time() < deadline:
    s = get_status("testjob01")
    if s.get("stage") in ("awaiting_human", "error", "done"):
        break
    time.sleep(0.5)

final = get_status("testjob01")
print(f"  Final stage: {final.get('stage')}")
print(f"  Final report: {final.get('report')}")

# Find the autofill tab (not the dashboard) and close it
autofill_tab = next((p for p in ctx.pages if "/form" in p.url), None)
if autofill_tab is None:
    print("  ! Could not find autofill tab to close")
else:
    autofill_tab.close()
    print("  Closed autofill tab")
    time.sleep(2)
    print(f"  Remaining tabs: {len(ctx.pages)}")
    for i, p in enumerate(ctx.pages):
        print(f"    [{i}] {p.url}")

# Verify the dashboard tab is STILL alive
alive = [p for p in ctx.pages if not p.is_closed()]
dashboard_alive = any("9913" in p.url and "/form" not in p.url for p in alive)
if dashboard_alive:
    print("  PASS — dashboard tab survived autofill close")
else:
    print("  FAIL — dashboard tab was killed when autofill closed")

worker.shutdown()
print("\nAll done.")
