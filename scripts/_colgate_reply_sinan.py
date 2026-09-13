"""Consolidate Colgate outreach onto the real job id + log Sinan's reply.

Two problems this fixes:
  1. Contacts/outreach for the Colgate Ecommerce Manager role were stored under
     job_id ``colgate_ecom_mgr_ae`` while the dashboard job card lives under
     ``colgate-ecom-174114`` (the real 174114 req). The card therefore showed
     ZERO contacts. We move contacts + meta + outreach onto the real id.
  2. Sinan Kaya replied to Paula's outreach asking for her CV by email
     (sinan_kaya@colpal.com) to forward to the hiring manager. We record the
     confirmed email, mark his status "replied", and store the ready reply.

Learned fact: Colgate corporate email pattern is firstname_lastname@colpal.com
(UNDERSCORE), confirmed by Sinan's own address.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops import outreach_store

OLD_ID = "colgate_ecom_mgr_ae"
NEW_ID = "colgate-ecom-174114"        # the real job card in scored_jobs.json
SINAN_LINKEDIN = "https://ae.linkedin.com/in/sinankaya1"
SINAN_EMAIL = "sinan_kaya@colpal.com"  # confirmed by Sinan directly

REPLY_SUBJECT = "Re: Ecommerce Manager – Paula De Francisco (CV attached)"
REPLY_BODY = (
    "Hi Sinan,\n\n"
    "Thank you — I really appreciate you offering to forward my CV to the hiring "
    "manager. Please find it attached.\n\n"
    "For context when you pass it along: I lead Brand & E-Commerce at DoFreeze "
    "here in Dubai, and previously spent two years at Alibaba's Miravia growing "
    "42 key accounts by +30% GMV QoQ. I've integrated brands hands-on into Noon, "
    "Talabat, Careem and Deliveroo, and I'm already on a UAE residence visa "
    "(no relocation or sponsorship needed).\n\n"
    "Happy to share more or jump on a quick call whenever useful. Thanks again "
    "for the help.\n\n"
    "Best regards,\n"
    "Paula De Francisco\n"
    "+971 50 386 3656 · paulich98@hotmail.com\n"
    "linkedin.com/in/paula-de-francisco-perez"
)


def _move_file(old: Path, new: Path) -> bool:
    if not old.exists():
        return False
    new.parent.mkdir(parents=True, exist_ok=True)
    new.write_text(old.read_text(encoding="utf-8"), encoding="utf-8")
    old.unlink()
    return True


def _consolidate_contacts() -> None:
    cdir = settings.data_dir / "contacts"
    moved = []
    for suffix in (".json", ".meta.json"):
        if _move_file(cdir / f"{OLD_ID}{suffix}", cdir / f"{NEW_ID}{suffix}"):
            moved.append(suffix)
    print(f"[contacts] moved {OLD_ID} -> {NEW_ID} ({', '.join(moved) or 'nothing'})")

    # Give Sinan his confirmed email so the dashboard surfaces the email button.
    cpath = cdir / f"{NEW_ID}.json"
    if cpath.exists():
        contacts = json.loads(cpath.read_text(encoding="utf-8"))
        for c in contacts:
            if c.get("linkedin_url") == SINAN_LINKEDIN:
                c["email"] = SINAN_EMAIL
                c["source"] = (c.get("source") or "") + " · email confirmed by contact"
        cpath.write_text(json.dumps(contacts, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[contacts] set Sinan email = {SINAN_EMAIL}")


def _consolidate_outreach() -> None:
    odir = settings.data_dir / "outreach"
    _move_file(odir / f"{OLD_ID}.json", odir / f"{NEW_ID}.json")
    print(f"[outreach] moved store {OLD_ID} -> {NEW_ID}")

    # Log Sinan's reply: append the ready reply email as the current version,
    # mark status "replied".
    cid = outreach_store.contact_id("Sinan Kaya", SINAN_LINKEDIN)
    body = f"Subject: {REPLY_SUBJECT}\n\n{REPLY_BODY}"
    outreach_store.add_version(NEW_ID, cid, "email", body)   # becomes current
    outreach_store.set_status(NEW_ID, cid, "replied")
    print(f"[outreach] Sinan ({cid}) -> reply email stored, status=replied")


def _bump_job_status() -> None:
    path = settings.data_dir / "scored_jobs.json"
    jobs = json.loads(path.read_text(encoding="utf-8"))
    for j in jobs:
        if j.get("id") == NEW_ID and j.get("status") in (None, "Inbox", "CV Ready"):
            j["status"] = "Applied"
            print(f"[job] {NEW_ID} status -> Applied")
    path.write_text(json.dumps(jobs, indent=2, ensure_ascii=False), encoding="utf-8")


def _write_reply_file() -> None:
    out_dir = settings.output_dir / "2026-07-05" / "Colgate-Palmolive - Ecommerce Manager" / "03_Outreach"
    out_dir.mkdir(parents=True, exist_ok=True)
    cv_rel = "../01_CV_y_Carta/CV_Paula_Colgate-Palmolive_Ecommerce_Manager.pdf"
    md = (
        "# Reply to Sinan Kaya — send from Paula's email\n\n"
        f"**To:** {SINAN_EMAIL}\n"
        f"**Subject:** {REPLY_SUBJECT}\n"
        f"**Attach:** `{cv_rel}` (the tailored Colgate CV)\n\n"
        "> Sinan (Head of Modern Trade UAE) replied to Paula's LinkedIn outreach "
        "and offered to forward her CV to the hiring manager. Send this from her "
        "hotmail (paulich98@hotmail.com), the address she applied with.\n\n"
        "---\n\n"
        f"{REPLY_BODY}\n"
    )
    p = out_dir / "REPLY_to_Sinan_Kaya.md"
    p.write_text(md, encoding="utf-8")
    print(f"[reply] wrote {p}")


def main() -> None:
    print("[start] Consolidating Colgate outreach + logging Sinan reply...")
    _consolidate_contacts()
    _consolidate_outreach()
    _bump_job_status()
    _write_reply_file()
    print("Done.")


if __name__ == "__main__":
    main()
