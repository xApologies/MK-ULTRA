# ASTRAEUS Dark-Matter Wind Tunnel E012
## T5 Route Persistence + Rainbow-Road Portal Contract Audit

**Status:** route-persistence result / Portal typing audit  
**Physical dark-matter witness:** NOT ESTABLISHED  
**Parent promotions:** 0

## Question

E011 showed that every robust E010 state has at least one optimal two-corridor
selection that can geometrically compose into a route.

E012 asks two separate questions:

1. Does a route survive the `p=0 -> p=1` persistence transition associated with
   the T4/T5 boundary?
2. Does that route already satisfy the full Rainbow-Road Portal transaction contract?

These must not be conflated.

## Route-persistence test

For each of the **296** robust states:

- compute all optimal connected B=2 route selections at `p=0`;
- compute all optimal connected B=2 route selections at `p=1`;
- use both ER chirality-index conventions;
- use every deterministic E010 score condition;
- require that, for every condition, at least one **same connected route**
  is optimal on both sides of the persistence boundary.

Results:

- states passing strict T5 route persistence:
  **224 / 296**
- states possessing one single fixed route that survives *all* tested conditions
  and both persistence regimes:
  **0 / 296**
- robust hidden pairs for which both states pass the strict route-persistence test:
  **92 / 148**
- pairs where both sides possess one globally fixed route:
  **0 / 148**

Thus route persistence is a meaningful additional filter beyond mere route readiness.

## Portal contract

The mounted Portal Interconnect Architecture requires:

`source address`
`target address`
`geometric identity`
`occupancy`
`chirality`
`basin distribution`
`persistence contract`
`invariant residue`
`ancestry`
`provenance`
`resolution required`
`bandwidth required`
`closure target`.

For the controlled E010 tile grammar we can currently supply:

- source/target graph addresses;
- state identity;
- occupancy;
- chirality;
- ancestry;
- complete experiment provenance;
- R1 Resolution separation;
- an experimentally tested persistence contract.

But we **cannot** source-validly supply yet:

- `basin_distribution`;
- tile-state `invariant_residue`.

And only partially:

- source Bandwidth cost/capacity;
- destination closure.

Therefore:

**Full Portal transactions closed: 0.**

That is a typing boundary, not a route failure.

## Interpretation

Rainbow Road is now doing something precise in the dark-matter branch:

`Pipeline`
selects/stabilizes candidate relations,

while

`Rainbow Road`
asks whether those relations form a persistent navigable route with a complete
identity/recovery transaction contract.

E012 shows that route persistence can survive the T5 transition for a nontrivial
subset of the robust hidden states, but full Portal semantics require additional
metadata not yet recovered for the tile grammar.

## Next handle

`RECOVER_TILE_TO_BASIN_AND_INVARIANT_RESIDUE_TYPING_OR_KEEP_RAINBOW_ROAD_AS_ROUTE_ONLY`
