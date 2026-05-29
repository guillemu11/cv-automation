"""Redeploy a landing folder to its Vercel slot.

Usage:
  python scripts/deploy_landing_slot.py a <landing_folder>
  python scripts/deploy_landing_slot.py b <landing_folder>

Where:
  - "a" / "b" picks the slot (paula-pitch-a / paula-pitch-b)
  - <landing_folder> is the path to the folder containing index.html

Examples:
  # First-time: link a fresh folder to slot A then deploy
  python scripts/deploy_landing_slot.py a output/landings/landing_new_brand

  # Re-deploy the existing buscopan landing (it's already linked to slot A)
  python scripts/deploy_landing_slot.py a output/landings/landing_opella_buscopan

The Vercel project NAME stays the same forever (paula-pitch-a / paula-pitch-b),
which means the production URL stays the same:
  https://paula-pitch-a.vercel.app
  https://paula-pitch-b.vercel.app

Rotation pattern: build a new landing into a new folder, then point it at the
slot you want to overwrite. The previous content is replaced; the URL keeps
working with the new content.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SLOTS = {
    "a": "paula-pitch-a",
    "b": "paula-pitch-b",
}


def run(cmd: list[str], cwd: Path) -> str:
    print(f"  $ {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise SystemExit(f"command failed: {' '.join(cmd)}")
    return proc.stdout


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in SLOTS:
        print(__doc__)
        sys.exit(1)
    slot, folder_arg = sys.argv[1], sys.argv[2]
    project = SLOTS[slot]
    folder = Path(folder_arg).resolve()
    if not (folder / "index.html").exists():
        raise SystemExit(f"No index.html in {folder}")

    print(f"[deploy] slot {slot.upper()} -> project '{project}' from {folder}")

    # Link (idempotent — same project name → re-uses existing link)
    run(["vercel", "link", "--yes", "--project", project], folder)

    # Production deploy
    run(["vercel", "--prod", "--yes"], folder)

    print(f"\n[done] https://{project}.vercel.app")


if __name__ == "__main__":
    main()
