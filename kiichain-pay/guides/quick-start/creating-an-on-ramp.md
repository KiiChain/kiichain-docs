---
description: >-
  Move fiat into crypto with KiiChain Pay. Quote a rail, open the on-ramp, have
  the user pay off-platform, and track the activity to completion.
---

# Creating an on-ramp

An **on-ramp** converts **fiat into crypto**. You quote a rail, open the on-ramp, and the user pays fiat off-platform — through a provider checkout URL or by depositing to a set of instructions (a PIX key, a CLABE, a wallet address). There is **no on-chain transaction for you to sign**: once the fiat lands, the provider settles the crypto and the activity moves to `fulfilled`.

## At a glance

<table><thead><tr><th width="200">Property</th><th>Value</th></tr></thead><tbody>
<tr><td><strong>Direction</strong></td><td>Fiat → Crypto</td></tr>
<tr><td><strong>Create endpoint</strong></td><td><code>POST /market/v1/products-providers/{id}/onramp</code> (market module)</td></tr>
<tr><td><strong>User acts</strong></td><td>Off-chain — pays fiat via a URL or deposit instructions</td></tr>
<tr><td><strong>On-chain signing</strong></td><td>None</td></tr>
<tr><td><strong>You need</strong></td><td>A KYC-verified account, an on-ramp <code>products_provider_id</code>, a <code>destination_id</code> (wallet that receives the crypto), and a write-enabled API key</td></tr>
<tr><td><strong>Tracks via</strong></td><td><code>display_status</code> on the activity</td></tr>
</tbody></table>

## Prerequisites

