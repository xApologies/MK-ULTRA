# ASTRAEUS Dark-Matter Wind Tunnel — Experiment E001

## Layered readout-equivalent pair through the ER-foam environment

**Status:** Controlled MK43 sandbox experiment  
**Physical dark-matter witness:** NOT ESTABLISHED  
**Parent/API promotions:** 0

## Question

Can two mathematical states that have the **same declared top-down readout**
produce distinguishable ER-foam organization when they differ only in hidden
layer/depth organization?

This is the smallest direct test suggested by the mounted Pipeline / Pipeline 2 /
ER-Foam environment.

---

## 1. Controlled pair

Use one `2x2x2` ER-cell-scale layered state.

### Full state

`z = 0`

```text
+  .
.  +
```

`z = 1`

```text
.  -
-  .
```

The two layers carry opposite diagonal chirality organization.

### Visible reconstruction

Take the exact top-down readout and re-embed it as one flat layer:

`z = 0`

```text
+  -
-  +
```

`z = 1`

```text
.  .
.  .
```

This visible lift is an experiment definition, not a newly promoted canonical
projection operator.

---

## 2. Readout equality

Define the controlled top-down readout by summing over depth.

Both states give exactly the same occupancy:

```text
1 1
1 1
```

and exactly the same projected chirality:

```text
+1 -1
-1 +1
```

Therefore, in this controlled experiment,

`P_top(full) = P_top(visible)`.

The two objects are readout-equivalent by construction.

---

## 3. Exact geometric difference before T5

The inherited ER tile is the cube graph `Q3`:

- 8 sites
- 12 unit edges

Using ordinary six-neighbor cube adjacency:

### Full layered state

- occupied-to-occupied edges: **0**
- occupied/background interface edges: **12**

### Flat visible reconstruction

- occupied-to-occupied edges: **4**
- occupied/background interface edges: **4**

So the first exact combinatorial split occurs no later than T2:

`Adj(full) != Adj(visible)`.

No field equation or calculus is required for this result.

---

## 4. ER-foam response

The supplied ER tensor has shape

`(operator, x, y, z, chirality, persistence) = (7,2,2,2,2,2)`.

Because the package does not name which chirality index is `+` and which is `-`,
the experiment was run under **both** conventions.

Empty sites retain the chirality-averaged local ER rest value.
Occupied sites select their local chirality branch.

### Before T5 — persistence index p=0

The full and visible states already produce a nonzero ER-state separation:

- L2 separation ≈ **0.141421**
- L1 separation ≈ **0.400000**

under either chirality-index convention.

### T5 and later — persistence index p=1

When the state crosses the T5 persistence boundary, the ER separation remains
nonzero and slightly thickens:

- L2 separation ≈ **0.144250**
- L1 separation ≈ **0.408000**

under either convention.

Thus the T5 transition does **not** force the two readout-equivalent
environmental states to coincide.

This is the key result of E001:

`same top-down readout != same ER-foam state`.

---

## 5. R4 -> R6 corridor-survival stress test

For this controlled experiment, R4 candidate corridors are the bounded
occupancy/background interface edges.

Every candidate is scored by the same source-ER constructive response at its
occupied endpoint:

`score = mean(stabilize, redistribute, close)` at persistence `p=1`.

No element identity or dark-matter label enters the score.

R5 is stress-tested with a fixed corridor-bandwidth budget `B`.
The same ranking/selection rule is applied to both states.
R6 preserves selected bounded zero-strain corridors because the controlled test
introduces no ancestry loss, strain failure, or over-budget selection.

### Result

For **both** possible chirality-index conventions:

- `B = 1`: outcome is symmetry/tie sensitive.
- `B >= 2`: the stabilized full and visible corridor sets differ.

Therefore, for this sandbox:

`K6(full) triangle K6(visible) != empty`

is robust once the available corridor budget is at least two.

This is a new experimental reduction:

> the hidden depth distinction survives the generalized topology engine unless
> the corridor bandwidth is collapsed to the single-corridor symmetric limit.

---

## 6. Why this matters for the dark-matter branch

E001 supplies a concrete microscopic mechanism witness for the architecture:

```text
same S2 readout
    ->
different hidden layer/depth adjacency
    ->
different ER-foam state
    ->
difference survives T5 persistence thickening
    ->
R4/R5/R6 can preserve a different stabilized corridor set
```

It does **not** yet establish physical dark matter.

The next high-value gates are:

1. choose a source-admitted physical realization of the pair;
2. select `K_*` from the stabilized symmetric difference;
3. place an admissible target isolator on `K_*`;
4. test `Respond(M_*,K_*) != M_*`;
5. carry the response through the direct gravity / Time-Shell readout;
6. test the final Dark-Matter Qualification Locus.

---

## 7. Interpretation

The important object is not an invisible extra particle.

The controlled experiment shows that the **environment can distinguish organization
that the declared visible projection cannot distinguish**.

At the sandbox level:

`P_top(full) = P_top(visible)`

while

`ER(full) != ER(visible)`.

That is exactly the kind of information-conservation/readout defect the current
dark-matter program is designed to test.
