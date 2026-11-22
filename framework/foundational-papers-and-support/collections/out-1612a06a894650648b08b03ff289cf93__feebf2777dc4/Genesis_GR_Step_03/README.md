# Genesis–GR Step 03

**Input:** `3 | Audit(2).zip` → `GENESIS_GR_DROPIN_v1.2.1`.

**New result:** An explicit exact nonlinear two-way tensor translation for the supplied module's faithfully realized smooth GR sector:

    F_G = A^T F_GR A,
    F_GR = A^{-T} F_G A^{-1},
    F_G=0 iff F_GR=0.

The connection transformation includes the derivative of the smooth invertible frame map A. Curvature, Ricci/scalar/Einstein tensors and covariant source conservation follow with the stated assumptions. This is a representation theorem, not a proof that every GR solution has a unique native Genesis history.

**New executed checks:** 20/20 passed. These are constructed classical tensor examples, including a nonlinear expanding metric, frame transformations, source conservation and exact counterexamples to insufficient readout assumptions. They do not test the unspecified native metric generator or native dynamics.

## Files

- `DERIVATION_STEP_03.md`: the complete argument, exact scope, explicit inverse, covariant source refinement, qualifications and native boundary.
- `AUDIT_FINDINGS.md`: source-aware findings; proposed clarifications do not modify uploaded canon.
- `checks.py`, `CHECK_RESULTS.json`: executable calculations and actual results.
- `evidence/SOURCE_EXCERPTS_STEP_03.md`: exact supplied passages, original paths and line numbers.
- `evidence/INPUT_INTEGRITY.json`, `PROVENANCE.json`: source hashes, validation and inspection scope.
- `source/3_Audit_2_original.zip`: byte-for-byte copy of the supplied audit archive; renamed only for convenient transport.
- `prior/`: the earlier two output ZIPs, unchanged.
- `SHA256SUMS.txt`: integrity list for this release.

No upstream physics has been replaced, no repository has been edited, and no source executable has been run. Read the determination at the top of the derivation before treating any completion label as a claim of total native equivalence.
