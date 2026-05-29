"""Generate 3 city keyframes for the Lipton "17 Bottlers, One Tea" landing.

Each keyframe shows the SAME Lipton bottle in the same frame position
(foreground-right, lower third), with a different AMESA cityscape behind it.
Imagen 4 produces Dubai (KF_A) natively 16:9. Flash Image edit then uses
Dubai as visual anchor to lock the bottle for Cairo (KF_B) and Karachi (KF_C),
so the bottle stays consistent across the 3 cities while the landscape changes.

Cost: 1 Imagen 4 (~$0.04) + 2 Flash edits (~$0.08) = ~$0.12 total.
"""

from __future__ import annotations

import os
from io import BytesIO
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

OUT = Path("output/landing_lipton_v3/assets/cities")
OUT.mkdir(parents=True, exist_ok=True)

KF_DUBAI = OUT / "01_dubai.jpg"
KF_CAIRO = OUT / "02_cairo.jpg"
KF_KARACHI = OUT / "03_karachi.jpg"

# ============================================================================
# Prompts
# ============================================================================

_SHARED = (
    "Cinematic ultra-realistic editorial travel photograph, 16:9 horizontal "
    "composition, 2K quality. In the foreground, lower-right third of the "
    "frame, stands a single real Lipton Ice Tea bottle — the iconic yellow "
    "Lipton label with the red Lipton shield logo faces the camera, upright "
    "and fully legible, not mirrored. The bottle is lit dramatically by the "
    "same directional warm amber light in every image. Behind and around the "
    "bottle stretches a specific cityscape. The sky dominates the upper half "
    "of the frame. The bottle occupies roughly the same physical area of the "
    "frame in every image so a viewer flipping between images only sees the "
    "city change, not the product. Premium National-Geographic-meets-Apple-"
    "campaign aesthetic. Negative: no people, no hands, no extra bottles, no "
    "text overlays, no watermarks, no logos other than Lipton, no tourist-"
    "cliche shots."
)

PROMPT_DUBAI = (
    "Subject: Lipton Ice Tea bottle in foreground-right, Dubai skyline behind "
    "it in the middle and background. Visible: the Burj Khalifa piercing into "
    "a peachy-pink sunrise sky on the left, Sheikh Zayed Road with modern "
    "glass towers trailing into distance, a hint of desert dunes beyond. Time "
    "of day: dawn, cool blue shadows meeting warm orange sun on the horizon. "
    "Color grade: cool steel-blue in shadows, warm amber highlights on the "
    "bottle. "
    + _SHARED
)

PROMPT_CAIRO = (
    "Keep the Lipton Ice Tea bottle in EXACTLY the same position, scale, "
    "angle, and lighting as in the reference image. The bottle itself is "
    "unchanged. Replace ONLY the background and surroundings with a Cairo "
    "scene at golden-hour: the Pyramids of Giza rising in the middle ground "
    "under a hazy dusty-amber sky, silhouettes of minarets of the old Islamic "
    "Cairo skyline on the right, the Nile river reflecting warm orange light "
    "in the distance. Time of day: late golden hour, warm dusty-amber haze. "
    "Color grade: saturated warm ochres, dusty rose in the sky, the bottle "
    "still catches the same warm highlight. Keep the bottle identical to the "
    "reference image — do not move, resize, relabel, or rotate it. "
    + _SHARED
)

PROMPT_KARACHI = (
    "Keep the Lipton Ice Tea bottle in EXACTLY the same position, scale, "
    "angle, and lighting as in the reference image. The bottle itself is "
    "unchanged. Replace ONLY the background and surroundings with a Karachi "
    "scene at dusk: the Arabian Sea meeting the horizon on the left lit by a "
    "vibrant coral-red sunset, the silhouette of the Mazar-e-Quaid monument "
    "and a dense layered mid-rise Karachi cityscape extending to the right, "
    "warm yellow-orange streetlights starting to glow in the far distance. "
    "Time of day: dusk, magic hour, the sky is a gradient from deep coral-red "
    "at the horizon to purple at the zenith. Color grade: rich saturated reds "
    "and purples, the bottle still catches the warm highlight. Keep the "
    "bottle identical to the reference image — do not move, resize, relabel, "
    "or rotate it. "
    + _SHARED
)

# ============================================================================
# Generation helpers
# ============================================================================


def imagen_generate(prompt: str, out_path: Path) -> None:
    from google import genai
    from google.genai import types
    from PIL import Image as PILImage

    client = genai.Client(api_key=GEMINI_API_KEY)
    print(f"  [imagen4] generating -> {out_path.name}")
    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt,
        config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio="16:9"),
    )
    if not response.generated_images:
        raise RuntimeError(f"Imagen returned nothing: {response}")
    png_bytes = response.generated_images[0].image.image_bytes
    img = PILImage.open(BytesIO(png_bytes)).convert("RGB")
    img.save(out_path, format="JPEG", quality=88, optimize=True)
    print(f"  [imagen4] saved {out_path} ({out_path.stat().st_size // 1024} KB)")


def flash_edit(prompt: str, reference: Path, out_path: Path, target_size: tuple[int, int]) -> None:
    from google import genai
    from PIL import Image as PILImage

    client = genai.Client(api_key=GEMINI_API_KEY)
    ref_img = PILImage.open(reference)
    print(f"  [flash-edit] generating -> {out_path.name}")
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt, ref_img],
    )
    raw = None
    for cand in response.candidates or []:
        for part in cand.content.parts or []:
            if getattr(part, "inline_data", None) is not None:
                raw = part.inline_data.data
                break
        if raw:
            break
    if raw is None:
        raise RuntimeError("Flash Image returned no image")

    img = PILImage.open(BytesIO(raw)).convert("RGB")
    w, h = img.size
    tw, th = target_size
    tr = tw / th
    cr = w / h
    if cr > tr:
        new_w = int(h * tr)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / tr)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    img = img.resize(target_size, PILImage.LANCZOS)
    img.save(out_path, format="JPEG", quality=88, optimize=True)
    print(f"  [flash-edit] cropped to {target_size} -> {out_path.stat().st_size // 1024} KB")


# ============================================================================


def main() -> None:
    from PIL import Image as PILImage

    print("\n[1/3] Imagen 4 — Dubai (reference keyframe)")
    imagen_generate(PROMPT_DUBAI, KF_DUBAI)

    target = PILImage.open(KF_DUBAI).size
    print(f"  reference size: {target}")

    print("\n[2/3] Flash edit — Cairo (bottle locked from Dubai)")
    flash_edit(PROMPT_CAIRO, KF_DUBAI, KF_CAIRO, target)

    print("\n[3/3] Flash edit — Karachi (bottle locked from Dubai)")
    flash_edit(PROMPT_KARACHI, KF_DUBAI, KF_KARACHI, target)

    print("\nDONE")


if __name__ == "__main__":
    main()
