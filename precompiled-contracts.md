---
description: >-
  KiiChain has precompiled smart contracts crafted to allow EVM interaction with
  the Cosmos SDK functionalities
---

# Precompiled contracts

### List of precompiles and their addresses

KiiChain supports both EVM JSON-RPC and Cosmos RPC interfaces. In order to easily interact with certain Cosmos modules, KiiChain has a set of precompiled contracts that can be called from the EVM.

| Precompile              | Description                                                                                                   | Address                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Bank Precompile         | Provides functionalities for checking balances and supply.                                                    | 0x0000000000000000000000000000000000000804 |
| Distribution Precompile | Handles reward distribution and related functionalities.                                                      | 0x0000000000000000000000000000000000000801 |
| Governance Precompile   | Supports actions such as depositing funds into proposals, voting, and interacting with proposals.             | 0x0000000000000000000000000000000000000805 |
| IBC Precompile          | Allows IBC transfers                                                                                          | 0x0000000000000000000000000000000000001002 |
| ICS20 Precompile        | Facilitates usage of ICS20 token transfers                                                                    | 0x0000000000000000000000000000000000000802 |
| Slashing Precompile     | Provides management and query options for penalties                                                           | 0x0000000000000000000000000000000000000806 |
| Staking Precompile      | Enables staking functionalities such as delegation, undelegation, or obtaining information on validators.      | 0x0000000000000000000000000000000000000800 |
| WASM Precompile         | Provides interaction with WASM contracts                                                                      | 0x0000000000000000000000000000000000001001 |

### Interacting with precompiles

You can utilize direct JSON-RPC connections to those addresses. We also have [a TS/JS library](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-evm.md) to help interact with them.
