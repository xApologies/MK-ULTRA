# 122 — Dark Matter as a Readout-Factorization Defect

## Purpose

Give the recovered phrase

```text
dark matter = unreadable topology
```

a precise cartographic meaning without introducing a particle, a new field, or an arbitrary halo density.

The central object is a mismatch between **matter-readable equivalence** and **gravitational equivalence**.

---

## 1. Matter and gravity readouts

At fixed declared Resolution `R`, write

```text
M_R := Read_(R,M) : X -> M_Range
G_R := Read_(R,G) : X -> G_Range.
```

For the current Atlas branch, `X` is the admissible full continuity organization feeding both readouts.

---

## 2. Factorization theorem

### Theorem V15-T1 — Readout Factorization Criterion

There exists a map

```text
Gbar_R : Im(M_R) -> G_Range
```

such that

```text
G_R = Gbar_R o M_R
```

if and only if

```text
M_R(x) = M_R(y)
=>
G_R(x) = G_R(y)
```

for every admissible `x,y in X`.

### Proof

If `G_R = Gbar_R o M_R`, equality of `M_R(x)` and `M_R(y)` immediately gives equality of `G_R(x)` and `G_R(y)`.

Conversely, if `G_R` is constant on every fiber of `M_R`, define `Gbar_R(m)` to be `G_R(x)` for any `x` satisfying `M_R(x)=m`. Fiber constancy makes this definition independent of representative. QED.

---

## 3. Dark readout defect

Define

```text
D_R
=
{
  (x,y) in X x X
  |
  M_R(x)=M_R(y)
  and
  G_R(x)!=G_R(y)
}.
```

Then

```text
D_R != empty
```

if and only if gravitational readout does **not** factor through ordinary matter readout.

Equivalent relation form:

```text
~_(R,M) is not contained in ~_(R,G).
```

This is the precise v15 meaning of a gravitationally active structure that is hidden by the ordinary matter-readable channel.

---

## 4. Matter fiber and gravitational multiplicity

For `x in X`, define the matter-readable fiber

```text
F_M,R(x)
:=
M_R^-1(M_R(x)).
```

Now examine its gravity image:

```text
Gamma_G,R(x)
:=
G_R(F_M,R(x)).
```

If

```text
|Gamma_G,R(x)| = 1,
```

then the matter readout is sufficient to determine gravity on that fiber.

If

```text
|Gamma_G,R(x)| > 1,
```

then matter readout has conflated formal organizations that gravity still distinguishes.

That non-singleton gravitational image is the **dark readout multiplicity**.

---

## 5. Relation to the v14 full-minus-reference residual

V14 compared

```text
N_full
```

with an observer-side

```text
N_ref.
```

V15 identifies the exact mathematical issue: matter readout alone generally determines a **fiber**, not a unique formal reference representative.

A selected `N_ref` is therefore a section/representative choice inside

```text
F_M,R(N_full).
```

The pairwise v14 metric residual

```text
Delta g_D(N_full,N_ref)
=
g(N_full)-g(N_ref)
```

remains valid once a reference representative is declared.

But the **existence** of a dark sector is stronger and reference-independent:

```text
D_R != empty.
```

### Important consequence

No unique quantitative dark profile can be derived from matter readout alone unless an additional source-grounded rule selects a canonical reference section.

This explains rather than hides the v14 Watcher partial on `N_ref`.

---

## 6. Black-hole / ER / S3 specialization

Let `X_H^R` be the closure-stable translated ER/S3 neighborhood associated with a marked black-hole continuity address.

Then the dark-matter cartography problem becomes:

```text
Does M_R collapse distinctions in X_H^R
that G_R preserves?
```

If yes, the black-hole-connected continuity neighborhood contains gravitationally readable structure that is absent from the ordinary matter-readable representation.

This does not imply

```text
black hole = dark matter
S3 = dark matter
corridor = dark matter.
```

It identifies a relation among their readouts.

---

## 7. Main v15 statement

> **Darkness is a channel-relative failure of factorization: the ordinary matter-readable projection is not sufficient to reconstruct the gravitational projection of the same formal Time-Space organization.**

This is a mathematical readout statement. The physical identity of the hidden formal organization remains the recovered persistent ER-connected/load-bearing geometry until a more specific identification is derived.

---

## Status

```text
Readout Factorization Criterion              PROVED
Dark readout defect D_R                      V15 DEFINED
Un-readable topology interpretation          V15 FORMALIZED
Unique reference representative              NOT IMPLIED
Particle ontology                            NOT REQUIRED
Quantitative astronomical profile            NOT YET DERIVED
```
