"""Build a personalized outreach pack as a Word document (the canonical
Paula-format).

Per Paula's feedback after the Opella v2 pass — every outreach deliverable
must follow this shape:

  - One .docx with a cover (job + landings + sequence)
  - One section per contact ranked by tier (A high → E low)
  - Each section: Title / LinkedIn / Email / Why this contact
    + Email (subject + body, both Vercel URLs embedded inline as <a href>)
    + LinkedIn connection note (<=300 chars, one URL)
    + LinkedIn InMail (longer variant)

The pack reads ``data/contacts/<job_id>.emails.json`` (produced by the
``career_ops.email_finder`` pipeline) and ``data/scored_jobs.json``.

Usage:

  python scripts/build_outreach_pack.py \\
      --job-id f324f5af0ff41e06 \\
      --landing "Buscopan:https://paula-pitch-a.vercel.app:late-night quick-commerce for the UAE" \\
      --landing "Doliprane:https://paula-pitch-b.vercel.app:MENA Francophone diaspora launch" \\
      --mode speculative \\
      --out output/Opella_Outreach_Pack.docx

Modes:
  - ``speculative``  — posting was pulled or no posting exists. Email never
                       says "I saw your posting" or "Application for X".
  - ``applied``      — posting is active. Email opens by acknowledging it.

The LLM provider is forced to anthropic (the project default LLM_PROVIDER
is often ``chatqueue`` which blocks waiting for a human reply).
"""
from __future__ import annotations

import html
import json
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import click

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings

settings.llm_provider = "anthropic"

from career_ops import llm  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-5s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------
# Landing spec parsing
# ---------------------------------------------------------------------

@dataclass
class Landing:
    title: str
    url: str
    desc: str

    @classmethod
    def parse(cls, raw: str) -> "Landing":
        """``Title:URL:Description`` — handles colons inside URL (https://).

        Strategy: locate the ``https?://`` substring. Title is everything
        before the first colon. URL ends at the first colon *after* the
        protocol's ``://``. Description is everything after that.
        """
        m = re.search(r"https?://", raw)
        if not m:
            raise click.BadParameter(
                f"--landing must contain an http(s) URL, got: {raw!r}"
            )
        first_colon = raw.find(":")
        if first_colon < 0 or first_colon > m.start():
            raise click.BadParameter(
                f"--landing must start with 'Title:URL:Description', got: {raw!r}"
            )
        title = raw[:first_colon].strip()
        rest = raw[first_colon + 1 :]                       # "URL:Description"
        after_proto = rest.find("://") + 3
        sep = rest.find(":", after_proto)
        if sep < 0:
            raise click.BadParameter(
                f"--landing missing description after URL, got: {raw!r}"
            )
        url = rest[:sep].strip()
        desc = rest[sep + 1 :].strip()
        if not title or not url or not desc:
            raise click.BadParameter(
                f"--landing has empty Title/URL/Description, got: {raw!r}"
            )
        return cls(title=title, url=url, desc=desc)


@dataclass
class Attachment:
    """A file (e.g. the FULL deck PDF) attached to the email — NOT a URL.

    Referenced in the body as an attachment ("I've attached..."), never
    hyperlinked, since it travels with the email rather than living online.
    """
    title: str
    desc: str

    @classmethod
    def parse(cls, raw: str) -> "Attachment":
        """``Title:Description`` — no URL involved."""
        if ":" not in raw:
            raise click.BadParameter(
                f"--attachment must be 'Title:Description', got: {raw!r}"
            )
        title, desc = raw.split(":", 1)
        title, desc = title.strip(), desc.strip()
        if not title or not desc:
            raise click.BadParameter(
                f"--attachment has empty Title/Description, got: {raw!r}"
            )
        return cls(title=title, desc=desc)


# ---------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------

