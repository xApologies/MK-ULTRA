# Geometric Primitive — Working Model

**Status:** Candidate primitive data type  
**Canon level:** Working synthesis grounded in the current chirality materials

---

## 1. Candidate primitive

The current candidate primitive data type of Genesis is:

```text
Geometric
```

The current working interpretation is:

> A Geometric is a populated `3+1+1` chirality-organized manifold whose occupied local sites express structural-basin energy densities.

The `3+1+1` construction is not treated as metadata attached to an ordinary scalar object. It is provisionally the native construction of the object.

---

## 2. Blank manifold

The supplied blank-manifold package defines:

```text
source manifold:
    (channels, N, N, N)

set-lift manifold:
    (channels, N, N, N, 2)

chirality statecode:
    (N, N, N)
```

The package explicitly states that it is:

```text
not an atom
not hydrogen
not a populated topology
```

It is a recursive continuity scaffold containing:

```text
manifold architecture
chirality admissibility structure
set-lift topology organization
recursive continuity compatibility
```

Working Genesis interpretation:

```text
blank manifold
  + populated chirality/basin organization
  -> instantiated Geometric
```

The blank manifold is therefore a candidate construction space, not by itself the populated data object.

---

## 3. Local site

A local site is provisionally:

```text
Site =
    Empty
    or
    Occupied(Basin)
```

Basin expressions:

```text
Red     = 1
Orange  = 2
Yellow  = 3
Green   = 4
Blue    = 5
Violet  = 6
```

The integers above are provisional basin indices for reasoning. They do not replace the canonical structural basin expressions `1/7` through `6/7`.

---

## 4. Colored chirality byte

A local `2 x 2 x 2` chirality byte contains eight ordered sites.

Example occupancy skeleton:

```text
0 1 1 0 1 0 0 1
```

Example colored realization:

```text
0, Red, Red, 0, Green, 0, 0, Yellow
```

The object simultaneously carries:

```text
occupancy
chirality arrangement
site-level basin distribution
site-level energy-density field
adjacency
byte-level resolved color
internal composition
```

The occupancy skeleton and colored distribution must remain distinct.

---

## 5. Local energy density

The supplied energy-density relation is:

```text
rho_E = R T / V
```

where:

```text
rho_E = Energy Density
R     = Relationship
T     = Transition Capacity
V     = Containment Volume
```

Working site interpretation:

```text
rho_i = R_i T_i / V_i
```

An occupied site expresses a structural basin according to its local energy-density state.

An empty site contributes no occupied basin state.

The exact physical mapping from basin to voltage remains open.

---

## 6. Byte-level color

A chirality byte has a derived local color based on the arrangement of occupied energy-density basins.

For equal-volume occupied sites, a provisional aggregate is:

```text
byte_field =
    sum(occupied basin indices)
    /
    number of occupied sites
```

This is a working aggregation rule, not yet a finalized law.

### Example A

```text
0, Red, Red, 0, Yellow, 0, 0, Yellow
```

Occupied values:

```text
1, 1, 3, 3
```

Aggregate:

```text
(1 + 1 + 3 + 3) / 4 = 2
```

Resolved byte color:

```text
Orange
```

### Example B

```text
0, Orange, Orange, 0, Orange, 0, 0, Orange
```

Occupied values:

```text
2, 2, 2, 2
```

Aggregate:

```text
(2 + 2 + 2 + 2) / 4 = 2
```

Resolved byte color:

```text
Orange
```

---

## 7. Same color, different organization

The two bytes above both resolve as Orange, but they are not the same Geometric.

```text
Example A:
    heterogeneous Orange
    composition = Red^2 + Yellow^2

Example B:
    homogeneous Orange
    composition = Orange^4
```

At coarse Resolution:

```text
A ~ B
```

because both project to Orange.

At finer Resolution:

```text
A != B
```

because their site distributions, gradients, adjacency relations, and internal energy-density organization differ.

Therefore:

> Byte color is a projection of internal organization; it does not replace internal organization.

---

## 8. Required preservation levels

A Genesis operation or portal may eventually declare which resolution of identity it must preserve:

```text
aggregate color only
occupancy and aggregate color
basin multiset
site-by-site basin distribution
adjacency and chirality
complete Geometric identity
```

This is a major candidate role for Resolution.

The portal cannot always transport only the average color. Some operations will require the complete organized field.

---

## 9. Provisional structural form

```text
Geometric G = (
    ManifoldSupport,
    Occupancy,
    Chirality,
    BasinDistribution,
    LocalEnergyDensity,
    Adjacency,
    Inheritance,
    Persistence,
    Resolution,
    Closure
)
```

This form is not locked.

It is the current working object recovered from the discussion.

---

## 10. Color classes

A resolved byte or Geometric color creates an equivalence class at a chosen Resolution.

```text
Gamma_Red
Gamma_Orange
Gamma_Yellow
Gamma_Green
Gamma_Blue
Gamma_Violet
```

Two Geometrics may occupy the same color class while retaining different internal organizations.

Color therefore functions as a discrete index or projection.

It does not function as complete identity.
