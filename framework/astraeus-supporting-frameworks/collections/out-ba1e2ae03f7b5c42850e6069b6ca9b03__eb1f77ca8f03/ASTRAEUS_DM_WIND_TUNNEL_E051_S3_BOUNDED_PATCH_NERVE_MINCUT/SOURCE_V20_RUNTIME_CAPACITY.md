# 151 — Transition Capacity as an Admissible Continuity-Flow Bound

## Status

```text
DERIVED ATLAS MATHEMATICS / v20
Source objects recovered independently; constitutive definition is new.
No astronomy fit and no particle ontology assumed.
```

## 1. Existing source objects

The Phase III substrate already contains a directed admissibility graph

```text
G = (S,E)
```

with edge `e_ij` present only when the transition is admissible. Continuity flow is represented by

```text
Phi_ij
```

and local redistribution obeys

```text
Delta C(s_i)
=
sum_j Phi_ji - sum_j Phi_ij.
```

A closed region obeys

```text
sum_i Delta C(s_i) = 0.
```

Atlas v19 additionally selects a persistent support `E_*` through:

```text
R4 feasible corridors
-> dual selector (Argmax Xi intersect Argmin Strain)
-> R6 survivability
-> R7 persistence
-> E_*.
```

The native energy-density equation is already recovered as

```text
rho_E = Relationship * TransitionCapacity / ContainmentVolume.
```

The unresolved object is `TransitionCapacity`.

---

## 2. Runtime feasible-flow family

Fix:

- a selected persistent support graph `G_*=(V_*,E_*)`;
- a state/configuration `x`;
- boundary data `beta` for the local transaction;
- Bandwidth state `B`;
- Resolution `R` when a readable restriction is required;
- chirality/history/persistence constraints inherited from the selected support.

Define the **runtime feasible-flow family**

```text
F_run(G_* | x,beta,B,R)
```

to be the set of all directed continuity-flow assignments

```text
Phi : E_* -> R_{>=0}
```

that simultaneously satisfy:

1. edge admissibility;
2. the declared local continuity redistribution equation;
3. conservation on closed persistent interior regions;
4. chirality compatibility;
5. Bandwidth constraints;
6. ancestry/recoverability requirements;
7. R6 survivability;
8. R7 persistence;
9. the fixed boundary data `beta`.

The exact algebraic implementation of individual guards may vary by sector. Their role here is not to multiply a flow amplitude. They define the feasible set on which capacity is measured.

---

## 3. Edge Transition Capacity

For a directed selected relationship

```text
e in E_*,
```

define its feasible scalar flow set

```text
F_e
=
{ Phi(e) | Phi in F_run(G_* | x,beta,B,R) }.
```

The **runtime Transition Capacity** of `e` is

```text
T_run(e)
:=
sup F_e.
```

If `F_e` is empty or contains only zero, set

```text
T_run(e)=0.
```

If the feasible flow family is unbounded, `T_run(e)=+infinity`; such a realization fails the finite-capacity requirement and is not yet physically admissible.

Because `e` is directed, reverse capacity is represented by the distinct reverse relationship when that relationship exists. No unsigned symmetrization is imposed.

---

## 4. Why this is a capacity rather than a new field

`T_run(e)` is not a new substrate substance.

It is a property of the already-existing feasible continuity-flow family:

```text
selected relationship
+
all native admissibility constraints
->
maximum realizable continuity flow on that relationship.
```

Thus the v19 placeholder

```text
J_D : constraints -> deformation load
```

can be reduced to a concrete construction:

```text
constraints
-> feasible-flow set
-> edgewise capacity functional.
```

No additional primitive is required.

---

## 5. Formation capacity versus runtime capacity

The v16/v19 `Tcap^free` object measured remaining reconfiguration freedom. That is a **formation/reconfiguration capacity**.

Define schematically:

```text
T_form
=
capacity associated with still-available topology-changing transitions.
```

The present object is instead:

```text
T_run
=
capacity carried by already-selected persistent relationships.
```