_SYSTEM_TEMPLATE = """\
You write concise, compelling outreach for Paula De Francisco, a Brand/
Marketing Manager based in Dubai. She is targeting {company} ({mode_phrase}).

Tone: professional, intelligent, concrete, never sycophantic, never
self-impressed, never AI-slop (no "passionate", "innovative", "leverage",
"unleash", "synergy", "I came across your profile", "I hope this finds you
well", "cutting-edge", "revolutionary").

Each message must reference Paula's speculative campaign landing(s) already
deployed online:

{landings_block}

CRITICAL: the email body must NATURALLY weave in {url_count_phrase} as
clickable hyperlinks, one sentence describing each. They are distinct
strategic angles — embed them inline in a sentence, not pasted at the end.
{attachments_block}

Rules:
1. Email subject: under 60 chars, specific.
   {mode_subject_rule}
2. Email body: HTML with <p> tags. 5-7 sentences. Open with a SPECIFIC
   observation about {company}, the contact's domain, or the market — not
   a compliment. Land the landing URL(s) naturally. End with a soft ask
   (15 min call, opinion on the angles, an introduction).
3. LinkedIn connection note: MUST be under 300 characters. One sentence
   about why connecting + one about what you bring. Reference ONE landing
   only — pick the one most relevant to the contact's domain. Always
   include the URL.
4. LinkedIn InMail: 3-5 sentences, slightly more detailed than the
   connection note.
5. Tailor the angle to the contact's tier:
   - A-tier (Hiring Manager) → pitch directly, landing URL(s) prominent
   - B-tier (Country head)   → frame as commercial opportunity per geography
   - C-tier (Peer Brand Mgr) → peer-to-peer 15-min ask, one URL as seed
   - D-tier (Cross-functional) → angle to their function
   - E-tier (Referral node)  → ask for a warm intro to the right hirer
6. {mode_framing_rule}

Output via the submit_outreach tool. The email_body MUST be valid HTML with
<p> tags. URLs MUST appear as <a href="...">...</a> tags inside it.
"""


_TOOL = {
    "name": "submit_outreach",
    "description": "Submit all outreach copy for this contact",
    "input_schema": {
        "type": "object",
        "properties": {
            "email_subject": {"type": "string"},
            "email_body": {"type": "string", "description": "HTML with <p> tags, MUST include landing URL(s) as <a href> hyperlinks inline"},
            "linkedin_connection": {"type": "string", "description": "<=300 chars, must include the most relevant landing URL"},
            "linkedin_inmail": {"type": "string"},
        },
        "required": ["email_subject", "email_body", "linkedin_connection", "linkedin_inmail"],
    },
}


def _build_system_prompt(company: str, landings: list[Landing], mode: str,
                         attachments: list[Attachment] | None = None) -> str:
    attachments = attachments or []
    landings_block = "\n".join(
        f"  - {l.title} ({l.desc}). Live at: {l.url}" for l in landings
    )
    if attachments:
        att_lines = "\n".join(f"  - {a.title}: {a.desc}" for a in attachments)
        attachments_block = (
            "\nPaula is ALSO attaching the following PDF to the email "
            "(a file, travelling with the message — NOT a link):\n"
            f"{att_lines}\n"
            "Reference the attached PDF naturally in ONE sentence (e.g. "
            "\"I've attached the full proposal — a short pitch deck plus the "
            "trade & shopper plan behind it\"). It is an ATTACHMENT: never "
            "wrap it in <a href>, never give it a URL. The deck and the live "
            "landing(s) are complementary — the landing is the quick online "
            "look, the PDF is the depth."
        )
    else:
        attachments_block = ""
    if mode == "speculative":
        mode_phrase = (
            "no public posting is active right now — the play is speculative "
            "outreach into the org before a referral closes the gap"
        )
        mode_subject_rule = (
            "NEVER use 'Application for' (it is wrong without an active "
            "posting). Use angles like 'Two {company} campaign concepts' or "
            "specific pitch hooks."
        ).format(company=company)
        mode_framing_rule = (
            f"NEVER reference 'the open position' or 'your job posting' for "
            f"{company} — there is none active. Frame as 'I wanted to share "
            "two campaign concepts I built' or similar speculative framing."
        )
    else:  # applied
        mode_phrase = "she is applying for a posted role"
        mode_subject_rule = (
            f"You may reference the specific role (e.g. 'Application: <role> "
            f"@ {company}') but lead with substance not the job title."
        )
        mode_framing_rule = (
            "You may acknowledge the posting in the opening but do not "
            "linger — get to the campaign concepts in sentence 2."
        )
    url_count_phrase = "all the URLs" if len(landings) > 1 else "the URL"
    return _SYSTEM_TEMPLATE.format(
        company=company,
        mode_phrase=mode_phrase,
        landings_block=landings_block,
        attachments_block=attachments_block,
        url_count_phrase=url_count_phrase,
        mode_subject_rule=mode_subject_rule,
        mode_framing_rule=mode_framing_rule,
    )


# ---------------------------------------------------------------------
# Per-contact LLM call
# ---------------------------------------------------------------------

