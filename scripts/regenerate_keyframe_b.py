"""Regenerate keyframe B using Gemini 2.5 Flash Image in edit mode, with
keyframe A as the visual reference, then crop/resize to match A's 16:9 dims.

Goal: keep the exact glass/bottle/lighting composition from A, only change
the state of the scene to show the glass fully poured with a visible
half-dark / half-gold layered split.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from PIL import Image as PILImage

from generate_hero_v2 import flash_edit_to_16x9, KEYFRAME_A, KEYFRAME_B

PROMPT_B_EDIT = (
    "Keep this exact scene identical: same glass, same ice, same Lipton bottle "
    "with its yellow 'Lipton Ice Tea' label upright and legible, same camera "
    "angle, same warm backlight window, same moody dark background, same matte "
    "surface, same bottle tilt angle and position. Do NOT move or change any "
    "object. The only change: the glass is now completely full of tea up to the "
    "rim. The tea inside the glass is split into TWO clearly distinct horizontal "
    "layers meeting at the exact midpoint of the glass: the BOTTOM half is a "
    "deep dark amber tea color, the TOP half is a much lighter translucent "
    "golden color (like pale honey). The boundary line between the two layers "
    "is clean and visible. Ice cubes still visible through the tea. One final "
    "drop of golden tea is falling from the bottle spout into the glass. "
    "Photorealistic, cinematic grade, 16:9 wide composition. Negative: no "
    "hands, no people, no extra text, no logo distortion, no mirrored labels."
)

ref = PILImage.open(KEYFRAME_A)
target_size = ref.size
print(f"Target size (from keyframe A): {target_size}")

flash_edit_to_16x9(PROMPT_B_EDIT, KEYFRAME_A, KEYFRAME_B, target_size)
print("DONE")
