# Wallet, top-only gradients and recovery setup — revision 16

## Wallet layout

The first uploaded Ledger reference (`first-step.webp`) informs the structure, not the image content: total balance, one Transfer / Swap / Buy action row, asset wallets, then recent activity. Add wallet appears once beside the asset heading. The root Wallet no longer repeats Cards, Deposit logs or Withdrawal shortcuts. Each asset opens its own Receive / Withdraw view; no extra card shortcut is inserted there either.

Transfer opens the wallet picker, then the selected wallet's existing receiving/withdrawal controls. Buy and general wallet-to-wallet Swap are future-flow previews and say so when opened. They do not perform purchases, swaps or balance mutations. The existing working sample card top-up popup remains separate on Cards.

Wallet recent activity combines native wallet deposits, withdrawals and card-funding debits. The card balances remain outside the total crypto value. The small Ledger carousel stays at the bottom of Home and Wallet.

## Gradient reference and correction

`got-access-to-revolut-v0-2s1q7h50meug1(3).webp` and the repeated `(4)` reference control the background finish. Only their muted top colour is reproduced in CSS. No Revolut photograph, card or screenshot is used as an app background.

Wallet and all card-flow screens share the same normal dark base, #0c0f13. A subtle tinted gradient is confined to the top **min(430px, 52svh)** of the page. It fades entirely into that base around halfway down the viewport. The gradient's dimensions do not grow when the content or an accordion becomes taller. The rest of the page remains the base dark colour. Plus has a restrained slate-blue top, Premium a muted steel-green top, and Metal a desaturated champagne-grey top; they are not fully blue/green/gold pages. The header shares the canvas without an opaque strip. Panels use low-opacity fills and thin edges so the top gradient can show through.

## WHOO account backup preview

The uploaded MetaMask screenshot (`asset_4787030390301A.png`) informs a dark, compact recovery layout. This feature is explicitly for the WHOO account and not a Ledger wallet, hardware seed or cryptocurrency key.

Home shows a small Create your backup recovery phrase prompt. Profile has a Recovery phrase setting with setup status. The flow requires the one-time-view acknowledgement, shows twelve numbered **synthetic example words**, asks the user to write them down securely and confirms the saved-backup status. The page prominently separates WHOO recovery from Ledger recovery.

Only reveal/confirmation timestamps enter saved browser state; the example words do not. Reveal progress must be saved before the words appear. A blocked storage write prevents reveal. Leaving the route, reloading or leaving the document removes the displayed list. Reopening the setting shows Already shown once or Backup saved, without another reveal control. A repeated reveal event does not clear the currently visible list. Existing backup progress from another preview tab is respected.

This is a visual and interaction prototype, **not live account recovery**. The example phrase is public demo copy and cannot authenticate or recover any account. Browser flags are not an enforceable security boundary. Reset demo clears the example setup state, just as it clears sample balances. No real secret is generated, collected, copied, logged, exported, transmitted or changed on a server.

## Required later backend integration

A production recovery credential must be independent of Ledger's recovery phrase and every wallet's signing keys. Require recent authenticated enrollment, generate a high-entropy random WHOO credential on the server, encode it in the approved twelve-word format, and send it through the authenticated protected channel. Store only its secure verifier plus enrollment/use metadata. Enforce first disclosure and subsequent consumption atomically on the server across devices. Exclude plaintext secrets from browser persistence, caches, logs, analytics, screenshots and exports.

On recovery, throttle attempts, validate the saved credential, apply the required account-assurance checks, revoke/replace the consumed credential, invalidate affected sessions and notify the account owner. The exact account recovery policy and credential scheme remain backend work. After reauthentication, a lost or consumed code may be replaced by a **new** code; previously disclosed words are never fetched for redisplay. Handle interrupted enrollment explicitly rather than relying on frontend flags.

Primary references reviewed:

- NIST SP 800-63B-4, Account Recovery / Saved Recovery Codes: https://pages.nist.gov/800-63-4/sp800-63b/events/
- NIST SP 800-63B-4, Look-Up Secret Verifiers: https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
- OWASP Forgot Password Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html

The application is not claimed to satisfy a NIST assurance level. The references guide later implementation, not a certification of this HTML preview.

## Verification

Event/data checks cover one-time disclosure, twelve-word count, acknowledgement, storage failure, repeat submissions, navigation/reload/page-cache handling, saved progress, financial-state preservation and existing native wallet/card operations. Full mobile browser visual QA was unavailable in the managed environment. The live review URL and offline HTML are provided for layout review.