def generate_for_contact(contact: dict, job: dict, company: str,
                          landings: list[Landing], system_prompt: str,
                          attachments: list[Attachment] | None = None) -> dict:
    first_name = contact["name"].split()[0]
    urls_block = "\n".join(f"  - {l.title} ({l.desc}): {l.url}" for l in landings)
    attachments = attachments or []
    att_block = "\n".join(f"  - {a.title} (attached PDF): {a.desc}" for a in attachments)
    user = f"""\
## Contact
- Name: {contact['name']}
- Use first name: {first_name}
- Title: {contact['title']}
- LinkedIn: {contact['linkedin_url']}
- Email (pattern-guess, unverified): {contact['primary_email']}
- Tier: {contact['tier']}  ({contact['role_type']})
- Strategic notes about this contact:
  {contact['notes']}

## Target context
- Company: {company}
- Job title: {job.get('title','(unspecified)')}
- Job location: {job.get('location','(unspecified)')}

## Paula's differentiators (use sparingly, only where relevant)
- 4 years FMCG + UAE quick-commerce execution (Noon, Talabat, Careem, Deliveroo)
- +30% GMV QoQ at Alibaba/Miravia across 42 key accounts
- Mondelez + Inditex foundation, Spanish/English C1, already in Dubai with visa

## Landings to embed (as inline <a href> hyperlinks)
{urls_block}

## Attached PDF(s) — reference as an attachment, NEVER as a link
{att_block if att_block else "  (none)"}

Use the submit_outreach tool. The email body MUST be HTML and MUST contain
the landing URL(s) as inline <a href> hyperlinks (one sentence each, woven
in naturally — not pasted at the end). If a PDF is attached, mention it in
one sentence as an attachment (no URL, no <a href> on it)."""

    data = llm.generate_structured(
        system=system_prompt, user=user, tool_schema=_TOOL,
        tier="sonnet", max_tokens=1500, temperature=0.4,
    )
    if not data:
        raise RuntimeError(f"empty LLM response for {contact['name']}")
    conn = data.get("linkedin_connection", "")
    if len(conn) > 300:
        data["linkedin_connection"] = conn[:297] + "..."
    return data


# ---------------------------------------------------------------------
# HTML → readable paragraphs (preserves URLs as 'text (url)')
# ---------------------------------------------------------------------

def html_to_paragraphs(html_str: str) -> list[str]:
    s = html_str

    def _anchor_repl(m: re.Match) -> str:
        href = m.group(1).strip()
        label = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if label and label != href:
            return f"{label} ({href})"
        return href

    s = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', _anchor_repl, s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    parts = re.split(r"</p\s*>", s, flags=re.I)
    out = []
    for p in parts:
        text = re.sub(r"<[^>]+>", "", p)
        text = html.unescape(text)
        text = re.sub(r"[ \t]+", " ", text)
        text = text.strip()
        if text:
            out.append(text)
    return out


# ---------------------------------------------------------------------
# Word builder
# ---------------------------------------------------------------------

def build_docx(records: list[dict], company: str, landings: list[Landing],
               mode: str, out_path: Path,
               attachments: list[Attachment] | None = None) -> None:
    attachments = attachments or []
    from docx import Document
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    doc.add_heading(f"{company} — Outreach Pack", level=0)

    sub = doc.add_paragraph()
    if mode == "speculative":
        msg = (
            f"Speculative outreach to {len(records)} {company} contacts. No active "
            "posting; the play is to insert directly into the org before a "
            "referral closes the gap."
        )
    else:
        msg = (
            f"Outreach to {len(records)} {company} contacts following an "
            "active job application."
        )
    r = sub.add_run(msg)
    r.italic = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    doc.add_heading("Deliverables to include", level=2)
    for l in landings:
        p = doc.add_paragraph()
        p.add_run(f"{l.title} (live landing) — ").bold = True
        p.add_run(f"{l.desc}:  ")
        p.add_run(l.url)
    for a in attachments:
        p = doc.add_paragraph()
        p.add_run(f"{a.title} (attached PDF) — ").bold = True
        p.add_run(a.desc)

    doc.add_heading("Suggested outreach sequence", level=2)
    seq = doc.add_paragraph(
        "A-tier first (they decide). C-tier (peer at same role, different geo) "
        "is the strongest warm-intro path. E-tier (alumni / referral nodes) as "
        "pressure if A-tier is silent by week 3. One contact per day max — "
        "don't let them compare notes."
    )

    doc.add_page_break()

    for i, rec in enumerate(records, start=1):
        c = rec["contact"]
        o = rec["outreach"]
        head = doc.add_heading(f"{i:02d}. {c['name']}", level=1)
        head.paragraph_format.keep_with_next = True

        meta = doc.add_paragraph()
        meta.add_run(c["title"]).italic = True
        meta.add_run(f"   ·   Tier {c['tier']}   ·   {c['role_type']}").italic = True

        link_p = doc.add_paragraph()
        link_p.add_run("LinkedIn:  ").bold = True
        link_p.add_run(c["linkedin_url"])
        email_p = doc.add_paragraph()
        email_p.add_run("Email:  ").bold = True
        email_p.add_run(f"{c['primary_email']}  (status: {c['primary_email_status']})")

        if c.get("notes"):
            n = doc.add_paragraph()
            n_run = n.add_run(f"Why this contact:  {c['notes']}")
            n_run.font.size = Pt(9)
            n_run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

        doc.add_heading("Email", level=3)
        s = doc.add_paragraph()
        s.add_run("Subject:  ").bold = True
        s.add_run(o["email_subject"])
        for para in html_to_paragraphs(o["email_body"]):
            doc.add_paragraph(para)

        doc.add_heading("LinkedIn connection note (<=300 chars)", level=3)
        doc.add_paragraph(o["linkedin_connection"])

        doc.add_heading("LinkedIn InMail", level=3)
        doc.add_paragraph(o["linkedin_inmail"])

        sep = doc.add_paragraph()
        sep_run = sep.add_run("— · —")
        sep_run.font.size = Pt(8)
        sep_run.font.color.rgb = RGBColor(0xAA, 0xAA, 0xAA)
        sep.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.save(str(out_path))


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------