These are different typed roles.

Therefore:

```text
T_form = 0
```

does not imply

```text
T_run = 0.
```

A saturated persistent geometry may possess little or no new reconfiguration freedom while remaining load-bearing and capable of continuity transmission along its committed support.

---

## 6. Theorem V20-T1 — Constraint monotonicity

Let two feasible-flow families satisfy

```text
F_run' subseteq F_run.
```

Then for every selected relationship `e`,

```text
T_run'(e) <= T_run(e).
```

### Proof

By definition,

```text
F_e' subseteq F_e.
```

The supremum of a subset cannot exceed the supremum of the containing set.

Therefore

```text
sup F_e' <= sup F_e.
```

Hence

```text
T_run'(e) <= T_run(e).
```

QED.

### Interpretation

Tightening Bandwidth, chirality, recoverability, persistence, strain-selected support, or boundary constraints can remove feasible flow states but cannot create additional runtime capacity.

---

## 7. Theorem V20-T2 — Forbidden relationship has zero runtime capacity

If a relationship `e` is absent from `E_*`, or every admissible flow assignment requires

```text
Phi(e)=0,
```

then

```text
T_run(e)=0.
```

This follows immediately from the definition.

QED.

---

## 8. Corridor capacity

Let an admissible serial corridor be

```text
P=(e_1,e_2,...,e_n)
```

with conserved through-flow `f` across each edge.

Then

```text
f <= T_run(e_k)
```

for every `k`.

Therefore

```text
f <= min_k T_run(e_k).
```

Define the serial corridor capacity

```text
T_run(P)
:=
min_{e in P} T_run(e).
```

### Theorem V20-T3 — Bottleneck theorem

No conserved through-flow along a serial corridor can exceed its minimum edge capacity.

This is a direct consequence of the edgewise bounds.

QED.

---

## 9. Network capacity between persistent addresses

For two persistent addresses `a,b` in a finite selected support graph, define

```text
Cap_run(a,b)
```

as the maximum conserved admissible flow from `a` to `b` subject to the capacities `T_run(e)`.

Once the selected support satisfies the ordinary finite directed-flow hypotheses, the standard max-flow/min-cut theorem applies:

```text
Cap_run(a,b)
=
min over a-b cuts K
sum_{e in K} T_run(e).
```

This theorem is inherited mathematics applied to the Atlas capacity object. It is not a new physical law.

The result gives a rigorous cartographic quantity for continuity connectivity between localized addresses without inserting a particle, halo profile, or continuum field.

---

## 10. Relation to finite expression capacity

The Phase I/III archive independently contains a finite local expression-capacity split

```text
E_0 = E_int + E_tr,
```

where translational adjacency expression consumes part of the finite restructuring capacity.

`E_tr` and `T_run` are therefore type-compatible candidates for a later aggregate/local bridge:

```text
edgewise runtime capacities
-> local translational expression allocation E_tr.
```

V20 does **not** identify them numerically. A calibration/aggregation law is still required.

---

## 11. Dark-sector relevance

The earliest dark-matter recovery describes a constrained, load-bearing relational geometry. The present construction allows precisely the combination that v19 needed:

```text
low formation/reconfiguration freedom
+
nonzero persistent runtime transmission capacity.
```

This is a structural result only. It does not yet prove that the corresponding capacity is the observed dark-matter source.

---

## 12. Status

```text
Continuity flow Phi_ij                         RECOVERED
Selected persistent support E_*               V19 ESTABLISHED
Formation/free Transition Capacity            V16/V19 CONDITIONAL
Runtime feasible-flow family                  V20 DERIVED
Runtime Transition Capacity T_run(e)           V20 DERIVED
Serial bottleneck capacity                    V20 PROVED
Inter-address max-flow/min-cut capacity        STANDARD THEOREM SPECIALIZATION
Numeric Bandwidth->flow bound                  OPEN
Physical calibration to joules / SI density   OPEN
Dark-matter identification                     OPEN
```
