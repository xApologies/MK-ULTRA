# Dark Matter API Circularity Audit

## Detection method

The strict dependency subgraph is normalized using:

- the five RP-46 dependency relations from API 4.3;
- an explicit orientation table for custom Dark Matter relations;
- OPEN_TARGET edges excluded from solved composition.

Strongly connected components are then computed on the normalized primitive dependency graph.

## Inherited parent SCCs

The crawl finds inherited coupled components in the Time-Space parent subgraph.

These are **not modified** by the Dark Matter child self-crawl.

## Child SCC found

```text
@continuity_redistribution -> @dm_continuity_laplacian -> @dm_runtime_transition_capacity
```

More usefully, the dependency loop is:

```text
@dm_runtime_transition_capacity
-> @continuity_redistribution
-> @dm_continuity_laplacian
-> @dm_runtime_transition_capacity
```

## Audit disposition

```text
UNGROUNDED / MIS-TYPED CHILD CYCLE
```

Reason:

`L_N` does not use `T_run` as its edge coefficient.

It uses:

```text
w_e = kappa_ij A_ij.
```

`T_run` instead bounds the realized flow and determines when the local unsaturated operator must be re-evaluated.

## Patch candidate

Introduce:

```text
@dm_local_continuity_response_coefficient

w_e = kappa_ij A_ij.
```

Then:

```text
@dm_continuity_laplacian
USES
@dm_local_continuity_response_coefficient.
```

Retain:

```text
@dm_runtime_transition_capacity
SATURATION_GUARDS
@dm_continuity_laplacian
```

as a non-composable validity constraint.

## Result

After candidate patch:

```text
child nontrivial SCC count = 0
```

The branch remains alive; only the bad circular definition is removed.
