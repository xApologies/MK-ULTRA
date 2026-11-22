# 131 — GR Boundary/Topology Factorization Test

## Purpose

Formal 125 proves that a v15 dark gravitational pair must hide at least one readable GR input:

```text
stress-energy T_R
or
boundary / initial / gauge / topology data beta_R.
```

V16 now makes the boundary branch independently testable.

---

## 1. Boundary/topology readout map

At fixed Resolution `R`, let

```text
beta_R : X_R -> GRBoundaryData_R
```

collect the non-stress-energy data required by the declared readable GR problem.

The exact contents of `beta_R` must be declared for each application. It may include:

- boundary conditions;
- initial data;
- global topology / solution branch;
- gauge fixing or coordinate convention where needed for the readout;
- asymptotic / horizon data not already encoded in `T_R`.

`beta_R` is a downstream readable-data object, not a new native substrate primitive.

---

## 2. Boundary factorization theorem

### Theorem V16-T6

There exists a map

```text
beta_bar_R : Im(M_R) -> GRBoundaryData_R
```

such that

```text
beta_R = beta_bar_R o M_R
```

if and only if

```text
M_R(x)=M_R(y)
=>
beta_R(x)=beta_R(y)
```

for every `x,y in X_R`.

### Proof

Identical to the standard fiber-factorization proof used in v15.

If `beta_R = beta_bar_R o M_R`, equality of matter readouts gives equality of `beta_R`.

Conversely, if `beta_R` is constant on every matter fiber, define `beta_bar_R(m)` using any representative `x` with `M_R(x)=m`. Fiber constancy makes the definition well-defined. QED.

---

## 3. Hidden boundary/topology defect

Define

```text
B_R^GR
=
{
 (x,y)
 |
 M_R(x)=M_R(y)
 and
 beta_R(x)!=beta_R(y)
}.
```

Then

```text
B_R^GR != empty
```

if and only if the readable GR boundary/topology data do not factor through ordinary matter readout.

This is mathematically separate from the hidden stress-energy set

```text
E_R^T
=
{
 (x,y)
 |
 M_R(x)=M_R(y)
 and
 T_R(x)!=T_R(y)
}.
```

---

## 4. Dark-input decomposition

From Theorem V16-T1:

```text
D_R subseteq E_R^T union B_R^GR.
```

Thus every dark pair must lie in at least one of two hidden-input defects:

```text
ordinary matter readout lost stress-energy information
```

or

```text
ordinary matter readout lost GR boundary/topology information.
```

The pair may lie in both.

This is an exact set-theoretic decomposition of the current ordinary-GR branch.

---

## 5. Energy-branch decision test

If

```text
B_R^GR = empty,
```

then `beta_R` factors through matter readout and

```text
D_R subseteq E_R^T.
```

Every dark gravitational distinction then requires a hidden stress-energy distinction.

If

```text
B_R^GR != empty,
```

the Atlas must determine whether the observed gravitational multiplicity on each affected matter fiber comes from:

1. `E_R^T` only;
2. `B_R^GR` only;
3. both.

This is the exact mathematical test for the user's current question:

> Is the dark sector primarily hidden energetic load, or is part of the gravitational effect carried by hidden Time-Space boundary/topology data?

---

## 6. Time-Shell / S3 relevance

The current Atlas already allows upstream S3 continuity and Time-Shell boundary organization to contain distinctions absent from a local S2 matter readout.

Therefore v16 does **not** assume

```text
B_R^GR = empty.
```

Instead, it promotes boundary factorization to an explicit next audit.

If Time-Shell / S3 data are fully represented by the total stress-energy projection in the chosen GR chart, the energetic branch should absorb them.

If not, the hidden-boundary branch remains independently operative.

---

## Status

```text
GR boundary/topology input beta_R                    V16 TYPED
Boundary factorization criterion                     PROVED
Hidden boundary defect B_R^GR                        V16 DEFINED
Dark-input decomposition D_R subset E_R^T union B_R  PROVED
B_R^GR empty for actual galaxy readout               OPEN
Native-energy branch uniquely selected               NOT YET
```
