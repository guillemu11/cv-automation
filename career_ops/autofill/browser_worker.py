"""Singleton browser worker — one Chromium for the whole app.

The dashboard and every autofill run share a single visible Chromium window
with the persistent profile. The dashboard lives in tab 1; each autofill
opens a new tab in the same window.

Why a worker instead of running Playwright directly from FastAPI handlers:
Playwright's sync API uses greenlets and is **not thread-safe**. A single
context cannot be touched by FastAPI's worker threads. So we own one
dedicated thread that runs the Playwright loop, and FastAPI handlers post
jobs onto a Queue.

Lifecycle:
- ``BrowserWorker.start()`` spawns the thread and launches Chromium.
- ``BrowserWorker.submit_autofill(job, analysis)`` enqueues a job; the
  worker processes it in its own greenlet so Playwright stays happy.
- ``BrowserWorker.shutdown()`` is best-effort; we don't normally close
  Chromium because Paula likes keeping the dashboard tab open.

Resilience:
- If Paula closes the whole window, the worker detects that on its next
  poll and tears down the context. The next submission triggers a new
  ``_ensure_browser()`` which reopens everything (dashboard tab + autofill
  tab). She never has to restart the server.
"""
from __future__ import annotations

import logging
import os
import queue
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional

from ..config import settings

logger = logging.getLogger(__name__)


@dataclass
class _AutofillTask:
    job: Any           # career_ops.discovery.normalize.Job
    analysis: Any      # career_ops.analyzer.JobAnalysis


