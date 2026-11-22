# E039 — Direction-Free TT Support Theorem

> **2026-08-18 Geometry-First Amendment:**  
> The canonical MK43 derivation is now the geometry-first proof in
> `GEOMETRY_FIRST_TT_SUPPORT_THEOREM.md`.  
> The spherical-integral derivation below is retained only as a downstream verification.


## A. Dead-end audit

The current source-component branch self-terminates at two missing typed maps:

1. current-pair native density requires a source-qualified
   `Relationship x canonical TransitionCapacity`;
2. readable density requires `T_rho,R` nonannihilation.

The mounted source explicitly forbids the shortcuts:
- `Bandwidth = TransitionCapacity`;
- runtime transition capacity = canonical transition capacity;
- nonzero native density => readable density automatically;
- one scalar density => full stress-energy tensor.

WL-v174 additionally says the stress-gate branch loops back to the already-known
metric-action selection handle and stops.

Therefore these handles are not "wrong"; they are presently **terminal under the
mounted source state**.

Clover disposition:
preserve them, mark them, and move on.

## B. New mathematical path: direction-free TT support

E038 showed numerically that every E006 trace-free rank-two precursor is TT-visible
for almost every sampled direction, but each also has special silent directions.

Instead of chasing one propagation direction, define the spherical TT-support
functional.

Let `S` be a real symmetric trace-free `3x3` tensor.

For unit direction `n`, let

`P(n)=I-n n^T`

and define the conventional transverse-traceless projection

`TT_n(S)=P S P - (1/2) P tr(P S P)`.

Define the direction-free support functional

`J_TT(S)`
`:= (1/4pi) integral_(S2) ||TT_n(S)||_F^2 dOmega`.

### Theorem E039-T1

For every real symmetric trace-free `S`,

`J_TT(S) = (2/5) ||S||_F^2`.

Hence

`J_TT(S)>0`

if and only if

`S!=0`.

### Proof sketch

For trace-free `S`, write `v=S n` and `q=n^T S n`.

Direct expansion gives

`||TT_n(S)||_F^2`
`= ||S||_F^2 - 2 ||S n||^2 + (1/2)(n^T S n)^2`.

Use the isotropic sphere averages:

`<n_i n_j> = delta_ij/3`

and

`<n_i n_j n_k n_l>`
`= (delta_ij delta_kl + delta_ik delta_jl + delta_il delta_jk)/15`.

Then:

`<||S n||^2> = (1/3)||S||_F^2`

and for trace-free `S`:

`<(n^T S n)^2> = (2/15)||S||_F^2`.

Therefore:

`J_TT`
`= [1 - 2/3 + 1/15] ||S||_F^2`
`= (2/5)||S||_F^2`.

QED.

## C. Meaning

This theorem removes one ambiguity from E038.

A nonzero STF precursor may be silent along special directions, but it cannot be TT
silent in every direction.

So the E006 precursor family has an exact, rotation-averaged, direction-free
TT-support certificate.

This still does NOT identify the physical gravitational mode or replace source `A_g`.

It creates a new work-layer admissibility notion:

`A_TT^exist(S)=1 iff J_TT(S)>0`.

For symmetric trace-free tensors this is equivalent to:

`S!=0`.

Thus all 12 E006 tensors pass a direction-free **existence of TT channel** test.

## D. Why this is useful for the dark-matter trail

The remaining physical question is no longer:

"does any TT channel exist?"

For the current precursor family the answer is mathematically YES.

The remaining question is:

"which TT/helicon channel is selected by the actual gravitational continuation?"

That is a selector/typing problem, not a support-existence problem.

This is a cleaner frontier than continuing to probe scalar density or re-search the
same missing `A_g` formula.
