# 06 — Chirality Localization Action

The recovered historical equation is

```text
T_s = P_c tensor C.
```

The Tome explicitly warns that the operation denoted by the tensor-like symbol is not typed and must not be presumed to be an ordinary tensor product.

Atlas therefore defines a candidate localization action:

```text
Lambda_chi : P_cl x C_adm -> TS_loc
```

and reads the historical expression as

```text
T_s = Lambda_chi(P_c,chi).
```

## Required contracts

A valid localization action must preserve:

### Identity residue

```text
Inv(T_s)=Inv(P_c)
```

for the declared transported invariant set.

### Chirality consistency

The localized orientation/history must be the admissible realization of the input chirality state, not an independently assigned label.

### Boundary support

`T_s` must be supported on / associated with the persistent boundary `dXi` selected by persistence closure.

### Presentation distinction

The localized shell realization may change its readable appearance without changing its Formal Identity when a valid Identity Witness survives.

## Status

**TYPED CANDIDATE ACTION.** This is a formal replacement for assuming the historical `tensor C` symbol is ordinary tensor multiplication.
