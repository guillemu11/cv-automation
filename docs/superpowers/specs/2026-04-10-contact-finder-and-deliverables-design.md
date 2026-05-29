# Contact Finder + Value-add Deliverables — Design Spec

## Context

Paula's job-search pipeline is ~95% complete (discovery → filters → scoring → Notion → CV/CL → email drafts). Two features remain to maximize differentiation:

1. **Contact Finder** — identify hiring managers, HR, and peers at target companies so outreach is personalized ("Dear Sarah" not "Dear Hiring Manager")
2. **Value-add Deliverables** — 4 types of mini-audit/proposal that Paula sends alongside her CV to stand out from other candidates

Both features plug into the existing pipeline after Claude scoring.

---

## Feature 1: Contact Finder

### Module: `career_ops/contact_finder.py`

### Data Model

```python
@dataclass
class Contact:
    name: str
    title: str
    company: str
    email: str | None
    linkedin_url: str | None
    role_type: str   # "Hiring Manager" | "HR/Recruiter" | "Peer"
    source: str      # "Apollo"
```

### API: Apollo.io People Search

- **Endpoint:** `POST https://api.apollo.io/api/v1/mixed_people/search`
- **Auth:** API key via `settings.apollo_api_key`
- **Free tier:** 10,000 credits/month (more than enough)
- **Cost per job:** ~6 credits (3 searches × 2 credits each)

### Search Strategy (per job)

For each job that scores ≥ 60, run 3 searches against Apollo:

1. **Hiring Manager** (max 2 results)
   - Filter: company name + location (Dubai/UAE)
   - Titles inferred from job title by Claude:
     - e.g., "Brand Manager" job → search "Head of Marketing", "Marketing Director", "Brand Director", "CMO"
   - Seniority: 1-2 levels above the job's seniority

2. **HR / Recruiter** (max 2 results)
   - Filter: company name + location (Dubai/UAE)
   - Titles: "Talent Acquisition", "HR Manager", "Recruiter", "People Partner"

3. **Peer** (max 1 result)
   - Filter: company name + location (Dubai/UAE)
   - Titles: same or similar to the job title (e.g., "Brand Manager", "Senior Brand Manager")
   - Purpose: internal referral opportunity

### Title Inference

Use Claude (claude-haiku, cheap) to infer search titles from the job title + description:

```
Given this job: "Brand Manager at Chalhoub Group"
Return 3-4 titles for the likely hiring manager (1-2 levels up).
```

This avoids hardcoding title mappings and handles edge cases (some companies use "Head of", others use "Director of", others use "VP").

### Functions

```python
def find_contacts(company: str, job_title: str, job_description: str = "") -> list[Contact]:
    """Find hiring manager, HR, and peer contacts at a company via Apollo."""

def _search_apollo(company: str, titles: list[str], location: str = "United Arab Emirates", max_results: int = 2) -> list[Contact]:
    """Search Apollo People API for contacts matching company + titles."""

def _infer_hiring_manager_titles(job_title: str, job_description: str) -> list[str]:
    """Use Claude to infer likely hiring manager titles from a job posting."""
```

### Notion Sync

Extend `career_ops/notion_sync.py` with:

```python
def sync_contacts(contacts: list[Contact], job_page_id: str) -> None:
    """Create or update contacts in Notion Contacts DB, linked to a job."""
```

- Uses existing `NOTION_DB_CONTACTS` (already created: `33e98509-f844-81e3-a646-d8de80829a2c`)
- Deduplicates by (name + company) — same contact found for multiple jobs gets updated, not duplicated
- Sets relation to the job in Job Pipeline DB

### Integration Points

- **Pipeline** (`pipeline.py`): new stage after scoring, before content generation. Only for jobs with score ≥ 60.
- **Outreach** (`outreach.py`): `generate_outreach()` already accepts `contact_name` — will now receive actual names. Generate separate outreach per contact (email for email contacts, LinkedIn note for LinkedIn-only contacts).
- **generate_for_job.py**: add `--contacts` flag to show/find contacts for a specific job.

### Dry-run behavior

When `PIPELINE_DRY_RUN=true`:
- Apollo searches are skipped
- Returns mock contacts for testing
- No Notion writes

---

## Feature 2: Value-add Deliverables

### Module: `career_ops/generators/deliverables.py`

### 4 Deliverable Types

#### A) Digital Presence Audit (`type: "digital_audit"`)
- **Scrape:** Company website (homepage, about, products) via Firecrawl
- **Analyze:** UX, messaging clarity, brand consistency, mobile experience, SEO basics
- **Output:** 3-5 observations + actionable suggestions
- **Best for:** Marketing Manager, Digital Marketing Manager, Brand Manager

#### B) E-commerce / Quick-commerce Teardown (`type: "ecommerce_teardown"`)
- **Scrape:** Company listings on Noon.com, Amazon.ae (Firecrawl)
- **Analyze:** Product photos, A+ content, pricing vs competitors, review sentiment, catalog completeness
- **Output:** Competitive positioning analysis + 3-5 improvement recommendations
- **Best for:** E-Commerce Manager, Key Account Manager, Trade Marketing Manager
- **Paula's edge:** Her Noon/Talabat/Deliveroo experience makes this especially credible

