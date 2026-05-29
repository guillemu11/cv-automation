"""Apply a list of FieldAction objects to a Playwright page.

Also handles automatic file uploads: for any ``<input type=file>`` whose
label mentions resume / CV / cover letter, attach the matching PDF from
``output/`` if it exists.
"""
from __future__ import annotations

import logging
from pathlib import Path

from playwright.sync_api import Page, TimeoutError as PWTimeout

from .extractor import FormField
from .mapper import FieldAction

logger = logging.getLogger(__name__)


class FillReport:
    """Result counters for one autofill run."""


    def __init__(self) -> None:
        self.filled: int = 0
        self.skipped: int = 0
        self.failed: int = 0
        self.uploaded: list[str] = []
        self.errors: list[str] = []

    def to_dict(self) -> dict:
        return {
            "filled": self.filled,
            "skipped": self.skipped,
            "failed": self.failed,
            "uploaded": self.uploaded,
            "errors": self.errors,
        }


def apply_actions(page: Page, actions: list[FieldAction]) -> FillReport:
    """Apply each action to the page. Best-effort, never raises on a bad field."""
    report = FillReport()

    for act in actions:
        if act.action == "skip":
            report.skipped += 1
            continue

        try:
            locator = page.locator(act.selector).first
            locator.scroll_into_view_if_needed(timeout=2000)

            if act.action == "fill":
                locator.fill(act.value, timeout=3000)
                report.filled += 1

            elif act.action == "select":
                try:
                    locator.select_option(label=act.value, timeout=2000)
                except PWTimeout:
                    locator.select_option(value=act.value, timeout=2000)
                report.filled += 1

            elif act.action == "check_radio":
                radio = page.locator(f'{act.selector}[value="{act.value}"]').first
                if radio.count() == 0:
                    radio = page.get_by_label(act.value, exact=False).first
                radio.check(timeout=2000)
                report.filled += 1

            elif act.action == "check":
                locator.check(timeout=2000)
                report.filled += 1

            elif act.action == "uncheck":
                locator.uncheck(timeout=2000)
                report.filled += 1

            else:
                report.skipped += 1

        except Exception as e:
            report.failed += 1
            report.errors.append(f"{act.selector}: {e.__class__.__name__}: {e}")
            logger.debug("autofill failed for %s: %s", act.selector, e)

    return report


def auto_upload_files(
    page: Page,
    fields: list[FormField],
    cv_path: Path | None,
    cover_path: Path | None,
    report: FillReport,
) -> None:
    """Attach the CV and cover-letter PDFs to file inputs whose label matches."""
    cv_kw = ("resume", "cv", "curriculum")
    cover_kw = ("cover", "letter", "carta", "presentacion", "presentación")

    for f in fields:
        if f.field_type != "file":
            continue
        label_lower = (f.label or "").lower() + " " + (f.name or "").lower()
        target: Path | None = None
        if any(k in label_lower for k in cv_kw):
            target = cv_path
        elif any(k in label_lower for k in cover_kw):
            target = cover_path

        if not target or not target.exists():
            continue

        try:
            page.locator(f.selector).first.set_input_files(str(target), timeout=3000)
            report.uploaded.append(f"{target.name} → {f.label or f.name}")
            report.filled += 1
        except Exception as e:
            report.failed += 1
            report.errors.append(f"upload {target.name}: {e}")
