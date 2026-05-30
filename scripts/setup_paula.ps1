# Setup helper for Paula's machine — recreates the Python environment after the
# repo has been cloned and paula_repo_extras.tgz has been unpacked.
#
# Run from the repo root:
#   powershell -ExecutionPolicy Bypass -File scripts\setup_paula.ps1
#
# This is a one-off developer setup step (see docs/SETUP_paula_machine.md). It does
# NOT touch git or the .env/output extras — move those over first.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
Write-Host "Repo root: $root"

# --- Tool checks ---------------------------------------------------------
function Require-Cmd($name, $hint) {
    if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
        Write-Host "MISSING: $name  -> $hint" -ForegroundColor Red
        exit 1
    }
    Write-Host ("OK  {0}: {1}" -f $name, (Get-Command $name).Source)
}
Require-Cmd python "Install Python 3.12 from https://www.python.org (tick Add to PATH)"

# --- Warn if the gitignored extras aren't in place -----------------------
if (-not (Test-Path ".env")) {
    Write-Host "WARNING: .env not found. Unpack paula_repo_extras.tgz first (tar -xzf paula_repo_extras.tgz)." -ForegroundColor Yellow
}
if (-not (Test-Path "output")) {
    Write-Host "WARNING: output/ not found. The deliverables live there; unpack the extras archive." -ForegroundColor Yellow
}

# --- Virtualenv + dependencies ------------------------------------------
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtualenv (.venv)..."
    python -m venv .venv
}
$py = Join-Path $root ".venv\Scripts\python.exe"
Write-Host "Installing requirements..."
& $py -m pip install --upgrade pip
& $py -m pip install -r requirements.txt

# --- Playwright (PDF/deck rendering + autofill) --------------------------
Write-Host "Installing Playwright Chromium..."
& $py -m playwright install chromium

Write-Host ""
Write-Host "Done. Launch the dashboard with:" -ForegroundColor Green
Write-Host "  .\.venv\Scripts\Activate.ps1; python scripts\run_webapp.py"
