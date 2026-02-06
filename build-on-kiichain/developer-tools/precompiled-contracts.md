---
description: >-
  KiiChain boasts a sophisticated framework of precompiled smart contracts
  meticulously crafted to harmonize with the Cosmos SDK functionalities,
  bolstering the network's efficiency and adaptability.
hidden: true
---

# Precompiled Contracts

### **KiiChain Precompiled Contracts**

Among these contracts, the "Bank," "Staking," and "Rewards" contracts are integral components seamlessly integrated into Kiichain's operations through the Polaris EVM module, meticulously engineered by Berachain. These contracts play pivotal roles in managing sKII balances, orchestrating staking activities, and computing rewards, thereby fortifying the network's core functions while maintaining compatibility with the Ethereum Virtual Machine standards.

| Contract Name | Contract Address                                          | Description                                                                                                                                                                                                                                                                           |
| ------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bank          | 0x4381dC2aB14285160c808659aEe005D51255adD7                | The Bank contract governs the determination of sKII balances associated with individual addresses, serving as the cornerstone for transactional integrity and account management within Kiichain.                                                                                     |
| Staking       | 0xd9A998CaC66092748FfEc7cFBD155Aae1737C2fF                | The Staking contract intricately manages the staking functionality within Kiichain, including the delegation of sKII tokens to validators and the maintenance of staking balances, ensuring the robustness and security of the network's consensus mechanism.                         |
| Rewards       | 0x55684E2CA2BACE0ADC512C1AFF880B15B8EA7214                | The Rewards contract plays a crucial role in computing and distributing accumulated rewards stemming from the staking activity within Kiichain, fostering incentivization and participation among network participants through fair and transparent reward allocation mechanisms.     |
| Swap          | 0xF948f57612E05320A6636a965cA4fbaed3147A0f (Only Testnet) | The custom-deployed Swap contract facilitates the seamless exchange of sKII tokens to KII and vice versa, enabling fluid token interoperability and liquidity provision within the Kiichain ecosystem, thereby enhancing user accessibility and utility across token functionalities. |

Complementing these foundational contracts, the custom-deployed Swap contract serves as a pivotal component in enabling seamless token conversion between sKII and KII, further enriching Kiichain's utility and accessibility. Together, these contracts, spearheaded by the Polaris EVM module developed by Berachain, form the bedrock of Kiichain's operational infrastructure, fostering a cohesive ecosystem conducive to streamlined interactions and value exchange among participants.

To interact with these precompiled contracts, you can view them over at Berachain's Precompiled Contracts Docs.

[https://github.com/berachain/polaris/tree/main/cosmos/precompile](https://github.com/berachain/polaris/tree/main/cosmos/precompile)

For the Swap contract, below shows the two function signatures that you would require to interact with if exchanging tokens. _**NOTE: You will need KII to pay for gas fees when interacting with any of the smart contracts.**_

```
// exchange your KII for sKII
function buySkii() external payable

// exchange your sKII for KII
function sellSkii(uint256 amount) external
```

_**ABI for the Swap Contract**_

```
[
    {
      "inputs": [],
      "name": "bankContractAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "buySkii",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "sellSkii",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ] 
```

<br>
