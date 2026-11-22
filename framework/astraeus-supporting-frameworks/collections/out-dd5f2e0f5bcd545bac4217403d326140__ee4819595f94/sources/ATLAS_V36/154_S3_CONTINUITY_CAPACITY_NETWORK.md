# 154 — S3 Continuity-Capacity Network

## Status

```text
CARTOGRAPHIC DERIVATION / v20
No new dimension introduced.
Master geometry remains the established S4 closure -> S3 continuity -> S2 localized projection architecture.
```

## 1. Continuity carrier

Let the selected persistent relational support used to model the `S3` continuity layer be represented by a finite directed graph approximation

```text
G_3^*=(V_3,E_3^*).
```

Each selected relationship `e in E_3^*` is assigned the v20 runtime Transition Capacity

```text
T_run(e).
```

The pair

```text
C_3=(G_3^*,T_run)
```

is the **S3 continuity-capacity network**.

This is not a new physical field. It is the established S3 relational support equipped with the derived capacity functional.

---

## 2. Persistent-address capacity

For persistent addresses `a,b in V_3`, define

```text
Cap_3(a,b)
:=
maximum admissible conserved flow from a to b
```

subject to

```text
0 <= Phi(e) <= T_run(e).
```

Under ordinary finite network-flow hypotheses,

```text
Cap_3(a,b)
=
min over cuts K(a,b)
sum_{e in K} T_run(e).
```

Thus the continuity relationship between two localized addresses has a precise, computable network invariant: its maximum admissible flow / minimum separating cut capacity.

---

## 3. Why this matters for the dark-sector search

The historic dark-matter branch repeatedly described a global nonluminous network linking load-bearing relational geometry.

V20 does not identify `Cap_3` with dark matter.

Instead it gives the Atlas a rigorous test object:

```text
full S3 continuity capacity
versus
capacity retained by ordinary S2 matter/readout.
```

If every gravitationally relevant S3 capacity is faithfully represented in ordinary S2 matter readout, this route cannot explain a dark gravitational residual.

If ordinary readout identifies/erases capacity distinctions that the gravitational projection preserves, the capacity network becomes a mathematically qualified dark-sector candidate.

No assertion is made until that factorization test is performed.

---

## 4. Resolution-capacity test

Let

```text
rho_R : C_3 -> C_3^R
```

be a declared Resolution/readout map.

Call `rho_R` **capacity-faithful** on addresses `a,b` when

```text
Cap_3(a,b)
=
Cap_3^R(rho_R(a),rho_R(b)).
```

Call it **capacity-losing** when

```text
Cap_3^R(rho_R(a),rho_R(b))
<
Cap_3(a,b).
```

The difference

```text
DeltaCap_R(a,b)
:=
Cap_3(a,b)
-
Cap_3^R(rho_R(a),rho_R(b))
```

is defined only for readout realizations known not to create capacity.

`DeltaCap_R` is a Resolution-capacity defect. It is not yet dark matter.

---

## 5. Gravitational qualification

A capacity defect enters the dark-sector candidate class only if the Time-Shell/UCM gravitational readout distinguishes states that ordinary matter readout identifies.

Therefore the v15 factorization criterion remains mandatory:

```text
M_R(x)=M_R(y)
and
G_R(x)!=G_R(y).
```

V20 adds a stronger diagnostic question:

```text
Does the gravitational distinction track a nonzero S3 capacity defect?
```

If not, the transition-capacity branch is rejected as the explanation of that dark readout.

---

## 6. Next computational target

Construct finite selected `S3` support graphs from the existing ER/corridor architecture, assign only source- or theorem-supported capacity bounds, and compute:

```text
edge capacities
serial bottlenecks
parallel max flow
minimum cuts
Resolution-induced capacity loss.
```

Do not fit rotation curves until a unique or tightly constrained gravitational projection has been derived.
