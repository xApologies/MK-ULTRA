# WL-v168 — ER Readout Branch / Rotational Symmetry Interface

**QMO:** QMO-AST-DM-WL-053  
**Status:** closed branch architecture queried; no witness promoted.

The radius-2 interface of `@dm_er_branch_readout_separation` and `@rotational_symmetry_constraint` is:

`{@er_foam, @graviton, @helicon, @gravitational_helicon_mode, @zer0_interaction}`.

The direct registered path is:

`@dm_er_branch_readout_separation -> @er_foam -> @helicon -> @rotational_symmetry_constraint`.

DM2.2 already marks the ER branch-separation object CLOSED. Therefore no new branch theorem is required.

## Next handle

`@er_foam` — the common source-native branch origin.

`@zer0_interaction` is deliberately not followed here; its appearance as an interface handle is not sufficient to give it a dark-sector role.
