#!/usr/bin/env bash
# Generate Colgate "Always Shelf-Ready" landing/deck images via Higgsfield.
set -u
HF="$HOME/.local/bin/higgsfield.exe"
OUT="c:/Users/pfrancisco/Desktop/CV_Automation/output/2026-06-11/Colgate-Palmolive - Ecommerce Manager/02_Deliverables/landing_colgate/assets"
mkdir -p "$OUT"

gen () {
  local name="$1"; local prompt="$2"
  echo "=== generating $name ==="
  local out
  out="$("$HF" generate create gpt_image_2 --prompt "$prompt" --aspect_ratio 16:9 --quality high --resolution 2k --wait 2>&1)"
  echo "$out"
  local url
  url="$(echo "$out" | grep -oE 'https://[^ ]+\.(png|jpg|jpeg|webp)' | head -n1)"
  if [ -n "$url" ]; then
    curl -fsSL -o "$OUT/$name.jpg" "$url" && echo "SAVED $name <- $url"
  else
    echo "NO_URL for $name"
  fi
}

STYLE="Bright, premium, clean commercial photography. Colgate brand world: signature Colgate red (#FB0007) and crisp white, fresh cyan accents. Modern UAE / Dubai e-commerce context. Sharp, optimistic, trustworthy, high-end advertising look. No text overlays, no watermarks, no logos of other brands."

gen "hero" "Hero image for an e-commerce strategy pitch. A glowing smartphone floating against a clean red-and-white gradient backdrop, its screen showing an online shopping search grid full of premium oral-care and personal-care products. Soft studio lighting, subtle motion, confident and futuristic digital-shelf feeling. $STYLE"

gen "digitalshelf" "A pristine product detail page shown on a tablet held in hand: a premium white-and-red toothpaste box as the hero product, with A+ rich content modules, five-star reviews, a 'Best Seller' badge and a bright add-to-cart button. Crisp, conversion-optimised, premium. $STYLE"

gen "qcommerce" "A quick-commerce delivery moment in Dubai: a delivery courier with a branded bag handing a small order of oral-care and personal-care essentials, a phone showing a '10 minutes' delivery timer, modern UAE city light in the background. Energetic, fast, convenient. $STYLE"

gen "marketplace" "An online marketplace search-results page on a laptop screen: a clean grid of premium oral-care products, a 'Sponsored' retail-media banner across the top, filters on the side, price tags and ratings. Looks like a top GCC e-commerce marketplace. $STYLE"

gen "retailmedia" "A sleek analytics dashboard on a wide monitor showing e-commerce performance: conversion-rate curves, ROAS and digital-shelf scorecard gauges climbing toward 100 percent, bar charts in red and cyan, a sponsored-product banner preview. Data-confident, premium SaaS look. $STYLE"

echo "=== DONE ==="
ls -la "$OUT"
