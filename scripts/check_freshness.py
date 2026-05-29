"""Verify which Hot/Warm jobs in scored_jobs.json are still live.

For each Hot+Warm URL: HEAD then GET if needed, mark:
  - active_old : 2xx and body has no expired markers
  - expired    : 4xx/5xx OR body has expired markers
  - unknown    : transport error, timeout, or ambiguous

Writes back into data/scored_jobs.json adding `freshness` and `checked_at`.
Cold jobs left untouched (will be filtered out at dashboard level).
"""
from __future__ import annotations

import asyncio
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
SCORED = ROOT / "data" / "scored_jobs.json"

EXPIRED_MARKERS = [
    "no longer accepting applications",
    "this job is no longer",
    "job is closed",
    "position has been filled",
    "position is no longer available",
    "this job posting is no longer",
    "we're sorry, this job",
    "the job you are looking for",
    "page not found",
    "job not found",
    "currently not available",
    "expired",
]

# host-specific signals (path/query that indicate redirect to a search/listing fallback)
EXPIRED_REDIRECT_PATHS = [
    "/jobs/search",
    "/jobs/collections",
    "/jobs/view/expired",
    "/job-not-found",
]

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
TIMEOUT = httpx.Timeout(15.0, connect=8.0)
SEM = asyncio.Semaphore(10)


async def classify(client: httpx.AsyncClient, url: str) -> tuple[str, str]:
    """Return (freshness, note)."""
    if not url:
        return "unknown", "no_url"
    async with SEM:
        try:
            r = await client.get(url, headers={"User-Agent": USER_AGENT}, follow_redirects=True)
        except (httpx.TimeoutException, httpx.TransportError) as e:
            return "unknown", f"transport_error:{type(e).__name__}"
        except Exception as e:
            return "unknown", f"error:{type(e).__name__}"

    final_url = str(r.url)
    status = r.status_code

    if status in (404, 410):
        return "expired", f"http_{status}"
    if status in (401, 403, 429):
        # bot-blocking / auth-walled — cannot conclude expiration
        return "unknown", f"http_{status}_blocked"
    if status >= 500:
        return "unknown", f"http_{status}"
    if status >= 400:
        return "unknown", f"http_{status}"

    # check redirect signals
    low = final_url.lower()
    for p in EXPIRED_REDIRECT_PATHS:
        if p in low:
            return "expired", f"redirected_to:{p}"

    # body markers (only on text)
    ctype = r.headers.get("content-type", "")
    if "text" in ctype or "html" in ctype:
        body = r.text.lower()
        # strip very long body for matching efficiency
        snippet = body[:200_000]
        for m in EXPIRED_MARKERS:
            if m in snippet:
                return "expired", f"body_marker:{m[:30]}"

    return "active_old", f"http_{status}"


async def main() -> int:
    data = json.loads(SCORED.read_text(encoding="utf-8"))
    targets = [j for j in data if str(j.get("ai_tier", "")).lower() in ("hot", "warm")]
    print(f"Checking {len(targets)} Hot/Warm jobs out of {len(data)} total...")

    now = datetime.now(timezone.utc).isoformat()

    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        results = await asyncio.gather(
            *(classify(client, j.get("url", "")) for j in targets)
        )

    by_status: dict[str, int] = {}
    for j, (status, note) in zip(targets, results):
        j["freshness"] = status
        j["freshness_note"] = note
        j["freshness_checked_at"] = now
        by_status[status] = by_status.get(status, 0) + 1

    # ensure Cold get a freshness too so frontend filter is consistent
    for j in data:
        if str(j.get("ai_tier", "")).lower() == "cold":
            j.setdefault("freshness", "skipped_cold")

    SCORED.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Results:")
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")

    # show expired examples
    expired = [j for j in targets if j.get("freshness") == "expired"]
    print(f"\nExpired sample (up to 10):")
    for j in expired[:10]:
        print(f"  [{j.get('ai_tier'):4}] {j.get('title','')[:50]:50} @ {j.get('company','')[:25]:25} -> {j.get('freshness_note')}")

    unknown = [j for j in targets if j.get("freshness") == "unknown"]
    if unknown:
        print(f"\nUnknown sample (up to 5):")
        for j in unknown[:5]:
            print(f"  [{j.get('ai_tier'):4}] {j.get('title','')[:50]:50} -> {j.get('freshness_note')}")

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
