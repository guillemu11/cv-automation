"""Resume the hero pipeline at step 3 using the 2 keyframes already generated.

Re-uses the same URLs that Kie returned in the last run (tempfile.aiquickdraw.com
URLs are short-lived but usually valid for at least 30 minutes).
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

KIE_API_KEY = os.environ["KIE_API_KEY"]
BASE = "https://api.kie.ai/api/v1/jobs"
HEADERS = {"Authorization": f"Bearer {KIE_API_KEY}", "Content-Type": "application/json"}
OUTPUT_DIR = Path("output/landing_lipton/assets")

URL_A = "https://tempfile.aiquickdraw.com/workers/nano/image_1775908125334_ovqvks.png"
URL_B = "https://tempfile.aiquickdraw.com/workers/nano/image_1775908143310_lc6oco.png"

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


def create_task(body: dict) -> str:
    r = requests.post(f"{BASE}/createTask", headers=HEADERS, json=body, timeout=60)
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        raise RuntimeError(f"Kie createTask failed: {data}")
    tid = data["data"]["taskId"]
    print(f"  -> task {tid}")
    return tid


def poll_task(task_id: str, label: str, timeout_s: int = 1200) -> dict:
    deadline = time.time() + timeout_s
    last = None
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
        if state != last:
            print(f"  [{label}] state={state}")
            last = state
        if state == "success":
            return json.loads(data.get("resultJson") or "{}")
        if state in ("fail", "failed", "error"):
            raise RuntimeError(f"Kie task failed: {data}")
        time.sleep(10)
    raise TimeoutError("Kie task timed out")


def download(url: str, dest: Path) -> None:
    print(f"  downloading -> {dest}")
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 15):
                f.write(chunk)
    print(f"  saved {dest.stat().st_size // 1024} KB")


def main() -> None:
    print("resuming at step 3: Kling 3.0 video (A->B)")
    task_v = create_task(
        {
            "model": "kling-3.0/video",
            "input": {
                "prompt": PROMPT_VIDEO,
                "image_urls": [URL_A, URL_B],
                "duration": "8",
                "aspect_ratio": "16:9",
                "mode": "pro",
                "multi_shots": False,
                "sound": False,
            },
        }
    )
    result = poll_task(task_v, "kling video", timeout_s=1500)
    video_url = result["resultUrls"][0]
    print(f"  video URL: {video_url}")
    download(video_url, OUTPUT_DIR / "hero-loop.mp4")
    print("DONE")


if __name__ == "__main__":
    main()
