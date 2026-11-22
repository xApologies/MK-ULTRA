# Boundary Contract

AI⁵ receives capabilities, not unrestricted module internals. It must not inspect BRANE private state, filesystem paths outside its module root, Library internals, API storage internals, or QMO manager internals.

The only persistent state permitted is immutable policy configuration, model assets explicitly declared in the manifest, and audit-safe aggregate metrics. Request reasoning state must be isolated and disposable.
