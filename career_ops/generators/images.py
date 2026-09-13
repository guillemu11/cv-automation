"""Image generation via Google's Gemini image API ("Nano Banana").

Replaces the previous Higgsfield-based flow. Every image the pipeline needs
(campaign-landing stills, deck visuals, etc.) is produced here through the
Generative Language REST API so we depend on nothing but the stdlib + a key.

Config (all via ``career_ops.config.settings``):
  - ``GOOGLE_IMAGE_API_KEY`` — Gemini API key with **billing enabled**. Image
    models have a free-tier quota of 0, so a pay-as-you-go project is required.
    Falls back to ``GEMINI_API_KEY`` if the dedicated key is absent.
  - ``IMAGE_MODEL`` — default ``gemini-3-pro-image`` (Nano Banana Pro, best
    quality). ``gemini-2.5-flash-image`` is the cheaper/faster alternative.

Honors ``PIPELINE_DRY_RUN`` (no network call, returns None).

Public API:
  - ``generate_image(prompt, out_path, ...)`` — one image.
  - ``generate_batch(specs, out_dir, ...)`` — many, with optional reference
    chaining so a set stays visually consistent.
"""
from __future__ import annotations

import base64
import json
import logging
import mimetypes
import time
import urllib.error
import urllib.request
from pathlib import Path

from ..config import settings

logger = logging.getLogger(__name__)

_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

# Aspect ratios accepted by the Gemini image models.
_ALLOWED_ASPECT = {"1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"}


class ImageGenError(RuntimeError):
    """Image generation failed."""


class ImageQuotaError(ImageGenError):
    """The key's project has no image-generation quota (free tier / no billing)."""


# -------------------------------------------------------------------
# Request helpers
# -------------------------------------------------------------------

def _ref_part(path: Path) -> dict:
    """Load a local image as an inline_data part for image-to-image chaining."""
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return {"inline_data": {"mime_type": mime, "data": data}}


def _extract_image(resp: dict) -> tuple[bytes, str] | None:
    """Pull the first inline image (bytes, mime) out of a generateContent response."""
    for cand in resp.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                mime = inline.get("mimeType") or inline.get("mime_type") or "image/png"
                return base64.b64decode(inline["data"]), mime
    return None


def _post(model: str, body: dict, key: str, timeout: int) -> dict:
    url = f"{_API_BASE}/{model}:generateContent"
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def _is_hard_quota(payload: dict) -> bool:
    """True when the 429 is a free-tier ``limit: 0`` (billing not enabled), which
    no amount of retrying will fix — distinct from a transient per-minute cap."""
    msg = json.dumps(payload)
    return "limit: 0" in msg or "FreeTier" in msg and "PerDay" in msg


def _retry_delay(payload: dict, default: float) -> float:
    for d in payload.get("error", {}).get("details", []):
        if d.get("@type", "").endswith("RetryInfo"):
            raw = str(d.get("retryDelay", "")).rstrip("s")
            try:
                return min(float(raw), 60.0)
            except ValueError:
                pass
    return default


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

