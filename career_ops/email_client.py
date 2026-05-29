"""Email client router — delegates to Outlook (MS Graph) or Gmail.

All email operations create **drafts only** — nothing is ever sent
automatically. Paula reviews and sends manually.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

from .config import settings

logger = logging.getLogger(__name__)


@dataclass
class EmailDraft:
    """Payload for creating an email draft."""
    to: str
    subject: str
    body_html: str
    attachments: list[Path] = field(default_factory=list)


def create_draft(draft: EmailDraft) -> str:
    """Create a draft email via the configured provider.

    Returns the draft/message ID, or "" if no provider is configured.
    """
    if settings.ms_graph_refresh_token:
        from .outlook_client import create_draft as _outlook
        return _outlook(draft)

    if settings.gmail_token_json:
        from .gmail_client import create_draft as _gmail
        return _gmail(draft)

    logger.warning("No email client configured (set MS_GRAPH_REFRESH_TOKEN or GMAIL_TOKEN_JSON)")
    return ""
