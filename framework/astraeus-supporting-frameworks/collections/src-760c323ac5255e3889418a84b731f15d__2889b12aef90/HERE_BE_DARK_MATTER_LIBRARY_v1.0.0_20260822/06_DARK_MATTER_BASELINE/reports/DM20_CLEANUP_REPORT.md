# Dark Matter API 2.0 Cleanup Report

## Promoted correction

DM1 contained:

```text
@dm_continuity_laplacian
USES
@dm_runtime_transition_capacity
```

Self-crawl exposed a circular definition.

Atlas source audit showed the correct separation:

```text
w_e = kappa_ij A_ij
```

defines the Laplacian coefficient, while:

```text
T_run(e)
```

is a global realizable flow ceiling.

DM2 therefore promotes:

```text
@dm_local_continuity_response_coefficient
```

and changes the capacity relation to a non-definition saturation guard.

## Boundary cleanup

DM1's:

```text
@dm_hidden_boundary_realization
```

mixed three mathematical jobs.

DM2 supersedes it with:

```text
@dm_hidden_state_embedding
@dm_formal_persistence_qualification
@dm_persistent_boundary_incidence
```

No branch is lost.

The path is merely typed correctly.

## Open mathematics

Master-QMO OpenSlots are now real API handles rather than hidden question
marks.

They are queryable but remain unresolved.

## Complexity policy

Direct DM edges:

`62`

Derived composed dependency pairs:

`4605`

The direct graph stays compact.

The dense recursive mathematics lives in the closure index.

## Circularity

Child nontrivial SCC count after cleanup:

`1`

Result:

```text
PASS — no Dark Matter child handle participates in a nontrivial dependency SCC after semantic correction.
```

## Final semantic correction

`@dm_formal_persistence_qualification` now:

```text
DEPENDS_ON @persistent_locus
```

because the dark-specific predicate evaluates against the already-defined
formal Persistent Locus. The parent locus does not depend on the child
qualification test.

This removes the apparent child participation in an inherited Time-Space
recursive SCC without altering the parent recursion.
