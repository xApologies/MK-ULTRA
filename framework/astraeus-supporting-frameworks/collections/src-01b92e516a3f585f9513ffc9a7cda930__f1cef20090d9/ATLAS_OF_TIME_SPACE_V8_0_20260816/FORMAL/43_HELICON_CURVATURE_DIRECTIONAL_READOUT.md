# 41 — Helicon Curvature to Local S² Directional Readout

## Purpose

Provide the first explicit, minimally typed map from a horizontal `S3` Helicon curvature to a field living on the local `S2` projection fiber.

## Helicon connection

Let

```text
A_H in Omega^1(S3, g_H)
```

be the candidate horizontal Helicon connection, with curvature

```text
F_H = dA_H + A_H ^ A_H
```

and invariant inner product `< , >_H` on `g_H`.

## Directional readout

For `p in S3` and a unit vector

```text
v in S(T_p S3) ~= S2_p,
```

define the directional Helicon load

```text
L_H(p,v)
:=
|| i_v F_H(p) ||_H^2.
```

This is a scalar function on the local `S2` fiber:

```text
L_H,p : S2_p -> R_+.
```

It is the first explicit Atlas map of the form

```text
horizontal S3 curvature -> localized S2 readout.
```

## Three-dimensional dual form

Because the base is three-dimensional, the Hodge dual maps a two-form to a one-form:

```text
B_H := *_3 F_H.
```

In an Abelian component or after invariant contraction, the directional load has the familiar geometric form

```text
L_H(p,v)
=
|B_H|^2 - |<B_H,v>|^2.
```

Thus the local S2 projection records how the hidden continuity curvature is oriented relative to each local direction.

## Zeroth and second moments

Define

```text
M0(p) = integral_(S2_p) L_H(p,v) dOmega(v)
```

and

```text
M2_ab(p)
=
integral_(S2_p)
(v_a v_b - h_ab/3) L_H(p,v) dOmega(v).
```

For a single Abelian three-vector representation `B_H`, standard spherical integration gives

```text
M0 = (8*pi/3) |B_H|^2
```

and

```text
M2_ab
=
-(8*pi/15)
[
 B_a B_b - (|B|^2/3) h_ab
].
```

These moments provide canonical scalar-load and anisotropic-load data for the local gravitational transduction.

## Homogeneous no-go recovery

If `F_H` is homogeneous on `S3`, then `M0(p)` is constant across continuity addresses. The local S2 pattern can still carry orientation anisotropy, but no address-localized halo profile arises without an additional localization mechanism.
