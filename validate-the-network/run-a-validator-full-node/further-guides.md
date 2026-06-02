---
description: Other guides into configuring Kiichain nodes
---

# Further guides

### Enabling debug EVM JSON-RCP namespace

To enable `debug_` calls on your JSON-RCP node, you need to update your `app.toml`:

1. Go to `app.toml`&#x20;

```bash
cd $NODE_HOME/config/app.toml
```

Where `$NODE_HOME` is where your node configuration lives.

2. Add the new configuration

On your `app.toml` look for the `json-rpc` section. There, you need to find the `api` key. The section looks like this:

```
###############################################################################
###                           JSON RPC Configuration                        ###
###############################################################################

[json-rpc]

# API defines a list of JSON-RPC namespaces that should be enabled
# Example: "eth,txpool,personal,net,debug,web3"
api = "eth,net,web3"
```

There, you need to add the namespace you want to add. In this case `debug` :

Replace:

```
api = "eth,net,web3"
```

With:

```
api = "eth,net,web3,debug"
```

You can also enable any other namespace that you may want, such as `personal` and `txpool`.

3. Restart the node

Once the node goes live again, the configuration should be applied.
