"""Deploy a static folder to Vercel via the REST API (no Node/CLI needed).

Usage:
    VERCEL_TOKEN=xxx python -m scripts._vercel_deploy "<folder>" [project-name] [--prod]

Uploads every file under <folder>, creates a deployment, polls until READY,
and prints the public URL. Pure stdlib + requests.
"""
from __future__ import annotations

import hashlib
import os
import sys
import time
from pathlib import Path

import requests

API = "https://api.vercel.com"


def _iter_files(root: Path):
    for p in root.rglob("*"):
        if p.is_file() and not p.name.startswith(".") and "qa" not in p.parts:
            yield p


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if not args:
        print("ERROR: pass the folder to deploy")
        return 2
    folder = Path(args[0]).resolve()
    project = args[1] if len(args) > 1 else folder.name.replace("_", "-").lower()
    prod = "--prod" in flags

    token = os.environ.get("VERCEL_TOKEN", "").strip()
    if not token:
        print("ERROR: set VERCEL_TOKEN env var")
        return 2

    headers = {"Authorization": f"Bearer {token}"}

    files_meta = []
    uploaded = 0
    for f in _iter_files(folder):
        data = f.read_bytes()
        sha = hashlib.sha1(data).hexdigest()
        rel = f.relative_to(folder).as_posix()
        # Upload file body
        up = requests.post(
            f"{API}/v2/files",
            headers={**headers, "Content-Type": "application/octet-stream",
                     "x-vercel-digest": sha},
            data=data,
            timeout=120,
        )
        if up.status_code not in (200, 201):
            print(f"UPLOAD FAILED {rel}: {up.status_code} {up.text[:200]}")
            return 1
        files_meta.append({"file": rel, "sha": sha, "size": len(data)})
        uploaded += 1
        print(f"  uploaded {rel} ({len(data)} bytes)")

    print(f"== {uploaded} files uploaded ==")

    body = {
        "name": project,
        "files": files_meta,
        "projectSettings": {"framework": None},
        "target": "production" if prod else None,
    }
    body = {k: v for k, v in body.items() if v is not None}

    dep = requests.post(f"{API}/v13/deployments", headers=headers, json=body, timeout=120)
    if dep.status_code not in (200, 201, 202):
        print(f"DEPLOY CREATE FAILED: {dep.status_code} {dep.text[:400]}")
        return 1
    d = dep.json()
    dep_id = d.get("id")
    url = d.get("url")
    alias = d.get("alias") or []
    print(f"deployment id: {dep_id}")
    print(f"deployment url: https://{url}")

    # Poll until ready
    for _ in range(60):
        st = requests.get(f"{API}/v13/deployments/{dep_id}", headers=headers, timeout=60)
        state = st.json().get("readyState") or st.json().get("status")
        print(f"  state: {state}")
        if state in ("READY", "ERROR", "CANCELED"):
            break
        time.sleep(5)

    print("=== RESULT ===")
    print(f"LIVE: https://{url}")
    for a in alias:
        print(f"ALIAS: https://{a}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
