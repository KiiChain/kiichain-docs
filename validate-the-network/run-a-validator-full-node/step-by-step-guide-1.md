---
description: Launch a node or validator on KiiChain Testnet Oro
hidden: true
---

# Step by step guide

## Run Single Local Node (Docker)

```
git clone git@github.com:KiiChain/kiichain.git
cd kiichain
```

```
nano docker/rpcnode/scripts/step1_configure.init.sh

# replace REPLACE_SYNC_RPC with 18.226.34.140:26669

# replace REPLACE_SYNC_PEERS with d2fbe128da8cf541a44ae3f893e4f14395fdfd3a@18.226.34.140:26668,2a6353f698929346e4a7b4ea8987a5c7748c73af@3.142.36.147:26668
```

```
make run-prime-node # this is to run a local node

# once the container is running, verify that you can reach the rpc
# by visiting http://localhost:26669 on your browser.  You should see a list of rpc endpoints

# execute commands once the container is running:
docker ps

# retrieve the container id
docker exec -it <container id> sh

# you will then shell into the container

kiichaind # you should now see a list of all the sub commands that can be used with kiichaind
```

## Run Testnet Validator Node

### Step 1: Run Single Testnet Node (Docker)

```sh
git clone git@github.com:KiiChain/kiichain.git
cd kiichain
make run-rpc-node # this is to run a rpc node

# once the container is running, verify that you can reach the rpc
# by visiting http://localhost:26669 on your browser.  You should see a list of rpc endpoints

# execute commands once the container is running:
docker ps

# retrieve the container id
docker exec -it <container id> sh

# you will then shell into the container

kiichaind # you should now see a list of all the sub commands that can be used with kiichaind
```

### Step 2: Create a Key

```sh
# ensure you are in the docker container from the previous step and have access to kiichaind

kiichaind keys add <KEY NAME>

# get your kiichain address for the faucet step
kiichaind keys show <KEY NAME> -a
```

### Step 3: Get Testnet Tokens

Go to the Kiichain discord channel and request for kiichain testnet tokens from the faucet.

### Step 4: Create a Validator Transaction

```sh
# ensure you are in the docker container from the previous step and have access to kiichaind

kiichaind tx staking create-validator \
--from <KEY NAME> \
--chain-id  \
--moniker="<VALIDATOR NAME>" \
--commission-max-change-rate=0.01 \
--commission-max-rate=1.0 \
--commission-rate=0.05 \
--details="<description>" \
--security-contact="<contact information>" \
--website="<your website>" \
--pubkey $(kiichaind tendermint show-validator) \
--min-self-delegation="1" \
--amount <token delegation>ukii \
--node localhost:26669
```

## Testnet Genesis

**How to validate on the Kiichain Testnet**

_This is the Kiichain kiichain Testnet_

> Genesis [Published](https://raw.githubusercontent.com/KiiChain/testnets/refs/heads/main/testnet_oro/genesis.json)

### Hardware Requirements

**Minimum**

* 64 GB RAM
* 1 TB NVME SSD
* 16 Cores (modern CPU's)

### Operating System

> Linux (x86\_64) or Linux (amd64) Recommended Arch Linux

**Dependencies**

> Prerequisite: go1.18+ required.

* Arch Linux: `pacman -S go`
* Ubuntu: `sudo snap install go --classic`

> Prerequisite: git.

* Arch Linux: `pacman -S git`
* Ubuntu: `sudo apt-get install git`

> Optional requirement: GNU make.

* Arch Linux: `pacman -S make`
* Ubuntu: `sudo apt-get install make`

### Upgrading node

When a new upgrade has launched and your node is requesting upgrade it to continue with the validation process, follow these steps:

#### 1. Pull all changes

```
$ git pull origin main
```

#### 2. Run upgrade command

We have created a command which interacts with the cosmovisor tool, installed in the docker file that helps to upgrade the blockchain. The most important part is to run the command with the parameters **UPGRADE\_NAME** and **CONTAINER\_NAME** where:

* **UPGRADE\_NAME**: This is the title name of the upgrade proposal. It must be the name of the proposal plan if this is different, cosmoviso won't upgrade the node.

```
$ make upgrade UPGRADE_NAME=<upgradeName> CONTAINER_NAME=<yourContainerName>
```

For instance upgrading the blockchain to the v2.0.0, running in a container called **kiichain-rpc-node**:

```
$ make upgrade UPGRADE_NAME=v2.0.0 CONTAINER_NAME=kiichain-rpc-node
```

