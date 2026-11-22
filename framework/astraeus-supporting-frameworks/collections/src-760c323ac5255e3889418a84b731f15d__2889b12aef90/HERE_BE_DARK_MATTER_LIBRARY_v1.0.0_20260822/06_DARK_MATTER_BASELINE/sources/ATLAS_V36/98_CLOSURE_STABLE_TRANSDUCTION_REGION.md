# 98 — Closure-Stable Transduction Region

## Definition

Let `C_TS` be the Time-Shell context graph/category candidate. Define the **closure-stable transduction region**
`C_TS^cl` as the largest currently recovered subregion in which:

1. forward realization `f_!` exists;
2. readback `f^*` exists;
3. the Time-Shell invariant contract is preserved;
4. unit round-trip retains an Identity Witness;
5. Dynamic Closure Recursion remains inside the same typed operator family.

Symbolically:

```text
C_TS^cl = {
  f : U -> V |
  f_!, f^* exist,
  I_T is recoverable,
  IdWitness(x, f^*f_!x),
  R_Cl preserves operator typing
}.
```

## Interpretation

This is the domain on which the shell has enough structure to support repeatable transduction/readback without losing the
mathematical grammar that defines the operation.

## Use

The closure-stable region is the correct place to search for a true adjunction. It prevents the Atlas from demanding a universal
categorical structure across domains where the source data supports only one-way translation or incomplete readback.

## Status

ATLAS_NATIVE CANDIDATE DOMAIN RESTRICTION.
