# Push–Pull Algorithms

Pull: normalize handle; resolve alias; resolve active version; recover all typed blocks in stable order; recover identity, relations, membership, provenance; return complete package or unresolved receipt.

Pull QMO: accept ordered address plan; validate; pull each node; preserve relation/depth/placement; emit unresolved nodes; compute coverage/order hash; return QMO-shaped result.

Add One: validate; stage; check conflicts; insert object/version/blocks/aliases/relations/provenance; set active; rebuild indexes; commit; receipt.

Add Many/Package: validate every package and relation; stage all rows; reject entire batch on required failure; commit atomically; rebuild once; emit package receipt.
