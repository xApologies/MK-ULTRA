# Chirality Set Lift

## Purpose

The chirality set lift embeds canonical module objects into a request-relative BRANE realization without mutating their source state.

## Base set

Let `A` be a set of canonical objects:

```text
A = {a₁,a₂,...,aₙ}
```

Let the chirality assignment be:

```text
χ : A → Χ
```

The five-dimensional canonical representation is:

```text
κ(a) = (I(a),D(a),Χ(a),R(a),P(a))
```

## Lift

For request `q`, define the BRANE lift:

```text
Lχ,q : A → B⁶
```

by:

```text
Lχ,q(a) = (I(a),D_q(a),Χ_q(a),R_q(a),P(a),Z_q(a))
```

The lifted set is:

```text
Lχ,q[A] = { Lχ,q(a) | a ∈ A }
```

## Non-mutation law

For canonical state `C(a)` and lifted realization `Lχ,q(a)`:

```text
C(a) remains invariant under Lχ,q
```

Equivalently:

```text
Lχ,q is representation-generating, not source-mutating.
```

## Admissibility

A lift is admissible only if:

```text
Admit(a,q) = true
```

Possible admissibility conditions include:

- edge-type compatibility
- chirality compatibility
- provenance validity
- recursive-depth bound
- request-domain membership
- cycle-safety

## Rewrite-as-derived

A rewrite is defined as:

```text
R_q(a) = transform(Lχ,q(a))
```

with:

```text
R_q(a) ≠ overwrite(C(a))
```

Derived rewrites may populate QMO⁶ or report state. They do not alter canonical module storage.
