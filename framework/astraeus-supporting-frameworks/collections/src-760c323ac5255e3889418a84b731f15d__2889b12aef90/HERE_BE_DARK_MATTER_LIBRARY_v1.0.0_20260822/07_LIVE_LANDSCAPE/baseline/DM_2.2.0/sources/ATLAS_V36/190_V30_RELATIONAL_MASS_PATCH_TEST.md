# V30 — Relational Mass Patch Test

## Recovered pair correction

The Mass formalism defines, for an admissible organizational composite,

```text
DeltaMass_rel([K1],[K2])
=
Mass_MK([K1 star K2])
-
Mass_MK([K1])
-
Mass_MK([K2]).
```

Its sign may be positive, zero, or negative.

## Finite network-patch generalization

Let a finite hidden-network patch have readable T4 lock constituents

```text
K_1,...,K_n
```

and let `K_N` be a declared, provenance-preserving admissible composite formed from them and their admitted relational closure. No associativity of `star` is assumed; the actual construction tree belongs to provenance.

If

```text
K_N in D_M4,
```

define the network relational Mass residual

```text
DeltaMass_N
=
Mass_MK([K_N])
-
sum_i Mass_MK([K_i]).
```

## Interpretation

If the visible reference contains the isolated lock contributions while the full state differs only by admitted hidden relational closure, then `DeltaMass_N` is the exact Native Mass residual associated with that relational closure on the declared patch.

The sign is not assumed.

## Domain firewall

If `K_N` is not Mass-admissible or cannot form bounded T4 closure, `DeltaMass_N` is undefined. It must not be set to zero.

Therefore the global inter-galactic S3 network is not automatically a single Native Mass object.

A local/patch Mass channel exists only where bounded T4 closure is actually established.
