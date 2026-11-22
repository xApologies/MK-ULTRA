# Atlas v22 — Mode-0 Cycle-Load Geometry

## Status

Derived mathematics / dark-matter source-precursor investigation.

This module does **not** identify dark matter with graph cycles, circulation, ER connectivity, or Transition Capacity. It derives a finite native object that can carry nonzero relational activity while local net continuity redistribution vanishes, and then tests the additional condition required for that activity to become a gravitational precursor.

The active sphere hierarchy remains:

```text
S4 -> S3 -> S2
```

No higher sphere is used.

---

## 1. Parent objects

Let

```text
G_* = (V,E)
```

be the persistent S3 relational support selected by the existing R4-R7 architecture.

Fix one orientation for each edge. This orientation is bookkeeping only; reversing an edge reverses the sign of its signed flow.

For every edge `e`, let

```text
T_e = T_run(e)
```

be the v20/v21 globally realizable runtime Transition Capacity, with

```text
0 <= T_e <= U_e,
```

where `U_e` is the v21 local constitutive capacity envelope.

Let

```text
phi in R^E
```

be a realized signed continuity-flow assignment satisfying

```text
|phi_e| <= T_e
```

and every additional Time-Space feasibility condition defining the runtime feasible-flow family.

---

## 2. Native continuity boundary operator

Define the finite edge-to-vertex boundary operator

```text
partial_1 : R^E -> R^V
```

by

```text
(partial_1 phi)_i
=
SUM_{e entering i} phi_e
-
SUM_{e leaving i} phi_e.
```

This is exactly the graph form of the recovered Phase-III continuity redistribution law

```text
Delta C(i) = inflow - outflow.
```

Hence

```text
Delta C = partial_1 phi.
```

No calculus is used.

---

## 3. Equilibrium cycle sector

Define the runtime circulation/cycle sector

```text
Z_run(G_*)
=
F_run(G_*) intersection ker(partial_1).
```

Thus

```text
phi in Z_run(G_*)
```

iff the flow is globally feasible and

```text
partial_1 phi = 0.
```

This means every vertex has balanced continuity flow even though individual relationships may carry nonzero continuity.

The zero vector is always a trivial member when the feasible set contains it. A nonzero element is a persistent circulation state.

---

## 4. Runtime cycle-capacity invariant

For a finite network define

```text
C_cyc(G_*)
=
sup_{phi in Z_run(G_*)} ||phi||_1
```

with

```text
||phi||_1 = SUM_{e in E} |phi_e|.
```

Because every edge has finite runtime capacity,

```text
C_cyc(G_*) <= SUM_e T_e < infinity.
```

`C_cyc` measures the greatest globally feasible magnitude of continuity that can circulate through persistent support with zero net vertex redistribution.

It is a **continuity-capacity invariant**, not yet physical energy or gravitational mass.

---

## 5. Load-without-redistribution theorem

### Theorem V22-T1

Let `C` be a directed simple cycle whose edges have capacities `T_e > 0`. Let

```text
t_C = min_{e in C} T_e.
```

For every

```text
0 < a <= t_C,
```

define

```text
phi_e = a   for e in C,
phi_e = 0   otherwise.
```

Then, under the capacity constraints alone,

```text
partial_1 phi = 0
```

while

```text
||phi||_1 = a |C| > 0.
```

### Proof

Every vertex on the directed cycle receives one edge carrying `a` and emits one edge carrying `a`, so inflow minus outflow is zero. Vertices outside the cycle receive and emit zero. Yet every edge on the cycle carries nonzero continuity. QED.

### Time-Space corollary

If this cycle flow also satisfies chirality, Bandwidth, ancestry, R5 recoverability, R6 survivability, R7 persistence, and all other runtime conditions, then

```text
phi in Z_run(G_*),
C_cyc(G_*) > 0.
```

Therefore:

```text
Delta C = 0
```

at every vertex does **not** imply

```text
no relational continuity is being carried.
```

---

## 6. Tree falsifier

### Theorem V22-T2

If a connected finite support graph is a tree, then

```text
ker(partial_1) = {0}
```

for ordinary edge flows. Hence

```text
C_cyc(G_*) = 0.
```

### Consequence

If the Mode-0 inter-black-hole support is ultimately proved to be tree-like at the operative Resolution, this entire cycle-load branch is killed at that Resolution.

This is a genuine falsifier.

---

## 7. Local incident-load profile

For a realized circulation `phi`, define the vertex incident-load profile

```text
lambda_i(phi)
=
(1/2) SUM_{e incident on i} |phi_e|.
```

Then

```text
lambda_i(phi) >= 0
```

and

