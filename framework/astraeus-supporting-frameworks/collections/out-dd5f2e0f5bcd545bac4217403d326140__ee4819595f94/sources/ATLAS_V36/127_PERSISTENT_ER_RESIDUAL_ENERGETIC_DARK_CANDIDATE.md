# 127 — Persistent ER Residual as an Energetic Dark Candidate

## Purpose

The Universal Coupling recovery already contains an energy bookkeeping structure with a retained environmental term.
V16 tests whether that pre-existing term can occupy the dark readout defect identified in v15.

It is **not** declared to be dark matter by definition.

---

## 1. Recovered bookkeeping structure

The Universal Coupling recovery states, in extended local form:

```text
InitialAvailableState
=
FinalLocalState
+
EnvironmentTransfer
+
ResidualFieldState.
```

The same source records that the environment can inherit:

- local chirality polarization;
- adjacency corridor thickening;
- redistribution channels;
- topology memory traces;
- residual strain / field state.

The environmental trace is not permanent by default.

Thus the source itself forces a split between **transient residual** and any residual organization that actually survives persistence/closure.

---

## 2. Typed residual extraction

Let

```text
u in U
```

be a universal-coupling transaction / ledger.

Define the source-grounded residual extractor

```text
Res(u)
:=
ResidualFieldState(u).
```

Let

```text
Persist_R7(Res(u))
```

denote the existing R7 persistence/recoverability test applied to the residual organization.

Define the persistent residual class

```text
Res_P
=
{
 r = Res(u)
 |
 Persist_R7(r)=true
}.
```

Transient residuals are excluded from `Res_P`.

---

## 3. Energetic residual condition

For a persistent residual `r`, use the local native energy-density role rather than the closed-history endpoint difference:

```text
rho_E(r)
=
Rel(r) * Tcap(r) / V(r).
```

A residual is **energetically nontrivial** when

```text
rho_E(r) != 0
```

or, more generally, when its total stress-energy projection differs from the no-residual state.

This avoids the invalid inference

```text
E_MK(H_closed)=0
=>
zero local residual energy.
```

---

## 4. Residual augmentation map

Let

```text
Aug(x,r)
```

denote the full formal state obtained by retaining residual ER/environment organization `r` alongside the local persistent organization `x`.

No linear addition law is assumed.

Define

```text
x_r := Aug(x,r).
```

---

## 5. Sufficient dark-residual criterion

A persistent residual `r` is a **dark energetic candidate at Resolution R** when all of the following hold:

### Persistence

```text
r in Res_P.
```

### Matter-readout nullity

```text
M_R(x_r) = M_R(x).
```

The ordinary matter-readable description does not distinguish the residual organization.

### Stress-energy non-nullity

```text
T_R(x_r) != T_R(x).
```

The total readable stress-energy does distinguish it.

Under the fixed-GR-chart condition from Theorem V16-T1,

```text
G_R(x_r) != G_R(x).
```

Therefore

```text
(x_r,x) in D_R.
```

---

## 6. Theorem V16-T3 — Persistent residual sufficient condition

For one fixed downstream GR chart `beta`, every residual satisfying

```text
Persist_R7(r)
M_R(Aug(x,r)) = M_R(x)
T_R(Aug(x,r)) != T_R(x)
```

generates a v15 dark readout pair.

### Proof

The first condition makes `r` eligible as persistent structure rather than a transient environmental trace.
The second places `x_r` and `x` in one matter-readable fiber.
The third gives different stress-energy readouts.
If `G_R = Gamma_beta o T_R` and the two stress-energy states produce distinct gravity in the declared chart, then the gravity readouts differ, so the pair lies in `D_R`. QED subject to the stated nondegenerate gravity response.

### Important guardrail

`T_R(x_r) != T_R(x)` is necessary for a dark pair in a fixed GR chart, but a stress-energy difference need not always produce a distinguishable metric difference under every observational quotient. The final gravitational nondegeneracy remains a readout test.

---

## 7. Relation to historical dark-matter language

The historical dark-matter recovery describes the candidate sector as persistent, non-luminous, load-bearing ER-connected geometry.

The UCM residual class supplies a source-grounded candidate location for such a load:

```text
persistent local organization
-> perturbs shared ER substrate
-> redistribution / corridor selection
-> residual ER/environment organization
-> persistence test
-> ordinary matter readout may discard it
-> stress-energy / gravity may retain it.
```

This is the first v16 bridge that makes the phrase

```text
native energy wrapped in geometry
```

mathematically testable without declaring energy to be a material substance.

---

## Status

```text
UCM ResidualFieldState bookkeeping term               RECOVERED
Environmental topology-memory / residual behavior     RECOVERED
Residual persistence filter                            V16 TYPING USING EXISTING R7
Residual = dark matter                                 NOT CLAIMED
Persistent matter-null / stress-energy-nonnull test    V16 DERIVED
Particle carrier                                       NOT REQUIRED
```
