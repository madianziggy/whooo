# Integration map — supplied oninee_r3.zip

## Current quick-view refinement — revision 18

Home and wallet/card quick views have a new layout only. Receive uses the same non-payable example address/QR. Send in a wallet sheet submits the existing native withdrawal review path with an explicit asset/network wallet ID; the preview performs no debit before confirmation. Real address assignment, QR content and minimum/provider terms must come from the server. Actual crypto logo artwork is reused from the supplied backend assets.

Eligible reminders and News and Insights share campaign IDs and image assets. A promoted reminder is removed from the lower rail while shown, and returns after session dismissal. Retain the existing planned server-side session/eligibility behavior from revision 17. No backend/database/admin changes are made here.

## Current Home presentation — revision 17

Home's total is the estimated USD value of **all native asset/network wallets plus all card balances**. Wallet's total still excludes cards. Use one consistent server valuation snapshot and count each holding once; a pending conversion/top-up must not appear simultaneously as both available wallet funds and settled card credit.

Home quick sheets reuse the authenticated wallet/card identities. Copyable PAN/CVV/billing and lock/replacement actions must come from the authorized issuer path after integration. The prototype displays only sample credentials and non-payable wallet details. Replacement is a local confirmed request with a zero-value pending activity entry; no live replacement, fee or new PAN is produced. Reconcile real replacement capability, authentication and fees with the provider before connecting it.

Store the dismissible alert per authenticated login session; choose the next eligible reminder on a new login and derive setup/recovery eligibility from server records. The prototype uses sessionStorage for dismissal and localStorage for rotation metadata. Account-wide activity spans all wallets/cards; specific pages retain their existing filters.

The Resources rail is presentation only. Staking's 16% is an illustrative annual rate, with daily payout copy only a planned feature; no deposit, accrual, locking or withdrawal engine is implemented. Ledger Sync, automated bills, spend approval rules and general wallet exchange remain future integrations. The exchange tile currently opens the existing card top-up converter. Support opens the existing local chat preview. Keep admin/database changes outside this HTML prototype. See HOME-REVAMP-V17.md.

## Current recovery preview — revision 16

Home and Profile expose a proposed twelve-word WHOO account recovery setup. The sample words cannot recover accounts. The supplied Laravel authentication does not implement this credential; add authenticated enrollment, random server generation, hashed verification, atomic one-time disclosure/consumption, throttled recovery and appropriate session/notification handling later. Do not reuse or request a Ledger recovery phrase. See WALLET-RECOVERY-V16.md. No backend or database changes have been applied.

## Current wallet model — revision 15

The UI now holds BTC, ETH, USDT, TRX and USDC in distinct native asset/network wallets and totals their estimated USD values. Cards are funded from a selected wallet through a fixed-USDT conversion preview. The original backend map below describes the supplied USD Account design; it does not already implement these native subaccounts or ChangeNOW settlement. Keep the existing user/admin/card identity while adapting the ledger, receiving and funding paths during integration. See WALLETS-AND-CHANGENOW-V15.md for the exact prototype assumptions and integration work. No backend or database was changed.

Ledger banners are forthcoming-feature previews only. They open the official Ledger site or a Coming soon dialog; there is no device connection, wallet import or new external balance.

## Historical supplied-route reference

This mobile-only prototype is a new presentation layer. The desktop dashboard is a separate project. The authoritative reference for this map is `oninee_r3/routes/web.php`, `app/Http/Controllers/PortalController.php`, `AuthController.php` and the supplied models. The archive is not deployed or modified.

## Retained flows

