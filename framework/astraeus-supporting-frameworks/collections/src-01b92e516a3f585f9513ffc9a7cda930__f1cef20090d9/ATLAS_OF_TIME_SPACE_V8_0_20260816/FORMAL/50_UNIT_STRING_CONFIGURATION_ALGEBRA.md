# 50 — Unit String Configuration Algebra

## Native Unit String

A Unit String configuration is an admissible path/configuration `c` in the S3 continuity domain with intrinsic valuation

```text
ell(c) = 1.
```

The value `1` is the invariant normalization. It does not specify a straight shape.

Define

```text
U_1 = { c | Adm(c)=1 and ell(c)=1 }.
```

## Bandwidth action

Let `A_B` be the Bandwidth Algebra. A generator `g in Gen(B)` may act on a Unit String configuration when the transformation is typed and admissible:

```text
g : c_i -> c_j.
```

The action must preserve the Unit String invariant when declared as a configuration-preserving transformation:

```text
ell(c_j)=ell(c_i)=1.
```

The S3 continuity structure, chirality constraints, Helicon organization, boundary conditions and Bandwidth determine which configurations are available. The configuration is not arbitrarily chosen by an observer.

## Lift to Time-Space

Each stage of a path carries an address plus a local direction class:

```text
c_hat = ((p_0,d_0),...,(p_n,d_n)).
```

The smooth readout of this construction is the tangent lift into `UT(S3)`.
