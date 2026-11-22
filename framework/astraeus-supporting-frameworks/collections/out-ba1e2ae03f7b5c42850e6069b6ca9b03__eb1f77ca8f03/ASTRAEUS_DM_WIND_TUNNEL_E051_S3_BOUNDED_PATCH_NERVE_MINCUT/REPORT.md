# ASTRAEUS Dark-Matter Wind Tunnel E051
## Bounded S3-Candidate Patch + Nerve + Min-Cut

**Bounded local merge seam:** PASS  
**Local nerve witness:** PASS  
**Unit-capacity channel multiplicity:** PASS  
**Physical runtime capacities:** OPEN  
**Physical dark matter:** NOT YET

I bypassed the runner-global locality problem from E050.

The E049 corridor seam survives inside the small patch:

`x=13..18, y=15..17, z=14..16`

with exactly the same merge threshold:

`0.604379076253`.

Immediately above that level A and B are disconnected.

At the merge they connect through a single topological bottleneck:

`unit min-cut = 1`.

As the corridor thickens:

- `t=0.60`: min-cut **2**
- `t=0.58`: min-cut **6**

So the local geometry goes:

`disconnected -> throat -> redundant corridor`.

The maximin path also admits a three-piece local good-cover nerve:

`U_A -- U_M -- U_B`.

This is compatible with the recovered admissible-nerve architecture without pretending
the entire ER network has been proven globally equivalent to S3.

I kept the capacity firewall intact: unit edges measure **topological path
multiplicity**, not physical `T_run`.

## Next

Track this same bottleneck skeleton across E1...E16.

That will tell us whether the local throat is History-organized and persistent, rather
than an accident of the final driven state.
