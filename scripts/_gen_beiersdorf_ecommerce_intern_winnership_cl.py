"""One-off: carta de presentación para **WINNERSHIP: E-Commerce Intern** en **Beiersdorf Middle East** (Dubái) —
reutiliza el job de `_gen_beiersdorf_ecommerce_intern_winnership.py`. Dirigida a Kartik Kulshrestha (TA Lead), el
contacto que da la oferta.

El reto de esta carta es el elefante: 5 años y título de Manager aplicando a una beca de 6 meses. La apertura lo
nombra sin rodeos y lo enlaza con lo que la beca le daría de verdad: Amazon y Carrefour (no ha trabajado con
ellos), contenido A+, keyword tagging y SEO en retailers, y NIVEA, Eucerin y Hansaplast desde dentro. **La
motivación es una inferencia nuestra, no una frase de Paula: que la valide o la reescriba con sus palabras.**

No repite la apertura de la carta del 6-oct ("I already know Beiersdorf from the other side of the table") porque
el mismo equipo de selección puede leer las dos; NIVEA va en el cuerpo.

Guardarraíles de honestidad (idénticos a los del CV):
- A+, SEO, keyword tagging, digital shelf, Amazon y Carrefour: no los ha hecho; la carta lo dice como lo que
  quiere aprender.
- NIVEA 3 meses en Miravia, sin métricas propias (el +30% GMV QoQ es de toda la cartera).
- Dashboard de stock "we built"; Deliveroo: DoFreeze NO está.
- Visa: solo "based in Dubai"; nunca "no sponsorship needed" ni "available immediately". El cierre deja abierta la
  conversación sobre "the practical side" de un programa de 6 meses.
"""
from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "_gen_beiersdorf_ecommerce_intern_winnership_cv",
    ROOT / "scripts" / "_gen_beiersdorf_ecommerce_intern_winnership.py",
)
cvmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvmod)

from career_ops.config import settings
from career_ops.generators import cover_letter as cl

CONTACT = "Kartik Kulshrestha"

PARAGRAPHS = {
    "opening_paragraph": (
        "I am applying for the WINNERSHIP E-Commerce Intern role in Beiersdorf's Middle East team, and I know it is "
        "an unusual application: I have five years in e-commerce and FMCG, and today I am Brand & Marketing Manager "
        "at DoFreeze in Dubai. I am applying because I want to work on NIVEA, Eucerin and Hansaplast from inside "
        "your e-commerce team, and because most of what you describe (content, promotions and weekly tracking on "
        "Noon and talabat) is already part of my week."
    ),
    "body_paragraph_1": (
        "At DoFreeze I look after three brands on talabat, Noon and Careem: SKU onboarding, product content and "
        "images, pricing and promotional mechanics, planned on a seasonal calendar. I measure every activation on "
        "sales. When we launched SMASH on talabat, daily sales rose 165% while a brand we left out of the campaign "
        "grew 4.7%; Befit's \"New Year, New Me\" event on Noon added 4,176 incremental units, 31% over baseline. "
        "Every week I review stock risk by dark store with an AI dashboard we built, checking whether platform "
        "orders cover demand, and I plan our Meta and Google Ads against ROI and ROAS."
    ),
    "body_paragraph_2": (
        "I have also seen NIVEA from the retailer side: at Miravia (Alibaba) I managed the account for three months, "
        "one of 42 beauty, fragrance and fashion brands whose promotions, pricing and assortment I planned, growing "
        "GMV 30% quarter on quarter across the portfolio. My habit of reading the numbers first comes from category "
        "planning at Mondelez, where I measured sell-in, sell-out and promotional effectiveness. What I would learn "
        "with you is just as clear: I have not worked with Amazon or Carrefour, and I have not yet managed A+ "
        "content, keyword tagging or retailer SEO. Those are the skills I want this programme to give me."
    ),
    "closing_paragraph": (
        "I am based in Dubai and would welcome a conversation about how I could contribute from the first week, "
        "and about the practical side of a six-month programme. Thank you for your consideration."
    ),
}


def main() -> None:
    job = cvmod.make_job()
    final_dir = settings.output_dir / cvmod.DATE_FOLDER / f"{cvmod.COMPANY} - {cvmod.TITLE}"
    dest = final_dir / "01_CV_y_Carta"
    dest.mkdir(parents=True, exist_ok=True)

    cl_docx = cl._fill_template(PARAGRAPHS, job, CONTACT)
    cl_pdf = cvmod._to_pdf_soffice(cl_docx)

    moved = dest / cl_pdf.name
    shutil.move(str(cl_pdf), str(moved))
    shutil.copy(str(moved), str(dest / "Paula De Francisco - Cover Letter.pdf"))
    print("OK", moved.name, "PAGES", cvmod._pages(moved))

    stray = cl_pdf.parent.parent
    if stray.exists() and stray.resolve() != final_dir.resolve():
        shutil.rmtree(stray, ignore_errors=True)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
