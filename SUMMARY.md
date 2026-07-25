# Table of contents

## Learn

* [What is KiiChain?](README.md)
* [KiiChain](learn/kiichain/README.md)
  * [Vision of KiiChain](learn/kiichain/vision-of-kiichain.md)
  * [Use Cases](learn/kiichain/use-cases.md)
  * [Roadmap](learn/kiichain/roadmap.md)
  * [Whitepaper](learn/kiichain/whitepaper.md)
* [Tokenomics](learn/tokenomics/README.md)
  * [Intro Coin Details](learn/tokenomics/intro-coin-details.md)
  * [Utility](learn/tokenomics/utility.md)
  * [Evergreen Model](learn/tokenomics/evergreen-model.md)
* [Getting Started](learn/getting-started/README.md)
  * [Get a Wallet](learn/getting-started/get-a-wallet.md)
  * [Download a Mobile Wallet](learn/getting-started/download-a-mobile-wallet.md)
  * [Set Up a Web Wallet](learn/getting-started/set-up-a-web-wallet.md)
  * [Connect Wallet to Explorer App](learn/getting-started/connect-wallet-to-explorer-app.md)
* [Kii Ambassadors](learn/kii-ambassadors.md)

## KiiChain Pay

* [Introduction](kiichain-pay/introduction/README.md)
  * [Generating API keys](kiichain-pay/introduction/generating-api-keys.md)
  * [Internal wallets](kiichain-pay/introduction/internal-wallets.md)
  * [Privy delegated access](kiichain-pay/introduction/privy-delegated-access.md)
  * [KYC](kiichain-pay/introduction/kyc.md)
* [Guides](kiichain-pay/guides/README.md)
  * [Quick Start](kiichain-pay/guides/quick-start/README.md)
    * [Creating an on-ramp](kiichain-pay/guides/quick-start/creating-an-on-ramp.md)
    * [Creating an off-ramp](kiichain-pay/guides/quick-start/creating-an-off-ramp.md)
    * [Creating an FX swap](kiichain-pay/guides/quick-start/creating-an-fx-swap.md)
    * [Creating a DEX swap](kiichain-pay/guides/quick-start/creating-a-dex-swap.md)
* [API Reference](kiichain-pay/api-reference/README.md)
  * [Accounts](kiichain-pay/api-reference/accounts.md)
  * [Blockchain](kiichain-pay/api-reference/blockchain.md)
  * [Ledger](kiichain-pay/api-reference/ledger.md)
  * [Market](kiichain-pay/api-reference/market.md)
  * [Notifications](kiichain-pay/api-reference/notifications.md)
  * [Portfolio](kiichain-pay/api-reference/portfolio.md)
  * [Tickets](kiichain-pay/api-reference/tickets.md)
  * [Users](kiichain-pay/api-reference/users.md)

## CONNECT TO KIIEX

* [Set up your Kii Account](connect-to-kiiex/set-up-your-kiiex-account/README.md)
  * [Upgrade your Account to Enterprise Level](connect-to-kiiex/set-up-your-kiiex-account/upgrade-your-account-to-enterprise-level.md)
* [Authenticate with API Key](connect-to-kiiex/authenticate-with-api-key.md)
* [Stablecoin FX Quick Start](connect-to-kiiex/stablecoin-fx-quick-start/README.md)
  * [Swap USDT to COPM with UI](connect-to-kiiex/stablecoin-fx-quick-start/swap-usdt-to-copm-with-ui.md)
