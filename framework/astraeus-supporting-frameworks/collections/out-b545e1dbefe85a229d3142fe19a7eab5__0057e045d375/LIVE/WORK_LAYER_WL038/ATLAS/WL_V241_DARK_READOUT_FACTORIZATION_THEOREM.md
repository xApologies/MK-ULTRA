# WL-v241 — Dark Readout Factorization Theorem

**QMO:** QMO-AST-DM-WL-125  
**Work layer:** WL-038  
**Parent promotions:** 0  
**Status:** PROVED WORK-LAYER MATHEMATICS

## Setup

Let `X` be any declared common admissible state domain on which both readouts are defined:

```text
M_R : X -> Y_M
G_R : X -> Y_G.
```

`M_R` is ordinary matter/readout information and `G_R` is gravitational readout.

Dark Matter API 2.2 already defines

```text
D_R
=
{(x,y) in X x X : M_R(x)=M_R(y), G_R(x)!=G_R(y)}.
```

## Theorem

The following are equivalent:

1. `D_R` is empty.
2. `G_R` is constant on every fiber of `M_R`.
3. There exists a unique map on the image of `M_R`,

```text
Gbar_R : im(M_R) -> Y_G,
```

such that

```text
G_R = Gbar_R o M_R.
```

### Proof

If `D_R` is empty and `M_R(x)=M_R(y)`, then by definition `G_R(x)=G_R(y)`. Therefore define

```text
Gbar_R(m)=G_R(x)
```

for any `x` with `M_R(x)=m`. Fiber constancy makes this independent of representative, hence well-defined. The factorization follows immediately and uniqueness on `im(M_R)` is forced.

Conversely, if `G_R=Gbar_R o M_R`, then equal matter readouts imply equal gravitational readouts, so no pair can belong to `D_R`.

QED.

## Fiber form

For one matter-readout value `m`, define the matter fiber

```text
Fib_M^R(m)=M_R^(-1)(m).
```

Define its gravitational image

```text
DarkFib_R(m)
=
{ G_R(x) : x in Fib_M^R(m) }.
```

Then

```text
D_R != empty
```

if and only if there exists `m` such that

```text
|DarkFib_R(m)| > 1.
```

## Geometry-first interpretation

A matter/readout quotient may collapse several formal states into one readable class while the gravitational quotient splits that class into multiple classes.

Therefore the exact mathematical content of the current working reduction is:

```text
DARKNESS = failure of gravitational readout to factor through ordinary matter readout.
```

This is not a physical dark-matter witness. It is an exact reformulation of the API-native readout defect.

## Relation to Resolution

This theorem is compatible with the mounted Resolution Landscape result that a non-injective observational map can place multiple Formal Identity classes inside one Observational Identity class. The new condition asks whether gravity distinguishes at least two members of such a matter/readout class.
