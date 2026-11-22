# 61 — Helicon Spectrum and Hidden Configuration Modes

The equitable quotient theorem separates two mode families.

## Helicon-readable sector

The image of the lift `Q` consists of amplitudes that are constant on each Helicon identity class:

```text
H_read = Im(Q).
```

When the partition is equitable,

```text
L_U(H_read) subseteq H_read.
```

These are the configuration modes that can be represented by the quotient operator `L_H^Q`.

## Intra-class sector

Let

```text
H_hidden = H_read^perp
```

for a chosen inner product / normalized weighting.

A mode in `H_hidden` changes fine Unit-String configuration while averaging to zero at the Helicon class level.

Therefore Atlas v7 obtains the native distinction

```text
configuration mode
=
Helicon-readable collective mode
+
hidden intra-Helicon deformation mode.
```

This is structurally analogous to the framework-wide rule that an upstream object may contain information absent from a downstream readout.

## Pi-reduced Helicon sector

If pi-rotation is a symmetry and `L_U` commutes with `R_pi`, the Helicon-readable sector can be further restricted to

```text
H_read,+ = H_read intersect Im(P_+).
```

This is a strong candidate for the coherent half-turn-reduced Helicon sector preserved by the recovered relation

```text
H(theta+pi)=H(theta).
```

## Resolution

A later Resolution quotient may merge multiple Helicon classes again:

```text
U_1
 -> Q_H
 -> Q_H/K_R
 -> readable spectral geometry.
```

Thus the full hierarchy becomes

```text
Unit-String configuration
 -> Helicon coherent class
 -> Resolution-readable class
 -> continuum wave/QFT readout.
```

## Status

**DERIVED FROM v7 QUOTIENT CONSTRUCTION.**
