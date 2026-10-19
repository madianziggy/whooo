# Mint Home, compact stacks and reference quick views — revision 18

The supplied dotted-wave backgrounds set the mint-green hue for Home's top-only glow. More status/cutout clearance lowers the balance. Four smaller translucent square icon backplates and the floating translucent toolbar retain the existing mobile navigation.

The image-backed compact banner exchanges eligible campaigns with News and Insights; the promoted campaign is removed from the rail until dismissal. Every tile now uses a full-bleed image. The lower toolbar clearance is reduced. Native swipes, mouse dragging and one visibility-triggered tour remain.

The Apple Wallet reference is followed with shallow single-line stack headers, a Wallets plus and no hover instructions. Actual source crypto logo SVGs replace the text symbols. The supplied Tether wordmark is used unchanged.

Quick sheets are content-sized and capped at 78dvh with a fixed close handle/X and one independently scrolling body. Wallet Receive follows the large QR/network/address-copy reference; Send embeds the reviewed native withdrawal form. Card artwork fills the sheet width above compact field panels and outlined controls. Approved card/intro imagery is unchanged. HOME-REFINEMENTS-V18.md records the mapping, asset provenance, image prompt and verification limits.

## Previous revision notes

# Home stacks, quick sheets and Resources — revision 17

The Home page uses one combined all-wallets/all-cards balance, four square quick actions and a restrained steel-blue gradient that reaches the normal #0c0f13 base by min(430px, 52svh). There is no avatar, greeting, bell, currency badge, fake phone chrome or opaque header. The approved card photographs and intro scenes are preserved.

Wallets and Cards are two separate overlapping stacks with shallow visible headers. Asset colours distinguish wallets. Balances appear on mouse hover or a 330ms touch/pen hold; normal taps open a 75dvh quick sheet while leaving the Home balance visible above. Sheets offer relevant copying/actions and a second tap on the wallet header or card photograph opens its full page. Native vertical scrolling cancels a pending hold.

One dismissible oblong reminder replaces the multi-step setup block. A session dismissal survives refresh and navigation; the next completed demo sign-in rotates to another eligible message. Recovery has a compact Resources tile unless it is promoted to the reminder.

Resources replaces the standalone Home Ledger banner and global support footer. Two square tiles fit across; larger tiles occupy at most 75% width. Native swipe, mouse drag, arrows and keyboard are supported. A single visibility-triggered tour reveals all tiles and returns to default. It stops on interaction, page hiding or reduced motion. There is no repeating autoplay. Images fill their tiles edge to edge, with HTML labels over quiet negative space.

Ledger Sync, staking, spending approvals and bill automation remain future-feature previews. The staking rate is explicitly an illustrative annual rate. Existing wallet conversion is still a reviewed browser-local sample. HOME-REVAMP-V17.md contains the asset sources, full prompts and integration notes. Automated event/data checks do not substitute for full browser visual QA, which is unavailable in this managed environment.

## Previous revision notes

# Wallet simplification, top-only fades and account backup — revision 16

The latest reference makes the background boundary explicit: subtle colour at the top fades into the app's normal dark base around halfway down the viewport. All card-flow screens and Wallet use a capped min(430px, 52svh) gradient over #0c0f13, so long pages cannot stretch the colour all the way down. Their panels remain translucent and headers transparent. Earlier full-height colour washes are superseded.

Wallet follows the Ledger reference's balance / three actions / assets / activity hierarchy. Repeated Cards, deposit-log and withdrawal shortcuts are removed. Asset detail retains Receive and Withdraw. A single Add wallet remains beside the asset list. The bottom copy describes the multi-currency account rather than repeating card instructions.

A compact Home reminder links to a dark Profile recovery page. A guarded one-time demo reveal displays twelve ordered example words and explains that this is WHOO account recovery, separate from Ledger. Only setup timestamps persist. The full scope and production boundary are in WALLET-RECOVERY-V16.md.

## Previous revision notes

# Wallets, card-funding sheets and Ledger banners — revision 15

Wallet now contains native crypto rows and their combined estimated USD value, excluding card balances. Adding a wallet selects asset/network; wallet detail offers Receive and Withdraw. The card list stays on Cards. Funding opens as a bottom-sheet-style popup, uses a funded source wallet, fixes the destination to USDT and requires review before confirming the local sample debit. The same subdued charcoal/steel gradient runs behind the header and content.

The first intro background is a targeted built-in image edit: owl artwork is visible on the exposed silver and gold cards behind the black card. The stack remains on its side at the existing size/position. The approved account card faces and other intro scenes are unchanged. INTRO-STACK-V15.md records the exact prompt and sources.

