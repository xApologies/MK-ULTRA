# Atlas application to Genesis–GR

This is a supplementary research checkpoint, not a declaration of total native Genesis–GR equivalence.

Read `DERIVATION.md` for the source-based application and full proofs. `SOURCE_MAP.md` identifies the supplied passages. `evidence/` contains the original Atlas PDF, its extracted text, the exact checked optional API passage, and the supplied v1.2.1 endpoint module. `PROVENANCE.json` records hashes and scope.

Run the independent finite checks:

    python finite_atlas.py --self-test

To check an explicitly supplied finite native/target model pair:

    python finite_atlas.py --input finite_bridge.json

The input object has `native`, `target`, `mapping`, and optionally `physical_classes`. Each model has `states` (unique string IDs), `observations` (one string label per state), and `transitions` (operation name to a partial source-state/target-state dictionary). An absent source state means the operation is undefined. Both models must declare the same operation alphabet, even for an operation with an empty domain.

The checker tests the tables given to it. Matching operation names does not independently certify matching physical meanings. A supplied physical-class table is an assumption to check for mathematical consistency, not a proof of gauge redundancy. Continuum or nondeterministic physics is not replaced with a finite deterministic table by default.

`CHECK_RESULTS.json` records the executed tests. `NATIVE_STATUS.json` explicitly records that the actual native-gravity equivalence has not been evaluated by this finite tool. The new checkpoint does not recursively include the earlier ZIP checkpoints, and no original source was changed.