def generate_image(
    prompt: str,
    out_path: str | Path,
    *,
    aspect_ratio: str = "4:5",
    model: str | None = None,
    reference_images: list[str | Path] | None = None,
    max_retries: int = 2,
    timeout: int = 180,
) -> Path | None:
    """Generate one image and write it to ``out_path``. Returns the path or None.

    ``reference_images`` are passed as inline image inputs (image-to-image), which
    keeps a series visually consistent — pass the first result into later calls.
    Raises :class:`ImageQuotaError` when the project has no image quota so callers
    can surface a clear "enable billing" message instead of a generic failure.
    """
    key = settings.google_image_api_key
    if not key:
        logger.warning("no GOOGLE_IMAGE_API_KEY / GEMINI_API_KEY set — cannot generate image")
        return None

    if settings.dry_run:
        logger.info("[DRY RUN] would generate image -> %s (%s, %s)", out_path, model or settings.image_model, aspect_ratio)
        return None

    if aspect_ratio not in _ALLOWED_ASPECT:
        raise ImageGenError(f"aspect_ratio {aspect_ratio!r} not in {sorted(_ALLOWED_ASPECT)}")

    model = model or settings.image_model
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    parts: list[dict] = [{"text": prompt}]
    for ref in reference_images or []:
        rp = Path(ref)
        if rp.exists():
            parts.append(_ref_part(rp))
        else:
            logger.warning("reference image not found, skipping: %s", rp)

    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio},
        },
    }

    for attempt in range(max_retries + 1):
        try:
            resp = _post(model, body, key, timeout)
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {"error": {"message": raw[:300]}}
            if e.code == 429:
                if _is_hard_quota(payload):
                    raise ImageQuotaError(
                        f"'{model}' has no image quota on this project — Gemini image models "
                        "are free-tier limit 0. Enable billing (pay-as-you-go) on the Google "
                        "Cloud project behind GOOGLE_IMAGE_API_KEY, then retry."
                    ) from e
                if attempt < max_retries:
                    delay = _retry_delay(payload, 5.0)
                    logger.info("429 transient on %s — retrying in %.0fs (%d/%d)", model, delay, attempt + 1, max_retries)
                    time.sleep(delay)
                    continue
            msg = payload.get("error", {}).get("message", raw[:300])
            raise ImageGenError(f"HTTP {e.code} generating image with {model}: {msg}") from e
        except urllib.error.URLError as e:
            if attempt < max_retries:
                logger.info("network error on %s (%s) — retrying", model, e.reason)
                time.sleep(3)
                continue
            raise ImageGenError(f"network error generating image: {e.reason}") from e

        got = _extract_image(resp)
        if not got:
            texts = [p.get("text", "") for c in resp.get("candidates", []) for p in c.get("content", {}).get("parts", [])]
            raise ImageGenError(f"{model} returned no image (text: {texts[:1]})")
        data, _mime = got
        out_path.write_bytes(data)
        logger.info("image saved: %s (%d bytes, %s)", out_path, len(data), model)
        return out_path

    return None


def generate_batch(
    specs: list[dict],
    out_dir: str | Path,
    *,
    aspect_ratio: str = "4:5",
    model: str | None = None,
    chain_reference: bool = True,
    ext: str = "png",
) -> dict[str, Path]:
    """Generate many images from ``specs`` = [{"name","prompt", ["aspect_ratio"]}, ...].

    When ``chain_reference`` is set, the first successful image is fed as a
    reference into every later call so the set shares lighting/finish.
    Returns {name: path} for the images that succeeded.
    """
    out_dir = Path(out_dir)
    results: dict[str, Path] = {}
    anchor: Path | None = None

    for spec in specs:
        name = spec["name"]
        refs = [anchor] if (chain_reference and anchor) else None
        path = generate_image(
            spec["prompt"],
            out_dir / f"{name}.{ext}",
            aspect_ratio=spec.get("aspect_ratio", aspect_ratio),
            model=model,
            reference_images=refs,
        )
        if path:
            results[name] = path
            if anchor is None:
                anchor = path
    return results


# -------------------------------------------------------------------
# CLI: python -m career_ops.generators.images --spec specs.json --out dir/
# -------------------------------------------------------------------

def _main() -> int:
    import argparse

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser(description="Generate images via the Google Gemini image API.")
    ap.add_argument("--spec", required=True, help="JSON file: [{'name','prompt',['aspect_ratio']}, ...]")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--model", default=None, help="override IMAGE_MODEL")
    ap.add_argument("--aspect", default="4:5")
    ap.add_argument("--no-chain", action="store_true", help="don't chain reference images")
    args = ap.parse_args()

    specs = json.loads(Path(args.spec).read_text())
    try:
        out = generate_batch(
            specs, args.out, aspect_ratio=args.aspect, model=args.model, chain_reference=not args.no_chain
        )
    except ImageQuotaError as e:
        logger.error("QUOTA: %s", e)
        return 2
    logger.info("done: %d/%d images -> %s", len(out), len(specs), args.out)
    return 0 if len(out) == len(specs) else 1


if __name__ == "__main__":
    raise SystemExit(_main())
