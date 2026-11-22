# 144 — Dual Selector Compatibility: Xi-Maximality and R5 Minimal Strain

## Purpose

Two independent source lines select admissible gravitational/continuity paths without native calculus.

### Phase III gravitational selector

For an admissible restructuring path `P`:

```text
P* = argmax Xi(P)
```

where `Xi(P)` is path efficiency and the interpretation is maximal admissibility continuity efficiency.

### UCM R5 selector

For an R4 candidate corridor `c`:

```text
c* = argmin TotalStrain(c)
```

subject to:

```text
ChiralityOK(c)
BandwidthOK(c)
AncestryOK(c)
Recoverable(c)
ordered closure / minimized topology conflict.
```

The sources do **not** provide an equation identifying `Xi` with inverse strain. V19 therefore refuses to invent one.

## Common typed domain

Let

```text
C_R4
```

be an R4 corridor candidate family. Define the feasible set

```text
C_feas
=
{
 c in C_R4
 |
 ChiralityOK(c)
 and BandwidthOK(c)
 and AncestryOK(c)
 and Recoverable(c)
}.
```

Where a corridor can be represented as an admissible restructuring path, introduce only the typing map

```text
iota : C_feas -> P_adm.
```

No additional physical law is assigned to `iota`.

Define

```text
C_Xi
=
Argmax_{c in C_feas} Xi(iota(c))
```

and

```text
C_S
=
Argmin_{c in C_feas} TotalStrain(c).
```

## Dual-selector compatibility set

The simultaneous source-compatible selector is

```text
C_* = C_Xi intersect C_S.
```

This yields a falsifiable consistency condition:

```text
C_* != empty.
```

Interpretation:

- `|C_*| = 1` — the two recovered selectors jointly determine one corridor;
- `|C_*| > 1` — a degeneracy survives and R6/R7 or another recovered invariant must resolve it;
- `C_* = empty` — the two selector rules cannot both describe the same decision event under the current typing. The branch must be retyped, reconciled, or rejected. No weighted compromise may be inserted without a declared new constitutive assumption.

## Why this matters

This converts two verbal selection principles into one geometry-first audit object while preserving their independence.

It does **not** define a numerical strain law and does **not** define `Xi` numerically. It is valid at the ordering/extremizer level.
