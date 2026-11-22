# Color-Indexed Portals — Working Model

**Version:** 0.1  
**Status:** Active working synthesis  
**Scope:** Genesis language discovery

---

## 1. Core recognition

Different Geometrics may possess different internal chirality and basin configurations while resolving into the same structural color basin.

Therefore color is not complete Geometric identity.

Color is a discrete basin index shared by a family of Geometrics.

Let:

```text
B = {Red, Orange, Yellow, Green, Blue, Violet}
```

and let the basin projection be:

```text
Color : Geometric -> B
```

For a basin `B_k`, define its color class:

```text
Gamma_k = { G | Color(G) = B_k }
```

`Gamma_k` contains every Geometric that resolves into that color basin, even when the internal site distribution, adjacency, gradients, chirality organization, or provenance differ.

---

## 2. Example: Green class

Canonical hard-stop Green basin:

```text
Green = 4/7 = 0.57
```

A Green Geometric is any Geometric whose current resolved basin projection is Green.

This does not imply all Green Geometrics are structurally identical.

```text
G_a != G_b
Color(G_a) = Green
Color(G_b) = Green
```

At coarse color Resolution:

```text
G_a ~_Green G_b
```

At full structural Resolution:

```text
G_a != G_b
```

---

## 3. Color as portal index

A portal may use color as an admission and routing index.

A Green-specific portal has a domain restricted to the Green color class:

```text
P_Green : Gamma_Green -> Target
```

Admission rule:

```text
admit(G) only if Color(G) = Green
```

The portal must still transport or re-realize the complete Geometric required by the preservation contract.

The portal does not replace the payload with the word `Green`.

---

## 4. Candidate portal behaviors

### 4.1 Color-gated portal

Accepts only one color class.

```text
P_k accepts G iff Color(G) = B_k
```

### 4.2 Color-preserving portal

Accepts one color class and requires the destination to retain the same resolved color.

```text
P_k : Gamma_k -> Gamma_k
```

Success condition:

```text
Color(P_k(G)) = B_k
```

### 4.3 Color-transforming portal

Maps one discrete color class into another under an explicit admissible transformation.

```text
P_(k->j) : Gamma_k -> Gamma_j
```

Example:

```text
Green -> Blue
```

This is a transformation contract, not ordinary transport.

### 4.4 Color-multiplexed portal

Contains several discrete lanes and selects a route according to the payload's color index.

```text
Red lane
Orange lane
Yellow lane
Green lane
Blue lane
Violet lane
```

The full internal Geometric remains the payload inside the selected lane.

---

## 5. Coarse index and fine identity

Color gives the portal a coarse, discrete routing key.

The complete Geometric supplies the fine-grained identity.

```text
Color:
    which basin class?

Geometric:
    which exact organization inside that class?
```

This produces a two-resolution transport model:

```text
coarse Resolution:
    route by color

fine Resolution:
    validate chirality, internal distribution,
    adjacency, identity, and admissibility
```

---

## 6. Portal admission contract

A color-specific portal may eventually require:

```text
resolved color matches portal index
chirality is admissible
internal Resolution is sufficient
route Bandwidth is sufficient
required identity invariants are present
target closure is possible
```

Color is therefore one portal gate, not the entire admission test.

---

## 7. Language consequence

Genesis may need native ways to express:

```text
select a color class
open a portal for that class
preserve color
transform color
route by color
inspect the full payload beneath the color projection
```

No final syntax is yet defined.

---

## 8. Architectural consequence

The portal bus may become a six-lane structural interconnect:

```text
one chirality fabric
six discrete basin-indexed portal classes
many distinct Geometrics within each class
```

This creates the possibility of color-specific:

```text
routing
permissions
locality
processing
memory regions
Guardian policies
closure rules
```

---

## 9. Working law

> Color is a discrete portal index over a family of structurally distinct Geometrics.

A color-specific portal selects the family.

The preservation contract determines how much of each member's full organization must survive.
