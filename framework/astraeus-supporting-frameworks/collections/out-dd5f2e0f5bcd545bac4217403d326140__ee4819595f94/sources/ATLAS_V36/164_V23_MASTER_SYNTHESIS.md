# 164 — Atlas v23 Master Synthesis

## Active geometry

```text
S4 -> S3 -> S2
```

## Question inherited from v22

Can a nonzero divergence-free Mode-0 S3 circulation produce the already-recovered gravitational readout?

## Exact answer

Not directly.

For edge flow `phi`,

```text
delta C = D_C phi = partial_1 phi.
```

For every cycle flow `z` with

```text
D_C z = 0,
```

the direct Time-Shell perturbation channel receives zero:

```text
G_dir(z)
=
Pi_TS^grav(TT(D_C z))
=
0.
```

Thus the direct channel factors through

```text
Flow / ker(D_C).
```

Divergence-free cycle information is invisible to that quotient.

## Surviving source-grounded route

The gravity recovery separately states that nonlinear closure depends on the full continuity organization `N`:

```text
delta C_*^[N]
=
R_C^[N](
  delta C_src + F_g^[N](delta C_*^[N])
).
```

Therefore compare an unloaded organization `N_0` with a Mode-0 cycle-retaining organization `N_z` while keeping the ordinary source and external GR data fixed.

Define

```text
Delta_C^cyc(z)
=
delta C_*^[N_z] - delta C_*^[N_0].
```

A nonzero result can arise only through cycle sensitivity of the already-existing network-dependent closure/source architecture, not from adding the divergence-free flow as a source.

## Hard no-go

If

```text
R_C^[N_z] = R_C^[N_0]
```

and

```text
F_g^[N_z] = F_g^[N_0]
```

with the same selected fixed-point branch, then

```text
Delta_C^cyc(z) = 0.
```

If UCM source projection is also unchanged, the cycle branch is gravitationally dead in the current model.

## Readable residual

```text
g_z = gbar + Pi_TS^grav(delta C_*^[N_z])
g_0 = gbar + Pi_TS^grav(delta C_*^[N_0])
Delta g_cyc = g_z - g_0.
```

At fixed external GR data, if

```text
Delta g_cyc != 0,
```

then the existing UCM source theorem requires

```text
Delta T_U^cyc != 0.
```

## Path witness

The existing native curvature criterion remains

```text
Xi(P) != Xi(Q).
```

The new diagnostic is whether retaining the Mode-0 cycle changes this asymmetry:

```text
Delta_Xi^z(P,Q) != 0.
```

That demonstrates cycle sensitivity of path geometry but does not yet prove that the nonlinear closure transmits it into `delta C_*`.

## Current dark-matter statement

Do not say:

```text
dark matter = circulation.
```

The surviving candidate is narrower:

```text
Mode-0 persistent S3 cycle organization
-> cycle-sensitive full continuity/UCM transaction
-> nonlinear closure residual
-> Time-Shell gravity
-> gravitational distinction lost by ordinary S2 matter readout.
```

## Immediate next task

Recover or derive whether the existing `R_C^[N]`, `F_g^[N]`, R4-R7 selector, or UCM transaction is actually sensitive to the cycle/path data already present in `N`.

If not, kill the cycle route and return to a non-cycle Mode-0 network mechanism.
