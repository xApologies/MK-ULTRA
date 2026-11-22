# Six-Dimensional BRANE

## State space

Let the BRANE internal state be a six-coordinate organizational space:

```text
B⁶ = I × D × Χ × R × P × Z
```

where:

- `I` — identity coordinate
- `D` — dependency coordinate
- `Χ` — chirality / admissibility coordinate
- `R` — recursive-depth coordinate
- `P` — provenance coordinate
- `Z` — realization coordinate

An internal realized object is:

```text
b = (i, d, χ, r, p, z) ∈ B⁶
```

These are not assumed to be ordinary Euclidean spatial dimensions. They are typed organizational coordinates.

## Coordinate meanings

### Identity I

Canonical handle, domain, object class, aliases, version identity.

### Dependency D

Upstream/downstream placement, edge type, path identity, layer, branch, closure membership.

### Chirality Χ

Orientation, admissible continuation, side, handedness, transformation state, local chirality history.

### Recursive depth R

Traversal depth, nested recovery depth, aggregation scale, continuation frontier, termination state.

### Provenance P

Source file, source section, recovery pass, canonical status, confidence, audit state, checksum, revision.

### Realization Z

Canonical object, active traversal object, QMO node, library chunk, equation realization, analogy realization, report section, language rendering.

## Embedding principle

Every loaded module is five-dimensional and is embedded into B⁶ by adding an execution-relative realization coordinate:

```text
ι_M : M⁵ → B⁶
ι_M(m) = (m₁,m₂,m₃,m₄,m₅,z_M(q))
```

where `q` is the current request.

## External projection

The runtime never receives `B⁶`. It receives only a projection:

```text
π_artifact : QMO⁶ → Artifact
```

For Markdown:

```text
π_md : QMO⁶ → .md
```

## Simplicity invariant

```text
Complexity(BRANE interior) must not increase Complexity(runtime contract).
```

The public boundary remains request/response regardless of internal dimensionality.
