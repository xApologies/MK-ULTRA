# ASTRAEUS Dark-Matter Wind Tunnel E010
## Pipeline Robustness Filter of the Exhaustive Tile Scan

**Status:** controlled pipeline-guard / R4-R6 robustness result  
**Physical dark-matter witness:** NOT ESTABLISHED  
**Parent promotions:** 0

## Result

E009 found 1,215 readout-degenerate classes in the complete controlled 6,561-state tile
space.

E010 now applies explicit local Pipeline/ER guards, removes pairs related by any of the
48 cube coordinate symmetries, and stress-tests R5 selection.

### Single-corridor Bandwidth

For `B=1..4` simultaneously:

- non-symmetry classes with a pair guaranteed to remain distinct under every tested R5
  score/tie condition: **0**

So the single-corridor limit can always annihilate the nontrivial hidden distinction somewhere
in the tested model family.

### Multi-corridor Bandwidth

For `B=2,3,4`:

- readout classes containing a non-symmetry hidden pair that remains separated under **every**
  deterministic scoring/tie condition: **148**
- distinct microstates in those representative pairs: **296**
- occupied-site range of the survivors: **4..7**

Then every one of those 148 pairs was tested against **10,000 additional random
R5 weight vectors**, under both ER chirality-index conventions and B=2,3,4.

Random-stress failures:

**0**

## Interesting controlled feature

A sharp sandbox threshold appears:

`B = 1`
does not provide selection-guaranteed non-symmetry hidden retention,

while

`B >= 2`
admits a family of strongly robust readout-degenerate hidden topologies.

Within this controlled model the dark-like distinction therefore behaves less like an
isolated hidden bit and more like a **relational multi-corridor structure**.

This is especially interesting because the live MK43 architecture treats Bandwidth as finite
organizational capacity rather than merely a numerical storage count.

## Boundary

The experiment uses corridor count `B` as a controlled finite-Bandwidth proxy.

It is **not yet** a source-derived calibration of the project's Bandwidth Algebra.

Therefore E010 records a new handle rather than promoting a law.

## Next handle

`TEST_MULTICORRIDOR_THRESHOLD_AGAINST_BANDWIDTH_ALGEBRA_AND_SOURCE_NATIVE_RESOLUTION`
