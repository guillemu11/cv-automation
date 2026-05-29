"""Content generators — CV, cover letter, outreach, deliverables, and form responses."""
from ._paths import job_output_dir
from .cover_letter import generate_cover_letter
from .cv_generator import generate_cv
from .deliverables import generate_all_deliverables, generate_deliverable
from .form_responses import generate_form_responses
from .landing_generator import generate_landing, landing_to_pdf
from .outreach import create_outreach_draft, generate_outreach

__all__ = [
    "generate_cv",
    "generate_cover_letter",
    "generate_outreach",
    "create_outreach_draft",
    "generate_deliverable",
    "generate_all_deliverables",
    "generate_form_responses",
    "generate_landing",
    "landing_to_pdf",
    "job_output_dir",
]
