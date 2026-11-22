# WL-v213 — ER-Throat Pair Test Stops at Representation Seam

**QMO:** QMO-AST-DM-WL-097  
**Work layer:** WL-035  
**Parent promotions:** 0  
**Protocol:** AST-DM-WL-P024  
**Status:** REPRESENTATION_SEAM_OPEN / INCIDENCE NOT EVALUATED

## Question

P024 asked whether the frozen rotational-History pair

```text
H0 = common-mode / trivial relative orientation History
H1 = persistent nontrivial relative orientation / shear / holonomy History
```

could be represented in the API-4.3 `@chirality_labelled_mote` class and then compared at:

```text
@er_throat_incidence
@weighted_adjacency
```

under the same declared local Resolution/Bandwidth constraints.

## Source result

The detailed modern mote family and the older `@chirality_labelled_mote` handle occupy overlapping source neighborhoods, but the mounted API exposes no direct source-typed representation/equivalence map:

```text
@mote  -/->  @chirality_labelled_mote
```

The clean ER chain exists:

```text
@chirality_labelled_mote
  -> @er_throat_incidence
  -> @weighted_adjacency
  -> @adjacency_lattice
  -> @er_foam
```

but P024 Stage A requires the controlled H0/H1 states to be admitted into its source class before incidence can be recovered.

## Disposition

P024 returns:

```text
REPRESENTATION_SEAM_OPEN
```

not:

```text
I0 = I1
```

and not:

```text
I0 != I1.
```

No incidence/weight comparison was mathematically available, so the branch cannot be called a positive or null ER-incidence witness.

## Next-handle rule

Do not manufacture a mote representation or adjacency law.

Return to the already-mounted `@chirality_fabric` source and follow the next source-native structural handle exposed by its query runtime:

```text
@holonomy_class
```

The ER-incidence route remains preserved as an independent blocked witness route.
