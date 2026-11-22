# ASTRAEUS Dark-Matter Wind Tunnel E027
## History / Residue / Holonomy Retype

**Status:** formal seam recovered; numerical/instance holonomy remains open  
**Physical dark-matter witness:** NOT YET  
**Parent promotions:** 0

## The source changed the target

The current source does not support the simple idea:

`History -> different invariant residue`.

For an admissible Chirality Corridor with inherited states:

`xi_0 -> xi_1 -> ... -> xi_N`

the source explicitly requires:

`Inv(xi_n) = Inv(xi_0)`

at every stage.

So E027 defines the derived corridor-residue map:

`Res_corr(H_W) := Inv(xi_0)`.

This is well-defined on source-valid corridor histories because residue is constant
through the traversal.

The corridor source also calls the S3-class corridor the **accumulated ordered History**
of the S2 states and requires matching residue for corridor composition.

## Where History actually goes

Version-1 UTO gives the stronger clue.

`TRANSPORT(T,path)` must:
- append the path to History;
- update holonomy records;
- preserve provenance.

Therefore:

`History -> transport -> Holonomy`

is more source-native than:

`History -> residue value`.

The canonical residue bundle then supplies a Hermitian connection, and its curvature
measures failure of path-independent transport.

That means two routes can share:
- source;
- target;
- preserved residue;

while differing by the transport accumulated along the path.

## E013 loop opportunities

E023 already contained:

**34/92**

same-readout hidden pairs with at least one same typed endpoint but different route word.

In the exact 2x2x2 route catalog, alternative two-edge paths between one endpoint pair
close into simple four-edge loops.

Unique loop supports recovered:

**6**

All are square four-edge cycles:

**True**

Those are **holonomy candidates**, not measured holonomies.

No connection matrices or source-valid route transport operator have yet been assigned
to the E013 cube edges, so E027 does not invent a holonomy value.

## Consequence for E026

The fixed Hydrogen quantum-anchor fiber does not require the hidden distinction to be
stored as different invariant-residue labels.

A cleaner source-compatible architecture is:

`same quantum anchor`
+
`preserved residue structure`
+
`different History / transport holonomy`
+
`different pre-G response`.

This is exactly the kind of lifted distinction that can survive a quotient/readout.

## Next handle

`TYPE_E013_SAME_ENDPOINT_ROUTE_LOOPS_INTO_RESIDUE_BUNDLE_HOLONOMY_AND_SEARCH_FOR_SOURCE_VALID_CONNECTION_INSTANCE`
