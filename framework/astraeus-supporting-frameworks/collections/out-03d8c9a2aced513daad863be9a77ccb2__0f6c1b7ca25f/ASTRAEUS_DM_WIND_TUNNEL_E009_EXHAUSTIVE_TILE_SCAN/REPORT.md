# ASTRAEUS Dark-Matter Wind Tunnel E009
## Exhaustive Native ER-Tile Readout-Degeneracy Scan

**Status:** exhaustive controlled sandbox enumeration  
**Physical dark-matter witness:** NOT ESTABLISHED  
**Parent/API promotions:** 0

## Why brute force here

The native ER tile is only `2 x 2 x 2`.

For this controlled parse, each site is allowed three local states:

- `-1`: occupied negative-chirality state
- `0`: empty
- `+1`: occupied positive-chirality state

Therefore the complete local state space contains exactly:

`3^8 = 6561`

microstates.

E009 enumerates **all 6,561**. No Monte Carlo sampling is used.

## Readout

A top-down XY readout records, for each of the four XY columns:

- occupancy count through depth;
- net chirality through depth.

Thus states with different hidden z-ordering can occupy the exact same declared
top-down readout class.

## Probe test

Every microstate is inserted into the native ER tensor under:

- persistence `p=0` (T0-T4 class);
- persistence `p=1` (T5+ class);
- both possible unlabeled ER chirality-index conventions.

The resulting ER state is then weighted by the local activation of:

- mounted Hydrogen H-v2;
- mounted Oxygen Phase-5.

A readout-degenerate pair is called **robust cross-probe distinguishable** only if
its ER response differs for H and O, at p=0 and p=1, under **both** chirality-index
conventions.

## Result

- total microstates: **6,561**
- distinct top-down readout classes: **1,296**
- degenerate readout classes: **1,215**
- classes with more than one adjacency signature: **729**
- classes containing at least one robust H/O-distinguishable hidden pair: **1,215**
- microstates lying in those robust classes: **6,480**
- fraction of complete controlled state space inside robust classes: **98.7654%**

The important result is qualitative:

> E001 was not a one-off hand-picked accident.

Across the entire controlled 2x2x2 three-state tile space, there are many classes
in which the **same top-down readout** contains microstates with different adjacency
and different ER response visible to **both** Hydrogen and Oxygen before and after
the T5 persistence boundary.

## What this closes

E009 closes the narrow sandbox question:

> Is readout-degenerate / ER-distinguishable hidden depth a rare special geometry
> that appeared only because E001 was chosen conveniently?

**No.**

It is a broad structural property of the controlled tile state space.

## What remains open

Not every enumerated (-1, 0, 1) tile state is automatically a physically admissible
MK43 state.

The next parse must filter the robust classes through:

1. Pipeline chirality/admissibility constraints;
2. persistence through T4/T5;
3. R4 candidate formation;
4. R5 finite-Bandwidth resolution;
5. R6 survivability.

Next handle:

`FILTER_E009_ROBUST_CLASSES_BY_PIPELINE_ADMISSIBILITY_PERSISTENCE_AND_R4_R6_SURVIVAL`
