# E041 — Intrinsic Principal TT Channel Theorem

## 1. Setup

Let `S` be a real symmetric trace-free `3x3` tensor with distinct ordered eigenvalues:

`lambda_1 < lambda_2 < lambda_3`

and orthonormal eigenvectors:

`e_1,e_2,e_3`.

E040 showed that TT support exists on:

`RP^2 minus two silent projective axes`.

That still leaves infinitely many supported channels.

E041 asks whether the tensor geometry itself contains one distinguished projective
channel without adding an external calibration.

## 2. Principal-axis TT powers

For propagation along a principal axis, the transverse plane is spanned by the other
two eigenvectors.

Therefore:

`||TT_(e_1)(S)||^2 = (1/2)(lambda_2-lambda_3)^2`

`||TT_(e_2)(S)||^2 = (1/2)(lambda_1-lambda_3)^2`

`||TT_(e_3)(S)||^2 = (1/2)(lambda_1-lambda_2)^2`.

Because:

`lambda_3-lambda_1`

is strictly larger than either adjacent eigenvalue gap,

the middle-eigenvalue axis satisfies:

`||TT_(e_2)(S)||`
`>`
`||TT_(e_1)(S)||`

and:

`||TT_(e_2)(S)||`
`>`
`||TT_(e_3)(S)||`.

So among the three intrinsic principal axes, `[e_2]` is the unique projective
max-TT channel.

## 3. Global maximality

Write:

`n = n_1 e_1 + n_2 e_2 + n_3 e_3`

and:

`x_i = n_i^2`.

Then:

`x_i >= 0`

and:

`x_1+x_2+x_3=1`.

For trace-free `S`:

`||TT_n(S)||^2`
`= ||S||^2`
`  - 2 sum_i lambda_i^2 x_i`
`  + (1/2)(sum_i lambda_i x_i)^2`.

As a function of the barycentric coordinates `x_i`, this is a convex quadratic on the
2-simplex.

A convex function on a simplex attains its maximum at a vertex.

The three vertices are exactly the principal projective axes.

The previous principal-axis comparison therefore proves that the unique global
projective maximizer is:

`[e_2]`.

Thus define the parameter-free geometry-only selector candidate:

`Sel_maxTT(S) := [e_2]`.

## 4. Relation to the silent axes

For a biaxial STF tensor, E040 gave the two silent projective axes:

`[n_+]`, `[n_-]`

with both lying in:

`span(e_1,e_3)`.

Therefore:

`e_2 dot n_+ = 0`

and:

`e_2 dot n_- = 0`.

The unique maximum-TT axis is geometrically normal to the plane containing both
TT-silent axes.

So the projective TT landscape has an exact intrinsic skeleton:

- two silent lines in the extreme-eigenvector plane;
- one unique maximal line normal to that plane.

## 5. What this does NOT prove

No mounted source says:

"gravity chooses the maximum-TT channel."

Therefore:

`Sel_maxTT`

is a **geometry-only canonical selector candidate**,
not the physical gravitational selector.

It is valuable because:
- it uses no scale;
- it uses no calibration;
- it is rotation-covariant;
- it is unique for every current biaxial precursor;
- it is derived entirely from the precursor tensor itself.

## 6. Source chirality / helicon interface

The Version-1 API directly recovers:

`@chirality CONTRIBUTES_TO @helicon_orientation`.

The Transduction source also recovers:

`chirality structure -> allowed spectral mode -> admissible update`.

But the same source explicitly says the exact native spectral mode is unresolved.

Therefore a natural decomposition is:

`STF geometry -> projective channel [e_2]`

then, only if source data permits:

`chirality/helicon orientation -> orientation lift of [e_2]`.

Because conventional TT is projective:

`[e_2] = {+e_2,-e_2}`.

Chirality is the correct kind of structure to distinguish the two orientations, but
the current source does not supply the instance map.

## 7. Construction-stability audit

E006 contains 12 precursor tensors generated from three memory fields and four
endpoint-edge lift constructions.

Every tensor has a unique intrinsic `[e_2]`.

However these projective axes do not all agree across the 12 constructions.

Therefore the geometry-only selector is unique **per precursor tensor** but is not yet
construction-independent.

That means the physical branch still requires a source rule telling us which precursor
construction / helicon realization is the relevant one.

This prevents accidental overpromotion.

## 8. Result

E041 closes a new mathematical question:

**Given one nonzero biaxial STF precursor tensor, is there a unique parameter-free
projective direction singled out by TT geometry itself?**

YES:

`[e_2]`.

But the physical selector remains open because:
- maximum-TT selection is not source-promoted;
- precursor construction is not unique;
- exact chirality-to-helicon orientation lift is unresolved.
