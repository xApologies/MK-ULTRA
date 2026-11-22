# GR/QMO API — complete mathematical object

**Release:** 1.0.0  
**Active API:** General Relativity / Genesis equivalence QMO  
**Object population:** 2,397 linked mathematical objects  
**Active graph:** 75,457 typed connections

This is the complete Queryable Mathematical Object supplied in the GR package,
repaired in place. It is not a summary registry. The canonical mathematics,
full dependency index, SQLite query object, source occurrences, integration
objects, checkpoints, source papers, executable translators, and regression
suites remain together.

## Active entry points

- `api/GR_QMO_API_FULL_CURRENT/GR_QMO_API_CURRENT_CANONICAL.md`
- `api/GR_QMO_API_FULL_CURRENT/GR_QMO_DEPENDENCY_INDEX.json`
- `registry/GR_QMO.sqlite`
- `registry/QMO_MANIFEST.json`
- `registry/ENTRYPOINTS.json`
- `mk43.py`

The old API 4.3 graph is not an active dependency source. The public edition
omits its separate distribution and historical API directory; original hashes
are recorded in `registry/OMITTED_HISTORICAL_MATERIAL.json`. Sealed research
checkpoints retain inactive source evidence as documented in `PUBLICATION.md`.

## Graph repair applied

The source equation is `h = Pi_T(q*)`. The active graph therefore carries:

```text
@time_shell_projection REALIZES @metric_perturbation
@metric_perturbation REALIZED_BY @time_shell_projection
```

The former reversed pair is absent. Three RP-47 typed compositions whose
witnesses depended on that reversed direction are retired:

```text
@graviton PROJECTS_TO @time_shell_projection
@linear_metric_perturbation REALIZES @time_shell_projection
@spin_2_projection PROJECTS_TO @time_shell_projection
```

All 28 GR integration dependencies remain active and expose their mathematical
conditions in both `registry/INTEGRATION_DEPENDENCIES.json` and SQLite metadata.

## Query and verify

```text
python mk43.py status
python mk43.py object @graviton --limit 50
python mk43.py object @time_shell_projection --limit 50
python mk43.py find metric
python mk43.py verify
python tests/test_installation.py
```

Rebuild the full SQLite QMO without overwriting the sealed database:

```text
python tools/rebuild_registry.py --output reruns/GR_QMO.sqlite
```

## Preservation boundary

Of the supplied 75,432 parent edge records, 75,419 are unchanged, two direction
records are corrected, and three stale derived records are retired. The 28 GR
integration edges produce 75,457 active database edges. All 2,384 inherited
handles plus 13 integration/imported objects remain present.

No Git staging, commit, push, or remote publication is performed by this package.
