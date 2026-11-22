# 84 — Time-Shell Invariant Transport Contract

Transduction Geometry recovered an earlier Time-Shell Translation Contract.

Define the transported invariant set:

```text
I_T = {
  recoverable identity,
  temporal ordering / ordered continuation,
  organizational chirality,
  persistent identity class,
  organizational locality,
  topological organization,
  recursive ancestry
}
```

Let

```text
T_S : RuntimeState -> ShellObs
```

be the shell translation.

The translation is **loss-controlled, not lossless**.

It need not preserve the complete runtime representation. It must preserve recoverability of the declared invariant set.

Thus:

```text
runtime representation may change
while
recoverable organizational ancestry survives.
```

## Identity preservation

If `k1 ~ k2` in the declared Identity relation, then admissible shell translation must preserve recoverable equivalence:

```text
T_S(k1) ~ T_S(k2).
```

## Ordering preservation

The shell preserves ordered continuation:

```text
before -> after
```

without requiring preservation of the source runtime parameterization.

## Atlas compression

```text
Time-Shell translation
=
representation change under declared invariant transport.
```

This is a specialization of the general Transduction Geometry law.
