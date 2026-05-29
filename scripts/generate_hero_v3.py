"""Exploded-blueprint hero for landing_lipton_v2.

Animation concept ("Option A"):
  Phase 1 (frames 0-75):   whole Lipton bottle  -> exploded into components
                           (cap, label, liquid, tea leaves, sugar crystals,
                            water drops, ice cubes) floating with thin blueprint labels.
  Phase 2 (frames 75-150): exploded  -> bottle reassembles, BUT the sugar
                           crystals returning are visibly HALF as many as
                           before — the other half stays suspended in frame.

Pipeline:
  1. Imagen 4     -> keyframe A (whole bottle on blueprint bg, 16:9)
  2. Flash edit   -> keyframe B (same composition, fully exploded blueprint)
  3. Flash edit   -> keyframe C (same composition, reassembled with half sugar)
  4. Kling 3.0 pro 5s   -> video_1 (A -> B)
  5. Kling 3.0 pro 5s   -> video_2 (B -> C)
  6. ffmpeg concat      -> hero-loop.mp4 (10s total, 150 frames extracted)

Cost: ~$0.12 Imagen/Flash + 2 * ~$0.90 Kling = ~$1.92.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from io import BytesIO
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
KIE_API_KEY = os.environ["KIE_API_KEY"]

OUT = Path("output/landing_lipton_v2/assets")
OUT.mkdir(parents=True, exist_ok=True)
FRAMES_DIR = OUT / "frames"
FRAMES_DIR.mkdir(parents=True, exist_ok=True)

KF_A = OUT / "hero-kf-a-whole.png"
KF_B = OUT / "hero-kf-b-exploded.png"
KF_C = OUT / "hero-kf-c-halfsugar.png"
VIDEO_1 = OUT / "hero-part1.mp4"
VIDEO_2 = OUT / "hero-part2.mp4"
HERO_MP4 = OUT / "hero-loop.mp4"
FRAME_COUNT = 150

KIE_BASE = "https://api.kie.ai/api/v1/jobs"
KIE_HEADERS = {"Authorization": f"Bearer {KIE_API_KEY}", "Content-Type": "application/json"}
KIE_UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"

# ============================================================================
# Prompts
# ============================================================================

_SHARED_SCENE = (
    "Cinematic ultra-realistic editorial product photograph in the style of a "
    "high-end Apple or Dyson product reveal, wide 16:9 horizontal composition, "
    "2K quality. Background: a deep moody near-black studio void with a very "
    "subtle warm amber radial glow behind the subject like distant sunlight. "
    "The lighting is dramatic and directional, with strong rim-light tracing the "
    "edges of every object. The overall color grade is sophisticated and "
    "editorial: deep blacks, golden amber highlights, accents of Lipton yellow "
    "(#FFD100) and Lipton red (#E30613). No people, no hands, no shadows on the "
    "ground, no text overlays, no watermarks, no additional brand logos other "
    "than Lipton."
)

PROMPT_A_WHOLE = (
    _SHARED_SCENE
    + " Subject of this image: a single real Lipton Ice Tea bottle standing "
    "perfectly vertical and centered in the frame. The iconic yellow Lipton "
    "label with the red Lipton shield logo faces the camera directly, fully "
    "legible. The bottle is filled with rich amber iced tea. The cap is on. "
    "Thin elegant white blueprint guide lines (like technical schematic marks) "
    "subtly intersect the bottle at cap, neck, shoulder, mid-body and base — "
    "suggesting this is a technical product reveal about to begin. The "
    "background is a seamless deep matte black studio void fading to warm amber "
    "only at the extreme corners. Sharp, premium, editorial."
)

PROMPT_B_EXPLODED = (
    "Keep the same scene, same camera framing, same dark studio background, "
    "same lighting, same 16:9 composition as the reference image. The Lipton "
    "bottle has now FULLY DISASSEMBLED into its individual components floating "
    "in mid-air in an exploded-view technical illustration arrangement, spread "
    "radially around the center of the frame. Visible floating components, each "
    "clearly separated from the others and suspended in space: (1) the yellow "
    "plastic cap floating top-left, (2) the yellow Lipton label peeling off and "
    "floating upper-right, (3) the clear empty bottle body floating center, (4) "
    "a cluster of real tea leaves floating left, (5) a cluster of pure white-"
    "golden sugar crystals floating right like tiny diamonds catching light, (6) "
    "droplets of pure water floating bottom-left, (7) a few crystal-clear ice "
    "cubes floating bottom-right. Thin elegant white blueprint lines connect "
    "some of the components to the empty bottle body. The overall look is an "
    "Apple Keynote exploded-view product render, editorial, sophisticated. The "
    "bottle itself is now transparent/empty — the tea has fully broken into its "
    "ingredients. Keep the background and lighting identical to the reference."
)

PROMPT_C_HALFSUGAR = (
    "Keep the same scene, same camera framing, same dark studio background, "
    "same lighting, same 16:9 composition as the reference image. The components "
    "are RECOMPOSING back into a full Lipton bottle in the center of the frame. "
    "The bottle is 85% reassembled: yellow cap back on top, yellow Lipton label "
    "back on the body facing the camera legibly, and the bottle is filling with "
    "amber iced tea from the top. HOWEVER, only HALF of the sugar crystals are "
    "returning to the bottle — a small cluster of golden-white sugar crystals "
    "visibly flows INTO the bottle from above, while an equally-sized cluster "
    "of sugar crystals remains SUSPENDED and FROZEN in mid-air to the right of "
    "the bottle, glowing softly, clearly NOT going back in. The suspended sugar "
    "cluster looks like a deliberate sculpture of what was removed. A thin "
    "elegant white blueprint line connects the suspended sugar cluster to a "
    "subtle label area (empty — no text). Everything else reassembles normally: "
    "tea leaves merging back into the liquid, water and ice combining. Keep the "
    "background and lighting identical to the reference."
)

PROMPT_V1 = (
    "A smooth cinematic 5-second product-reveal animation. The camera stays "
    "completely locked and static — no zoom, no pan, no shake. The Lipton Ice "
    "Tea bottle in the center of the frame gradually DISASSEMBLES into its "
    "floating components in a clean exploded-view technical-illustration style: "
    "the cap floats upward, the yellow label peels off and drifts to the upper "
    "right, the liquid inside the bottle separates into visible tea leaves "
    "floating left, sugar crystals floating right, water droplets and ice cubes "
    "scattering outward. By the end of the 5 seconds the bottle has fully "
    "exploded into its parts, suspended in mid-air, matching the reference "
    "last-frame image exactly. No text, no people, no hands, no shadows. "
    "Editorial Apple-keynote style product reveal, moody dark studio background "
    "with warm amber highlights. Seamless slow deliberate motion, no camera "
    "movement at all."
)

PROMPT_V2 = (
    "A smooth cinematic 5-second product-reveal animation. The camera stays "
    "completely locked and static — no zoom, no pan, no shake. The floating "
    "exploded components of the Lipton Ice Tea bottle gradually REASSEMBLE back "
    "into a full bottle in the center of the frame: the cap floats down on top, "
    "the yellow label wraps back around the body, the tea leaves and water "
    "combine into amber iced tea filling the bottle. HOWEVER, only HALF of the "
    "sugar crystals return to the bottle — a cluster of sugar visibly flows "
    "into the bottle from above while an equal-sized cluster stays suspended "
    "in mid-air to the right of the bottle, glowing softly, NOT going back in. "
    "By the end of the 5 seconds the scene matches the reference last-frame "
    "image exactly: 85%-reassembled bottle in the center, suspended sugar "
    "cluster floating to its right. No text, no people, no hands, no shadows. "
    "Editorial product reveal style, moody dark studio background. Seamless "
    "slow deliberate motion, no camera movement at all."
)

# ============================================================================
# Helpers
# ============================================================================


def imagen_generate(prompt: str, out_path: Path) -> None:
    from google import genai
    from google.genai import types

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
    with open(out_path, "wb") as f:
        f.write(png_bytes)
    print(f"  [imagen4] saved {out_path} ({out_path.stat().st_size // 1024} KB)")


def flash_edit(prompt: str, reference: Path, out_path: Path, target_size: tuple[int, int]) -> None:
    """Gemini 2.5 Flash Image edit, then crop/resize to match target 16:9 size."""
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

    img = PILImage.open(BytesIO(raw_bytes))
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
    img.save(out_path, format="PNG")
    print(f"  [flash-edit] cropped to {target_size} -> {out_path.stat().st_size // 1024} KB")


def kie_upload(local_path: Path) -> str:
    with open(local_path, "rb") as f:
        r = requests.post(
            KIE_UPLOAD,
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


def kling_image_to_video(url_start: str, url_end: str, prompt: str, label: str, out: Path) -> None:
    task = kie_create_task(
        {
            "model": "kling-3.0/video",
            "input": {
                "prompt": prompt,
                "image_urls": [url_start, url_end],
                "duration": "5",
                "aspect_ratio": "16:9",
                "mode": "pro",
                "multi_shots": False,
                "sound": False,
            },
        }
    )
    print(f"  task {task}")
    result = kie_poll(task, label)
    kie_download(result["resultUrls"][0], out)


def concat_videos(v1: Path, v2: Path, out: Path) -> None:
    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    listfile = OUT / "_concat.txt"
    listfile.write_text(f"file '{v1.resolve()}'\nfile '{v2.resolve()}'\n")
    print(f"  concatenating {v1.name} + {v2.name} -> {out.name}")
    subprocess.run(
        [ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", str(listfile), "-c", "copy", str(out)],
        check=True,
        capture_output=True,
    )
    listfile.unlink(missing_ok=True)
    print(f"  saved {out.name} ({out.stat().st_size // 1024} KB)")


def extract_frames(video: Path, out_dir: Path, n_frames: int) -> None:
    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    for old in list(out_dir.glob("frame_*.jpg")) + list(out_dir.glob("frame_*.webp")):
        old.unlink()

    probe = subprocess.run([ffmpeg, "-i", str(video)], capture_output=True, text=True)
    duration_s = 10.0
    for line in probe.stderr.splitlines():
        if "Duration:" in line:
            ts = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = ts.split(":")
            duration_s = int(h) * 3600 + int(m) * 60 + float(s)
            break
    print(f"  video duration: {duration_s:.1f}s")

    fps = n_frames / duration_s
    print(f"  extracting {n_frames} frames @ {fps:.1f} fps")
    subprocess.run(
        [
            ffmpeg, "-y", "-i", str(video),
            "-vf", f"fps={fps},scale=1600:-2",
            "-q:v", "4",
            str(out_dir / "frame_%04d.jpg"),
        ],
        check=True,
        capture_output=True,
    )
    extracted = sorted(out_dir.glob("frame_*.jpg"))
    total_kb = sum(p.stat().st_size for p in extracted) // 1024
    print(f"  extracted {len(extracted)} frames ({total_kb} KB total)")


# ============================================================================
# Main
# ============================================================================


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"
    from PIL import Image as PILImage

    if step in ("all", "keyframes"):
        print("\n[1/6] Imagen 4 — keyframe A (whole bottle)")
        imagen_generate(PROMPT_A_WHOLE, KF_A)

        target_size = PILImage.open(KF_A).size
        print(f"  target size: {target_size}")

        print("\n[2/6] Flash edit — keyframe B (exploded)")
        flash_edit(PROMPT_B_EXPLODED, KF_A, KF_B, target_size)

        print("\n[3/6] Flash edit — keyframe C (reassembled half-sugar)")
        flash_edit(PROMPT_C_HALFSUGAR, KF_A, KF_C, target_size)

    if step in ("all", "videos"):
        print("\n[4/6] Upload 3 keyframes to Kie")
        url_a = kie_upload(KF_A)
        url_b = kie_upload(KF_B)
        url_c = kie_upload(KF_C)
        print(f"  A: {url_a}\n  B: {url_b}\n  C: {url_c}")

        print("\n[5/6] Kling 3.0 pro — video 1 (A -> B, 5s)")
        kling_image_to_video(url_a, url_b, PROMPT_V1, "video 1", VIDEO_1)

        print("\n[5/6] Kling 3.0 pro — video 2 (B -> C, 5s)")
        kling_image_to_video(url_b, url_c, PROMPT_V2, "video 2", VIDEO_2)

    if step in ("all", "concat"):
        print("\n[6/6] Concat + extract frames")
        concat_videos(VIDEO_1, VIDEO_2, HERO_MP4)
        extract_frames(HERO_MP4, FRAMES_DIR, FRAME_COUNT)

    print("\nDONE")


if __name__ == "__main__":
    main()
