# 14 — Chirality Transport Connection

## Purpose

Define the missing transport law:

```text
P_gamma^chi : C_alpha -> C_beta
```

without deciding the final global Time-Space topology or importing an external gauge group.

---

## 14.1 Two connections are required

The five-dimensional architecture contains:

```text
pi : T5 -> S3
```

with localized fibers `Sigma_p ~= S2`.

Choose an Ehresmann connection on the Time-Space fibration:

```text
T(T5) = V direct_sum H_TS,
V = ker(d pi).
```

`H_TS` determines how points of one localized `S2` projection are continuously identified with points of nearby `S2` projections along an `S3` path.

Separately, choose a chirality connection:

```text
nabla^chi
```

on `E_chi` (or the equivalent connection-selected transport structure when a differential bundle realization is not used).

These objects must not be collapsed:

```text
H_TS != nabla^chi.
```

The first transports the address/fiber geometry. The second transports chirality organization on that geometry.

---

## 14.2 Horizontal lift of a base path

Let:

```text
gamma : [0,1] -> S3
```

with endpoints:

```text
gamma(0)=p_alpha,
gamma(1)=p_beta.
```

For `x_0 in Sigma_alpha`, the Time-Space connection defines a horizontal lift:

```text
x_tilde(s) in T5
```

satisfying:

```text
pi(x_tilde(s)) = gamma(s),
x_tilde(0)=x_0,
x_tilde_dot(s) in H_TS.
```

When defined for all `x_0`, this generates a fiber transport map:

```text
Phi_gamma^TS : Sigma_alpha -> Sigma_beta.
```

---

## 14.3 Chirality parallel-transport law

Along each lifted point path `x_tilde(s)`, chirality transport is defined by:

```text
D_s^chi c(s)
:=
nabla^chi_{x_tilde_dot(s)} c(s)
=
0.
```

The unique solution, when existence/uniqueness conditions hold, defines:

```text
T_gamma,x0^chi : (E_chi)_{x_0} -> (E_chi)_{Phi_gamma^TS(x_0)}.
```

The full field transport is then:

```text
(P_gamma^chi chi_alpha)(Phi_gamma^TS(x))
=
T_gamma,x^chi( chi_alpha(x) ).
```

Thus:

```text
P_gamma^chi : C_alpha^formal(B) -> C_beta^formal(B).
```

Resolution readout can be applied afterward when the transport is compatible with the Resolution quotient.

---

## 14.4 Discrete relation to the recovered chirality transport tau

For a partition:

```text
0=s_0 < s_1 < ... < s_N=1,
```

the continuum transport reduces to a sequence:

```text
chi_(n+1) = tau_n(chi_n),
```

with:

```text
tau_n in G_chi(B)
```

for reversible corridor transport.

Therefore the existing inheritance relation:

```text
chi(I^n(xi)) = tau^n(chi(xi))
```

is recovered as the discrete/finite-step form of the chirality connection law when the transport is homogeneous or when `tau^n` is read as ordered composition.

---

## 14.5 Identity-preserving corridor condition

Let `W_Id` denote the declared Identity Witness data.

A corridor transport is identity-preserving when:

```text
P_gamma^chi(W_Id(alpha)) ~_Id W_Id(beta).
```

Equivalently, for each protected invariant `J`:

```text
J(P_gamma^chi chi_alpha) = J(chi_alpha)
```

within the stated scope.

This permits representation change without identity loss.

---

## 14.6 Horizontal continuity law

The minimal inter-projection continuity condition is:

```text
nabla_H^chi chi = 0
```

for pure corridor transport.

Local dynamics inside a selected `S2` projection need not vanish:

```text
nabla_V^chi chi = R_local(chi)
```

for a model-specific local redistribution/transduction operator `R_local`.

This supplies the disciplined split:

```text
horizontal = preserve/inherit across S3 continuity
vertical   = local physical organization inside S2.
```

---

## Status

**CROSSROAD_B_STRUCTURAL_CLOSURE**

Atlas v2.0 now possesses an exact abstract transport law. The remaining specialization is the concrete connection representation and its operator coefficients, not the meaning of corridor transport itself.
