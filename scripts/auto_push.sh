#!/bin/bash
# Nightly auto-commit + merge + push at 00:00. macOS: launchd
# (~/Library/LaunchAgents/com.cvautomation.autopush.plist). Windows: Task
# Scheduler task "CV_Automation AutoPush" (scripts/install_auto_push_windows.ps1).
# Merges any origin branch not yet in the current one (e.g. claude/* from web
# sessions) when it merges cleanly; conflicting branches are skipped and flagged.
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

# Runs around midnight: before 06:00 the snapshot belongs to the previous day.
SNAP_DATE="$(date '+%Y-%m-%d')"
if [ "$(date '+%H')" -lt 6 ]; then
  SNAP_DATE="$(date -v-1d '+%Y-%m-%d' 2>/dev/null || date -d yesterday '+%Y-%m-%d')"
fi

if [ -n "$(git status --porcelain)" ]; then
  # GitHub rejects files >100MB — leave those out and warn.
  git add -A
  BIG="$(git diff --cached --name-only -z | xargs -0 -I{} find {} -type f -size +95M 2>/dev/null)"
  if [ -n "$BIG" ]; then
    echo "$BIG" | while read -r f; do git reset -q -- "$f"; done
    log "WARN: skipped large files: $BIG"; notify "Archivos >95MB no subidos (ver logs/auto_push.log)"
  fi
  if ! git diff --cached --quiet; then
    git commit -q -m "chore(auto): snapshot diario $SNAP_DATE" && log "Committed $(git rev-parse --short HEAD)"
  fi
fi

# Merge origin branches not yet in $BRANCH. merge-tree (git >= 2.38) dry-runs the
# merge; anything that would conflict (or an older git) is skipped, never forced.
if git fetch -q --prune origin >> "$LOG" 2>&1; then
  git for-each-ref --format='%(refname:short)' --no-merged HEAD refs/remotes/origin |
  while read -r ref; do
    case "$ref" in origin/HEAD|origin|"origin/$BRANCH") continue ;; esac
    if git merge-tree --write-tree HEAD "$ref" >/dev/null 2>&1; then
      if git merge -q --no-edit -m "chore(auto): merge $ref" "$ref" >> "$LOG" 2>&1; then
        log "Merged $ref"
      else
        git merge --abort >/dev/null 2>&1
        log "WARN: merge of $ref failed"; notify "No se pudo mergear ${ref#origin/}"
      fi
    else
      log "WARN: $ref conflicts with $BRANCH, not merged"; notify "Rama ${ref#origin/} con conflictos — no mergeada"
    fi
  done
else
  log "WARN: fetch failed, skipping branch merges"
fi

AHEAD="$(git rev-list --count "origin/$BRANCH..HEAD" 2>/dev/null || echo 1)"
if [ "$AHEAD" = "0" ]; then
  log "Nothing to push"; exit 0
fi

if git push -q origin "$BRANCH" >> "$LOG" 2>&1; then
  log "Pushed $AHEAD commit(s) to origin/$BRANCH"
else
  log "Push rejected, trying pull --rebase"
  if git pull -q --rebase=merges origin "$BRANCH" >> "$LOG" 2>&1 && git push -q origin "$BRANCH" >> "$LOG" 2>&1; then
    log "Pushed after rebase"
  else
    git rebase --abort >/dev/null 2>&1
    log "ERROR: push failed"; notify "Push fallido — revisar logs/auto_push.log"; exit 1
  fi
fi
