# 152 — Relational Network Realization of Native Energy Density

## Status

```text
DERIVED HETEROGENEOUS REALIZATION / v20
Reduces to the recovered scalar equation rho_E = R T / V.
```

## 1. Recovered scalar law

The native energy-density equation is

```text
rho_E = R T / V
```

with:

```text
R = Relationship
T = Transition Capacity
V = Containment Volume.
```

V20 now possesses an edgewise runtime Transition Capacity `T_run(e)` on selected persistent support.

---

## 2. Relationship valuation

For every selected directed relationship `e`, let

```text
r(e) >= 0
```

be its declared native Relationship valuation.

In an ER-network specialization, the recovered weighted adjacency `W_ij` is a natural candidate realization of `r(e_ij)`, but V20 does not force the identification until normalization/units are fixed.

---

## 3. Native relational-capacity load

For a finite contained selected-support region `U`, define

```text
L_E(U)
:=
sum_{e in E_*(U)} r(e) T_run(e).
```

This is a derived aggregate of existing relationship and Transition-Capacity terms.

Define the heterogeneous native energy density by

```text
rho_E(U)
:=
L_E(U) / V(U)
```

or equivalently

```text
rho_E(U)
=
[sum_e r(e) T_run(e)] / V(U).
```

No continuum integral is required at the native layer.

---

## 4. Theorem V20-T4 — Scalar-law reduction

Suppose every selected relationship in `U` carries the same runtime capacity `T`, and define the aggregate Relationship quantity

```text
R(U)
:=
sum_{e in E_*(U)} r(e).
```

Then

```text
rho_E(U)
=
R(U) T / V(U).
```

### Proof

By definition,

```text
rho_E(U)
=
[sum_e r(e)T] / V(U)
=
T [sum_e r(e)] / V(U)
=
R(U)T/V(U).
```

QED.

Thus the heterogeneous network realization reduces exactly to the recovered scalar equation in the uniform-capacity case.

---

## 5. Realized utilization is not Transition Capacity

For an actual admissible flow `Phi`, define, when `T_run(e)>0`,

```text
u_Phi(e)
:=
Phi(e)/T_run(e),
```

so

```text
0 <= u_Phi(e) <= 1.
```

The realized flow load is then

```text
L_Phi(U)
=
sum_e r(e) T_run(e) u_Phi(e)
=
sum_e r(e) Phi(e).
```

This separates:

```text
capacity  = what the persistent relationship can support
utilization = how much of that capacity is expressed in one state/transaction.
```

The recovered API equation uses `Transition Capacity`, not utilization, so `u_Phi` remains a diagnostic rather than a replacement of the canonical term.

---

## 6. Closed-history compatibility

The native general-energy functional satisfies

```text
E_MK(H_closed)=0.
```

That is a signed endpoint/history statement.

The relational-capacity density depends on supported relationship capacities and need not vanish merely because a complete history closes:

```text
E_MK(H_closed)=0
```

does not imply

```text
T_run(e)=0
```

for every edge, and therefore does not imply

```text
rho_E(U)=0.
```

This resolves the earlier apparent conflict between zero net energy change around a closed history and nonzero local load-bearing relational organization.

---

## 7. No automatic additivity across overlapping support

The sum above applies to a declared edge decomposition of a finite contained region. If two descriptions count the same physical relationship twice, they must first be quotient/reconciled.

V20 therefore does not assert that arbitrary overlapping subregions satisfy naive independent additivity.

---

## 8. GR/UCM handoff

Once calibrated and passed through the UCM source projection, `rho_E(U)` may contribute to the readable stress-energy ledger.

The current typed route is:

```text
selected persistent relationships
-> runtime Transition Capacity
-> native relational-capacity density
-> UCM full source
-> Time-Shell gravitational projection
-> readable geometry.
```

No claim is made yet that the entire dark sector equals this density.

---

## 9. Status

```text
rho_E = RT/V                            RECOVERED
relationship weight r(e)                TYPED; NUMERIC REALIZATION OPEN
T_run(e)                                V20 DERIVED
heterogeneous sum realization           V20 DERIVED
uniform reduction to RT/V               V20 PROVED
utilization variable u_Phi              V20 DERIVED DIAGNOSTIC
SI calibration                          OPEN
dark-matter quantitative profile        OPEN
```
