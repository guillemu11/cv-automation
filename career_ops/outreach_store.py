"""Outreach message storage — per-job, per-contact JSON sidecar.

Each job has a file at data/outreach/<job_id>.json mapping a stable contact_id
(hash of name + linkedin_url) to its message history. Versions are appended,
never overwritten — regenerating preserves the previous draft so Paula can
revert if the new one is worse.

Status lifecycle: pending -> generated -> sent -> replied. Status lives at the
contact level (not per-version) because "sent" applies to whichever version
was the current_version at the time.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .config import settings

VARIANTS = ("linkedin_connection", "linkedin_inmail", "email")
STATUSES = ("pending", "generated", "sent", "replied")


def contact_id(name: str, linkedin_url: str | None) -> str:
    """Stable id for a contact within a job's outreach file.

    Uses linkedin_url when present (canonical), falls back to name. 10 hex
    chars is enough collision resistance for ~dozens of contacts per job.
    """
    key = (linkedin_url or name or "").strip().lower()
    return "c_" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:10]


@dataclass
class MessageVersion:
    v: int
    variant: str  # one of VARIANTS
    body: str
    generated_at: str  # ISO 8601

    def to_dict(self) -> dict:
        return {"v": self.v, "variant": self.variant, "body": self.body, "generated_at": self.generated_at}


@dataclass
class ContactOutreach:
    """All outreach state for one contact: versions + status."""
    versions: list[MessageVersion] = field(default_factory=list)
    current_version: int = 0  # 0 = no message yet
    status: str = "pending"
    sent_at: str | None = None
    replied_at: str | None = None

    def to_dict(self) -> dict:
        return {
            "versions": [v.to_dict() for v in self.versions],
            "current_version": self.current_version,
            "status": self.status,
            "sent_at": self.sent_at,
            "replied_at": self.replied_at,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ContactOutreach":
        versions = [MessageVersion(**v) for v in d.get("versions", [])]
        return cls(
            versions=versions,
            current_version=d.get("current_version", 0),
            status=d.get("status", "pending"),
            sent_at=d.get("sent_at"),
            replied_at=d.get("replied_at"),
        )

    def current(self) -> MessageVersion | None:
        if not self.versions or self.current_version == 0:
            return None
        for v in self.versions:
            if v.v == self.current_version:
                return v
        return self.versions[-1]


def _path(job_id: str) -> Path:
    out_dir = settings.data_dir / "outreach"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{job_id}.json"


def load(job_id: str) -> dict[str, ContactOutreach]:
    p = _path(job_id)
    if not p.exists():
        return {}
    with p.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return {cid: ContactOutreach.from_dict(d) for cid, d in raw.items()}


def save(job_id: str, data: dict[str, ContactOutreach]) -> None:
    p = _path(job_id)
    payload = {cid: c.to_dict() for cid, c in data.items()}
    with p.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def add_version(job_id: str, cid: str, variant: str, body: str) -> ContactOutreach:
    """Append a new version, set it as current, mark status=generated."""
    if variant not in VARIANTS:
        raise ValueError(f"unknown variant: {variant}")
    data = load(job_id)
    co = data.get(cid) or ContactOutreach()
    next_v = (co.versions[-1].v + 1) if co.versions else 1
    co.versions.append(MessageVersion(
        v=next_v,
        variant=variant,
        body=body,
        generated_at=datetime.now(timezone.utc).isoformat(),
    ))
    co.current_version = next_v
    if co.status == "pending":
        co.status = "generated"
    data[cid] = co
    save(job_id, data)
    return co


def set_current(job_id: str, cid: str, version: int) -> ContactOutreach | None:
    data = load(job_id)
    co = data.get(cid)
    if not co or not any(v.v == version for v in co.versions):
        return None
    co.current_version = version
    save(job_id, data)
    return co


def update_body(job_id: str, cid: str, body: str) -> ContactOutreach | None:
    """Edit the current version's body in place (manual edits by Paula)."""
    data = load(job_id)
    co = data.get(cid)
    if not co:
        return None
    cur = co.current()
    if not cur:
        return None
    cur.body = body
    save(job_id, data)
    return co


def set_status(job_id: str, cid: str, status: str) -> ContactOutreach | None:
    if status not in STATUSES:
        raise ValueError(f"unknown status: {status}")
    data = load(job_id)
    co = data.get(cid)
    if not co:
        return None
    co.status = status
    now = datetime.now(timezone.utc).isoformat()
    if status == "sent" and not co.sent_at:
        co.sent_at = now
    if status == "replied" and not co.replied_at:
        co.replied_at = now
    save(job_id, data)
    return co
