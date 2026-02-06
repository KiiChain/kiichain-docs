# TokenFactory

## Token Factory

The tokenfactory module allows any account to create a new token with the name `factory/{creator address}/{subdenom}`.\
Because tokens are namespaced by creator address, this allows token minting to be permissionless, due to not needing to resolve name collisions.\
A single account can create multiple denoms, by providing a unique subdenom for each created denom. Once a denom is created, the original creator is given "admin" privileges over the asset.

This allows them to:

* Mint their denom to any account
* Burn their denom from any account
* Create a transfer of their denom between any two accounts
* Change the admin. In the future, more admin capabilities may be added. Admins can choose to share admin privileges with other accounts using the authz module. The `ChangeAdmin` functionality, allows changing the master admin account, or even setting it to `""`, meaning no account has admin privileges for the asset.

### Interaction with other modules

<table><thead><tr><th width="188.83331298828125">Module</th><th>Interaction</th></tr></thead><tbody><tr><td>Account</td><td>Finds module accounts when they are used by tokens</td></tr><tr><td>Bank</td><td>Mint, burn and intermediate tokens. Checks blocked addresses.</td></tr><tr><td>Community pool</td><td>Fees for denom creation go to the community pool</td></tr></tbody></table>

### Messages

#### CreateDenom

Creates a denom  `factory/{creator address}/{subdenom}` given the denom creator address and the subdenom. Subdenoms can contain `[a-zA-Z0-9./]`.

```go
message MsgCreateDenom {
  string sender = 1 [ (gogoproto.moretags) = "yaml:\"sender\"" ];
  string subdenom = 2 [ (gogoproto.moretags) = "yaml:\"subdenom\"" ];
}
```

**State Modifications:**

* Fund the community pool with the denom creation fee from the creator address, set in `Params`.
* Set `DenomMetaData` via the bank keeper.
* Set `AuthorityMetadata` for the given denom to store the admin for the created denom `factory/{creator address}/{subdenom}`. Admin is automatically set as the Msg sender.
* Add denom to the `CreatorPrefixStore`, where a state of denoms created per creator is kept.

#### Mint

Minting of a specific denom is only allowed for the current admin.\
Note, the current admin is defaulted to the creator of the denom.

```go
message MsgMint {
  string sender = 1 [ (gogoproto.moretags) = "yaml:\"sender\"" ];
  cosmos.base.v1beta1.Coin amount = 2 [
    (gogoproto.moretags) = "yaml:\"amount\"",
    (gogoproto.nullable) = false
  ];
}
```

**State Modifications:**

* Safety check the following
  * Check that the denom minting is created via `tokenfactory` module
  * Check that the sender of the message is the admin of the denom
* Mint a designated amount of tokens for the denom via `bank` module

#### Burn

Burning of a specific denom is only allowed for the current admin.\
Note, the current admin is defaulted to the creator of the denom.

```go
message MsgBurn {
  string sender = 1 [ (gogoproto.moretags) = "yaml:\"sender\"" ];
  cosmos.base.v1beta1.Coin amount = 2 [
    (gogoproto.moretags) = "yaml:\"amount\"",
    (gogoproto.nullable) = false
  ];
}
```

**State Modifications:**

* Safety check the following
  * Check that the denom minting is created via `tokenfactory` module
  * Check that the sender of the message is the admin of the denom
* Burn a designated amount of tokens for the denom via `bank` module

#### ChangeAdmin

Change the admin of a denom. Note, this is only allowed to be called by the current admin of the denom.

```go
message MsgChangeAdmin {
  string sender = 1 [ (gogoproto.moretags) = "yaml:\"sender\"" ];
  string denom = 2 [ (gogoproto.moretags) = "yaml:\"denom\"" ];
  string newAdmin = 3 [ (gogoproto.moretags) = "yaml:\"new_admin\"" ];
}
```

#### SetDenomMetadata

Setting of metadata for a specific denom is only allowed for the admin of the denom.\
It allows the overwriting of the denom metadata in the bank module.

```go
message MsgChangeAdmin {
  string sender = 1 [ (gogoproto.moretags) = "yaml:\"sender\"" ];
  cosmos.bank.v1beta1.Metadata metadata = 2 [ (gogoproto.moretags) = "yaml:\"metadata\"", (gogoproto.nullable)   = false ];
}
```

**State Modifications:**

* Check that the sender of the message is the admin of the denom
* Modify `AuthorityMetadata` state entry to change the admin of the denom
