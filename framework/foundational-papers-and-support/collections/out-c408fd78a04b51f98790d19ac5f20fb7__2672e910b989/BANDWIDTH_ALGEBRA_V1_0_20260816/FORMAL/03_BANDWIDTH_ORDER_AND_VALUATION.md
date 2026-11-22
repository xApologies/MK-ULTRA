# 3. Bandwidth Order and Optional Scalar Valuation

The native object is `A_B`, not a scalar.

## BA-D10 — Capacity order

```text
B1 <= B2
```

means every transformation available under `B1` is available under `B2` after typing/provenance is respected.

Equivalently, there is a Bandwidth-preserving inclusion:

```text
A_B1 -> A_B2.
```

## BA-D11 — Scalar Bandwidth valuation

When a scalar summary is needed, introduce a valuation:

```text
beta : BandwidthSubobjects -> R_nonnegative
```

subject to at minimum:

1. `beta(0_B) = 0`;
2. monotonicity under pure inclusion;
3. invariance under structural renaming/isomorphism;
4. explicit declaration of what the valuation measures.

Possible finite-scope valuation:

```text
beta_R(B,x) = log(1 + | rho_R(Free_B(x)) | ).
```

This is a candidate readout, not the definition of Bandwidth.

## BA-D12 — Historical scalar `B_d`

In equations such as:

```text
G = G * SUM_d (R_d * B_d)
```

interpret `B_d` as a scalarized/readable Bandwidth quantity:

```text
B_d := beta_d(A_B,d)
```

unless a source explicitly declares a different type.

This preserves the historical Genesis equation while preventing the scalar from replacing the richer Bandwidth Algebra.
