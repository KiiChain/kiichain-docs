---
description: >-
  Overview for deploying a smart contract with Hardhat, Remix, Foundry, and
  Thirdweb.
---

# Deploy a smart contract

### Chain Information

| RPC URL:  | [https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/](https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/) |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| Chain Id: | 1336                                                                                                                 |

### Deploy with Hardhat

#### 1. Install Hardhat

Install the hardhat framework in your project, by typing the following command:

```yaml
$ npm install --save-dev hardhat
```

#### 2. Create a hardhat project

After installing Hardhat, create a project. You can create it using typescript or javascript in the following screen:

```yaml
$ npx hardhat init
```

```tsx
888    888                      888 888               888
888    888                      888 888               888
888    888                      888 888               888
8888888888  8888b.  888d888 .d88888 88888b.   8888b.  888888
888    888     "88b 888P"  d88" 888 888 "88b     "88b 888
888    888 .d888888 888    888  888 888  888 .d888888 888
888    888 888  888 888    Y88b 888 888  888 888  888 Y88b.
888    888 "Y888888 888     "Y88888 888  888 "Y888888  "Y888

Welcome to Hardhat v2.22.8 

? What do you want to do? …
❯ Create a JavaScript project
  Create a TypeScript project
  Create a TypeScript project (with Viem)
  Create an empty hardhat.config.js
  Quit
```

#### 3. Create a Smart contract and Compile project

After creating the smart contract in the “Contracts” folder, run the following command to check your code.

```yaml
$ npx hardhat compile 
```

#### 4. Set the hardhat configuration file and deploy the smart contract

After creating the ignition deploy file, let's set the blockchain information into the hardhat.config file, with the following information:

```tsx
import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

const config: HardhatUserConfig = {
  solidity: "0.8.20", // Solidity Version
  networks: {
    kiichain: {
      url: "https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/",
      chainId: 1336,
      accounts: [`0x${yourPrivateKey}`],
    },
  },
};

export default config;

```

```yaml
$ npx hardhat ignition deploy ignition/modules/<contractName>.ts --network kiichain
```

### Deploy with Remix

Remix is a web compiler page where you can write smart contracts, scripts and deploy using your wallet from Metamask. You can enter Remix [here](https://remix.ethereum.org/#lang=en\&optimize=false\&runs=200\&evmVersion=null).

<figure><img src="../../.gitbook/assets/image (15) (1).png" alt="" width="563"><figcaption></figcaption></figure>

In the Workspace create the file which contains the Smart contract with the .sol extension.

<figure><img src="../../.gitbook/assets/image (16) (1).png" alt="" width="272"><figcaption></figcaption></figure>

After writing the smart contract, go to the Solidity Compiler section and select your compiler version, is recommended to use the most recent one.

Then press “Compile” button under the Compiler selector.

<figure><img src="../../.gitbook/assets/image (17) (1).png" alt="" width="320"><figcaption></figcaption></figure>

#### 3. Select your Metamask wallet as Deploy environment

In the “Deploy and Run Transactions” section, move to the Environment and select your Metamask Provider, remember you must be connected to KiiChain Testnet

<figure><img src="../../.gitbook/assets/image (18) (1).png" alt="" width="320"><figcaption></figcaption></figure>

#### 4. Deploy Smart contract

Select the smart contract to be deployed and write the Constructor parameters if Remix detects them

<figure><img src="../../.gitbook/assets/image (19) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Finally, you can interact with the different functions in the same section above the Deploy button.

### Deploy with Foundry

#### 1. Create a project and installation

Run the following commands in your terminal in order to start the foundry’s installation.

```bash
curl -L https://foundry.paradigm.xyz | bash
```

then run the following command in another terminal or restart the current one for finishing the installation process.

```json
foundryup
```

After finishing the foundry’s installation let’s create a new project, run the following commands for starting the new project and then move to it’s folder:

```bash
forge init projectName
cd projectName
```

#### 2. Write and build a contract

Write your smart contract in ‘/src/smartContractName.sol’ and the script in ‘/script/smartContractName.s.sol’, here is an example of that:

This contract will be placed in the path: /src/Counter.sol

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Counter {
    uint256 public number;

    function setNumber(uint256 newNumber) public {
        number = newNumber;
    }

    function increment() public {
        number++;
    }
    
    
    function getCounter() public view returns (uint256) {
        return number;
    }
}

```

This is the script and will be placed in /script/Counter.s.sol remember to add the .s before the .sol extension.

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console} from "forge-std/Script.sol";
import {Counter} from "../src/Counter.sol";

contract CounterScript is Script {
    Counter public counter;

    function setUp() public {}

    function run() public {
        vm.startBroadcast();

        counter = new Counter();

        vm.stopBroadcast();
    }
}

```

then run the following command for build and check that everything is correct.

```bash
forge build
```

#### 3. Deploy

First, you need to run a simulation.

```bash
forge script script/Counter.s.sol:CounterScript --fork-url https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/ --private-key yourPrivateKey
```

The simulation will be complete after that, and you can run with broadcast.

```bash
forge script script/Counter.s.sol:CounterScript --fork-url https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/ --private-key yourPrivateKey --broadcast
```

A success message should appear.

### Troubleshooting — Remix on Oro (Testnet, Chain ID 1336)

If a Remix deploy shows **“Transaction mined but execution failed (status 0x0)”**, set:

* **Solidity Compiler → EVM Version = `london`**
* **Optimizer: enabled (200 runs)**
* **Disable `viaIR`** (if it was enabled)

Re-compile, then deploy again on **KiiChain Testnet (Oro, chainId 1336)**. This avoids newer EVM opcodes not yet supported by Oro.

#### Hardhat — KiiChain Oro Network

```ts
// hardhat.config.ts
import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

const config: HardhatUserConfig = {
  solidity: { version: "0.8.20", settings: { optimizer: { enabled: true, runs: 200 } } },
  networks: {
    kiichain: {
      url: "https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/",
      chainId: 1336,
      // accounts: [process.env.PRIVATE_KEY!], // use .env, never hardcode keys
    },
  },
};
export default config;

```
