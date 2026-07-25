---
description: T-REX Protocol on KiiChain
---

# RWA Protocol

**Note: This project is still under development so future changes will be made.**

### Overview

This document outlines the detailed implementation plan for the T-REX (Token for Regulated EXchanges) protocol using CosmWasm smart contracts on KiiChain. The T-REX protocol is designed for compliant issuance and management of tokens on blockchain networks.

### Important Links

* [GitHub Repo](https://github.com/KiiChain/Kii-RWA-Protocol)
* [Rust SDK](https://docs.kiiglobal.io/docs/build-on-kiichain/developer-tools/rust-sdk)

### Contracts and Their Methods

#### 1. CW20 T-REX Token

Extends the CW20 standard with T-REX functionalities and implements permissioned transfers.

**Storage**

* `token_info`: TokenInfo
* `balances`: Map\<Addr, Uint128>
* `allowances`: Map<(Addr, Addr), AllowanceInfo>
* `identity_registry`: Addr
* `compliance`: Addr

**Execute**

* `transfer(recipient: Addr, amount: Uint128) -> Result<Response>`
  * Description: Transfers tokens to a recipient if they are verified and compliant.
  * Interaction: Calls `is_verified` on Identity Registry and `can_transfer` on Modular Compliance.
* `transfer_from(owner: Addr, recipient: Addr, amount: Uint128) -> Result<Response>`
  * Description: Transfers tokens on behalf of the owner if the recipient is verified and compliant.
  * Interaction: Similar to `transfer`, but checks allowances first.

**Query**

* `balance(address: Addr) -> BalanceResponse`
* `token_info() -> TokenInfoResponse`
* `is_verified_transfer(from: Addr, to: Addr, amount: Uint128) -> IsVerifiedTransferResponse`
  * Description: Checks if a transfer would be valid without executing it.
  * Interaction: Calls Identity Registry and Modular Compliance.

#### 2. Identity Registry

Manages investor identities and eligibility.

**Storage**

* `identity_storage`: Addr
* `trusted_issuers_registry`: Addr
* `claim_topics_registry`: Addr
* `agents`: Vec

**Execute**

* `register_identity(address: Addr, identity: Addr) -> Result<Response>`
  * Description: Registers a new identity for an address.
  * Interaction: Calls Identity Registry Storage to store the mapping.
* `update_identity(address: Addr, identity: Addr) -> Result<Response>`
  * Description: Updates an existing identity for an address.
* `remove_identity(address: Addr) -> Result<Response>`
  * Description: Removes an identity for an address.

**Query**

* `is_verified(address: Addr) -> IsVerifiedResponse`
  * Description: Checks if an address is verified (has required claims).
  * Interaction: Queries Identity Registry Storage, Trusted Issuers Registry, and Claim Topics Registry.

#### 3. Identity Registry Storage

Stores the mapping of wallet addresses to identity contracts.

**Storage**

* `identities`: Map\<Addr, Addr>

**Execute**

* `add_identity(address: Addr, identity: Addr) -> Result<Response>`
* `remove_identity(address: Addr) -> Result<Response>`

**Query**

* `get_identity(address: Addr) -> GetIdentityResponse`

#### 4. Trusted Issuers Registry

Manages the list of trusted claim issuers.

**Storage**

* `trusted_issuers`: Map\<Addr, TrustedIssuer>

**Execute**

* `add_trusted_issuer(issuer: Addr, claim_topics: Vec<u32>) -> Result<Response>`
* `remove_trusted_issuer(issuer: Addr) -> Result<Response>`

**Query**

* `is_trusted_issuer(issuer: Addr) -> IsTrustedIssuerResponse`
* `get_trusted_issuers() -> GetTrustedIssuersResponse`

#### 5. Claim Topics Registry

Stores the required claim topics for token eligibility.

**Storage**

* `required_claim_topics`: Vec

**Execute**

* `add_claim_topic(topic: u32) -> Result<Response>`
* `remove_claim_topic(topic: u32) -> Result<Response>`

**Query**

* `get_required_claim_topics() -> GetRequiredClaimTopicsResponse`

#### 6. Modular Compliance

Implements transfer restriction rules.

**Storage**

* `modules`: Vec
* `bound_tokens`: Vec

**Execute**

* `add_module(module: Addr) -> Result<Response>`
* `remove_module(module: Addr) -> Result<Response>`
* `bind_token(token: Addr) -> Result<Response>`

**Query**

* `can_transfer(from: Addr, to: Addr, amount: Uint128) -> CanTransferResponse`
  * Description: Checks if a transfer complies with all modules.
  * Interaction: Calls `check_transfer` on each compliance module.

#### 7. ONCHAINID

Represents user identities (similar to ERC-734/735).

**Storage**

* `keys`: Map\<bytes32, Key>
* `claims`: Map\<bytes32, Claim>

**Execute**

* `add_key(key: bytes32, purpose: u32, key_type: u32) -> Result<Response>`
* `remove_key(key: bytes32) -> Result<Response>`
* `add_claim(topic: u32, scheme: u32, issuer: Addr, signature: Vec<u8>, data: Vec<u8>, uri: String) -> Result<Response>`
* `remove_claim(topic: u32) -> Result<Response>`

**Query**

* `get_key(key: bytes32) -> GetKeyResponse`
* `get_claim(topic: u32) -> GetClaimResponse`

#### 8. T-REX Factory

Deploys and configures T-REX token suites.

**Storage**

* `implementation_authority`: Addr
* `deployed_tokens`: Vec

**Execute**

* `deploy_token_suite(token_info: TokenInfo, compliance_info: ComplianceInfo, identity_info: IdentityInfo) -> Result<Response>`
  * Description: Deploys a new T-REX token suite.
  * Interaction: Instantiates all necessary contracts and configures them.

**Query**

* `get_deployed_tokens() -> GetDeployedTokensResponse`

#### 9. Implementation Authority

Manages contract upgrades and versioning.

**Storage**

* `versions`: Map\<String, ContractVersion>
* `current_version`: String

**Execute**

* `add_version(name: String, contracts: Vec<(String, Addr)>) -> Result<Response>`
* `set_current_version(name: String) -> Result<Response>`

**Query**

* `get_current_version() -> GetCurrentVersionResponse`
* `get_version(name: String) -> GetVersionResponse`

### Implementation Roadmap

1. Implement CW20 T-REX Token
2. Implement Identity Registry and Identity Registry Storage
3. Implement Trusted Issuers Registry and Claim Topics Registry
4. Implement Modular Compliance
5. Implement ONCHAINID
6. Implement T-REX Factory
7. Implement Implementation Authority
8. Integrate all contracts and perform thorough testing
9. Conduct security audit
10. Deploy to Kii-Chain testnet
11. Final testing and adjustments
12. Deploy to Kii-Chain mainnet

### Testing Strategy

* Implement unit tests for each contract function
* Develop integration tests for contract interactions
* Create end-to-end scenarios to test the entire T-REX suite
* Perform fuzz testing to uncover edge cases
* Conduct governance testing to ensure proper access control
