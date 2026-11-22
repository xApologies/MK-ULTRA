# ASTRAEUS Dark-Matter Wind Tunnel E015
## Support-Aware Cross-Probe Test of Persistent Route Memory

**Status:** controlled correction of E014  
**Physical dark-matter witness:** NOT ESTABLISHED  
**Parent promotions:** 0

## Why E014 failed its strongest claim

E014 required every Hydrogen/Oxygen projection to return a nonzero route-memory response.

That produced `0/92` all-test passes.

The failure audit shows the cause is not hidden-route annihilation.

The `O_max_abs` projection has **exactly zero local activation on all eight sites**
of the selected 2x2x2 ER tile.

A probe with zero overlap with the tested region cannot interrogate that region.

So its zero result is a null measurement, not evidence that the route family disappeared.

No other failed probe is removed.

## Support rule

Before looking at pair separation, define a probe as locally valid only when:

`sum_tile |W_probe| > 0`.

This is a geometric overlap precondition.

## Retest

Valid local probes:

- `H_mean_abs`
- `H_l2_norm`
- `H_max_abs`
- `H_semantic_shell_env`
- `O_mean_abs`
- `O_l2_norm`

Stress dimensions retained:

- both persistent-route memory encodings;
- both ER chirality-index conventions;
- every locally supported Hydrogen/Oxygen projection;
- all 92 same-readout T5-persistent route-family pairs.

Total supported pair tests:

**2,208**

Pairs with nonzero response under **every** supported test:

**92 / 92**

Global worst-case L2 separation:

`0.0552359034227`

Median pair worst-case L2:

`0.237851638422`

## Ruling

Within the controlled route-memory diagnostic, persistent route-family information
is cross-probe visible to both H and O whenever the probe actually overlaps the local
ER region being tested.

This repairs E014 without hiding its failed null-support control.

## Boundary

The route-family -> probe-response law is still work-layer mathematics.

It is not yet a source-canonical UCM/Portal response equation.

Next:

`COMPARE_ROUTE_FAMILY_MEMORY_WITH_ENDOGENOUS_ER_HISTORY_AND_UCM_RESPOND`
