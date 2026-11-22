# 2. Readout Architecture

The readout process is separated into two operations:

1. **Resolution quotient** — remove distinctions not available at `R`.
2. **Representation realization** — render the quotient into the target readable geometry/physics.

Write schematically:

```text
Read_R = Realize_R o q_R.
```

where

```text
q_R       : Formal -> Formal_R
Realize_R : Formal_R -> Readable_R.
```

This separation prevents a common category error: a projection/readout is not automatically the same object as the formal structure being read.

## Readout noncreation rule

If `x` and `y` are not formally distinct, readout cannot make them formally distinct. A readout may display different coordinates/presentations only if another declared degree of freedom enters the representation map.

## Readout conflation

If

```text
x != y
```

formally but

```text
x ~_R y,
```

then readout conflates the two at Resolution `R`.

At finer Resolution `R'`, they may separate:

```text
q_R(x) = q_R(y)
but
q_R'(x) != q_R'(y).
```

This is observational splitting without formal creation.
