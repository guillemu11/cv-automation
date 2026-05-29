#!/usr/bin/env python3
"""One-shot script: creates the Job Pipeline and Contacts databases in Notion.

Reads NOTION_TOKEN and NOTION_PARENT_PAGE_ID from .env, creates both DBs
with the full schema, and prints the IDs to paste back into .env.

Usage:
    python scripts/setup_notion_db.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from notion_client import Client

from career_ops.config import Settings
import career_ops.config as cfg

cfg.get_settings.cache_clear()
cfg.settings = Settings()

notion = Client(auth=cfg.settings.notion_token)
parent_page_id = cfg.settings.notion_parent_page_id

if not parent_page_id:
    print("ERROR: NOTION_PARENT_PAGE_ID not set in .env")
    sys.exit(1)


def create_job_pipeline() -> str:
    """Create the Job Pipeline database."""
    db = notion.databases.create(
        parent={"type": "page_id", "page_id": parent_page_id},
        title=[{"type": "text", "text": {"content": "Job Pipeline"}}],
        icon={"type": "emoji", "emoji": "🎯"},
        properties={
            "Job Title": {"title": {}},
            "Company": {"rich_text": {}},
            "Score": {"number": {"format": "number"}},
            "Priority": {
                "select": {
                    "options": [
                        {"name": "Hot", "color": "red"},
                        {"name": "Warm", "color": "yellow"},
                        {"name": "Cold", "color": "blue"},
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Inbox", "color": "default"},
                        {"name": "Analyzed", "color": "gray"},
                        {"name": "CV Ready", "color": "purple"},
                        {"name": "Applied", "color": "blue"},
                        {"name": "Followed Up", "color": "yellow"},
                        {"name": "Interview", "color": "orange"},
                        {"name": "Offer", "color": "green"},
                        {"name": "Rejected", "color": "red"},
                        {"name": "Withdrawn", "color": "brown"},
                    ]
                }
            },
            "Source": {
                "select": {
                    "options": [
                        {"name": "Indeed", "color": "blue"},
                        {"name": "LinkedIn", "color": "default"},
                        {"name": "Google Jobs", "color": "green"},
                        {"name": "Firecrawl", "color": "orange"},
                        {"name": "Apify", "color": "purple"},
                        {"name": "Referral", "color": "yellow"},
                    ]
                }
            },
            "Link": {"url": {}},
            "Sector": {
                "select": {
                    "options": [
                        {"name": "FMCG", "color": "green"},
                        {"name": "Beauty & Fragrances", "color": "pink"},
                        {"name": "E-commerce", "color": "purple"},
                        {"name": "F&B", "color": "orange"},
                        {"name": "Retail / Modern Trade", "color": "blue"},
                        {"name": "Luxury / Fashion", "color": "yellow"},
                        {"name": "Quick-commerce", "color": "red"},
                        {"name": "Consumer Goods", "color": "default"},
                        {"name": "Other", "color": "gray"},
                    ]
                }
            },
            "Seniority": {
                "select": {
                    "options": [
                        {"name": "Mid", "color": "blue"},
                        {"name": "Senior", "color": "green"},
                        {"name": "Lead", "color": "yellow"},
                        {"name": "Director", "color": "orange"},
                    ]
                }
            },
            "Salary Range": {"rich_text": {}},
            "Applied Date": {"date": {}},
            "Follow-up Date": {"date": {}},
            "Sector Fit": {"rich_text": {}},
            "Seniority Fit": {"rich_text": {}},
            "Analysis": {"rich_text": {}},
            "Skills Match": {"rich_text": {}},
            "Missing Skills": {"rich_text": {}},
            "ATS Keywords": {"rich_text": {}},
            "Red Flags": {"rich_text": {}},
            "Job ID": {"rich_text": {}},
        },
    )
    return db["id"]


def create_contacts() -> str:
    """Create the Contacts database."""
    db = notion.databases.create(
        parent={"type": "page_id", "page_id": parent_page_id},
        title=[{"type": "text", "text": {"content": "Contacts"}}],
        icon={"type": "emoji", "emoji": "👤"},
        properties={
            "Name": {"title": {}},
            "Company": {"rich_text": {}},
            "Role": {
                "select": {
                    "options": [
                        {"name": "Hiring Manager", "color": "green"},
                        {"name": "Director", "color": "blue"},
                        {"name": "HR Manager", "color": "yellow"},
                        {"name": "Recruiter", "color": "purple"},
                        {"name": "Talent Acquisition", "color": "orange"},
                        {"name": "Team Lead", "color": "default"},
                    ]
                }
            },
            "LinkedIn URL": {"url": {}},
            "Email": {"email": {}},
            "Source": {
                "select": {
                    "options": [
                        {"name": "Apollo", "color": "blue"},
                        {"name": "LinkedIn", "color": "default"},
                        {"name": "Company Website", "color": "green"},
                        {"name": "Manual", "color": "gray"},
                    ]
                }
            },
            "Notes": {"rich_text": {}},
        },
    )
    return db["id"]


if __name__ == "__main__":
    print("\n  Setting up Notion databases...")
    print(f"  Parent page: {parent_page_id}\n")

    print("  Creating Job Pipeline DB...", end=" ", flush=True)
    jobs_id = create_job_pipeline()
    print(f"OK  ->  {jobs_id}")

    print("  Creating Contacts DB...", end=" ", flush=True)
    contacts_id = create_contacts()
    print(f"OK  ->  {contacts_id}")

    print(f"\n  Add these to your .env:")
    print(f"  NOTION_DB_JOBS={jobs_id}")
    print(f"  NOTION_DB_CONTACTS={contacts_id}")
    print()
