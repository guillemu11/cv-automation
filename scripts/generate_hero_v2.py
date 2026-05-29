"""Scroll-frame hero generator for the Lipton campaign landing.

Concept "The Pour": a glass of ice sitting in warm light. A Lipton bottle pours
tea into it. First half of the pour = dark amber (full sugar). Second half =
lighter translucent gold (half sugar). Final frame = half-dark, half-gold glass.

Pipeline:
  1. Gemini 2.5 Flash Image  -> keyframe A (empty glass of ice, bottle about to pour)
  2. Gemini 2.5 Flash Image  -> keyframe B (full glass, half dark / half gold)
     (passes keyframe A as reference image to preserve composition)
  3. Kie.ai Kling 3.0 pro    -> 10s image-to-video A -> B (1080p)
  4. ffmpeg (imageio-ffmpeg) -> extract ~150 frames as .webp for scroll binding

Cost: ~$0.08 Gemini + ~$0.90 Kie = ~$1 total.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
KIE_API_KEY = os.environ["KIE_API_KEY"]

# --- Config -----------------------------------------------------------------
OUT = Path("output/landing_lipton/assets")
OUT.mkdir(parents=True, exist_ok=True)
FRAMES_DIR = OUT / "frames"
FRAMES_DIR.mkdir(parents=True, exist_ok=True)

KEYFRAME_A = OUT / "hero-keyframe-a.png"
KEYFRAME_B = OUT / "hero-keyframe-b.png"
HERO_MP4 = OUT / "hero-loop.mp4"
FRAME_COUNT = 150  # frames extracted from the video for the scroll sequence

KIE_BASE = "https://api.kie.ai/api/v1/jobs"
KIE_HEADERS = {
    "Authorization": f"Bearer {KIE_API_KEY}",
    "Content-Type": "application/json",
}

# --- Prompts ----------------------------------------------------------------

_COMMON_SCENE = (
    "Cinematic ultra-realistic product photograph, wide 16:9 horizontal composition, "
    "2K quality. Scene: a tall clear pint-style glass tumbler packed with large, "
    "crystal-clear ice cubes, standing on a matte black reflective surface at the "
    "exact center of the frame. Directly ABOVE and slightly to the right of the "
    "glass, a real Lipton Ice Tea bottle is tilted at a gentle 20 degrees from "
    "vertical — nearly upright, only slightly tipped. The bottle's OPEN NECK and "
    "MOUTH point straight down toward the center of the glass rim, so any liquid "
    "would fall cleanly and vertically from the mouth into the ice. The bottle "
    "CAP has been removed and lies flat on the matte surface to the right of the "
    "glass, clearly visible, yellow-and-red. The bottle body shows the iconic "
    "yellow Lipton label with the red Lipton shield logo, label facing the camera "
    "directly, upright and fully legible, NOT mirrored, NOT upside down. "
    "Background: a deep moody warm gradient — near-black at the top fading to a "
    "rich peachy-amber glow at the bottom, with a soft out-of-focus warm window "
    "shape behind suggesting low sunlight. Strong rim-light on the glass and ice, "
    "shallow depth of field, dramatic cinematic color grade, like a high-end "
    "beverage commercial. Negative: no hands, no people, no extra text, no "
    "watermarks, no mirrored logos, no floor shadows, no reflections of a studio "
    "setup, no additional bottles or glasses, no liquid emerging from the side of "
    "the bottle, no cap on the bottle."
)

PROMPT_A = (
    _COMMON_SCENE
    + " State of the scene: the bottle is positioned above the glass ready to "
    "pour but NO liquid is falling yet. The glass contains only clear ice — no "
    "tea yet. The bottle's open mouth is aimed perfectly at the center of the "
    "glass rim, as if the pour is about to start in the next second."
)

PROMPT_B = (
    _COMMON_SCENE
    + " State of the scene: the glass is now completely full of Lipton iced tea, "
    "filled to just below the rim over the ice. The tea is a rich golden-amber "
    "color, slightly translucent, with the ice cubes clearly visible floating in "
    "it. A single clean CYLINDRICAL vertical stream of tea is falling straight "
    "down from the bottle's OPEN MOUTH into the center of the glass — the stream "
    "is obviously coming from the bottle's neck opening, not from the side or "
    "body of the bottle. The stream is a thin, clean, photorealistic column of "
    "golden liquid."
)

PROMPT_VIDEO = (
    "A smooth cinematic 10-second product pour. The camera stays perfectly locked "
    "— no zoom, no shake, no movement. The Lipton Ice Tea bottle slowly tilts and "
    "pours a continuous stream of tea into the glass of ice. During the first 5 "
    "seconds the tea pouring is dark amber; during the second 5 seconds the tea "
    "visibly lightens to a translucent golden color as it continues to fill the "
    "glass, creating two stacked layers (dark bottom, golden top). The pour is "
    "slow, elegant, and continuous. End frame matches the reference last-frame "
    "image exactly. No camera movement, no text, no people, no hands, seamless "
    "cinematic grade, photorealistic."
)


# --- Gemini image generation ------------------------------------------------


def imagen_generate(prompt: str, out_path: Path) -> None:
    """Generate a 16:9 image with Imagen 4 and save to disk."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=GEMINI_API_KEY)
    print(f"  [imagen4] generating -> {out_path.name}")
    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="16:9",
        ),
    )
    if not response.generated_images:
        raise RuntimeError(f"Imagen returned nothing: {response}")
    png_bytes = response.generated_images[0].image.image_bytes
    with open(out_path, "wb") as f:
        f.write(png_bytes)
    print(f"  [imagen4] saved {out_path} ({out_path.stat().st_size // 1024} KB)")


