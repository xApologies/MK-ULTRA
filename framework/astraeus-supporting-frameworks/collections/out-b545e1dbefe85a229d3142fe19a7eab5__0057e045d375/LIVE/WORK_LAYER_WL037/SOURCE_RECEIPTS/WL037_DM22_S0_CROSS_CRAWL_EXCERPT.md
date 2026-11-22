-Space handles touching two or more distinct
dark-matter branches.

Top examples:

- `@mote` — 6 branches, branch distances {'chromatic': 2, 'network': 2, 'readout': 2, 'state_persistence': 2, 'load': 2, 'mode0': 2}
- `@mote_closure` — 5 branches, branch distances {'chromatic': 2, 'network': 1, 'state_persistence': 2, 'load': 2, 'history': 2}
- `@mote_lattice` — 4 branches, branch distances {'network': 1, 'state_persistence': 1, 'load': 1, 'history': 2}
- `@closure` — 4 branches, branch distances {'network': 2, 'state_persistence': 2, 'load': 2, 'history': 1}
- `@native_constraint_closure` — 4 branches, branch distances {'chromatic': 2, 'network': 1, 'readout': 2, 'history': 2}
- `@recoverability` — 4 branches, branch distances {'network': 2, 'state_persistence': 2, 'load': 2, 'history': 1}
- `@mote_ensemble` — 4 branches, branch distances {'network': 2, 'readout': 2, 'state_persistence': 2, 'load': 2}
- `@geodesic` — 3 branches, branch distances {'network': 2, 'readout': 1, 'state_persistence': 2}
- `@native_causal_order` — 3 branches, branch distances {'network': 1, 'readout': 2, 'state_persistence': 2}
- `@mote_diagonal_rule` — 3 branches, branch distances {'network': 2, 'state_persistence': 2, 'load': 2}
- `@mote_occupancy_function` — 3 branches, branch distances {'network': 2, 'state_persistence': 2, 'load': 2}
- `@planck_landscape` — 3 branches, branch distances {'chromatic': 2, 'state_persistence': 2, 'history': 2}
- `@smooth_manifold` — 3 branches, branch distances {'chromatic': 2, 'network': 2, 'history': 2}
- `@unit_string` — 3 branches, branch distances {'network': 2, 'readout': 2, 'state_persistence': 2}
- `@cosmology` — 2 branches, branch distances {'network': 2, 'readout': 1}
- `@general_relativity` — 2 branches, branch distances {'readout': 1, 'load': 2}
- `@S0` — 2 branches, branch distances {'network': 2, 'state_persistence': 2}
- `@adjacency_lattice` — 2 branches, branch distances {'network': 2, 'readout': 2}
- `@native_probability_preservation` — 2 branches, branch distances {'network': 2, 'readout': 2}
- `@ringdown` — 2 branches, branch distances {'readout': 2, 'mode0': 2}

The crawl did **not** blindly import them.

The high-degree `mote` family, for example, is mathematically close to many
branches but would increase the API surface substantially without resolving
a current blocker.

`@native_constraint_closure`, by contrast, directly reduces a current
primary blocker and has an explicit source-level type/equation record, so it
was promoted.

---

## Operation B — Dark Matter 2.1 crawled against the full Time-Space 4.3 API

Novel Time-Space handles exposed beyond the smaller DM parent subgraph:

```text
1 parent hop: 17
2 parent hops: 101
3 parent hops: 279
```

Again, this is a mining field, not an import list.

### Promoted parent handles

```text
@native_constraint_closure
@total_action
@diffeomorphism_invariance
@particle_readable_organization
```

Why only these four:

1. each resolves or sharply reduces a current dark-matter obligation;
2. each has source-backed role/type evidence in API 4.3;
3. none introduces a new dimensional assumption;
4. none reopens a quarantined branch;
5. each supports a compact new mathematical object.

---

# Three cross-API objects earned

## 1. `@dm_constraint_preserving_embedding_family`

```text
Emb_H,phys^R
=
{
 iota_H:E_H^R -> E
 |
 base diagram commutes,
 inheritance diagram commutes,
 image lies in ker(C)
}.
```

This turns hidden-state embedding from a vague monomorphism problem into a
physical-state-preserving embedding problem.

It does not prove the family is nonempty.

## 2. `@dm_covariant_hidden_action_family`

```text
S_H^cov(Q_H,g)
subseteq
S_adm(Q_H,g)
```

with compatibility to the parent:

```text
total action
-> diffeomorphism invariance
-> Noether / conservation architecture.
```

This removes arbitrary action guessing from the primary path.

## 3. `@dm_er_branch_readout_separation`

The parent ER-Foam branch contract independently realizes:

```text
localized persistent topology
-> particle/matter readability
```

and:

```text
propagating/helicon organization
-> gravity readability.
```

That supplies a source-backed architecture underneath the existing dark
readout defect.

It does not prove a physical dark state inhabits the defect.

---

# Candidate generated but not promoted

`QMO-XAPI-CAND-001` reframes dark-matter nonemptiness as a con