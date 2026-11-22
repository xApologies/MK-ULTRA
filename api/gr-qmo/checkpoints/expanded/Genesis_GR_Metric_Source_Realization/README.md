# Genesis GR: Metric and Source Realization

This is a new, scoped supplement. Earlier checkpoints and original files remain unchanged.

**Established here:** explicit calibrated-metric extension using smooth transport, local source decoding using directional momentum-flux densities, and a two-sided inverse for the stated smooth geometric records.

**Not established:** a full physical inverse of the existing native Genesis theory or its total equivalence with GR. The actual native record-extraction law has not been evaluated or inverted.

Read `DERIVATION.md` first. `SOURCE_EVIDENCE.md` preserves exact source passages. `realization.py` implements the matrix reconstruction operations. `checks.py` exercises symbolic identities and one constructed curved geometry, not a native gravity solver. `CHECK_RESULTS.json` records the 18 executed checks with their individual scope. `PROVENANCE.json` records input hashes and the bounded inspection scope.

To repeat the checks in a Python environment with SymPy installed:

```text
python checks.py
```

Tested with Python 3.13.5 and SymPy 1.14.0. This package does not contain an implementation of Q_R, native lift selection, or native matter dynamics. It rejects insufficient matrix data rather than supplying a physical law implicitly.