* [Kii API's](connect-to-kiiex/kiiex-apis/README.md)
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

## BUILD ON KIICHAIN

* [Developer Hub](build-on-kiichain/developer-hub.md)
* [Testnet Oro](build-on-kiichain/testnet-oro.md)
* [Endpoints - EVM](build-on-kiichain/endpoints-evm.md)
* [Endpoints - Cosmos](build-on-kiichain/endpoints-cosmos/README.md)
  * [EVM](build-on-kiichain/endpoints-cosmos/evm/README.md)
    * [VM](build-on-kiichain/endpoints-cosmos/evm/vm.md)
    * [ERC20](build-on-kiichain/endpoints-cosmos/evm/erc20.md)
    * [FeeMarket](build-on-kiichain/endpoints-cosmos/evm/feemarket.md)
  * [IBC](build-on-kiichain/endpoints-cosmos/ibc.md)
  * [Kiichain](build-on-kiichain/endpoints-cosmos/kiichain/README.md)
    * [TokenFactory](build-on-kiichain/endpoints-cosmos/kiichain/tokenfactory.md)
  * [Cosmwasm](build-on-kiichain/endpoints-cosmos/cosmwasm.md)
  * [Cosmos](build-on-kiichain/endpoints-cosmos/cosmos/README.md)
    * [Auth](build-on-kiichain/endpoints-cosmos/cosmos/auth.md)
    * [Authz](build-on-kiichain/endpoints-cosmos/cosmos/authz.md)
    * [Bank](build-on-kiichain/endpoints-cosmos/cosmos/bank.md)
    * [Tendermint](build-on-kiichain/endpoints-cosmos/cosmos/tendermint.md)
    * [Consensus](build-on-kiichain/endpoints-cosmos/cosmos/consensus.md)
    * [Distribution](build-on-kiichain/endpoints-cosmos/cosmos/distribution.md)
    * [Evidence](build-on-kiichain/endpoints-cosmos/cosmos/evidence.md)
    * [Feegrant](build-on-kiichain/endpoints-cosmos/cosmos/feegrant.md)
    * [Gov](build-on-kiichain/endpoints-cosmos/cosmos/gov.md)
    * [Slashing](build-on-kiichain/endpoints-cosmos/cosmos/slashing.md)
    * [Staking](build-on-kiichain/endpoints-cosmos/cosmos/staking.md)
    * [Tx](build-on-kiichain/endpoints-cosmos/cosmos/tx.md)
    * [Upgrade](build-on-kiichain/endpoints-cosmos/cosmos/upgrade.md)
* [Developer Tools](build-on-kiichain/developer-tools/README.md)
  * [RWA Protocol](build-on-kiichain/developer-tools/rwa-protocol.md)
  * [Rust SDK](build-on-kiichain/developer-tools/rust-sdk.md)
  * [JS/TS SDK](build-on-kiichain/developer-tools/js-ts-sdk/README.md)
    * [Kiijs-evm](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-evm.md)
    * [Kiijs-proto](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-proto.md)
    * [Kiijs-utils](build-on-kiichain/developer-tools/js-ts-sdk/kiijs-utils.md)
  * [Deploy a smart contract](build-on-kiichain/developer-tools/deploy-a-smart-contract.md)
  * [Deploy a dApp](build-on-kiichain/developer-tools/deploy-a-dapp.md)
  * [Testnet faucet](build-on-kiichain/developer-tools/testnet-faucet.md)
  * [Resources](build-on-kiichain/developer-tools/resources.md)
  * [Precompiled Contracts](build-on-kiichain/developer-tools/precompiled-contracts.md)
* [Smart Contracts](build-on-kiichain/smart-contracts.md)
* [Wasmbindings](build-on-kiichain/wasmbindings.md)
* [Modules](build-on-kiichain/modules/README.md)
  * [TokenFactory](build-on-kiichain/modules/tokenfactory.md)
  * [EVM](build-on-kiichain/modules/evm.md)
  * [Rewards](build-on-kiichain/modules/rewards.md)
  * [Oracle](build-on-kiichain/modules/oracle.md)
  * [Fee Abstraction](build-on-kiichain/modules/fee-abstraction.md)
* [Precompiled contracts](build-on-kiichain/precompiled-contracts/README.md)
  * [Oracle Precompile](build-on-kiichain/precompiled-contracts/oracle-precompile.md)

## Validate the Network

* [Getting Started](validate-the-network/getting-started/README.md)
  * [What is a delegator?](validate-the-network/getting-started/what-is-a-delegator.md)
  * [What is a validator?](validate-the-network/getting-started/what-is-a-validator.md)
  * [What is an Oracle?](validate-the-network/getting-started/what-is-an-oracle.md)
* [Run a Validator / Full Node](validate-the-network/run-a-validator-full-node/README.md)
  * [Getting started](validate-the-network/run-a-validator-full-node/getting-started.md)
  * [Step-by-Step Guide](validate-the-network/run-a-validator-full-node/step-by-step-guide/README.md)
    * [Becoming a Validator](validate-the-network/run-a-validator-full-node/step-by-step-guide/becoming-a-validator.md)
    * [Recovering Legacy Addresses](validate-the-network/run-a-validator-full-node/step-by-step-guide/recovering-legacy-addresses.md)
  * [Maintaining a validator](validate-the-network/run-a-validator-full-node/maintaining-a-validator.md)
  * [Running the Price feeder](validate-the-network/run-a-validator-full-node/running-the-price-feeder.md)
  * [Incentive](validate-the-network/run-a-validator-full-node/incentive.md)
  * [Technical requirements](validate-the-network/run-a-validator-full-node/technical-requirements.md)
  * [Validator Security](validate-the-network/run-a-validator-full-node/validator-security.md)
  * [Further guides](validate-the-network/run-a-validator-full-node/further-guides.md)
* [Economics](validate-the-network/economics/README.md)
  * [Staking Requirements](validate-the-network/economics/staking-requirements.md)
  * [Delegation / Staking](validate-the-network/economics/delegation-staking.md)
  * [Rewards](validate-the-network/economics/rewards.md)
  * [Block Rewards Formula](validate-the-network/economics/block-rewards-formula.md)
  * [APR](validate-the-network/economics/apr.md)
* [Delegator Information](validate-the-network/delegator-information/README.md)
  * [Choosing a validator](validate-the-network/delegator-information/choosing-a-validator.md)
  * [Directives of delegators](validate-the-network/delegator-information/directives-of-delegators.md)
  * [Incentive to stake](validate-the-network/delegator-information/incentive-to-stake.md)
  * [Security considerations](validate-the-network/delegator-information/security-considerations.md)
  * [Risks to consider](validate-the-network/delegator-information/risks-to-consider.md)

***

* [Legal & Risk Disclaimer](legal-and-risk-disclaimer.md)
