---
description: Everything you need to know about Kiichain mainnet.
---

# Kiichain Mainnet

Kiichain is a peer-to-peer decentralized EVM-compatible network built with the Cosmos SDK. The mainnet chain ID is `kiichain_1783-1`.

For experimentation, hackathons, and test deployments, use [Testnet Oro](testnet-oro.md). Use mainnet for production deployments and mainnet validator operations.

## Source code

* [Kiichain](https://github.com/KiiChain/kiichain)
* [Mainnet configs and join scripts](https://github.com/KiiChain/mainnets/tree/main/kiichain)

## Endpoints

* **RPC:** [https://rpc.kiivalidator.com](https://rpc.kiivalidator.com)
* **Rest (LCD):** [https://lcd.kiivalidator.com](https://lcd.kiivalidator.com)
* **GRPC:** grpc.kiivalidator.com:443
* **JSON-RPC (EVM):** [https://json-rpc.kiivalidator.com](https://json-rpc.kiivalidator.com)
* **WebSocket:** wss://ws.kiivalidator.com/websocket

Persistent peers:

* `4d0c3be48018cf8234faa46d789634f8a811dc5b@p2p-1.kiivalidator.com:26656`
* `ac58976b16880535d56b2e1fe1f499a3841c4039@p2p-2.kiivalidator.com:26656`

## Chain information

* **Chain ID:** `kiichain_1783-1`
* **EVM Chain ID:** `1783`
* **Token Denom:** `akii`
* **Decimals:** `18`
* **Bech32 Prefix:** `kii`
* **Max Supply:** `1.8b KII`

## How to join the network

Instructions and join scripts are available in the mainnets repository:

* [Join Kiichain](https://github.com/KiiChain/mainnets/blob/main/kiichain/join_kiichain.sh)
* [Join Kiichain with Cosmovisor](https://github.com/KiiChain/mainnets/blob/main/kiichain/join_kiichain_cv.sh)
* [Step-by-Step Guide](../validate-the-network/run-a-validator-full-node/step-by-step-guide/)

## Bridge KII

KII is available on connected chains through Hyperlane. See:

* [Bridge](../learn/getting-started/bridge.md)

## Developer tools

* [RWA Protocol](developer-tools/rwa-protocol.md)
* [Deploying a smart contract](developer-tools/deploy-a-smart-contract.md)
* [Deploying a dApp](developer-tools/deploy-a-dapp.md)
* [Endpoints - EVM](endpoints-evm.md)
* [Endpoints - Cosmos](endpoints-cosmos/)
