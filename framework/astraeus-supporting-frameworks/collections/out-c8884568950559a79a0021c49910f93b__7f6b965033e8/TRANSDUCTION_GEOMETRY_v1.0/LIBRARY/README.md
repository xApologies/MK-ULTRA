# MK43 Transduction Library v0.1.0

This is the maintained metadata Library for the Transduction QMO/API.

The architectural model is inherited from the supplied Library 1.0 pseudocode/specification and Library 3.0 executable implementation, but the physics/domain payload has been zeroed.

## Addressing rule

```text
QMO/API mathematical object = Library address
metadata encoded beneath the address = recoverable Library package
```

Root:

```text
@global_transduction_object
```

Model:

```text
@transduction_qmo
```

## Populated state

```text
addresses: 36
typed relations: 34
equation/operator records represented through root metadata: 9
live ledger entries represented through root metadata: 285
```

## Recovery examples

```text
python -m transduction_library.cli --db state/library.sqlite3 recover @global_transduction_object

python -m transduction_library.cli --db state/library.sqlite3 recover @transduction_connection

python -m transduction_library.cli --db state/library.sqlite3 model @transduction_qmo

python -m transduction_library.cli --db state/library.sqlite3 search holonomy
```

The root address carries the complete QMO registries, runtime, validation, release manifest, and query contract. Individual addresses carry their own definition/status/typed-edge metadata.

## Restore

A fresh thread/runtime only needs the combined workspace ZIP. The QMO API gives machine traversal; this Library gives metadata recovery beneath those mathematical addresses.

## v0.2.0 update

Added scope-aware fabric classification metadata:

```text
@fabric_signature
@classifier_scope
@fabric_equivalence_test
```

Holonomy remains indexed as a strong invariant but is no longer treated as a complete global classifier.

## v0.3.0 — High-Recall Research Metadata

The Library now stores first-class research metadata:

```text
THEORY
MODEL
ANALOGY
HEURISTIC
HYPOTHESIS
COUNTEREXAMPLE
FAILED_PATH
LANGUAGE_RULE
AUDIT_RULE
QUESTION
POLICY
```

The storage policy is intentionally high-recall. Metadata may be filtered downstream; it should not be discarded upstream merely because it is exploratory.
