# GENESIS / MK Ultra — Time-Space S0→S4 Mathematics Handoff v1.0.0

**Date:** 2026-09-03  
**Scope:** mathematics only  
**Canonical top-level project name:** **MK Ultra**  
**Historical source alias preserved:** `MK43 Ultra`

## Purpose

Portable continuity package for the Time-Space hierarchy developed/recovered in this thread. It is designed so a future thread or Codex/QMO crawl can recover the actual mathematics without re-deriving the sphere hierarchy from conversation history.

## Included

- source-preserved Time-Space hierarchy from `S^0` through `S^4`;
- explicit standard Riemann-sphere chart for `S^2`;
- explicit recursive/suspension lift `S^2 -> S^3`;
- explicit recursive/suspension lift `S^3 -> S^4` completed on 2026-09-03;
- nested `S^2 -> S^3 -> S^4` coordinate law;
- local backwards/recovery maps;
- pole/History guard;
- normalized squared-coordinate constraint weights;
- QMO/SQLite index with provenance and authority status;
- original source archives and SHA-256 receipts.

## Explicitly excluded

No SPARC, KiDS, T01–T06, dark-matter scoring, fitted parameters, empirical pass/fail claims, or observational test results are included.

## Core nested law

Let `n=(n_x,n_y,n_z) in S^2`, let `tau` be the `S^3` ordering parameter, and let `sigma` be the `S^4` organization parameter.

```text
x = cos(tau) n_x
y = cos(tau) n_y
z = cos(tau) n_z
w = sin(tau)
```

so `(x,y,z,w) in S^3`, and then

```text
X = cos(sigma) x
Y = cos(sigma) y
Z = cos(sigma) z
W = cos(sigma) w
V = sin(sigma)
```

so `(X,Y,Z,W,V) in S^4`.

Combined:

```text
X = cos(sigma) cos(tau) n_x
Y = cos(sigma) cos(tau) n_y
Z = cos(sigma) cos(tau) n_z
W = cos(sigma) sin(tau)
V = sin(sigma)
```

and identically

```text
X^2 + Y^2 + Z^2 + W^2 + V^2 = 1.
```

Read `01_TIME_SPACE_S0_S4_CORE.md` first.