```text
SUM_i lambda_i(phi) = SUM_e |phi_e| = ||phi||_1.
```

The factor `1/2` prevents double-counting each edge at its two endpoints.

Thus a divergence-free cycle can satisfy simultaneously

```text
partial_1 phi = 0
```

and

```text
lambda_i(phi) > 0
```

on every vertex participating in the circulation.

This is the first exact local quantity in the Atlas that distinguishes **balanced redistribution** from **zero relational activity**.

`lambda_i` is not yet a mass density or stress-energy component.

---

## 8. Capacity profile versus realized-load profile

Define the supported capacity profile

```text
s_i
=
(1/2) SUM_{e incident on i} T_e.
```

Because `|phi_e| <= T_e`, every feasible flow obeys

```text
lambda_i(phi) <= s_i.
```

This separates three roles:

```text
U_e     = local constitutive allowance,
T_e     = globally realizable runtime capacity,
|phi_e| = realized continuity use.
```

They must not be conflated.

---

## 9. Resolution-qualified circulation density

If `nu_R(i) > 0` is the already-established Resolution-qualified containment measure for the local address, define

```text
rho_cyc^R(i;phi)
=
lambda_i(phi) / nu_R(i).
```

This is a **continuity-circulation density precursor**.

It has not yet been identified with the recovered native energy density or with a covariant stress-energy tensor. It becomes energy-compatible only after the Relationship valuation and normalization required by the native energy equation are supplied.

---

## 10. Alternative-path theorem and curvature availability

A connected finite graph has a nontrivial cycle iff there exist two distinct simple paths between at least one pair of vertices.

Therefore nonzero cycle topology is exactly what permits same-endpoint path comparison.

Let

```text
P,Q : a -> b
```

be two distinct admissible paths. Define the v20 path runtime capacity

```text
T(P) = min_{e in P} T_e,
T(Q) = min_{e in Q} T_e.
```

The recovered Phase-III gravitational criterion already uses path efficiency `Xi(P)` and states that neighboring path-efficiency inequality is the native curvature precursor.

Do **not** multiply unlike quantities. Instead define the typed support signatures

```text
Sigma(P) = (Xi(P), T(P)),
Sigma(Q) = (Xi(Q), T(Q)).
```

and the two-component support defect

```text
Delta_Sigma(P,Q)
=
(Xi(P)-Xi(Q), T(P)-T(Q)).
```

The first component is the recovered path-efficiency asymmetry channel. The second is a runtime-support anisotropy channel.

A nonzero second component is not by itself curvature. A nonzero first component is the already-recovered native curvature condition. Together they give a richer path-level relational-load diagnostic without inventing a scalar coupling constant.

---

## 11. Holonomy compatibility

The recovered gauge/orientation construction also supplies loop transport

```text
G(L) = product of edge transports around L.
```

with

```text
G(L) = identity   -> flat orientation transport,
G(L) != identity -> nontrivial field-strength / curvature witness.
```

For the loop

```text
L = P * reverse(Q),
```

we may therefore retain three logically separate diagnostics:

```text
1. cycle existence,
2. path-efficiency asymmetry Xi(P) != Xi(Q),
3. nontrivial holonomy G(L) != identity.
```

No theorem in v22 asserts that any two of these are automatically equivalent.

---

## 12. Mode-0 specialization

Genesis's current routing ruling is retained:

```text
Mode 0:
@time_space -> @white_state_core -> @singularity
```

with Mode 0 serving as access to the inter-black-hole dark-network problem.

Let

```text
G_0 subseteq G_*
```

denote the still-to-be-fully-reconstructed Mode-0 S3 network.

Define

```text
Z_0 = Z_run(G_0)
```

and

```text
C_cyc^0 = C_cyc(G_0).
```

These are derived mathematical objects. They are **not** yet dark matter.

The branch survives only if future reconstruction finds

```text
C_cyc^0 > 0
```

and a nontrivial gravitational readout that does not factor through ordinary S2 matter readout.

---

## 13. Current dark-matter boundary

The strongest v22 statement is therefore:

```text
persistent Mode-0 S3 support
-> finite runtime capacities
-> possible nonzero divergence-free circulation sector
-> same-endpoint path alternatives
-> possible Phase-III path-efficiency / holonomy curvature witness
-> Time-Shell/UCM gravitational handoff [still open].
```

This begins filling the old Volume-XII "load-bearing geometry" gap by supplying an explicit **dynamical relational support state**, not merely graph connectivity.

It does **not** yet supply:

```text
T_eff_mn,
metric reconstruction,
continuum limit,
rotation curves,
lensing,
clustering,
or a dark-matter identity theorem.
```