- A KiiChain Pay account that has completed [KYC](../../introduction/kyc.md).
- An [API key](../../introduction/generating-api-keys.md); write calls must be signed (see [Sign write requests](../../introduction/generating-api-keys.md#4.-sign-write-requests)).
- Your `account_id` and a **wallet destination** that will receive the crypto — see [Discovering rails & IDs](../README.md#discovering-rails-and-ids). The examples assume `KII_API_KEY`, `KII_ACCOUNT_ID`, and `KII_DESTINATION_ID` are set.

{% hint style="info" %}
Some providers require their own KYC in certain countries. If so, the create call will tell you — see [Provider KYC / KYB](../../introduction/kyc.md#provider-kyc-kyb).
{% endhint %}

## Step 1 — Get a quote

Find an **on-ramp** rail (a `products-provider` whose `type` is `"onramp"`) and quote it for the **fiat amount** the user wants to spend. For an on-ramp the `amount` is fiat in decimal units.

```bash
curl "https://backend.pay.kiichain.io/market/v1/products-providers/$KII_PP_ID/quote?amount=100&account_id=$KII_ACCOUNT_ID" \
  -H "Authorization: APIKey $KII_API_KEY"
```

The response is a signed `quote` envelope. You pass it back **unchanged** in the next step.

```json
{
  "quote": {
    "quote_payload": {
      "id": "9b2c1d0e-3f4a-5b6c-7d8e-9f0a1b2c3d4e",
      "account_id": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
      "target_id": "7f6e5d4c-3b2a-1c0d-9e8f-7a6b5c4d3e2f",
      "target_type": "onramp",
      "asset_in": { "code": "BRL", "type": "fiat", "amount": "100" },
      "asset_out": { "code": "USDC", "type": "crypto", "amount": "19500000" },
      "product_fee": { "code": "BRL", "type": "fiat", "amount": "1.5" },
      "price": "0.195",
      "expiration_date": "2026-07-15T18:45:00Z",
      "exp": 1784138700
    },
    "signature": "MEUCIQD…"
  }
}
```

{% hint style="warning" %}
Quotes expire (`expiration_date` / `exp`). Create the on-ramp promptly, and request a fresh quote if it lapses.
{% endhint %}

## Step 2 — Create the on-ramp

Send the quote, your `account_id`, and the `destination_id` (the wallet that receives the crypto) to the on-ramp endpoint. This is a **write** request, so it must be signed.

```bash
curl -X POST "https://backend.pay.kiichain.io/market/v1/products-providers/$KII_PP_ID/onramp" \
  -H "Authorization: APIKey $KII_API_KEY" \
  -H "x-timestamp: $KII_TIMESTAMP" \
  -H "x-signature: $KII_SIGNATURE" \
  -H "Content-Type: application/json" \
  -d '{
    "account_id": "'"$KII_ACCOUNT_ID"'",
    "destination_id": "'"$KII_DESTINATION_ID"'",
    "quote": { … the quote object from step 1 … }
  }'
```

The response gives you the new activity's `ticket_id` and **one** of two payment payloads:

**A checkout URL** (`url_payload`) — send the user to a hosted provider flow (e.g. a card checkout):

```json
{
  "ticket_id": "c0ffee00-1234-5678-9abc-def012345678",
  "url_payload": {
    "url": "https://buy.provider.example/session/abc123",
    "expires_at": 1784138700
  }
}
```

**Deposit instructions** (`deposit_payload`) — show the user where to send the fiat:

```json
{
  "ticket_id": "c0ffee00-1234-5678-9abc-def012345678",
  "deposit_payload": {
    "deposit_key": "710969000000431628",
    "deposit_code": "00020126580014br.gov.bcb.pix…"
  }
}
```

`deposit_key` is the rail-agnostic destination (a PIX key, a CLABE, a bank reference); `deposit_code` is an optional copy-and-paste / QR value (for example, a PIX BR Code). Render whichever fields are present.

## Step 3 — The user pays

The user completes payment off-platform — on the checkout URL, or by sending fiat to the deposit instructions. **Nothing to sign on your side.** KiiChain Pay detects the incoming payment and advances the activity through provider processing.

## Step 4 — Track to completion

Poll the activity by its `ticket_id` and watch `display_status`.

```bash
curl "https://backend.pay.kiichain.io/tickets/v1/$KII_TICKET_ID" \
  -H "Authorization: APIKey $KII_API_KEY"
```

```json
{
  "ticket": {
    "id": "c0ffee00-1234-5678-9abc-def012345678",
    "type": "onramp",
    "amount_usd": "19.5",
    "display_status": "processing"
  }
}
```

`display_status` moves `pending` → `processing` → **`fulfilled`** once the provider settles the crypto to the destination wallet. Terminal values are `fulfilled`, `failed`, `canceled`, `refunded`, and `expired`. If you need to re-show the payment instructions while the activity is still open, call `GET /tickets/v1/{ticketId}/pending_user_actions` — for an on-ramp it returns the `url_payload` again.

## Full example

An end-to-end on-ramp with deposit instructions, using the signing helper from [Generating API keys](../../introduction/generating-api-keys.md#reference-implementation) (`kiiFetch` handles the `Authorization`, `x-timestamp` and `x-signature` headers).

```typescript
import { kiiFetch } from "./kii-pay"; // the signed-fetch helper

const ACCOUNT_ID = process.env.KII_ACCOUNT_ID!;
const DESTINATION_ID = process.env.KII_DESTINATION_ID!; // wallet that receives the crypto

// 1 · Find an on-ramp rail (BRL → USDC in this example).
const { products_providers } = await kiiFetch(
  "GET",
  `/market/v1/products-providers?account_id=${ACCOUNT_ID}`,
).then((r) => r.json());

const rail = products_providers.find(
  (pp: any) =>
    pp.type === "onramp" &&
    pp.enabled &&
    pp.fiat_asset.code === "BRL" &&
    pp.product.chain_token?.token.symbol === "USDC",
);
if (!rail) throw new Error("no matching on-ramp rail");

// 2 · Quote it for the fiat amount the user will pay (decimals).
const { quote } = await kiiFetch(
  "GET",
  `/market/v1/products-providers/${rail.id}/quote?amount=100&account_id=${ACCOUNT_ID}`,
).then((r) => r.json());

// 3 · Open the on-ramp.
const created = await kiiFetch(
  "POST",
  `/market/v1/products-providers/${rail.id}/onramp`,
  { account_id: ACCOUNT_ID, destination_id: DESTINATION_ID, quote },
).then((r) => r.json());

const ticketId = created.ticket_id;
if (created.deposit_payload) {
  console.log("Pay to:", created.deposit_payload.deposit_key);
  console.log("Copy-paste / QR:", created.deposit_payload.deposit_code);
} else {
  console.log("Complete payment at:", created.url_payload.url);
}

// 4 · Poll until the activity is terminal.
const TERMINAL = new Set(["fulfilled", "failed", "canceled", "refunded", "expired"]);
let status = "pending";
while (!TERMINAL.has(status)) {
  await new Promise((r) => setTimeout(r, 5000));
  const { ticket } = await kiiFetch("GET", `/tickets/v1/${ticketId}`).then((r) =>
    r.json(),
  );
  status = ticket.display_status;
  console.log("status:", status);
}
console.log(status === "fulfilled" ? "On-ramp complete 🎉" : `Ended as ${status}`);
```

## Related

- [Creating an off-ramp](creating-an-off-ramp.md) — the reverse: crypto → fiat.
- [Guides overview](../README.md#discovering-rails-and-ids) — discovering rails, destinations, and IDs.
- [KYC](../../introduction/kyc.md) — account levels, limits, and provider verification.
