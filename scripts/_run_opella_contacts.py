"""Find Opella Dubai contacts (LinkedIn via Google) and enrich with emails.

Output:
  data/contacts/<job_id>.json — list of contact dicts (Contact.to_dict()).
  data/contacts/<job_id>.meta.json — metadata.
  data/contacts/<job_id>.emails.json — email candidates per contact, with
    Hunter.io verification when HUNTER_API_KEY is set.

The contacts JSON keeps the existing Contact shape so the dashboard renders
unchanged. The .emails.json sidecar is what we'll wire into the dashboard
later (Step 8 of the plan).
"""
from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.contact_finder import find_contacts
from career_ops.email_finder import domain_pattern, enrich_name

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(name)s  %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

OPELLA_JOB_ID = "f324f5af0ff41e06"
OPELLA_DOMAINS = ("opella.com", "opella.healthcare", "sanofi.com")


def main() -> None:
    scored_path = settings.data_dir / "scored_jobs.json"
    scored = json.loads(scored_path.read_text(encoding="utf-8"))
    job_data = next((r for r in scored if r.get("id", "").startswith(OPELLA_JOB_ID)), None)
    if not job_data:
        raise SystemExit(f"Job {OPELLA_JOB_ID} not found")

    print(f"[start] Finding contacts at {job_data['company']}...")

    # Force dry_run off (we want real SerpAPI hits).
    prev_dry = settings.dry_run
    settings.dry_run = False
    try:
        contacts = find_contacts(
            company=job_data["company"],
            job_title=job_data["title"],
            job_description=job_data["description"],
        )
    finally:
        settings.dry_run = prev_dry

    print(f"[contacts] Found {len(contacts)} contacts at Opella.")
    for c in contacts:
        print(f"  [{c.role_type}] {c.name} — {c.title}")
        print(f"    LinkedIn: {c.linkedin_url}")

    contacts_dir = settings.data_dir / "contacts"
    contacts_dir.mkdir(parents=True, exist_ok=True)
    contacts_path = contacts_dir / f"{OPELLA_JOB_ID}.json"
    meta_path = contacts_dir / f"{OPELLA_JOB_ID}.meta.json"
    emails_path = contacts_dir / f"{OPELLA_JOB_ID}.emails.json"

    contacts_path.write_text(
        json.dumps([c.to_dict() for c in contacts], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    meta_path.write_text(
        json.dumps({
            "searched_at": datetime.now(timezone.utc).isoformat(),
            "count": len(contacts),
            "company": job_data["company"],
            "job_title": job_data["title"],
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[saved] {contacts_path.name} + {meta_path.name}")

    # -------- Email enrichment --------
    print("\n[emails] Enriching candidates...")
    has_hunter = bool(settings.hunter_api_key)
    print(f"  Hunter.io: {'enabled' if has_hunter else 'NOT configured — patterns only, status=unverified'}")

    enriched = []
    for c in contacts:
        per_contact = {
            "name": c.name,
            "title": c.title,
            "linkedin_url": c.linkedin_url,
            "role_type": c.role_type,
            "candidates_by_domain": {},
        }
        for domain in OPELLA_DOMAINS:
            candidates = enrich_name(c.name, domain, max_verify=2)
            per_contact["candidates_by_domain"][domain] = [cand.to_dict() for cand in candidates]
        # Pick best primary email: first deliverable, else first candidate of primary domain
        primary = None
        for domain in OPELLA_DOMAINS:
            for cand in per_contact["candidates_by_domain"].get(domain, []):
                if cand["status"] == "deliverable":
                    primary = cand["email"]
                    break
            if primary:
                break
        if not primary and per_contact["candidates_by_domain"].get(OPELLA_DOMAINS[0]):
            primary = per_contact["candidates_by_domain"][OPELLA_DOMAINS[0]][0]["email"]
        per_contact["primary_email"] = primary
        per_contact["primary_email_status"] = "deliverable" if has_hunter and primary else "unverified"
        enriched.append(per_contact)
        print(f"  - {c.name}: {primary or '(could not split name)'} ({'verified' if per_contact['primary_email_status']=='deliverable' else 'unverified'})")

    emails_path.write_text(json.dumps(enriched, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[saved] {emails_path.name}")
    print("Done.")


if __name__ == "__main__":
    main()
