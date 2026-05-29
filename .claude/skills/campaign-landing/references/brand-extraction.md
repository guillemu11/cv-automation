# Brand extraction

How phase 1 of the campaign-landing skill pulls brand tokens from a live site. Derived from `wiki/concepts/brand-extraction-firecrawl.md`.

## Preferred path — Firecrawl branding format

If a Firecrawl API key is available in `.env` as `FIRECRAWL_API_KEY`:

```bash
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<company_url>", "formats": ["branding"]}'
```

Firecrawl returns a structured JSON with colors (hex), fonts detected in CSS, and logo URLs. Parse it into the `brand.json` shape defined in `workflow.md`.

## Fallback — WebFetch + inference

If no Firecrawl key, use WebFetch with a targeted prompt:

```text
Visit <company_url>. Extract a JSON object with this exact shape:
{
  "palette": {"primary": "<hex>", "secondary": "<hex>", "accent": "<hex>", "bg": "<hex>", "text": "<hex>"},
  "typography": {"display": "<font>", "body": "<font>"},
  "logo_hint": "<short visual description>",
  "tone": ["<adjective>", "<adjective>", "<adjective>"]
}
Base the palette on dominant colors you actually see. Do NOT invent.
Return ONLY valid JSON. No prose.
```

## Sub-brand focusing (`brand_override`)

When the target is a sub-brand under a parent company (Lipton under PepsiCo, Ben & Jerry's under Unilever, etc.), extraction should focus on the **sub-brand's** own site, not the parent. Examples:

- `company_name = "PepsiCo"`, `brand_override = "Lipton"` → extract from `lipton.com` (or the regional AMESA variant), not `pepsico.com`.
- The parent company's palette is almost always wrong for the campaign because Paula's campaign is for the sub-brand.

If unsure which URL belongs to the sub-brand, WebSearch `"<sub-brand> official site"` first.

## Tone extraction

Tone is inferred from the copy on the homepage, not the colors. WebFetch with:

```text
Read the headline, hero subhead, and first two body paragraphs of <url>.
Return a JSON array of 3-5 single-word adjectives describing the voice.
Examples of good adjectives: playful, authoritative, rebellious, calm, premium, accessible, witty.
Return ONLY the JSON array.
```

Feed this into `brand.json` → `tone`. Phase 2 uses tone to bias the 3 campaign angles toward voices the brand already uses (a "playful" brand gets witty campaign names; a "premium" brand gets restrained ones).

## Sanity checks

Before handing the JSON to phase 2:

- `palette.primary` and `palette.secondary` must be different hex values.
- `palette.text` on `palette.bg` must pass WCAG AA contrast (ratio ≥ 4.5). If not, swap `text` to `#111111` on light bg or `#F5F5F5` on dark bg.
- `typography.display` and `typography.body` must either be real web fonts (load from Google Fonts in the template) or `system-ui`. Never leave made-up font names.

If any check fails, fix it silently and note the correction in a `brand.notes` field.

## Write to disk

Final JSON goes to `output/landing_<slug>/brand.json`. Phase 5 reads it directly to populate the CSS custom properties in `styles.css`.