def flash_edit_to_16x9(prompt: str, reference: Path, out_path: Path, target_size: tuple[int, int]) -> None:
    """Generate via Gemini 2.5 Flash Image edit (square output), then center-crop
    + resize to match the reference's 16:9 dimensions."""
    from google import genai
    from PIL import Image as PILImage

    client = genai.Client(api_key=GEMINI_API_KEY)
    ref_img = PILImage.open(reference)

    print(f"  [flash-edit] generating -> {out_path.name}")
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt, ref_img],
    )
    raw_bytes = None
    for cand in response.candidates or []:
        for part in cand.content.parts or []:
            if getattr(part, "inline_data", None) is not None:
                raw_bytes = part.inline_data.data
                break
        if raw_bytes:
            break
    if raw_bytes is None:
        raise RuntimeError("Flash Image returned no image")

    tmp = out_path.with_suffix(".raw.png")
    with open(tmp, "wb") as f:
        f.write(raw_bytes)

    img = PILImage.open(tmp)
    # Center-crop to 16:9 ratio then resize to target.
    w, h = img.size
    target_w, target_h = target_size
    target_ratio = target_w / target_h
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    img = img.resize(target_size, PILImage.LANCZOS)
    img.save(out_path, format="PNG")
    tmp.unlink(missing_ok=True)
    print(f"  [flash-edit] cropped to {target_size} -> {out_path.stat().st_size // 1024} KB")


# --- Kie.ai Kling video -----------------------------------------------------


def kie_create_task(body: dict) -> str:
    r = requests.post(f"{KIE_BASE}/createTask", headers=KIE_HEADERS, json=body, timeout=60)
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        raise RuntimeError(f"Kie createTask failed: {data}")
    return data["data"]["taskId"]


def kie_poll(task_id: str, label: str, timeout_s: int = 1500) -> dict:
    deadline = time.time() + timeout_s
    last = None
    while time.time() < deadline:
        r = requests.get(
            f"{KIE_BASE}/recordInfo",
            headers=KIE_HEADERS,
            params={"taskId": task_id},
            timeout=30,
        )
        r.raise_for_status()
        data = r.json().get("data", {})
        state = data.get("state")
        if state != last:
            print(f"  [{label}] state={state}")
            last = state
        if state == "success":
            return json.loads(data.get("resultJson") or "{}")
        if state in ("fail", "failed", "error"):
            raise RuntimeError(f"Kie task failed: {data}")
        time.sleep(10)
    raise TimeoutError("Kie task timed out")


