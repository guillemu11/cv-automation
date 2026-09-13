# Asset prompts — House Rules (Alabbar Enterprises & ANOTHER)

The 5 stills below were **generated in-project** with `career_ops/generators/images.py`
(Google Gemini image API, `gemini-3-pro-image`) and are live in the landing: 4 in the
"moments" gallery + the House Passport execution card.

To regenerate / tweak: edit the specs and run
`career_ops.generators.images.generate_batch(specs, "output/landing_alabbar/assets", aspect_ratio="4:5", ext="jpg")`.
Video (hero loop) stays optional and out-of-project for now.

Palette to enforce in every prompt: warm cream `#FBF9F5`, near-black `#141414`, Alabbar gold `#C8971C`,
warm espresso `#7A4E2D`. Editorial, sophisticated, guest-obsessed. **No people's faces** unless Paula
has rights. No logos of the real brands.

## Hero loop video (optional — Archetype B, replaces the typographic hero)
> 8s seamless loop, 1920×1080, ≤5MB, first frame == last frame.
> Slow, cinematic macro montage of hospitality "moments": a karak being poured from height into a glass
> cup (amber liquid, steam), a chocolate bar cracking, popcorn tumbling in gold light, a coffee crema
> swirl — each clip 1.5s, hard cuts on the beat. Warm cream and near-black set design, single gold key
> light. Premium, editorial, unbranded. Shallow depth of field. No text, no faces, no logos.

## Signature-moment stills (execution cards — 4:5, 2K, 4 iterations each)
1. **The karak pour** — amber tea poured from height into a clear glass, backlit steam, near-black
   backdrop, single warm key light, macro, editorial.
2. **The first crack** — a dark chocolate bar snapping in two, cocoa dust suspended mid-air, cream
   surface, gold rim light, macro.
3. **The gold shake** — caramel popcorn mid-tumble in a matte-black vessel, warm gold light, motion blur.
4. **The crema swirl** — espresso crema being drawn in a cup, top-down, warm cream saucer, minimal.

## House Passport (retail card — 4:5)
> A minimalist matte-black passport-style card with a gold foil emboss and a single QR, resting on a
> warm cream marble café table, soft daylight, shallow DOF. Premium stationery product shot. No text.

## Chaining tip
Generate #1 first, then pass it as a reference image to #2–#4 so lighting/finish stay consistent across
the set (identity/lighting chain). Keep every output on the 4-color palette above.
