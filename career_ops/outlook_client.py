"""Outlook email client via Microsoft Graph API.

Creates email **drafts** in the user's mailbox — never sends automatically.
Uses MSAL for OAuth2 token refresh.

Prerequisites:
  - Azure AD app registration with Mail.ReadWrite delegated permission
  - MS_GRAPH_CLIENT_ID, MS_GRAPH_CLIENT_SECRET, MS_GRAPH_TENANT_ID,
    MS_GRAPH_REFRESH_TOKEN, MS_GRAPH_USER_EMAIL in .env
"""
from __future__ import annotations

import base64
import logging
from pathlib import Path

import httpx
import msal

from .config import settings

logger = logging.getLogger(__name__)

_GRAPH_BASE = "https://graph.microsoft.com/v1.0"
_SCOPE = ["https://graph.microsoft.com/Mail.ReadWrite"]


def _get_access_token() -> str:
    """Acquire an access token using the stored refresh token."""
    app = msal.ConfidentialClientApplication(
        client_id=settings.ms_graph_client_id,
        client_credential=settings.ms_graph_client_secret,
        authority=f"https://login.microsoftonline.com/{settings.ms_graph_tenant_id}",
    )
    result = app.acquire_token_by_refresh_token(
        refresh_token=settings.ms_graph_refresh_token,
        scopes=_SCOPE,
    )
    if "access_token" not in result:
        raise RuntimeError(f"MS Graph token refresh failed: {result.get('error_description', result)}")
    return result["access_token"]


def _attach_files(message_id: str, token: str, files: list[Path]) -> None:
    """Attach files to an existing draft message."""
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    for file_path in files:
        if not file_path.exists():
            logger.warning("attachment not found: %s", file_path)
            continue
        content_bytes = file_path.read_bytes()
        payload = {
            "@odata.type": "#microsoft.graph.fileAttachment",
            "name": file_path.name,
            "contentBytes": base64.b64encode(content_bytes).decode("ascii"),
        }
        resp = httpx.post(
            f"{_GRAPH_BASE}/me/messages/{message_id}/attachments",
            headers=headers,
            json=payload,
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            logger.error("failed to attach %s: %s", file_path.name, resp.text[:200])
        else:
            logger.debug("attached %s to message %s", file_path.name, message_id)


def create_draft(draft) -> str:
    """Create a draft email in Outlook. Returns the message ID.

    Args:
        draft: An EmailDraft instance (from email_client.py).
    """
    token = _get_access_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    payload = {
        "subject": draft.subject,
        "body": {
            "contentType": "HTML",
            "content": draft.body_html,
        },
        "toRecipients": [
            {"emailAddress": {"address": draft.to}},
        ],
        "isDraft": True,
    }

    resp = httpx.post(
        f"{_GRAPH_BASE}/me/messages",
        headers=headers,
        json=payload,
        timeout=30,
    )

    if resp.status_code not in (200, 201):
        raise RuntimeError(f"Failed to create Outlook draft: {resp.status_code} {resp.text[:300]}")

    message_id = resp.json()["id"]
    logger.info("outlook: created draft %s — %s", message_id[:20], draft.subject)

    if draft.attachments:
        _attach_files(message_id, token, draft.attachments)

    return message_id
