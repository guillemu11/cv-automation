#!/bin/bash
# Nightly auto-commit + push at 23:00. macOS: launchd
# (~/Library/LaunchAgents/com.cvautomation.autopush.plist). Windows: Task
# Scheduler task "CV_Automation AutoPush" (scripts/install_auto_push_windows.ps1).
# No-op on days with no changes and nothing unpushed. Secrets stay out via .gitignore.
set -u
export PATH="/usr/local/bin:/opt/homebrew/bin:/mingw64/bin:/usr/bin:/bin:$PATH"
export GIT_TERMINAL_PROMPT=0

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 1
mkdir -p logs
LOG="logs/auto_push.log"
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"; }
notify() {
  if command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"$1\" with title \"cv-automation auto-push\"" >/dev/null 2>&1
  elif command -v msg.exe >/dev/null 2>&1; then
    msg.exe "$USERNAME" /TIME:3600 "cv-automation auto-push: $1" >/dev/null 2>&1
  fi
}

# Don't touch the repo mid-merge/rebase.
if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ] || [ -f .git/MERGE_HEAD ]; then
  log "SKIP: merge/rebase in progress"; notify "Saltado: merge/rebase en curso"; exit 0
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

if [ -n "$(git status --porcelain)" ]; then
  # GitHub rejects files >100MB — leave those out and warn.
  git add -A
  BIG="$(git diff --cached --name-only -z | xargs -0 -I{} find {} -type f -size +95M 2>/dev/null)"
  if [ -n "$BIG" ]; then
    echo "$BIG" | while read -r f; do git reset -q -- "$f"; done
    log "WARN: skipped large files: $BIG"; notify "Archivos >95MB no subidos (ver logs/auto_push.log)"
  fi
  if ! git diff --cached --quiet; then
    git commit -q -m "chore(auto): snapshot diario $(date '+%Y-%m-%d')" && log "Committed $(git rev-parse --short HEAD)"
  fi
fi

AHEAD="$(git rev-list --count "origin/$BRANCH..HEAD" 2>/dev/null || echo 1)"
if [ "$AHEAD" = "0" ]; then
  log "Nothing to push"; exit 0
fi

if git push -q origin "$BRANCH" >> "$LOG" 2>&1; then
  log "Pushed $AHEAD commit(s) to origin/$BRANCH"
else
  log "Push rejected, trying pull --rebase"
  if git pull -q --rebase origin "$BRANCH" >> "$LOG" 2>&1 && git push -q origin "$BRANCH" >> "$LOG" 2>&1; then
    log "Pushed after rebase"
  else
    git rebase --abort >/dev/null 2>&1
    log "ERROR: push failed"; notify "Push fallido — revisar logs/auto_push.log"; exit 1
  fi
fi
