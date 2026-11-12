# Rewards

The rewards module (also called the Utility Rewards Module) pays staking rewards from a prefunded pool. Each block it moves tokens from its module account into the `fee_collector`, and the distribution module pays them out to validators and delegators in the same way as transaction fees.

The amount released each block follows an inflation curve driven by the bonded ratio, the same model as the Cosmos SDK `x/mint` module.

{% hint style="info" %}
The rewards module **does not mint KII**. Every token it pays out must first be sent to the module account. Emissions stop when that account is empty.
{% endhint %}

Emissions are off by default (`supply_base = 0`). Governance turns them on.

### Flow

1. Fund the pool: send tokens to the rewards module account with a normal bank send. Anyone can do this.
2. Pass a governance proposal with `MsgUpdateParams` that sets `supply_base` above `0`.
3. At the start of each block, the module releases `inflation(bondedRatio) × supply_base / blocks_per_year` into the fee collector.
4. Emissions continue until the module account is empty or governance sets `supply_base` back to `0`.

The rewards module runs before the distribution module in each block, so a block's release is paid out in that same block.

### Module account

| Format | Address                                      |
| ------ | -------------------------------------------- |
| Bech32 | `kii1245yut9zht8q4hz39sd0lzqtzkuw5us5rermc4` |
| Hex    | `0x55684e2ca2bace0adc512c1aff880b15b8ea7214` |

The address is derived from the module name, so it is the same on every KiiChain network.

### Interaction with other modules

<table><thead><tr><th width="181.5">Module</th><th>Interaction</th></tr></thead><tbody><tr><td>Bank</td><td>Holds the pool as the rewards module account balance; moves the release from the module account to the fee collector</td></tr><tr><td>Staking</td><td>Provides the bonded ratio that drives the emission curve</td></tr><tr><td>Distribution</td><td>Pays the fee collector balance out to validators and delegators</td></tr><tr><td>Governance</td><td>The only account that can change module params, including enabling and disabling emissions</td></tr></tbody></table>

### Emission formula

```
inflation = clamp((1 - bondedRatio / goalBonded) × inflationRateChange × bondedRatio,
                  inflationMin, inflationMax)
amount    = inflation × supplyBase / blocksPerYear
pay       = min(amount, moduleBalance)
```

| Term                            | Meaning                                                                    |
| ------------------------------- | -------------------------------------------------------------------------- |
| `bondedRatio`                   | Bonded tokens divided by total staking-token supply, read from the staking module |
| `goalBonded`                    | Target bonded ratio (param `goal_bonded`)                                  |
| `inflationRateChange`           | Steepness of the curve (param `inflation_rate_change`)                     |
| `inflationMin` / `inflationMax` | Floor and ceiling on the annual emission rate                              |
| `supplyBase`                    | Notional base used to size annual provisions (param `supply_base`)        |
| `blocksPerYear`                 | Expected number of blocks per year (param `blocks_per_year`)               |
| `moduleBalance`                 | Rewards module account balance in `token_denom`                            |

If the calculated amount is larger than the module balance, the block pays only the balance.

#### Curve shape

Before clamping, the curve is a parabola in the bonded ratio:

* It is `0` when nothing is bonded and when `bondedRatio = goalBonded`.
* It peaks at `bondedRatio = goalBonded / 2`, with value `inflationRateChange × goalBonded / 4`.
* Above `goalBonded` it would go negative, so the clamp returns `inflationMin`.

With the default params, the peak rate is `0.13 × 0.67 / 4 = 2.1775%` per year. The default `inflation_max` of 20% does not come into play unless `inflation_rate_change` or `goal_bonded` is raised.

{% hint style="warning" %}
This curve is different from `x/mint`. Here the rate rises as the bonded ratio climbs toward `goalBonded / 2`, then falls to the floor as it approaches `goalBonded`.
{% endhint %}

#### `supply_base` is not the total supply

The annual provision is `inflation × supply_base`. `supply_base` is a governance setting that controls the scale of emissions. It is **not** read from the chain's total supply. It is an integer in base units of `token_denom` (`akii`, 18 decimals).

#### Per block, not per second

Each block releases a fixed share of the annual provision (`annual / blocks_per_year`), as in `x/mint`. Release does not depend on elapsed time. If blocks are slower than `blocks_per_year` assumes, less is released per calendar year. The default `15778800` assumes 2-second blocks.

#### Example

Default params, with `supply_base = 1000000000000000000000000000` (1,000,000,000 KII):

| Bonded ratio | Inflation  | Annual provision | Per block  |
| ------------ | ---------- | ---------------- | ---------- |
| 0.335 (peak) | 2.1775%    | 21,775,000 KII   | \~1.380 KII |
| 0.50         | \~1.6493%  | \~16,492,537 KII | \~1.045 KII |
| 0.67 or more | 0% (floor) | 0                | 0          |

### Each block

At the start of every block the module:

1. Does nothing if `supply_base` is `0` or the module account is empty.
2. Reads the bonded ratio and calculates the release.
3. Caps the release at the module account balance.
4. Sends the release to the fee collector.
5. Adds the release to `total_released` and emits a `reward_distributed` event.

If reading the bonded ratio or sending the funds fails, the module logs the error and skips that block. The chain does not halt.

### Params

