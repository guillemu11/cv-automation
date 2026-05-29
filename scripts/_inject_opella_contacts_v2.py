"""v2 expansion of the Opella contact list.

The original Opella posting was pulled, so the strategy shifts from
"apply to a specific role" to "speculative outreach into the AMET org".
This v2 expands the contact list from 5 to 13, covering:

  A-tier (Hiring Manager / decision-maker):  Murali Rao, Duygu Cetin
  B-tier (Country / Commercial sign-off):    Hossam Abo Ouf, Pelit Duman,
                                              Marianne Abou Elkheir
  C-tier (Peer brand managers):              Olivia Stefanelli (NY referral),
                                              Sid Ali Bentarcha
  D-tier (Cross-functional peers):           Shahab Mirza, Ahsan Rizvi,
                                              Amal Fathy
  E-tier (Referral nodes / alumni):          Rashmi Gupta, Ahmed El Kamhawy,
                                              Jamal Ali

All LinkedIn URLs verified via WebSearch (May 2026). Email pattern is
``firstname.lastname@opella.com`` (the Opella corporate pattern confirmed via
ZoomInfo / RocketReach public listings). Hunter.io verification still
pending — Paula has not added a HUNTER_API_KEY. Status remains ``unverified``.

Idempotent: overwrites ``data/contacts/<job_id>.json`` and ``.emails.json``.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.contact_finder import Contact
from career_ops.email_finder import enrich_name

OPELLA_JOB_ID = "f324f5af0ff41e06"
PRIMARY_DOMAIN = "opella.com"

# Note: Amal Fathy is the only special case — her email at ZoomInfo (May 2026)
# still showed @sanofi.com because the Sanofi → Opella spin-off (Oct 2024) may
# not have fully migrated the Science Hub team yet. We try both domains for her.
SANOFI_LEGACY_DOMAIN = "sanofi.com"

# Curated list. Sources listed inline (web research May 2026, last verified
# via WebSearch on opella.com / linkedin.com snippets / ZoomInfo / RocketReach).
CONTACTS = [
    # ===========================================================
    # A-tier — Hiring Manager / decision-maker
    # ===========================================================
    {
        "name": "Murali Rao",
        "title": "Head of Brand & Innovation, AMET (Africa, Middle East, Turkey) — Opella",
        "linkedin_url": "https://tr.linkedin.com/in/murali-rao",
        "role_type": "Hiring Manager",
        "tier": "A",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Direct decision-maker for AMET brand roles. Stepped into role Apr 2026 "
            "(succeeded Rashmi Gupta). 22+ years FMCG/CHC, prior at Reckitt and "
            "FrieslandCampina. Based in Istanbul, covers UAE."
        ),
    },
    {
        "name": "Duygu Cetin",
        "title": "Head of Brand & Innovation / Regional Marketing Director — AMET — Opella",
        "linkedin_url": "https://www.linkedin.com/in/duygu-%C3%A7etin-abbbbb227/",
        "role_type": "Hiring Manager",
        "tier": "A",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Senior brand & innovation lead in the AMET zone alongside Murali Rao "
            "(Turkey-based). Strong second touch if Murali doesn't bite — same "
            "circle, same authority level."
        ),
    },
    # ===========================================================
    # B-tier — Country / Commercial sign-off
    # ===========================================================
    {
        "name": "Hossam Abo Ouf",
        "title": "Country Head, KSA & UAE — Opella",
        "linkedin_url": "https://sa.linkedin.com/in/hossam-abo-ouf-75102b11",
        "role_type": "Hiring Manager",
        "tier": "B",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Country lead for the UAE geography. Likely co-signs local marketing "
            "hires. Prior: Sanofi Head of Operations KSA & UAE, Boehringer "
            "Ingelheim, Pfizer. Based in Riyadh; oversees Dubai office."
        ),
    },
    {
        "name": "Pelit Duman",
        "title": "Country General Manager, Turkiye — Opella",
        "linkedin_url": "https://tr.linkedin.com/in/pelit-duman",
        "role_type": "Peer",
        "tier": "B",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "GM Türkiye, appointed 2025 (per PharmaWorld Dergisi). Strategic "
            "context but not the UAE hirer. Useful for understanding the AMET "
            "operating model + cross-country pollination."
        ),
    },
    {
        "name": "Marianne Abou Elkheir",
        "title": "Head Africa Middle Markets Partner — Opella",
        "linkedin_url": "https://www.linkedin.com/in/marianne-abou-elkheir-57826028",
        "role_type": "Hiring Manager",
        "tier": "B",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Paris-based but covers Africa+Middle East commercial. ZoomInfo "
            "confirmed @opella.com email. Prior at Boehringer Ingelheim, Medtronic, "
            "Janssen and J&J — Paula's FMCG track will resonate."
        ),
    },
    # ===========================================================
    # C-tier — Peer Brand Managers (would be future colleagues)
    # ===========================================================
    {
        "name": "Olivia Stefanelli",
        "title": "Senior Brand Manager — Opella (NY Metro)",
        "linkedin_url": "https://www.linkedin.com/in/olivia-stefanelli-68369159/",
        "role_type": "Peer",
        "tier": "C",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "NOT in AMET — based in NYC, U-Michigan Ross MBA. Doing the exact role "
            "Paula wants, one geo away. Excellent peer-to-peer warm intro source: "
            "'Hi Olivia, applying to the AMET version of your role and would value 15 min'."
        ),
    },
    {
        "name": "Sid Ali Bentarcha",
        "title": "Opella (role TBD via LinkedIn login)",
        "linkedin_url": "https://www.linkedin.com/in/sid-ali-bentarcha-628b1824/",
        "role_type": "Peer",
        "tier": "C",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Confirmed Opella employee per public LinkedIn snippet, exact title not "
            "surfaced in Google. Likely brand or commercial role given last name "
            "appearing alongside AMET team mentions. Worth a connection request to "
            "learn role."
        ),
    },
    # ===========================================================
    # D-tier — Cross-functional peers
    # ===========================================================
    {
        "name": "Shahab Fraz Mirza",
        "title": "Trade & Revenue Management Head, AMET — Opella",
        "linkedin_url": "https://ae.linkedin.com/in/shahab-fraz-mirza",
        "role_type": "Peer",
        "tier": "D",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Based in UAE — Opella Dubai office. Strong commercial counterpart to "
            "brand roles. Useful for an in-person second touch once warm with Murali."
        ),
    },
    {
        "name": "Ahsan Rizvi",
        "title": "Digital Lead, AMET — Opella",
        "linkedin_url": "https://www.linkedin.com/in/ahsanrizvi/",
        "role_type": "Peer",
        "tier": "D",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Digital lead for AMET — natural ally given Paula's UAE quick-commerce "
            "experience (Noon, Talabat, Careem). Email confirmed @opella.com via "
            "RocketReach."
        ),
    },
    {
        "name": "Amal Fathy",
        "title": "AMET Science Hub Head, Sanofi CHC / Opella",
        "linkedin_url": "https://eg.linkedin.com/in/amal-fathy-5a621b140",
        "role_type": "Peer",
        "tier": "D",
        "domains": [PRIMARY_DOMAIN, SANOFI_LEGACY_DOMAIN],
        "notes": (
            "Egypt-based. Scientific affairs — NOT brand, but holds context on which "
            "Opella brands have an active medical pipeline in AMET. Useful background "
            "before pitching specific brand opportunities. ZoomInfo showed her email "
            "as @sanofi.com — likely still on the legacy domain post-spin-off."
        ),
    },
    # ===========================================================
    # E-tier — Referral nodes / alumni
    # ===========================================================
    {
        "name": "Rashmi Gupta",
        "title": "Former Head of Brand & Innovation AMET, Opella — now London",
        "linkedin_url": "https://www.linkedin.com/in/rashmi-gupta-674a283/",
        "role_type": "HR/Recruiter",
        "tier": "E",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Built AMET Brand & Innovation from scratch; handed off to Murali in "
            "Apr 2026. Strong referral node — a warm intro from her to Murali would "
            "carry weight."
        ),
    },
    {
        "name": "Ahmed El Kamhawy",
        "title": "AMET Leadership Team — Opella (role TBD)",
        "linkedin_url": "https://www.linkedin.com/in/ahmed-el-kamhawy-48b9a763/",
        "role_type": "Peer",
        "tier": "E",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Confirmed AMET Leadership Team member per Opella internal comms (Apr 2026). "
            "Background in consumer products + pharma. Egypt-based likely. Useful "
            "horizontal contact across the AMET zone."
        ),
    },
    {
        "name": "Jamal Ali",
        "title": "Opella (role TBD via LinkedIn login)",
        "linkedin_url": "https://www.linkedin.com/in/jamal-ali-4b44b145/",
        "role_type": "Peer",
        "tier": "E",
        "domains": [PRIMARY_DOMAIN],
        "notes": (
            "Confirmed Opella employee per public LinkedIn snippet. Worth a low-cost "
            "connection request to learn role."
        ),
    },
]


def main() -> None:
    has_hunter = bool(settings.hunter_api_key)
    print(f"[start] Injecting {len(CONTACTS)} Opella contacts (v2 expansion).")
    print(f"[setup] Hunter.io: {'ENABLED' if has_hunter else 'NOT configured — patterns only, status=unverified'}")

    # --- Build the Contact dataclass list for the dashboard JSON ---
    contacts = [
        Contact(
            name=c["name"],
            title=c["title"],
            company="Opella",
            email=None,
            linkedin_url=c["linkedin_url"],
            role_type=c["role_type"],
            source="manual research v2 (May 2026)",
        )
        for c in CONTACTS
    ]

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
            "company": "Opella",
            "job_title": "Brand Manager",
            "source": "manual research v2 — original posting pulled, speculative outreach",
            "version": 2,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[saved] {contacts_path.name}")

    # --- Email enrichment per contact ---
    print("\n[emails] enriching candidates...")
    enriched = []
    for raw in CONTACTS:
        record = {
            "name": raw["name"],
            "title": raw["title"],
            "linkedin_url": raw["linkedin_url"],
            "role_type": raw["role_type"],
            "tier": raw["tier"],
            "notes": raw["notes"],
            "candidates_by_domain": {},
        }
        primary = None
        for domain in raw["domains"]:
            candidates = enrich_name(raw["name"], domain, max_verify=2)
            record["candidates_by_domain"][domain] = [c.to_dict() for c in candidates]
            if not primary and candidates:
                primary = candidates[0].email
        record["primary_email"] = primary
        record["primary_email_status"] = "deliverable" if has_hunter else "unverified"
        enriched.append(record)
        print(f"  [{raw['tier']}] {raw['name']}: {primary}")

    emails_path.write_text(json.dumps(enriched, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[saved] {emails_path.name}")

    # --- A bit of summary so we can paste into the README ---
    print("\nSummary by tier:")
    by_tier: dict[str, list] = {}
    for r in CONTACTS:
        by_tier.setdefault(r["tier"], []).append(r["name"])
    for tier in "ABCDE":
        if tier in by_tier:
            print(f"  {tier}: {len(by_tier[tier])}  →  {', '.join(by_tier[tier])}")
    print("\nDone.")


if __name__ == "__main__":
    main()
