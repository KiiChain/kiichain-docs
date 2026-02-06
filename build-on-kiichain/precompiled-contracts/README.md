---
description: >-
  KiiChain has precompiled smart contracts crafted to allow EVM interaction with
  the Cosmos SDK functionalities
---

# Precompiled contracts

### List of precompiles and their addresses

KiiChain supports both EVM JSON-RPC and Cosmos RPC interfaces. In order to easily interact with certain Cosmos modules, KiiChain has a set of precompiled contracts that can be called from the EVM.

<table><thead><tr><th width="134.41668701171875">Precompile</th><th>Description</th><th>Address</th></tr></thead><tbody><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/bank">Bank</a></td><td>Provides functionalities for checking balances and supply</td><td>0x0000000000000000000000000000000000000804</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/bech32">Bech32</a></td><td>Utilities for address format conversion between EVM and Cosmos</td><td>0x0000000000000000000000000000000000000400</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/distribution">Distribution</a> </td><td>Deals with reward distribution and related</td><td>0x0000000000000000000000000000000000000801</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/governance">Governance</a></td><td>Supports actions such as depositing funds into proposals, voting and interacting with proposals</td><td>0x0000000000000000000000000000000000000805</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/p256">P256</a> </td><td>Support for verifying secp256r1 curve signatures</td><td>0x0000000000000000000000000000000000000100</td></tr><tr><td><a href="oracle-precompile.md">Oracle</a></td><td>Support for price information and oracle module</td><td>0x0000000000000000000000000000000000001003</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/slashing">Slashing</a> </td><td>Provides management and query options for penalties</td><td>0x0000000000000000000000000000000000000806</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/staking">Staking</a> </td><td>Enables staking functionalities like delegation and undelegation or obtaining information on validators.</td><td>0x0000000000000000000000000000000000000800</td></tr><tr><td>Vesting</td><td>Interacts with Cosmos Vesting module</td><td>0x0000000000000000000000000000000000000803</td></tr><tr><td><a href="https://docs.cosmos.network/evm/v0.5.0/documentation/smart-contracts/precompiles/werc20">WERC20</a> </td><td>ERC20 interface for native Kii</td><td>0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE</td></tr></tbody></table>

### Interacting with precompiles

You can utilize direct json-rpc connections to those addresses. We also have [a TS/JS library ](../developer-tools/js-ts-sdk/kiijs-evm.md)to help interact with them.
