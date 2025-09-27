# Table of Contents

## Learn

* [What is Kii?](README.md)
* [What is KiiChain?](learn/readme-1.md)
* [KiiChain](learn/kiichain/README.md)
  * [Vision of KiiChain](learn/kiichain/vision-of-kiichain.md)
  * [Blockchain features](learn/kiichain/blockchain-features.md)
  * [The problems we solve](learn/kiichain/the-problems-we-solve.md)
  * [Use cases](learn/kiichain/use-cases.md)
  * [Roadmap](learn/kiichain/roadmap.md)
  * [Whitepaper](learn/kiichain/whitepaper.md)
  * [Business model](learn/kiichain/business-model.md)
* [Tokenomics](learn/tokenomics/README.md)
  * [Intro coin details](learn/tokenomics/intro-coin-details.md)
  * [Coin distribution](learn/tokenomics/coin-distribution.md)
  * [Coin unlocking schedule](learn/tokenomics/coin-unlocking-schedule.md)
  * [Utility](learn/tokenomics/utility.md)
  * [Evergreen model](learn/tokenomics/evergreen-model.md)
* [Getting started](learn/getting-started/README.md)
  * [Get a wallet](learn/getting-started/get-a-wallet.md)
  * [Download a mobile wallet](learn/getting-started/download-a-mobile-wallet.md)
  * [Set up a web wallet](learn/getting-started/set-up-a-web-wallet.md)
  * [Connect wallet to Explorer app](learn/getting-started/connect-wallet-to-explorer-app.md)

---

* [Kii Ambassadors](kii-ambassadors.md)

## Connect to KiiEx

* [Set up your KiiEx account](connect-to-kiiex/set-up-your-kiiex-account/README.md)
  * [Upgrade your account to enterprise level](connect-to-kiiex/set-up-your-kiiex-account/upgrade-your-account-to-enterprise-level.md)
* [Authenticate with API key](connect-to-kiiex/authenticate-with-api-key.md)
* [Stablecoin FX quick start](connect-to-kiiex/stablecoin-fx-quick-start/README.md)
  * [Swap USDT to COPM with UI](connect-to-kiiex/stablecoin-fx-quick-start/swap-usdt-to-copm-with-ui.md)
* [Kii APIs](connect-to-kiiex/kiiex-apis/README.md)
  * ```yaml
    props:
      models: true
    type: builtin:openapi
    dependencies:
      spec:
        ref:
          kind: openapi
          spec: kiiex-all-calls
    ```

## Build on KiiChain

* [Developer hub](build-on-kiichain/developer-hub.md)
* [Testnet Oro](build-on-kiichain/testnet-oro.md)
* [Endpoints - Cosmos](build-on-kiichain/endpoints-cosmos/README.md)
  * [EVM](build-on-kiichain/endpoints-cosmos/evm/README.md)
    * [VM](build-on-kiichain/endpoints-cosmos/evm/vm.md)
    * [ERC20](build-on-kiichain/endpoints-cosmos/evm/erc20.md)
    * [Fee market](build-on-kiichain/endpoints-cosmos/evm/feemarket.md)
  * [IBC](build-on-kiichain/endpoints-cosmos/ibc.md)
  * [KiiChain](build-on-kiichain/endpoints-cosmos/kiichain/README.md)
    * [Token factory](build-on-kiichain/endpoints-cosmos/kiichain/tokenfactory.md)
  * [CosmWasm](build-on-kiichain/endpoints-cosmos/cosmwasm.md)
  * [Cosmos](build-on-kiichain/endpoints-cosmos/cosmos/README.md)
    * [Auth](build-on-kiichain/endpoints-cosmos/cosmos/auth.md)
    * [Authz](build-on-kiichain/endpoints-cosmos/cosmos/authz.md)
    * [Bank](build-on-kiichain/endpoints-cosmos/cosmos/bank.md)
    * [Tendermint](build-on-kiichain/endpoints-cosmos/cosmos/tendermint.md)
    * [Consensus](build-on-kiichain/endpoints-cosmos/cosmos/consensus.md)
    * [Distribution](build-on-kiichain/endpoints-cosmos/cosmos/distribution.md)
    * [Evidence](build-on-kiichain/endpoints-cosmos/cosmos/evidence.md)
    * [Feegrant](build-on-kiichain/endpoints-cosmos/cosmos/feegrant.md)
    * [Governance](build-on-kiichain/endpoints-cosmos/cosmos/gov.md)
    * [Slashing](build-on-kiichain/endpoints-cosmos/cosmos/slashing.md)
    * [Staking](build-on-kiichain/endpoints-cosmos/cosmos/staking.md)
    * [Transactions](build-on-kiichain/endpoints-cosmos/cosmos/tx.md)
    * [Upgrade](build-on-kiichain/endpoints-cosmos/cosmos/upgrade.md)
