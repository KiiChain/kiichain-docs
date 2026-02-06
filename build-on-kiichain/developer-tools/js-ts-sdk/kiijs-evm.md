# Kiijs-evm

## @kiichain/kiijs-evm

Typescript library containing helper functions for interacting with the EVM on KiiChain. The full code can be found here: [https://github.com/KiiChain/kiijs-sdk/tree/main/packages/evm](https://github.com/KiiChain/kiijs-sdk/tree/main/packages/evm)

### Installation

```bash
yarn add @kiichain/kiijs-evm ethers viem
```

### Wallet Connection

This package provides exports for easily interacting with viem, and ethers.js. You can interact with the KiiChain EVM using all the same hooks and helper functions these tools offer. Read the viem and ethers v6 documentation for more information on how to use these tools.

#### Wallet network setup

Ensure that your EVM wallet has the KiiChain network enabled.

#### Connection with ethers v6

The 'ethers' package is a popular library for interacting with the Ethereum blockchain. This package provides a helper function for creating an ethers provider that is connected to the KiiChain EVM.

```tsx
import { getBankPrecompileEthersV6Contract } from '@kiichain/kiijs-evm';
import { ethers } from 'ethers';

const provider = new ethers.BrowserProvider(window.ethereum); // or any other provider
const signer = await provider.getSigner();

const accounts = await provider.send('eth_requestAccounts', []);

const contract = getBankPrecompileEthersV6Contract(signer);

const cosmosAddress = await contract.balances("yourAddress");
```

An alternative without the popup is to directly use your private key to connect.

```tsx
import { ethers } from 'ethers';

const provider = new ethers.JsonRpcProvider('https://json-rpc.dos.sentry.testnet.v3.kiivalidator.com/');
const wallet = new ethers.Wallet("0xyourprivatekey", provider);
```

#### Usage with viem

This package exports `viem` Chains and precompile ABI's for KiiChain. The ABI used in the ethers example above is a viem ABI instance and the `ARCTIC_1_VIEM_CHAIN` is a `viem Chain` instance.

### Interoperability with Cosmos

KiiChain supports both EVM JSON-RPC and Cosmos RPC interfaces. In order to easily interact with certain Cosmos modules, KiiChain has a set of precompiled contracts that can be called from the EVM.

| Precompile                                                      | Description                                                                                              |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [Bank Precompile](kiijs-evm.md#bank-precompile)                 | Provides functionalities for checking balances and supply.                                               |
| [Bech32 Precompile](kiijs-evm.md#bech32-precompile)             | Facilitates conversion between hex address and bech32                                                    |
| [Distribution Precompile](kiijs-evm.md#distribution-precompile) | Deals with reward distribution and related                                                               |
| [Governance Precompile](kiijs-evm.md#governance-precompile)     | Supports actions such as depositing funds into proposals, voting and interacting with proposals.         |
| [IBC Precompile](kiijs-evm.md#ibc-precompile)                   | Allows IBC transfers                                                                                     |
| [ICS20 Precompile](kiijs-evm.md#ics20-precompile)               | Facilitates conversion between hex address and bech32                                                    |
| [Slashing Precompile](kiijs-evm.md#slashing-precompile)         | Provides management and query options for penalties                                                      |
| [Staking Precompile](kiijs-evm.md#staking-precompile)           | Enables staking functionalities like delegation and undelegation or obtaining information on validators. |
| [Wasm Precompile](kiijs-evm.md#wasm-precompile)                 | Precompile for interacting with wasm contracts                                                           |

#### Interoperability using Wagmi, viem, and ethers

Each precompile has contract exports a typed 'ethers' contracts and provides the ABI and contract addresses for each precompile for usage with Wagmi and viem.

### Bank Precompile

The Bank precompile contract provides functionalities for managing balances, supply, symbols, and more.

**Functions**

| Function Name | Input Parameters | Return Value                                     | Description                                                          |
| ------------- | ---------------- | ------------------------------------------------ | -------------------------------------------------------------------- |
| `balances`    | `acc: string`    | `balances : [{ denom: string, amount: string }]` | Retrieves the balances of a given address                            |
| `supplyOf`    | `denom: string`  | `{ response: string }`                           | Retrieves the total supply of tokens for the specified denomination. |
| `totalSupply` | -                | `balances : [{ denom: string, amount: string }]` | Retrieves all the supplies from the chain                            |

**Precompile Addresses**

0x000000000000000000000000000000000000080

### Bech32 Precompile

The bech32 precompile contract provides ways to turn a hex address to bech32 and vice-versa. There is also functions in the library under the precompile to do the same without using the contract.

```tsx
import { HexToBech32, Bech32ToHex } from '@kiichain/kiijs-evm'

const kiiAddress = HexToBech32("0xyourhex")

const evmAddress = Bech32ToHex("kiiYouraddress)
```

### Distribution Precompile

The Distribution precompile contract facilitates operations related to rewards withdrawal and distribution.

**Functions**

Here's the table representation of your Distribution ABI:

| Function Name                 | Input Parameters                                                                                                                                                                                                                                             | Return Value                                                                                                                                                                                              | Description                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `claimRewards`                | <p><code>delegatorAddress: string</code> (address)<br><code>maxRetrieve: number</code> (uint32)</p>                                                                                                                                                          | `success: boolean`                                                                                                                                                                                        | Claims rewards for a delegator (up to maxRetrieve) |
| `delegationRewards`           | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code></p>                                                                                                                                                              | `rewards: [{ denom: string, amount: string, precision: number }]`                                                                                                                                         | Gets rewards for a specific delegation             |
| `delegationTotalRewards`      | `delegatorAddress: string` (address)                                                                                                                                                                                                                         | <p><code>rewards: [{ validatorAddress: string, reward: [{ denom: string, amount: string, precision: number }] }]</code><br><code>total: [{ denom: string, amount: string, precision: number }]</code></p> | Gets all rewards for a delegator with totals       |
| `delegatorValidators`         | `delegatorAddress: string` (address)                                                                                                                                                                                                                         | `validators: string[]`                                                                                                                                                                                    | Lists all validators a delegator is staked with    |
| `delegatorWithdrawAddress`    | `delegatorAddress: string` (address)                                                                                                                                                                                                                         | `withdrawAddress: string`                                                                                                                                                                                 | Gets the withdrawal address for a delegator        |
| `fundCommunityPool`           | <p><code>depositor: string</code> (address)<br><code>amount: string</code> (uint256)</p>                                                                                                                                                                     | `success: boolean`                                                                                                                                                                                        | Funds the community pool                           |
| `setWithdrawAddress`          | <p><code>delegatorAddress: string</code> (address)<br><code>withdrawerAddress: string</code></p>                                                                                                                                                             | `success: boolean`                                                                                                                                                                                        | Sets the withdrawal address for rewards            |
| `validatorCommission`         | `validatorAddress: string`                                                                                                                                                                                                                                   | `commission: [{ denom: string, amount: string, precision: number }]`                                                                                                                                      | Gets commission rewards for a validator            |
| `validatorDistributionInfo`   | `validatorAddress: string`                                                                                                                                                                                                                                   | `distributionInfo: { operatorAddress: string, selfBondRewards: [{ denom: string, amount: string, precision: number }], commission: [{ denom: string, amount: string, precision: number }] }`              | Gets full distribution info for a validator        |
| `validatorOutstandingRewards` | `validatorAddress: string`                                                                                                                                                                                                                                   | `rewards: [{ denom: string, amount: string, precision: number }]`                                                                                                                                         | Gets outstanding rewards for a validator           |
| `validatorSlashes`            | <p><code>validatorAddress: string</code><br><code>startingHeight: number</code> (uint64)<br><code>endingHeight: number</code> (uint64)<br><code>pageRequest: { key: bytes, offset: number, limit: number, countTotal: boolean, reverse: boolean }</code></p> | <p><code>slashes: [{ validatorPeriod: number, fraction: { value: string, precision: number } }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p>                                | Gets slash events for a validator with pagination  |
| `withdrawDelegatorRewards`    | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code></p>                                                                                                                                                              | `amount: [{ denom: string, amount: string }]`                                                                                                                                                             | Withdraws delegator's rewards from a validator     |
| `withdrawValidatorCommission` | `validatorAddress: string`                                                                                                                                                                                                                                   | `amount: [{ denom: string, amount: string }]`                                                                                                                                                             | Withdraws validator's commission rewards           |

**Precompile Addresses**

0x0000000000000000000000000000000000000801

### Evidence Precompile

The Evidence precompile contract provides functionalities for dealing with evidences.

**Functions**

| Function Name    | Input Parameters                                                                                    | Return Value                                                                                                                                                              | Description                                    |
| ---------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `evidence`       | `evidenceHash: bytes`                                                                               | `evidence: { height: number, time: number, power: number, consensusAddress: string }`                                                                                     | Retrieves evidence by its hash                 |
| `getAllEvidence` | `pageRequest: { key: bytes, offset: number, limit: number, countTotal: boolean, reverse: boolean }` | <p><code>evidence: [{ height: number, time: number, power: number, consensusAddress: string }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p> | Retrieves all evidence with pagination support |
| `submitEvidence` | `evidence: { height: number, time: number, power: number, consensusAddress: string }`               | `success: boolean`                                                                                                                                                        | Submits new evidence of validator equivocation |

**Precompile Addresses**

0x0000000000000000000000000000000000000807

### Governance Precompile

The Governance precompile contract supports actions to deposit funds into proposals, view them and interact with them.

**Functions**

| Function Name    | Input Parameters                                                                                                                                                                       | Return Value                                                                                                                                                                                        | Description                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `getDeposit`     | <p><code>proposalId: number</code> (uint64)<br><code>depositor: string</code> (address)</p>                                                                                            | `deposit: { proposalId: number, depositor: string, amount: [{ denom: string, amount: string }] }`                                                                                                   | Gets a specific deposit for a proposal           |
| `getDeposits`    | <p><code>proposalId: number</code> (uint64)<br><code>pagination: { key: bytes, offset: number, limit: number, countTotal: boolean, reverse: boolean }</code></p>                       | <p><code>deposits: [{ proposalId: number, depositor: string, amount: [{ denom: string, amount: string }] }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p>              | Gets all deposits for a proposal with pagination |
| `getParams`      | -                                                                                                                                                                                      | `params: { votingPeriod: number, minDeposit: [{ denom: string, amount: string }], maxDepositPeriod: number, quorum: string, threshold: string, vetoThreshold: string, ... }`                        | Returns governance parameters                    |
| `getProposal`    | `proposalId: number` (uint64)                                                                                                                                                          | `proposal: { id: number, messages: string[], status: number, finalTallyResult: { yes: string, abstain: string, no: string, noWithVeto: string }, submitTime: number, ... }`                         | Gets full proposal details                       |
| `getProposals`   | <p><code>proposalStatus: number</code> (uint32)<br><code>voter: string</code> (address)<br><code>depositor: string</code> (address)<br><code>pagination: { ... }</code></p>            | <p><code>proposals: [{ id: number, messages: string[], status: number, finalTallyResult: { ... }, ... }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p>                 | Lists proposals with filters and pagination      |
| `getTallyResult` | `proposalId: number` (uint64)                                                                                                                                                          | `tallyResult: { yes: string, abstain: string, no: string, noWithVeto: string }`                                                                                                                     | Gets current tally results for a proposal        |
| `getVote`        | <p><code>proposalId: number</code> (uint64)<br><code>voter: string</code> (address)</p>                                                                                                | `vote: { proposalId: number, voter: string, options: [{ option: number, weight: string }], metadata: string }`                                                                                      | Gets an individual vote                          |
| `getVotes`       | <p><code>proposalId: number</code> (uint64)<br><code>pagination: { ... }</code></p>                                                                                                    | <p><code>votes: [{ proposalId: number, voter: string, options: [{ option: number, weight: string }], metadata: string }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p> | Gets all votes for a proposal with pagination    |
| `vote`           | <p><code>voter: string</code> (address)<br><code>proposalId: number</code> (uint64)<br><code>option: number</code> (uint8)<br><code>metadata: string</code></p>                        | `success: boolean`                                                                                                                                                                                  | Submits a vote on a proposal                     |
| `voteWeighted`   | <p><code>voter: string</code> (address)<br><code>proposalId: number</code> (uint64)<br><code>options: [{ option: number, weight: string }]</code><br><code>metadata: string</code></p> | `success: boolean`                                                                                                                                                                                  | Submits a weighted vote on a proposal            |

**Precompile Addresses**

0x0000000000000000000000000000000000000805

### IBC Precompile

Enables cross-chain token transfers via IBC with simplified parameters

**Functions**

| Function Name                    | Input Parameters                                                                                                                                                                                                                                                                                                                                                  | Return Value       | Description                                                                           |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------- |
| **`transfer`**                   | <p><code>receiver: string</code> (address)<br><code>port: string</code><br><code>channel: string</code><br><code>denom: string</code><br><code>amount: string</code> (uint256)<br><code>revisionNumber: number</code> (uint64)<br><code>revisionHeight: number</code> (uint64)<br><code>timeoutTimestamp: number</code> (uint64)<br><code>memo: string</code></p> | `success: boolean` | Initiates an IBC token transfer with full timeout control (both height and timestamp) |
| **`transferWithDefaultTimeout`** | <p><code>receiver: string</code> (address)<br><code>port: string</code><br><code>channel: string</code><br><code>denom: string</code><br><code>amount: string</code> (uint256)<br><code>memo: string</code></p>                                                                                                                                                   | `success: boolean` | Initiates an IBC transfer using default timeout values (simplified interface)         |

**Precompile Addresses**

0x0000000000000000000000000000000000001002

### ICS20 Precompile

Enables cross-chain token transfers via IBC with granular permission control over channels and denominations.

**Functions**

| Function Name           | Input Parameters                                                                                                                                                                                                                                                                                                                                                                      | Return Value                                                                                                                                                      | Description                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **`allowance`**         | <p><code>grantee: string</code> (address)<br><code>granter: string</code> (address)</p>                                                                                                                                                                                                                                                                                               | `allocations: [{ sourcePort: string, sourceChannel: string, spendLimit: [{ denom: string, amount: string }], allowList: string[], allowedPacketData: string[] }]` | Checks granted IBC transfer permissions                                                       |
| **`approve`**           | <p><code>grantee: string</code> (address)<br><code>allocations: [{ sourcePort: string, sourceChannel: string, spendLimit: [{ denom: string, amount: string }], ... }]</code></p>                                                                                                                                                                                                      | `approved: boolean`                                                                                                                                               | Grants IBC transfer permissions                                                               |
| **`decreaseAllowance`** | <p><code>grantee: string</code> (address)<br><code>sourcePort: string</code><br><code>sourceChannel: string</code><br><code>denom: string</code><br><code>amount: string</code> (uint256)</p>                                                                                                                                                                                         | `approved: boolean`                                                                                                                                               | Reduces spend limit for a specific channel/denom                                              |
| **`denomHash`**         | `trace: string` (e.g., "transfer/channel-1/uatom")                                                                                                                                                                                                                                                                                                                                    | `hash: string` (IBC denom hash)                                                                                                                                   | Converts IBC denom trace to hash (e.g., `ibc/27394FB092...`)                                  |
| **`denomTrace`**        | `hash: string` (IBC denom hash)                                                                                                                                                                                                                                                                                                                                                       | `denomTrace: { path: string, baseDenom: string }`                                                                                                                 | Decodes IBC hash to original trace (e.g., `path: "transfer/channel-1"`, `baseDenom: "uatom"`) |
| **`denomTraces`**       | `pageRequest: { key: bytes, offset: number, limit: number, ... }`                                                                                                                                                                                                                                                                                                                     | <p><code>denomTraces: [{ path: string, baseDenom: string }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p>                            | Lists all registered denom traces with pagination                                             |
| **`increaseAllowance`** | <p><code>grantee: string</code> (address)<br><code>sourcePort: string</code><br><code>sourceChannel: string</code><br><code>denom: string</code><br><code>amount: string</code> (uint256)</p>                                                                                                                                                                                         | `approved: boolean`                                                                                                                                               | Increases spend limit for a specific channel/denom                                            |
| **`revoke`**            | `grantee: string` (address)                                                                                                                                                                                                                                                                                                                                                           | `revoked: boolean`                                                                                                                                                | Revokes all IBC transfer permissions for a grantee                                            |
| **`transfer`**          | <p><code>sourcePort: string</code><br><code>sourceChannel: string</code><br><code>denom: string</code><br><code>amount: string</code> (uint256)<br><code>sender: string</code> (address)<br><code>receiver: string</code><br><code>timeoutHeight: { revisionNumber: number, revisionHeight: number }</code><br><code>timeoutTimestamp: number</code><br><code>memo: string</code></p> | `nextSequence: number` (uint64)                                                                                                                                   | Initiates an IBC token transfer                                                               |

**Precompile Addresses**

0x0000000000000000000000000000000000000802

### Slashing Precompile

Enables query, interaction and management of validator penalties.

**Functions**

| Function Name     | Input Parameters                                                                                   | Return Value                                                                                                                                                                                                                                      | Description                                     |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `getParams`       | -                                                                                                  | `params: { signedBlocksWindow: number, minSignedPerWindow: string, downtimeJailDuration: number, slashFractionDoubleSign: string, slashFractionDowntime: string }`                                                                                | Returns slashing module parameters              |
| `getSigningInfo`  | `consAddress: string` (address)                                                                    | `signingInfo: { validatorAddress: string, startHeight: number, indexOffset: number, jailedUntil: number, tombstoned: boolean, missedBlocksCounter: number }`                                                                                      | Gets signing info for a validator               |
| `getSigningInfos` | `pagination: { key: bytes, offset: number, limit: number, countTotal: boolean, reverse: boolean }` | <p><code>signingInfos: [{ validatorAddress: string, startHeight: number, indexOffset: number, jailedUntil: number, tombstoned: boolean, missedBlocksCounter: number }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p> | Gets all validator signing info with pagination |
| `unjail`          | `validatorAddress: string` (address)                                                               | `success: boolean`                                                                                                                                                                                                                                | Releases a validator from jail status           |

**Precompile Addresses**

0x0000000000000000000000000000000000000806

### Staking Precompile

The Staking precompile manages validator operations, delegations, and governance permissions in a Cosmos-based blockchain with EVM compatibility.

**Functions**

| Function Name                   | Input Parameters                                                                                                                                                                                                                                                                                                        | Return Value                                                                                                              | Description                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **`allowance`**                 | <p><code>grantee: string</code> (address)<br><code>granter: string</code> (address)<br><code>method: string</code></p>                                                                                                                                                                                                  | `remaining: string` (uint256)                                                                                             | Checks remaining allowance for a grantee's staking actions      |
| **`approve`**                   | <p><code>grantee: string</code> (address)<br><code>amount: string</code> (uint256)<br><code>methods: string[]</code></p>                                                                                                                                                                                                | `approved: boolean`                                                                                                       | Grants staking permissions to another address                   |
| **`cancelUnbondingDelegation`** | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code><br><code>amount: string</code> (uint256)<br><code>creationHeight: string</code> (uint256)</p>                                                                                                                               | `success: boolean`                                                                                                        | Cancels an unbonding delegation before completion               |
| **`createValidator`**           | <p><code>description: { moniker: string, identity: string, ... }</code><br><code>commissionRates: { rate: string, maxRate: string, ... }</code><br><code>minSelfDelegation: string</code><br><code>validatorAddress: string</code> (address)<br><code>pubkey: string</code><br><code>value: string</code> (uint256)</p> | `success: boolean`                                                                                                        | Registers a new validator                                       |
| **`decreaseAllowance`**         | <p><code>grantee: string</code> (address)<br><code>amount: string</code> (uint256)<br><code>methods: string[]</code></p>                                                                                                                                                                                                | `approved: boolean`                                                                                                       | Reduces staking permissions for a grantee                       |
| **`delegate`**                  | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code><br><code>amount: string</code> (uint256)</p>                                                                                                                                                                                | `success: boolean`                                                                                                        | Delegates tokens to a validator                                 |
| **`delegation`**                | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code></p>                                                                                                                                                                                                                         | <p><code>shares: string</code> (uint256)<br><code>balance: { denom: string, amount: string }</code></p>                   | Returns delegation details between a delegator and validator    |
| **`editValidator`**             | <p><code>description: { moniker: string, ... }</code><br><code>validatorAddress: string</code> (address)<br><code>commissionRate: number</code> (int256)<br><code>minSelfDelegation: number</code> (int256)</p>                                                                                                         | `success: boolean`                                                                                                        | Modifies validator metadata/parameters                          |
| **`increaseAllowance`**         | <p><code>grantee: string</code> (address)<br><code>amount: string</code> (uint256)<br><code>methods: string[]</code></p>                                                                                                                                                                                                | `approved: boolean`                                                                                                       | Increases staking permissions for a grantee                     |
| **`redelegate`**                | <p><code>delegatorAddress: string</code> (address)<br><code>srcValidatorAddress: string</code><br><code>dstValidatorAddress: string</code><br><code>amount: string</code> (uint256)</p>                                                                                                                                 | `completionTime: number` (int64)                                                                                          | Transfers delegation between validators (with unbonding period) |
| **`redelegation`**              | <p><code>delegatorAddress: string</code> (address)<br><code>srcValidatorAddress: string</code><br><code>dstValidatorAddress: string</code></p>                                                                                                                                                                          | `redelegation: { entries: [{ creationHeight: number, completionTime: number, ... }] }`                                    | Returns redelegation details                                    |
| **`redelegations`**             | <p><code>delegatorAddress: string</code> (address)<br><code>srcValidatorAddress: string</code><br><code>dstValidatorAddress: string</code><br><code>pageRequest: { key: bytes, ... }</code></p>                                                                                                                         | <p><code>response: [{ redelegation: { ... } }]</code><br><code>pageResponse: { nextKey: bytes, total: number }</code></p> | Paginated redelegation history                                  |
| **`revoke`**                    | <p><code>grantee: string</code> (address)<br><code>methods: string[]</code></p>                                                                                                                                                                                                                                         | `revoked: boolean`                                                                                                        | Revokes all staking permissions for a grantee                   |
| **`unbondingDelegation`**       | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code></p>                                                                                                                                                                                                                         | `unbondingDelegation: { entries: [{ creationHeight: number, completionTime: number, ... }] }`                             | Returns active unbonding delegations                            |
| **`undelegate`**                | <p><code>delegatorAddress: string</code> (address)<br><code>validatorAddress: string</code><br><code>amount: string</code> (uint256)</p>                                                                                                                                                                                | `completionTime: number` (int64)                                                                                          | Initiates token unbonding from a validator                      |
| **`validator`**                 | `validatorAddress: string` (address)                                                                                                                                                                                                                                                                                    | `validator: { operatorAddress: string, jailed: boolean, tokens: string, ... }`                                            | Returns validator details by address                            |
| **`validators`**                | <p><code>status: string</code><br><code>pageRequest: { key: bytes, ... }</code></p>                                                                                                                                                                                                                                     | <p><code>validators: [{ operatorAddress: string, jailed: boolean, ... }]</code><br><code>pageResponse: { ... }</code></p> | Lists validators (filtered by status) with pagination           |

**Precompile Addresses**

0x0000000000000000000000000000000000000800

### Wasm Precompile

The wasm precompile makes wasm contracts available to being used via evm, with instantiate, query and execute.

**Functions**

| Function Name     | Input Parameters                                                                                                                                                                                                   | Return Value                  | Description                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------- |
| **`execute`**     | <p><code>contractAddress: string</code><br><code>msg: bytes</code> (JSON-encoded)<br><code>coins: [{ denom: string, amount: string }]</code></p>                                                                   | `success: boolean`            | Executes a contract method with optional token transfer |
| **`instantiate`** | <p><code>admin: string</code> (address)<br><code>codeID: number</code> (uint64)<br><code>label: string</code><br><code>msg: bytes</code> (init msg)<br><code>coins: [{ denom: string, amount: string }]</code></p> | `success: boolean`            | Deploys a new contract instance from stored code        |
| **`queryRaw`**    | <p><code>contractAddress: string</code><br><code>queryData: bytes</code> (raw query)</p>                                                                                                                           | `data: bytes` (raw response)  | Low-level contract query (returns raw bytes)            |
| **`querySmart`**  | <p><code>contractAddress: string</code><br><code>msg: bytes</code> (JSON-encoded query)</p>                                                                                                                        | `data: bytes` (JSON response) | Smart query (parses input/output as JSON)               |

**Precompile Addresses**

0x0000000000000000000000000000000000001001

\
<br>