| Prototype screen | Existing Laravel route / action | Existing data and integration notes |
| --- | --- | --- |
| Home / Wallet | `GET /dashboard` → `dashboard` | USD `Account`, recent `LedgerEntry`, `VirtualCard` and confirmed `Deposit`. The supplied backend exposes a USD Account. Revision 15 proposes native asset/network subaccounts; reconcile this explicitly during integration. |
| Add money: amount | `POST /deposit` → `depositStart` | `amount`, minimum 10; session draft and reference. |
| Add money: crypto/network | `GET /deposit/form` → `depositForm`; `POST /deposit/form` → `depositCreate` | `asset`, `network`, `amount`. Replace preview choices with active `WalletAddress` combinations from the admin panel. Reuse existing assigned address selection. |
| Deposit payment | `GET /deposit/{id}` → `depositShow` | Use the real wallet address and genuine payment QR only after integration. The current QR is an illustration. |
| Deposit status | `GET /deposit/{id}/status` → `depositStatus` | Poll status/confirmations. Remove the preview payment-confirmation button. Credit through existing webhook/admin and ledger paths, not in the frontend. |
| Deposit logs | `GET /deposit-logs` → `depositLogs` | Existing deposit records and pagination. |
| Your cards | `GET /cards` → `cards` | Existing `VirtualCard` records and monthly ledger activity. |
| Choose design / create | `GET /cards/create` → `cardCreate`; `POST /cards` → `cardStore` | Existing required fields: `holder_name`, `country`, `email`, `amount`; optional `wallet_support`. Minimum first load 10. Issue 5 + funding 4% + processing 1. |
| Card details | `GET /cards/{card}` → `cardShow` | Preserve user ownership and the existing card/ledger relationship. Use provider-authorized card detail handling, never prototype details. |
| Card top-up | `GET /cards/{card}/fund` → `cardFundPage`; `POST /cards/{card}/fund` → `cardFund` | `amount`, minimum 1. Existing debit is amount + 4% + 1. |
| Freeze / unfreeze | `POST /cards/{card}/toggle` → `cardToggle` | Preserve existing `active` / `frozen` state and provider implementation. |
| Withdraw | `GET /withdraw` → `withdraw`; `POST /withdraw` → `withdrawStore` | `asset`, `network`, `amount`, `address`. Minimum 10. Debit gross wallet amount, retain 3% fee, store net amount and pending request. |
| Withdrawal history | `GET /withdraw/history` → `withdrawHistory` | Existing `Withdrawal` records. |
| Activity | `GET /history` → `history` | Existing `LedgerEntry` records; map source reference types to simplified filters. Preserve pagination. |
| CSV export | `GET /statement.csv` → `statementCsv` | Use the existing authenticated CSV response. Prototype export is local sample data. |
| Profile | `GET /profile` → `profile`; `PATCH /profile` → `profileSave` | Existing required `name` and `email`, optional address fields. The preview phone field is a proposed UI field; confirm storage/auth support before integrating it. |
| Referrals | `GET /referrals` → `referrals` | Existing referral code, registration link and `Referral` records. Replace all sample metrics with stored values. Preserve `?ref=` attribution at registration. |
| Support chat overlay | `GET /live-chat/messages` → `chatMessages`; `POST /live-chat` → `chatSend` | Existing `ChatConversation` and `ChatMessage`, same admin chats panel. Add JSON responses if needed for the overlay. |
| Security PIN | `POST /settings/pin` → `securityPin` | Existing `type` (`auth` or `transaction`) and `pin`; source permits 4–8 digits. The preview accepts four digits and stores no PIN. |

## Authentication requires a later change

The supplied `AuthController` still uses email/password login and requires name, email, password and password confirmation at registration. It does not implement phone/passwordless login, OTP, Google or Apple OAuth.

The requested simple email/phone signup is therefore presented as a visual flow only. During integration, add the chosen verified authentication methods, provider credentials, rate limits and session handling while preserving the existing `User` identity and admin access. No authentication migration has been applied here. Phone-only users will also need an email before using the current card-creation action, unless that action is deliberately adapted.

## Current catalogue — revision 13

The current UI offers Plus, Premium and Metal, each with its fixed black/chrome, silver/black or gold/chrome face. The uploaded feature table is preserved in references/account-cards-v13/FEATURES.md. The native mobile selector remains a horizontal swipe carousel.

The prototype uses one-time activation prices of $49.99, $99.99 and $299.99; card-deposit fees are 3% (minimum $5), 0.75% (minimum $0) and 0% respectively. Activation is remembered once per tier in local demo state. Backend integration must implement and validate this new catalogue server-side; the old controller prices in the integration map above are historical reference values and are not automatically compatible with this new offer.

All three tiers advertise Apple Pay/Google Pay. Only Metal lists ATM cash access in the supplied table. Premium's withdrawal, transaction and decline fees are specified; the other blank fields remain unconfirmed. Cashback, free monthly card allowances, referral rewards and provider controls require their actual backend/provider implementation. The existing wallet-withdrawal flow remains separate from tier-specific card fees. No backend was modified by this UI change.

