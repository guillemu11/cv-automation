"""Autofill ATS application forms using Playwright + Claude semantic mapping.

Public entry point: ``runner.run_autofill_async(job, analysis, dashboard_url)``
— used by the dashboard's ``/autofill`` endpoint. Submits an autofill task to
the singleton ``BrowserWorker``, which owns one Chromium window with the
dashboard in tab 1 and one tab per autofill task. Each tab generates form
responses if missing, extracts the form, asks Claude to map fields, fills
them, and stays open for human review and submission.
"""
from .runner import run_autofill_async, run_autofill_in_tab, get_status

__all__ = ["run_autofill_async", "run_autofill_in_tab", "get_status"]
