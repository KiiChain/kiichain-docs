---
description: Incentives for validating the network.
---

# Incentive

### What is the incentive to stake? <a href="#what-is-the-incentive-to-stake" id="what-is-the-incentive-to-stake"></a>

Each member of a validator's staking pool earns different types of revenue:

* **Block rewards:** Native tokens of applications (eg. KII) run by validators are inflated to produce block provisions. These provisions exist to incentivize KII holders to bond their stake. Non-bonded KII are diluted over time.
* **Transaction fees:** The only fee token of Kiichain is the `KII`.

This total revenue is divided among validators' staking pools according to each validator's weight. Then, within each validator's staking pool the revenue is divided among delegators in proportion to each delegator's stake. A commission on delegators' revenue is applied by the validator before it is distributed.

### What is a validator commission? <a href="#what-is-a-validator-commission" id="what-is-a-validator-commission"></a>

Revenue received by a validator's pool is split between the validator and their delegators. The validator can apply a commission on the part of the revenue that goes to their delegators. This commission is set as a percentage. Each validator is free to set their initial commission, maximum daily commission change rate, and maximum commission. Kii Global enforces the parameter that each validator sets. The maximum commission rate is fixed and cannot be changed. However, the commission rate itself can be changed after the validator is created as long as it does not exceed the maximum commission.

### What is the incentive to run a validator? <a href="#what-is-the-incentive-to-run-a-validator" id="what-is-the-incentive-to-run-a-validator"></a>

Validators earn proportionally more revenue than their delegators because of the commission they take on the staking rewards from their delegators.

Validators also play a major role in governance. If a delegator does not vote, they inherit the vote from their validator. This voting inheritance gives validators a major responsibility in the ecosystem. On-chain governance is live from genesis and covers technical protocol matters such as network parameters, validator set size, and protocol upgrades.&#x20;

### How are block rewards distributed? <a href="#how-are-block-rewards-distributed" id="how-are-block-rewards-distributed"></a>

Block rewards are distributed proportionally to all validators relative to their voting power. This means that even though each validator gains ATOM with each reward, all validators maintain equal weight over time.

For example, 10 validators have equal voting power and a commission rate of 1%. For this example, the reward for a block is 1000 KII and each validator has 20% of self-bonded KII. These tokens do not go directly to the proposer. Instead, the tokens are evenly spread among validators. So now each validator's pool has 100 KII. These 100 KII are distributed according to each participant's stake:

* Commission: `100*80%*1% = 0.8 KII`
* Validator gets: `100\*20% + Commission = 20.8 KII`
* All delegators get: `100\*80% - Commission = 79.2 KII`

Then, each delegator can claim their part of the 79.2 KII in proportion to their stake in the validator's staking pool.

### How are fees distributed? <a href="#how-are-fees-distributed" id="how-are-fees-distributed"></a>

Fees are similarly distributed with the exception that the block proposer can get a bonus on the fees of the block they propose if the proposer includes more than the strict minimum of required precommits.

When a validator is selected to propose the next block, the validator must include at least 2/3 precommits of the previous block. However, an incentive to include more than 2/3 precommits is a bonus. The bonus is linear: it ranges from 1% if the proposer includes 2/3rd precommits (minimum for the block to be valid) to 5% if the proposer includes 100% precommits. Of course the proposer must not wait too long or other validators may timeout and move on to the next proposer. As such, validators have to find a balance between wait-time to get the most signatures and risk of losing out on proposing the next block. This mechanism aims to incentivize non-empty block proposals, better networking between validators, and mitigates censorship.

For a concrete example to illustrate the aforementioned concept, there are 10 validators with equal stake. Each validator applies a 1% commission rate and has 20% of self-delegated KII. Now comes a successful block that collects a total of 1025.51020408 KII in fees.

First, a 2% tax is applied. The corresponding KII go to the reserve pool. The reserve pool's funds can be allocated through governance to fund bounties and upgrades.

* `2% * 1025.51020408 = 20.51020408` KII go to the reserve pool.

1005 KII now remain. For this example, the proposer included 100% of the signatures in its block so the proposer obtains the full bonus of 5%.

To solve this simple equation to find the reward R for each validator:

`9*R + R + R*5% = 1005 ⇔ R = 1005/10.05 = 100`

* For the proposer validator:
  * The pool obtains `R + R * 5%`: 105 KII
  * Commission: `105 * 80% * 1%` = 0.84 KII
  * Validator's reward: `105 * 20% + Commission` = 21.84 KII
  * Delegators' rewards: `105 * 80% - Commission` = 83.16 KII (each delegator is able to claim its portion of these rewards in proportion to their stake)
* For each non-proposer validator:
  * The pool obtains R: 100 KII
  * Commission: `100 * 80% * 1%` = 0.8 KII
  * Validator's reward: `100 * 20% + Commission` = 20.8 KII
  * Delegators' rewards: `100 * 80% - Commission` = 79.2 KII (each delegator is able to claim their portion of these rewards in proportion to their stake)

### What are the slashing conditions? <a href="#what-are-the-slashing-conditions" id="what-are-the-slashing-conditions"></a>

If a validator misbehaves, their delegated stake is partially slashed. Two faults can result in slashing of funds for a validator and their delegators:

* **Double signing:** If someone reports on chain A that a validator signed two blocks at the same height on chain A and chain B, and if chain A and chain B share a common ancestor, then this validator gets slashed by 5% on chain A.
* **Downtime:** If a validator misses more than `95%` of the last `10,000` blocks (roughly \~19 hours), they are slashed by 0.01%.

### Are validators required to self-delegate KII? <a href="#are-validators-required-to-self-delegate-atom" id="are-validators-required-to-self-delegate-atom"></a>

No, they do not need to self-delegate. Even though there is no obligation for validators to self-delegate, delegators may want their validator to have self-delegated KII in their staking pool. In other words, validators share the risk.

Note however that it's possible that some validators decide to self-delegate via a different address for security reasons.

### How to prevent concentration of stake in the hands of a few top validators? <a href="#how-to-prevent-concentration-of-stake-in-the-hands-of-a-few-top-validators" id="how-to-prevent-concentration-of-stake-in-the-hands-of-a-few-top-validators"></a>

The community is expected to behave in a smart and self-preserving way. When a mining pool in Bitcoin gets too much mining power the community usually stops contributing to that pool. Kiichain relies on the same effect. Additionally, when delegators switch to another validator, they are not subject to the unbonding period, which removes any barrier to quickly redelegating tokens in service of improving decentralization.
