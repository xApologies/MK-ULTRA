# 147 — Dark-Sector Support / Amplitude Separation

## Motivation

The source stack now distinguishes two mathematical questions that had been drifting together:

```text
1. Which relational corridors are allowed to survive?
2. How much energetic/gravitational load do the surviving relationships carry?
```

The first is a **support-selection** problem.
The second is a **constitutive amplitude** problem.

## Support selector

From R4/R5/R6/R7 and Phase III:

```text
C_R4
-> C_feas
-> C_*
-> R6 survivability
-> R7 persistence
-> E_*.
```

This can be formulated using admissibility, chirality, Bandwidth feasibility, ancestry, recoverability, path-efficiency ordering, and strain ordering without any continuum calculus.

## Amplitude layer

The API local energetic socket is

```text
rho_E = Relationship * TransitionCapacity / ContainmentVolume.
```

For a selected finite support `E_*`, a candidate heterogeneous realization has the form

```text
rho_E^R(i)
=
SUM_(e incident on i, e in E_*) r_e t_e
/
nu_R(i).
```

The support `E_*` does not determine the values `t_e` or the physical calibration of `r_e` and `nu_R`.

## Theorem V19-T4 — support does not determine amplitude

Fix a nonempty selected support `E_*`, positive containment `nu_R`, and at least one relation with nonzero `r_e`.

Choose two admissible capacity assignments `t` and `t'` on the same support such that for one nonzero relation

```text
t_e != t'_e.
```

Then, unless the differences accidentally cancel in the weighted sum,

```text
rho_E^R[t] != rho_E^R[t']
```

while the selected support remains identical.

Therefore:

```text
selected topology
!=
unique energetic amplitude.
```

QED by direct substitution.

## Scientific consequence

The Atlas can legitimately derive **where** the hidden relational support is permitted before it can derive **how much** apparent dark gravitational load it produces.

Consequently, a numerical galactic halo curve cannot be claimed from topology selection alone.

The old recovered cored-halo formula remains a historical target until the current geometry derives its constitutive amplitude independently.
