"""Generate outreach copy for the Opella Brand Manager application.

Produces one tailored OutreachContent per contact (subject + email HTML +
LinkedIn connection note + LinkedIn InMail) and dumps them to
``data/outreach/<job_id>.json`` plus a human-readable Markdown summary at
``output/Opella - Brand Manager/Outreach.md``.

Email drafts are NOT created in a mailbox (no Outlook/Gmail configured in
.env). Paula will copy-paste from the Markdown file.
"""
from __future__ import annotations

import html
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings

settings.llm_provider = "anthropic"

from career_ops.analyzer import JobAnalysis  # noqa: E402
from career_ops.discovery.normalize import Job  # noqa: E402
from career_ops.generators.outreach import generate_outreach  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

OPELLA_JOB_ID = "f324f5af0ff41e06"


def _load_job():
    rec = next(
        r for r in json.loads((settings.data_dir / "scored_jobs.json").read_text(encoding="utf-8"))
        if r.get("id", "").startswith(OPELLA_JOB_ID)
    )
    job = Job(
        id=rec["id"], title=rec["title"], company=rec["company"],
        location=rec["location"], url=rec["url"], source=rec["source"],
        description=rec["description"],
    )
    analysis = JobAnalysis(
        score=rec.get("ai_score", 50), tier=rec.get("ai_tier", "Warm"),
        skills_match=rec.get("skills_match", []),
        missing_skills=rec.get("missing_skills", []),
        sector_fit=rec.get("sector_fit", ""), seniority_fit=rec.get("seniority_fit", ""),
        red_flags=rec.get("red_flags", []), ats_keywords=rec.get("ats_keywords", []),
        reasoning=rec.get("reasoning", ""),
    )
    return job, analysis


def main() -> None:
    job, analysis = _load_job()
    emails_path = settings.data_dir / "contacts" / f"{OPELLA_JOB_ID}.emails.json"
    contacts = json.loads(emails_path.read_text(encoding="utf-8"))

    print(f"[start] Generating outreach for {len(contacts)} contacts at Opella.")
    outreach_records = []
    for c in contacts:
        first_name = c["name"].split()[0]
        print(f"\n  [{c['role_type']}] {c['name']} — generating personalized copy...")
        content = generate_outreach(job, analysis, contact_name=first_name)
        if not content:
            print("    FAILED — skipping")
            continue
        rec = {
            "contact_name": c["name"],
            "contact_role": c["role_type"],
            "contact_title": c["title"],
            "linkedin_url": c["linkedin_url"],
            "primary_email": c["primary_email"],
            "primary_email_status": c["primary_email_status"],
            "email_subject": content.email_subject,
            "email_body_html": content.email_body,
            "linkedin_connection": content.linkedin_connection,
            "linkedin_inmail": content.linkedin_inmail,
            "notes": c.get("notes", ""),
        }
        outreach_records.append(rec)
        print(f"    subject: {content.email_subject}")

    # Persist JSON
    outreach_dir = settings.data_dir / "outreach"
    outreach_dir.mkdir(parents=True, exist_ok=True)
    json_path = outreach_dir / f"{OPELLA_JOB_ID}.json"
    json_path.write_text(json.dumps(outreach_records, indent=2, ensure_ascii=False), encoding="utf-8")

    # Persist human-readable Markdown
    md_path = settings.output_dir / "Opella - Brand Manager" / "Outreach.md"
    md_lines = [
        "# Opella Brand Manager — Outreach pack",
        "",
        f"Job URL: {job.url}",
        "",
        "Para cada contacto, abajo encontrarás 3 canales: **Email**, **LinkedIn connection note**, **LinkedIn InMail**. Copia-pega.",
        "",
        "> Email status: si dice `unverified`, el email es una conjetura por patrón corporativo (`firstname.lastname@opella.com`) sin verificar con Hunter.io. Mándalo y observa bounces, o verifica con un servicio antes.",
        "",
        "---",
    ]
    for r in outreach_records:
        md_lines += [
            "",
            f"## {r['contact_name']} — _{r['contact_role']}_",
            f"- **Title**: {r['contact_title']}",
            f"- **LinkedIn**: {r['linkedin_url']}",
            f"- **Email** ({r['primary_email_status']}): `{r['primary_email']}`",
            f"- **Why him/her**: {r['notes']}",
            "",
            f"### ✉️ Email — `{r['email_subject']}`",
            "```html",
            r["email_body_html"],
            "```",
            "",
            "Plain-text preview:",
            "",
            "> " + _html_to_text(r["email_body_html"]).replace("\n", "\n> "),
            "",
            "### 🔗 LinkedIn connection note (<=300 chars)",
            "```",
            r["linkedin_connection"],
            "```",
            "",
            "### 💬 LinkedIn InMail",
            "```",
            r["linkedin_inmail"],
            "```",
            "",
            "---",
        ]
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"\n[saved] {json_path}")
    print(f"[saved] {md_path}")
    print("Done.")


def _html_to_text(s: str) -> str:
    import re
    s = re.sub(r"<\s*br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p\s*>", "\n\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


if __name__ == "__main__":
    main()