#### C) Brand & Competitor Analysis (`type: "brand_analysis"`)
- **Scrape:** Company website + 2-3 competitor websites in same sector/GCC
- **Analyze:** Brand positioning, messaging, target audience, product differentiation
- **Output:** Positioning map + gap analysis + opportunities
- **Best for:** Brand Manager, Category Manager, Senior Marketing Manager

#### D) 90-Day Action Plan (`type: "action_plan"`)
- **Input:** Job description + company research (no heavy scraping needed)
- **Analyze:** JD requirements mapped to Paula's experience → concrete initiatives
- **Output:** Week 1-2 (onboarding/audit), Month 1 (quick wins with metrics), Month 2-3 (strategic initiatives)
- **Best for:** Universal — works for any role. Most impressive to hiring managers

### Common Architecture

```python
def generate_deliverable(
    job: dict,
    analysis: dict,
    deliverable_type: str | None = None  # None = auto-select
) -> Path:
    """Generate a value-add deliverable for a job."""

def _auto_select_type(job: dict, analysis: dict) -> str:
    """Use Claude to pick the best deliverable type for this job/company."""

def _scrape_company(company: str, company_url: str | None, deliverable_type: str) -> dict:
    """Scrape company data via Firecrawl based on deliverable type needs."""

def _render_pdf(content: dict, deliverable_type: str, job: dict) -> Path:
    """Render deliverable content to a branded 1-2 page PDF."""
```

### Auto-selection Logic

When `deliverable_type=None`, Claude picks the best type based on:
- Job title (e-commerce role → ecommerce_teardown)
- Company sector (FMCG retail → brand_analysis)
- Available data (no e-commerce presence → skip teardown)
- Default fallback: `action_plan` (always applicable)

### PDF Output

- **Format:** 1-2 pages, clean professional layout
- **Header:** Paula's name + contact info + date
- **Title:** Type-specific (e.g., "Digital Presence Insights — Chalhoub Group")
- **Body:** 3-5 numbered observations, each with: finding → insight → recommendation
- **Footer:** "Prepared by Paula De Francisco — [LinkedIn URL]"
- **Filename:** `output/Deliverable_Paula_{Company}_{Role}_{Type}.pdf`
- **Rendering:** WeasyPrint (HTML → PDF), same as existing cover letter flow

### Integration Points

- **Pipeline** (`pipeline.py`): for Hot jobs (≥ 80), auto-generate after CV + cover letter
- **generate_for_job.py**: add `--deliverable` flag with optional type override
- **Outreach** (`outreach.py`): attach deliverable PDF to email draft alongside CV + cover letter. Mention it in email body ("I've also prepared a brief analysis of [Company]'s digital presence...")

### Dry-run behavior

When `PIPELINE_DRY_RUN=true`:
- Firecrawl scraping is skipped
- Uses placeholder company data
- Still generates PDF (useful for testing templates)

---

## Pipeline Integration (updated flow)

```
Discovery → Dedup → Hard Filters → Claude Scoring
                                        │
                                        ▼
                                   Score ≥ 60?
                                   ├── No → skip
                                   └── Yes (Warm + Hot)
                                        │
                                        ├── Contact Finder (Apollo)
                                        │   └── Notion Contacts DB
                                        │
                                        └── Score ≥ 80? (Hot only)
                                             ├── CV Generator
                                             ├── Cover Letter Generator
                                             ├── Deliverable Generator (auto-type)
                                             └── Outreach (email draft + LinkedIn messages)
                                                  └── Attachments: CV + CL + Deliverable
                                                  └── Personalized per contact found
```

---

## Files to Create / Modify

### New files:
- `career_ops/contact_finder.py` — Apollo integration + title inference
- `career_ops/generators/deliverables.py` — 4 deliverable types + PDF rendering

### Modified files:
- `career_ops/pipeline.py` — add contact-finding stage + deliverable generation for Hot jobs
- `career_ops/notion_sync.py` — add `sync_contacts()` function
- `career_ops/generators/outreach.py` — accept list of contacts, generate per-contact messages, attach deliverable
- `scripts/generate_for_job.py` — add `--contacts` and `--deliverable` flags
- `career_ops/config.py` — add any new settings (Firecrawl scrape limits, deliverable defaults)
- `.env.example` — document Apollo API key setup

### Example generation (for user evaluation):
- Pick 1 real job from `data/scored_jobs.json` (Hot score)
- Generate all 4 deliverable types for that job
- Output to `output/` for Paula to review and choose

---

## Verification Plan

1. **Contact Finder:**
   - Set `APOLLO_API_KEY` in `.env`
   - Run `python scripts/generate_for_job.py --job-id <id> --contacts` for a known company
   - Verify: contacts appear in console output + Notion Contacts DB
   - Verify: outreach email draft addresses contact by name

2. **Deliverables:**
   - Run `python scripts/generate_for_job.py --job-id <id> --deliverable digital_audit`
   - Repeat for `ecommerce_teardown`, `brand_analysis`, `action_plan`
   - Verify: 4 PDFs generated in `output/`
   - Verify: PDFs are 1-2 pages, professional, readable

3. **Full pipeline:**
   - Run `PIPELINE_DRY_RUN=true python -m career_ops.pipeline`
   - Verify: contact finding + deliverable generation stages execute without errors
   - Run without dry-run on 2-3 jobs, verify Notion + email drafts + attachments
