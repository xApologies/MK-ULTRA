# WL-v212 — ER-Throat Incidence Dark-Readout Ingress

**QMO:** QMO-AST-DM-WL-096  
**Work layer:** WL-034  
**Parent promotions:** 0  
**Status:** CONTROLLED PAIR TEST READY / NONEMPTY WITNESS STILL OPEN

## API landscape

At radius 3, `@er_throat_incidence` meets `@dm_dark_matter_qualification_nonempty` only at:

```text
@er_foam
```

Against the closed `@dm_er_branch_readout_separation` branch, the interface additionally exposes:

```text
@weighted_adjacency
@adjacency_lattice
@er_foam
```

This is the cleanest current Stage-1 ingress.

## Controlled observation

Use the existing rotational pair:

```text
H0 = trivial/common-mode relative orientation History
H1 = persistent nontrivial relative orientation/shear/holonomy History
```

At fixed declared local Resolution/Bandwidth constraints, recover the corresponding ER-throat incidence/weight records when source-admitted:

```text
I0 = I_ER(H0)
I1 = I_ER(H1)
W0 = W_ER(H0)
W1 = W_ER(H1)
```

Stage-1 pass requires either:

```text
I0 != I1
```

or:

```text
W0 != W1
```

A null result is retained.

Only after a pass should the pair enter the existing ER readout / hidden-state / UCM / gravity qualification machinery.

## Current handle

```text
@er_throat_incidence
```

This is an observation/selection handle, not a dark-matter identity.
