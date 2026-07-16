---
description: >-
  Move crypto into a bank account with KiiChain Pay. Quote a rail, open the
  off-ramp, execute the on-chain transaction, and track the activity until the
  fiat lands.
---

# Creating an off-ramp

An **off-ramp** converts **crypto into fiat**, paid out to a bank account. Unlike an on-ramp, the user (or your backend, via a delegated wallet) must **execute an on-chain transaction** to move the crypto into settlement. After that, the activity passes an AML check and provider processing before the fiat is sent to the destination bank account.

## At a glance

<table><thead><tr><th width="200">Property</th><th>Value</th></tr></thead><tbody>
<tr><td><strong>Direction</strong></td><td>Crypto → Fiat</td></tr>
<tr><td><strong>Create endpoint</strong></td><td><code>POST /tickets/v1/offramp</code></td></tr>
<tr><td><strong>User acts</strong></td><td>On-chain — executes the returned transaction</td></tr>
<tr><td><strong>On-chain signing</strong></td><td>Delegated Kii Wallet (server-side) or external wallet (self-sign)</td></tr>
<tr><td><strong>You need</strong></td><td>A KYC-verified account, an off-ramp <code>products_provider_id</code>, a <strong>bank</strong> <code>withdraw_destination_id</code>, and a delegated Kii Wallet (for the primary path)</td></tr>
<tr><td><strong>Tracks via</strong></td><td><code>display_status</code> on the activity</td></tr>
</tbody></table>

## Prerequisites

- A KiiChain Pay account that has completed [KYC](../../introduction/kyc.md), with its [Kii Wallet](../../introduction/internal-wallets.md) [delegated](../../introduction/privy-delegated-access.md) if you want KiiChain Pay to sign the on-chain step for you.
- An [API key](../../introduction/generating-api-keys.md) with `tickets.tickets.write` and (for the delegated path) `blockchain.transactions.execute`; write calls must be signed.
- Your `account_id`, your on-chain wallet address, and a **bank withdrawal destination**.

### Set up a bank withdrawal destination

The fiat payout goes to a confirmed **bank** destination. If you don't have one yet, create it (see [Discovering rails & IDs](../README.md#discovering-rails-and-ids) for the full flow):

1. `GET /accounts/v1/rails/schemas?country={country}` — read the bank rail's required `payload` fields.
2. `POST /accounts/v1/users/{userId}/accounts/{accountId}/withdrawal_destinations` — register it with `{ rail_code, rail_version, payload, name }`.
3. `POST …/withdrawal_destinations/{destinationId}:confirm` — confirm with the `verify_code` you receive.

Then list your destinations and pick the `id` of the `"bank"` one — that's your `withdraw_destination_id`. The examples assume `KII_API_KEY`, `KII_ACCOUNT_ID`, `KII_ADDRESS` (your `0x…` wallet address), and `KII_WITHDRAW_DEST_ID` are set.

## Step 1 — Get a quote

Find an **off-ramp** rail (a `products-provider` whose `type` is `"offramp"`) and quote it for the **crypto amount** you want to sell. For an off-ramp the `amount` is crypto in **atoms** (smallest unit).

```bash
# 25 USDC (6 decimals) → 25000000 atoms
curl "https://backend.pay.kiichain.io/market/v1/products-providers/$KII_PP_ID/quote?amount=25000000&account_id=$KII_ACCOUNT_ID" \
  -H "Authorization: APIKey $KII_API_KEY"
```

The response is a signed `quote` envelope with `target_type: "offramp"`; pass it back unchanged in the next step. Quotes expire — check `expiration_date` / `exp`.

## Step 2 — Create the off-ramp

Create the activity with the quote, your `account_id`, `user_chain_address`, and the bank `withdraw_destination_id`. This is a signed **write** request.

```bash
curl -X POST "https://backend.pay.kiichain.io/tickets/v1/offramp" \
  -H "Authorization: APIKey $KII_API_KEY" \
  -H "x-timestamp: $KII_TIMESTAMP" \
  -H "x-signature: $KII_SIGNATURE" \
  -H "Content-Type: application/json" \
  -d '{
    "products_provider_id": "'"$KII_PP_ID"'",
    "account_id": "'"$KII_ACCOUNT_ID"'",
    "user_chain_address": "'"$KII_ADDRESS"'",
    "withdraw_destination_id": "'"$KII_WITHDRAW_DEST_ID"'",
    "quote": { … the quote object from step 1 … }
  }'
```

The response holds the new `ticket` **and** the `transactions` you must execute on-chain to fund the off-ramp:

```json
{
  "ticket": {
    "id": "c0ffee00-1234-5678-9abc-def012345678",
    "type": "offramp",
    "display_status": "pending"
  },
  "transactions": [
    {
      "evm": {
        "type": "kiifulfillment",
        "chain_id": "1336",
        "from": "0x1A2b3C4d5E6f7A8b9C0d1E2f3A4b5C6d7E8f9A0b",
        "to": "0xRouterContractAddress…",
        "value": "0",
        "data": "0xa9059cbb…"
      }
    }
  ]
}
```

{% hint style="info" %}
If the token needs an ERC-20 allowance, an `approval` transaction is prepended to the list. Execute the transactions **in order**.
{% endhint %}

