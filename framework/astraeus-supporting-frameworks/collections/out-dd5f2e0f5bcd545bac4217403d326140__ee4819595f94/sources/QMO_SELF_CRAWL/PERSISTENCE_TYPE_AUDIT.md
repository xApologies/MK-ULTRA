# QMO Crawl 001 — Persistence Type Audit

## Input objects

- QMO-DM-001: hidden S3 network support.
- QMO-TS-005: Persistent Recursive Topology -> Persistent Boundary.
- QMO-DM-002: open hidden-boundary realization gate.
- QMO-DM-003: composition of the above.

## Candidate initially generated

```text
j_R7 : E_H^* -> Xi
```

## Crawl result

REJECT AS TOO STRONG / ILL-TYPED.

### Reason 1 — domain type

The dark selector defines:

```text
E_H^*
=
Persist_R7(E_H^surv)
```

as persistent corridor **support**.

The formal Persistent Locus is:

```text
Xi
=
{
  xi in E
  |
  exists n >= 1 such that I^n(xi) ~ xi
}.
```

Thus Xi contains inherited organizational states, not bare edge sets.

A state-encoding map is required first.

### Reason 2 — API 4.3 persistence audit

API 4.3 explicitly records:

```text
persistence contribution
-> persistence potential
-> candidate Persistent Recursive Topology
-> chirality and admissibility closure
-> formal Persistent Locus
```

and states that persistence potential is **not silently identified** with the formal locus.

Therefore `R7 persistence` cannot be promoted directly to `Xi` by terminology.

## Replacement candidate

```text
iota_HE^R : X_H^R ⇀ E
```

followed by the exact formal test:

```text
P_Xi(x)
=
[
  exists n >= 1 such that
  I^n(iota_HE^R(x))
  ~
  iota_HE^R(x)
].
```

Only after this condition is satisfied may the hidden state be placed in Xi.

## Optional intermediate

API 4.3 suggests a less aggressive intermediate target:

```text
j_HPRT^R :
X_H^R
⇀
PersistentRecursiveTopology.
```

That stage still requires chirality/admissibility closure before the formal locus.

## Effect on v36

The former monolithic target

```text
R_HdXi^R
subseteq
X_H^R x dXi
```

should be decomposed into:

```text
hidden state encoding
-> formal persistence qualification
-> locus membership
-> local boundary incidence / realization.
```

The global existence of dXi is supplied by the Boundary Formation Axiom once Xi is present, but that axiom does not make every xi in Xi a boundary point.

## Status

QMO-DM-CAND-001: SUPERSEDED.

QMO-DM-CAND-002: OPEN, TYPE-CORRECT, NOT PROMOTED.
