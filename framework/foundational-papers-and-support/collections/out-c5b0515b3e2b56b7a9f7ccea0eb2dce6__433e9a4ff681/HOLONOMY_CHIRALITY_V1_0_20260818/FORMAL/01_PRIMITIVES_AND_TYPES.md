# 01 — Primitives and Type Discipline

## 1. Dependency domain

Let `D` denote the dependency category or typed dependency graph. Objects `U,V,...` are local organizational/dependency domains. Arrows

```text
f:U->V
```

denote permitted dependency transitions or context changes. An arrow states where a transition may go; it does not by itself state how a state is transported.

## 2. State fibers

Each dependency object has a state fiber

```text
F(U).
```

No global fibration theorem is assumed merely from this notation.

## 3. Chirality structure

Each state carries or induces local chirality/admissibility data. Write a chirality readout schematically as

```text
chi_U : F(U) -> Chi(U).
```

`Chi(U)` is a book-level typed carrier for chirality state at `U`; it need not be a group and need not reduce to binary handedness.

## 4. Admissibility

For `f:U->V`, define

```text
Adm_f subseteq F(U) x F(V).
```

`Adm_f(x,y)` means `y` is an admissible continuation/realization of `x` along `f`.

Recovered core axioms:

```text
A0 Typed Admissibility
A1 Identity Admissibility
A2 Compositional Closure
A3 Gluing-Compatible Admissibility
A4 Transition Cocycle Coherence
```

Universal lift existence, uniqueness, and invertibility are not assumed.

## 5. Formal and operative lifts

Formal lift family:

```text
Lift_f(x) = {y in F(V) | Adm_f(x,y)}.
```

Bandwidth-restricted family:

```text
Lift_f^B(x) subseteq Lift_f(x).
```

The family may be empty, singleton, or multiply populated. Multiple lifts are branching information, not automatically a defect.

## 6. Resolution equivalence

For active Resolution `R`,

```text
y_1 ~_R y_2  iff  Read_R(y_1)=Read_R(y_2).
```

Resolution-quotiented lift family:

```text
Lift_f^R(x)=Lift_f(x)/~_R.
```

## 7. Connection selector

The Transduction Connection is a typed selector

```text
Conn(f,x | R,B,H,E,chi)
```

that may select a horizontal lift

```text
lambda_f,x in Lift_f^B(x).
```

The source does not assert that a selection exists or is unique for every arrow/state.

## 8. Defect comparator

Let

```text
Def(a,b)
```

be the declared same-type comparison used to test equality or admissible equivalence. It may be a typed symbolic defect rather than a number.

## 9. Identity witness

An Identity Witness is recoverable data certifying that two states/realizations belong to the same declared Formal Identity class. Identity Witness transport is distinct from state transport.

## 10. Status vocabulary

This book uses:

- `RECOVERED` — explicit source mathematics.
- `BOOK FORMALIZATION` — typed definition derived to close a source gap without changing source claims.
- `WORK-LAYER` — application-specific construction.
- `BRACED` — source itself marks incomplete/conditional structure.
- `OPEN` — required object not yet instantiated.
