"""One-off: generate Paula's cover letter for Canon Middle East "CME - PR &
Social Media Specialist - Dubai" (Job Id 876).

Reuses the job defined in _gen_canon_pr_social_specialist.py. Paragraphs are
authored directly (no LLM API key in this repo) and kept strictly truthful. The
letter leans on the genuine fit (social media strategy owned end-to-end + brand /
organizational communications + stakeholder content approvals + AI-enabled
content) and addresses the honest gaps — traditional press-desk PR and the
imaging / tech-hardware sector — with confidence rather than hiding them.

Fills the real cover-letter template, converts to PDF via soffice, and lands the
package under output/2026-08-16/ alongside the CV.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_canon_cv", ROOT / "scripts" / "_gen_canon_pr_social_specialist.py"
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.generators import cover_letter as cl

CONTACT = None  # no named contact yet → "Hiring Manager"

PARAGRAPHS = {
    "opening_paragraph": (
        "Canon has spent 85+ years helping people capture and share their world — which makes it, at "
        "heart, a storytelling company, and storytelling is the craft behind great PR and social. The CME "
        "PR & Social Media Specialist role caught my attention because it pairs the two disciplines I work "
        "in every day: publishing brand communications that reach the public, press and partners, and "
        "owning a social media strategy end-to-end, from content calendar to KPI. Building campaigns inside "
        "a culture of Kyosei — 'living and working together for the common good' — is exactly the kind of "
        "team I want to contribute to."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze I create and execute the social media strategy across "
        "Instagram, TikTok, Facebook and Pinterest — driving campaign development, content planning, "
        "content calendars and performance tracking against KPIs — while briefing creative and media "
        "agencies and safeguarding governance and consistency across every channel. I also develop and "
        "publish organizational and brand communications for the public, customers, trade partners and "
        "media across 50+ markets, and I run the local approval process for launch content and editorial "
        "materials with stakeholders across product categories, ensuring accuracy and timely delivery. "
        "Building the influencer and creator programme from zero to 25–50 creators per campaign taught me "
        "how to turn earned social reach and UGC into measurable brand awareness."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, I have already built a generative-AI content system (Claude / GPT) "
        "that scales content creation, campaign planning and KPI reporting — precisely how a lean "
        "communications team produces more, faster, without losing the brand voice. Second, I am already in "
        "Dubai on a UAE residence visa, bilingual Spanish/English (C1) and comfortable in the hybrid, "
        "cross-functional cadence this role runs on. I'll be candid that my PR experience is brand and "
        "organizational communications rather than a traditional press desk, and my background is FMCG, "
        "beauty and e-commerce rather than imaging — what I bring is genuine end-to-end social-media "
        "ownership, strong campaign and stakeholder-management discipline, and a fast learning curve."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of social-media ownership, brand communications and "
        "AI-enabled content to Canon's Middle East team. I am available to start immediately and would "
        "welcome the chance to discuss how I would approach the content calendar, agency briefs and PR "
        "campaign measurement. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def main() -> None:
    job = cvmod.make_job()
    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    cl_pdf = cvmod._to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    # Relocate into the dated package (same helper as the CV script)
    pos_dir = cl_pdf.parent.parent
    final_dir = cvmod._relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
