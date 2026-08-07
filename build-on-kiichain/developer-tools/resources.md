---
description: Helpful resources to start building on Kiichain
hidden: true
---

# Resources

**CosmJS** - [https://github.com/cosmos/cosmjs](https://github.com/cosmos/cosmjs)

This is a Javascript library that could be utilized on the frontend for creating robust dApps in the cosmos ecosystem.  This library has been used to build many things such as wallets and applications that require sending transaction messages on a cosmos based blockchain.


Easy CosmJS starting point documentation - [https://gist.github.com/webmaster128/8444d42a7eceeda2544c8a59fbd7e1d9](https://gist.github.com/webmaster128/8444d42a7eceeda2544c8a59fbd7e1d9)



**Cosmpy** - [https://github.com/fetchai/cosmpy](https://github.com/fetchai/cosmpy)

A python library created by fetchai.  Similar to CosmJS, this library handles connectivity and transaction creation and broadcasting to cosmos based chains.



If adding a library in your dApp is not an option or you prefer not to use javascript/typescript or python, communicating via rpc endpoints is also possible. Kiichain validators expose rpc endpoints that dApp developers can utilize when building dApps. It is highly recommended  for dApp developers to bring up their own node in order to utilize these rpc endpoints (more information about setting up a node here: [Run a Validator / Full Node](../../validate-the-network/run-a-validator-full-node/getting-started.md))



Kiichain RPC endpoints:

* **Mainnet:** [https://rpc.kiivalidator.com](https://rpc.kiivalidator.com) (JSON-RPC: [https://json-rpc.kiivalidator.com](https://json-rpc.kiivalidator.com))
* **Testnet Oro:** [https://rpc.uno.sentry.testnet.v3.kiivalidator.com/](https://rpc.uno.sentry.testnet.v3.kiivalidator.com/)

See also:

* [Kiichain Mainnet](../kiichain-mainnet.md)
* [Testnet Oro](../testnet-oro.md)
* [Bridge](../../learn/getting-started/bridge.md)
