---
description: Join the testnet, set up your wallet, and request KII tokens.
---

# Testnet faucet

### About the Faucet

Testnet participation is a great way to signal to the community that you are ready and able to operate a validator.

Important to create your web wallet first and then link to the explorer app.&#x20;

* [Testnet explorer app](https://explorer.kiichain.io/faucet)

Testnet KII can be found in the faucet in Discord and on our Explorer App. It can be called on every 24 hours.

* [Discord Kiichain Invitation](https://discord.com/invite/kiichain)

### Discord Faucet Commands

Request tokens:

```
$request {address}
```

Example EVM:

```
$request 0x12345abcde…
```

Example CW:&#x20;

```
$request kii12345abcde…
```

### List of Commands:

See all available commands:

```
$help
```

Request tokens:

```
$request [kii address]
```

Query an address balance:

```
$balance [kii address]
```

Query a transaction:

```
$tx_info [transaction hash ID]
```

Query the faucet and node status:

```
$faucet_status [chain ID]
```

Query the faucet address:

```
$faucet_address [chain ID]
```
