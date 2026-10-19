# Crypto wallets and card funding — revision 15

## Requested account model

Wallet contains separate native crypto wallets, identified by asset and network. The header totals their estimated USD values and excludes card balances. BTC, ETH, USDT, TRX and USDC are preview choices. Asset availability and receiving networks must ultimately come from server/admin configuration.

Adding a wallet starts its balance at zero. Receiving a deposit credits the native wallet without exchanging it. Ledger banner controls are forthcoming placeholders; they do not import wallets or include external Ledger balances in the total.

Cards remain separate. The user chooses a card, selects a funded source wallet in a popup and reviews a conversion to a fixed USDT destination. The prototype treats 1 USDT as 1 USD of card credit solely to demonstrate the requested dollar-spending flow. Confirm the issuer's real funding currency, USDT chain, destination and settlement rules before implementing it.

## Exact preview calculations

- Native balances are unsigned atomic-unit decimal strings: BTC 8 decimals, ETH 18, TRX/USDT/USDC 6. Calculations use BigInt; JSON stores strings.
- USD display prices are illustrative constants: BTC 67,000; ETH 2,400; TRX 0.15; USDT/USDC 1. They are not market data or provider quotes.
- An old version-2 USD sample balance migrates once to USDT/TRC20. History is never replayed as new wallet credit. Pending historical stablecoin deposits get native amounts and their original asset/network destination.
- USDT amount to the card is entered with two decimal places. Existing supplied card activation/deposit fees are added. Required source units round upward to a whole atomic unit.
- A second review step shows source debit, USDT target, card credit and card fees. Confirmation rechecks the exact wallet/card balances and fee state, and rejects quotes older than two minutes. Confirmations are single-use in this browser.
- Only the selected wallet is debited. Card balances stay in USD cents in the current prototype. Total crypto value is derived again after every mutation; it is never an independent balance to spend.
- The wallet-withdrawal preview retains its historical 3% fee, applied in the selected native asset, separate from card-specific fees.
- ChangeNOW/network fees are not fabricated. The interface says they will be included in the live quote. No exchange request, private key, live API credential or real financial operation exists here.

## Backend work for the later integration

The supplied Laravel reference has a USD Account/ledger and assigned WalletAddress combinations. A receiving address is not evidence of an independently accounted native asset balance. The new holding model therefore needs backend asset/network subaccounts and a native-precision ledger, while preserving the existing User, card ownership, admin access and history.

1. Read configured currencies/networks and provision assigned receiving details through the existing wallet/admin services. Persist confirmations and native quantities server-side, idempotently. Replace demo QR/address and preview-confirmation buttons only then.
2. Return live market valuations separately from spendable native quantities. Never let a cached USD total authorise a debit.
3. Store the existing ChangeNOW partner API key on the server. The browser requests a quote for the selected owned wallet and card; the backend validates balances, allowed asset/network pair, limits, issuer destination and exact required fees.
4. Use the official ChangeNOW API documentation for the selected standard/fixed-rate flow. Fetch permitted currencies/pairs, limits and current estimates. Include provider/network/partner fees, expiry, rate changes and any required refund information in the final reviewed quote. If the source is already USDT on the required network, resolve whether a direct transfer suffices rather than forcing a redundant swap.
5. Create a funding operation with an idempotency key and reserve the required native units. Submit the exchange through the backend and track the provider operation. On-chain swaps and issuer loads are asynchronous; show pending, completed, failed and refund states rather than immediately claiming success.
6. Verify settlement before asking the card provider to load the card. Reconcile provider reference, source wallet debit, conversion proceeds, card fees and card credit in auditable ledger entries. Retries/webhooks must not issue or fund a card twice. A failure must reconcile reserved funds and any refund.
7. Preserve authentication, CSRF/session protection, ownership checks and the same admin panel. Apply commercial pricing server-side; the historical controller fee constants differ from the new Plus/Premium/Metal table.

These are integration requirements, not claims that the supplied backend already implements them. Staking remains out of the current mobile navigation.

## Provider and artwork sources

- Official ChangeNOW API overview: https://changenow.io/api
- Official API documentation linked from that page: https://documenter.getpostman.com/view/8180765/SVfTPnM8?version=latest
- Official fee guidance: https://support.changenow.io/hc/en-us/articles/22686447453596-Integration-Commissions-fees-and-payouts
- Original ChangeNOW logo: https://changenow.io/images/press-page/linear-logo-dark.png, linked by https://changenow.io/press. Original image geometry and colours are retained.
- Ledger banner originals: uploaded S1D.webp, A4D.webp, image-1-1024x313.webp. They are copied unchanged to the static assets. Website destination: https://www.ledger.com/. No affiliate identifier or tracking query is added.

## Integration previews

The ChangeNOW logo/attribution shows the intended future exchange provider. Ledger Sync is explicitly marked Coming soon, and its dialog explains that connection/import comes later. Neither control establishes a real provider relationship or changes external account state.