## Step 3 — Execute the transaction

KiiChain Pay does **not** sign for you at create time — the transactions come back unsigned. You execute them one of two ways.

### With a delegated Kii Wallet (recommended)

Hand the returned `transactions` straight to the blockchain execute endpoint. KiiChain Pay signs and broadcasts them from your delegated Kii Wallet, with gas sponsored. This is a signed **write** request.

```bash
curl -X POST "https://backend.pay.kiichain.io/blockchain/v1/transactions/execute" \
  -H "Authorization: APIKey $KII_API_KEY" \
  -H "x-timestamp: $KII_TIMESTAMP" \
  -H "x-signature: $KII_SIGNATURE" \
  -H "Content-Type: application/json" \
  -d '{ "transactions": [ … the transactions from step 2 … ] }'
```

```json
{ "tx_hashes": ["0x9f8e7d6c5b4a…"] }
```

A hash of `"0x00"` in the array means that transaction failed to broadcast.

{% hint style="warning" %}
This path requires a **delegated** Kii Wallet. Without delegation the call errors — see [Privy delegated access](../../introduction/privy-delegated-access.md).
{% endhint %}

### With an external wallet

If the user holds their own keys, don't call KiiChain Pay to sign. Take each `evm` transaction's `chain_id`, `to`, `value`, and `data`, then sign and broadcast it with your own signer (for example, viem's `sendTransaction`). KiiChain Pay observes the on-chain event and advances the activity.

You can re-fetch the outstanding transaction at any time while the activity is open with `GET /tickets/v1/{ticketId}/pending_user_actions` (it returns a `transaction_payload`).

## Step 4 — Track to completion

Poll the activity and watch `display_status`.

```bash
curl "https://backend.pay.kiichain.io/tickets/v1/$KII_TICKET_ID" \
  -H "Authorization: APIKey $KII_API_KEY"
```

After your transaction confirms, the activity runs an AML check, then provider processing, then pays out — `display_status` moves through `processing` to **`fulfilled`** when the fiat is sent to the bank account. If the AML check or provider rejects the transfer, the crypto is returned and the activity ends as **`refunded`** (or `canceled` / `failed`). While the activity is awaiting on-chain confirmation you can cancel it — `GET /tickets/v1/{ticketId}/user_txs` returns a `cancel` transaction when that action is available.

## Full example

End-to-end off-ramp via a delegated Kii Wallet, using the `kiiFetch` signing helper from [Generating API keys](../../introduction/generating-api-keys.md#reference-implementation).

```typescript
import { kiiFetch } from "./kii-pay";

const ACCOUNT_ID = process.env.KII_ACCOUNT_ID!;
const ADDRESS = process.env.KII_ADDRESS!; // your 0x… wallet address
const WITHDRAW_DEST_ID = process.env.KII_WITHDRAW_DEST_ID!; // confirmed bank destination

// 1 · Find an off-ramp rail (USDC → BRL) and quote 25 USDC (atoms).
const { products_providers } = await kiiFetch(
  "GET",
  `/market/v1/products-providers?account_id=${ACCOUNT_ID}`,
).then((r) => r.json());

const rail = products_providers.find(
  (pp: any) =>
    pp.type === "offramp" &&
    pp.enabled &&
    pp.product.chain_token?.token.symbol === "USDC" &&
    pp.fiat_asset.code === "BRL",
);
if (!rail) throw new Error("no matching off-ramp rail");

const { quote } = await kiiFetch(
  "GET",
  `/market/v1/products-providers/${rail.id}/quote?amount=25000000&account_id=${ACCOUNT_ID}`,
).then((r) => r.json());

// 2 · Create the off-ramp — returns the ticket and the tx to execute.
const { ticket, transactions } = await kiiFetch("POST", "/tickets/v1/offramp", {
  products_provider_id: rail.id,
  account_id: ACCOUNT_ID,
  user_chain_address: ADDRESS,
  withdraw_destination_id: WITHDRAW_DEST_ID,
  quote,
}).then((r) => r.json());

// 3 · Execute on-chain from the delegated Kii Wallet.
const { tx_hashes } = await kiiFetch("POST", "/blockchain/v1/transactions/execute", {
  transactions,
}).then((r) => r.json());
console.log("broadcast:", tx_hashes);

// 4 · Poll until terminal.
const TERMINAL = new Set(["fulfilled", "failed", "canceled", "refunded", "expired"]);
let status = ticket.display_status;
while (!TERMINAL.has(status)) {
  await new Promise((r) => setTimeout(r, 5000));
  const res = await kiiFetch("GET", `/tickets/v1/${ticket.id}`).then((r) => r.json());
  status = res.ticket.display_status;
  console.log("status:", status);
}
console.log(status === "fulfilled" ? "Fiat on its way 🎉" : `Ended as ${status}`);
```

## Related

- [Creating an on-ramp](creating-an-on-ramp.md) — the reverse: fiat → crypto.
- [Creating an FX swap](creating-an-fx-swap.md) — same create-and-execute shape, crypto → crypto.
- [Privy delegated access](../../introduction/privy-delegated-access.md) — server-side signing for the on-chain step.
- [Guides overview](../README.md#discovering-rails-and-ids) — discovering rails, destinations, and IDs.
