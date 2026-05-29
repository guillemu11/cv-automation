"""Standalone salary parser for job descriptions and salary strings.

Normalizes salary to AED/month regardless of input format.
Used by hard_filters to enforce the 20K AED floor.

Design principle: when in doubt, return None. A false negative (letting a
low-paying job through to the scorer) is much better than a false positive
(rejecting a great job because we mis-parsed "AED 25K" as 25 AED).
"""
from __future__ import annotations

import re

from ..config import settings

# Currency symbols to ISO codes
_SYMBOL_TO_CODE: dict[str, str] = {
    "$": "USD", "€": "EUR", "£": "GBP", "Dhs": "AED", "dhs": "AED",
}

# How to convert an interval to monthly
_INTERVAL_TO_MONTHLY: dict[str, float] = {
    "year": 1 / 12, "annum": 1 / 12, "annual": 1 / 12, "annually": 1 / 12,
    "yr": 1 / 12, "p.a.": 1 / 12, "pa": 1 / 12,
    "month": 1.0, "mo": 1.0, "monthly": 1.0, "pm": 1.0,
    "week": 52 / 12, "wk": 52 / 12, "weekly": 52 / 12, "pw": 52 / 12,
    "day": 365 / 12, "daily": 365 / 12,
    "hour": (40 * 52) / 12, "hr": (40 * 52) / 12, "hourly": (40 * 52) / 12,
}

# Range pattern: "AED 15K - AED 25K a month", "USD 4,000-6,000/month"
_RANGE_RE = re.compile(
    r"(?P<cur>AED|USD|EUR|GBP|SAR|QAR|KWD|BHD|OMR|\$|€|£|Dhs)\s*"
    r"(?P<min>[\d,\.]+)\s*(?P<min_k>[kK])?"
    r"\s*[-–—]+\s*(?:AED|USD|EUR|GBP|SAR|QAR|KWD|BHD|OMR|\$|€|£|Dhs)?\s*"
    r"(?P<max>[\d,\.]+)\s*(?P<max_k>[kK])?"
    r"(?:\s*(?:a|/|per)\s*)?(?P<int>[a-z.]+)?",
    re.IGNORECASE,
)

# Single value: "AED 25K a month", "USD 5,000/yr"
_SINGLE_RE = re.compile(
    r"(?P<cur>AED|USD|EUR|GBP|SAR|QAR|KWD|BHD|OMR|\$|€|£|Dhs)\s*"
    r"(?P<amt>[\d,\.]+)\s*(?P<amt_k>[kK])?"
    r"(?:\s*(?:a|/|per)\s*)?(?P<int>[a-z.]+)?",
    re.IGNORECASE,
)


def _to_aed_monthly(amount: float, currency: str, interval: str | None) -> int | None:
    """Convert an amount in any currency/interval to AED/month. Returns None if unknown."""
    code = _SYMBOL_TO_CODE.get(currency, currency.upper())
    rates = settings.currency_to_aed
    if code == "AED":
        rate = 1.0
    elif code in rates:
        rate = rates[code]
    else:
        return None  # unknown currency → can't convert → don't filter

    int_key = (interval or "month").lower().strip().rstrip(".")
    multiplier = _INTERVAL_TO_MONTHLY.get(int_key, 1.0)

    return int(round(amount * rate * multiplier))


def parse_salary(text: str | None) -> tuple[int | None, int | None]:
    """Best-effort extraction of monthly AED salary range from free-form text.

    Returns (aed_min_monthly, aed_max_monthly). Both None if unparseable — which
    is the correct outcome for "Competitive", "Negotiable", or no salary info.
    """
    if not text:
        return None, None

    # Try range first
    m = _RANGE_RE.search(text)
    if m:
        try:
            lo = float(m["min"].replace(",", ""))
            hi = float(m["max"].replace(",", ""))
            if m.group("min_k"):
                lo *= 1000
            if m.group("max_k"):
                hi *= 1000
            return (
                _to_aed_monthly(lo, m["cur"], m.group("int")),
                _to_aed_monthly(hi, m["cur"], m.group("int")),
            )
        except Exception:
            pass

    # Try single value
    m = _SINGLE_RE.search(text)
    if m:
        try:
            amt = float(m["amt"].replace(",", ""))
            if m.group("amt_k"):
                amt *= 1000
            val = _to_aed_monthly(amt, m["cur"], m.group("int"))
            return val, val
        except Exception:
            pass

    return None, None
