---
type: concept
domain: ai
tags: [nano-banana, keyframe, image-generation, kling, seedance, kie-ai]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-claude-nano-banana-websites]]", "[[nate-herk-nano-banana-2-websites]]", "[[nate-herk-seedance-2-websites]]", "[[nick-saraev-claude-kling-animated-sites]]", "[[jack-roberts-firecrawl-intelligence-websites]]"]
---

# Nano Banana Keyframe Workflow

The upstream half of every AI-generated landing-page animation: producing two consistent keyframe images (start and end) that a video model can interpolate between. The animation is only as good as the keyframes.

## Why two images, not a prompt

Text-to-video models produce random motion. The seed determines the composition, and you rarely get exactly what you want. The workaround: use a text-to-image model with strong prompt adherence (Nano Banana 2 / Gemini Image), generate the two extreme states separately, then hand both as first-frame + last-frame to an image-to-video model. The video model now has only one job: interpolate. This is vastly more controllable.

## The recipe

**Step 1 — Reference image (optional but recommended).** If the subject is a real product or brand, grab an existing photo of it from the company's own website or Google Images. This anchors the model to the correct shape/logo/form factor.

**Step 2 — Start frame.** Prompt Nano Banana 2 with:

- 16×9 aspect ratio (matches video output)
- ≥ 2K resolution (1K looks amateur per [[jack-roberts-claude-nano-banana-websites]])
- 4 iterations minimum — the keyframes matter too much to settle for the first
- "Clean [black|white] background, nothing touching the edges"
- Reference image attached

**Step 3 — End frame.** Same prompt structure, but describe the end state:

- "exploded", "deconstructed", "opened", "in pieces", "fully built"
- **Use the start frame as a reference image** via Nano Banana's reference feature. This maintains visual consistency — same logo placement, same lighting, same materials. Without this, the end frame drifts and the video transition looks wrong.

**Step 4 — Animate.** Feed start frame and end frame to [[Kling 3.0]] (or Seedance 2.0). Prompt describes the motion: "The lid floats off. Fruit and juice are dropped in from above. The lid returns. No shadows, no hands, no reflections." 7-10 seconds is the sweet spot — [[nate-herk-seedance-2-websites]] found 10s feels more engaging than 15s.

**Step 5 — The Claude-for-prompts trick.** Both Nate and Jack recommend pasting both keyframes into Claude (regular chat, not Code) and asking: "Write me an AI video prompt to transition from image A to image B, with these constraints: [...]". Claude writes a prompt optimized for the motion you want. Paste it into Kling. Reliable.

## Negative prompts that matter

Across sources, the same cruft keeps appearing in generations unless explicitly excluded:

- "no shadows"
- "no hands"
- "no reflections"
- "no text" (unless you want text, in which case specify exact placement)
- "clean background"
- "no people"

Add these as defaults to any prompt template.

## Seamless loop variant (for hero videos, not scroll)

For [[Seedance Loop Video Hero]] use cases, set **first frame = last frame** (same image in both slots). The model generates motion in the middle and returns to the start, making the loop invisible. See [[Seedance Loop Video Hero]] for the full variant.

## Model access

[[Kie.ai]] is the consolidation point: one API key hits Nano Banana 2, Seedance 2, Kling 3, GPT-image, Qwen, and Gemini 3. For Paula's skill, this avoids maintaining 5 separate API clients. Credits-based pricing (not per-minute) is predictable.

Alternative: [[Hixelon]] for the video step (Jack's choice). Either works — Hixelon is UI-friendly, Kie.ai is better for automation.

## Costs (rough, 2025)

- Nano Banana 2 image: ~$0.02-0.05 per image × 4 iterations × 2 frames = ~$0.30-0.40 for a pair of keyframes
- Seedance 2 10s video at 720p: ~$0.82 (410 credits at Kie.ai pricing)
- Kling 3.0 7s video: similar range

Total per landing page hero animation: **~$1-2** in model costs. Cheap enough that Paula can afford to iterate and regenerate for every "hot" job application.

## The Higgsfield reference-image chain (for before/after animations)

[[jack-roberts-firecrawl-intelligence-websites]] demonstrates the cleanest way to maintain composition consistency across keyframes when you want a "state A → state B" animation (dirty pool → clean pool, messy room → tidy room, empty store → packed store):

1. Generate **keyframe A** with Nano Banana 2 in Higgsfield. 4 iterations, 2K, 16×9, clean white background, description of state A.
2. Pick the best of the 4 iterations.
3. **Click "reference" on that image** in the Higgsfield UI. This uses it as the visual anchor for the next generation.
4. Delete the prompt, paste the **keyframe B** prompt (the "state B" description).
5. Generate. The output keeps the exact same pool shape, camera angle, water level, lighting — only the described state changes. This is why the resulting Kling video transition looks coherent.

Without this reference chain, the two states drift in composition (different pool angles, different water levels) and the video model has to "fake" a transition between two unrelated scenes. The result is visibly broken.

In Nano Banana 2 directly (not via Higgsfield), the equivalent is attaching keyframe A as an input image when generating keyframe B — same idea, different UI.

## Parallel generation for probability

[[nick-saraev-claude-kling-animated-sites]] recommends kicking off **2-3 Kling generations simultaneously** instead of sequential. Kling/Higgsfield don't queue your requests — they run in parallel. Cost is 2-3× but so is the probability that one of them matches what you want. Given that a single generation is $0.40-1.00, spending $1-3 to triple your odds is the right tradeoff.

## Related concepts

- [[Scroll-Driven Animation]] — downstream consumer of the keyframes.
- [[Seedance Loop Video Hero]] — the loop variant.
- [[Brand Extraction with Firecrawl]] — upstream: provides brand colors that should appear in the generated images.
