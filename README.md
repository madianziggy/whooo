# Revision 20 update

Original card-top crops with centred arrows; native wallet colours; neutral controls and text; white receiving QR; copyable card details including cardholder name; repaired single-lap Insights tour.

# Revision 19 update

Home action buttons and navbar restored to their previous styling. Removed tinted campaign-image overlays and simplified the recovery heading to “Secure Your Account”.

# WHOO Card — mobile prototype, revision 18

A phone-only HTML design preview. Open the live review URL or the self-contained `WHOO-Card-Mobile.html`. It runs without a build or backend. All balances, deposits, card details, exchanges and withdrawals are browser-local samples.

## Current flow

1. Three-screen intro → swipe between Plus, Premium and Metal → select a card.
2. Home shows the combined estimated USD value of all wallets **and cards**, four square quick actions, shallow overlapping wallet/card stacks, account-wide activity and Resources. Hover or hold a stack header to peek at a balance; tap for a three-quarter-height quick sheet and tap its artwork/header for the full detail page.
3. Wallet shows the combined estimated USD value of the user's crypto wallets. Card balances are separate and are excluded from this total.
4. Wallet uses a compact Transfer / Swap / Buy row. Transfer chooses an asset; Receive and Withdraw are inside that asset. Buy and general wallet Swap are future-flow previews. Add a Bitcoin, Ethereum, Tether, TRON or USD Coin wallet and choose its network. Wallet rows show native quantities and estimated USD values. Different networks have separate wallets.
5. Receive crypto into a selected wallet without converting it. The non-payable demo address and illustrative QR cannot receive funds; Preview crypto received credits the selected sample wallet once.
6. In Cards, choose Top up. A popup lets the user select a funded wallet, enter the USDT amount, review source crypto, card activation/deposit fees and card credit, then confirm a demo top-up.
7. Only the quoted native amount leaves the selected wallet. Other wallets retain their original currency. The destination funding currency is always USDT; the preview models card credit at 1 USDT = 1 USD.
8. Native withdrawals, card controls, activity, deposit logs, profile and local support chat remain available.

ChangeNOW quotes are **not connected**. Clearly labelled sample prices drive the HTML flow, with no API key or network operations. Provider/network fees, live prices, pair availability, settlement and card-provider funding are deferred to backend integration. `WALLETS-AND-CHANGENOW-V15.md` explains the boundary and integration work.

## Current Home updates

Home uses the mint-green range from the supplied dotted-wave references, fading fully to dark around halfway down the viewport. The balance sits lower beneath the phone's own status/cutout area. Four smaller translucent square icon buttons provide Withdraw, Transfer, New card and New wallet. Wallet/card stacks use one-line headers, real crypto source logos and hidden-until-peek balances; a small Wallets plus opens Add wallet. Hover instructions are removed.

The thinner image banner and **News and Insights** rail share eligible campaigns. The promoted item moves out of the rail and returns after dismissal. Every lower tile has a full-image background. The rail performs one visible tour, returns to default and stops, with native swiping, mouse grabbing, arrows and keyboard access. Lower spacing now clears the translucent toolbar without the previous excess gap. Dismissal still lasts until the next demo sign-in, which chooses a different eligible reminder.

Wallet and card quick views size to their contents, cap at 78dvh and scroll only inside their content region. Both the centre handle and X close them. Receive uses a large centred QR, network/available rows and a full-width copy bar; Send uses the existing reviewed native withdrawal flow. The card fills the available sheet width above compact number/reveal, expiry/CVV, billing-copy and Lock/Replace controls. All details remain samples. Read `HOME-REFINEMENTS-V18.md` for reference mapping and image provenance.

Staking, Ledger Sync, spend approvals and bill automation remain future-feature previews. The displayed 16% is an illustrative **annual** rate, not a monthly or guaranteed return. No staking or payment service is connected.

## Retained Wallet and recovery updates

Wallet and card pages use a subtle coloured glow at the top, fading fully to the normal dark app background by roughly halfway down the viewport. The fade has a capped height instead of stretching with long page content. Panels are translucent. The Wallet layout keeps only the total, three actions, assets, combined recent activity, a short multi-currency-account caption and the existing small Ledger banner.

Home and Profile link to the recovery setup in Profile. Its dark page explains the WHOO/Ledger distinction, requires acknowledgement, reveals twelve numbered example words once and records the saved-backup status. The example cannot recover an account. Only progress metadata is saved; no real credential is generated or handled. Read `WALLET-RECOVERY-V16.md` for scope and future server requirements.

## Retained visual updates

The first intro stack now has black owl artwork on the exposed silver card and chrome owl artwork on the exposed gold card. It remains a landscape-card stack rotated onto its side. The other intro backgrounds and approved account card faces are preserved. The source images and exact built-in image editing prompt are in `INTRO-STACK-V15.md`.

A small three-banner Ledger carousel remains at the bottom of Wallet. Home now uses the compact Ledger tile in Resources. It uses the three supplied images unchanged, preserving Ledger's device pictures and shop artwork. The images open the official Ledger website in a new tab. Activate Ledger Sync opens a **coming-soon preview** and does not connect a device or import balances. This is not a claim of an active Ledger integration or partnership. Banner swiping, dots and keyboard arrows are supported.

The existing continuous gradients, phone-width shell, translucent controls, card-selection drag/swipe rail and expandable benefits/fees are retained. Strong teal remains restrained.

## Saved demo data

Revision 15 migrates the old sample USD wallet to a USDT/TRC20 wallet once. Card IDs, balances, statuses, transaction history, messages, plan activation and intro completion are preserved. Existing pending stablecoin deposits retain their amounts and networks. Native balances are integer atomic-unit strings, including all 18 ETH decimal places; no floating-point arithmetic changes those quantities.

The base review URL replays the intro for review without resetting account data. Profile → Getting started also replays it. Returning sign-in honours the stored completion flag. Reset demo intentionally starts over.

## Verification

Run `node tests/prototype-checks.cjs` from the editable package, or `node tests/prototype-checks.cjs WHOO-Card-Mobile.html` to check the standalone copy. The harness verifies events and data, not browser layout.

## Files

- `WHOO-Card-Mobile.html`: standalone offline copy with embedded images/fonts.
- `index.html`, `app.js`, `styles.css`, `finish.css`, `assets/`: editable static source.
- `BACKEND-INTEGRATION.md`: existing Laravel routes and differences to resolve.
- `HOME-REFINEMENTS-V18.md`: current Home, source logos, reference sheets, campaigns and exact image prompt.
- `HOME-REVAMP-V17.md`: previous Home implementation and image prompts.
- `WALLET-RECOVERY-V16.md`: current wallet layout, top-only gradients and account recovery preview.
- `WALLETS-AND-CHANGENOW-V15.md`: current wallet model, conversion preview and later integration.
- `INTRO-STACK-V15.md`, `CARD-SELECTOR-V13.md` and prior notes: artwork provenance and prompts.
- `VALIDATION.json`: automated event/data, route and asset verification. Full browser visual QA was unavailable in this environment.

The prototype changes presentation and local sample state only. The supplied backend/database/admin panel has not been modified.
