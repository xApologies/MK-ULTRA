# WL-v232 — Recursive Chirality Evolution Cannot Define the Missing Adjacency

**QMO:** QMO-AST-DM-WL-116  
**Work layer:** WL-036  
**Parent promotions:** 0  
**Status:** CIRCULARITY FIREWALL / MOTE BRANCH LOCALLY EXHAUSTED

API 4.3 gives the recursive chirality evolution scaffold

```text
chi_{t+1}(x,y,z)
 = Pi_occ(
     sum_{n in N(x,y,z)} w_n chi_t(n)
     - lambda chi_t(x,y,z)
   ).
```

The API types `N(x,y,z)` as neighboring structures and `w_n` as coupling weights. The same mote-system audit explicitly keeps **the exact adjacency graph `N(x,y,z)` OPEN**.

Therefore this evolution object cannot be used to derive the missing mote adjacency without circularity: it already assumes the neighborhood whose selection P024 is trying to recover.

The source-backed dependency graph also forms the loop

```text
@mote_configuration_space
 <-> @recursive_chirality_evolution_field
```

but supplies no independent orientation-History -> neighborhood selector.

Disposition:

```text
creation/collapse route     -> pruned for runtime History (InfinityClass input)
local_recursive_state       -> semantic but graph-unlinked
mote_identity/inheritance   -> correct semantic neighborhood, no incidence map
recursive chirality update  -> assumes N(x,y,z), cannot define N(x,y,z)
```

The mote-specific P024 route is therefore **locally source-exhausted at the adjacency-selection problem**. Do not continue elaborating this branch.

**Next move:** return to global API ranking and select a fresh non-mote handle.
