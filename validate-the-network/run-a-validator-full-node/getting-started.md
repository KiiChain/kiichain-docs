---
description: >-
  Everyone is welcome to launch their own validator. Please review all
  information carefully.
---

# Getting started

### How to become a validator? <a href="#how-to-become-a-validator" id="how-to-become-a-validator"></a>

Any participant in the network can signal that they want to become a validator by sending a `create-validator` transaction, where they must fill out the following parameters:

* **Validator's Pubkey:** The private key associated with this Tendermint `PubKey` is used to sign _prevotes_ and _precommits_.
* **Validator's Address:** Application level address that is used to publicly identify your validator. The private key associated with this address is used to delegate, unbond, claim rewards, and participate in governance.
* **Validator's name**&#x20;
* **Validator's website (Optional)**
* **Validator's description (Optional)**
* **Initial commission rate**: The commission rate on block rewards and fees charged to delegators.
* **Maximum commission:** The maximum commission rate that this validator can charge. This parameter is fixed and cannot be changed after the `create-validator` transaction is processed.
* **Commission max change rate:** The maximum daily increase of the validator commission. This parameter is fixed cannot be changed after the `create-validator` transaction is processed.

After a validator is created, KII holders can delegate KII to them, effectively adding stake to the validator's pool. The total stake of an address is the combination of KII bonded by delegators and KII self-bonded by the validator.

From all validator candidates that signaled themselves, the 100 validators with the most total stake are the designated **validators**. If a validator's total stake falls below the top 100, then that validator loses its validator privileges. The validator cannot participate in consensus or generate rewards until the stake is high enough to be in the top 100. Over time, the maximum number of validators may be increased via on-chain governance proposal.

## Run a Local Full Node (For Development & Testing)

You can simulate a KiiChain validator environment locally. This is useful for:

- Testing validator commands
- Understanding consensus flow
- Experimenting without risking real funds

### Prerequisites

Make sure the following tools are installed:

- [Go](https://go.dev/dl/) ≥ 1.21
- Git
- Make

### Steps

1. Clone the repo:

   ```bash
   git clone https://github.com/KiiChain/kiichain.git
   cd kiichain
   make install
   kiid init my-local-node --chain-id kii-local
   kiid keys add mykey
   kiid add-genesis-account $(kiid keys show mykey -a) 1000000000ukii
   kiid gentx mykey 700000000ukii --chain-id kii-local
   kiid collect-gentxs
   kiid start
   ```