@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--job-id", required=True, help="Job ID (or prefix) from scored_jobs.json")
@click.option("--landing", "landings_raw", multiple=True, required=True,
              help="Landing spec 'Title:URL:Description'. Repeat for multiple landings.")
@click.option("--attachment", "attachments_raw", multiple=True,
              help="Attached PDF spec 'Title:Description' (a file, not a URL). Repeat for multiple. e.g. the FULL deck PDF.")
@click.option("--mode", type=click.Choice(["speculative", "applied"]),
              default="speculative", show_default=True,
              help="speculative = no active posting (or pulled); applied = active posting")
@click.option("--out", "out_path", type=click.Path(), default=None,
              help="Output .docx path. Default: output/<Company>_Outreach_Pack.docx")
@click.option("--dry-run", is_flag=True, help="Validate inputs but don't call Claude or write the doc")
def main(job_id: str, landings_raw: tuple, attachments_raw: tuple, mode: str,
         out_path: str | None, dry_run: bool) -> None:
    landings = [Landing.parse(l) for l in landings_raw]
    attachments = [Attachment.parse(a) for a in attachments_raw]

    # Load contacts
    contacts_path = settings.data_dir / "contacts" / f"{job_id}.emails.json"
    if not contacts_path.exists():
        raise click.ClickException(
            f"No contacts file at {contacts_path}. Run a contact injector first."
        )
    contacts = json.loads(contacts_path.read_text(encoding="utf-8"))

    # Load job
    scored = json.loads((settings.data_dir / "scored_jobs.json").read_text(encoding="utf-8"))
    job = next((r for r in scored if r["id"].startswith(job_id)), None)
    if not job:
        raise click.ClickException(f"Job {job_id} not found in scored_jobs.json")

    company = job["company"]
    if out_path is None:
        slug = re.sub(r"[^A-Za-z0-9]+", "_", company)
        # Standing rule: outreach packs live in the position's 03_Outreach/.
        from career_ops.discovery.normalize import Job
        from career_ops.generators._paths import job_subdir
        job_obj = Job(
            id=job.get("id", ""),
            title=job.get("title", ""),
            company=company,
            location=job.get("location", ""),
            url=job.get("url", ""),
            source=job.get("source", "indeed"),
            description="",
        )
        out_path = str(job_subdir(job_obj, "outreach") / f"{slug}_Outreach_Pack.docx")
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    click.echo(f"[setup] company={company}  mode={mode}  contacts={len(contacts)}")
    for l in landings:
        click.echo(f"[setup] landing: {l.title} -> {l.url}  ({l.desc})")
    for a in attachments:
        click.echo(f"[setup] attachment: {a.title}  ({a.desc})")
    click.echo(f"[setup] out: {out}")

    if dry_run:
        click.echo("[dry-run] inputs OK. Not calling Claude.")
        return

    system_prompt = _build_system_prompt(company, landings, mode, attachments)

    records = []
    for i, c in enumerate(contacts, start=1):
        click.echo(f"  [{i}/{len(contacts)}] {c['name']} (tier {c.get('tier','?')}) ...")
        try:
            o = generate_for_contact(c, job, company, landings, system_prompt, attachments)
            records.append({"contact": c, "outreach": o})
            click.echo(f"     subject: {o['email_subject']}")
        except Exception as exc:  # noqa: BLE001
            click.echo(f"     FAILED: {exc}")
            continue

    # Persist backup JSON
    outreach_dir = settings.data_dir / "outreach"
    outreach_dir.mkdir(parents=True, exist_ok=True)
    backup = outreach_dir / f"{job_id}_pack.json"
    backup.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    click.echo(f"\n[saved] {backup}")

    build_docx(records, company, landings, mode, out, attachments)
    click.echo(f"[saved] {out}")
    click.echo("Done.")


if __name__ == "__main__":
    main()
