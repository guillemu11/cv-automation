"""Discovery sources — each module exposes ``fetch(queries, locations, limit) -> list[Job]``.

``discover_all`` is the dispatcher called by the pipeline. It runs each source
independently, isolates failures (one broken source does not kill the run), and
deduplicates inside each source's output before returning the combined list.
"""
from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable

from .normalize import Job

logger = logging.getLogger(__name__)


def discover_all(
    queries: list[str],
    locations: list[str],
    limit: int = 30,
    hours_old: int = 48,
    sources: list[str] | None = None,
) -> list[Job]:
    """Run all enabled sources in parallel. Returns a deduplicated list of Jobs.

    Failures in individual sources are logged and skipped — they do not raise.
    """
    from ..config import settings
    from . import firecrawl_careers, jobspy_source, serpapi_source

    registry: dict[str, Callable[..., list[Job]]] = {
        "jobspy": jobspy_source.fetch,
        "serpapi": serpapi_source.fetch,
        "firecrawl": firecrawl_careers.fetch,
        # apify_linkedin plugs in later as a LinkedIn fallback
    }
    # Default to the configured sources (Indeed-only via jobspy) unless an explicit
    # subset is requested. Keeps paid sources (serpapi/firecrawl) off unless turned on.
    enabled = sources if sources is not None else settings.discovery_sources
    available = {k: v for k, v in registry.items() if k in enabled}
    if not available:
        logger.warning("no discovery sources enabled (requested=%s) — nothing to discover", enabled)
        return []

    all_jobs: list[Job] = []
    with ThreadPoolExecutor(max_workers=len(available)) as ex:
        futs = {
            ex.submit(fn, queries=queries, locations=locations, limit=limit, hours_old=hours_old): name
            for name, fn in available.items()
        }
        for fut in as_completed(futs):
            name = futs[fut]
            try:
                jobs = fut.result()
                logger.info("source=%s ok jobs=%d", name, len(jobs))
                all_jobs.extend(jobs)
            except Exception as exc:  # noqa: BLE001 — we want to swallow per-source
                logger.exception("source=%s failed: %s", name, exc)

    # intra-run dedupe (across sources); cross-run dedupe is filters/dedupe.py
    seen: set[str] = set()
    out: list[Job] = []
    for j in all_jobs:
        if j.id in seen:
            continue
        seen.add(j.id)
        out.append(j)
    return out
