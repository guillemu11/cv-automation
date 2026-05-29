"""Unified LLM wrapper — routes calls between Anthropic, Gemini and chatqueue.

All generator/scorer modules should call ``generate_text`` or
``generate_structured`` here instead of importing ``anthropic`` directly.
That way switching providers is a single env var (``LLM_PROVIDER``).

Two model tiers per provider:
  - "sonnet" — main generation (Claude Sonnet 4 / Gemini 2.5 Flash)
  - "haiku"  — short/cheap calls (Claude Haiku 4.5 / Gemini 2.5 Flash-Lite)

The ``chatqueue`` provider doesn't hit any API — it parks the request on
disk under ``data/chat_queue/inbox/`` and blocks until a human in chat
drops a JSON/markdown reply in ``data/chat_queue/outbox/``. See
``_queue_request`` / ``_wait_for_response`` below.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import logging
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import settings

logger = logging.getLogger(__name__)


_ANTHROPIC_MODELS = {
    "sonnet": "claude-sonnet-4-20250514",
    "haiku": "claude-haiku-4-5-20251001",
}

_GEMINI_MODELS = {
    "sonnet": "gemini-2.5-flash",
    "haiku": "gemini-2.5-flash-lite",
}


# -------------------------------------------------------------------
# JSON-Schema (Anthropic tool input_schema) → Gemini OpenAPI schema
# -------------------------------------------------------------------

_TYPE_MAP = {
    "string": "STRING",
    "integer": "INTEGER",
    "number": "NUMBER",
    "boolean": "BOOLEAN",
    "array": "ARRAY",
    "object": "OBJECT",
}


def _to_gemini_schema(schema: dict) -> dict:
    """Convert a JSON-Schema (as used in Anthropic tool input_schema) to the
    OpenAPI dict the google-genai SDK expects (uppercase types, recursive)."""
    if not isinstance(schema, dict):
        return schema

    out: dict[str, Any] = {}
    for k, v in schema.items():
        if k == "type" and isinstance(v, str):
            out[k] = _TYPE_MAP.get(v.lower(), v.upper())
        elif k == "properties" and isinstance(v, dict):
            out[k] = {pk: _to_gemini_schema(pv) for pk, pv in v.items()}
        elif k == "items":
            out[k] = _to_gemini_schema(v) if isinstance(v, dict) else v
        elif k == "enum":
            out[k] = v
        else:
            out[k] = v
    return out


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# In-memory override stack — lets an orchestrator (e.g. agent_ops) feed
# pre-computed answers to generate_text/generate_structured without
# touching API / Gemini / chatqueue. Keyed by tool_name (structured) or
# the literal "_text" key (text). Designed so a chat-driven flow can
# do `with llm.override({"submit_cv_content": {...}}): generate_cv(job)`
# and pretend the model just returned that payload.
# -------------------------------------------------------------------

import contextlib

_OVERRIDE_STACK: list[dict] = []


@contextlib.contextmanager
def override(answers: dict):
    """Push an answer-dict onto the override stack.

    ``answers`` keys:
      - ``"<tool_name>"`` → dict, returned by ``generate_structured`` when
        a caller passes ``tool_schema["name"] == "<tool_name>"``.
      - ``"_text"`` → str, returned by ``generate_text`` (single text slot;
        if you need multiple, push multiple contexts).

    Innermost override wins; values not found delegate to the next outer
    override and finally to the configured provider. Returns the
    consumed key on exit so callers can assert coverage.
    """
    _OVERRIDE_STACK.append(dict(answers))
    try:
        yield _OVERRIDE_STACK[-1]
    finally:
        _OVERRIDE_STACK.pop()


def _lookup_override(key: str):
    """Walk the stack inside-out. Returns ``(found, value)``."""
    for layer in reversed(_OVERRIDE_STACK):
        if key in layer:
            return True, layer[key]
    return False, None


def is_available() -> tuple[bool, str]:
    """Return (available, reason). Use in callers that previously checked
    ``settings.anthropic_api_key`` directly."""
    if _OVERRIDE_STACK:
        return True, "override"
    provider = settings.llm_provider
    if provider == "gemini":
        if not settings.gemini_api_key:
            return False, "GEMINI_API_KEY missing"
        return True, "gemini"
    if provider == "anthropic":
        if not settings.anthropic_api_key:
            return False, "ANTHROPIC_API_KEY missing"
        return True, "anthropic"
    if provider == "chatqueue":
        # Always "available" — the queue itself doesn't require credentials.
        # The block happens in generate_*; timeout returns the same graceful
        # fallback callers already handle for missing keys.
        return True, "chatqueue"
    return False, f"unknown LLM_PROVIDER '{provider}'"


# -------------------------------------------------------------------
# chatqueue provider — park request on disk, wait for human reply
# -------------------------------------------------------------------

def _chatqueue_paths() -> tuple[Path, Path, Path]:
    base = settings.chatqueue_dir
    inbox = base / "inbox"
    outbox = base / "outbox"
    done = base / "done"
    for p in (inbox, outbox, done):
        p.mkdir(parents=True, exist_ok=True)
    return inbox, outbox, done


def _caller_module() -> str:
    """Walk up the stack and return the first frame outside this module —
    used to label requests so the chat sees which generator asked."""
    here = __name__
    for frame in inspect.stack()[1:]:
        mod = frame.frame.f_globals.get("__name__", "")
        if mod and mod != here and not mod.startswith("career_ops.llm"):
            return mod
    return "unknown"


def _request_id(*, caller: str, tool_name: str, user: str) -> str:
    """Deterministic short id. Same payload → same id → reuses any
    already-answered slot (so a double click doesn't queue twice)."""
    payload = f"{caller}|{tool_name}|{user}".encode("utf-8")
    return hashlib.sha1(payload).hexdigest()[:12]


def _format_request_markdown(req: dict) -> str:
    """Human-readable form so the chat can read it without parsing JSON."""
    lines = [
        f"# chatqueue request `{req['id']}`",
        "",
        f"- **caller**: `{req['caller']}`",
        f"- **kind**: `{req['kind']}`",
        f"- **tier**: `{req.get('tier', 'sonnet')}`",
        f"- **created_at**: {req['created_at']}",
    ]
    if req.get("tool_name"):
        lines.append(f"- **tool**: `{req['tool_name']}`")
    lines.append("")
    lines.append("## system")
    lines.append("")
    lines.append("```")
    lines.append(req["system"])
    lines.append("```")
    lines.append("")
    lines.append("## user")
    lines.append("")
    lines.append("```")
    lines.append(req["user"])
    lines.append("```")
    if req.get("tool_schema"):
        lines.append("")
        lines.append("## expected output (JSON-Schema)")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(req["tool_schema"], indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")
        lines.append("**Reply**: write a single fenced ```json``` block in "
                     f"`outbox/{req['id']}.md` whose object matches `input_schema`.")
    else:
        lines.append("")
        lines.append(f"**Reply**: write plain text in `outbox/{req['id']}.md`.")
    return "\n".join(lines) + "\n"


def _queue_request(req: dict) -> tuple[Path, Path]:
    """Drop the request on disk. Returns (json_path, markdown_path)."""
    inbox, _outbox, _done = _chatqueue_paths()
    j = inbox / f"{req['id']}.json"
    m = inbox / f"{req['id']}.md"
    if not j.exists():
        j.write_text(json.dumps(req, indent=2, ensure_ascii=False), encoding="utf-8")
        m.write_text(_format_request_markdown(req), encoding="utf-8")
        logger.info(
            "chatqueue: parked request id=%s caller=%s kind=%s tool=%s",
            req["id"], req["caller"], req["kind"], req.get("tool_name", "-"),
        )
    else:
        logger.info("chatqueue: request id=%s already queued — reusing slot", req["id"])
    return j, m


def _wait_for_response(req_id: str) -> dict | None:
    """Poll outbox/{id}.{md,json} until present or timeout. Returns the
    parsed payload as a dict (with ``text`` for text-kind, ``data`` for
    structured), or ``None`` on timeout."""
    inbox, outbox, done = _chatqueue_paths()
    md = outbox / f"{req_id}.md"
    js = outbox / f"{req_id}.json"

    deadline = time.monotonic() + settings.chatqueue_timeout_seconds
    poll = max(0.5, settings.chatqueue_poll_seconds)

    while time.monotonic() < deadline:
        if js.exists():
            payload = json.loads(js.read_text(encoding="utf-8"))
        elif md.exists():
            payload = _parse_md_reply(md.read_text(encoding="utf-8"))
        else:
            time.sleep(poll)
            continue

        # Archive consumed request + reply so the inbox stays clean.
        for src in (inbox / f"{req_id}.json", inbox / f"{req_id}.md", md, js):
            if src.exists():
                try:
                    shutil.move(str(src), str(done / src.name))
                except Exception:
                    # If move fails (file lock on Windows), best-effort delete.
                    try:
                        src.unlink()
                    except Exception:
                        pass
        return payload

    logger.warning("chatqueue: request id=%s timed out after %ds", req_id, settings.chatqueue_timeout_seconds)
    return None


def _parse_md_reply(text: str) -> dict:
    """Extract either a fenced ```json``` block (structured) or the raw
    markdown body (text) into a normalized payload dict."""
    # Find first ```json ... ``` block
    fence = "```json"
    i = text.find(fence)
    if i != -1:
        rest = text[i + len(fence):]
        j = rest.find("```")
        if j != -1:
            blob = rest[:j].strip()
            try:
                return {"data": json.loads(blob)}
            except json.JSONDecodeError as exc:
                logger.warning("chatqueue: reply has json fence but invalid JSON (%s)", exc)
                return {"data": {}, "raw": blob}
    # Fall back to plain-text reply
    return {"text": text.strip()}


def _chatqueue_text(*, system: str, user: str, tier: str) -> str:
    req = {
        "id": _request_id(caller=_caller_module(), tool_name="", user=user),
        "kind": "text",
        "tier": tier,
        "system": system,
        "user": user,
        "tool_schema": None,
        "tool_name": None,
        "caller": _caller_module(),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _queue_request(req)
    payload = _wait_for_response(req["id"])
    if payload is None:
        return ""
    return (payload.get("text") or "").strip()


def _chatqueue_structured(*, system: str, user: str, tool_schema: dict, tier: str) -> dict:
    tool_name = tool_schema.get("name", "submit")
    req = {
        "id": _request_id(caller=_caller_module(), tool_name=tool_name, user=user),
        "kind": "structured",
        "tier": tier,
        "system": system,
        "user": user,
        "tool_schema": tool_schema,
        "tool_name": tool_name,
        "caller": _caller_module(),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _queue_request(req)
    payload = _wait_for_response(req["id"])
    if payload is None:
        return {}
    data = payload.get("data")
    if not isinstance(data, dict):
        return {}
    # Soft-validate `required` so a malformed chat reply doesn't crash callers.
    required = tool_schema.get("input_schema", {}).get("required", [])
    missing = [k for k in required if k not in data]
    if missing:
        logger.warning("chatqueue: reply for %s missing required fields: %s", tool_name, missing)
    return data


def generate_text(
    *,
    system: str,
    user: str,
    tier: str = "sonnet",
    max_tokens: int = 1024,
    temperature: float = 0.3,
    timeout: float | None = None,
) -> str:
    """Plain-text generation. Returns the model's text reply (stripped)."""
    found, val = _lookup_override("_text")
    if found:
        logger.info("llm.override: served text from in-memory stack")
        return (val or "").strip() if isinstance(val, str) else ""

    provider = settings.llm_provider

    if provider == "chatqueue":
        return _chatqueue_text(system=system, user=user, tier=tier)

    if provider == "gemini":
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=settings.gemini_api_key)
        model = _GEMINI_MODELS.get(tier, _GEMINI_MODELS["sonnet"])
        response = client.models.generate_content(
            model=model,
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=temperature,
                max_output_tokens=max_tokens,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
            ),
        )
        return (response.text or "").strip()

    # Default / anthropic
    import anthropic

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    model = _ANTHROPIC_MODELS.get(tier, _ANTHROPIC_MODELS["sonnet"])
    kwargs: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
        "temperature": temperature,
    }
    if timeout is not None:
        kwargs["timeout"] = timeout
    response = client.messages.create(**kwargs)
    for block in response.content:
        if getattr(block, "type", None) == "text":
            return (block.text or "").strip()
    return ""


def generate_structured(
    *,
    system: str,
    user: str,
    tool_schema: dict,
    tier: str = "sonnet",
    max_tokens: int = 2048,
    temperature: float = 0.2,
    timeout: float | None = None,
) -> dict:
    """Structured-output generation.

    ``tool_schema`` is in Anthropic tool format::

        {"name": "...", "description": "...", "input_schema": {...JSON-Schema...}}

    Returns the dict matching ``input_schema``. Empty dict on failure.
    """
    tool_name = tool_schema.get("name", "")
    found, val = _lookup_override(tool_name)
    if found:
        logger.info("llm.override: served structured(%s) from in-memory stack", tool_name)
        return dict(val) if isinstance(val, dict) else {}

    provider = settings.llm_provider
    input_schema = tool_schema.get("input_schema", {})

    if provider == "chatqueue":
        return _chatqueue_structured(
            system=system, user=user, tool_schema=tool_schema, tier=tier
        )

    if provider == "gemini":
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=settings.gemini_api_key)
        model = _GEMINI_MODELS.get(tier, _GEMINI_MODELS["sonnet"])

        gemini_schema = _to_gemini_schema(input_schema)
        # Gemini fails on JSON-Schema fields it doesn't recognise; strip them.
        # (additionalProperties, $schema, etc. are not in the OpenAPI subset.)
        for k in ("additionalProperties", "$schema"):
            gemini_schema.pop(k, None)

        # Append schema reminder so even if the SDK ignores response_schema
        # we still get JSON.
        full_user = (
            f"{user}\n\n"
            "Reply with a JSON object matching the requested schema. "
            "Do not include any text before or after the JSON."
        )

        try:
            response = client.models.generate_content(
                model=model,
                contents=full_user,
                config=types.GenerateContentConfig(
                    system_instruction=system,
                    response_mime_type="application/json",
                    response_schema=gemini_schema,
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                ),
            )
        except Exception as exc:
            logger.warning("Gemini structured call failed (%s) — retrying without schema", exc)
            response = client.models.generate_content(
                model=model,
                contents=full_user,
                config=types.GenerateContentConfig(
                    system_instruction=system,
                    response_mime_type="application/json",
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                ),
            )

        text = (response.text or "").strip()
        if not text:
            logger.warning("Gemini returned empty structured response")
            return {}
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Sometimes the model wraps JSON in ```json ... ```
            stripped = text.strip().lstrip("`").lstrip("json").strip("`").strip()
            try:
                return json.loads(stripped)
            except json.JSONDecodeError:
                logger.warning("Gemini returned non-JSON structured response: %s", text[:200])
                return {}

    # Default / anthropic
    import anthropic

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    model = _ANTHROPIC_MODELS.get(tier, _ANTHROPIC_MODELS["sonnet"])
    kwargs: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "tools": [tool_schema],
        "messages": [{"role": "user", "content": user}],
    }
    if timeout is not None:
        kwargs["timeout"] = timeout
    response = client.messages.create(**kwargs)

    tool_name = tool_schema.get("name")
    for block in response.content:
        if getattr(block, "type", None) == "tool_use" and block.name == tool_name:
            return dict(block.input)

    logger.warning("Anthropic did not return tool_use for %s", tool_name)
    return {}