## Omitted from the mobile navigation

Staking and staking forms, prepaid cards, gift cards, eSIMs, product catalogue, invoice collection/payment links, team management and support tickets are omitted. The prototype does not delete their routes or historical database records. The shared admin panel can remain in place.

## Conversion approach

1. Approve the mobile screens, card designs and terminology in this HTML prototype.
2. Convert the shared shell and screens into Blade partials/views and reconnect the routes above, including CSRF and method handling.
3. Replace local sample state with controller data, keeping all balance changes server-side in the existing ledger flow.
4. Complete the chosen authentication methods and real card-provider configuration, then test real authenticated workflows in a staging environment.
5. Add the selected app delivery approach after the web experience is settled.

## Revision 2: first-login setup and three card plans

The new flow is first login → three-slide intro → card selection → secure wallet → deposit → keep funds or choose a card → review and fund card → Home.

### First-login state

The HTML prototype stores `onboardingCompleted` in local browser state. During Laravel integration, replace this with a persistent **per-user** completion value, for example an existing preference/metadata field or an explicitly approved `onboarding_completed_at` field. It must survive sign-out and work across devices. Do not reset it on every session. The Profile replay link must not clear completion or financial state.

Derive the current single Home setup reminder from actual records: selected plan, confirmed deposit and funded/issued virtual card. Returning users land on the mobile Home screen; unfinished users can continue from the reminder. The historical multi-step checklist is superseded by revision 17. The desktop dashboard is a separate interface.

### Selection versus issuance

Selecting a plan in the prototype creates a **draft selection** with zero card balance and `selected` presentation status. It does not debit the wallet. This state is not an instruction to immediately create a real `VirtualCard` in the existing database.

The existing `cardStore` action requires an initial amount and cardholder fields and immediately charges its issue/load fees. To preserve this behaviour, retain a plan selection in the user's session/preferences until first funding. The first confirmed move to that draft should call the existing issuance path; later moves to an issued card use `cardFund`. Map the provider's actual state to the UI. Do not expose a usable PAN, CVV or wallet provisioning action while the card is only a draft.

Existing required cardholder fields must still be collected or validated before real issuance, particularly an email for phone-only registrations. The HTML selection screen deliberately does not imply that the current controller already accepts only a plan ID.

### Historical plans (revision 2; superseded by revision 13 above)

The old controller implements one demo virtual card product. The new **Disposable**, **Standard** and **Platinum** options are a proposed catalogue in `app.js`.

- Standard preview pricing follows the supplied controller: first load = amount + $5 + 4% + $1; later load = amount + 4% + $1.
- Disposable and Platinum issue/funding fees are null placeholders. The UI displays "To be confirmed" and does not deduct sample fees for those plans. Do not copy this no-fee demo behaviour into a live controller.
- The proposed Platinum 10% cashback, lower fees and wallet support require actual product/provider terms. No cashback ledger or real reward processing is implemented here.
- Disposable auto-retirement after one successful purchase requires provider capability or a deliberate server-side implementation. The prototype does not simulate purchases or claim the old controller already implements that lifecycle.

### Deposit completion

The historical supplied implementation credits a USD wallet. In revision 15, deposits must instead credit the selected native asset/network subaccount once through a server ledger/webhook path. It must not automatically fund a card. Show the confirmed wallet balance, "Keep it in my wallet" and the user's eligible card destinations. A subsequent move is a separate reviewed, authenticated operation with fees shown first.

Use the real card selection and wallet balances from the server. Preserve the existing authenticated ownership checks and apply server-side idempotency to deposit confirmation and card funding. The local preview's calculations are not the source of truth for live balances.

### Digital wallet handoff

The prototype shows Apple Wallet / Google Wallet entry points only for Standard and Platinum after the sample card is funded. They open explanatory preview dialogs and do not provision a payment token. Actual support requires an eligible card product, issuer/network enablement and supported countries/devices.

### Design research references

- Revolut virtual cards: https://www.revolut.com/cards/virtual-card/ — distinguishes disposable online cards from reusable cards for recurring and contactless payments, and places card controls next to the selected card.
- Apple Pay setup: https://support.apple.com/en-us/108398 — requires a supported card from a participating issuer; issuer verification may be part of adding the card.

These references inform the proposed UI. They do not establish WHOO's issuer capabilities or commercial benefits.
