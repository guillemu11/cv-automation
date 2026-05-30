# Setting up the repo on Paula's machine

Goal: reproduce the working setup **exactly as it is on Guille's machine**. The code
lives on GitHub (private), but a lot of the value is **not** in git — it's
gitignored: the deliverables under `output/`, the API keys in `.env`, Paula's source
CV, and the master plan doc. So setup = **clone the code, then drop in the ignored
extras**.

These are developer/setup steps (Guille runs them once). Paula never needs a terminal
afterwards — she uses the dashboard.

## What you need to move by hand

The clone gives you all tracked code. From Guille's machine you also carry over the
gitignored extras, bundled into one archive:

```
paula_repo_extras.tgz   →  contains:  .env  ·  output/  ·  Paula_De_Francisco_CV_Dubai.pdf  ·  Plan_Sistema_Busqueda_Empleo_Dubai.md
```

⚠️ This archive contains **real API keys** (`.env`). Move it over a trusted channel
(USB stick or a private cloud folder) — not email, not a public link.

## Prerequisites on Paula's machine

- **Git** — https://git-scm.com
- **Python 3.12** — https://www.python.org (tick "Add to PATH")
- **Node 20+** (only if she'll deploy landings / use vercel) — https://nodejs.org
- **The `paula_repo_extras.tgz` archive already copied onto the machine** (USB / private
  cloud). Nothing can fetch it for you — carry it over by hand before step 2.

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

### 2. Drop in the gitignored extras

Copy `paula_repo_extras.tgz` into the repo root, then unpack it (it expands into
`.env`, `output/`, and the two root files, exactly where they belong):

```powershell
# from inside CV_Automation\
tar -xzf paula_repo_extras.tgz
Remove-Item paula_repo_extras.tgz
```

`tar` ships with Windows 10/11. If for some reason it's missing, 7-Zip opens `.tgz`
too (extract here, twice — once for gzip, once for tar).

### 3. Recreate the Python environment

The virtualenv is machine-specific and is **not** transferred — rebuild it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium      # for PDF/deck rendering + autofill
```

`scripts/setup_paula.ps1` does steps 3 for you in one go (see below).

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
- `output/` is ~294 MB (the landings carry hundreds of frame images — that's normal).

## Keeping it in sync later

Paula's clone is a real git clone, so future changes pull cleanly:

```powershell
git pull
```

The deliverables in `output/` are local-only (gitignored); regenerate them from the
dashboard or carry a fresh `paula_repo_extras.tgz` when there's new work.
