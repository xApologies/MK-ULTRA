# 07 — Curvature and Same-Endpoint Path Defects

## 1. Pre-differential curvature

For same-endpoint paths `gamma_1,gamma_2:U->V`, define

```text
K_Conn(gamma_1,gamma_2;x)
 = Def(P_gamma1^Conn(x),P_gamma2^Conn(x)).
```

This is the project's native pathwise curvature diagnostic.

## 2. Flatness

A connection is flat on a declared scope when every admissible same-endpoint pair agrees under the declared equivalence:

```text
K_Conn(gamma_1,gamma_2;x)=0.
```

This is not a claim of vanishing differential curvature tensor unless a smooth bundle/interface has separately been established.

## 3. Commutative square

Given

```text
U --f--> V
|        |
g        h
v        v
W --k--> Z
```

the square defect is

```text
K_square(x)=Def(P_(h o f)(x),P_(k o g)(x)).
```

## 4. Base versus lifted curvature

A dependency/readout square can commute while its lifted state transport fails to commute. Therefore define two layers:

```text
K_base
K_state.
```

`K_base=0` does not imply `K_state=0`.

## 5. Hydrogen result

The six elementary Hydrogen Resolution squares have `K_base=0` because feature union commutes. Their lifted `K_Conn` values remain open pending connection-lift instantiation.

## 6. Curvature as path dependence

The conceptual meaning is simple:

```text
same start
same end
same readable destination
but different transported state
=> path dependence.
```

That path dependence is the pre-differential curvature object of this book.
