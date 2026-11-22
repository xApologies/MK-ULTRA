# Genesis → GRC-1 faithful-embedding audit

Start with REPORT.md. It contains the complete comparison and proofs.

## Result

The original microscopic theory has **not** been certified as a faithful subtheory of GRC-1. The audit finds two specific scoped failures: a recovered metric-interface collision surviving canonical re-encoding, and a nonzero kinetic field-space curvature in a stated source-action specialization that rules out an ordinary eight-field same-metric coordinate embedding into the explicit free-scalar GRC-1 model.

GRC-1's own regular reformulation remains intact. Its 43 tests passed again. The 32 new audit tests pass by verifying the comparison identities and correctly detecting the discrepancies; they do not certify an embedding.

## Files

- REPORT.md: full derivation, source distinction, hypotheses, obstructions, and compatible matched-matter route.
- code/checks.py: executable exact checks.
- code/field_space_geometry.py: direct full-dimensional metric-jet curvature calculation.
- code/grc1_reference.py and code/gr_geometry_reference.py: unchanged copied routines from the prior checkpoint.
- evidence/: exact original API passages, canonical source text, prior theorem and changes.
- results/: rerun and new results, execution logs.
- prior/: unchanged GRC-1 ZIP.
- SOURCE_MANIFEST.json: source lineage and hashes.
- MANIFEST.json and verify.py: integrity verification.

Run `python code/checks.py`; then `python verify.py` to check the delivered manifest before changing any generated test output. An additional rerun changes elapsed-time fields and therefore intentionally changes output hashes.

No source file was overwritten. The report distinguishes a counterexample to an interface, an action-sector exclusion theorem, failure of a particular solution identification, and an unestablished entire microscopic embedding.
