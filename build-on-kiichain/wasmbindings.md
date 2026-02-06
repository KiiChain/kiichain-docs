---
description: Wasm contract bindings for custom modules
---

# Wasmbindings

### Core Concept

**WASM Bindings** (WebAssembly bindings) are interfaces that allow CosmWasm smart contracts to interact with **native blockchain modules** beyond the standard Cosmos SDK bank and staking modules. They provide a bridge between WebAssembly smart contracts and the underlying blockchain's specialized functionality.

We currently only support queries for our custom modules.

### Covered modules

<table><thead><tr><th width="139.33331298828125">Module Name</th><th>Queries</th></tr></thead><tbody><tr><td>TokenFactory</td><td>FullDenom, Admin, Metadata, DenomsByCreator, Params</td></tr><tr><td>EVM</td><td>EthCall, ERC20Information, ERC20Balance, ERC20Allowance</td></tr><tr><td>Oracle</td><td>ExchangeRate, ExchangeRates, Twaps</td></tr><tr><td>Bech32</td><td>HexToBech32, Bech32ToHex</td></tr></tbody></table>
