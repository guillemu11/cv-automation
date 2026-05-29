"""Background launcher for the Career Ops dashboard.

Used by the Windows auto-start entry (shell:startup → start_careerops.vbs).
Differs from `run_webapp.py` in three ways:
  - reload=False: no file-watcher CPU spin when running idle in the background
  - logs/webapp.log: pythonw.exe has no console, so stdout/stderr are routed
    to a rotating file for post-mortem debugging
  - sys.stdout/stderr replaced before importing uvicorn: under pythonw they
    default to None, and uvicorn's default StreamHandler crashes on .write()
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "webapp.log"

# Open log first so even import-time errors get captured.
_log = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
sys.stdout = _log
sys.stderr = _log

import logging  # noqa: E402
from logging.handlers import RotatingFileHandler  # noqa: E402

handler = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=3, encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
logging.basicConfig(level=logging.INFO, handlers=[handler])

def _find_free_port(start: int, attempts: int = 10) -> int:
    """Walk up from `start` until we find a port we can actually bind.

    Windows occasionally leaks sockets when uvicorn --reload kills its workers
    — the PID is gone but the port stays "owned" until reboot. Port-hopping
    sidesteps it without requiring a reboot.
    """
    import socket
    for i in range(attempts):
        port = start + i
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("127.0.0.1", port))
            s.close()
            return port
        except OSError:
            continue
        finally:
            s.close()
    raise RuntimeError(f"no free port in {start}..{start+attempts-1}")


if __name__ == "__main__":
    try:
        port = _find_free_port(8062)
        # Write the live port so the desktop shortcut can read it.
        (ROOT / "data" / "webapp_port.txt").write_text(str(port), encoding="utf-8")
        logging.info("starting on port %d", port)

        import uvicorn
        uvicorn.run(
            "career_ops.webapp.api:app",
            host="127.0.0.1",
            port=port,
            reload=False,
            log_level="info",
        )
    except Exception:
        logging.exception("webapp crashed at startup")
        raise
