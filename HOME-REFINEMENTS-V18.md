# Revision 20 corrections

- Wallet and card tabs are 60px high, with a bottom-centred downward arrow and no added border or corner radius. Card rows show only the top of the unchanged approved card photo, at its original full width, with no extra label, wordmark, tint, enlargement, or shadow.
- USDT wallet tabs use the supplied official icon’s green (#50af95); other wallet tabs use their own asset colours.
- Home quick actions, their borders and labels, balance text, and bottom navigation use neutral charcoal, grey and white. Their translucent surfaces desaturate the backdrop to prevent the page gradient tinting them.
- The receiving QR is a dedicated white-on-charcoal SVG. It has no colour inversion, teal demo plate or red backing. Only the official coin icon appears in its centre. The separate Tether title wordmark is removed.
- Card quick sheets show PAN/reveal/copy, expiry/copy, CVV/copy, cardholder-name/copy and billing-address/copy for both selected and active sample cards. Selected cards retain a top-up action; live-card controls stay disabled until activation. No financial state changes merely by viewing or copying.
- News and Insights starts one tour when visible, returns to the start and stops. Ordinary vertical scrolling/touch no longer cancels it before it starts; only deliberate horizontal interaction, focus or selection stops the tour. Incomplete tours can restart after a Home re-render. Reduced-motion mode uses discrete steps without smooth animation. Hidden pages pause; navigation cleans up timers.

Verification: existing event/data checks plus regressions for vertical-scroll entry, incomplete-tour remounts, and selected-card sample fields. Browser visual verification is unavailable in this environment.

The earlier revision notes below are historical.

---

# Revision 19 correction

Restored the Home quick-action markup and button styling from revision 17 and removed the revision 18 navbar recolouring. The navbar retains the previous translucent charcoal surface. Removed tinted campaign-image overlays and changed the account-security heading to “Secure Your Account”. The page background gradient remains the revision 18 background. No card artwork, wallet sheets, financial state or carousel behavior changed.

Validation: source comparison against revision 17 for the restored controls, JavaScript syntax and existing prototype behavior checks. Browser visual verification remains unavailable in this environment.

---

# Home refinements — revision 18

The latest supplied references govern this revision. This remains a mobile-only, browser-local design preview. No backend, database, admin panel or provider integration changed.

## Home

- The top glow uses the mint/green range of the supplied dotted-wave references: #68b896 at the top, #274c3e around 38% of the glow, then the normal #0c0f13 app base. The glow is capped at min(430px, 52svh), rather than stretching down long pages.
- The balance starts below a reserved max(88px, safe-area-top + 28px) offset, leaving room for the phone's own status area and cutout. No fake time/signal elements are added.
- The four quick actions use smaller 47px translucent square icon backgrounds with labels below. The Home bottom toolbar is also translucent.
- The thinner reminder is a full-image banner. Setup, recovery, Ledger, card controls, exchange, staking, bills and support share their image/campaign identity with News and Insights. The promoted campaign is omitted from the lower rail; dismissal puts it back there. The next completed demo sign-in rotates to another eligible reminder. Completed setup/recovery campaigns are excluded.
- Wallet and card stack headers use one line. Secondary balance labels and hover instructions are removed. A small plus beside Wallets opens Add wallet while the existing New wallet action remains at the top. Hover/focus or a touch hold still reveals the balance.
- Resources is renamed News and Insights. Every tile has a full-bleed image. The lower clearance is reduced to fit the floating toolbar, without the previous excessive blank area. Swipe, mouse grabbing, arrows and keyboard navigation are retained. The rail waits until visible, tours once, returns to the start and stops; interaction cancels the tour.

## Quick views

The outer sheet now sizes to its content with a maximum height of 78dvh. A fixed header contains a tappable centre handle and X, both of which close the view. Only the inner content area scrolls; there is no fixed empty sheet body extending below the content. Background Home stays visible and inert.

Wallet Receive follows the supplied reference: a Receive [asset] heading, Receive/Send tabs, a large centred QR with the asset's real icon, Network and Available rows, and a full-width address-copy bar. The QR/address remain clearly non-payable demo details. Tether uses the supplied full wordmark and an unchanged source crypto icon. Send switches to the existing native-asset withdrawal form inside the sheet and reviews before any confirmed demo debit. Tapping the wallet title opens its full page.

The card image now spans the sheet's available width. Below it are the compact number/reveal panel, two equal expiry/CVV fields, a billing disclosure with an always-visible copy control, and outlined Lock/Replace controls. Tapping the card opens the full page. The approved card photographs, chip/logo geometry and three intro compositions are byte-for-byte unchanged.

## Assets and image generation

Existing source files are reused without redrawing brand marks:

- `dist/assets/crypto-{btc,eth,usdt,trx,usdc}-source-v18.svg`: unchanged bytes from the supplied `oninee_r3.zip`, originally `oninee_r3/public/assets/images/crypto-<asset>.svg`.
- `dist/assets/tether-wordmark-source-v18.png`: unchanged supplied `logoGreen.png`.
- `dist/assets/insight-abstract-source-v18.png`: unchanged supplied `66304f9b5ce3d054b3c3ea9b_Recent Work -2.png`.
- `dist/assets/insight-mint-flow-v18.png`: a new 1254×1254 bitmap background, produced with the built-in image-generation tool using the two dotted-wave images as palette/style references. It is an original composition; the stock images and their watermarks are not edited or packaged.

Exact generation prompt:

```text
Use case: stylized-concept. Asset type: full-bleed background for a premium mobile finance support tile and account reminder. Create an original high-resolution square abstract image of a softly undulating fabric-like field of tiny luminous mint-green dots, fading into deep black. Reference images are style and palette references only, not edit targets. Match the mint, pale emerald and fresh yellow-green highlights, with occasional cool cyan accents, on a black background. Place the most beautiful flowing wave across the lower and right portions; leave calm near-black negative space in the upper-left for separately rendered white HTML text. The dots should feel finely rendered and three-dimensional, with elegant depth, not noisy neon or a busy futuristic dashboard. Keep the scene edge-to-edge, no inset illustration, no frame, no text, no logos, no UI, no watermark. Create a new composition rather than copying either reference.
```

The Ledger, coin still-life, card-control and payment-device image assets from revision 17 are retained as full-background crops. No new card, owl, payment logo or crypto logo is generated.

## Validation

The event/data harness passes 85 checks over 42 route states, including the existing native wallet quantities/fees, quote expiry and idempotency, plus wallet Send/Receive switching, full-address copying, handle close behavior, single-line stacks, image coverage, campaign promotion/demotion and the one-lap carousel. Approved image and crypto-logo bytes were compared with their sources. The standalone HTML is checked separately before publication.

Full browser visual QA is unavailable in this managed environment. The checks do not establish pixel-level rendering, physical-device gestures or the browser accessibility tree. Review the published phone preview for those details.
