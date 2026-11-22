# 08 — Chirality Transport and Chirality Holonomy

## 1. Chirality state

Recovered source D50 names Chirality State. This book types it as an element

```text
c_x in Chi(U)
```

associated with state `x in F(U)`.

## 2. Chirality transport

Source D51 is BRACED. Book formalization defines a chirality transport induced by a selected state lift whenever the local chirality readout is defined:

```text
T_chi(f;x): c_x -> c_y,
```

where `y=lambda_f,x(x)` and the transported chirality must be the admissible inherited realization, not an independently assigned label.

This definition does not assert that every chirality state has a standalone autonomous transport law.

## 3. Chirality holonomy

For a closed path `gamma:U->U`, define

```text
Hol_chi(gamma;x)
```

as the equivalence class of the returned chirality transformation induced by the selected loop transport.

## 4. Chirality holonomy defect

Define

```text
Def_chi(gamma;x)
 = Def_chi(Hol_chi(gamma;x), id_chi).
```

Nonzero defect means the chirality organization did not return to its initial equivalence class even if the readable base point closed.

## 5. Readable closure with chirality nonclosure

Recovered Lemma L27 states that readable closure can coexist with chirality nonclosure. This is one of the central mechanisms by which a loop can be hidden by projection.

## 6. Chirality-insensitive versus sensitive identities

Recovered L25-L26 separate two cases:

- Identity may be insensitive to a given chirality holonomy and remain unchanged.
- A chirality-sensitive Identity may transform nontrivially under relevant chirality holonomy.

This sensitivity must be declared; it cannot be inferred from chirality nontriviality alone.
