# 199 — Hidden Boundary-Response Form

## Status

```text
NEW_DERIVED_MATH
finite positive-network theorem
not a spacetime metric
not a stress-energy tensor
not dark matter
```

## 1. Input from v31

Let `P` be the readable S2 port set and let the port-relevant hidden S3 network have reduced operator

```text
Lambda_H = Lambda_H^T >=_PSD 0.
```

V31 proved

```text
ker Lambda_H
=
{c_P : c_p=c_q whenever p and q lie in the same hidden port-connectivity component}.
```

Write

```text
V_P = R^P
K_H = ker Lambda_H.
```

## 2. Quotient state space

Define the relative port-state quotient

```text
Vbar_H = V_P / K_H.
```

If the hidden network connects all relevant ports, then

```text
Vbar_H = R^P / span{1}.
```

Thus the hidden network naturally acts on relative S2-port distinctions rather than a uniform offset.

## 3. Boundary-response bilinear form

For equivalence classes `[x],[y] in Vbar_H`, define

```text
B_H([x],[y]) = x^T Lambda_H y.
```

### Proposition 199.1 — well-definedness

`B_H` is independent of the representatives.

Proof. If

```text
x' = x + k,
y' = y + l,
```

with `k,l in K_H`, then

```text
x'^T Lambda_H y'
=
x^T Lambda_H y
 + k^T Lambda_H y
 + x^T Lambda_H l
 + k^T Lambda_H l.
```

Since `Lambda_H k = Lambda_H l = 0` and `Lambda_H` is symmetric, all added terms vanish. Therefore

```text
B_H([x'],[y']) = B_H([x],[y]).
```

QED.

### Proposition 199.2 — positive definiteness on the quotient

Because `Lambda_H >=_PSD 0`,

```text
B_H([x],[x]) >= 0.
```

For a positive-semidefinite symmetric matrix,

```text
x^T Lambda_H x = 0
iff
x in ker Lambda_H.
```

Therefore

```text
B_H([x],[x]) = 0
iff
[x] = [0] in Vbar_H.
```

Hence `B_H` is positive definite on the quotient.

## 4. Quadratic response functional

Define

```text
Q_H([x]) = (1/2) x^T Lambda_H x.
```

Then the finite polarization identity gives

```text
B_H([x],[y])
=
Q_H([x+y]) - Q_H([x]) - Q_H([y]).
```

No native calculus is required.

## 5. Direct continuity-response pairing

The v27/v31 hidden direct response is

```text
deltaC_H(c_P) = -Lambda_H c_P.
```

For any port test state `eta`,

```text
eta^T deltaC_H(c_P)
=
-B_H([eta],[c_P]).
```

Thus the same object `Lambda_H` simultaneously determines:

```text
1. hidden-port response geometry;
2. the v27 direct continuity residual;
3. a symmetric finite response form on relative S2-port states.
```

## 6. Interpretation boundary

The exact mathematical type is

```text
B_H in Sym^2(Vbar_H^*).
```

This is **not** yet

```text
T_mn in Sym^2(T^*M)
```

and it is **not** a readable spacetime metric.

The result supplies a native finite response object that a later transduction may consume. It does not supply that transduction by itself.

## 7. Falsifiers

The response form vanishes when the hidden component is one-port only or when the tested state lies entirely in the hidden-component kernel.

Therefore the response-form branch remains falsifiable at the topology/state level.
