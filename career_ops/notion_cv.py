"""Upload generated CV/CL info to Notion job pages.

Updates the job page with:
  - Status → "CV Ready"
  - A callout block with generated file info
  - The outreach messages (email + LinkedIn) as page content

File attachments (PDF) must be uploaded manually to the FILES property
in Notion (drag & drop) — the API doesn't support file uploads with
integration tokens.
"""
from __future__ import annotations

import logging
from datetime import date
from pathlib import Path

import httpx

from .config import settings

logger = logging.getLogger(__name__)

_HEADERS = {
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def _auth_headers() -> dict:
    return {**_HEADERS, "Authorization": f"Bearer {settings.notion_token}"}


def _find_page_by_job_id(job_id: str) -> str | None:
    """Find the Notion page ID for a given job ID."""
    resp = httpx.post(
        f"https://api.notion.com/v1/databases/{settings.notion_db_jobs}/query",
        headers=_auth_headers(),
        json={
            "filter": {
                "property": "Job ID",
                "rich_text": {"starts_with": job_id[:16]},
            }
        },
        timeout=15,
    )
    results = resp.json().get("results", [])
    if results:
        return results[0]["id"]
    return None


def update_job_with_cv(
    job_id: str,
    cv_path: Path | None = None,
    cl_path: Path | None = None,
    form_path: Path | None = None,
    outreach_email_subject: str = "",
    outreach_email_body: str = "",
    outreach_linkedin: str = "",
) -> bool:
    """Update a Notion job page after CV/CL generation.

    - Sets Status → "CV Ready"
    - Adds callout blocks with file info and outreach copy
    """
    if not settings.notion_token or not settings.notion_db_jobs:
        logger.warning("Notion not configured — skipping CV upload")
        return False

    page_id = _find_page_by_job_id(job_id)
    if not page_id:
        logger.warning("job %s not found in Notion", job_id[:8])
        return False

    headers = _auth_headers()
    today = date.today().isoformat()

    # 1. Update Status → CV Ready
    resp = httpx.patch(
        f"https://api.notion.com/v1/pages/{page_id}",
        headers=headers,
        json={"properties": {"Status": {"select": {"name": "CV Ready"}}}},
        timeout=15,
    )
    if resp.status_code != 200:
        logger.error("failed to update status: %s", resp.text[:200])
        return False

    # 2. Build content blocks
    blocks = []

    # CV info callout
    if cv_path:
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "📄"},
                "rich_text": [{"type": "text", "text": {
                    "content": f"CV personalizado generado — {today}\n{cv_path.name}"
                }}],
                "color": "purple_background",
            },
        })

    # Form responses callout
    if form_path:
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "\U0001f4cb"},
                "rich_text": [{"type": "text", "text": {
                    "content": f"Respuestas de formulario generadas \u2014 {today}\n{form_path.name}"
                }}],
                "color": "orange_background",
            },
        })

    # Cover letter info callout
    if cl_path:
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "✉️"},
                "rich_text": [{"type": "text", "text": {
                    "content": f"Cover letter generada — {today}\n{cl_path.name}"
                }}],
                "color": "blue_background",
            },
        })

    # Outreach copy
    if outreach_email_subject:
        blocks.append({
            "object": "block",
            "type": "heading_3",
            "heading_3": {
                "rich_text": [{"type": "text", "text": {"content": "Outreach Copy"}}],
            },
        })
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "📧"},
                "rich_text": [{"type": "text", "text": {
                    "content": f"Subject: {outreach_email_subject}\n\n{_strip_html(outreach_email_body)}"
                }}],
                "color": "yellow_background",
            },
        })

    if outreach_linkedin:
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "💼"},
                "rich_text": [{"type": "text", "text": {
                    "content": f"LinkedIn connection note:\n{outreach_linkedin}"
                }}],
                "color": "green_background",
            },
        })

    # 3. Append blocks to page
    if blocks:
        resp = httpx.patch(
            f"https://api.notion.com/v1/blocks/{page_id}/children",
            headers=headers,
            json={"children": blocks},
            timeout=15,
        )
        if resp.status_code != 200:
            logger.error("failed to add blocks: %s", resp.text[:200])
            return False

    logger.info("notion: updated %s → CV Ready with %d blocks", page_id[:12], len(blocks))
    return True


def _strip_html(html: str) -> str:
    """Rough HTML to plain text."""
    import re
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<p>", "", text)
    text = re.sub(r"</p>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()
