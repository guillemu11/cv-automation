"""Generate the Lipton hero loop video via Kie.ai (Nano Banana + Seedance 2).

Flow:
  1. Nano Banana 2: generate keyframe A (full-sun, dark-amber liquid)
  2. Nano Banana Edit: generate keyframe B using A as reference (two-suns, lighter liquid)
  3. Seedance 2: interpolate A -> B into an 8s loop (16:9, 720p)
  4. Download the MP4 to output/landing_lipton/assets/hero-loop.mp4

Respects PIPELINE_DRY_RUN=true (prints what it would do and exits).
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

KIE_API_KEY = os.environ.get("KIE_API_KEY")
if not KIE_API_KEY:
    sys.exit("KIE_API_KEY missing from environment (.env)")

DRY_RUN = os.environ.get("PIPELINE_DRY_RUN", "").lower() == "true"

BASE = "https://api.kie.ai/api/v1/jobs"
HEADERS = {
    "Authorization": f"Bearer {KIE_API_KEY}",
    "Content-Type": "application/json",
}

OUTPUT_DIR = Path("output/landing_lipton/assets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --- Prompts ----------------------------------------------------------------

PROMPT_A = (
    "Cinematic studio photograph of a single Lipton Ice Tea bottle standing vertically "
    "in the dead center of the frame. The bottle has a clean yellow label with red "
    "accents and is filled with dark amber tea liquid. Behind the bottle: a large "
    "golden desert sun low on the horizon, heat haze, warm orange-to-black vertical "
    "gradient sky. The bottle catches the backlight, producing a gentle rim light on "
    "its edges. Surface is a matte dark ground that fades to black at the edges. "
    "Ultra sharp product photography, shallow depth of field, 16:9, 2K, no shadows on "
    "the ground, no hands, no text on the bottle other than the yellow label, no "
    "reflections, no people, no logos other than Lipton, cinematic color grade."
)

PROMPT_B = (
    "Same Lipton Ice Tea bottle, exact same composition, same camera angle, same "
    "framing, same product — but the tea liquid inside is now visibly HALF as dark, "
    "a lighter translucent golden color (simulating 50% less sugar). Behind the "
    "bottle there are now TWO suns side by side instead of one, both glowing bright "
    "yellow-white, casting a brighter sky with a warmer peachy-gold gradient. Same "
    "matte dark ground fading to black. Ultra sharp, cinematic, 16:9, 2K, no "
    "shadows, no hands, no extra text, no reflections, no people, keep the bottle "
    "100% identical to the reference image — only the liquid color and the sky change."
)

PROMPT_VIDEO = (
    "A smooth cinematic product video. The camera stays locked on the Lipton Ice Tea "
    "bottle. Across 8 seconds the scene transitions naturally: the single sun in the "
    "background splits and becomes two suns, the tea liquid inside the bottle "
    "gradually lightens from dark amber to translucent gold, and the sky warms to a "
    "peachy-gold gradient. The bottle itself does not move or rotate — only the light "
    "and the liquid change. End frame exactly matches the reference last-frame image. "
    "No camera shake, no zoom, no text overlay, no people, no hands, no shadows on "
    "the ground, seamless cinematic grade."
)

# --- Kie.ai helpers ---------------------------------------------------------


def create_task(body: dict) -> str:
    if DRY_RUN:
        print(f"[DRY RUN] POST {BASE}/createTask  body={json.dumps(body)[:200]}...")
        return "dry-run-task-id"
    r = requests.post(f"{BASE}/createTask", headers=HEADERS, json=body, timeout=60)
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        raise RuntimeError(f"Kie createTask failed: {data}")
    task_id = data["data"]["taskId"]
    print(f"  -> task {task_id}")
    return task_id


def poll_task(task_id: str, label: str, timeout_s: int = 600) -> dict:
    """Poll until state == 'success' (or 'fail'). Returns parsed resultJson."""
    if DRY_RUN:
        print(f"[DRY RUN] would poll task {task_id}")
        return {"resultUrls": ["https://dry-run.example/placeholder.png"]}
    deadline = time.time() + timeout_s
    last_state = None
    while time.time() < deadline:
        r = requests.get(
            f"{BASE}/recordInfo",
            headers=HEADERS,
            params={"taskId": task_id},
            timeout=30,
        )
        r.raise_for_status()
        data = r.json().get("data", {})
        state = data.get("state")
        if state != last_state:
            print(f"  [{label}] state={state}")
            last_state = state
        if state == "success":
            result_json = data.get("resultJson") or "{}"
            return json.loads(result_json)
        if state in ("fail", "failed", "error"):
            raise RuntimeError(f"Kie task {task_id} failed: {data}")
        time.sleep(5)
    raise TimeoutError(f"Kie task {task_id} timed out after {timeout_s}s")


def download(url: str, dest: Path) -> None:
    if DRY_RUN:
        print(f"[DRY RUN] would download {url} -> {dest}")
        return
    print(f"  downloading -> {dest}")
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 15):
                f.write(chunk)
    print(f"  saved {dest.stat().st_size // 1024} KB")


# --- Pipeline ---------------------------------------------------------------


def main() -> None:
    print(f"generate_hero.py  DRY_RUN={DRY_RUN}")
    print(f"output dir: {OUTPUT_DIR}")

    # 1. Keyframe A (text-to-image)
    print("\n[1/3] Keyframe A — one sun, dark amber liquid")
    task_a = create_task(
        {
            "model": "google/nano-banana",
            "input": {
                "prompt": PROMPT_A,
                "output_format": "png",
                "image_size": "16:9",
            },
        }
    )
    result_a = poll_task(task_a, "keyframe A")
    url_a = result_a["resultUrls"][0]
    print(f"  keyframe A URL: {url_a}")
    download(url_a, OUTPUT_DIR / "hero-keyframe-a.png")

    # 2. Keyframe B (reference-chain edit from A)
    print("\n[2/3] Keyframe B — two suns, half-sugar light golden liquid")
    task_b = create_task(
        {
            "model": "google/nano-banana-edit",
            "input": {
                "prompt": PROMPT_B,
                "image_urls": [url_a],
                "output_format": "png",
                "image_size": "16:9",
            },
        }
    )
    result_b = poll_task(task_b, "keyframe B")
    url_b = result_b["resultUrls"][0]
    print(f"  keyframe B URL: {url_b}")
    download(url_b, OUTPUT_DIR / "hero-keyframe-b.png")

    # 3. Kling 3.0 video (A -> B, 8s, 16:9, pro mode = 1080p)
    #    image_urls[0] = first frame, image_urls[1] = last frame.
    print("\n[3/3] Kling 3.0 video — 8s interpolation A->B (pro 1080p)")
    task_v = create_task(
        {
            "model": "kling-3.0/video",
            "input": {
                "prompt": PROMPT_VIDEO,
                "image_urls": [url_a, url_b],
                "duration": "8",
                "aspect_ratio": "16:9",
                "mode": "pro",
                "multi_shots": False,
                "sound": False,
            },
        }
    )
    result_v = poll_task(task_v, "seedance video", timeout_s=1200)
    video_url = result_v["resultUrls"][0]
    print(f"  video URL: {video_url}")
    download(video_url, OUTPUT_DIR / "hero-loop.mp4")

    print("\nDONE. Update index.html <video> src to assets/hero-loop.mp4")


if __name__ == "__main__":
    main()
