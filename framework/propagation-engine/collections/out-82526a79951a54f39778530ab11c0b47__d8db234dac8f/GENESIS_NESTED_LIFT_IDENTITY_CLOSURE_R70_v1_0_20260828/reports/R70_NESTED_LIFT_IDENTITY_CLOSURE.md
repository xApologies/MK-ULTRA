# R70 — NESTED LIFT IDENTITY CLOSURE

## Theorem candidate

Let:

`A_0(y) superseteq A_1(y) superseteq A_2(y) superseteq ...`

be nonempty compact admissible lift sets inside a closed bounded identity carrier.

Then:

`A_infty(y)=intersection_R A_R(y)`

is nonempty.

This gives a mathematically exact notion of **identity closure under recursive projection refinement**.

### Unique closure case

If the nested constraints separate the identity so that:

`A_infty(y)={x}`,

then the seed plus the full recursive admissibility tower uniquely reconstructs `x`.

A sufficient metric condition is shrinking diameter:

`diam(A_R(y))->0`.

No calculus is foundationally required; this is compactness/separation geometry.

### Residual closure case

Closedness alone does NOT imply:

`A_infty(y)`

is a singleton.

The intersection may remain a nontrivial fiber.

Then the projection system identifies an equivalence class rather than a unique object.

This is not failure.
It is an earned branch:

- **singleton identity closure**
- **residual identity fiber**

## Key correction to "no information loss"

A single lower-dimensional shadow generally loses uniqueness.

But the pair:

`(seed, full coherent lift/refinement tower)`

can retain enough information for unique reconstruction.

Thus the lossless carrier is not the shadow alone.
It is the **seed plus its closed recursive lift structure**.

Next:
`@qmo/inverse_limit_projection_identity`.
