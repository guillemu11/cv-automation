"""Central config loader: .env + profile.yaml + blacklist.yaml.

Every module should import ``settings`` from here instead of reading env vars
directly. Keeps secrets and tunables in one place and makes testing easier.
"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent

load_dotenv(ROOT / ".env", override=True)


def _env(key: str, default: str | None = None, required: bool = False) -> str | None:
    val = os.getenv(key, default)
    if required and not val:
        raise RuntimeError(f"Missing required env var: {key}")
    return val


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Expected config file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class Settings:
    # --- paths ---
    root: Path = ROOT
    data_dir: Path = ROOT / "data"
    logs_dir: Path = ROOT / "logs"
    templates_dir: Path = ROOT / "templates"
    output_dir: Path = ROOT / "output"

    seen_jobs_path: Path = data_dir / "seen_jobs.json"
    analysis_cache_path: Path = data_dir / "analysis_cache.sqlite"
    golden_set_path: Path = data_dir / "golden_set.yaml"
    form_response_history_path: Path = data_dir / "form_response_history.json"
    chatqueue_dir: Path = data_dir / "chat_queue"

    # --- profile & blacklist ---
    profile: dict[str, Any]
    blacklist: dict[str, Any]

    # --- API keys ---
    anthropic_api_key: str | None
    gemini_api_key: str | None
    google_image_api_key: str | None  # Gemini image API ("Nano Banana"); needs billing
    image_model: str  # default gemini-3-pro-image
    llm_provider: str  # "anthropic" | "gemini" | "chatqueue"
    chatqueue_timeout_seconds: int
    chatqueue_poll_seconds: float
    notion_token: str | None
    notion_db_jobs: str | None
    notion_db_contacts: str | None
    notion_parent_page_id: str | None
    serpapi_key: str | None
    apify_token: str | None
    firecrawl_api_key: str | None
    apollo_api_key: str | None
    hunter_api_key: str | None

    # --- email ---
    ms_graph_client_id: str | None
    ms_graph_client_secret: str | None
    ms_graph_tenant_id: str | None
    ms_graph_refresh_token: str | None
    ms_graph_user_email: str | None
    gmail_token_json: str | None

    # --- pipeline tunables ---
    timezone: str
    digest_to: str | None
    max_results_per_query: int
    hours_old: int
    dry_run: bool
    notion_enabled: bool

    # --- discovery ---
    # Which discovery sources run in discover_all(). Indeed-only by default:
    # SerpAPI is out of credits and firecrawl/apify are not used. jobspy is the
    # engine that scrapes Indeed natively (no paid API), so it is the sole source.
    discovery_sources: list[str]
    # Which sites jobspy scrapes. Indeed-only by default (linkedin disabled).
    jobspy_sites: list[str]

    def __init__(self) -> None:
        # ensure dirs exist at import time so downstream code can just write
        for p in (self.data_dir, self.logs_dir, self.output_dir):
            p.mkdir(parents=True, exist_ok=True)

        self.profile = _load_yaml(ROOT / "profile.yaml")
        self.blacklist = _load_yaml(ROOT / "blacklist.yaml")

        self.anthropic_api_key = _env("ANTHROPIC_API_KEY")
        self.gemini_api_key = _env("GEMINI_API_KEY")
        # Image generation (Google Gemini image API, aka "Nano Banana"). Replaces
        # the old Higgsfield flow. Falls back to the text Gemini key if a dedicated
        # image key isn't set. NOTE: image models require a billing-enabled project
        # (free-tier quota is 0), unlike text scoring which works on the free tier.
        self.google_image_api_key = _env("GOOGLE_IMAGE_API_KEY") or self.gemini_api_key
        self.image_model = _env("IMAGE_MODEL", "gemini-3-pro-image") or "gemini-3-pro-image"
        self.llm_provider = (_env("LLM_PROVIDER", "anthropic") or "anthropic").lower()
        self.chatqueue_timeout_seconds = int(_env("CHATQUEUE_TIMEOUT_SECONDS", "1800") or 1800)
        self.chatqueue_poll_seconds = float(_env("CHATQUEUE_POLL_SECONDS", "2.0") or 2.0)
        self.notion_token = _env("NOTION_TOKEN")
        self.notion_db_jobs = _env("NOTION_DB_JOBS")
        self.notion_db_contacts = _env("NOTION_DB_CONTACTS")
        self.notion_parent_page_id = _env("NOTION_PARENT_PAGE_ID")
        self.serpapi_key = _env("SERPAPI_KEY")
        self.apify_token = _env("APIFY_TOKEN")
        self.firecrawl_api_key = _env("FIRECRAWL_API_KEY")
        self.apollo_api_key = _env("APOLLO_API_KEY")
        self.hunter_api_key = _env("HUNTER_API_KEY")

        self.ms_graph_client_id = _env("MS_GRAPH_CLIENT_ID")
        self.ms_graph_client_secret = _env("MS_GRAPH_CLIENT_SECRET")
        self.ms_graph_tenant_id = _env("MS_GRAPH_TENANT_ID", "common")
        self.ms_graph_refresh_token = _env("MS_GRAPH_REFRESH_TOKEN")
        self.ms_graph_user_email = _env("MS_GRAPH_USER_EMAIL")
        self.gmail_token_json = _env("GMAIL_TOKEN_JSON")

        self.timezone = _env("PIPELINE_TIMEZONE", "Asia/Dubai") or "Asia/Dubai"
        self.digest_to = _env("PIPELINE_DIGEST_TO") or self.profile["personal"]["email"]
        self.max_results_per_query = int(_env("PIPELINE_MAX_RESULTS_PER_QUERY", "30") or 30)
        self.hours_old = int(_env("PIPELINE_HOURS_OLD", "48") or 48)
        self.dry_run = (_env("PIPELINE_DRY_RUN", "false") or "false").lower() == "true"
        # Notion is now read-only from the import script. The pipeline no longer
        # writes to Notion by default — the dashboard (scored_jobs.json) is the source of truth.
        self.notion_enabled = (_env("NOTION_ENABLED", "false") or "false").lower() == "true"

        # Indeed-only discovery. jobspy is the engine that scrapes Indeed for free
        # (no paid API). SerpAPI is out of credits; firecrawl/apify are off. Override
        # via DISCOVERY_SOURCES (comma-separated) only if a paid source comes back.
        self.discovery_sources = [
            s.strip().lower() for s in (_env("DISCOVERY_SOURCES", "jobspy") or "jobspy").split(",") if s.strip()
        ]
        # Which sites jobspy scrapes. Indeed-only by default — LinkedIn is disabled
        # because it blocks scrapers aggressively and Paula's search is Indeed-only.
        self.jobspy_sites = [
            s.strip().lower() for s in (_env("JOBSPY_SITES", "indeed") or "indeed").split(",") if s.strip()
        ]

    # --- helpers ---
    @property
    def target_titles(self) -> list[str]:
        return self.profile["target_titles"]

    @property
    def target_locations(self) -> list[str]:
        return self.profile["target_locations"]

    @property
    def min_salary_aed(self) -> int:
        return int(self.blacklist.get("min_salary_aed_month", 0))

    @property
    def allowed_locations(self) -> list[str]:
        return self.blacklist.get("allowed_locations", [])

    @property
    def keywords_reject(self) -> list[str]:
        return [k.lower() for k in self.blacklist.get("keywords_reject", [])]

    @property
    def seniority_reject(self) -> list[str]:
        return [s.lower() for s in self.blacklist.get("seniority_reject", [])]

    @property
    def companies_blacklist(self) -> list[str]:
        return [c.lower() for c in self.blacklist.get("companies", [])]

    @property
    def title_reject_patterns(self) -> list[str]:
        return [p.lower() for p in self.blacklist.get("title_reject_patterns", [])]

    @property
    def currency_to_aed(self) -> dict[str, float]:
        return self.blacklist.get("currency_to_aed", {})


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
