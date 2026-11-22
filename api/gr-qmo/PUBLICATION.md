# GR/QMO public edition

This public package preserves the full authoritative COMPLETE 1.0.0 mathematical payload: 2,397 objects, 75,457 graph edges, 12,260 occurrences, 14 checkpoints, and zero dangling endpoints. The SQLite registry, full dependency index, canonical mathematical definitions, integration objects, conditions, and source papers are unchanged. No graph was rebuilt or merged, and no mathematical closure was reinterpreted.

`PUBLICATION_EDITION.json` records the original-to-public file dispositions. The source is `COMPLETE.zip`, SHA-256 `2cfd927ac20aee20b33f3eed8326344e5ef5bcb4a74bc0fe501644d0089c9149`.

The public verifier includes the tested Windows comparison-boundary path normalization. Manifest keys use forward slashes and remove harmless leading `./` components; filenames, case, mathematics, and hash inputs are preserved. The separate API 4.3 archive and historical API directory are omitted; `registry/OMITTED_HISTORICAL_MATERIAL.json` records their identities. They are not runtime dependencies.

Research checkpoint archives and expanded records remain byte-identical and are explicitly required by `registry/CHECKPOINTS.json`. Inactive historical source evidence inside those checkpoints records the original research context; it does not supply active graph edges or aliases. The active loader uses only the current GR/QMO index and registry. Retired connections stay retired.

`api/GR_QMO_API_FULL_CURRENT/GR_QMO_CHECKSUMS.sha256` uses paths relative to its containing directory. Its listed file digests are unchanged. Only publication metadata, packaging documentation, and verifier compatibility code differ from COMPLETE. `MANIFEST.json` seals this public edition.

The full dependency index exceeds GitHub's ordinary file limit and is tracked through Git LFS. Obtain LFS content before running checks; a pointer file is not a usable mathematical index.

```text
git lfs pull
python mk43.py verify
python tests/test_installation.py
python tools/run_regressions.py --output reruns/regressions
```

Installation and regression checks establish software integrity and supplied fixture results, not independent scientific validation or peer review.