Home and the root Wallet screen end with one compact Ledger carousel using the three user-supplied banners. Original imagery and baked-in button artwork are preserved. Banner links open Ledger's official site; Activate Ledger Sync is marked Coming soon and opens an explanatory preview. No automatic rotation competes with reading; native swipes, small dots and keyboard arrows choose the artwork. Wallet detail, Cards and intro do not show these banners.

Exact native balances use atomic integer strings, and conversion prices are labelled samples. WALLETS-AND-CHANGENOW-V15.md documents the future backend boundary. Full browser visual QA was unavailable; automated checks cover account events, precision, migrations, source-only debits, quote expiry, banners and routes.

## Previous revision notes

# Selector disclosure and dragging — revision 14

The approved card artwork, pricing header, logo tiles and primary feature list remain intact. Below them, section headings sit directly on the continuous page gradient beside relevant shield/card icons. Each section has a translucent rounded two-column comparison panel with two immediately visible rows. A compact native More disclosure shows the number of remaining rows and a down chevron; opening it reveals the rest and changes the label to Less with an up chevron. Section titles are no longer styled as buttons.

The full selector canvas now uses plan-specific gradients behind its transparent header and footer: navy for Plus, steel for Premium and warm charcoal for Metal. Background attachment is local to the scrolling app shell so it continues through the whole content area.

Desktop mouse dragging uses pointer capture after a small horizontal threshold, temporarily disables scroll snapping, follows the pointer and snaps to a card on release. A release click is suppressed so a drag cannot activate a neighbouring card. Touch input retains native scrolling and vertical gestures; keyboard selection remains supported. Small filled triangle arrows beside the dots provide an additional path, with disabled endpoint states. All listeners are removed when leaving the selector.

Full browser visual QA remains unavailable in this environment. Event/data checks cover drag directions, click suppression, cancellation, arrow endpoints, touch pass-through and the existing card/account flows.

## Previous revision notes

# WHOO mobile — account selector, revision 13

## Current account card catalogue

Plus, Premium and Metal replace Disposable, Standard and Platinum. Black/chrome and silver/black faces are direct whole-face normalizations of the intro artwork. Gold/chrome is a material edit of that approved design. All account card views use the same three images with a separate high-resolution Visa mark. No replacement owl or reconstructed wordmark is drawn on the card. The image references and exact generation prompt are in CARD-SELECTOR-V13.md.

The native swipe carousel and visible neighbouring edge are retained. Each selected tier updates its heading, price, logo tiles, benefits, fees and choice. Real Apple Pay, Google Pay and Visa artwork appears on equal white tiles. High-level cashback, spending limits and card allowances remain immediately visible; all supplied benefits and security policies are in an expandable section, with fees in their own section. Missing fee values remain To be confirmed.

The prototype preserves existing local wallet/card data while mapping saved tiers and designs. Activation and card-deposit quotes follow the supplied table. The monthly allowances and cashback are displayed features; they are not a production rewards or billing engine.

## Historical design notes (revisions 1–12)

The following notes describe earlier iterations. The revision-13 account card photographs and feature table above supersede earlier card drawing, materials and pricing notes.

# WHOO mobile — intro refinements, revision 12

The mobile app uses a neutral charcoal interface, translucent controls and photographic backgrounds. Its phone-width layout, browser-local balances and funding flows are preserved.

## Whole-card rotation

The first two complete prior landscape faces are geometrically mapped onto the original on-its-side card planes, with all printed elements locked together. The first stack is raised 220 source pixels above its earlier position to clear the button. Neutral metal colours are retained. CARD-ROTATION-V11.md and CARD-ROTATION-V11.json document this deterministic correction; the version-10 generation notes below are historical.

All three intro headers use the existing owl favicon alone in white. Step three uses four identical white tile containers for Apple Pay, Google Pay, blue Visa and Mastercard. Wordmark paths and source-image pixels retain their geometry; no watermark is removed from the stock reference.

## Full-screen introduction

Every intro is one full-height portrait photograph, absolutely positioned over the entire screen with `object-fit: cover`. It runs behind the header, text, progress and translucent bottom controls. There is no middle illustration container, image mask, top/bottom image seam or separate card overlay. On step three, the requested transaction example sits in the bottom control area, above the progress markers. One heading and a short explanation remain on each page. The two card scenes preserve the original reference poses, with landscape face artwork rotated with each card as it stands on its side. The first scene retains the three-card stack; the phone/card scene is now step two, with a glossy teal display. Step three uses the supplied payment terminals, with an illustrative scan-to-pay screen and the small reader's Revolut name removed.

