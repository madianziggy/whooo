# Whole-card rotation, revision 11

The first two intro pages use the previous complete landscape card faces as image inputs. Each face is mapped to its on-its-side card plane with one perspective transform. No logo, owl, chip, contactless symbol or tagline is extracted, moved, resized or generated separately. The existing graphite/silver and platinum/graphite colours are retained.

Source files are frozen in `references/card-rotation-v11/graphite-layout.png` and `platinum-layout.png`. The original stack pose and existing glossy teal phone scene are retained as the two templates. `CARD-ROTATION-V11.json` records source hashes, measured corner coordinates and output names. `scripts/rotate-reference-cards-v11.py` reproduces the transforms with ImageMagick, using Python only for source-edge measurement and geometry.

The whole first scene is translated up 220 source pixels, approximately 100 CSS pixels at 390 × 844, so the stack finishes above the bottom button. Both backgrounds use bottom alignment for the shorter mobile viewports. The payment-terminal photograph and app data flows are retained. All three intro headers use the existing owl favicon in white. Page three adds Apple Pay, Google Pay, Visa and Mastercard on equal white tiles, with original logo proportions and colours.

Final assets:

- `/workspace/sites/whoo-card-mobile/dist/assets/intro-cards-rotated-v11.png`
- `/workspace/sites/whoo-card-mobile/dist/assets/intro-wallet-card-rotated-v11.png`

Verification confirms that pixels outside each card face are identical to their template before the requested first-scene translation. The cards are processed as complete photographic surfaces. This verifies the asset operation; full mobile-browser visual testing is still unavailable.