* [Developer tools](build-on-kiichain/developer-tools/README.md)
  * [RWA protocol](build-on-kiichain/developer-tools/rwa-protocol.md)
  * [Rust SDK](build-on-kiichain/developer-tools/rust-sdk.md)
  * [JS/TS SDK](build-on-kiichain/developer-tools/js-ts-sdk/README.md)
    * [Kii EVM SDK](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-evm.md)
    * [Kii Proto SDK](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-proto.md)
    * [Kii Utils SDK](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-utils.md)
  * [Deploy a smart contract](build-on-kiichain/developer-tools/deploy-a-smart-contract.md)
  * [Deploy a dApp](build-on-kiichain/developer-tools/deploy-a-dapp.md)
  * [Testnet faucet](build-on-kiichain/developer-tools/testnet-faucet.md)
  * [Resources](build-on-kiichain/developer-tools/resources.md)
  * [Precompiled contracts](build-on-kiichain/developer-tools/precompiled-contracts.md)
* [Smart contracts](build-on-kiichain/smart-contracts.md)
* [Modules](build-on-kiichain/modules/README.md)
  * [Token factory](build-on-kiichain/modules/tokenfactory.md)
  * [EVM](build-on-kiichain/modules/evm.md)
  * [Rewards](build-on-kiichain/modules/rewards.md)
  * [Oracle](build-on-kiichain/modules/oracle.md)
  * [Fee abstraction](build-on-kiichain/modules/fee-abstraction.md)

---

* [Precompiled contracts](precompiled-contracts.md)

## Validate the Network

* [Getting started](validate-the-network/getting-started/README.md)
  * [What is a delegator?](validate-the-network/getting-started/what-is-a-delegator.md)
  * [What is a validator?](validate-the-network/getting-started/what-is-a-validator.md)
  * [What is an oracle?](validate-the-network/getting-started/what-is-an-oracle.md)
* [Run a validator / full node](validate-the-network/run-a-validator-full-node/README.md)
  * [Getting started](validate-the-network/run-a-validator-full-node/getting-started.md)
  * [Step-by-step guide](validate-the-network/run-a-validator-full-node/step-by-step-guide/README.md)
    * [Becoming a validator](validate-the-network/run-a-validator-full-node/step-by-step-guide/becoming-a-validator.md)
    * [Recovering legacy addresses](validate-the-network/run-a-validator-full-node/step-by-step-guide/recovering-legacy-addresses.md)
  * [Maintaining a validator](validate-the-network/run-a-validator-full-node/maintaining-a-validator.md)
  * [Running the price feeder](validate-the-network/run-a-validator-full-node/running-the-price-feeder.md)
  * [Incentives](validate-the-network/run-a-validator-full-node/incentive.md)
  * [Technical requirements](validate-the-network/run-a-validator-full-node/technical-requirements.md)
  * [Validator security](validate-the-network/run-a-validator-full-node/validator-security.md)
* [Economics](validate-the-network/economics/README.md)
  * [Staking requirements](validate-the-network/economics/staking-requirements.md)
  * [Delegation / staking](validate-the-network/economics/delegation-staking.md)
  * [Rewards](validate-the-network/economics/rewards.md)
  * [Block rewards formula](validate-the-network/economics/block-rewards-formula.md)
  * [APR](validate-the-network/economics/apr.md)
* [Delegator information](validate-the-network/delegator-information/README.md)
  * [Choosing a validator](validate-the-network/delegator-information/choosing-a-validator.md)
  * [Directives of delegators](validate-the-network/delegator-information/directives-of-delegators.md)
  * [Incentives to stake](validate-the-network/delegator-information/incentive-to-stake.md)
  * [Security considerations](validate-the-network/delegator-information/security-considerations.md)
  * [Risks to consider](validate-the-network/delegator-information/risks-to-consider.md)