| Param                   | Default    | Rule                     | Description                                         |
| ----------------------- | ---------- | ------------------------ | --------------------------------------------------- |
| `token_denom`           | `akii`     | Valid denom              | Denom paid out                                      |
| `goal_bonded`           | `0.67`     | `0 < x ≤ 1`              | Target bonded ratio                                 |
| `inflation_min`         | `0`        | `≥ 0`                    | Floor on the annual rate                            |
| `inflation_max`         | `0.20`     | `≥ inflation_min`        | Ceiling on the annual rate                          |
| `supply_base`           | `0`        | `≥ 0`                    | Emission scale in base units. `0` turns emissions off |
| `inflation_rate_change` | `0.13`     | `0 < x ≤ 1`              | Curve steepness                                     |
| `blocks_per_year`       | `15778800` | `> 0`                    | Expected blocks per year                            |

### Internal state

```go
type RewardPool struct {
    // Cumulative amount sent to the fee collector
    TotalReleased types.Coin `protobuf:"bytes,3,opt,name=total_released,json=totalReleased,proto3" json:"total_released" yaml:"total_released"`
}
```

`RewardPool` only tracks what has been released. The funds available to pay out are the module account balance in the bank module.

### Messages

#### Update Params

Changes module params. Only the governance module account can send it, so others need to pass a proposal. All params must be supplied.

```protobuf
message MsgUpdateParams {
  // authority is the address of the governance account.
  string authority = 1 [ (cosmos_proto.scalar) = "cosmos.AddressString" ];

  // params defines the x/rewards parameters to update.
  //
  // NOTE: All parameters must be supplied.
  Params params = 2 [ (gogoproto.nullable) = false ];
}

message Params {
  string token_denom = 1;
  string goal_bonded = 2;           // LegacyDec, e.g. "0.67"
  string inflation_min = 3;         // LegacyDec, e.g. "0.00"
  string inflation_max = 4;         // LegacyDec, e.g. "0.20"
  string supply_base = 5;           // Int, base units; 0 disables emissions
  string inflation_rate_change = 6; // LegacyDec, e.g. "0.13"
  uint64 blocks_per_year = 7;
}
```

**State Modifications:**

* Validates and replaces all module params
* Setting `supply_base` above `0` starts emissions; setting it to `0` stops them. Funds stay in the module account.
* Emits an `update_params` event

#### Funding the pool

There is no fund message. Send tokens to the module account with a bank send:

```bash
kiichaind tx bank send <from> kii1245yut9zht8q4hz39sd0lzqtzkuw5us5rermc4 1000000000000000000000akii
```

### Enabling emissions

Create `proposal.json`:

```json
{
  "messages": [
    {
      "@type": "/kiichain.rewards.v1.MsgUpdateParams",
      "authority": "kii10d07y265gmmuvt4z0w9aw880jnsr700jrff0qv",
      "params": {
        "token_denom": "akii",
        "goal_bonded": "0.67",
        "inflation_min": "0",
        "inflation_max": "0.20",
        "supply_base": "1000000000000000000000000000",
        "inflation_rate_change": "0.13",
        "blocks_per_year": "15778800"
      }
    }
  ],
  "metadata": "",
  "deposit": "10000000akii",
  "title": "Enable utility rewards emissions",
  "summary": "Set supply_base to start x/rewards emissions"
}
```

Submit it:

```bash
kiichaind tx gov submit-proposal proposal.json --from <key>
```

Set the deposit to at least the governance minimum deposit for the network. To stop emissions, submit the same proposal with `"supply_base": "0"`.

### Queries

| CLI                              | REST                                   | Returns                                                     |
| -------------------------------- | -------------------------------------- | ----------------------------------------------------------- |
| `kiichaind q rewards params`      | `GET /kiichain/rewards/v1/params`      | Module params                                               |
| `kiichaind q rewards reward-pool` | `GET /kiichain/rewards/v1/reward-pool` | `total_released` and the module account balance (`balance`) |

### Events

| Type                 | Attributes                                                   | When                                    |
| -------------------- | ------------------------------------------------------------ | --------------------------------------- |
| `update_params`      | —                                                            | Params are updated                      |
| `reward_distributed` | `amount`, `total_released`, `inflation_rate`, `bonded_ratio` | A release is sent to the fee collector  |

### Upgrading from the release schedule

Earlier versions of the module released a fixed budget linearly until an end date (`ReleaseSchedule`). That model was removed in consensus version 2, together with `MsgChangeSchedule`, `MsgFundPool`, and the release-schedule query and CLI.

The upgrade migration deletes the old schedule, fills the new params with defaults, and keeps the existing `token_denom`. `supply_base` stays `0`, so emissions stay off until governance enables them.

The API package is now `kiichain.rewards.v1`. The old `kiichain.rewards.v1beta1` types are still registered so existing transactions and proposals decode:

| v1beta1                 | Behavior                                                   |
| ----------------------- | ---------------------------------------------------------- |
| `MsgUpdateParams`       | Updates only `token_denom`                                 |
| `MsgFundPool`           | Returns an error. Use a bank send to the module account.   |
| `MsgChangeSchedule`     | Returns an error                                           |
| `Query/Params`          | Returns `token_denom` only                                 |
| `Query/RewardPool`      | Reports the module account balance as `community_pool`     |
| `Query/ReleaseSchedule` | Returns an error                                           |
