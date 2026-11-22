# Major API-Native and QMO-Derived Objects

## `@native_unit_of_energy`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Addressable native energy unit feeding the general-energy sector.
- Declared parent/dependency handles: `@general_energy`
- Compiled equations: 5
- Compiled QMO records: 0
- API neighborhood: 3 incoming / 3 outgoing edges

## `@unit_of_energy`

- Provenance: `QMO_DERIVED`
- Role: Unit-level energy object kept distinct from the general-energy aggregate.
- Declared parent/dependency handles: `@native_unit_of_energy`
- Compiled equations: 1
- Compiled QMO records: 0
- API neighborhood: 1 incoming / 1 outgoing edges

## `@general_energy`

- Provenance: `API_NATIVE_DERIVATION`
- Role: General-energy target of the recovered native-energy vertical chain.
- Declared parent/dependency handles: `@native_unit_of_energy`
- Compiled equations: 6
- Compiled QMO records: 0
- API neighborhood: 3 incoming / 2 outgoing edges

## `@universal_coupling`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Cross-domain coupling object with its own equations and typed neighborhood.
- Declared parent/dependency handles: to be reconstructed in the object chapter
- Compiled equations: 6
- Compiled QMO records: 0
- API neighborhood: 2 incoming / 2 outgoing edges

## `@native_causal_order`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Native causal-order object used by locality, Lorentz-limit, and Graviton propagation structures.
- Declared parent/dependency handles: `@chirality`, `@locality`
- Compiled equations: 14
- Compiled QMO records: 0
- API neighborhood: 422 incoming / 12 outgoing edges

## `@native_constraint_closure`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Constraint algebra for preserving admissible native states across transduction.
- Declared parent/dependency handles: `@admissibility`, `@continuity_conservation`, `@chirality`, `@persistent_recursive_topology`, `@time_shell`
- Compiled equations: 16
- Compiled QMO records: 0
- API neighborhood: 427 incoming / 13 outgoing edges

## `@native_graviton_dispersion`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Native dispersion object supporting effective masslessness and propagation analysis.
- Declared parent/dependency handles: `@graviton`, `@gravitational_helicon_mode`
- Compiled equations: 15
- Compiled QMO records: 0
- API neighborhood: 22 incoming / 11 outgoing edges

## `@native_graviton_quantization`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Quantization object directed toward native probability preservation.
- Declared parent/dependency handles: `@graviton`
- Compiled equations: 10
- Compiled QMO records: 0
- API neighborhood: 1 incoming / 2 outgoing edges

## `@native_interaction_factorization`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Native factorization object used by soft-limit and multiparticle-gravity sectors.
- Declared parent/dependency handles: `@graviton`
- Compiled equations: 9
- Compiled QMO records: 0
- API neighborhood: 57 incoming / 8 outgoing edges

## `@native_probability_preservation`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Probability-preservation object feeding readable projection and unitarity audits.
- Declared parent/dependency handles: `@native_graviton_quantization`
- Compiled equations: 13
- Compiled QMO records: 0
- API neighborhood: 421 incoming / 8 outgoing edges

## `@continuity_conservation`

- Provenance: `QMO_DERIVED`
- Role: Conservation structure attached to continuity-sector perturbations.
- Declared parent/dependency handles: `@continuity_perturbation`
- Compiled equations: 6
- Compiled QMO records: 0
- API neighborhood: 2 incoming / 4 outgoing edges

## `@conservation_of_recoverable_structure`

- Provenance: `API_NATIVE_DERIVATION`
- Role: Conservation target for recoverable structural content.
- Declared parent/dependency handles: `@recoverability`
- Compiled equations: 2
- Compiled QMO records: 0
- API neighborhood: 2 incoming / 0 outgoing edges

## `@helicon`

- Provenance: `QMO_DERIVED`
- Role: Primary coherent-mode QMO and upstream projective domain.
- Declared parent/dependency handles: to be reconstructed in the object chapter
- Compiled equations: 10
- Compiled QMO records: 11080
- API neighborhood: 76 incoming / 190 outgoing edges

## `@time_shell`

- Provenance: `QMO_DERIVED`
- Role: Persistent boundary and translation-domain QMO.
- Declared parent/dependency handles: `@persistence`, `@chirality`
- Compiled equations: 11
- Compiled QMO records: 19729
- API neighborhood: 439 incoming / 155 outgoing edges

## `@graviton`

- Provenance: `QMO_DERIVED`
- Role: Projection-mode QMO mediating the gravity handoff.
- Declared parent/dependency handles: `@gravitational_helicon_mode`
- Compiled equations: 14
- Compiled QMO records: 46042
- API neighborhood: 678 incoming / 413 outgoing edges

