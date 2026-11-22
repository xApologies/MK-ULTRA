# 03 — History Path Algebra

## 1. History path

Let `E_H` be admitted directed state transitions. A finite admissible History is a composable path

```text
h=e_n...e_2e_1:x_0->x_n.
```

with source and target:

```text
src(h)=x_0,
tgt(h)=x_n.
```

History composition is defined when endpoints match. Every state has a trivial History `1_x`.

## 2. No automatic inverse

An inverse History is not assumed. Therefore the native structure is a path category/path algebra, not automatically a groupoid.

This distinction matters for holonomy: a closed loop may be formed from an admissible cycle without requiring each microscopic step to possess a formal inverse.

## 3. Prefix structure

For `h=(e_1,...,e_n)`, define prefixes

```text
h|k=e_k...e_1.
```

Persistence may be tested at every prefix rather than only at the endpoint.

## 4. Closed readable History loop

A History path `gamma_H` is closed at operative/readable level when

```text
Read_R(tgt(gamma_H)) ~ Read_R(src(gamma_H)).
```

Readable closure does not imply Formal Identity closure.

## 5. History orbit

The source braces the History Orbit

```text
Orb_H(Fabr)
```

as the set of History-reachable operative states of a fabric under admissible evolution.

## 6. History and S3

In the current Time-Space atlas, S3 is the principal continuity/history carrier among localized S2 readouts. A local S2 presentation may therefore fail to retain the entire S3 History that produced it.
