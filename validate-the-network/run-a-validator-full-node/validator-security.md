---
description: Protect your validator from malicious attacks.
---

# Validator Security

Each validator candidate is encouraged to run its operations independently, as diverse setups increase the resilience of the network. Validator candidates should commence their setup phase now in order to be on time for launch.

### Key Management - HSM <a href="#key-management-hsm" id="key-management-hsm"></a>

It is mission critical that an attacker cannot steal a validator's key. If this is possible, it puts the entire stake delegated to the compromised validator at risk. Hardware security modules are an important strategy for mitigating this risk.

HSM modules must support `ed25519` signatures for the hub. The YubiHSM2 supports `ed25519` and [this yubikey library is available (opens new window)](https://github.com/iqlusioninc/yubihsm.rs). The YubiHSM can protect a private key but cannot ensure in a secure setting that it won't sign the same block twice.

### Sentry Nodes (DDOS Protection) <a href="#sentry-nodes-ddos-protection" id="sentry-nodes-ddos-protection"></a>

Validators are responsible for ensuring that the network can sustain denial of service attacks.

One recommended way to mitigate these risks is for validators to carefully structure their network topology in a so-called sentry node architecture.

Validator nodes should only connect to full-nodes they trust because they operate them themselves or are run by other validators they know socially. A validator node will typically run in a data center. Most data centers provide direct links to the networks of major cloud providers. The validator can use those links to connect to sentry nodes in the cloud. This shifts the burden of denial-of-service from the validator's node directly to its sentry nodes, and may require new sentry nodes be spun up or activated to mitigate attacks on existing ones.

Sentry nodes can be quickly spun up or change their IP addresses. Because the links to the sentry nodes are in private IP space, an internet-based attack cannot disturb them directly. This will ensure validator block proposals and votes always make it to the rest of the network.

To setup your sentry node architecture you can follow the instructions below:

Validators nodes should edit their `config.toml`:

```
# Comma separated list of nodes to keep persistent connections to 
# Do not add private peers to this list if you don't want them advertised 
persistent_peers =[list of sentry nodes] 
# Set true to enable the peer-exchange reactor 
pex = false
```

Sentry Nodes should edit their `config.toml`:

```
# Comma separated list of peer IDs to keep private (will not be gossiped to other peers) 
# Example ID: 3e16af0cead27979e1fc3dac57d03df3c7a77acc@3.87.179.235:26656 
private_peer_ids = "node_ids_of_private_peers"
```

### Environment Variables <a href="#environment-variables" id="environment-variables"></a>

By default, uppercase environment variables with the following prefixes will replace lowercase command-line flags:

* `GA` (for Gaia flags)
* `TM` (for Tendermint/CometBFT flags)
* `BC` (for democli or basecli flags)

For example, the environment variable `GA_CHAIN_ID` will map to the command line flag `--chain-id`. Note that while explicit command-line flags will take precedence over environment variables, environment variables will take precedence over any of your configuration files. For this reason, it's imperative that you lock down your environment such that any critical parameters are defined as flags on the CLI or prevent modification of any environment variables.
