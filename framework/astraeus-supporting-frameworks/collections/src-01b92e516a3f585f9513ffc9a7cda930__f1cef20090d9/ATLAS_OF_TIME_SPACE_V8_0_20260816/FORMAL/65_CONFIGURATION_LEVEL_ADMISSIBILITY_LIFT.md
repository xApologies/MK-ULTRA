# 65 — Configuration-Level Admissibility Lift

The recovered operator `T_A` acts on substrate states. Atlas requires an operator on normalized Unit-String configurations.

Let

```text
U_1 = { c | Adm(c)=1, ell(c)=1 }.
```

A single admissible reconfiguration step between Unit Strings is written

```text
c -> d.
```

Define the configuration-level admissibility kernel

```text
A_U(c,d)
```

as the recovered/derived admissibility assigned to that reconfiguration after enforcing:

- Bandwidth availability;
- chirality/orientation compatibility;
- topology compatibility;
- invariant Unit-String normalization;
- any declared persistence constraints relevant to the sector.

Require the normalized sector law

```text
sum_d A_U(c,d)=1
```

whenever the admissible successor set is nonempty.

Then

```text
(T_U f)(c)=sum_d A_U(c,d) f(d).
```

and

```text
L_U = I - T_U.
```

## Important distinction

`A_U` is not automatically identical to the primitive state-level `A_ij`. It is the **induced admissibility kernel on configuration space**. A complete implementation must derive it from the lower state/path algebra rather than inventing it independently.

## Status

**TYPED LIFT TARGET.**

Its required algebraic form is fixed; its exact derivation from primitive state transitions remains an implementation/recovery task.
