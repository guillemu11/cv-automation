#!/usr/bin/env python3
"""Start the Career Ops web dashboard.

Usage:
    python scripts/run_webapp.py
    python scripts/run_webapp.py --port 8062

Note: default port has been bumped to 8062 because Windows is leaking orphaned
TCP sockets on 8060 and 8061 (zombie PIDs that survive `taskkill`). When that
happens we just bump to the next free port. If 8062 also goes ghost, try 8063.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import uvicorn

if __name__ == "__main__":
    port = 8062
    if "--port" in sys.argv:
        idx = sys.argv.index("--port")
        port = int(sys.argv[idx + 1])

    # Tell the FastAPI startup hook which port the dashboard is on so the
    # BrowserWorker can open the right URL in tab 1.
    os.environ["CAREEROPS_PORT"] = str(port)

    print(f"\n  Career Ops Dashboard")
    print(f"  http://localhost:{port}\n")

    # reload=True is great for dev but it RESPAWNS the process on file changes,
    # which would close Chromium and re-open it every time. Disable it when the
    # browser worker is enabled — the cost of restarting manually is much less
    # than losing the browser tabs mid-task.
    auto_browser = os.environ.get("CAREEROPS_AUTO_BROWSER", "1") != "0"
    uvicorn.run(
        "career_ops.webapp.api:app",
        host="127.0.0.1",
        port=port,
        reload=not auto_browser,
        log_level="info",
    )
