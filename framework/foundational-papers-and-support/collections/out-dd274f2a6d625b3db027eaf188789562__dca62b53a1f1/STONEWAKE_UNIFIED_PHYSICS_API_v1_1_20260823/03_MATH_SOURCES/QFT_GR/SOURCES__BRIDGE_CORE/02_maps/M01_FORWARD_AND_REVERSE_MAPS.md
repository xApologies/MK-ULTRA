# M01 — Forward and Reverse Maps

## Atomic projection

```text
A_A
:
Q_A -> X_A.
```

## Atomic reverse recovery

Because the Atomic Profile does not retain every gauge, phase, and
representation coordinate, its inverse is a quotient recovery:

```text
R_A
:
X_A -> Q_A / ~_A.
```

Thus:

```text
R_A o A_A
=
identity
```

on the declared atomic admissible-equivalence class.

## Environmental composition

```text
U_ENV^(N)
:
X_A1 x ... x X_AN
->
X_M.
```

## Molecular reverse recovery

```text
R_M
:
X_M
->
Q_M / ~_M.
```

## Admiral's Bridge

```text
B_Adm^(N)
=
R_M
o
U_ENV^(N)
o
(A_A1 x ... x A_AN).
```
