---
description: >-
  Swap one crypto asset for another as a custodial, tracked KiiChain Pay
  activity. Quote an instrument, open the swap, execute the on-chain
  transaction, and track it to completion.
---

# Creating an FX swap

An **FX swap** exchanges one crypto asset for another as a **custodial, tracked activity**. You quote an **instrument** (a swap pair), open the swap, and execute an on-chain transaction — just like an off-ramp, but with no fiat leg. By default the swapped funds land on the wallet that executes the trade; you can optionally redirect them to a registered destination. Depending on the instrument, the swap either **settles automatically** on-chain or routes through provider settlement.

## At a glance

<table><thead><tr><th width="200">Property</th><th>Value</th></tr></thead><tbody>
<tr><td><strong>Direction</strong></td><td>Crypto → Crypto</td></tr>
<tr><td><strong>Create endpoint</strong></td><td><code>POST /tickets/v1/swap</code></td></tr>
<tr><td><strong>User acts</strong></td><td>On-chain — executes the returned transaction</td></tr>
<tr><td><strong>On-chain signing</strong></td><td>Delegated Kii Wallet (server-side) or external wallet (self-sign)</td></tr>
<tr><td><strong>You need</strong></td><td>A KYC-verified account, an <code>instrument_id</code>, a delegated Kii Wallet (for the primary path), and optionally a <code>withdraw_destination_id</code> to redirect the output</td></tr>
<tr><td><strong>Tracks via</strong></td><td><code>display_status</code> on the activity</td></tr>
</tbody></table>

## Prerequisites

