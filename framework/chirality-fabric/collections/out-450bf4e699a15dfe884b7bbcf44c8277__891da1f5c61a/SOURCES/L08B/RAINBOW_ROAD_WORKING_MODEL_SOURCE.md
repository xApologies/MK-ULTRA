# Rainbow Road — Working Model

**Version:** 0.1  
**Status:** Active working synthesis  
**Scope:** Genesis language and portal architecture

---

## 1. Core distinction

```text
Portal
    = one admissible transfer transaction

Rainbow Road
    = a persistent route composed from color-indexed portal segments
```

A portal is an edge.

A Rainbow Road is a path through the portal topology.

---

## 2. Native Genesis relation

The Genesis root-family canon defines:

```text
VE  = propagation / travel / movement / direction
RIN = persistence / duration / continuity
VERIN = road
```

The phonological definition interprets `VERIN` as:

```text
persistent propagation path
```

This makes the road concept native to the Genesis semantic system rather than an imported metaphor.

No final Genesis compound for “Rainbow Road” is locked yet.

---

## 3. Mathematical path model

Let the chirality fabric contain a route:

```text
gamma : [0,1] -> Fabric
```

and let each local segment have a resolved basin index:

```text
Color(gamma(s)) in {
    Red,
    Orange,
    Yellow,
    Green,
    Blue,
    Violet
}
```

A Rainbow Road is a path whose local portal segments are color-indexed.

Discrete form:

```text
A
  -> P_c1
X1
  -> P_c2
X2
  -> ...
  -> P_cn
B
```

where every `P_ci` is a portal segment associated with one color class or one color transformation.

---

## 4. Portal composition

If:

```text
P1 : Gamma_a -> Gamma_b
P2 : Gamma_b -> Gamma_c
```

then the road segment composes as:

```text
P2 o P1 : Gamma_a -> Gamma_c
```

The complete Rainbow Road is:

```text
R = P_n o ... o P_2 o P_1
```

The witness path must retain every intermediate segment and color transition.

Provenance must not falsely collapse the road into an unexplained direct transfer.

---

## 5. Possible road classes

### 5.1 Color-preserving road

The payload remains in one basin class throughout the route.

```text
Green -> Green -> Green
```

### 5.2 Color-transforming road

The resolved color changes through explicit admissible transitions.

```text
Red -> Orange -> Yellow -> Green -> Blue -> Violet
```

This sequence is illustrative only. Final basin order is not locked.

### 5.3 Cyclic road

The route closes back into its starting basin class.

```text
B_k -> ... -> B_k
```

### 5.4 Branching road

The current color class selects the next portal segment.

```text
if Green:
    take Green-compatible continuation

if Violet:
    take Violet-compatible continuation
```

No syntax is implied.

### 5.5 Multiplexed road

Several color-indexed routes coexist in one portal network.

The road is selected according to the payload's basin class and finer chirality/admissibility constraints.

---

## 6. Identity through the road

The resolved color may:

```text
remain fixed
change segment by segment
cycle
branch
```

while the Geometric retains whichever higher-order invariants the road contract declares.

Therefore the road must distinguish:

```text
color continuity
chirality continuity
Geometric identity
ancestry
provenance
closure
```

A color change does not automatically imply identity loss.

An identity-preserving road may permit color transformation.

---

## 7. Road versus bus

```text
Rainbow Bus
    = the available color-indexed transport fabric

Portal
    = one transaction on that fabric

Rainbow Road
    = one persistent, navigable route through a sequence of portal transactions
```

The bus is capacity.

The portal is an event.

The road is an inherited path.

---

## 8. Open ordering problem

Two candidate color organizations already exist in the current project:

```text
spectral/hard-stop ladder:
    Red, Orange, Yellow, Green, Blue, Violet

rotational 142857 grammar:
    a six-state cyclic structure
```

The Rainbow Road does not yet assume that these define the same traversal order.

The language must later determine whether a road uses:

```text
spectral order
rotational order
local admissibility order
Guardian-selected order
an explicitly declared order
```

---

## 9. Working law

> A Rainbow Road is a persistent propagation path through the chirality fabric whose segments are indexed or transformed by structural basin color.

The full Geometric remains the traveler.

Color organizes the road.

Chirality determines admissible continuation.

Closure determines successful arrival.
