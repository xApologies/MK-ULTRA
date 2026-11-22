# WL-v231 — Inheritance Is the Source-Native Mote-Identity / History Seam

**QMO:** QMO-AST-DM-WL-115  
**Work layer:** WL-036  
**Parent promotions:** 0  
**Status:** SEMANTIC CARRIER RECOVERED / TRANSFORMATION UNRESOLVED

The mote system source states:

```text
@inheritance
  carries @occupancy
  carries @chirality
  carries @orientation_history
  carries @mote_identity
```

and the registered dependency graph explicitly contains

```text
@inheritance -> @occupancy
@inheritance -> @mote_identity.
```

This identifies the correct runtime neighborhood after pruning the Infinity-spectrum collapse branch: rotational History belongs on the inherited-organization side of the mote, not by rewriting the primitive collapse input.

The source-backed graph does **not** contain a registered `@inheritance -> @orientation_history` edge even though the canonical prose gives that semantic role, nor does `@mote_identity` have an outgoing edge into ER-throat incidence.

Pairwise QMO comparison with `@er_throat_incidence` meets through `@occupancy` / `@persistent_recursive_topology` at larger radius, not through a direct identity-to-incidence map.

Therefore the useful result is a reorientation of the search, not a closed transformation:

```text
History candidate
 -> inherited organization neighborhood
 -> mote state/identity/occupancy
 -?-> adjacency/incidence
```

No History -> mote-identity law is invented.

**Next handle:** `@recursive_chirality_evolution_field` as the nearest state-update object, with a circularity audit required before use.
