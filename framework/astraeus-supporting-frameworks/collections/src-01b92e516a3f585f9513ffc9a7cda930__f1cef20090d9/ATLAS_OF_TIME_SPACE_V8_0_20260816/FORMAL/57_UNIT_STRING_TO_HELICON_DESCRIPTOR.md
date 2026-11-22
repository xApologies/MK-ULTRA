# 57 — Unit String → Helicon Descriptor Map

## Recovered source constraint

The recovered Helicon structural tuple is

```text
H = (L, Omega_H, C_H, W_H)
```

where `L` is a circulation loop/loop-family, `Omega_H` orientation circulation, `C_H` continuity circulation / redistribution density, and `W_H` winding/topology class.

Phase III also gives a native admissibility graph `G`, with `Helicon H subset G`. The Unit String is treated as an invariant continuation path. Atlas v7 therefore tests whether Helicon structure can be **read directly from normalized path configurations** without importing calculus.

## Unit-String configuration domain

Let

```text
U_1 = { c | Adm(c)=1 and ell(c)=1 }.
```

A configuration is an admissible finite/recursive path in the S3 continuity/path algebra, with invariant normalized path valuation `ell(c)=1`.

Let `U_H subset U_1` contain configurations that possess a closed circulation support or recoverable loop-family sufficient to define Helicon circulation data.

## Helicon descriptor

Define

```text
J_H : U_H -> X_H
```

by

```text
J_H(c)
=
(
  L(c),
  Omega(c),
  Ccirc(c),
  W(c)
).
```

Components:

1. `L(c)` = closed circulation support / loop-family carried by the configuration.
2. `Omega(c)` = orientation holonomy/circulation obtained by composing orientation transport around the loop-family.
3. `Ccirc(c)` = continuity-circulation class obtained from admissible edge-flow accounting around the loop-family.
4. `W(c)` = winding/topology class of the closed configuration.

This is a **descriptor map**, not yet a claim that every normalized Unit String is a Helicon.

## Helicon-compatible configuration

A configuration `c` is Helicon-compatible when its descriptor satisfies the recovered structural conditions for coherent restructuring, including the relevant closure, admissibility, orientation-circulation, continuity, and topology requirements.

Write

```text
Hel(c)=1
```

for this predicate.

Then

```text
U_Hel = { c in U_H | Hel(c)=1 }.
```

## Interpretation

Atlas v7 sharpens the earlier candidate:

```text
not every Unit-String configuration is a Helicon.
```

Instead:

```text
Helicon data are recoverable invariants of a coherent class of normalized continuation configurations.
```

This gives the Unit String a role beneath Helicon mode structure while preserving the recovered Helicon tuple.

## Status

**FORMAL CANDIDATE / SOURCE-COMPATIBLE.**

The tuple is recovered. The descriptor extraction rules are new Atlas formalization and require continued reconciliation with the full Helicon archive.