The three assets and exact built-in image-edit prompts are recorded in INTRO-REFERENCE-EDITS-V10.md. The photographs are reference-based edits; card artwork in a raster edit is not claimed to be pixel-identical to the input. The introduction header uses the existing white favicon owl by itself. Main app headers retain the approved wordmark in whoo-approved-wordmark-v10.svg.

Continue, Back, progress links, Skip intro and horizontal swipes remain available. Swipe direction checks ignore predominantly vertical gestures. Opening the base URL still replays the introduction for review without resetting the stored account.

## Everyday payment examples

Step three shows one compact translucent transaction card at a time: taxi with Uber, hotel with Booking.com, and lunch with Starbucks. Recognisable merchant icons sit beside the merchant name, with the USD amount right-aligned. A CSS-only 10.5-second cycle gives each example a 3.5-second slot, fading and moving it upward. All example text is exposed as one stable accessible description; reduced-motion mode cycles through all three examples with instant changes and no spatial movement. The glass gradient uses approximately 8–10% opacity and 8px blur, so the full-screen photograph remains visible. The heading is “Spend your crypto in dollars.” The smaller copy uses the requested 150 million merchants, Visa acceptance, Apple Pay, Google Pay and global ATM access wording. No balances, cards or transaction records are changed. Short screens can scroll rather than clip the controls.

## Card-selection interaction

The supplied flat card screenshots control this screen's layout and interaction. Card selection is a horizontal scroll-snap carousel, with a visible neighbouring edge as a swipe affordance. The tile width and end padding keep all three cards aligned to the same left inset, including the last card. There are no plan-tab buttons or perspective corner photographs on the selector.

Only the details region below the rail changes during a swipe. The active plan controls its title, payment logos, features, fees, preview and Choose action. Native scrolling updates the route with replaceState so the rail is not rerendered and every swipe does not add a back-history entry. Keyboard left/right, Home and End work; viewport resize realigns the current card. The resize listener is removed when leaving the selector. Horizontal gestures are native; vertical page scrolling is preserved.

Full vector Apple Pay and Google Pay marks and the existing original Visa mark appear above the feature list. Disposable uses Visa online payments alone. Google Pay retains a multicolour G, while the wordmarks use light ink on the dark surface. Sources and adaptation notes are in PAYMENT-MARK-LICENSE.txt.

## Palette

Charcoal, steel grey and off-white form the page backgrounds, panels, controls and typography. Strong teal is confined to small highlights: the central Add money control and active navigation marker, with a small intro-progress accent. The full-screen gradients remain continuous through transparent headers. Neutral ink replaces the large teal wordmarks on black/silver card faces; the bright material option stays available as an individual card design. The user will supply final card art.

## Card construction

Midnight and Night Owl use a separate neutral black-metal photograph, Platinum uses the original silver brushed-metal photograph, and Electric uses a separate reflective teal photograph. All material images render at full opacity with normal compositing; no CSS colour tint or low-opacity blend washes out the surface reflections. The WHOO wordmark and owl are flat SVG ink, with no emboss, bevel, filter or text shadow. The full-body card logo integrates the owl eyes as OO; the header uses the original approved wordmark pixels extracted from the supplied mock-up. The two eye-pattern card designs use the upper owl geometry at a larger scale. The material is separate from the brand and card details, so generated logo shading cannot create a false thick-card effect.

All four designs use the same 856 × 539.8 overlay coordinate system (85.60 × 53.98 card proportions). The supplied 2048 × 2048 card screenshot is measured in CARD-LAYOUT.json. The right-hand card is normalized counterclockwise to landscape. Contact-chip bounds become left 10.7937%, top 34.0604%, width 13.2275%, height 15.2685%. The existing photographic chrome chip is sized to those bounds. The number is moved up into the reference number line and enlarged: Farrington 7B is rendered at an actual 43.2-unit glyph height, fixed 36.3-unit pitch, first character centre 101.8 and baseline 354.8. OCR B supplies the name and expiry at their separately measured positions. The expiry is above the name, below the number. The card selector shows a complete illustrative number so its scale can be reviewed; owned-card faces retain masking. Card values are sample data. These are image-layout measurements, not a production card-manufacturing certification.

Visa is a separate original vector, extracted from the blue Brand Mark in Visa’s January 2026 public physical-card guide. Black/white variants preserve its geometry. Every card uses the lower-right bounds measured from the supplied reference: left 74.3915%, top 83.3893%, width 22.0106%. Black is used on Platinum; white is used on the dark and teal designs. The teal face uses light number printing on its darker right half and light expiry printing, with dark printing over the brighter left half. Positions and glyph dimensions stay fixed. Production issuer approval is outside this prototype.

Contact-location reference: https://downloads.acs.com.hk/technology/462-01-smart-card-technical-introduction.pdf