def kie_download(url: str, dest: Path) -> None:
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 15):
                f.write(chunk)
    print(f"  saved {dest.name} ({dest.stat().st_size // 1024} KB)")


def upload_to_tempfile(local_path: Path) -> str:
    """Kling wants a URL, not bytes. Upload via Kie's file-stream-upload endpoint."""
    url = "https://kieai.redpandaai.co/api/file-stream-upload"
    with open(local_path, "rb") as f:
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {KIE_API_KEY}"},
            files={"file": (local_path.name, f, "image/png")},
            data={"uploadPath": "images/campaign-landing"},
            timeout=120,
        )
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        raise RuntimeError(f"Upload failed: {data}")
    return data["data"]["downloadUrl"]


# --- ffmpeg frame extraction ------------------------------------------------


def extract_frames(video: Path, out_dir: Path, n_frames: int) -> None:
    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    # Clear prior frames
    for old in list(out_dir.glob("frame_*.jpg")) + list(out_dir.glob("frame_*.webp")):
        old.unlink()

    probe = subprocess.run(
        [ffmpeg, "-i", str(video)],
        capture_output=True,
        text=True,
    )
    duration_s = 10.0
    for line in probe.stderr.splitlines():
        if "Duration:" in line:
            ts = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = ts.split(":")
            duration_s = int(h) * 3600 + int(m) * 60 + float(s)
            break
    print(f"  video duration: {duration_s:.1f}s")

    fps = n_frames / duration_s
    out_pattern = str(out_dir / "frame_%04d.jpg")
    print(f"  extracting {n_frames} frames @ {fps:.1f} fps -> {out_dir.name}/")

    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i", str(video),
            "-vf", f"fps={fps},scale=1600:-2",
            "-q:v", "4",  # jpeg quality 2-5 = high; 4 is a good size/quality balance
            out_pattern,
        ],
        check=True,
        capture_output=True,
    )
    extracted = sorted(out_dir.glob("frame_*.jpg"))
    total_kb = sum(p.stat().st_size for p in extracted) // 1024
    print(f"  extracted {len(extracted)} frames ({total_kb} KB total, avg {total_kb // max(len(extracted),1)} KB/frame)")


# --- Main -------------------------------------------------------------------


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "keyframes"):
        print("\n[1/4] Imagen 4 keyframe A — empty iced glass + bottle tilting (16:9)")
        imagen_generate(PROMPT_A, KEYFRAME_A)

        print("\n[2/4] Imagen 4 keyframe B — full glass, half dark / half gold (16:9)")
        imagen_generate(PROMPT_B, KEYFRAME_B)

    if step in ("all", "video"):
        print("\n[3/4] Upload keyframes to Kie temp storage")
        url_a = upload_to_tempfile(KEYFRAME_A)
        url_b = upload_to_tempfile(KEYFRAME_B)
        print(f"  A: {url_a}")
        print(f"  B: {url_b}")

        print("\n[3/4] Kling 3.0 pro — 10s image-to-video")
        task_v = kie_create_task(
            {
                "model": "kling-3.0/video",
                "input": {
                    "prompt": PROMPT_VIDEO,
                    "image_urls": [url_a, url_b],
                    "duration": "10",
                    "aspect_ratio": "16:9",
                    "mode": "pro",
                    "multi_shots": False,
                    "sound": False,
                },
            }
        )
        print(f"  task {task_v}")
        result = kie_poll(task_v, "kling video")
        video_url = result["resultUrls"][0]
        print(f"  video URL: {video_url}")
        kie_download(video_url, HERO_MP4)

    if step in ("all", "frames"):
        print("\n[4/4] Extract scroll frames with ffmpeg")
        extract_frames(HERO_MP4, FRAMES_DIR, FRAME_COUNT)

    print("\nDONE.")
    print(f"  keyframes: {KEYFRAME_A.name}, {KEYFRAME_B.name}")
    print(f"  video:     {HERO_MP4.name}")
    print(f"  frames:    {FRAMES_DIR} ({FRAME_COUNT} × .webp)")
    print("\nNext: wire <section data-frame-sequence> into index.html.")


if __name__ == "__main__":
    main()
