# WL-v219 — Hidden Embedding / Typed-Lift Role Match

**QMO:** QMO-AST-DM-WL-103  
**Work layer:** WL-035  
**Parent promotions:** 0  
**Status:** STRUCTURAL_ROLE_MATCH / NOT_IDENTITY

## API objects

Dark Matter 2.2 defines the constrained embedding family

```text
Emb_H,phys^R = {
  iota_H:E_H^R ↪ E
  |
  pi_E o iota_H = j_T o pi_H,
  I o iota_H = iota_H o I_H,
  iota_H(E_H^R) subseteq ker(C)
}.
```

The family is mathematically defined. Its nonemptiness and physical member selection remain open.

Transduction Geometry v1.0 exposes:

```text
@typed_lift_architecture
```

as a promoted candidate with:

```text
restriction/localization -> cartesian-style lift semantics
forward realization/transduction -> cocartesian-style lift semantics.
```

## Role comparison

The DM square

```text
E_H^R --iota_H--> E
 |               |
pi_H            pi_E
 |               |
 v               v
T_H ----j_T----> T
```

has the structural shape of a typed forward realization over the base map `j_T`, with extra inheritance-equivariance and constraint-kernel requirements.

Therefore the Transduction typed-lift architecture is a **candidate architectural language** for organizing the open hidden-embedding problem.

This does not identify `iota_H` with a Transduction cocartesian lift and does not prove any lift axiom.

## Watcher firewall

Transduction Geometry explicitly warns not to promote its Grothendieck/fibration analogy to a canonical fibration/opfibration until the required universal lift axioms are established. The current source supports typed lift families, not a universal theorem.

## Next handle

```text
@transduction_connection
```

because it is the source-native lift-selection object inside the typed-lift architecture.
