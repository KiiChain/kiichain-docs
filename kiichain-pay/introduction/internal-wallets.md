---
description: >-
  Every KiiChain Pay account gets non-custodial embedded wallets — the Kii
  Wallet — provisioned automatically after KYC, with gas sponsored by the
  platform.
---

# Internal wallets

KiiChain Pay gives every account a set of **embedded wallets**, branded the **Kii Wallet** in the product. These are the on-chain accounts users transact from — and they are **non-custodial**: the private keys are managed by [Privy](https://privy.io) and owned by the user. KiiChain Pay never holds a private key.

Alongside these on-chain wallets, KiiChain Pay keeps an **internal ledger** that tracks fiat and reserved balances off-chain. Together they let you mix on-chain and off-chain operations seamlessly.

## What a Kii Wallet is

- An **embedded wallet** created and secured by Privy, one **per account, per supported chain**.
- **Supported chain types:** EVM (Ethereum-compatible, including KiiChain), Cosmos, Solana, Tron, and Bitcoin (SegWit).
- **Non-custodial:** keys live with Privy and belong to the user. To let your backend transact from a wallet, the user must first [delegate it](privy-delegated-access.md) to the platform signer.
- **Gas-sponsored:** every Kii Wallet operation is paid for by KiiChain Pay, so users never need native gas tokens.

{% hint style="info" %}
Kii Wallets are provisioned **automatically when KYC is approved** — not at signup. An account at level 0 (no KYC) has no wallets yet. See [KYC](kyc.md).
{% endhint %}

## On-chain balances vs. the off-chain ledger

KiiChain Pay tracks value in two places:

<table><thead><tr><th width="200">Where</th><th>What it holds</th></tr></thead><tbody>
<tr><td><strong>On-chain (Kii Wallet)</strong></td><td>Crypto assets, held at the wallet's address on each chain. Balances are read directly from the blockchain.</td></tr>
<tr><td><strong>Off-chain (internal ledger)</strong></td><td>Fiat and reserved balances, tracked in a double-entry ledger. Each balance has an <code>available</code> portion and a <code>locked</code> portion (funds reserved for an in-flight withdrawal, swap or ramp).</td></tr>
</tbody></table>

This split is why a swap or off-ramp can reserve funds (`locked`) the instant you create it, while the on-chain settlement happens moments later.

## How funds move

The Kii Wallet is the on-chain endpoint for every value flow:

- **Deposits** — receive crypto to the wallet address, or fund a fiat **virtual account** via an on-ramp provider.
- **Withdrawals** — send crypto to an external address, or off-ramp to a bank account through a provider.
- **Swaps / FX** — settle on-chain through KiiChain Pay's settlement contracts, with the platform signing on the delegated wallet's behalf.
- **On-ramps / off-ramps** — bridge fiat and crypto through integrated providers.

See the [Guides](../guides/README.md) for end-to-end [on-ramp](../guides/quick-start/creating-an-on-ramp.md), [off-ramp](../guides/quick-start/creating-an-off-ramp.md), and [FX swap](../guides/quick-start/creating-an-fx-swap.md) walkthroughs.

## Viewing your wallets

In the app, the Kii Wallet and its balances are shown in the wallet area of the dashboard.

<figure><img src="../../.gitbook/assets/kiichain-pay-kii-wallet.png" alt=""><figcaption><p><strong>📸 Screenshot needed:</strong> The Kii Wallet view in the dashboard showing the wallet address and balances.</p></figcaption></figure>

## Accessing wallets via the API

{% hint style="warning" %}
**Upcoming.** A dedicated endpoint to fetch a logged-in user's Kii Wallet addresses across all supported chain types is in development. This section will be updated with the endpoint and payload once it ships.
{% endhint %}

{% hint style="warning" %}
**Upcoming.** An endpoint to **send tokens from a Kii Wallet to another wallet** is in development. It will require the wallet to be [delegated](privy-delegated-access.md). This section will be updated when it ships.
{% endhint %}

## Next steps

- [Privy delegated access](privy-delegated-access.md) — let your backend sign wallet operations.
- [KYC](kyc.md) — required before wallets are provisioned.
