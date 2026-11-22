# GENESIS — 16 PROOF / DERIVATION THEORY

Genesis proof records are dependency structures with stronger semantics than reachability.

## Derivation record

A derivation node stores premises, rule, conclusion, type context, scope, provenance, status, and proof obligations. A proof DAG may share premises without multiplying evidence.

## Closure predicate

A candidate theorem is closed only when every premise is admitted, every inference rule is named and valid in scope, typing is consistent, all required witnesses exist, and provenance/status are attached.

## Reachability firewall

A path in a dependency graph is not a proof unless every edge is an admissible inference. Likewise a proof dependency does not become physical causation.

## Failed proof attempts

Failed derivations are retained as first-class -nai records with rollback point and counterexample/no-go witness where available.

## Future work

A complete internal Genesis logic is not yet derived. Current proofs use ordinary mathematical metalanguage plus Genesis admissibility/provenance discipline. Whether logic itself can be reconstructed from the Prime relation architecture remains open.
