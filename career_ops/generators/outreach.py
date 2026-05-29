"""Outreach message generator — email + LinkedIn copy per job.

Generates:
  - Email subject + body (HTML) for recruiting outreach
  - LinkedIn connection note (<=300 chars)
  - LinkedIn InMail (longer version)

Can also create a draft email with CV/CL attachments via the email client.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job
from ..email_client import EmailDraft, create_draft
from . import angles

logger = logging.getLogger(__name__)


@dataclass
class OutreachContent:
    """All outreach copy for a single job application."""
    email_subject: str
    email_body: str  # HTML
    linkedin_connection: str  # <=300 chars
    linkedin_inmail: str


# -------------------------------------------------------------------
# Claude prompt
# -------------------------------------------------------------------

_SYSTEM = """\
You write concise, compelling outreach messages for a job seeker.
The candidate is Paula De Francisco, a Brand/Marketing Manager in Dubai.

Rules:
1. Email subject: Under 60 chars, specific to the role, no clickbait.
2. Email body: 4-6 sentences. Lead with a relevant achievement, mention the
   specific role, end with a clear ask. Professional but human. Use HTML
   formatting (<p> tags, <strong> for emphasis).
3. LinkedIn connection note: MUST be under 300 characters total. One sentence
   about why you're connecting + one about what you bring.
4. LinkedIn InMail: 3-4 sentences, slightly more detailed than the connection note.
5. NEVER use phrases like "I came across your profile" or "I hope this finds you well".
6. Reference a specific metric or achievement from the profile.
7. Output via the submit_outreach tool.
"""

_OUTREACH_TOOL = {
    "name": "submit_outreach",
    "description": "Submit all outreach copy for this job application",
    "input_schema": {
        "type": "object",
        "properties": {
            "email_subject": {
                "type": "string",
                "description": "Email subject line, under 60 characters",
            },
            "email_body": {
                "type": "string",
                "description": "Email body in HTML (use <p> tags)",
            },
            "linkedin_connection": {
                "type": "string",
                "description": "LinkedIn connection note, MUST be under 300 characters",
            },
            "linkedin_inmail": {
                "type": "string",
                "description": "LinkedIn InMail message, 3-4 sentences",
            },
        },
        "required": ["email_subject", "email_body", "linkedin_connection", "linkedin_inmail"],
    },
}


# -------------------------------------------------------------------
# Claude API call
# -------------------------------------------------------------------

def generate_outreach(
    job: Job,
    analysis: JobAnalysis,
    contact_name: str | None = None,
) -> OutreachContent | None:
    """Generate all outreach copy for a specific job+contact."""
    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate outreach", reason)
        return None

    p = settings.profile
    angle = angles.get((job.raw or {}).get("positioning_angle"))
    speculative = bool((job.raw or {}).get("speculative"))

    system_msg = _SYSTEM
    angle_block = ""
    if angle:
        system_msg = _SYSTEM + "\n\n" + angle.system_addendum
        angle_block = "\n\n" + angle.user_addendum
    if speculative:
        system_msg += (
            "\n\nSPECULATIVE OUTREACH: There is no public job posting. Frame the "
            "message as a thoughtful introduction tied to something specific about the "
            "company's current moment (expansion, recent hires, new market) — NOT as a "
            "reply to a vacancy. The ask should be a short conversation, not a "
            "submission to a process."
        )

    user_msg = f"""\
Write outreach messages for this job application.

## Target
- Role: {job.title}
- Company: {job.company}
- Contact: {contact_name or 'Hiring Manager'}
- Location: {job.location}

### Job Description (excerpt)
{(job.description or 'No description')[:3000]}

### Match Analysis
- Score: {analysis.score}/100 ({analysis.tier})
- Skills match: {', '.join(analysis.skills_match)}
- Key differentiators to highlight:
  * +30% GMV QoQ with 42 key accounts (Alibaba/Miravia)
  * UAE quick-commerce: Noon, Talabat, Careem, Deliveroo
  * 6 NPD launches across 50+ countries
  * Already in Dubai with residence visa

## Candidate
{p['personal']['name']} — {p['headline']}{angle_block}

Use the submit_outreach tool to return all messages."""

    data = llm.generate_structured(
        system=system_msg,
        user=user_msg,
        tool_schema=_OUTREACH_TOOL,
        tier="sonnet",
        max_tokens=1024,
    )

    if not data:
        logger.warning("LLM did not return outreach content")
        return None

    # Enforce LinkedIn connection note limit
    linkedin_conn = data.get("linkedin_connection", "")
    if len(linkedin_conn) > 300:
        linkedin_conn = linkedin_conn[:297] + "..."

    return OutreachContent(
        email_subject=data.get("email_subject", ""),
        email_body=data.get("email_body", ""),
        linkedin_connection=linkedin_conn,
        linkedin_inmail=data.get("linkedin_inmail", ""),
    )


def create_outreach_draft(
    job: Job,
    analysis: JobAnalysis,
    contact_email: str,
    contact_name: str | None = None,
    cv_path: Path | None = None,
    cl_path: Path | None = None,
    deliverable_path: Path | None = None,
) -> str:
    """Create an email draft with outreach copy + optional attachments.

    Returns the draft ID, or "" if creation failed.
    """
    content = generate_outreach(job, analysis, contact_name=contact_name)
    if not content:
        return ""

    # If a deliverable is attached, mention it in the email body
    body_html = content.email_body
    if deliverable_path and deliverable_path.exists():
        mention = (
            f"<p>I've also prepared a brief analysis of {job.company}'s market "
            f"positioning that I hope you'll find useful — please see the attached document.</p>"
        )
        body_html = body_html + mention

    attachments = []
    if cv_path and cv_path.exists():
        attachments.append(cv_path)
    if cl_path and cl_path.exists():
        attachments.append(cl_path)
    if deliverable_path and deliverable_path.exists():
        attachments.append(deliverable_path)

    draft = EmailDraft(
        to=contact_email,
        subject=content.email_subject,
        body_html=body_html,
        attachments=attachments,
    )

    draft_id = create_draft(draft)
    if draft_id:
        logger.info("outreach draft created for %s @ %s: %s", job.title[:30], job.company, draft_id)
    return draft_id
