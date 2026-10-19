# Plus, Premium and Metal artwork

The black and silver card faces are whole-plane perspective normalizations of the two complete approved intro faces. No owl or wordmark is rebuilt. The source photographs and measured face corners are retained in `references/card-rotation-v11/` and `CARD-ROTATION-V11.json`.

Current project assets:

- `dist/assets/account-plus-v13.png`: black with chrome owl.
- `dist/assets/account-premium-v13.png`: silver with black owl.
- `dist/assets/account-metal-v13.png`: gold with chrome owl.
- `references/account-cards-v13/gold-edit.png`: original built-in image-generation edit with transparent background.
- `references/account-cards-v13/FEATURES.md`: the supplied feature table, unchanged.

Regenerate the normalized 856 × 540 account images with `python3 scripts/prepare-account-cards-v13.py`. ImageMagick maps the full original faces to the landscape canvas and normalizes the generated gold edit. The front-facing selector adds the exact supplied high-resolution Visa mark in black/white as appropriate. Card values appear separately in the detail view.

## Gold edit prompt

Mode: built-in image-generation tool, image edit, transparent background. Edit target: normalized black/chrome approved intro face. No CLI or API-key fallback was used.

> Use case: precise-object-edit. Asset: WHOO virtual card front for a mobile card selector. Image 1 is the edit target: the approved black/chrome card extracted from the intro. Change ONLY the black brushed-metal card material to warm premium champagne gold. Keep the large owl artwork, WHOO CARD wordmark, chip and two-line tagline EXACTLY the same shape, scale, position and lettering. The owl and wordmark stay polished silver chrome, the contact chip stays silver. Text must remain exactly WHOO, CARD, Your money., Your business. Preserve the entire landscape 85.60:53.98 face, straight front view, very thin edge, rounded corners, no perspective or rotation, no extra marks or card numbers. Photographic brushed gold and silver reflections, restrained colour, no yellow plastic or flat paint, no deep emboss or added 3D logo thickness. Return one complete card, centered and fully visible on a transparent background with a narrow transparent margin. Do not redesign or move any card element.

## Catalogue behaviour

Plus, Premium and Metal use the supplied activation prices, card-deposit rates/minimums, cashback ranges, limits, allowances and benefits. Empty fee cells display “To be confirmed.” All three show Apple Pay, Google Pay and Visa; Metal additionally lists ATM withdrawals. The prototype's card funding quote uses the supplied activation and deposit values, with activation remembered once per tier. Monthly card limits, cashback payouts and issuer services remain future backend work. The separate wallet withdrawal demonstration retains its previous behaviour.

Saved Disposable / Standard / Platinum selections map to Plus / Premium / Metal respectively, with corresponding artwork. IDs, balances, statuses, historical transactions and intro completion are preserved. Old selection routes remain compatible.

The three images and the final card composites were inspected as assets. Automated interaction/data checks cover swipe selection, fee minimums, one-time activation and saved-state migration. Full mobile browser visual QA is unavailable in this environment.
