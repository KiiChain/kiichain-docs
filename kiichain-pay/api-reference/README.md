---
description: >-
  Every KiiChain Pay backend endpoint, plus the official
  Postman collection.
---

# API Reference

This section documents every endpoint of the KiiChain Pay backend API. Endpoints are grouped by module.

{% hint style="info" %}
Both this reference and the Postman collection are regenerated automatically on every KiiChain Pay backend release.
{% endhint %}

{% hint style="info" %}
[Generating API keys](../introduction/generating-api-keys.md) covers authentication and request signing. The [Guides](../guides/README.md) walk through full on-ramp, off-ramp, FX and DEX flows end to end.
{% endhint %}

## Try it in Postman

You can explore the API in the **KiiChain Pay Backend** Postman collection. It has every endpoint in this reference, ready to run, with signing already wired up.

{% hint style="success" %}
**[Open the KiiChain Pay Backend collection in Postman →](https://www.postman.com/devs-453829c1-6442516/kiichain-pay-backend-api/collection/yi3rz5t/kiichain-pay-backend?action=share&creator=56716314&active-environment=56716314-01b919a8-c9f7-4f81-86c6-f4a6d9eeb017)**
{% endhint %}

What you get:

- **Requests grouped by RPC server.** Folders follow the service boundaries — one per `<Module>QueryServer` (reads) and `<Module>MsgServer` (writes). Example: `UsersQueryServer`, `TicketsMsgServer` — so each folder maps into a module in this reference.
- **Signing handled for you.** A pre-request script computes the Ed25519 signature for every write request (`POST`/`PATCH`/`PUT`/`DELETE`) from your environment's `api_key` and `priv_key`, following the scheme described in [Sign write requests](../introduction/generating-api-keys.md#4.-sign-write-requests). No manual `x-timestamp` / `x-signature` headers needed.
- **A ready-made environment.** Fork it alongside the collection and fill in:

<table><thead><tr><th width="140">Variable</th><th>Value</th></tr></thead><tbody>
<tr><td><code>base_url</code></td><td><code>https://backend.pay.kiichain.io</code> (production), or the staging base URL.</td></tr>
<tr><td><code>api_key</code></td><td>Your <code>api_key</code> from <a href="../introduction/generating-api-keys.md">Generating API keys</a>.</td></tr>
<tr><td><code>priv_key</code></td><td>Your <code>priv_key</code> — the pre-request script uses this to sign write requests.</td></tr>
</tbody></table>

### Getting started

1. **Fork** the collection and its environment into your own Postman workspace (top-right **Fork** button on each).
2. Open the forked **environment**, select it as active, and fill in `api_key`, and `priv_key`.
3. Send a read request first (You can try `Me` at `UsersQueryServer`) to confirm your API key is valid.
4. Send a write request (Anything with `*MsgServer`). The pre-request script signs it automatically.

{% hint style="warning" %}
Treat `priv_key` like any other private key. Postman environment values are visible to anyone you share the workspace with — don't fork a copy with a production key into a shared team workspace.
{% endhint %}
