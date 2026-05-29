"""Gmail email client via Google API.

Creates email **drafts** — never sends automatically.

Prerequisites:
  - Google Cloud project with Gmail API enabled
  - OAuth2 credentials (token JSON) stored in GMAIL_TOKEN_JSON env var
  - Run ``scripts/setup_gmail_token.py`` once to generate the token
"""
from __future__ import annotations

import base64
import json
import logging
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from .config import settings

logger = logging.getLogger(__name__)


def _get_service():
    """Build a Gmail API service from the stored token JSON."""
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    token_data = json.loads(settings.gmail_token_json)
    creds = Credentials.from_authorized_user_info(token_data)
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def _build_message(draft) -> str:
    """Build a base64url-encoded MIME message from an EmailDraft."""
    if draft.attachments:
        msg = MIMEMultipart()
        msg.attach(MIMEText(draft.body_html, "html", "utf-8"))

        for file_path in draft.attachments:
            if not file_path.exists():
                logger.warning("attachment not found: %s", file_path)
                continue
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file_path.read_bytes())
            from email import encoders
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={file_path.name}")
            msg.attach(part)
    else:
        msg = MIMEText(draft.body_html, "html", "utf-8")

    msg["to"] = draft.to
    msg["subject"] = draft.subject

    return base64.urlsafe_b64encode(msg.as_bytes()).decode("ascii")


def create_draft(draft) -> str:
    """Create a Gmail draft. Returns the draft ID.

    Args:
        draft: An EmailDraft instance (from email_client.py).
    """
    service = _get_service()
    raw = _build_message(draft)

    result = service.users().drafts().create(
        userId="me",
        body={"message": {"raw": raw}},
    ).execute()

    draft_id = result["id"]
    logger.info("gmail: created draft %s — %s", draft_id, draft.subject)
    return draft_id
