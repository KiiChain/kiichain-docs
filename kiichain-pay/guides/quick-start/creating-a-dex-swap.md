---
description: >-
  Swap tokens on-chain through a DEX from any wallet — permissionless, with no
  account, KYC, or activity. Quote the swap, approve if needed, then sign and
  broadcast the returned transaction yourself.
---

# Creating a DEX swap

{% hint style="warning" %}
DEX swaps will change heavily in the upcoming months, especially once the beta phase is done.
{% endhint %}

A **DEX swap** exchanges one token for another **on-chain**, routed through a decentralized exchange. It is **permissionless**: no account, no KYC, and **no activity** is created. You ask for a quote, and KiiChain Pay returns a ready-to-sign transaction (plus any ERC-20 approval) that **you sign and broadcast from your own wallet**. Routing is handled for you across chains.

{% hint style="info" %}
This is different from an [FX swap](creating-an-fx-swap.md). An FX swap is a **custodial, tracked activity** (a ticket) that KiiChain Pay settles for you. A DEX swap is a plain on-chain swap you broadcast yourself — there is nothing to track through `display_status`, only the on-chain transaction.
{% endhint %}

## At a glance

<table><thead><tr><th width="200">Property</th><th>Value</th></tr></thead><tbody>
<tr><td><strong>Direction</strong></td><td>Crypto → Crypto (cross-chain)</td></tr>
<tr><td><strong>Quote endpoint</strong></td><td><code>POST /market/v1/dex/quote</code> (public)</td></tr>
<tr><td><strong>You act</strong></td><td>Sign &amp; broadcast the returned transaction with your own wallet</td></tr>
<tr><td><strong>Account / KYC</strong></td><td>None</td></tr>
<tr><td><strong>Activity</strong></td><td>None — settles fully on-chain</td></tr>
<tr><td><strong>Tracking</strong></td><td>On-chain only (watch the transaction hash)</td></tr>
</tbody></table>

## Prerequisites

- A wallet on the source chain with the tokens to swap **and** native gas to pay for the transaction. (Gas sponsorship applies only to Kii Wallets, not to self-custody DEX swaps.)
- The token identifiers for both sides. Discover DEX-enabled tokens from the **public** endpoint:

```bash
curl "https://backend.pay.kiichain.io/blockchain/v1/chains/tokens/all?mode=dex"
```

Each `ChainToken` gives you the `chain.chain_id`, the `token.symbol` / `token.decimals`, whether it's `native`, and its `contract_address` (absent for native tokens). Use `contract_address` as the `denom` for ERC-20 tokens.

## Step 1 — Get a DEX quote

Post the source asset (with amount, in base units) and the destination asset. Include your `sender_address` so the returned transaction is built for your wallet.

```bash
curl -X POST "https://backend.pay.kiichain.io/market/v1/dex/quote" \
  -H "Content-Type: application/json" \
  -d '{
    "asset_in": {
      "denom": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      "chain_id": "1",
      "amount": "25000000"
    },
    "asset_out": {
      "denom": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
      "chain_id": "1"
    },
    "sender_address": "0x1A2b3C4d5E6f7A8b9C0d1E2f3A4b5C6d7E8f9A0b"
  }'
```

The response describes the route and — crucially — includes an **unsigned transaction** to broadcast:

```json
{
  "does_swap": true,
  "estimated_amount_out": "24980000",
  "txs_required": 1,
  "usd_amount_in": "25.00",
  "usd_amount_out": "24.98",
  "swap_price_impact_percent": "0.08",
  "provider": "lifi",
  "evm_tx": "0x02f8b20180…",
  "approval_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
  "approval_address": "0xLiFiRouterSpender…",
  "approval_amount": "25000000"
}
```

<table><thead><tr><th width="230">Field</th><th>Meaning</th></tr></thead><tbody>
<tr><td><code>evm_tx</code></td><td>An RLP-serialized <strong>unsigned EIP-1559 transaction</strong> (0x hex) — the swap itself, ready for you to sign and broadcast.</td></tr>
<tr><td><code>estimated_amount_out</code></td><td>Minimum output after slippage, in the destination token's base units.</td></tr>
<tr><td><code>approval_token</code> / <code>approval_address</code> / <code>approval_amount</code></td><td>The ERC-20 allowance the router needs. Present only when an approval is required (empty for native-token swaps).</td></tr>
<tr><td><code>txs_required</code></td><td>How many transactions the route needs.</td></tr>
<tr><td><code>swap_price_impact_percent</code></td><td>Estimated price impact, so you can reject a bad route.</td></tr>
</tbody></table>

