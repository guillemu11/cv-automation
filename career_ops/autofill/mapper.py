"""Ask Claude to map extracted form fields to pre-computed answers.

Claude receives:
  - the list of form fields (selector, label, type, options)
  - the FormResponses JSON (Paula's pre-computed answers)
and returns, via tool_use, a list of FieldAction objects telling the filler
what to do for each field. Fields with no good answer are marked "skip".
"""
from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from typing import Literal

from .. import llm
from ..config import settings
from .extractor import FormField

logger = logging.getLogger(__name__)


@dataclass
class FieldAction:
    selector: str
    action: Literal["fill", "select", "check_radio", "check", "uncheck", "upload", "skip"]
    value: str = ""           # text to type, option to select, radio value, or file path
    reason: str = ""          # why this mapping (or why skipped)


_SYSTEM = """\
You map ATS application form fields to pre-computed answers for Paula De \
Francisco. You will receive a list of form fields scraped from a live page \
and a JSON of Paula's prepared answers. Return one action per field.

Rules:
1. For text/textarea/email/tel: action="fill", value=the answer text. Pick \
   the closest narrative answer (why_interested, why_good_fit, \
   greatest_achievement, salary_expectation, availability, notice_period, \
   etc.) or a static profile field (full_name, email, phone, linkedin_url, \
   location, nationality).
2. For select: action="select", value must EXACTLY match one of the field's \
   options (case-sensitive). If no option fits, action="skip".
3. For radio: action="check_radio", value=the option label that matches \
   Paula's answer. Must exactly match an option string.
4. For checkbox: action="check" (true/required things like terms, \
   newsletter-opt-out=keep unchecked) or "uncheck". For ambiguous ones, \
   action="skip" so the human decides.
5. For file: action="skip" — the runner attaches CV/cover automatically \
   based on label keywords (resume, cv, cover letter), don't try to map.
6. If no answer fits or the question is genuinely custom (e.g. \
   "favorite brand and why"), check additional_qa for a matching question; \
   otherwise action="skip" with a short reason.
7. Be conservative: skipping is better than filling wrong data. The human \
   will review the browser before submitting.
8. Always return one action per input field, in the same order.
"""

_TOOL = {
    "name": "submit_field_actions",
    "description": "Return one action per form field describing how to fill it.",
    "input_schema": {
        "type": "object",
        "properties": {
            "actions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "selector": {"type": "string"},
                        "action": {
                            "type": "string",
                            "enum": ["fill", "select", "check_radio", "check", "uncheck", "skip"],
                        },
                        "value": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["selector", "action"],
                },
            }
        },
        "required": ["actions"],
    },
}


def map_fields(fields: list[FormField], responses: dict) -> list[FieldAction]:
    """LLM tool-use call: form fields + answers JSON → list of actions."""
    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot map form fields", reason)
        return [FieldAction(selector=f.selector, action="skip", reason="no LLM") for f in fields]

    if not fields:
        return []

    fields_payload = [asdict(f) for f in fields]
    answers = responses.get("responses", responses)

    user_msg = f"""\
## Pre-computed answers (Paula's profile + per-job narrative answers)

```json
{_truncate_json(answers, 6000)}
```

## Form fields extracted from the live application page

```json
{_truncate_json(fields_payload, 8000)}
```

Return one action per field via the submit_field_actions tool, preserving order."""

    data = llm.generate_structured(
        system=_SYSTEM,
        user=user_msg,
        tool_schema=_TOOL,
        tier="sonnet",
        max_tokens=4096,
        timeout=60.0,
    )

    actions_raw = data.get("actions", []) if data else []
    if not actions_raw:
        logger.warning("LLM did not return actions for field mapping")
        return [FieldAction(selector=f.selector, action="skip", reason="no mapping returned") for f in fields]

    return [
        FieldAction(
            selector=a.get("selector", ""),
            action=a.get("action", "skip"),
            value=a.get("value", ""),
            reason=a.get("reason", ""),
        )
        for a in actions_raw
    ]


def _truncate_json(obj, max_chars: int) -> str:
    import json
    s = json.dumps(obj, ensure_ascii=False, indent=2)
    if len(s) > max_chars:
        s = s[:max_chars] + "\n... [truncated]"
    return s
