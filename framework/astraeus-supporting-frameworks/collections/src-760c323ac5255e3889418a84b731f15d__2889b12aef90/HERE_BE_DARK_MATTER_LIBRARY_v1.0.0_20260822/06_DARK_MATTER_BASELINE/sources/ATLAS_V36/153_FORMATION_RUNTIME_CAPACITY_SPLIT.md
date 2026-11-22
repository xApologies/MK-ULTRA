# 153 — Formation Capacity / Runtime Capacity Split

## Purpose

V19 exposed a type collision: the free-Bandwidth transition valuation measures remaining reconfiguration headroom, while the native energy-density equation requires the Transition Capacity of relationships that already exist inside a region.

V20 resolves that collision structurally.

## Definitions

### Formation Capacity

`T_form` measures capacity for topology-changing or relationship-forming transformations that are still available before closure.

Its domain is the pre-selection / R4 candidate landscape.

### Runtime Capacity

`T_run` measures the maximum admissible continuity flow carried by an already-selected persistent relationship after R5/R6/R7 closure.

Its domain is the persistent support `E_*`.

Thus:

```text
T_form : candidate-reconfiguration structure -> nonnegative capacity
T_run  : persistent relationship -> nonnegative flow capacity.
```

They are not the same map.

## Theorem V20-T5 — Saturation separation

If formation Bandwidth is exhausted, then formation capacity may vanish:

```text
B_free = 0
=>
T_form = 0.
```

This places no logical requirement on `T_run` because `T_run` is defined on a different domain: the already-committed persistent support.

Hence it is consistent to have

```text
T_form = 0
and
T_run > 0.
```

QED by type separation.

## Interpretation

A persistent structure can be difficult or impossible to reconfigure while still carrying continuity load through the relationships that constitute it.

This supplies a precise mathematical version of the v19 observation that high worldweave inertia / low free Bandwidth need not imply gravitational emptiness.

## Black-hole relevance

The recovered black-hole condition

```text
A_out -> 0
```

constrains outward readable restructuring. It must not automatically be interpreted as

```text
all internal/network runtime capacity -> 0.
```

Any such conclusion would require an additional theorem about the relevant runtime feasible-flow family.

## Dark-sector relevance

This split permits a constrained relational network to be simultaneously:

```text
low-reconfiguration
high-persistence
load-bearing.
```

Whether the observed dark-matter phenomenon is produced by such a runtime-capacity sector remains an open physical question.