{% hint style="warning" %}
The quote does not execute anything. Broadcast promptly — routes and prices are time-sensitive.
{% endhint %}

## Step 2 — Approve the token (if needed)

If `approval_token`, `approval_address`, and `approval_amount` are present, the DEX router needs an ERC-20 allowance before it can pull your tokens. Send a standard `approve(spender, amount)` transaction from your wallet, where `spender` is `approval_address` and `amount` is at least `approval_amount`. Native-token swaps skip this step.

## Step 3 — Sign & broadcast the swap

`evm_tx` is a serialized unsigned transaction. Decode it, sign it with your own wallet, and broadcast it. With [viem](https://viem.sh), parse it and hand the fields to your wallet client:

```typescript
import { parseTransaction } from "viem";

const { evm_tx } = quote; // from step 1
const tx = parseTransaction(evm_tx); // { to, value, data, chainId, ... }

const hash = await walletClient.sendTransaction({
  to: tx.to,
  value: tx.value,
  data: tx.data,
  chainId: tx.chainId,
});
console.log("swap broadcast:", hash);
```

{% hint style="info" %}
**Prefer to have KiiChain Pay sign it?** If you hold a [delegated Kii Wallet](../../introduction/privy-delegated-access.md), you can instead decode `evm_tx` into its `to` / `value` / `data` / `chain_id` fields and submit it through `POST /blockchain/v1/transactions/execute` (authenticated, gas-sponsored). That routes the same swap through your Kii Wallet rather than an external one. Check out the [actions you can take with internal wallets](../../introduction/internal-wallets.md#accessing-wallets-via-the-api).
{% endhint %}

## Step 4 — Confirm on-chain

There is no activity to poll — confirmation is on-chain. Wait for the transaction receipt and check the destination-token balance in your wallet:

```typescript
const receipt = await publicClient.waitForTransactionReceipt({ hash });
console.log(receipt.status); // "success" or "reverted"
```

## Full example

An end-to-end ERC-20 → ERC-20 DEX swap with viem: quote, approve if needed, broadcast, confirm.

```typescript
import { parseTransaction } from "viem";
// assumes viem `walletClient` (with your account) and `publicClient` are configured

const BASE_URL = "https://backend.pay.kiichain.io";
const SENDER = walletClient.account.address;

// 1 · Quote: 25 USDC → USDT on Ethereum.
const quote = await fetch(`${BASE_URL}/market/v1/dex/quote`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    asset_in: {
      denom: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      chain_id: "1",
      amount: "25000000",
    },
    asset_out: {
      denom: "0xdAC17F958D2ee523a2206206994597C13D831ec7",
      chain_id: "1",
    },
    sender_address: SENDER,
  }),
}).then((r) => r.json());

if (!quote.does_swap) throw new Error("no route available");

// 2 · Approve the router if the quote asks for it.
if (quote.approval_token && quote.approval_address) {
  const approveHash = await walletClient.writeContract({
    address: quote.approval_token,
    abi: [
      {
        name: "approve",
        type: "function",
        stateMutability: "nonpayable",
        inputs: [
          { name: "spender", type: "address" },
          { name: "amount", type: "uint256" },
        ],
        outputs: [{ type: "bool" }],
      },
    ],
    functionName: "approve",
    args: [quote.approval_address, BigInt(quote.approval_amount)],
  });
  await publicClient.waitForTransactionReceipt({ hash: approveHash });
}

// 3 · Sign & broadcast the swap transaction.
const tx = parseTransaction(quote.evm_tx);
const hash = await walletClient.sendTransaction({
  to: tx.to,
  value: tx.value,
  data: tx.data,
  chainId: tx.chainId,
});

// 4 · Confirm on-chain.
const receipt = await publicClient.waitForTransactionReceipt({ hash });
console.log(
  receipt.status === "success" ? "Swap complete 🎉" : "Swap reverted",
);
```

## Related

- [Creating an FX swap](creating-an-fx-swap.md) — the custodial, tracked alternative (creates an activity).
- [Guides overview](../README.md) — how DEX swaps compare with the account-based flows.
- [Internal wallets](../../introduction/internal-wallets.md) — Kii Wallet vs. external wallet.
