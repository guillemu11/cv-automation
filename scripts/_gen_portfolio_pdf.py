"""Exporta el portfolio de Paula (output/portfolio_paula/) a PDF.

El sitio es una single-page con reveal-on-scroll (IntersectionObserver) y contadores
animados: al imprimir directamente, los elementos con `[data-reveal]` salen en
`opacity: 0` y los stats en "+0%". Por eso NO se imprime la carpeta original —
se copia a un temporal, se le inyectan overrides de print y un script que fija el
estado final, y se imprime esa copia con Chrome headless (`--print-to-pdf`).

Ver [[visual-verify-with-chrome-headless]]: Chrome headless NO rasteriza PDFs, así
que la verificación visual del resultado se hace con pypdfium2.

Uso (dev): python scripts/_gen_portfolio_pdf.py [destino.pdf]
Por defecto escribe output/portfolio_paula/Paula_De_Francisco_Portfolio.pdf
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "output" / "portfolio_paula"
DEFAULT_OUT = SRC / "Paula_De_Francisco_Portfolio.pdf"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PRINT_CSS = """
/* ---- PRINT / PDF EXPORT OVERRIDES (copia temporal, no el sitio live) ---- */
[data-reveal], [data-reveal].is-visible { opacity: 1 !important; transform: none !important; transition: none !important; }
.hero-tagline .line > span, .hero-fade, .hero-portrait { opacity: 1 !important; transform: none !important; transition: none !important; }
.ticker-track { animation: none !important; }
.top-nav { position: static !important; }
@media print {
  html, body { background: #fff !important; }
  .top-nav { display: none !important; }
  section { padding: var(--space-4) 0 !important; }
  .hero { padding-top: var(--space-4) !important; padding-bottom: var(--space-4) !important; }
  .work-card, .exp-item, .cap-card, .stat, .edu-item { break-inside: avoid; page-break-inside: avoid; }
  h2, .section-heading { break-after: avoid; page-break-after: avoid; }
  .experience { break-before: page; page-break-before: always; }
  a[href]:after { content: none !important; }
}
"""

FINALIZE_JS = """<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('[data-reveal]').forEach(function (e) { e.classList.add('is-visible'); });
  var hero = document.querySelector('[data-hero]'); if (hero) hero.classList.add('is-in');
  document.querySelectorAll('[data-count]').forEach(function (e) {
    var t = parseFloat(e.dataset.count), d = parseInt(e.dataset.decimals || '0', 10);
    e.textContent = (e.dataset.prefix || '') + (d > 0 ? t.toFixed(d) : Math.round(t)) + (e.dataset.suffix || '');
  });
});
</script>
</body>"""


def build(out_path: Path) -> Path:
    if not (SRC / "index.html").exists():
        raise SystemExit(f"no encuentro el portfolio en {SRC}")
    if not Path(CHROME).exists():
        raise SystemExit("Google Chrome no está instalado en la ruta esperada")

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "pf"
        shutil.copytree(SRC, work)

        with (work / "styles.css").open("a", encoding="utf-8") as fh:
            fh.write(PRINT_CSS)

        index = work / "index.html"
        html = index.read_text(encoding="utf-8")
        if "</body>" not in html:
            raise SystemExit("index.html sin </body>; no puedo inyectar el finalize script")
        index.write_text(html.replace("</body>", FINALIZE_JS, 1), encoding="utf-8")

        out_path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             "--virtual-time-budget=8000", f"--print-to-pdf={out_path}",
             f"file://{index}"],
            check=True, capture_output=True, timeout=180,
        )

    if not out_path.exists():
        raise SystemExit("Chrome no generó el PDF")

    try:
        from pypdf import PdfReader
        print(f"PAGES {len(PdfReader(str(out_path)).pages)}")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    return out_path


def main() -> None:
    out = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else DEFAULT_OUT
    print("OK_PORTFOLIO", build(out))


if __name__ == "__main__":
    main()
