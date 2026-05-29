"""Daily digest — HTML email summarizing the pipeline run.

Generates an HTML summary with Hot/Warm/Cold counts and top job tables,
then creates it as a draft via the email client. Falls back to writing
an HTML file to ``output/`` if no email provider is configured.
"""
from __future__ import annotations

import logging
from datetime import date
from pathlib import Path

from .config import settings
from .email_client import EmailDraft, create_draft

logger = logging.getLogger(__name__)


def send_digest(result) -> None:
    """Generate and create a draft email with the daily digest.

    Args:
        result: A PipelineResult from pipeline.py.
    """
    html = _build_html(result)
    today = date.today().isoformat()

    draft = EmailDraft(
        to=settings.digest_to or "",
        subject=f"Career Ops Digest — {today} | {result.hot} Hot, {result.warm} Warm",
        body_html=html,
    )

    draft_id = create_draft(draft)
    if draft_id:
        logger.info("digest draft created: %s", draft_id)
    else:
        # No email client — write HTML to output/ as fallback
        out_path = settings.output_dir / f"digest_{today}.html"
        out_path.write_text(html, encoding="utf-8")
        logger.info("digest saved to %s (no email client configured)", out_path)


def _build_html(result) -> str:
    """Build the HTML body for the digest email."""
    today = date.today().strftime("%d %B %Y")

    hot_jobs = [(j, a) for j, a in result.scored_jobs if a.tier == "Hot"]
    warm_jobs = [(j, a) for j, a in result.scored_jobs if a.tier == "Warm"]

    hot_rows = _job_rows(hot_jobs[:10])
    warm_rows = _job_rows(warm_jobs[:10])

    errors_section = ""
    if result.errors:
        items = "".join(f"<li>{_esc(e)}</li>" for e in result.errors)
        errors_section = f"""
        <div style="margin-top:24px; padding:12px; background:#fef2f2; border-left:4px solid #ef4444; border-radius:4px;">
          <strong style="color:#991b1b;">Errors ({len(result.errors)})</strong>
          <ul style="margin:8px 0 0 0; padding-left:20px; color:#991b1b;">{items}</ul>
        </div>"""

    return f"""\
<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="font-family:system-ui,-apple-system,sans-serif; max-width:700px; margin:0 auto; padding:20px; color:#1a1a2e;">

<h1 style="font-size:22px; margin-bottom:4px;">Career Ops Daily Digest</h1>
<p style="color:#666; margin-top:0;">{today}</p>

<!-- Stats bar -->
<table style="width:100%; border-collapse:collapse; margin:20px 0;">
<tr>
  <td style="text-align:center; padding:12px; background:#f8fafc; border-radius:8px 0 0 8px;">
    <div style="font-size:24px; font-weight:700;">{result.discovered}</div>
    <div style="font-size:11px; color:#666; text-transform:uppercase;">Discovered</div>
  </td>
  <td style="text-align:center; padding:12px; background:#f8fafc;">
    <div style="font-size:24px; font-weight:700;">{result.dedupe_new}</div>
    <div style="font-size:11px; color:#666; text-transform:uppercase;">New</div>
  </td>
  <td style="text-align:center; padding:12px; background:#f8fafc;">
    <div style="font-size:24px; font-weight:700;">{result.filter_passed}</div>
    <div style="font-size:11px; color:#666; text-transform:uppercase;">Passed Filters</div>
  </td>
  <td style="text-align:center; padding:12px; background:#f8fafc; border-radius:0 8px 8px 0;">
    <div style="font-size:24px; font-weight:700;">{result.analyzed}</div>
    <div style="font-size:11px; color:#666; text-transform:uppercase;">Analyzed</div>
  </td>
</tr>
</table>

<!-- Tier badges -->
<div style="margin:20px 0; display:flex; gap:12px;">
  <span style="padding:6px 16px; border-radius:20px; background:#fef2f2; color:#dc2626; font-weight:600;">
    {result.hot} Hot
  </span>
  <span style="padding:6px 16px; border-radius:20px; background:#fffbeb; color:#d97706; font-weight:600;">
    {result.warm} Warm
  </span>
  <span style="padding:6px 16px; border-radius:20px; background:#eff6ff; color:#2563eb; font-weight:600;">
    {result.cold} Cold
  </span>
</div>

<!-- Hot jobs -->
{_section("Hot Jobs", "#ef4444", hot_rows) if hot_jobs else '<p style="color:#999;">No Hot jobs today.</p>'}

<!-- Warm jobs -->
{_section("Warm Jobs", "#f59e0b", warm_rows) if warm_jobs else ""}

{errors_section}

<!-- Footer -->
<p style="margin-top:32px; padding-top:16px; border-top:1px solid #e5e7eb; color:#999; font-size:12px;">
  Pipeline ran in {result.duration_seconds:.1f}s &middot;
  Notion: {result.notion_inserted} inserted, {result.notion_skipped} skipped
</p>

</body></html>"""


def _section(title: str, color: str, rows: str) -> str:
    """Build an HTML section with a colored header and job table."""
    return f"""
<h2 style="font-size:16px; margin-top:28px; padding-bottom:6px; border-bottom:2px solid {color};">
  {title}
</h2>
<table style="width:100%; border-collapse:collapse; font-size:13px;">
<tr style="background:#f8fafc;">
  <th style="text-align:left; padding:8px;">Title</th>
  <th style="text-align:left; padding:8px;">Company</th>
  <th style="text-align:center; padding:8px;">Score</th>
  <th style="text-align:left; padding:8px;">Why</th>
</tr>
{rows}
</table>"""


def _job_rows(jobs: list) -> str:
    """Build HTML table rows for a list of (Job, JobAnalysis) tuples."""
    rows = []
    for job, analysis in jobs:
        title_cell = f'<a href="{_esc(job.url)}" style="color:#2563eb;">{_esc(job.title[:50])}</a>' if job.url else _esc(job.title[:50])
        rows.append(f"""<tr style="border-bottom:1px solid #f0f0f0;">
  <td style="padding:8px;">{title_cell}</td>
  <td style="padding:8px;">{_esc(job.company[:30])}</td>
  <td style="padding:8px; text-align:center; font-weight:600;">{analysis.score}</td>
  <td style="padding:8px; color:#666; font-size:12px;">{_esc(analysis.reasoning[:100])}</td>
</tr>""")
    return "\n".join(rows)


def _esc(text: str) -> str:
    """Minimal HTML escaping."""
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
