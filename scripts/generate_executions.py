"""Generate 6 campaign execution mockups for the Lipton pitch landing.

Each image is 16:9 via Imagen 4, matching the brand palette extracted in
brand.json. Output: output/landing_lipton/assets/executions/exec_{1..6}.jpg
(JPEG to keep page weight reasonable — originals are 1408x768 PNG from Imagen).

Cost: ~$0.04 per image × 6 = ~$0.24 total.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image as PILImage
from io import BytesIO

load_dotenv()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

OUT_DIR = Path("output/landing_lipton/assets/executions")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Shared visual language across all 6 mockups.
STYLE = (
    "Ultra-realistic cinematic photograph, wide 16:9 horizontal composition, "
    "premium advertising campaign shot. Brand colors: vivid Lipton yellow "
    "(#FFD100), deep red (#E30613), and warm golden-amber light. Dramatic "
    "lighting, shallow depth of field, editorial high-end fashion-magazine grade, "
    "photorealistic, natural skin tones, no plastic-looking faces, no extra text "
    "overlays except where explicitly described. Negative: no stock-photo feel, "
    "no cheap clipart, no watermarks, no logos other than Lipton, no AI artifacts "
    "on hands or faces."
)

EXECUTIONS = [
    {
        "slug": "exec_1_ooh",
        "label": "OOH · Sheikh Zayed Rd",
        "prompt": (
            "A massive outdoor digital billboard on Sheikh Zayed Road in Dubai at "
            "golden hour. The billboard displays the Lipton Ice Tea yellow logo "
            "with the red shield and a bold tagline in Archivo Black typography "
            'reading "HALF THE SUGAR.". The billboard glows warm in the low desert '
            "sun, with the Dubai skyline and Burj Khalifa visible in the distance. "
            "Cars streaming on the highway below with motion blur. Warm amber "
            "sunset sky. "
        ),
    },
    {
        "slug": "exec_2_tiktok",
        "label": "Social · TikTok",
        "prompt": (
            "A phone screen held vertically at arms length showing a TikTok video "
            "of a young Middle-Eastern Gen Z woman in Dubai holding a can of Lipton "
            "Ice Tea Half-Sugar up to the sun, golden hour lighting, warm "
            "sun-drenched café terrace background, shallow depth of field. The "
            "TikTok UI is visible around the video with the hashtag "
            "#HalfTheSugarChallenge overlayed in yellow. Cinematic photograph of "
            "the hand holding the phone, blurred background shows the real café. "
        ),
    },
    {
        "slug": "exec_3_cooler",
        "label": "In-store · Carrefour",
        "prompt": (
            "Inside a Carrefour hypermarket in the UAE, a dedicated branded cooler "
            "zone completely wrapped in Lipton yellow vinyl, glowing warm yellow "
            "from within, stocked with cans of Lipton Ice Tea Half-Sugar. A large "
            "yellow sign above the cooler reads in Archivo Black typography "
            '"THE 3PM COOLER". A woman in her late twenties is reaching in to '
            "grab a can. The rest of the supermarket aisle is out of focus in the "
            "background. Clean, modern retail photography, bright store lighting "
            "mixed with the warm yellow cooler glow. "
        ),
    },
    {
        "slug": "exec_4_delivery",
        "label": "Digital · Delivery apps",
        "prompt": (
            "A top-down flat-lay photograph on a warm wooden table of a food "
            "delivery order just arrived from a UAE delivery app — a chicken "
            "shawarma wrap in open paper, fries, and next to them a chilled "
            "free can of Lipton Ice Tea with condensation. A small printed card "
            'next to the can reads "FREE WITH YOUR 3PM ORDER". Warm afternoon '
            "window light falling diagonally across the table. Hands of a person "
            "(out of focus) reaching in from one side. Premium food photography, "
            "high end editorial magazine style. "
        ),
    },
    {
        "slug": "exec_5_ramadan",
        "label": "Experiential · Ramadan",
        "prompt": (
            "An intimate iftar table scene at sunset, traditional Emirati majlis "
            "setting with ornate carpets and soft lanterns. On the table: dates, "
            "laban, and a tall chilled glass of Lipton Ice Tea with ice cubes "
            "visible, just poured, condensation on the glass. Warm amber dusk "
            "light streaming through a mashrabiya window casting geometric "
            "shadows on the table. A single yellow Lipton can placed beside the "
            "glass. Dramatic cinematic lighting, shallow depth of field focused "
            "on the glass. Authentic Middle Eastern atmosphere, respectful and "
            "warm, no people in frame. "
        ),
    },
    {
        "slug": "exec_6_creator",
        "label": "Creator · Influencer",
        "prompt": (
            "A split-panel editorial photograph showing the same young Arab "
            "woman creator holding a Lipton Ice Tea can in two completely "
            "different afternoon locations: left half of the image is her in a "
            "modern Dubai Marina office with floor-to-ceiling windows at 3pm, "
            "right half is her in a vibrant Cairo rooftop at golden hour with "
            "old-city buildings behind her. Both halves share the same warm "
            "afternoon color grade. She holds the same yellow Lipton can in "
            "both frames. Clean vertical divider line between the two halves. "
            'A small kicker caption overlay in the bottom corner reads "7 AFTERNOONS, 7 CITIES". '
        ),
    },
]


def main() -> None:
    client = genai.Client(api_key=GEMINI_API_KEY)
    for i, exe in enumerate(EXECUTIONS, 1):
        print(f"\n[{i}/6] {exe['label']}  -> {exe['slug']}.jpg")
        full_prompt = exe["prompt"] + STYLE
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=full_prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
            ),
        )
        if not response.generated_images:
            print(f"  !! no image returned for {exe['slug']}")
            continue
        png_bytes = response.generated_images[0].image.image_bytes
        img = PILImage.open(BytesIO(png_bytes)).convert("RGB")
        out = OUT_DIR / f"{exe['slug']}.jpg"
        img.save(out, format="JPEG", quality=85, optimize=True)
        print(f"  saved {out} ({out.stat().st_size // 1024} KB)")

    print("\nDONE. Files in", OUT_DIR)


if __name__ == "__main__":
    main()
