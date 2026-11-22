# 44 — Fiber Moments to Local Dark Geometry

## Inputs

At `p in S3`, the local direction sphere `S2_p` carries at least two hidden-load functions:

```text
L_H(p,v)       = directional Helicon curvature load
Lambda_ER(p,v) = coarse-grained transient-ER load.
```

Define a combined hidden directional density

```text
D_H(p,v)
=
c_F L_H(p,v)
+
c_ER Lambda_ER(p,v)
+
additional status-controlled invariants.
```

## Canonical moments

Define

```text
D0(p)
=
integral_(S2_p) D_H(p,v) dOmega
```

and

```text
D2_ab(p)
=
integral_(S2_p)
(v_a v_b - h_ab/3)
D_H(p,v) dOmega.
```

These are the lowest scalar and traceless tensor moments of the hidden continuity readout.

## Gravitational transduction socket

Define a typed but not-yet-unique map

```text
G_H,p : (D0,D2,history,chi,...) -> Delta g_H,p.
```

The full local metric is

```text
g_full,p = g_vis,p + Delta g_H,p.
```

The apparent dark source inferred by a conventional GR observer is

```text
T_app,H
=
(1/(8*pi*G))
[
G(g_full)-G(g_vis)
].
```

Because the apparent source is constructed from an Einstein-tensor difference of metrics, the geometric Bianchi identity is preserved on the full metric branch. Any split into visible and hidden sectors must still account for exchange terms when separate conservation is asserted.

## Dark-sector criterion

The current Atlas criterion remains:

```text
visible ordinary matter/radiation readout = absent or insufficient,
gravity readout = nonzero.
```

The hidden load is therefore geometry-first. A conventional stress tensor is a downstream representation of that load, not necessarily its primitive ontology.
