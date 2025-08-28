# Deploy Smart Contract on KiiChain using Remix

## 1. Add KiiChain Testnet to MetaMask
- Network Name: `KiiChain Testnet`
- RPC URL: `https://json-rpc.uno.sentry.testnet.v3.kiivalidator.com/`
- Chain ID: `1336`
- Currency Symbol: `KII`

## 2. Open Remix IDE
- Go to [https://remix.ethereum.org](https://remix.ethereum.org)
- Create a new file `HelloKii.sol` in the `contracts/` folder.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HelloKii {
    string public message;

    constructor(string memory _msg) {
        message = _msg;
    }

    function setMessage(string memory _msg) public {
        message = _msg;
    }
}