- A KiiChain Pay account that has completed [KYC](../../introduction/kyc.md), with its [Kii Wallet](../../introduction/internal-wallets.md) [delegated](../../introduction/privy-delegated-access.md) for the primary (server-side signing) path.
- An [API key](../../introduction/generating-api-keys.md) with `tickets.tickets.write` and (for the delegated path) `blockchain.transactions.execute`; write calls must be signed.
- Your `account_id`, your on-chain wallet address, and an `instrument_id` — see [Discovering rails & IDs](../README.md#discovering-rails-and-ids). The examples assume `KII_API_KEY`, `KII_ACCOUNT_ID`, `KII_ADDRESS`, and `KII_INSTRUMENT_ID` are set.

## Step 1 — Get a quote

Quote the instrument for the **crypto amount** in **atoms**, and specify a `side` — `buy` or `sell` — relative to the instrument's base asset.

```bash
curl "https://backend.pay.kiichain.io/market/v1/instruments/$KII_INSTRUMENT_ID/quote?amount=25000000&account_id=$KII_ACCOUNT_ID&side=sell" \
  -H "Authorization: APIKey $KII_API_KEY"
```

The response is a signed `quote` envelope with `target_type: "swap"`; pass it back unchanged. Quotes expire — check `expiration_date` / `exp`.

{% hint style="info" %}
An instrument has a `product_base` (input) and `product_quote` (output). Use `GET /market/v1/instruments/{id}/limits?side=sell` to read `min_base_amount` / `max_base_amount` before quoting.
{% endhint %}

## Step 2 — Create the swap

Create the activity with the quote, your `account_id`, and `user_chain_address`. This is a signed **write** request.

```bash
curl -X POST "https://backend.pay.kiichain.io/tickets/v1/swap" \
  -H "Authorization: APIKey $KII_API_KEY" \
  -H "x-timestamp: $KII_TIMESTAMP" \
  -H "x-signature: $KII_SIGNATURE" \
  -H "Content-Type: application/json" \
  -d '{
    "instrument_id": "'"$KII_INSTRUMENT_ID"'",
    "account_id": "'"$KII_ACCOUNT_ID"'",
    "user_chain_address": "'"$KII_ADDRESS"'",
    "quote": { … the quote object from step 1 … }
  }'
```

{% hint style="info" %}
**Where the swapped funds land.** By default the output asset goes to the wallet that executes the transaction (`user_chain_address`). To send it somewhere else, add an optional `withdraw_destination_id` — the `id` of a registered [withdrawal destination](../README.md#discovering-rails-and-ids) — and the funds settle there instead, regardless of which wallet executed the trade.
{% endhint %}

The response holds the new `ticket` and the `transactions` to execute on-chain:

```json
{
  "ticket": {
    "id": "c0ffee00-1234-5678-9abc-def012345678",
    "type": "swap",
    "display_status": "pending"
  },
  "transactions": [
    {
      "evm": {
        "type": "kiisettlement",
        "chain_id": "1336",
        "from": "0x1A2b3C4d5E6f7A8b9C0d1E2f3A4b5C6d7E8f9A0b",
        "to": "0xSettlementContractAddress…",
        "value": "0",
        "data": "0x38ed1739…"
      }
    }
  ]
}
```

As with off-ramp, an `approval` transaction is prepended when the token needs an ERC-20 allowance — execute the list **in order**.

## Step 3 — Execute the transaction

The transactions come back unsigned; execute them one of two ways (same as an off-ramp).

### With a delegated Kii Wallet (recommended)

```bash
curl -X POST "https://backend.pay.kiichain.io/blockchain/v1/transactions/execute" \
  -H "Authorization: APIKey $KII_API_KEY" \
  -H "x-timestamp: $KII_TIMESTAMP" \
  -H "x-signature: $KII_SIGNATURE" \
  -H "Content-Type: application/json" \
  -d '{ "transactions": [ … the transactions from step 2 … ] }'
```

KiiChain Pay signs and broadcasts from your delegated Kii Wallet (gas sponsored) and returns `{ "tx_hashes": [...] }`. A `"0x00"` entry means that transaction failed.

### With an external wallet

Sign and broadcast each `evm` transaction (`chain_id`, `to`, `value`, `data`) yourself. Re-fetch the outstanding transaction any time with `GET /tickets/v1/{ticketId}/pending_user_actions`.

## Step 4 — Track to completion

Poll the activity and watch `display_status`.

```bash
curl "https://backend.pay.kiichain.io/tickets/v1/$KII_TICKET_ID" \
  -H "Authorization: APIKey $KII_API_KEY"
```

After your transaction confirms, one of two things happens:

- **Auto-fulfillment** — if the settlement contract fills the swap directly, the activity goes straight to **`fulfilled`**.
- **Provider settlement** — otherwise it routes through provider processing (`processing`) before reaching **`fulfilled`**.

Terminal values are `fulfilled`, `failed`, `canceled`, `refunded`, and `expired`; a failed settlement returns your funds as `refunded`.

## Full example

End-to-end custodial swap via a delegated Kii Wallet, using the `kiiFetch` signing helper from [Generating API keys](../../introduction/generating-api-keys.md#reference-implementation).

```typescript
import { kiiFetch } from "./kii-pay";

const ACCOUNT_ID = process.env.KII_ACCOUNT_ID!;
const ADDRESS = process.env.KII_ADDRESS!;
const INSTRUMENT_ID = process.env.KII_INSTRUMENT_ID!;

// 1 · Quote the instrument (sell 25 units of the base asset, in atoms).
const { quote } = await kiiFetch(
  "GET",
  `/market/v1/instruments/${INSTRUMENT_ID}/quote?amount=25000000&account_id=${ACCOUNT_ID}&side=sell`,
).then((r) => r.json());

// 2 · Create the swap — returns the ticket and the tx to execute.
const { ticket, transactions } = await kiiFetch("POST", "/tickets/v1/swap", {
  instrument_id: INSTRUMENT_ID,
  account_id: ACCOUNT_ID,
  user_chain_address: ADDRESS,
  quote,
}).then((r) => r.json());

// 3 · Execute on-chain from the delegated Kii Wallet.
const { tx_hashes } = await kiiFetch(
  "POST",
  "/blockchain/v1/transactions/execute",
  {
    transactions,
  },
).then((r) => r.json());
console.log("broadcast:", tx_hashes);

// 4 · Poll until terminal.
const TERMINAL = new Set([
  "fulfilled",
  "failed",
  "canceled",
  "refunded",
  "expired",
]);
let status = ticket.display_status;
while (!TERMINAL.has(status)) {
  await new Promise((r) => setTimeout(r, 5000));
  const res = await kiiFetch("GET", `/tickets/v1/${ticket.id}`).then((r) =>
    r.json(),
  );
  status = res.ticket.display_status;
  console.log("status:", status);
}
console.log(status === "fulfilled" ? "Swap complete 🎉" : `Ended as ${status}`);
```

## Related

- [Creating a DEX swap](creating-a-dex-swap.md) — the permissionless, on-chain alternative (no activity).
- [Creating an off-ramp](creating-an-off-ramp.md) — same create-and-execute shape, crypto → fiat.
- [Privy delegated access](../../introduction/privy-delegated-access.md) — server-side signing for the on-chain step.
- [Guides overview](../README.md#discovering-rails-and-ids) — discovering instruments and IDs.
