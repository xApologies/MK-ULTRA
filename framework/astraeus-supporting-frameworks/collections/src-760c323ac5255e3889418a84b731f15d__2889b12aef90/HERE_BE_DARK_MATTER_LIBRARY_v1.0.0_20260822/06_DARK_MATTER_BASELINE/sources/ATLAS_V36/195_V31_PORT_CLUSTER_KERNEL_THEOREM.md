# 195 — V31 Port-Cluster Kernel and Multi-Port Response Theorem

## Status

```text
DERIVED FROM FINITE POSITIVE GRAPH GEOMETRY
```

## 1. Hidden-port connectivity relation

For the hidden graph `G_H`, define an equivalence relation on readable ports:

```text
p ~_H q
iff
p and q lie in the same connected component of G_H.
```

Components containing no readable port are irrelevant to the port response and are removed before Schur reduction.

## 2. V31-T2 — Kernel characterization

For positive hidden edge weights,

```text
ker(Lambda_H)
=
{
 c_P : c_p = c_q whenever p ~_H q
}.
```

### Proof

The reduced quadratic form is the minimum of

```text
E_H(c)
=
(1/2) sum_e w_e(c_u-c_v)^2.
```

It vanishes exactly when every edge difference in every relevant hidden component vanishes.

Because each component is connected, that happens exactly when the potential is constant throughout the component, including all ports attached to it.

QED.

## 3. One-port corollary

If every hidden connected component touches at most one readable port, then no hidden component can compare two port values.

Therefore

```text
Lambda_H = 0.
```

This reproduces the earlier one-port no-go.

## 4. Multi-port corollary

If some hidden connected component touches at least two readable ports, then

```text
Lambda_H != 0.
```

There exists a port contrast `c_P` for which

```text
c_P^T Lambda_H c_P > 0.
```

For a hidden component connecting all relevant ports,

```text
ker(Lambda_H)=span{1}.
```

Thus the hidden network is blind to a uniform offset but responds to relative port distinctions.

## 5. Two-port series example

For

```text
p --(a)-- h --(b)-- q,
```

Schur elimination gives

```text
w_eff = ab/(a+b)
```

and

```text
Lambda_H
=
w_eff [ 1 -1 ]
      [ -1 1 ].
```

No cycle is required.

## 6. Quadratic response functional

Define only the mathematical response form

```text
Q_H(c_P)
:=
(1/2)c_P^T DeltaLambda_H c_P.
```

Then

```text
Q_H(c_P) >= 0.
```

Under the clean port-glued model, `DeltaLambda_H=Lambda_H`.

`Q_H` is **not physical energy** and is not dark matter. It measures how much the hidden positive network changes the finite continuity response to a declared port contrast.

## 7. Relation to v29 equilibrium load

The two V31/V29 witnesses are different:

```text
Delta rho_H > 0
```

can survive at a uniform equilibrium because it measures supported relational capacity/load.

But

```text
Q_H(c0*1)=0
```

because a Laplacian responds only to differences.

Therefore:

```text
persistent supported load
!=
linear response to a port contrast.
```

This distinction is retained permanently.
