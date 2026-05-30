# Setting up the repo on Paula's machine

Goal: reproduce the working setup **exactly as it is on Guille's machine**. Almost
everything now lives in the (private) GitHub repo — code **and** all deliverables
under `output/`, Paula's source CV, and the master plan. The **only** thing not in git
is `.env` (it holds real API keys), so setup = **clone, drop in one `.env` file,
rebuild the Python environment**.

These are developer/setup steps (Guille runs them once). Paula never needs a terminal
afterwards — she uses the dashboard.

## The one file you move by hand: `.env`

`git clone` brings down everything except `.env`. Copy `.env` (≈1.6 KB) from Guille's
repo root to Paula's repo root after cloning.

⚠️ `.env` contains **real API keys**. Move it over a trusted channel (USB stick, a
private message, or a private cloud folder) — **not email, not a public link**. If it
ever travels over a dubious channel, rotate the keys afterwards.

## Prerequisites on Paula's machine

- **Git** — https://git-scm.com
- **Python 3.12** — https://www.python.org (tick "Add to PATH")
- **Node 20+** (only if she'll deploy landings / use vercel) — https://nodejs.org

### 0. GitHub access (the repo is PRIVATE)

`git clone` of a private repo needs an authenticated GitHub account **that has access
to `guillemu11/cv-automation`**. Pick one:

- **Git Credential Manager (simplest):** just run the clone in step 1 — Git for Windows
  pops a browser login. Sign in with an account that can see the repo (e.g. guillemu11).
- **GitHub CLI:** `gh auth login` once, then clone.
- **Collaborator:** add Paula's own GitHub account as a collaborator on the repo
  (GitHub → repo → Settings → Collaborators), then she signs in with hers.

Without this, step 1 fails with "Authentication failed" / "repository not found".

## Steps

### 1. Clone the repo and switch to the latest branch

```powershell
cd $HOME\Desktop
git clone https://github.com/guillemu11/cv-automation.git CV_Automation
cd CV_Automation
git checkout henkel-frizz-forecast-deck   # the branch with all the latest work
```

This already includes `output/` (~294 MB — every deliverable, landing and outreach
pack), so the clone takes a minute. No separate archive to unpack anymore.

### 2. Drop in `.env`

Copy the `.env` file from Guille's repo root into this folder (`CV_Automation\`). That
is the only piece not in git. Verify it's there:

```powershell
Test-Path .env   # must print True
```

### 3. Recreate the Python environment

The virtualenv is machine-specific and is **not** in git — rebuild it. The helper
script does it in one go (creates `.venv`, installs requirements, installs Playwright
Chromium):

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup_paula.ps1
```

Manual equivalent if you prefer:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium      # for PDF/deck rendering + autofill
```

### 4. (Optional) Node tooling for landings

Only if Paula will deploy/refresh Vercel landings:

```powershell
npm i -g vercel
vercel login
```

### 5. Launch the dashboard

```powershell
.\.venv\Scripts\Activate.ps1
python scripts/run_webapp.py
```

Then open the printed URL (default http://127.0.0.1:8062). Every Opella + Henkel
deliverable, outreach pack and landing link is on the job cards.

## Verify it came over "tal cual"

- Dashboard starts and lists jobs.
- Opella + Henkel cards show CV, CL, deliverables, outreach pack, and the
  `paula-pitch-*` links.
- `output/` is present and ~294 MB (the landings carry hundreds of frame images —
  that's normal).

## Keeping it in sync later

Paula's clone is a real git clone, so future changes pull cleanly — and because
`output/` is versioned now, new deliverables arrive with a plain pull:

```powershell
git pull
```

The only thing that never comes through git is `.env`; it only changes if Guille adds
or rotates a key, in which case re-copy it by a trusted channel.
