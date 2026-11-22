# 05 — Persistence Closure as Identity-Stable Algebraic Closure

The source equation is preserved:

```text
P_c = Phi( SUM_d R_d B_d O_d )
```

with historical variant

```text
P_c = lim(Chirality Freedom -> Local Minimum).
```

The source does not fully type `Phi`, the multiplication, or the limit. The Atlas supplies a geometry/algebra-native typing without overwriting the source.

## 1. Native organizational input

Instead of making the scalarized product fundamental, define the depth-indexed organizational record

```text
O_D = ((R_0,A_B0,O_0),...,(R_D,A_BD,O_D)).
```

Here `A_Bd` is the available Bandwidth Algebra at depth `d`, and `R_d` supplies the readout/distinguishability quotient.

## 2. Algebraic persistence closure

For a state/configuration `x`, let `Succ_B(x)` be the currently available Bandwidth-admissible successors.

A class `C` is Identity-stable when

```text
x in C and y in Succ_B(x)
=>
y ~_Id x
```

for every successor that remains in the declared closed regime.

Define

```text
Cl_P(x)
```

as the least declared witness-closed Identity-stable class containing `x`, when it exists.

This is the native persistence closure.

## 3. Closure condition

A closure-stable state/class satisfies

```text
Succ_B(Cl_P(x)) subseteq [Cl_P(x)]_Id.
```

In words:

> the transformations still available to the stabilized organization no longer force it out of its declared Identity class.

This gives the historical phrase `Chirality Freedom -> Local Minimum` a non-calculus reading: chirality-changing freedom has become locally constrained by the admissible Identity-preserving closure.

## 4. Persistent locus

The Atlas persistent locus is

```text
Xi = { x | Cl_P(x) exists and admits a valid persistent witness chain }.
```

Its persistent boundary is

```text
dXi = boundary(Xi).
```

## Status

`Cl_P` is a new Atlas typing of the source `Phi/P_c` role. It is **not** claimed as the recovered exact historical operator.
