# E051 — Bounded S3-Candidate Patch, Local Nerve, and Min-Cut Connectivity

## 1. Rebase

E050 showed that the reconstructed H2 ecology is not a clean physical-locality witness
because global summary operations couple separated diagnostics.

E051 therefore returns to the source-native finite network geometry:

`persistent support`
-> `admissible neighborhoods`
-> `continuity nerve`
-> `feasible flow`
-> `runtime capacity / cut`.

## 2. Bounded local patch

Use the E048 fixed-state corridor field and the E049 lobe addresses:

`A=(17, 16, 15)`

`B=(14, 16, 15)`.

Restrict to the bounded patch:

`x=13..18`,
`y=15..17`,
`z=14..16`.

This small patch preserves exactly the full-domain merge value:

`tau_merge=0.604379076252503`.

Therefore the recovered A-B coupling seam is genuinely local to this patch.

## 3. Exact connectivity transition

For threshold `t`, define the six-neighbor superlevel support graph:

`G_t = {x | K_hat(x)>=t}`.

The next discrete field level above the merge is:

`t_plus=0.6067716271752466`.

At `t_plus`, A and B are disconnected.

At `tau_merge`, they first connect.

One maximin path is:

`[(17, 16, 15), (17, 15, 15), (16, 15, 15), (15, 15, 15), (14, 15, 15), (14, 16, 15)]`.

The bottleneck/saddle is:

`(16, 15, 15)`

with:

`K_hat=0.604379076252503`.

## 4. Local nerve witness

Cover the selected corridor path by three path neighborhoods:

`U_A=[(17, 16, 15), (17, 15, 15), (16, 15, 15)]`

`U_M=[(16, 15, 15), (15, 15, 15), (14, 15, 15)]`

`U_B=[(14, 15, 15), (14, 16, 15)]`.

Each neighborhood is a contractible finite path.

Intersections obey:

`U_A intersect U_M != empty`

`U_M intersect U_B != empty`

`U_A intersect U_B = empty`

with no triple intersection.

Therefore the local nerve is:

`[U_A] -- [U_M] -- [U_B]`.

Its realization is an interval, matching the selected corridor path topology.

This is a **local good-cover witness** compatible with V13's admissible-nerve
architecture.

It does not establish a global ER-to-S3 equivalence.

## 5. Unit-capacity channel multiplicity

Canonical numerical `T_run(e)` is not available for this instance.

So assign unit edge capacities only as a topological comparator.

By standard max-flow/min-cut / Menger geometry, the value counts edge-disjoint
A-B channels.

Bounded patch:

- `t=0.606771627175`: connected=False, mincut=0, edge-disjoint paths=0, shortest=none
- `t=0.604379076253`: connected=True, mincut=1, edge-disjoint paths=1, shortest=5
- `t=0.6`: connected=True, mincut=2, edge-disjoint paths=2, shortest=5
- `t=0.58`: connected=True, mincut=6, edge-disjoint paths=6, shortest=3
- `t=0.55`: connected=True, mincut=6, edge-disjoint paths=6, shortest=3
- `t=0.5`: connected=True, mincut=6, edge-disjoint paths=6, shortest=3

Thus the local network thickens:

`disconnected`
-> `one-channel throat`
-> `two-channel corridor`
-> `six-channel corridor`.

The same merge and early cut values are reproduced in the full domain, so they are not
created by remote graph structure.

## 6. Runtime-capacity theorem boundary

V20 defines:

`T_run(e)=sup {Phi(e) | Phi in F_run}`

and inter-address runtime capacity by finite max-flow/min-cut.

Hence topology gives an exact prerequisite.

### Disconnected support

If no A-B path exists:

`Cap_run(A,B)=0`

on that selected support, irrespective of disconnected edge capacities.

### Connected support

If one A-B path exists and every edge on that path has strictly positive `T_run`, then:

`Cap_run(A,B)>0`.

The numerical magnitude remains open until the source-valid edge capacities are
instantiated.

So:

`topology decides possibility; capacity decides amount`.

## 7. Hidden-network response consequence

V31 proves that a positive hidden connected component touching at least two readable
ports has:

`Lambda_H != 0`.

Therefore, conditionally treating A and B as ports of a positive admitted hidden
network:

- above the merge: no two-port hidden connection;
- at/below the merge: a nonzero reduced hidden-network response exists for some port
  contrast.

This is still below the gravity claim.

## 8. Result

The current dark-defect geometry now has a source-compatible local skeleton:

`two separated patches`
-> `one bottleneck throat`
-> `redundant multi-route corridor`.

The skeleton is recovered inside a bounded patch, admits a local nerve presentation,
and has exact unit-capacity cut multiplicities.

No physical `T_run` numbers were fabricated.

## 9. Next hunt

Track this same bounded A-B bottleneck skeleton across the E043 endogenous History
orbit.

If its merge threshold / min-cut multiplicity evolves systematically and then
stabilizes with the History basin, the hidden state carries a persistent local network
skeleton rather than a fixed-state accident.
