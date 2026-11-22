# ASTRAEUS Dark-Matter Wind Tunnel E052
## History-Persistent Local Min-Cut Skeleton

**Fresh state:** no corridor skeleton  
**First endogenous write:** skeleton appears  
**E1-E16 skeleton persistence:** exact  
**Physical dark matter:** NOT YET

This one is clean.

At E0 the corridor field is zero.

At E1, the local A-B throat appears.

From E1 through E16, all of the following stay exactly unchanged:

- the maximin merge path;
- the one-edge bottleneck cut;
- unit min-cut at merge = **1**;
- unit min-cut at `t=0.60` = **2**;
- unit min-cut at `t=0.58` = **6**.

So the local defect skeleton is created by the first History write and then persists
combinatorially through the entire orbit.

What changes is its normalized merge strength:

`tau_1=0.606951849`

relaxing monotonically toward:

`tau_*=0.604379076`.

So we now have:

`persistent discrete skeleton + relaxing merge-strength coordinate`.

That local skeleton actually stabilizes **earlier** than the full E044 substrate
topography.

## Next

Test whether other dominant corridor-lobe pairs in E* show the same History-created
persistent skeleton pattern.

That tells us whether this is one special throat or a genuine family of local hidden
defects.
