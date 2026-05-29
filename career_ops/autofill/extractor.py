"""Extract a normalized list of form fields from a live page.

Single ``page.evaluate()`` round-trip walks the DOM and returns every input,
textarea, select, radio group and checkbox visible on the page along with a
stable selector and the best available human label (``<label for=>``,
``aria-label``, ``aria-labelledby``, placeholder, surrounding text).
"""
from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class FormField:
    selector: str          # CSS selector usable by Playwright (#id preferred)
    field_type: str        # "text" | "textarea" | "select" | "radio" | "checkbox" | "file" | "email" | "tel"
    label: str             # best human-readable label
    name: str              # name attribute (groups radios)
    required: bool
    options: list[str]     # for select / radio — visible option labels
    placeholder: str = ""


_EXTRACT_JS = r"""
() => {
  const cssEscape = (s) => (window.CSS && CSS.escape) ? CSS.escape(s) : s.replace(/"/g, '\\"');

  const labelFor = (el) => {
    if (el.id) {
      const lbl = document.querySelector(`label[for="${cssEscape(el.id)}"]`);
      if (lbl && lbl.innerText.trim()) return lbl.innerText.trim();
    }
    if (el.getAttribute('aria-label')) return el.getAttribute('aria-label').trim();
    const lbBy = el.getAttribute('aria-labelledby');
    if (lbBy) {
      const lb = document.getElementById(lbBy);
      if (lb && lb.innerText.trim()) return lb.innerText.trim();
    }
    let p = el.parentElement;
    for (let i = 0; i < 4 && p; i++) {
      const lbl = p.querySelector(':scope > label, :scope > legend');
      if (lbl && lbl.innerText.trim()) return lbl.innerText.trim();
      p = p.parentElement;
    }
    if (el.placeholder) return el.placeholder.trim();
    return '';
  };

  const stableSelector = (el) => {
    if (el.id) return `#${cssEscape(el.id)}`;
    if (el.name) return `${el.tagName.toLowerCase()}[name="${cssEscape(el.name)}"]`;
    const path = [];
    let cur = el;
    while (cur && cur.nodeType === 1 && path.length < 6) {
      let part = cur.tagName.toLowerCase();
      if (cur.parentElement) {
        const sibs = Array.from(cur.parentElement.children).filter(c => c.tagName === cur.tagName);
        if (sibs.length > 1) part += `:nth-of-type(${sibs.indexOf(cur) + 1})`;
      }
      path.unshift(part);
      cur = cur.parentElement;
    }
    return path.join(' > ');
  };

  const isVisible = (el) => {
    if (!el.isConnected) return false;
    const rect = el.getBoundingClientRect();
    if (rect.width === 0 && rect.height === 0) return false;
    const style = window.getComputedStyle(el);
    return style.display !== 'none' && style.visibility !== 'hidden';
  };

  const fields = [];
  const seenRadioGroups = new Set();

  document.querySelectorAll('input, textarea, select').forEach(el => {
    if (!isVisible(el)) return;
    if (el.disabled || el.readOnly) return;
    const tag = el.tagName.toLowerCase();
    const type = (el.type || tag).toLowerCase();
    if (['hidden', 'submit', 'button', 'reset', 'image'].includes(type)) return;

    if (type === 'radio') {
      const key = el.name || stableSelector(el);
      if (seenRadioGroups.has(key)) return;
      seenRadioGroups.add(key);
      const group = Array.from(document.querySelectorAll(`input[type="radio"][name="${cssEscape(el.name)}"]`));
      const opts = group.map(r => labelFor(r) || r.value).filter(Boolean);
      const groupContainer = el.closest('fieldset, [role="radiogroup"]') || el.parentElement;
      let groupLabel = '';
      if (groupContainer) {
        const lg = groupContainer.querySelector('legend, [role="heading"]');
        if (lg) groupLabel = lg.innerText.trim();
      }
      fields.push({
        selector: `input[type="radio"][name="${el.name || ''}"]`,
        field_type: 'radio',
        label: groupLabel || labelFor(el),
        name: el.name || '',
        required: el.required || false,
        options: opts,
        placeholder: '',
      });
      return;
    }

    if (type === 'select-one' || type === 'select-multiple' || tag === 'select') {
      const opts = Array.from(el.options).map(o => o.text.trim()).filter(t => t && t.toLowerCase() !== 'select');
      fields.push({
        selector: stableSelector(el),
        field_type: 'select',
        label: labelFor(el),
        name: el.name || '',
        required: el.required || false,
        options: opts,
        placeholder: '',
      });
      return;
    }

    if (type === 'checkbox') {
      fields.push({
        selector: stableSelector(el),
        field_type: 'checkbox',
        label: labelFor(el),
        name: el.name || '',
        required: el.required || false,
        options: [],
        placeholder: '',
      });
      return;
    }

    if (type === 'file') {
      fields.push({
        selector: stableSelector(el),
        field_type: 'file',
        label: labelFor(el),
        name: el.name || '',
        required: el.required || false,
        options: [],
        placeholder: '',
      });
      return;
    }

    fields.push({
      selector: stableSelector(el),
      field_type: tag === 'textarea' ? 'textarea' : type,
      label: labelFor(el),
      name: el.name || '',
      required: el.required || false,
      options: [],
      placeholder: el.placeholder || '',
    });
  });

  return fields;
}
"""


def extract_form_fields(page: Page) -> list[FormField]:
    """Walk the page DOM once and return all fillable form fields."""
    raw = page.evaluate(_EXTRACT_JS)
    return [FormField(**item) for item in raw]
