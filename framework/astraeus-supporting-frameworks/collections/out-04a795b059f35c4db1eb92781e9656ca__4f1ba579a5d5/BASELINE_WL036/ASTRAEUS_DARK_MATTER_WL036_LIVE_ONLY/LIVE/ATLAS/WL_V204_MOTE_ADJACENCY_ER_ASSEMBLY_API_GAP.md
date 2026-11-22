# WL-v204 — Mote-Lattice Adjacency / ER-Foam Assembly API Gap

**QMO:** QMO-AST-DM-WL-088  
**Work layer:** WL-032  
**Parent promotions:** 0  
**Status:** API-EXPOSED GAP / P022 STAGE-1 BLOCKER

## Why this handle matters

The controlled dark-matter witness search no longer needs another broad gravity crawl. The primitive source already supplies a finite orientation-dependent adjacency generator:

```text
C_z = (chi_plus, chi_minus)
R_i(C_z) = C_i

e_ij exists iff A(s_i,s_j,rho_ij)=1
```

The Time-Space API then supplies the sub-Planck route through chirality-labelled motes, ER-throat incidence, weighted adjacency, adjacency lattice, and ER Foam.

The remaining question was whether the primitive adjacency difference is lawfully inherited into that ER realization.

## API answer

API 4.3 itself records the missing mathematics in its mote audit:

```text
[OPEN] Define adjacency edges on the eight-site lattice explicitly.
[OPEN] Derive ER-foam assembly rules from mote adjacency.
```

Therefore P022 Stage 1 is not blocked by an unknown vague “scale lift.” It is localized to a named API-exposed gap.

## Next handle

```text
@mote_lattice
```

with supporting handles:

```text
@mote_configuration_space
@mote_occupancy_function
@mote_chirality
@mote_ensemble
@er_throat_incidence
@weighted_adjacency
```

Registered context includes:

```text
@mote_lattice -> @mote_configuration_space
@mote_lattice -> @mote_occupancy_function
@mote_configuration_space -> @mote_chirality
@mote_ensemble -> @er_foam
@chirality_labelled_mote -> @er_throat_incidence
@er_throat_incidence -> @weighted_adjacency -> @adjacency_lattice -> @er_foam
```

The dependency `@mote_ensemble -> @er_foam` does **not** itself derive the missing assembly rule.

## P022 status

```text
primitive rotation-generated adjacency: SOURCE-GROUNDED
mote-lattice adjacency law: OPEN IN API
mote-adjacency -> ER assembly law: OPEN IN API
selected ER H0/H1 incidence pair: NOT YET EARNED
matter-null condition: NOT YET TESTED
hidden-state embedding: OPEN / source-blocked selection
metric-action selection: OPEN / API-atomic
qualification nonemptiness: OPEN
```

## Research move

Do not expand ordinary GR or invent a scale-lift theorem. Query `@mote_lattice` and its admissibility/configuration-space neighborhood and construct new mathematics only if the API does not expose a stronger existing source for its two declared open items.

This is exactly the kind of gap where work-layer mathematics is permitted: the API has identified the missing object and constrained its domain, neighboring handles, and target realization.
