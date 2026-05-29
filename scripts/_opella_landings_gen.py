"""Generate 2 Opella scroll-driven landings (Buscopan + Doliprane).

Stages:
  1. Generate hero keyframe A + B per campaign  (gpt_image_2)
  2. Generate hero loop video A -> B per campaign  (seedance_2_0, 8s, 16:9, 720p)
  3. Extract 150 frames per mp4  (imageio_ffmpeg)
  4. Generate 4 execution images per campaign  (gpt_image_2)

Manifest persisted at output/landings/_opella_manifest.json so the script can
resume after a failure without re-billing.

Each Higgsfield call uses ``--wait`` so the CLI blocks until the job finishes
and prints the URL. We launch independent jobs as parallel subprocesses.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
HF = r"C:\Users\gmunoz02\node\node-v20.20.0-win-x64\node_modules\@higgsfield\cli\vendor\hf.exe"
LANDINGS_DIR = ROOT / "output" / "landings"
MANIFEST_PATH = LANDINGS_DIR / "_opella_manifest.json"
LANDINGS_DIR.mkdir(parents=True, exist_ok=True)


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def save_manifest(m: dict) -> None:
    MANIFEST_PATH.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------
# CAMPAIGNS
# ---------------------------------------------------------------------

BUSCOPAN_KEYFRAME_A_PROMPT = (
    "Cinematic photograph, 16:9, dim Dubai apartment at 11:47 pm. "
    "A hand holds a smartphone in the lower-right of the frame, screen lit up "
    "and clearly readable, showing a clean minimal pharmacy delivery app interface "
    "WITH ALL TEXT IN ENGLISH (this is critical — no Spanish, no Arabic, no other "
    "languages anywhere on the screen). The UI shows: a top headline reading "
    "'Order confirmed', a product line 'Buscopan 10mg x 1', a price '12 AED', "
    "an 'ETA 28 min' line with a small map preview, a progress bar with four steps "
    "labeled 'Confirmed', 'Preparing', 'On the way', 'Delivered', and a single warm "
    "green call-to-action button at the bottom that reads 'Track order'. The phone "
    "screen is razor-sharp, white background, dark text, no logos other than a "
    "subtle '+' pharmacy cross icon. The rest of the room is soft creamy bokeh — "
    "warm amber lamplight, blurred lights of Burj Khalifa and Dubai Marina through "
    "a floor-to-ceiling window. No people visible other than the hand. Sharp "
    "foreground UI, dreamy night-time background. ENGLISH UI ONLY."
)

BUSCOPAN_KEYFRAME_B_PROMPT = (
    "Cinematic photograph, 16:9, same dim Dubai apartment at 00:14 am, half an "
    "hour later. The smartphone now rests face-down on a marble kitchen counter "
    "in the mid-ground. The main subject is the entry doormat just inside the "
    "front door, on which a small white branded paper delivery bag sits with a "
    "single Buscopan blister pack visible on top — pale yellow box, white pills. "
    "Warm amber lamplight pooling from a floor lamp, blurry Dubai skyline through "
    "the window in deep background. Intimate, quiet, no people. Soft shadows, "
    "shallow depth of field on the doormat. No logos other than Buscopan."
)

BUSCOPAN_HERO_VIDEO_PROMPT = (
    "Cinematic slow camera move over 8 seconds. The shot begins on a smartphone "
    "screen in a dim Dubai apartment at 11:47 pm showing a confirmed pharmacy "
    "delivery order, then the camera slowly pulls back and drifts laterally toward "
    "the apartment's front door. We land on the same apartment moments later at "
    "00:14 am, the package now resting on the doormat with a single Buscopan "
    "blister visible. Warm amber lamplight throughout, blurred Dubai skyline lights "
    "through the window, no people, no on-screen text changes mid-clip, no logos "
    "other than the Buscopan blister at the end. 16:9, 720p, cinematic, smooth."
)

BUSCOPAN_EXECUTIONS = [
    {
        "slug": "exec_1_pharmacy_shelf",
        "prompt": (
            "Photograph, 4:3, of a UAE pharmacy shelf at night with all internal lights off "
            "except a soft cool-white LED strip. Among rows of OTC packaging, one row of "
            "Buscopan boxes is illuminated by a single mobile-phone flashlight beam coming "
            "from off-camera. Tagline 'PHARMACY CLOSED. RELIEF ISN'T.' rendered as a small "
            "discreet vinyl sticker on the bottom of the shelf in a clean sans-serif. "
            "Photoreal, moody, professional brand photography."
        ),
    },
    {
        "slug": "exec_2_rider_dubai_night",
        "prompt": (
            "Photograph, 4:3, of a quick-commerce motorbike rider seen from behind on a "
            "Dubai night street (Sheikh Zayed Road skyline blurred in background, neon "
            "reflections on wet asphalt). The rider has a small white insulated delivery "
            "bag on the back rack with a tiny pharmacy cross icon. Long-exposure tail lights, "
            "warm amber and cool blue palette. Photoreal, cinematic, no visible Talabat/"
            "Careem/Noon logos."
        ),
    },
    {
        "slug": "exec_3_app_card",
        "prompt": (
            "Mobile app card UI mockup, 1:1, displayed inside a phone frame on a dark counter. "
            "The card header reads 'Late-night relief, 30 min'. Below it sits a clean "
            "product photo of a Buscopan blister with a small price '12 AED' and a warm-orange "
            "'Order' button. Soft warm photographic background of a Dubai apartment kitchen, "
            "blurry. Clean modern typography, no real app branding."
        ),
    },
    {
        "slug": "exec_4_blister_macro",
        "prompt": (
            "Macro product photograph, 1:1, of a Buscopan blister pack laying on a white "
            "branded paper delivery envelope on a wooden table. A single pill has been "
            "pushed half-way through the foil. Soft natural morning light from a window "
            "frame visible off-camera. Photoreal, premium pharmaceutical brand photography, "
            "pale yellow box clearly readable, no other text in frame."
        ),
    },
    {
        "slug": "exec_5_telehealth_chat",
        "prompt": (
            "Photograph, 4:3, of a smartphone held in a hand at 23:34 (visible in the "
            "status bar) showing a clean telehealth chat interface IN ENGLISH ONLY (no "
            "other languages). The chat shows three messages: a pharmacist avatar "
            "saying 'Symptoms longer than 24h? I can help.', a green chip below reading "
            "'Buscopan ordered · arriving 28 min', and a button at the bottom 'Talk to "
            "a pharmacist'. Dim Dubai apartment background, blurry warm lights. Photoreal, "
            "intimate, no real chat app branding."
        ),
    },
    {
        "slug": "exec_6_metro_dooh",
        "prompt": (
            "Photograph, 4:3, of a Dubai Metro station platform at 00:14 am, nearly "
            "empty. A vertical 9:16 digital billboard mounted on the platform wall shows "
            "the tagline 'PHARMACY CLOSED. WE'RE NOT.' set in clean white sans-serif on "
            "a deep green background, with a small Opella wordmark and a Buscopan blister "
            "icon below. Cool blue station lights, long-exposure motion trails of a "
            "departing metro. Photoreal, cinematic OOH photography, no other readable "
            "ads or logos in frame. All text in English."
        ),
    },
]

DOLIPRANE_KEYFRAME_A_PROMPT = (
    "Cinematic photograph, 16:9, of the facade of a classic Parisian pharmacy at "
    "golden-hour dusk. The illuminated green-neon cross sign and the word 'PHARMACIE' "
    "in stately serif letters above the doorway. Cobblestone street, warm amber-orange "
    "sky reflected in the windows. In the front window display, neatly arranged behind "
    "the glass, a single yellow-orange Doliprane box is clearly visible and centered. "
    "A few faintly blurred pedestrians on the sidewalk. Photoreal, warm filmic color "
    "grade, no people in sharp focus, no other readable branding."
)

DOLIPRANE_KEYFRAME_B_PROMPT = (
    "Cinematic photograph, 16:9, of a modern minimalist Dubai apartment kitchen at "
    "the exact same golden-hour evening. A marble counter holds the same yellow-orange "
    "Doliprane box next to a tall glass of water. Floor-to-ceiling window behind reveals "
    "the Burj Khalifa silhouette and the warm desert sunset over Dubai Marina. Soft "
    "warm light wrapping the counter, no people visible. Photoreal, warm filmic color "
    "grade matching a classic Parisian dusk, no other brand logos in frame."
)

DOLIPRANE_HERO_VIDEO_PROMPT = (
    "Cinematic 8-second seamless dissolve. The shot opens on a classic Parisian pharmacy "
    "facade at golden-hour dusk, the Doliprane box centered in the lit window display. "
    "Over 8 seconds the Paris street scene slowly dissolves and morphs into a modern "
    "Dubai apartment kitchen at the same golden-hour evening — the Doliprane box remains "
    "anchored visually in the center, finally resting on a marble counter beside a glass "
    "of water with the Burj Khalifa skyline outside. Warm consistent filmic palette "
    "throughout. 16:9, 720p, cinematic, no people, no other readable logos."
)

DOLIPRANE_EXECUTIONS = [
    {
        "slug": "exec_1_diaspora_kitchen",
        "prompt": (
            "Photograph, 4:3, looking down at a kitchen drawer in a Dubai apartment. "
            "Inside the drawer, neatly arranged: a Doliprane box, a French passport, "
            "an Air France boarding pass stub, and a folded note in French handwriting. "
            "Warm overhead light, marble counter visible around the drawer. The visual "
            "speaks of a French expat who imports Doliprane from Paris by hand. Photoreal, "
            "magazine editorial style."
        ),
    },
    {
        "slug": "exec_2_search_map",
        "prompt": (
            "Editorial infographic illustration, 4:3, of a stylized Middle East and North "
            "Africa map in warm sandy tones, with small clusters of search-trend dots glowing "
            "in five cities: Beirut, Tunis, Casablanca, Algiers, and Dubai. The dots are "
            "labeled in tiny clean type ('+62%', '+48%', '+44%', '+39%', '+34%') for "
            "search interest in the word 'Doliprane'. The headline 'WHERE THE WORD STILL "
            "MEANS PARACETAMOL' set in a refined sans-serif. Premium editorial, soft warm "
            "background, no real flag or political markings."
        ),
    },
    {
        "slug": "exec_3_pharmacy_uae_shelf",
        "prompt": (
            "Photograph, 1:1, of a row of OTC paracetamol packages on a UAE pharmacy shelf "
            "in daylight. In the row, a single yellow-orange Doliprane box has been placed "
            "between local generic brands; a small handwritten paper price tag reads "
            "'Now in UAE'. Clean and bright pharmacy lighting, professional retail "
            "photography, photoreal, no other readable brand text."
        ),
    },
    {
        "slug": "exec_4_amazon_pdp",
        "prompt": (
            "Mockup of a clean e-commerce product detail page on a laptop screen, 1:1. "
            "The product image is a Doliprane box, the title reads 'Doliprane 1000mg — "
            "now available on Amazon.ae'. Star rating 4.9, price 18 AED, a small French "
            "flag emoji next to a 'Imported from France' badge. Modern minimalist e-commerce "
            "UI, no real Amazon branding visible. Soft photographic background of a desk "
            "with a coffee mug, blurry."
        ),
    },
    {
        "slug": "exec_5_generational_handoff",
        "prompt": (
            "Photograph, 4:3, intimate domestic scene in a warmly-lit Lebanese-style "
            "kitchen at golden hour. A grandmother's lined hand passes a yellow-orange "
            "Doliprane box across a wooden table to a teenager's hand — both hands "
            "visible, no faces. Marble counter, a small glass of water, soft natural "
            "light. The composition speaks of a generational ritual being passed on. "
            "Photoreal, editorial documentary style, warm filmic color grade. Doliprane "
            "box clearly readable, no other text in frame."
        ),
    },
    {
        "slug": "exec_6_cdg_airport_billboard",
        "prompt": (
            "Photograph, 4:3, of a luminous departure-gate area inside Charles de Gaulle "
            "airport (CDG) Terminal 2E at dusk. A large horizontal digital billboard "
            "mounted near the boarding gate displays the tagline 'DON'T PACK IT IN YOUR "
            "SUITCASE ANYMORE. IT'S ALREADY IN DUBAI.' set in elegant serif typography "
            "(IN ENGLISH ONLY), with a single yellow-orange Doliprane box centered below "
            "the words and a small Opella wordmark in green. Travelers walking past in "
            "the foreground are blurred motion. Warm gold lighting, modern airport "
            "architecture. Photoreal, sophisticated OOH photography. All visible "
            "billboard copy is English."
        ),
    },
]

CAMPAIGNS = [
    {
        "name": "buscopan",
        "dir": LANDINGS_DIR / "landing_opella_buscopan",
        "keyframe_a_prompt": BUSCOPAN_KEYFRAME_A_PROMPT,
        "keyframe_b_prompt": BUSCOPAN_KEYFRAME_B_PROMPT,
        "hero_prompt": BUSCOPAN_HERO_VIDEO_PROMPT,
        "executions": BUSCOPAN_EXECUTIONS,
    },
    {
        "name": "doliprane",
        "dir": LANDINGS_DIR / "landing_opella_doliprane",
        "keyframe_a_prompt": DOLIPRANE_KEYFRAME_A_PROMPT,
        "keyframe_b_prompt": DOLIPRANE_KEYFRAME_B_PROMPT,
        "hero_prompt": DOLIPRANE_HERO_VIDEO_PROMPT,
        "executions": DOLIPRANE_EXECUTIONS,
    },
]


# ---------------------------------------------------------------------
# Higgsfield helpers
# ---------------------------------------------------------------------

def _hf_run(args: list[str], label: str) -> dict:
    """Run hf.exe and return the parsed JSON job result (first job)."""
    print(f"  [hf] {label}: starting...")
    cmd = [HF] + args + ["--wait", "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        print(f"  [hf] {label}: FAILED")
        print(proc.stdout[-500:])
        print(proc.stderr[-500:])
        raise RuntimeError(f"hf.exe failed for {label}")
    raw = proc.stdout.strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Some hf builds emit one JSON object per line; take last.
        last = [l for l in raw.splitlines() if l.strip().startswith("{") or l.strip().startswith("[")]
        data = json.loads(last[-1]) if last else {}
    job = data[0] if isinstance(data, list) and data else data
    print(f"  [hf] {label}: done.")
    return job


def _job_media_url(job: dict) -> str | None:
    """Best-effort extraction of the result URL from a job object."""
    for key in ("media_url", "result_url", "output_url", "url"):
        v = job.get(key)
        if isinstance(v, str) and v.startswith("http"):
            return v
    results = job.get("results") or job.get("outputs") or []
    if isinstance(results, list):
        for r in results:
            if isinstance(r, dict):
                u = r.get("url") or r.get("media_url") or r.get("output_url")
                if isinstance(u, str) and u.startswith("http"):
                    return u
    raw = json.dumps(job)
    m = re.search(r"https?://[^\s\"']+\.(?:png|jpg|jpeg|webp|mp4)", raw)
    return m.group(0) if m else None


def _download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=180)
    r.raise_for_status()
    dest.write_bytes(r.content)
    print(f"  [dl] {dest.name}: {len(r.content) // 1024} KB")


def generate_image(prompt: str, dest: Path, aspect: str = "16:9", label: str = "img",
                   reference: Path | None = None) -> str:
    # Note: --image at 2k resolution upload often returns a stale-URL error from
    # Higgsfield. We skip the reference and rely on prompt-driven coherence.
    args = ["generate", "create", "gpt_image_2", "--prompt", prompt,
            "--aspect_ratio", aspect, "--resolution", "2k", "--quality", "high"]
    job = _hf_run(args, label)
    url = _job_media_url(job)
    if not url:
        raise RuntimeError(f"No URL in job for {label}")
    _download(url, dest)
    return url


def generate_hero_video(prompt: str, start_image: Path, end_image: Path,
                         dest: Path, label: str = "video") -> str:
    args = ["generate", "create", "seedance_2_0",
            "--prompt", prompt,
            "--start-image", str(start_image),
            "--end-image", str(end_image),
            "--duration", "5",
            "--aspect_ratio", "16:9",
            "--resolution", "720p"]
    job = _hf_run(args, label)
    url = _job_media_url(job)
    if not url:
        raise RuntimeError(f"No URL in job for {label}")
    _download(url, dest)
    return url


def extract_frames(mp4_path: Path, frames_dir: Path, n_frames: int = 150) -> None:
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    frames_dir.mkdir(parents=True, exist_ok=True)
    # First, get duration to compute fps for n_frames
    probe = subprocess.run([ffmpeg, "-i", str(mp4_path)], capture_output=True, text=True, encoding="utf-8")
    stderr = probe.stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", stderr)
    duration = 5.0
    if m:
        duration = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    fps = n_frames / duration
    out = frames_dir / "frame_%04d.jpg"
    cmd = [ffmpeg, "-y", "-i", str(mp4_path), "-vf", f"fps={fps:.4f}",
           "-vframes", str(n_frames), "-q:v", "3", str(out)]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"  [ffmpeg] extracted {n_frames} frames from {mp4_path.name} at {fps:.2f}fps")


# ---------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------

def run_campaign(campaign: dict, manifest: dict) -> None:
    name = campaign["name"]
    print(f"\n=== {name.upper()} ===")
    campaign_dir = campaign["dir"]
    assets = campaign_dir / "assets"
    assets.mkdir(parents=True, exist_ok=True)

    mfk = manifest.setdefault(name, {})

    # --- 1. Keyframes (sequential within a campaign since B refs A) ---
    kfa = assets / "hero-keyframe-a.png"
    kfb = assets / "hero-keyframe-b.png"
    if not kfa.exists():
        mfk["keyframe_a_url"] = generate_image(
            campaign["keyframe_a_prompt"], kfa, label=f"{name} keyframe A")
        save_manifest(manifest)
    if not kfb.exists():
        mfk["keyframe_b_url"] = generate_image(
            campaign["keyframe_b_prompt"], kfb, label=f"{name} keyframe B",
            reference=kfa)
        save_manifest(manifest)

    # --- 2. Hero video ---
    mp4 = assets / "hero-loop.mp4"
    if not mp4.exists():
        mfk["hero_video_url"] = generate_hero_video(
            campaign["hero_prompt"], kfa, kfb, mp4, label=f"{name} hero video")
        save_manifest(manifest)

    # --- 3. Frame extraction ---
    frames_dir = assets / "frames"
    if not frames_dir.exists() or len(list(frames_dir.glob("frame_*.jpg"))) < 100:
        extract_frames(mp4, frames_dir, n_frames=150)

    # --- 4. Executions (parallel) ---
    executions_dir = assets / "executions"
    executions_dir.mkdir(parents=True, exist_ok=True)
    pending = []
    for ex in campaign["executions"]:
        path = executions_dir / f"{ex['slug']}.jpg"
        if not path.exists():
            pending.append((ex, path))
    if pending:
        def _gen_exec(item):
            ex, path = item
            url = generate_image(ex["prompt"], path, aspect="4:3",
                                  label=f"{name} {ex['slug']}")
            return ex["slug"], url
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(_gen_exec, pending))
        mfk.setdefault("executions", {})
        for slug, url in results:
            mfk["executions"][slug] = url
        save_manifest(manifest)

    print(f"=== {name.upper()} done ===")


def main() -> None:
    manifest = load_manifest()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for campaign in CAMPAIGNS:
        if only and campaign["name"] != only:
            continue
        run_campaign(campaign, manifest)
    print("\nAll done. Manifest:", MANIFEST_PATH)


if __name__ == "__main__":
    main()
