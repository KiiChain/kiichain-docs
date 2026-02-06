---
description: >-
  The oracle precompile provides access to real-time exchange rate data and
  time-weighted average prices (TWAPs) for different denominations.
---

# Oracle Precompile

### **Functions**

| Function Name          | Input Parameters                                    | Return Value                                                                                                                                              | Description                                                                                        |
| ---------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **`getExchangeRate`**  | `denom: string` (currency denomination)             | <p><code>rate: string</code><br><code>lastUpdate: string</code><br><code>lastUpdateTimestamp: int64</code></p>                                            | Gets the current exchange rate for a specific denomination with update metadata                    |
| **`getExchangeRates`** | None                                                | <p><code>denoms: string[]</code><br><code>rates: string[]</code><br><code>lastUpdate: string[]</code><br><code>lastUpdateTimestamps: uint256[]</code></p> | Gets exchange rates for all available denominations with update metadata                           |
| **`getTwaps`**         | `lookbackSeconds: uint256` (time window in seconds) | <p><code>denoms: string[]</code><br><code>twaps: string[]</code></p>                                                                                      | Gets time-weighted average prices (TWAPs) for all denominations over the specified lookback period |

**Precompile Address**

`0x0000000000000000000000000000000000001003`
