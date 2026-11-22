# Genesis–GR Regular Completion v0.1 (GRC-1)

This is a **new proposed model**, not a recovery or validation of the unchanged historical microscopic Genesis theory.

## Result

A constrained eight-channel positive adjacency field encodes every smooth Lorentzian metric using ten independent real fields. The inverse and all chart transitions are explicit. The complete action is defined as a regular point-field rewriting of Einstein–Hilbert gravity with the same specified matter and boundary data. A phase/seven-chromatic-field squared completion supplies one explicit consistent matter model.

The written proof establishes exact classical solution-space equivalence for this defined branch. It is a reformulation, not a new mechanism explaining why microscopic Genesis produces gravity. No novelty, quantum or empirical claim is made.

## Read

- `THEOREM.md`: complete model, inverse, action, regularity and equivalence proofs, limits.
- `MODEL_CHANGES.md`: every substantive departure from the inherited model.
- `code/regular_completion.py`: encoder, decoder, chart transition, matter maps, source.
- `code/checks.py`: run the examples and negative controls.
- `results/CHECK_RESULTS.json`: 43 named checks and their actual scopes.
- `results/EXACT_SOLUTION.json`: a curved, matter-supported solution and native lift.
- `evidence/`: copied source evidence and prior determination, unchanged.
- `prior/`: preceding closure-assessment archive, unchanged.
- `PROVENANCE.json` and `MANIFEST.json`: sources, software and file hashes.

## Run

From this directory, with Python, SymPy and NumPy installed:

    python code/checks.py
    python verify.py

The reference implementation is local and symbolic/numerical; it is not a complete PDE solver or a machine-verified general proof. Hyperbolic and square-root functions are applied ENTRYWISE, never as matrix functions. Numeric error or insufficient symbolic assumptions must not be treated as a physical impossibility result.

No remote repository has been modified. This package is an incremental new-branch checkpoint, not a replacement for the earlier exhaustive recovery ZIP.
