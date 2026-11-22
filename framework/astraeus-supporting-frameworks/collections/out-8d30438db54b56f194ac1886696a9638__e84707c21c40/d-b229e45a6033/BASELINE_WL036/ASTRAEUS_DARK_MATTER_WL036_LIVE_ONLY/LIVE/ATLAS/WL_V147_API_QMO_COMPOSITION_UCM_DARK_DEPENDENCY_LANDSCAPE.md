# WL-v147 — API-Generated QMO Composition and UCM/Dark-Matter Dependency Landscape

## Status

- Work layer: WL-023
- Parent promotions: 0
- Method: API-first QMO generation / dependency-landscape composition
- Parent source mutation: none

## 1. Operational correction

The mounted project already contains the parent navigation tool `cross_qmo_chain.py`, whose own header states that it cross-crawls Time-Space 4.3 and Dark Matter 2.2 without promoting candidate relations. This directly matches the intended QMO workflow: query registered handles, preserve edge direction/provenance, form graph objects, then combine graph objects before writing new mathematics.

Time-Space API 4.3 itself requires:

```text
push starting handle
-> resolve aliases
-> merge dependency landscape
-> expand registered edges recursively
-> construct dependency network
-> recover mathematical object
-> derive equations
-> validate closure
-> register new handles and edges only after closure
-> preserve provenance classes
```

and explicitly says every generated dependency graph is a mathematical object.

## 2. QMO-UCM

Define the API-generated graph object

`Q_U = (V_U,E_U,pi_U)`

from a bidirectional radius-3 crawl of `@universal_coupling` in Time-Space 4.3 while preserving original edge directions and provenance.

Recovered size:

- |V_U| = 33
- |E_U| = 96 registered edge records
- distance histogram = {0: 1, 1: 2, 2: 10, 3: 20}

No derived RP-46 inverse/composed edges were required to construct this local object; this work-layer extraction used high-confidence non-derived registered Time-Space edges.

## 3. QMO-DM

Define

`Q_D = (V_D,E_D,pi_D)`

from a bidirectional radius-3 crawl of `@dm_dark_matter_qualification_locus` in Dark Matter 2.2 using its registered direct edge ledgers.

Recovered size:

- |V_D| = 89
- |E_D| = 313 registered edge records
- distance histogram = {0: 1, 1: 9, 2: 20, 3: 59}

## 4. Dependency-landscape composition

The two QMOs are combined only on exact shared handles:

`I_UD = V_U intersect V_D`.

For this crawl:

`|I_UD| = 12`.

The interface is:

- `@admissibility` — UCM radius 2, DM radius 3
- `@gravitational_helicon_mode` — UCM radius 2, DM radius 3
- `@native_constraint_closure` — UCM radius 2, DM radius 3
- `@native_graviton_dispersion` — UCM radius 2, DM radius 3
- `@spin_2_projection` — UCM radius 2, DM radius 3
- `@graviton` — UCM radius 3, DM radius 2
- `@time_shell` — UCM radius 3, DM radius 2
- `@chirality` — UCM radius 3, DM radius 3
- `@continuity_conservation` — UCM radius 3, DM radius 3
- `@gravitational_self_coupling` — UCM radius 3, DM radius 3
- `@helicon` — UCM radius 3, DM radius 3
- `@readable_graviton_projection` — UCM radius 3, DM radius 3

Define the composed dependency landscape as the typed graph union / pushout-like gluing

`L_UD = Q_U union_(I_UD) Q_D`.

This operation creates no new parent edge. It preserves the provenance map on every inherited edge.

The important result is therefore structural rather than physical:

**The UCM and dark-matter qualification graph objects are already connected through a 12-handle API-registered interface. A bespoke cross-API gravity bridge is not required merely to connect the mathematical landscapes.**

## 5. Forward API convergence paths

Using only registered Dark-Matter direct edges plus high-confidence non-derived Time-Space edges, the combined graph yields:

### Hidden-state branch -> Universal Coupling

`@dm_hidden_state_embedding` --DEPENDS_ON--> `@dm_constraint_preserving_embedding_family`  [DARK_MATTER_API_2.2; OPEN_HANDLE]
`@dm_constraint_preserving_embedding_family` --DEPENDS_ON--> `@native_constraint_closure`  [DARK_MATTER_API_2.2; ATLAS_DERIVED]
`@native_constraint_closure` --DIRECTED_TO--> `@graviton_radiative_stability`  [TIME_SPACE_API_4.3; recovered]
`@graviton_radiative_stability` --USED_BY--> `@universal_coupling`  [TIME_SPACE_API_4.3; recovered]

