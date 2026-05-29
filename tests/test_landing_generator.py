"""Unit tests for the structured-pitch landing generator (7-section model).

Schema since 2026-05-19:
    hero, diagnosis, thesis, plan, proof, win, closing
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from career_ops.generators import landing_template
from career_ops.generators import landing_generator


SAMPLE_CLAUDE_PAYLOAD = {
    "hero": {
        "headline": "A real proposal for testing",
        "support": "A six-month plan for the test company",
        "chapters": ["The diagnosis", "The thesis", "The plan", "The win"],
    },
    "diagnosis": {
        "eyebrow": "01 — the gap",
        "heading": "Where you are now.",
        "body_paragraphs": [
            "Two short paragraphs of diagnosis.",
            "A second one with more context.",
        ],
    },
    "thesis": {
        "eyebrow": "02 — the answer",
        "headline": "Build the brand before the store opens.",
        "body_paragraphs": ["Why the thesis holds."],
    },
    "plan": {
        "eyebrow": "03 — the plan",
        "headline": "Three phases. Six months.",
        "lede": "A practical roadmap.",
        "phases": [
            {"span": "Weeks 1-4",  "name": "Foundation",  "body": "Do A first."},
            {"span": "Months 2-3", "name": "Acceleration","body": "Then do B."},
            {"span": "Months 4-6", "name": "Launch",      "body": "Finally do C."},
        ],
    },
    "proof": {
        "eyebrow": "04 — what I bring",
        "headline": "Track record across categories.",
        "stats": [
            {"number": "42",   "label": "key accounts", "sublabel": "Miravia"},
            {"number": "+30%", "label": "GMV growth"},
            {"number": "50+",  "label": "markets", "sublabel": "from Dubai"},
        ],
    },
    "win": {
        "eyebrow": "05 — what success looks like",
        "headline": "In six months, the market knows you.",
        "metrics": [
            {"number": "+100K", "text": "verified IG followers"},
            {"number": "15%",   "text": "engagement on creator drops"},
            {"number": "3",     "text": "capsule launches with sell-through"},
        ],
    },
    "closing": {
        "paragraph": "Ready when you are.",
        "cta_line":  "Thirty minutes — coffee or call.",
    },
}

SAMPLE_CONTENT = {
    **SAMPLE_CLAUDE_PAYLOAD,
    "company": "TestCo",
    "candidate_name": "Paula De Francisco",
    "candidate_email": "paulich98@hotmail.com",
    "candidate_phone": "+971 50 386 3656",
    "candidate_linkedin": "linkedin.com/in/paula-de-francisco-perez",
}

SAMPLE_BRAND = {
    "ink":        "oklch(0.18 0.01 60)",
    "paper":      "oklch(0.97 0.008 80)",
    "paper_deep": "oklch(0.94 0.012 70)",
    "accent":     "oklch(0.55 0.14 35)",
    "muted":      "oklch(0.55 0.005 60)",
}


def test_render_returns_three_files():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    assert set(files.keys()) == {"index.html", "styles.css", "scroll.js"}


def test_render_emits_all_seven_sections():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    for cls in ("b-hero", "b-diagnosis", "b-thesis", "b-plan",
                "b-proof", "b-win", "b-closing"):
        assert cls in html, f"missing section: {cls}"


def test_render_emits_hero_index_with_chapters():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    assert "In this proposal" in html
    for ch in SAMPLE_CONTENT["hero"]["chapters"]:
        assert ch in html


def test_render_emits_three_named_phases():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    for name in ("Foundation", "Acceleration", "Launch"):
        assert name in html
    # Spans
    for span in ("Weeks 1-4", "Months 2-3", "Months 4-6"):
        assert span in html


def test_render_emits_three_stats_and_win_metrics():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    assert html.count('class="b-proof__stat"') == 3
    assert ">42<" in html and ">+30%<" in html and ">50+<" in html
    # win metrics
    for n in ("+100K", "15%", "3"):
        assert n in html


def test_render_injects_oklch_palette():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    css = files["styles.css"]
    assert "oklch(0.18 0.01 60)" in css
    assert "oklch(0.55 0.14 35)" in css
    assert "oklch(0.97 0.008 80)" in css


def test_render_loads_italiana_and_geist():
    html = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)["index.html"]
    assert "family=Italiana" in html
    assert "family=Geist" in html


def test_render_html_escapes_user_content():
    bad = dict(SAMPLE_CONTENT)
    bad["diagnosis"] = dict(SAMPLE_CONTENT["diagnosis"])
    bad["diagnosis"]["body_paragraphs"] = ["R&D under <5% churn.<script>x</script>"]
    html = landing_template.render(bad, SAMPLE_BRAND)["index.html"]
    assert "<script>x</script>" not in html
    assert "R&amp;D" in html
    assert "&lt;5% churn" in html


def test_render_picks_up_real_images(tmp_path):
    assets = tmp_path / "assets"
    assets.mkdir()
    for slot in ("hero", "man", "bleed", "dip1", "dip2", "tri1", "tri2", "tri3"):
        (assets / f"{slot}.png").write_bytes(b"x")
    html = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND,
                                    landing_dir=tmp_path)["index.html"]
    assert "has-image" in html
    # All three image-bearing blocks (hero, diagnosis figure as 'man', win 'bleed')
    assert 'src="assets/hero.png"' in html
    assert 'src="assets/man.png"' in html
    assert 'src="assets/bleed.png"' in html


def test_render_includes_contact_details():
    html = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)["index.html"]
    assert "paulich98@hotmail.com" in html
    assert "+971 50 386 3656" in html
    assert "linkedin.com/in/paula-de-francisco-perez" in html
    assert 'href="tel:+971503863656"' in html


def test_render_no_pure_black_or_white():
    css = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)["styles.css"]
    assert "#000" not in css
    assert "#fff" not in css and "#FFF" not in css


def test_render_no_gradient_text():
    css = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)["styles.css"]
    assert "background-clip: text" not in css
    assert "-webkit-background-clip: text" not in css


def test_word_count_in_target_range_for_canonical():
    """Canonical sample is tiny — used to exercise the counter, not budget."""
    wc = landing_generator._word_count(SAMPLE_CLAUDE_PAYLOAD)
    assert wc > 30  # tiny but nonzero
    assert wc < 2000


def test_banned_phrase_flag_detects_buzzwords():
    payload = {
        **SAMPLE_CLAUDE_PAYLOAD,
        "thesis": {
            "eyebrow": "02",
            "headline": "Headline",
            "body_paragraphs": [
                "We leverage our holistic ecosystem to ideate seamless synergy.",
            ],
        },
    }
    hits = landing_generator._flag_banned_phrases(payload)
    for w in ("leverage", "holistic", "ecosystem", "ideate", "synergy", "seamless"):
        assert w in hits


def test_banned_phrase_flag_clean_on_canonical():
    assert landing_generator._flag_banned_phrases(SAMPLE_CLAUDE_PAYLOAD) == []


def test_strip_brand_names_replaces_inditex_and_massimo():
    src = "Inditex-trained, the Inditex playbook from Massimo Dutti days."
    out = landing_generator._strip_brand_names(src)
    assert "Inditex" not in out
    assert "Massimo" not in out


# ─── Integration (mocks Claude) ────────────────────────────────────────

def test_generate_landing_writes_files_to_disk(tmp_path, monkeypatch):
    from career_ops.config import settings
    from career_ops.discovery.normalize import Job
    from career_ops.analyzer import JobAnalysis

    monkeypatch.setattr(settings, "output_dir", tmp_path)
    # Also stub landing_to_pdf so the integration test doesn't need a
    # running browser or dashboard.
    monkeypatch.setattr(landing_generator, "landing_to_pdf",
                        lambda *_args, **_kw: tmp_path / "stub.pdf")

    job = Job(
        id="testid", title="Marketing Manager (Speculative)", company="TestCo",
        location="Dubai, UAE", url="", source="speculative",
        description="A test company.",
        raw={"speculative": True},
    )
    analysis = JobAnalysis(
        score=85, tier="Hot", skills_match=[], missing_skills=[],
        sector_fit="", seniority_fit="", red_flags=[], ats_keywords=[],
        reasoning="speculative",
    )

    with patch.object(landing_generator.llm, "is_available",
                       return_value=(True, "anthropic")), \
         patch.object(landing_generator.llm, "generate_structured",
                       return_value=SAMPLE_CLAUDE_PAYLOAD):
        out = landing_generator.generate_landing(job, analysis)

    assert out is not None
    assert out.name == "index.html"
    assert out.parent.name == "landing"
    assert (out.parent / "styles.css").exists()
    assert (out.parent / "scroll.js").exists()
    html = out.read_text(encoding="utf-8")
    assert "TestCo" in html
    assert "Paula De Francisco" in html
    assert "Foundation" in html and "Launch" in html


def test_generate_landing_returns_none_when_llm_unavailable(tmp_path, monkeypatch):
    from career_ops.config import settings
    from career_ops.discovery.normalize import Job
    from career_ops.analyzer import JobAnalysis

    monkeypatch.setattr(settings, "output_dir", tmp_path)

    job = Job(
        id="x", title="x", company="X", location="x", url="", source="speculative",
        description="", raw={"speculative": True},
    )
    analysis = JobAnalysis(
        score=0, tier="Cold", skills_match=[], missing_skills=[],
        sector_fit="", seniority_fit="", red_flags=[], ats_keywords=[],
        reasoning="",
    )

    with patch.object(landing_generator.llm, "is_available",
                       return_value=(False, "no key")):
        out = landing_generator.generate_landing(job, analysis)

    assert out is None
