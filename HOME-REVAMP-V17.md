# WHOO Home — revision 17

This revision changes the phone-only Home prototype. The approved intro compositions, three account card faces and native-wallet funding model are retained. All account data and actions remain browser-local examples.

## Layout and interactions

1. Home starts directly with Total balance, including every wallet's estimated USD value and every card balance. Wallet's own total remains crypto-wallet-only. A muted steel-blue glow fades fully into #0c0f13 by min(430px, 52svh), including behind the transparent page top. No greeting, avatar, bell, currency badge, Home corner label or simulated phone status bar is shown.
2. Four square actions: Withdraw, Transfer, New card and New wallet. Withdraw chooses the source wallet; Transfer opens quick wallet access with Send/Receive. A single oblong reminder follows the actions. Its X dismisses it through refresh/navigation for this tab's current login session. A new completed demo login chooses a different eligible message. Setup and recovery are prioritised before informational reminders. The old numbered setup checklist is removed.
3. Wallets and Cards are separate overlapping stacks showing shallow headers. Wallet names, asset colours and card tier/status remain visible. Mouse hover or keyboard focus reveals a balance on the right. On touch/pen, hold for 330ms to peek; release keeps the balance visible briefly without opening the sheet. Moving more than 8px cancels a pending hold so ordinary vertical scrolling stays native. A normal tap opens quick access.
4. Quick access occupies 75dvh and leaves Home/balance visible above it. The card sheet uses the approved photograph, masked sample number/expiry/CVV with reveal/copy controls, copyable sample billing address, Lock/Unlock and Replace. Replacement requires confirmation, records one zero-value pending sample request and moves no money. A draft card instead offers its existing top-up path and no credentials. The wallet sheet shows native quantity, USD estimate, Send/Receive, an illustrative QR and copyable non-payable demo address. Tap the card photograph or wallet header to open the full page. Background content is inert while a dialog is open.
5. Recent activity includes the whole account: all wallet/card movements and non-monetary requests. Specific pages retain their own filters.
6. Resources replaces Home's standalone Ledger banner. Wallet retains its existing three-banner Ledger strip. The global support footer is removed; Support remains in Resources and Profile.

## Resources rail

Two half-width square tiles fit across with a 12px gap. Larger tiles are capped at 75% of the rail, so a neighbouring tile remains visible. All image-based tiles use a full-bleed background, with readable HTML copy rather than baked-in text.

The rail uses native touch swiping and horizontal scroll snapping. Mouse grabbing follows the pointer, snaps on release and suppresses the release click. Small arrows and left/right/Home/End keyboard keys provide additional navigation. When at least part of the rail first enters view on each Home visit, it waits 1.8 seconds, moves through the available positions with 1.65-second reading pauses, returns to the first two default tiles, and stops. It never loops. A touch, mouse drag, wheel, keyboard focus or arrow action stops the tour immediately. Reduced-motion preference disables automatic movement. Leaving Home removes listeners/timers; a hidden document cancels the current tour.

| Tile | Current action | Boundary |
| --- | --- | --- |
| 24/7 help & support | Opens local support chat | Existing browser demo; no message is sent externally |
| Ledger Sync | Opens Coming soon information and an official Ledger website link | No device connection, import or partnership claim |
| Staking | Opens the staking preview | Up to 16% is an illustrative annual rate; not a monthly or guaranteed return. No staking service, asset commitment or accrual is active. Daily interest is proposed copy only. |
| Recovery backup | Opens Profile recovery | Appears as a small tile until promoted to the current reminder; disappears after saved-backup confirmation |
| Currency exchange | Opens an eligible card's existing USDT top-up converter, or card selection if needed | Uses reviewed local sample rates; no ChangeNOW API call |
| Spend controls & approvals | Explains future approval rules and links to an active card's quick controls | Lock/Unlock works in demo state; spending/approval rules are future features |
| Bills, on autopilot | Opens Coming soon information | No mandate or payment is created |

## Artwork and prompt briefs

Mode: built-in image generation/editing. Two 1254×1254 PNGs were copied into the project without altering existing approved assets. These are presentation backgrounds, not functional wallet or payment artwork.

- **`dist/assets/resource-ledger-v17.png`** — compact square adaptation of the existing supplied `dist/assets/ledger-signer-banner-v15.webp`. Prompt brief: preserve the recognisable Ledger hardware, product shapes, screens and polished surfaces; arrange the devices toward the lower-right of a square full-bleed studio photograph, with calm dark negative space at the upper-left for HTML labels. Remove the original advertising headlines, button and coloured text box. Dark charcoal/navy background, subtle reflective surface, high photographic detail. No new written labels, devices or fabricated logos. The original wide banners stay available on Wallet.
- **`dist/assets/resource-coins-v17.png`** — new coin still-life for the staking/exchange tiles. Prompt brief: square full-bleed premium studio photograph, thin polished silver and champagne-gold milled coins in a stack and a few leaning coins, mainly lower-right. Dark charcoal/navy background and tactile reflective surface, realistic metal and fine edge detail, quiet upper-left negative space. No lettering, financial symbols, numbers, brand marks, interface, extra props or plants.

Other tiles reuse `dist/assets/account-plus-v13.png` and `dist/assets/intro-spending-terminal-v10.png` as full-background crops. Support and recovery use the established code-native icon system and restrained gradients. No replacement owl, Visa logo, chip, card geometry or wordmark was generated for this revision.

## Validation and integration

`tests/prototype-checks.cjs` runs 76 event/data checks across 42 route states, including native quantities/fees, source-only debits, idempotency, quote expiry, existing intro/selector behavior, the new holds/sheets, session alert rotation, one-round resource timing, user cancellation and future-feature non-mutation. It can also test the embedded standalone HTML. `VALIDATION.json` records the current result.

Full browser visual QA is unavailable in this managed environment. Automated checks do not establish pixel-level layout, physical touch behavior or accessibility-tree output; review the published phone preview for those. Nothing connects to the existing database, admin panel, ChangeNOW, Ledger or an issuer in this HTML revision. See BACKEND-INTEGRATION.md before conversion.
