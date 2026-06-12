"""Inject the Colgate-Palmolive Ecommerce Manager outreach package.

Paula has already applied (CV sent) to the Ecommerce Manager role at
Colgate-Palmolive in Dubai. There is no campaign deliverable yet — the goal of
this pass is simply to *connect now* with the relevant people on the MENA
e-commerce / UAE commercial team, primarily via LinkedIn.

Like ``_inject_opella_contacts.py``, this is a dev-only one-shot. There are no
API keys in this environment (no SerpAPI for contact discovery, no Anthropic for
copy generation), so contacts were researched manually from public sources and
the outreach copy is authored directly here. It pre-populates exactly the files
the dashboard reads, so the job shows up with contacts + ready-to-send messages:

  - data/scored_jobs.json                    (adds the job card)
  - data/contacts/<job_id>.json + .meta.json (the 3 contacts)
  - data/outreach/<job_id>.json              (outreach_store dict, 3 variants each)
  - output/Colgate-Palmolive - Ecommerce Manager/Outreach.md  (copy-paste pack)

Contact research (public sources, June 2026):
  - Nikki Ramm   - Regional Manager, eCommerce & Digital Retail Media, MENA
                   (Dubai) — the direct owner of the area this role sits in;
                   most likely hiring manager / future manager. (theorg, ZoomInfo)
  - Murat Akyuz  - Country Manager, UAE (Dubai) — senior sign-off for UAE hires.
                   (RocketReach, theorg)
  - Sinan Kaya   - Head of Modern Trade, UAE (Dubai) — commercial peer; the
                   e-commerce / modern-trade bridge. (LinkedIn)

Corporate email domain is colpal.com (confirmed pattern n***@colpal.com on
ZoomInfo for Nikki Ramm). We deliberately leave Contact.email = None so the
dashboard surfaces the LinkedIn button (the intended channel). Unverified
pattern guesses are listed in the Markdown pack only, clearly flagged.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops import outreach_store

JOB_ID = "colgate_ecom_mgr_ae"
COMPANY = "Colgate-Palmolive"
ROLE = "Ecommerce Manager"
LOCATION = "Dubai, United Arab Emirates"
EMAIL_DOMAIN = "colpal.com"

JOB_DESCRIPTION = (
    "Colgate-Palmolive is a global consumer products leader (oral care, personal "
    "care, home care, skin care, pet nutrition) operating in over 200 countries. "
    "The Ecommerce Manager, based in Dubai, drives digital commerce growth across "
    "the MENA / Gulf region — owning the e-commerce P&L and channel strategy "
    "across pure-play and omnichannel retailers and quick-commerce platforms.\n\n"
    "Responsibilities:\n"
    "- Build and execute the e-commerce and digital-commerce strategy for the "
    "region, partnering with Customer Development and Brand/Marketing.\n"
    "- Own online assortment, content, pricing and promotional mechanics across "
    "key e-retailers and quick-commerce platforms (Noon, Talabat, Careem, etc.).\n"
    "- Plan and optimise retail media / digital shelf, tracking ROAS, conversion "
    "and traffic to hit sell-out and profitability targets.\n"
    "- Lead joint business planning with key digital accounts; manage A&P budget.\n"
    "- Drive the digital shelf, search and content agenda to grow market share.\n\n"
    "Requirements: 4+ years in FMCG e-commerce / digital commerce / key account "
    "management; strong analytical and P&L skills; UAE/GCC market experience; "
    "hands-on with e-retail and quick-commerce platforms."
)

# Outreach scored ~ exact match: FMCG e-commerce in UAE is squarely Paula's track.
JOB_RECORD = {
    "id": JOB_ID,
    "title": ROLE,
    "company": COMPANY,
    "location": LOCATION,
    "url": "https://jobs.colgate.com/key/marketing-manager-dubai.html",
    "source": "manual:paula-application",
    "description": JOB_DESCRIPTION,
    "salary_raw": None,
    "salary_aed_min": None,
    "salary_aed_max": None,
    "posted_date": datetime.now(timezone.utc).date().isoformat(),
    "raw": {"manually_injected": True, "application_sent": True},
    "ai_score": 90,
    "ai_tier": "Hot",
    "skills_match": [
        "UAE quick-commerce hands-on (Noon, Talabat, Careem, Deliveroo)",
        "E-commerce key account management (Alibaba/Miravia, 42 accounts)",
        "+30% GMV QoQ growth track record",
        "Retail media / ROAS / digital-shelf optimisation",
        "FMCG brand, trade & shopper marketing across 50+ markets",
        "E-store management, content & UX, promo mechanics",
    ],
    "missing_skills": [
        "Direct oral-/personal-care category experience",
        "Fluent Arabic (Spanish/English C1 only)",
    ],
    "sector_fit": "exact",
    "seniority_fit": "exact",
    "red_flags": [],
    "ats_keywords": [
        "Ecommerce Manager", "e-commerce", "digital commerce", "FMCG", "GCC",
        "MENA", "quick-commerce", "Noon", "Talabat", "Careem", "retail media",
        "ROAS", "GMV", "key account management", "P&L", "digital shelf",
    ],
    "reasoning": (
        "Near-perfect fit. FMCG e-commerce in the UAE is exactly Paula's lane: "
        "hands-on Noon/Talabat/Careem integration, Alibaba/Miravia key-account "
        "pedigree (+30% GMV QoQ), and retail-media/ROAS fluency, all from a Dubai "
        "base (residence visa, zero relocation). CV already submitted; this pass "
        "is to connect with the MENA e-commerce + UAE commercial team."
    ),
    "scored_by": "manual:paula-decision",
    "freshness": "fresh",
    "discovered_at": datetime.now(timezone.utc).isoformat(),
    "status": "Applied",
}


# -------------------------------------------------------------------
# Contacts (researched from public sources, June 2026)
# -------------------------------------------------------------------
CONTACTS = [
    {
        "name": "Nikki Ramm",
        "first": "Nikki",
        "title": "Regional Manager, eCommerce & Digital Retail Media — MENA, Colgate-Palmolive",
        "linkedin_url": "https://ae.linkedin.com/in/nikki-ramm-95417458",
        "role_type": "Hiring Manager",
        "email_guess": ["nikki.ramm@colpal.com", "nramm@colpal.com"],
        "notes": (
            "Owns e-commerce & digital retail media for the whole MENA region from "
            "Dubai — the function this role sits inside. Most likely the hiring "
            "manager or the person Paula would report to. This is the #1 connection."
        ),
    },
    {
        "name": "Murat Akyuz",
        "first": "Murat",
        "title": "Country Manager, UAE — Colgate-Palmolive",
        "linkedin_url": "https://ae.linkedin.com/in/murat-akyuz-430a8b17",
        "role_type": "Hiring Manager",
        "email_guess": ["murat.akyuz@colpal.com", "makyuz@colpal.com"],
        "notes": (
            "Country lead for the UAE — senior sign-off on local hires. A respectful "
            "intro here puts Paula's name in front of the top of the UAE org."
        ),
    },
    {
        "name": "Sinan Kaya",
        "first": "Sinan",
        "title": "Head of Modern Trade, UAE — Colgate-Palmolive",
        "linkedin_url": "https://ae.linkedin.com/in/sinankaya1",
        "role_type": "Peer",
        "email_guess": ["sinan.kaya@colpal.com", "skaya@colpal.com"],
        "notes": (
            "Commercial peer running UAE modern trade. E-commerce and modern trade "
            "win when planned together — a natural ally and a strong 'second touch'."
        ),
    },
]


# -------------------------------------------------------------------
# Outreach copy (authored directly — no LLM key in this environment)
# Each contact gets: linkedin_connection (<=300), linkedin_inmail, email.
# -------------------------------------------------------------------
OUTREACH = {
    "Nikki Ramm": {
        "linkedin_connection": (
            "Hi Nikki — I've just applied for the Ecommerce Manager role on your MENA "
            "team. I lead Brand & E-Commerce at DoFreeze in Dubai, after two years at "
            "Alibaba/Miravia (42 accounts, +30% GMV QoQ) and hands-on UAE q-commerce "
            "(Noon, Talabat, Careem). Would love to connect."
        ),
        "linkedin_inmail": (
            "Hi Nikki, I just applied for the Ecommerce Manager position on your MENA "
            "eCommerce & Digital Retail Media team and wanted to reach out directly. "
            "I'm currently leading Brand & E-Commerce for DoFreeze in Dubai, and before "
            "that spent two years as a Key Account Manager at Alibaba's Miravia — 42 "
            "accounts, +30% GMV QoQ — with hands-on integration of brands into Noon, "
            "Talabat, Careem and Deliveroo here in the UAE. The mix of FMCG brand work, "
            "retail-media/ROAS optimisation and on-the-ground GCC quick-commerce feels "
            "like a strong match for what your team is building. Would you be open to a "
            "short conversation?"
        ),
        "email_subject": "Ecommerce Manager (MENA) — Dubai q-commerce + Alibaba bg",
        "email_body": (
            "<p>Hi Nikki,</p>"
            "<p>I've just applied for the <strong>Ecommerce Manager</strong> role on "
            "your MENA eCommerce &amp; Digital Retail Media team and wanted to "
            "introduce myself directly.</p>"
            "<p>I currently lead Brand &amp; E-Commerce at DoFreeze in Dubai, and "
            "previously spent two years as a Key Account Manager at Alibaba's Miravia, "
            "where I grew <strong>42 accounts by +30% GMV QoQ</strong> through pricing, "
            "assortment and retail-media optimisation. Here in the UAE I've integrated "
            "brands hands-on into <strong>Noon, Talabat, Careem and Deliveroo</strong> — "
            "owning listings, promo mechanics and ROAS across the funnel.</p>"
            "<p>I'm Dubai-based on a residence visa, so there's no relocation or "
            "sponsorship to factor in. I'd love a brief conversation about how I could "
            "contribute to Colgate's e-commerce growth in the region.</p>"
            "<p>Best regards,<br>Paula De Francisco<br>"
            "+971 50 386 3656 · paulich98@hotmail.com</p>"
        ),
    },
    "Murat Akyuz": {
        "linkedin_connection": (
            "Hi Murat — I've just applied for the Ecommerce Manager role in your UAE "
            "organisation. I lead Brand & E-Commerce at DoFreeze in Dubai and bring "
            "hands-on Noon/Talabat/Careem experience plus an Alibaba/Miravia background "
            "(+30% GMV QoQ). Already Dubai-based. Would be glad to connect."
        ),
        "linkedin_inmail": (
            "Hi Murat, I recently applied for the Ecommerce Manager position within your "
            "UAE team at Colgate-Palmolive and wanted to connect. I lead Brand & "
            "E-Commerce at DoFreeze here in Dubai, with a background spanning Alibaba's "
            "Miravia (42 key accounts, +30% GMV QoQ) and hands-on UAE quick-commerce "
            "across Noon, Talabat, Careem and Deliveroo. As a Dubai resident already, I "
            "could step in without any relocation or sponsorship runway. I'd welcome the "
            "chance to briefly introduce myself."
        ),
        "email_subject": "Ecommerce Manager application — Colgate UAE",
        "email_body": (
            "<p>Dear Murat,</p>"
            "<p>I recently submitted my application for the <strong>Ecommerce "
            "Manager</strong> role within your UAE organisation and wanted to introduce "
            "myself.</p>"
            "<p>I currently lead Brand &amp; E-Commerce at DoFreeze in Dubai, following "
            "two years at Alibaba's Miravia where I managed 42 key accounts and "
            "delivered <strong>+30% GMV growth QoQ</strong>. I have hands-on UAE "
            "quick-commerce experience across <strong>Noon, Talabat, Careem and "
            "Deliveroo</strong>, alongside FMCG brand and trade-marketing work across "
            "50+ markets.</p>"
            "<p>I'm already based in Dubai on a residence visa — no relocation or "
            "sponsorship required. I'd be grateful for the opportunity to contribute to "
            "Colgate-Palmolive's growth in the UAE.</p>"
            "<p>Kind regards,<br>Paula De Francisco<br>"
            "+971 50 386 3656 · paulich98@hotmail.com</p>"
        ),
    },
    "Sinan Kaya": {
        "linkedin_connection": (
            "Hi Sinan — I've just applied for the Ecommerce Manager role at Colgate UAE. "
            "With modern-trade and UAE quick-commerce execution behind me (Noon, "
            "Talabat, Careem) plus an Alibaba/Miravia e-commerce background, I'd love to "
            "connect with the commercial team driving growth here in Dubai."
        ),
        "linkedin_inmail": (
            "Hi Sinan, I've just applied for the Ecommerce Manager role at "
            "Colgate-Palmolive UAE and wanted to reach out to the commercial side. I "
            "lead Brand & E-Commerce at DoFreeze in Dubai, and my background bridges "
            "modern trade and digital: I've integrated brands into Noon, Talabat, Careem "
            "and Deliveroo, and managed 42 key accounts at Alibaba's Miravia (+30% GMV "
            "QoQ). I believe e-commerce and modern trade win when they're planned "
            "together, and I'd love to connect."
        ),
        "email_subject": "Ecommerce Manager — bridging e-comm & modern trade",
        "email_body": (
            "<p>Hi Sinan,</p>"
            "<p>I've just applied for the <strong>Ecommerce Manager</strong> role at "
            "Colgate-Palmolive UAE and wanted to reach out to the commercial side of "
            "the business.</p>"
            "<p>I lead Brand &amp; E-Commerce at DoFreeze in Dubai, and my background "
            "bridges modern trade and digital. I've integrated brands hands-on into "
            "<strong>Noon, Talabat, Careem and Deliveroo</strong>, and managed 42 key "
            "accounts at Alibaba's Miravia, delivering <strong>+30% GMV QoQ</strong>. "
            "I'm a firm believer that e-commerce and modern trade perform best when "
            "they're planned as one.</p>"
            "<p>I'm Dubai-based on a residence visa. I'd love to connect and learn more "
            "about how the UAE commercial team is approaching omnichannel growth.</p>"
            "<p>Best regards,<br>Paula De Francisco<br>"
            "+971 50 386 3656 · paulich98@hotmail.com</p>"
        ),
    },
}

# Order in which the three variants are stored as versions. Current = v1 so the
# dashboard surfaces the LinkedIn connection note first (the channel Paula wants
# to use to "connect now").
VARIANT_ORDER = ["linkedin_connection", "linkedin_inmail", "email"]


def _html_to_text(s: str) -> str:
    s = re.sub(r"<\s*br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p\s*>", "\n\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def _upsert_job() -> None:
    path = settings.data_dir / "scored_jobs.json"
    jobs = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    jobs = [j for j in jobs if j.get("id") != JOB_ID]  # replace if re-run
    jobs.append(JOB_RECORD)
    path.write_text(json.dumps(jobs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[job] upserted '{ROLE} @ {COMPANY}' (id={JOB_ID}) into scored_jobs.json")


def _write_contacts() -> None:
    contacts_dir = settings.data_dir / "contacts"
    contacts_dir.mkdir(parents=True, exist_ok=True)

    contacts = [
        {
            "name": c["name"],
            "title": c["title"],
            "company": COMPANY,
            "email": None,  # keep None → dashboard shows LinkedIn button (intended channel)
            "linkedin_url": c["linkedin_url"],
            "role_type": c["role_type"],
            "source": "manual research (June 2026)",
        }
        for c in CONTACTS
    ]
    (contacts_dir / f"{JOB_ID}.json").write_text(
        json.dumps(contacts, indent=2, ensure_ascii=False), encoding="utf-8")
    (contacts_dir / f"{JOB_ID}.meta.json").write_text(
        json.dumps({
            "searched_at": datetime.now(timezone.utc).isoformat(),
            "count": len(contacts),
            "company": COMPANY,
            "job_title": ROLE,
            "source": "manual research (no SerpAPI key in env)",
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[contacts] wrote {len(contacts)} contacts + meta")


def _write_outreach() -> None:
    """Build the outreach_store dict directly (3 versions per contact)."""
    now = datetime.now(timezone.utc).isoformat()
    store: dict[str, dict] = {}
    for c in CONTACTS:
        cid = outreach_store.contact_id(c["name"], c["linkedin_url"])
        copy = OUTREACH[c["name"]]
        versions = []
        for i, variant in enumerate(VARIANT_ORDER, start=1):
            if variant == "email":
                body = f"Subject: {copy['email_subject']}\n\n{_html_to_text(copy['email_body'])}"
            else:
                body = copy[variant]
            versions.append({"v": i, "variant": variant, "body": body, "generated_at": now})
        store[cid] = {
            "versions": versions,
            "current_version": 1,          # surface the LinkedIn connection note first
            "status": "generated",
            "sent_at": None,
            "replied_at": None,
        }
    outreach_dir = settings.data_dir / "outreach"
    outreach_dir.mkdir(parents=True, exist_ok=True)
    (outreach_dir / f"{JOB_ID}.json").write_text(
        json.dumps(store, indent=2, ensure_ascii=False), encoding="utf-8")

    # Length sanity check for LinkedIn connection notes (<=300 chars).
    for c in CONTACTS:
        note = OUTREACH[c["name"]]["linkedin_connection"]
        flag = "OK" if len(note) <= 300 else "TOO LONG"
        print(f"[outreach] {c['name']}: connection note {len(note)} chars [{flag}]")


def _write_markdown() -> None:
    out_dir = settings.output_dir / f"{COMPANY} - {ROLE}"
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {COMPANY} — {ROLE}: Outreach pack",
        "",
        "CV already submitted. No campaign deliverable yet — the goal here is to "
        "**connect now** with the relevant people, primarily via LinkedIn.",
        "",
        "For each contact: **LinkedIn connection note** (send with the connect "
        "request), **LinkedIn InMail** (if you have InMail / once connected), and an "
        "**Email** (optional, secondary channel).",
        "",
        "> ⚠️ Emails are **unverified pattern guesses** on the `@colpal.com` corporate "
        "domain (confirmed domain, not the exact handle). LinkedIn is the reliable "
        "channel — lead with the connection note.",
        "",
        "**Suggested order:** Nikki Ramm first (she owns the area / likely your future "
        "manager), then Sinan Kaya (commercial peer), and Murat Akyuz as a senior "
        "courtesy touch.",
        "",
        "---",
    ]
    for c in CONTACTS:
        copy = OUTREACH[c["name"]]
        lines += [
            "",
            f"## {c['name']} — _{c['role_type']}_",
            f"- **Title**: {c['title']}",
            f"- **LinkedIn**: {c['linkedin_url']}",
            f"- **Email (unverified guess)**: `{c['email_guess'][0]}` "
            f"(alt: `{c['email_guess'][1]}`)",
            f"- **Why**: {c['notes']}",
            "",
            "### 🔗 LinkedIn connection note (≤300 chars)",
            "```",
            copy["linkedin_connection"],
            "```",
            "",
            "### 💬 LinkedIn InMail",
            "```",
            copy["linkedin_inmail"],
            "```",
            "",
            f"### ✉️ Email — `{copy['email_subject']}`",
            "",
            "> " + _html_to_text(copy["email_body"]).replace("\n", "\n> "),
            "",
            "---",
        ]
    md_path = out_dir / "Outreach.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[markdown] wrote {md_path}")


def main() -> None:
    print(f"[start] Injecting {COMPANY} {ROLE} outreach package...")
    _upsert_job()
    _write_contacts()
    _write_outreach()
    _write_markdown()
    print("Done.")


if __name__ == "__main__":
    main()
