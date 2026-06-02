---
description: For hardware and software protocols.
---

# Technical requirements

### Recommended configuration

For optimal performance, we recommend:

* 4 vCPU x86\_64
* 8 GB RAM
* 1 TB NVME SSD

A modest level of hardware specifications is initially required and rises as network use increases.

Validators are recommended to set up sentry nodes to protect your validator node from DDoS attacks.

### What are software requirements? <a href="#what-are-software-requirements" id="what-are-software-requirements"></a>

Validators are expected to implement monitoring, alerting, and management solutions. There are several tools that you can use.

### What are bandwidth requirements? <a href="#what-are-bandwidth-requirements" id="what-are-bandwidth-requirements"></a>

Kiichain has the capacity for very high throughput relative to chains like Dash, Ethereum or Bitcoin.

We recommend that the data center nodes connect only to trusted full nodes in the cloud or other validators that know each other socially. This connection strategy relieves the data center node from the burden of mitigating denial-of-service attacks.

Ultimately, as the network becomes more heavily used, multi-gigabyte per day bandwidth is very realistic.

### How to handle key management? <a href="#how-to-handle-key-management" id="how-to-handle-key-management"></a>

Validators are expected to run an HSM that supports ed25519 keys. Here are potential options:

* YubiHSM 2
* Ledger Nano S
* Ledger BOLOS SGX enclave
* Thales nShield support

Kii Global nor the Interchain Foundation does not recommend one solution above the other. The community is encouraged to bolster the effort to improve HSMs and the security of key management.

### What can validators expect in terms of operations? <a href="#what-can-validators-expect-in-terms-of-operations" id="what-can-validators-expect-in-terms-of-operations"></a>

Running an effective operation is key to avoiding unexpected unbonding or slashing. Operations must be able to respond to attacks and outages, as well as maintain security and isolation in the data center.

### What are the maintenance requirements? <a href="#what-are-the-maintenance-requirements" id="what-are-the-maintenance-requirements"></a>

Validators are expected to perform regular software updates to accommodate chain upgrades and bug fixes. It is suggested to consider using [Cosmovisor (opens new window)](https://docs.cosmos.network/v0.45/run-node/cosmovisor.html) to partially automate this process.

During an chain upgrade, progress is discussed in a private channel in the Kii Discord. If your validator is in the active set we encourage you to request access to that channel by contacting a moderator.

### How can validators protect themselves from denial-of-service attacks? <a href="#how-can-validators-protect-themselves-from-denial-of-service-attacks" id="how-can-validators-protect-themselves-from-denial-of-service-attacks"></a>

Denial-of-service attacks occur when an attacker sends a flood of internet traffic to an IP address to prevent the server at the IP address from connecting to the internet.

An attacker scans the network, tries to learn the IP address of various validator nodes, and disconnects them from communication by flooding them with traffic.

One recommended way to mitigate these risks is for validators to carefully structure their network topology using a sentry node architecture.

Validator nodes are expected to connect only to full nodes they trust because they operate the full nodes themselves or the trust full nodes are run by other validators they know socially. A validator node is typically run in a data center. Most data centers provide direct links to the networks of major cloud providers. The validator can use those links to connect to sentry nodes in the cloud. This mitigation shifts the burden of denial-of-service from the validator's node directly to its sentry nodes, and can require that new sentry nodes are spun up or activated to mitigate attacks on existing ones.

Sentry nodes can be quickly spun up or change their IP addresses. Because the links to the sentry nodes are in private IP space, an internet-based attack cannot disturb them directly. This strategy ensures that validator block proposals and votes have a much higher chance to make it to the rest of the network.

For more sentry node details, see the [CometBFT Documentation (opens new window)](https://docs.cometbft.com/v0.34/core/validators) or the [Sentry Node Architecture Overview (opens new window)](https://forum.cosmos.network/t/sentry-node-architecture-overview/454) on the forum.
