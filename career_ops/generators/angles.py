"""Positioning angles — per-target campaign framings for speculative outreach.

A "positioning angle" is a named instruction set that tells the CV, cover
letter, outreach and deliverable generators *which slice* of Paula's profile
to emphasize when adapting content for a specific target.

Generators read the angle from ``Job.raw["positioning_angle"]`` (carried by
the speculative-target seed in scored_jobs.json) and inject the angle's
``system_addendum`` / ``user_addendum`` into their Claude prompts. Absent or
unknown angles are a no-op — existing flows stay identical.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Angle:
    key: str
    name: str
    # Extra system-prompt instruction prepended to the generator's default
    # system message. Keep short — Claude already has the full profile in
    # the user message.
    system_addendum: str
    # Extra user-prompt block appended after the job description, giving
    # Claude the explicit prioritisation order for this angle.
    user_addendum: str
    # Suggested deliverable type for this angle. Generators may use this
    # when the caller doesn't pick one explicitly.
    suggested_deliverable_type: str
    # Custom title hint passed into the deliverable system prompt so the
    # output is tilted toward the angle (e.g. "Inditex Retail Playbook for
    # MENA Launch" instead of the generic "90-Day Action Plan").
    deliverable_brief: str


_ANGLES: dict[str, Angle] = {
    "inditex_insider": Angle(
        key="inditex_insider",
        name="The Inditex Insider",
        system_addendum=(
            "POSITIONING ANGLE — Inditex Insider:\n"
            "Frame Paula as Inditex-trained and already based in Dubai, ready to bring "
            "the Inditex retail playbook (visual merchandising standards, store ops "
            "cadence, premium fashion retail discipline) into the target company's "
            "MENA expansion. Emphasize Massimo Dutti experience even though it is her "
            "earliest role — it is the strategic anchor for this application. Keep "
            "fashion-retail language front and centre; deprioritize FMCG-only framings."
        ),
        user_addendum=(
            "## Positioning priority for this application\n"
            "Lead with the Inditex / Massimo Dutti experience and the fashion-retail "
            "thread that runs through Paula's career (Miravia fashion accounts, Glovo "
            "Retail vertical, CUNEF Fashion Industry thesis specialisation).\n"
            "Reference 'Inditex-trained' or 'fashion retail' in the headline / opening "
            "where natural. Massimo Dutti should appear in the CV with a brief but "
            "intentional bullet set — not buried."
        ),
        suggested_deliverable_type="action_plan",
        deliverable_brief=(
            "Title this deliverable as an 'Inditex Retail Playbook' adapted to the "
            "target company's MENA / UAE launch context. Sections should translate "
            "Inditex operating principles (visual merchandising cadence, weekly product "
            "drops, store ops rhythm, NPD-to-floor flow) into concrete first-quarter "
            "initiatives for the target. Tone: confident, operationally specific."
        ),
    ),

    "fashion_commerce_bridge": Angle(
        key="fashion_commerce_bridge",
        name="Fashion-Commerce Bridge",
        system_addendum=(
            "POSITIONING ANGLE — Fashion-Commerce Bridge:\n"
            "Frame Paula as a bridge between fashion-aware brand work and operational "
            "e-commerce / multibrand retail execution. Lean on Miravia (42 multibrand "
            "key accounts, fashion + beauty), Glovo Retail vertical (multi-category "
            "marketplace mechanics), DoFreeze (50+ country multimarket scale) and "
            "Inditex roots (Massimo Dutti). Speak the language of multibrand portfolio "
            "operators with strong physical retail + digital ambition."
        ),
        user_addendum=(
            "## Positioning priority for this application\n"
            "Lead with multibrand portfolio fluency and the ability to orchestrate "
            "brands across physical retail + digital channels. Highlight Miravia (42 "
            "accounts is a direct analogue to a multibrand holding) and Glovo's Retail "
            "vertical. Mention Inditex/Massimo Dutti as the operational foundation, "
            "not the headline. Use 'fashion', 'multibrand', 'omnichannel' liberally; "
            "minimize FMCG-only phrasing."
        ),
        suggested_deliverable_type="brand_analysis",
        deliverable_brief=(
            "Title this deliverable around 'Digital-to-Physical Brand Activation for "
            "Multibrand Retail'. Pick one of the target company's portfolio brands "
            "(from the company website / job description) and outline a concrete "
            "omnichannel activation: digital touchpoints, store-level execution, "
            "campaign KPIs. Show portfolio-level thinking, not single-brand thinking."
        ),
    ),

    # Gloria Jeans — chosen 2026-05-19 from the deep-research dossier
    "gloria_land_the_brand": Angle(
        key="gloria_land_the_brand",
        name="Land the Brand Before the Store",
        system_addendum=(
            "POSITIONING ANGLE — Land the Brand Before the Store:\n"
            "Frame Paula as the digital-first brand builder who would use the "
            "6-12 month runway before Gloria Jeans' first MENA stores open to "
            "build localised brand presence: Arabic-first content, UAE creator "
            "network, modesty-aware capsule storytelling. The verifiable gap is "
            "the near-zero MENA social footprint (sub-300-follower regional IG "
            "accounts, Russian-language global handle). Lean into 'arrive in "
            "malls with awareness, not as another unknown logo'."
        ),
        user_addendum=(
            "## Positioning priority for this application\n"
            "Lead with the digital-pre-launch thesis. Concrete moves Paula "
            "would make: Arabic-first IG/TikTok, monthly UAE creator drops, "
            "modesty-aware capsule narrative, Ramadan and Eid as content "
            "moments not just sale moments. Stats should anchor on "
            "Miravia + Glovo (digital-native commerce work), not just DoFreeze."
        ),
        suggested_deliverable_type="action_plan",
        deliverable_brief=(
            "Title around 'Land the Brand Before the Store — a six-month "
            "MENA brand-build for Gloria Jeans'. Reference the visible gap "
            "(near-zero MENA social footprint) without naming follower counts. "
            "Manifesto must be concrete: name Ramadan, Eid, or a creator "
            "category by name. Tone: confident, fashion-magazine, NOT a "
            "consulting deck."
        ),
    ),

    # Azadea — chosen 2026-05-19 from the deep-research dossier
    "azadea_eataly_playbook": Angle(
        key="azadea_eataly_playbook",
        name="The Eataly Playbook",
        system_addendum=(
            "POSITIONING ANGLE — The Eataly Playbook:\n"
            "Frame Paula as the candidate who can turn Azadea's Feb 2025 "
            "Eataly restructuring (Investindustrial taking direct control, "
            "€100m / 40-store plan) into a category position. Position Azadea "
            "as the GCC's go-to operator for experiential, culture-led F&B — "
            "beyond Eataly: Beihouse, future Italian/European concepts. F&B "
            "has structurally higher repeat-visit frequency than apparel — "
            "ideal for loyalty data and consumer-brand pull-through before "
            "the IPO restarts. Lean into the Daher quotes; respect that "
            "Azadea is also a fashion-retail business and avoid sounding "
            "like the F&B play swallows the rest."
        ),
        user_addendum=(
            "## Positioning priority for this application\n"
            "Lead with the Eataly moment as the proof point. Specific moves "
            "Paula would make: cross-format loyalty (apparel customers eat; "
            "Eataly customers shop), F&B-first content programming, "
            "experiential calendar around Italian seasonal moments (truffle, "
            "olive harvest) localised for Ramadan iftars and Eid breakfasts. "
            "Stats should anchor on Miravia multi-category orchestration "
            "(beauty + fragrances + fashion across 42 accounts) as the closest "
            "Paula-experience analogue to multi-format Azadea."
        ),
        suggested_deliverable_type="brand_analysis",
        deliverable_brief=(
            "Title around 'The Eataly Playbook — turning a category bet into "
            "a category position'. Reference Investindustrial / €100m plan as "
            "evidence of board-level commitment. Manifesto must name at least "
            "one of: Eataly, Beihouse, iftar, olive harvest, Italian-week. "
            "Stats can use Paula's multi-category numbers from Miravia. Tone: "
            "confident editorial — Monocle Italy / Cereal Magazine register, "
            "NOT consulting-deck."
        ),
    ),
}


def get(angle_key: str | None) -> Angle | None:
    """Return the Angle for a key, or None if missing/unknown."""
    if not angle_key:
        return None
    return _ANGLES.get(angle_key)


def list_angles() -> list[dict]:
    """Return all angles as dicts — used by the dashboard UI dropdown."""
    return [
        {"key": a.key, "name": a.name, "deliverable": a.suggested_deliverable_type}
        for a in _ANGLES.values()
    ]
