---
description: >-
  Bridge KII between Kiichain and other networks. Includes Hyperlane warp route
  addresses and Nexus as a bridging option.
---

# Bridge

KII can move between Kiichain and supported external chains through Hyperlane warp routes. Use the addresses below to verify you are interacting with the correct contracts, and use [Nexus](https://nexus.hyperlane.xyz/?origin=kiichain&originToken=KII&destination=bsc&destinationToken=KII) as a UI option for bridging assets.

## Bridge with Nexus

[Nexus](https://nexus.hyperlane.xyz/?origin=kiichain&originToken=KII&destination=bsc&destinationToken=KII) is a Hyperlane-powered bridge interface. You can bridge KII between Kiichain and connected chains such as BNB Smart Chain (BSC), Polygon, Base, Ethereum, and Mantle.

Always confirm the destination chain and token address before signing a transaction.

## KII addresses on other chains

Official Hyperlane warp route configuration (source of truth):

* [Hyperlane registry — KII / kiichain-config.yaml](https://github.com/hyperlane-xyz/hyperlane-registry/blob/main/deployments/warp_routes/KII/kiichain-config.yaml)

| Chain | Contract address | Type |
| ----- | ---------------- | ---- |
| Kiichain | `0xEEC6574eAbBa52bac3f0277F2cD5Ac7e67197886` | Native (EvmHypNative) |
| BNB Smart Chain (BSC) | `0xEEC6574eAbBa52bac3f0277F2cD5Ac7e67197886` | Synthetic (EvmHypSynthetic) |
| Polygon | `0xEEC6574eAbBa52bac3f0277F2cD5Ac7e67197886` | Synthetic (EvmHypSynthetic) |
| Ethereum | `0xEEC6574eAbBa52bac3f0277F2cD5Ac7e67197886` | Synthetic (EvmHypSynthetic) |
| Mantle | `0xEEC6574eAbBa52bac3f0277F2cD5Ac7e67197886` | Synthetic (EvmHypSynthetic) |
| Base | `0x3EBA6644819546C44Eb3e7c3A92f034f921dcA80` | Synthetic (EvmHypSynthetic) |

On Kiichain, the warp route represents native KII. On other chains, the listed address is the synthetic KII token contract for that network.

Decimals are `18` on all listed chains. Symbol: `KII`.

## Safety checklist

* Prefer the Hyperlane registry link above when confirming addresses.
* Base uses a different contract address than the other listed chains.
* Do not send KII to an unverified or manually pasted address from unofficial sources.
* If a UI and the registry disagree, trust the [Hyperlane registry config](https://github.com/hyperlane-xyz/hyperlane-registry/blob/main/deployments/warp_routes/KII/kiichain-config.yaml).
