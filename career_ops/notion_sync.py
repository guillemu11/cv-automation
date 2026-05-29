"""Sync scored jobs and contacts to Notion databases.

Jobs go to the Job Pipeline DB; contacts go to the Contacts DB.
Duplicate detection is by Job ID (jobs) and name+company (contacts).
"""
from __future__ import annotations

import logging
from typing import Any

from notion_client import Client

from .analyzer import JobAnalysis
from .config import settings
from .contact_finder import Contact
from .discovery.normalize import Job

logger = logging.getLogger(__name__)

_SOURCE_MAP = {
    "indeed": "Indeed",
    "linkedin": "LinkedIn",
    "glassdoor": "Google Jobs",
    "google_jobs": "Google Jobs",
    "apify": "Apify",
    "firecrawl": "Firecrawl",
}


def _get_client() -> Client:
    if not settings.notion_token:
        raise RuntimeError("NOTION_TOKEN not set")
    return Client(auth=settings.notion_token)


def _truncate(text: str, max_len: int = 2000) -> str:
    """Notion rich_text blocks max out at 2000 chars."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def _rich_text(text: str) -> list[dict[str, Any]]:
    """Build a Notion rich_text array, splitting into 2000-char chunks if needed."""
    if not text:
        return []
    chunks = []
    for i in range(0, len(text), 2000):
        chunks.append({"type": "text", "text": {"content": text[i : i + 2000]}})
    return chunks


def _existing_job_ids(client: Client, db_id: str) -> set[str]:
    """Fetch all Job ID values already in the database to avoid duplicates."""
    import httpx

    ids: set[str] = set()
    cursor = None
    headers = {
        "Authorization": f"Bearer {settings.notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    while True:
        body: dict[str, Any] = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        resp = httpx.post(
            f"https://api.notion.com/v1/databases/{db_id}/query",
            headers=headers,
            json=body,
            timeout=30,
        )
        data = resp.json()
        if resp.status_code != 200:
            logger.warning("notion query failed: %s", data.get("message", resp.status_code))
            break
        for page in data.get("results", []):
            props = page.get("properties", {})
            job_id_prop = props.get("Job ID", {})
            rt = job_id_prop.get("rich_text", [])
            if rt:
                ids.add(rt[0].get("plain_text", ""))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return ids


def _build_page_properties(job: Job, analysis: JobAnalysis) -> dict[str, Any]:
    """Build the Notion page properties dict for a single job."""
    source_name = _SOURCE_MAP.get(job.source, job.source.title())

    props: dict[str, Any] = {
        "Job Title": {"title": [{"text": {"content": _truncate(job.title, 200)}}]},
        "Company": {"rich_text": _rich_text(job.company)},
        "Score": {"number": analysis.score},
        "Priority": {"select": {"name": analysis.tier}},
        "Status": {"select": {"name": "Analyzed"}},
        "Source": {"select": {"name": source_name}},
        "Analysis": {"rich_text": _rich_text(analysis.reasoning)},
        "Sector Fit": {"rich_text": _rich_text(analysis.sector_fit)},
        "Seniority Fit": {"rich_text": _rich_text(analysis.seniority_fit)},
        "Skills Match": {"rich_text": _rich_text(", ".join(analysis.skills_match))},
        "Missing Skills": {"rich_text": _rich_text(", ".join(analysis.missing_skills))},
        "ATS Keywords": {"rich_text": _rich_text(", ".join(analysis.ats_keywords))},
        "Job ID": {"rich_text": _rich_text(job.id)},
    }

    if job.url:
        props["Link"] = {"url": job.url}

    if job.salary_raw:
        props["Salary Range"] = {"rich_text": _rich_text(job.salary_raw)}

    if analysis.red_flags:
        props["Red Flags"] = {"rich_text": _rich_text(" | ".join(analysis.red_flags))}

    return props


def sync_jobs(scored_jobs: list[tuple[Job, JobAnalysis]]) -> dict[str, int]:
    """Insert scored jobs into the Notion Job Pipeline DB.

    Returns {"inserted": N, "skipped": M, "errors": E}.
    """
    if not settings.notion_db_jobs:
        logger.warning("NOTION_DB_JOBS not set — skipping Notion sync")
        return {"inserted": 0, "skipped": 0, "errors": 0}

    client = _get_client()
    db_id = settings.notion_db_jobs

    # Fetch existing job IDs to avoid duplicates
    existing = _existing_job_ids(client, db_id)
    logger.info("notion: %d existing jobs in DB", len(existing))

    inserted = 0
    skipped = 0
    errors = 0

    for job, analysis in scored_jobs:
        if job.id in existing:
            skipped += 1
            continue

        try:
            props = _build_page_properties(job, analysis)
            client.pages.create(
                parent={"database_id": db_id},
                properties=props,
            )
            inserted += 1
            logger.debug("notion: inserted %s — %s @ %s", job.id[:8], job.title, job.company)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            logger.error("notion: failed to insert %s: %s", job.id[:8], exc)

    logger.info("notion sync: inserted=%d skipped=%d errors=%d", inserted, skipped, errors)
    return {"inserted": inserted, "skipped": skipped, "errors": errors}


# -------------------------------------------------------------------
# Contacts sync
# -------------------------------------------------------------------

_ROLE_TYPE_MAP = {
    "Hiring Manager": "Hiring Manager",
    "HR/Recruiter": "Recruiter",
    "Peer": "Team Lead",
}


def _existing_contact_keys(client: Client, db_id: str) -> set[str]:
    """Fetch all (name, company) pairs already in the Contacts DB."""
    import httpx

    keys: set[str] = set()
    cursor = None
    headers = {
        "Authorization": f"Bearer {settings.notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    while True:
        body: dict[str, Any] = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        resp = httpx.post(
            f"https://api.notion.com/v1/databases/{db_id}/query",
            headers=headers,
            json=body,
            timeout=30,
        )
        data = resp.json()
        if resp.status_code != 200:
            logger.warning("notion contacts query failed: %s", data.get("message", resp.status_code))
            break
        for page in data.get("results", []):
            props = page.get("properties", {})
            name_prop = props.get("Name", {}).get("title", [])
            company_prop = props.get("Company", {}).get("rich_text", [])
            name = name_prop[0].get("plain_text", "") if name_prop else ""
            company = company_prop[0].get("plain_text", "") if company_prop else ""
            if name and company:
                keys.add(f"{name.lower()}|{company.lower()}")
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return keys


def sync_contacts(contacts: list[Contact]) -> dict[str, int]:
    """Insert contacts into the Notion Contacts DB.

    Deduplicates by (name + company). Returns {"inserted": N, "skipped": M, "errors": E}.
    """
    if not settings.notion_db_contacts:
        logger.warning("NOTION_DB_CONTACTS not set — skipping contacts sync")
        return {"inserted": 0, "skipped": 0, "errors": 0}

    client = _get_client()
    db_id = settings.notion_db_contacts

    existing = _existing_contact_keys(client, db_id)
    logger.info("notion contacts: %d existing contacts in DB", len(existing))

    inserted = 0
    skipped = 0
    errors = 0

    for contact in contacts:
        key = f"{contact.name.lower()}|{contact.company.lower()}"
        if key in existing:
            skipped += 1
            continue

        props: dict[str, Any] = {
            "Name": {"title": [{"text": {"content": contact.name}}]},
            "Company": {"rich_text": _rich_text(contact.company)},
            "Role": {"select": {"name": _ROLE_TYPE_MAP.get(contact.role_type, "Hiring Manager")}},
            "Source": {"select": {"name": contact.source}},
        }

        if contact.email:
            props["Email"] = {"email": contact.email}
        if contact.linkedin_url:
            props["LinkedIn URL"] = {"url": contact.linkedin_url}

        try:
            client.pages.create(
                parent={"database_id": db_id},
                properties=props,
            )
            inserted += 1
            existing.add(key)
            logger.debug("notion: inserted contact %s @ %s", contact.name, contact.company)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            logger.error("notion: failed to insert contact %s: %s", contact.name, exc)

    logger.info("notion contacts sync: inserted=%d skipped=%d errors=%d", inserted, skipped, errors)
    return {"inserted": inserted, "skipped": skipped, "errors": errors}