### Dark-matter qualification -> Universal Coupling

`@dm_dark_matter_qualification_locus` --DEPENDS_ON--> `@dm_er_branch_readout_separation`  [DARK_MATTER_API_2.2; ATLAS_DERIVED]
`@dm_er_branch_readout_separation` --DEPENDS_ON--> `@time_shell`  [DARK_MATTER_API_2.2; ATLAS_DERIVED]
`@time_shell` --FORMALLY_DEPENDS_ON--> `@native_constraint_closure`  [TIME_SPACE_API_4.3; recovered]
`@native_constraint_closure` --DIRECTED_TO--> `@graviton_radiative_stability`  [TIME_SPACE_API_4.3; recovered]
`@graviton_radiative_stability` --USED_BY--> `@universal_coupling`  [TIME_SPACE_API_4.3; recovered]

### Metric-action selection -> Universal Coupling

`@dm_metric_action_selection` --DEPENDS_ON--> `@dm_covariant_hidden_action_family`  [DARK_MATTER_API_2.2; OPEN_HANDLE]
`@dm_covariant_hidden_action_family` --DEPENDS_ON--> `@diffeomorphism_invariance`  [DARK_MATTER_API_2.2; ATLAS_DERIVED]
`@diffeomorphism_invariance` --FAMILY_DEPENDS_ON--> `@einstein_field_equation`  [TIME_SPACE_API_4.3; recovered]
`@einstein_field_equation` --DEPENDS_ON--> `@einstein_tensor`  [TIME_SPACE_API_4.3; recovered]
`@einstein_tensor` --FAMILY_DEPENDS_ON--> `@riemann_tensor`  [TIME_SPACE_API_4.3; recovered]
`@riemann_tensor` --GENERATED_BY--> `@metric_perturbation`  [TIME_SPACE_API_4.3; recovered]
`@metric_perturbation` --DEPENDS_ON--> `@graviton`  [TIME_SPACE_API_4.3; recovered]
`@graviton` --DEPENDS_TO--> `@time_shell`  [TIME_SPACE_API_4.3; recovered]
`@time_shell` --FORMALLY_DEPENDS_ON--> `@native_constraint_closure`  [TIME_SPACE_API_4.3; recovered]
`@native_constraint_closure` --DIRECTED_TO--> `@graviton_radiative_stability`  [TIME_SPACE_API_4.3; recovered]
`@graviton_radiative_stability` --USED_BY--> `@universal_coupling`  [TIME_SPACE_API_4.3; recovered]

These paths do not solve their open source objects. They show that the open dark-matter branches already terminate inside the established UCM/graviton/constraint landscape rather than outside it.

## 6. Retyping of the research workflow

The primary work operation is now:

```text
API handle pair
-> QMO graph object
-> API crawl
-> second QMO
-> exact-handle graph composition
-> dependency landscape
-> crawl the landscape
-> expose remaining OpenSlots
-> generate another QMO only at the exposed slot
```

The previous practice of manually constructing long bridges before asking the APIs is superseded as the default work-layer method.

## 7. Current exposed frontier

The combined landscape leaves the parent dark-matter open handles open:

- `@dm_hidden_state_embedding`
- `@dm_metric_action_selection`
- `@dm_dark_matter_qualification_nonempty`

but it changes how they are attacked. They should now be queried as QMO chains against the shared interface handles, especially:

- `@native_constraint_closure`
- `@time_shell`
- `@graviton`
- `@readable_graviton_projection`
- `@gravitational_self_coupling`
- `@universal_coupling`

The next operation is not to invent another bridge. It is to generate targeted QMO pairs around these open handles and interface handles, compose them, and let the APIs expose the smallest residual mathematical gap.

## 8. Guardrails

- QMO connectivity != physical realization.
- A shared handle != identity of all objects represented around that handle.
- A reverse graph traversal is navigation only; it does not reverse a dependency law.
- No new parent handle or edge has been registered.
- Dark-matter nonemptiness remains unproved.
- Parent promotions remain zero.
