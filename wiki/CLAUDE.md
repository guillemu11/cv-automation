# CLAUDE.md — Wiki schema

This file governs how Claude Code operates **inside this `wiki/` directory**. It does NOT replace the root `../CLAUDE.md`, which describes the Python pipeline (`career_ops/`). When a question is about code or the pipeline, the root file takes precedence. When a question is about the knowledge base, this file takes precedence.

## What this is

This vault is an **LLM Wiki** in the style of Andrej Karpathy's pattern: a persistent, interlinked knowledge base that *Claude* maintains on behalf of the user (Paula). Paula curates sources and asks questions; Claude does all the writing, linking, summarizing, and bookkeeping.

The wiki is NOT a chat log, NOT a RAG index, and NOT a place for Paula to take notes. It is a **compounding artifact** — every new source makes the existing pages richer, and Claude does the work of weaving it in.

**Two integrated domains**:
- **`jobs`** — Dubai job search research: companies, recruiters, industries, JD patterns, salary data, market intelligence.
- **`ai`** — AI/ML research that can feed back into the `career_ops/` pipeline: papers, techniques, prompts, agent patterns, tooling.

Cross-references between the two domains are welcome and encouraged.

## Directory layout

```
wiki/
├── CLAUDE.md          ← this file (schema)
├── README.md          ← human quick-start
├── index.md           ← catalog of all pages (Claude maintains)
├── log.md             ← append-only operations log
├── raw/               ← IMMUTABLE source documents. Claude only reads.
│   ├── jobs/          ← JDs, company pages, LinkedIn posts, recruiter profiles
│   ├── ai/            ← papers, blog posts, podcast notes, technical threads
│   └── assets/        ← images (from Obsidian Web Clipper, etc.)
├── entities/          ← pages for things with identity (company, person, product)
├── concepts/          ← pages for ideas (role types, industries, techniques)
├── sources/           ← one page per ingested source
│   ├── jobs/
│   └── ai/
└── synthesis/         ← cross-cutting analyses, theses, comparisons
```

**The raw/ rule**: Claude **never** writes, edits, renames, or moves files inside `raw/`. It is the immutable source of truth. All derived knowledge lives in the other folders.

## Frontmatter (mandatory on every page)

Every `.md` file outside of `raw/`, `index.md`, `log.md`, `CLAUDE.md`, and `README.md` MUST start with YAML frontmatter:

```yaml
---
type: entity | concept | source | synthesis
domain: jobs | ai | both
tags: [tag1, tag2, ...]
status: stub | draft | active | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["[[source-page-slug]]", ...]
---
```

- `type` matches the folder.
- `domain` enables filtering across the wiki.
- `tags` are Obsidian tags (lowercase, hyphenated).
- `status: stub` for auto-created placeholder pages that other pages link to; `draft` while being written; `active` once populated; `archived` when superseded.
- `sources` is the list of source pages that back the claims in this page. Every factual claim in an entity/concept/synthesis page should be traceable to at least one source.

## Link conventions

- Use **wikilinks** `[[Page Name]]` whenever you mention an entity or concept that has (or should have) its own page.
- If the target doesn't exist yet, **create it as a stub** with correct frontmatter (`status: stub`) and a one-line placeholder body. Do not leave dangling links.
- Wikilink slugs use Title Case with spaces (Obsidian handles both `[[Emirates Group]]` and `[[emirates-group]]`). Prefer Title Case for human readability.
- For external URLs, use standard markdown `[text](https://...)`.

## Contradiction markers

When a new source contradicts an existing claim, mark it explicitly on the affected page using an Obsidian callout:

```markdown
> [!warning] Contradiction
> [[old-source]] claims X, but [[new-source]] claims Y. As of <date>, unresolved.
```

Do not silently overwrite. Preserve the tension until the user explicitly resolves it.

## Ingest workflow

When the user says something like "ingesta esto", "añade esta fuente", or points at a file in `raw/`:

1. **Read** the raw file in full.
2. **Discuss** — in the chat, give the user a brief summary (TL;DR + 3-5 key takeaways) and wait for reaction before writing anything. The user may want to emphasize specific angles.
3. **Create the source page** at `sources/<domain>/<slug>.md` with this structure:
   ```markdown
   ---
   type: source
   domain: jobs | ai | both
   tags: [...]
   status: active
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   sources: []
   ---
   # <Title>

   **Source**: `raw/<domain>/<filename>` (or URL if web)
   **Author / Publisher**:
   **Date published**:

   ## TL;DR
   <2-3 sentences>

   ## Key takeaways
   - ...

   ## Quotes
   > ...

   ## Entities mentioned
   - [[Entity A]]
   - [[Entity B]]

   ## Concepts touched
   - [[Concept X]]
   ```
4. **Propagate to entities/concepts**: for each `[[Entity]]` or `[[Concept]]` mentioned:
   - If the page doesn't exist → create a stub with correct frontmatter and add it to the Entities Mentioned / Concepts section.
   - If it exists → append new evidence, citing `[[source-page]]`. Update `updated:` field and add the source to `sources:` if not already there. If the new info contradicts, use the callout.
5. **Update `index.md`** — add the new source page and any new entity/concept stubs under the right sections. Keep the index sorted alphabetically within each section.
6. **Append to `log.md`** using the parseable prefix:
   ```markdown
   ## [YYYY-MM-DD] ingest | <Source Title>
   Created: sources/jobs/acme-jd.md
   New stubs: [[Acme Corp]], [[Brand Manager UAE]]
   Updated: [[Dubai Retail Sector]], [[index]]
   ```

## Query workflow

When the user asks a question against the wiki:

1. **Read `index.md` first** to find relevant pages. Do NOT glob the whole vault.
2. **Read the relevant pages** (entities, concepts, synthesis, sources).
3. **Answer with citations**: every non-trivial claim should link back to its source via `[[source-page]]` or `[[entity]]` wikilinks.
4. **Offer to file the answer**: at the end, ask if the answer should be saved as a new page under `synthesis/` so future questions benefit. Save only if the user agrees — don't pollute the wiki with every chat exchange.
5. **Log the query** in `log.md`:
   ```markdown
   ## [YYYY-MM-DD] query | <short question>
   Pages read: [[a]], [[b]], [[c]]
   Filed as: synthesis/<slug>.md (or "not filed")
   ```

## Lint workflow

When the user says "lint the wiki", "health check", or similar:

1. **Orphan pages** — pages with zero backlinks from other wiki pages (use grep/search, not a full read). Flag as candidates for deletion or re-linking.
2. **Dangling stubs** — `status: stub` pages older than 7 days with no content added.
3. **Concepts without pages** — grep for phrases that look like they should be entities/concepts but are plain text. Suggest creating pages.
4. **Unresolved contradictions** — all `> [!warning] Contradiction` callouts still present. List them.
5. **Stale claims** — any page where `updated:` is older than 90 days AND new sources have been added to the same `domain` since. Flag for refresh.
6. **Missing cross-references** — entity A mentions entity B in prose but without `[[B]]` link.
7. **Data gaps** — concepts with `<3` sources backing them. Suggest web searches or new source hunts.

Output as an actionable checklist. Do NOT fix automatically — present the list and ask which items to address.

## Hard rules

- Never edit files in `raw/`. Read only.
- Never delete pages without explicit user confirmation. Archive instead (`status: archived`, move to bottom of index).
- Never break wikilinks. If you rename a page, grep all `[[old-name]]` references and update them atomically.
- Every factual claim on an entity/concept/synthesis page must have a `[[source-page]]` citation.
- When in doubt about structure, ask the user rather than guessing.
- Do NOT write personal notes on behalf of the user. The user writes thoughts in chat; you translate them into structured wiki updates only when they ask.

## Output discipline

- Keep page bodies tight. Prefer bullet lists over paragraphs where possible.
- Dates are always `YYYY-MM-DD`. Today is available from the session context.
- Slugs are lowercase-hyphenated. Page titles in H1 are Title Case.
- Don't add emoji unless the user asks.