Visa source: https://corporate.visa.com/content/dam/VCOM/corporate/about-visa/documents/visa-physical-card-brand-standards-jan2026.pdf

## Typography and interaction

Inter is bundled locally for consistent UI rendering. Card numbers use the unmodified Barcodesoft Farrington 7B font (publisher permits website publishing/artwork under its GPL license); cardholder and expiry use the freely distributable OCR B font by Matthew Skala/Norbert Schwarz. Their notices are in CARD-FONT-LICENSE.txt. Revolut’s current official web UI styles use Inter for body/control text and Aeonik Pro for some headings. No licensed Aeonik file was supplied, so this prototype uses Inter throughout; it does not claim exact native-app font identity from screenshots. Source: https://www.revolut.com/

The shared scale is 28px page titles, 20px sections, 15–16px body/control text, 13–14px secondary text and 12px captions. Intro headlines are 39px (37px on narrow/short screens), body 15px, and buttons 17px. The old repeated step label is removed. Text keeps its size on shorter screens; artwork gives up space first, with scrolling available when necessary. Button labels use medium weight. Letter spacing is restrained and consistent.

A continuous charcoal/steel-grey gradient with subtle grain covers the app screens; each introduction page instead has one full-screen photograph. The header is transparent, has no separator or background tile, and scrolls with the content. The content H1 owns the page title; headers do not repeat it. Support is a labelled footer button rather than an anonymous header icon.

Primary controls use quiet translucent neutral fills, fine edges and restrained shadows. Hover and press states do not move or resize them. Card selection uses flat card faces in a native horizontal carousel. Full card views retain native measured overlays. The earlier separate architectural selector image and material-name badges are removed. The original teal WHOO header wordmark has no background tile. Intro captions have no numeric prefix, headings are consistent, and payment marks sit below the step-three description without a separate panel.

## Active assets

| Asset | Role |
| --- | --- |
| `assets/apple-pay-mark-v9.svg`, `assets/google-pay-mark-v9.svg` | Recognisable payment-capability marks beneath the card carousel |
| `assets/card-metal-surface-v4.png` | Opaque silver brushed-metal photograph |
| `assets/card-black-surface-v6.png` | Neutral black metal with silver studio reflections |
| `assets/card-teal-surface-v6.png` | Reflective teal coating with visible studio highlights |
| `assets/ambient-grain-v6.svg` | Subtle monochrome grain over the continuous screen gradient |
| `assets/chip-silver-v4.png` | Shared photographic silver contact module |
| `assets/intro-cards-rotated-v11.png` | Original card-stack pose, with the approved printed owl layout |
| `assets/intro-wallet-card-rotated-v11.png` | Original on-its-side card pose, glossy teal phone and concrete plinth |
| `assets/intro-spending-terminal-v10.png` | Supplied payment terminals, with a payment-ready screen and competitor text removed |
| `assets/whoo-approved-wordmark-v10.svg` | Actual original approved WHOO wordmark pixels extracted onto transparency |
| `assets/owl-stamp-v8.svg` | Shared footless owl stamp |
| `assets/visa-white.svg`, `assets/visa-black.svg` | Original Visa geometry, monochrome |
| `assets/inter-latin.woff2` | Inter variable UI font, SIL Open Font License |

The material sources remain separate assets for the app's card views. The new intro scenes are tall raster photographs; their actual dimensions and source references are recorded in INTRO-REFERENCE-EDITS-V10.md. The terminal screen is illustrative artwork; deposit choices remain USDT and USDC.

Font source/license: https://github.com/rsms/inter

## Verification limits

The review base URL now always opens intro slide one, even with a previously completed local flag. Explicit app routes and returning sign-in retain their existing behavior. No balances or progress are reset.

The interaction/data checks cover 33 route states, including reopening the introduction with existing data, first visit, returning sign-in, deposits, wallet-to-card transfers, fees, withdrawals and persistent local data. JavaScript syntax, asset availability, offline export, SVG structure, CSS delimiters and font identity are checked separately. Full mobile browser visual QA is unavailable in this environment; inspect the live app at 360–430px before approving the visual finish.

Card-font sources: https://github.com/bcssupp0rt/farrington-7B-Font and https://tsukurimashou.org/ocr.php.en
Numeric pitch and allowed card typefaces were cross-checked against ISO/IEC 7811-1:2018, clauses 6 and 7; the visual positions follow the supplied screenshot.

The new black and teal material prompts are in MATERIAL-PROMPTS-V6.md. All photographic material faces are 1581 × 995 pixels, sufficient for the 360–430px app. A source-image review confirms the materials and framing; browser-level visual QA remains unavailable.