class BrowserWorker:
    """Owns the single Chromium instance + dashboard tab + autofill tabs."""

    def __init__(self, dashboard_url: str) -> None:
        self.dashboard_url = dashboard_url
        self._queue: queue.Queue[_AutofillTask] = queue.Queue()
        self._thread: Optional[threading.Thread] = None
        self._stopping = threading.Event()
        self._ready = threading.Event()
        self._started_lock = threading.Lock()
        self._mode: Optional[str] = None  # 'cdp' or 'managed', set by worker thread

    @property
    def mode(self) -> Optional[str]:
        """Return the current connection mode: 'cdp' (attached to user's Chrome)
        or 'managed' (we launched our own Chromium). None until ready."""
        return self._mode

    # -------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------

    def start(self) -> None:
        """Idempotent: starts the worker thread if it isn't running yet."""
        with self._started_lock:
            if self._thread and self._thread.is_alive():
                return
            self._stopping.clear()
            self._ready.clear()
            self._thread = threading.Thread(
                target=self._run, daemon=True, name="autofill-browser-worker",
            )
            self._thread.start()

    def submit_autofill(self, job, analysis) -> None:
        """Enqueue an autofill task. Starts the worker if it isn't running."""
        self.start()
        self._queue.put(_AutofillTask(job=job, analysis=analysis))

    def shutdown(self) -> None:
        self._stopping.set()
        self._queue.put(None)  # type: ignore[arg-type]
        if self._thread:
            self._thread.join(timeout=5)

    # -------------------------------------------------------------------
    # Worker thread — owns the Playwright greenlet
    # -------------------------------------------------------------------

    def _run(self) -> None:
        from playwright.sync_api import sync_playwright

        from .runner import _cleanup_stale_lockfile, run_autofill_in_tab

        profile_dir = settings.data_dir / "playwright_profile"
        profile_dir.mkdir(parents=True, exist_ok=True)
        _cleanup_stale_lockfile(profile_dir)

        # Connection mode: 'cdp' = attach to user's real Chrome, 'managed' = launch our own.
        # Decided on each (re)connect — if the user closes their Chrome and relaunches
        # without --remote-debugging-port, we automatically fall back to managed mode.
        cdp_port = int(os.environ.get("CAREEROPS_CDP_PORT", "9222"))

        try:
            with sync_playwright() as pw:
                context = None
                browser = None  # only set in CDP mode
                mode = None     # 'cdp' or 'managed'

                while not self._stopping.is_set():
                    # --- ensure the browser is alive ---
                    if context is None or self._context_dead(context, mode):
                        # Tear down anything left over
                        try:
                            if browser is not None and mode == "cdp":
                                # CDP: disconnect ONLY — never close the user's real Chrome
                                browser.close()  # disconnects in CDP mode; does not kill Chrome
                        except Exception:
                            pass
                        try:
                            if context is not None and mode == "managed":
                                context.close()
                        except Exception:
                            pass
                        context = None
                        browser = None
                        mode = None

                        # 1) Try CDP first
                        cdp_url = f"http://127.0.0.1:{cdp_port}"
                        try:
                            browser = pw.chromium.connect_over_cdp(cdp_url, timeout=2000)
                            # Use the user's existing context (with all their cookies/sessions),
                            # not a fresh one. Chrome always exposes the default context as [0].
                            if browser.contexts:
                                context = browser.contexts[0]
                            else:
                                context = browser.new_context()
                            mode = "cdp"
                            logger.info("browser_worker: attached to user's Chrome via CDP at %s", cdp_url)
                        except Exception as exc:
                            logger.info("browser_worker: CDP attach failed (%s); falling back to managed Chromium",
                                        exc.__class__.__name__)
                            browser = None
                            context = None

                        # 2) Fallback: managed Chromium with persistent profile
                        if context is None:
                            try:
                                context = pw.chromium.launch_persistent_context(
                                    user_data_dir=str(profile_dir),
                                    headless=False,
                                    viewport={"width": 1280, "height": 900},
                                    accept_downloads=True,
                                )
                                mode = "managed"
                            except Exception as exc:
                                logger.exception("browser_worker: failed to launch managed Chromium: %s", exc)
                                time.sleep(3)
                                continue

                        # Open the dashboard in a new tab. In CDP mode we NEVER touch
                        # the user's existing tabs — we add ours and that's it.
                        try:
                            dashboard_tab = context.new_page()
                            dashboard_tab.goto(self.dashboard_url, wait_until="domcontentloaded", timeout=30_000)
                            try:
                                dashboard_tab.bring_to_front()
                            except Exception:
                                pass
                        except Exception as exc:
                            logger.warning("browser_worker: dashboard tab failed to load: %s", exc)

                        self._mode = mode
                        self._ready.set()

                    # --- block waiting for a task ---
                    try:
                        task = self._queue.get(timeout=2.0)
                    except queue.Empty:
                        continue
                    if task is None:
                        break

                    # --- run the autofill in a NEW TAB of the same context ---
                    try:
                        run_autofill_in_tab(context, task.job, task.analysis)
                    except Exception:
                        logger.exception("browser_worker: autofill task crashed (job=%s)",
                                         getattr(task.job, "id", "?"))

                # --- final cleanup on shutdown ---
                if mode == "cdp":
                    # Disconnect from user's Chrome WITHOUT closing it
                    try:
                        if browser is not None:
                            browser.close()
                    except Exception:
                        pass
                elif mode == "managed":
                    try:
                        if context is not None:
                            context.close()
                    except Exception:
                        pass

        except Exception:
            logger.exception("browser_worker: fatal error in worker loop")
        finally:
            self._ready.clear()

    @staticmethod
    def _context_dead(context, mode: Optional[str]) -> bool:
        """True if we've effectively lost the browser session.

        In managed mode: all our pages are gone (user closed the window).
        In CDP mode: never declare 'dead' just because pages closed —
            the user's other tabs (gmail, banking, etc.) are still alive
            and we want to stay attached. Only true if the connection
            itself broke.
        """
        try:
            if mode == "cdp":
                # If we can iterate context.pages, we're still connected
                _ = list(context.pages)
                return False
            # managed mode
            return not any(not p.is_closed() for p in context.pages)
        except Exception:
            return True


# -------------------------------------------------------------------
# Module-level singleton — imported by FastAPI startup + endpoints
# -------------------------------------------------------------------

_singleton: Optional[BrowserWorker] = None
_singleton_lock = threading.Lock()


def get_worker(dashboard_url: str | None = None) -> BrowserWorker:
    """Return the process-wide BrowserWorker, creating it on first call."""
    global _singleton
    with _singleton_lock:
        if _singleton is None:
            if dashboard_url is None:
                raise RuntimeError("BrowserWorker requires dashboard_url on first call")
            _singleton = BrowserWorker(dashboard_url=dashboard_url)
        return _singleton
