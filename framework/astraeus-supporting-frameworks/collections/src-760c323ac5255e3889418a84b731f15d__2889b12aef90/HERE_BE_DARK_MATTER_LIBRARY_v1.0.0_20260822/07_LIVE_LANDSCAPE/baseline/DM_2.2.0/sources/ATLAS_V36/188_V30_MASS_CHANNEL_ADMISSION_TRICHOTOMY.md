# V30 — Mass-Channel Admission Trichotomy

## Purpose

Determine exactly when a hidden S3 organizational state may enter the Native Mass channel.

Let `X_H` denote a hidden organizational state or a bounded hidden-network patch.

Use the v3.0 T4 Mass domain `D_M4` and lock selector `P4_lock`.

## Case A — outside the Mass domain

If

```text
X_H not in D_M4,
```

then

```text
Mass_MK([X_H])
```

is not a legal expression in the Native Mass formalism.

The correct status is `UNDEFINED_ON_THIS_DOMAIN`, not zero.

This matters for an extended inter-galactic S3 network: global nonlocality or failure of bounded T4 closure cannot be silently translated into masslessness.

## Case B — admitted but lock-free

If

```text
X_H in D_M4
```

and

```text
P4_lock(X_H) ~ 0_E,
```

then the Masslessness Criterion gives

```text
Mass_MK([X_H]) = 0.
```

## Case C — admitted non-vacuum lock

If

```text
X_H in D_M4
```

and

```text
P4_lock(X_H) not ~ 0_E,
```

then

```text
Mass_MK([X_H]) > 0.
```

## Trichotomy

Therefore every proposed hidden Mass contribution must first answer:

```text
1. Is the state in the T4 Mass domain?
2. If yes, does the T4 lock return vacuum or non-vacuum closure?
```

No statement about dark matter is licensed before those questions are typed.
