"""Regenerate only keyframe B for landing_lipton_v2 with a blindaged prompt
that explicitly forbids the double-cap bug (one cap floating + one still on
the bottle neck). Uses Flash Image edit with keyframe A as visual anchor so
composition stays locked.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from PIL import Image as PILImage

from generate_hero_v3 import flash_edit, KF_A, KF_B

PROMPT_B_FIXED = (
    "Keep the same scene, same camera framing, same dark studio background, "
    "same dramatic directional lighting, same 16:9 composition as the reference "
    "image. The Lipton bottle has now FULLY DISASSEMBLED into its individual "
    "components floating in mid-air in an exploded-view technical illustration "
    "arrangement, spread radially around the center of the frame. "
    ""
    "CRITICAL RULE about the cap: there must be EXACTLY ONE yellow cap visible "
    "in the entire scene. That single cap is detached, floating in the upper-"
    "left area of the frame, clearly separated from the bottle. The BOTTLE BODY "
    "in the center must have its neck COMPLETELY OPEN — NO cap attached, NO "
    "remnant of a cap, NO closure of any kind at the top of the bottle. The "
    "neck opening of the bottle body is a clean round mouth. Do NOT draw two "
    "caps. Do NOT leave a cap on the bottle. "
    ""
    "Visible floating components (each clearly separated and suspended in "
    "space): (1) the single yellow plastic cap floating top-left, detached. "
    "(2) the yellow Lipton label with red shield peeling off and floating "
    "upper-right. (3) the clear EMPTY, OPEN-TOPPED bottle body floating center "
    "— transparent, no label, no cap, no liquid. (4) a cluster of real tea "
    "leaves floating left. (5) a cluster of pure white-golden sugar crystals "
    "floating right like tiny diamonds catching light. (6) droplets of pure "
    "water floating bottom-left. (7) a few crystal-clear ice cubes floating "
    "bottom-right. "
    ""
    "Thin elegant white blueprint lines connect some of the components to the "
    "empty bottle body. Apple Keynote exploded-view product render aesthetic, "
    "editorial, sophisticated. Keep the background and lighting identical to "
    "the reference. Negative: no second cap, no cap on the bottle neck, no "
    "closed bottle, no text overlays, no watermarks."
)

target_size = PILImage.open(KF_A).size
print(f"Target size: {target_size}")
flash_edit(PROMPT_B_FIXED, KF_A, KF_B, target_size)
print("DONE")
