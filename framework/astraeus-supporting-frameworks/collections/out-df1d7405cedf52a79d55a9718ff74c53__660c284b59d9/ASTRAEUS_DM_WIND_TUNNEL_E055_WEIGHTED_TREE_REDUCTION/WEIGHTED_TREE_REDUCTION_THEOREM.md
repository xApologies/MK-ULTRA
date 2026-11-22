# E055 — Low-Dimensional Weighted Merge-Tree Reduction

## 1. Question

E054 showed that the corridor merge-tree combinatorics are fixed from the first
nonfresh History state onward.

Only the numerical weights continue to relax.

E055 asks whether those weights require many independent History coordinates, or
whether they move approximately along one geometric direction.

## 2. Weighted-tree state space

For each nonfresh History state, define the 14-component tree-weight vector:

`w(E)`
`= (8 normalized peak heights, 6 ordered merge levels)`.

Because E054 already proved the combinatorial tree type invariant, all these vectors
live on the same labeled-tree coordinate space.

This is a finite Euclidean geometry problem.

No calculus is used.

## 3. Fixed-state origin

Use the driven fixed weighted tree:

`w_* = w(E_*)`

as the origin.

Define displacement:

`x_k = w(E_k)-w_*`.

The question becomes:

Do the vectors `x_k` lie near one line through the origin?

## 4. Best one-dimensional geometric subspace

Take the orthogonal best-fit line through the collection of displacement vectors.

Equivalently, use the first singular direction of the finite displacement matrix.

The first direction carries:

`99.978694036037%`

of the total squared displacement.

The global residual fraction outside that line is:

`1.459656259650%`.

So the weighted merge-tree evolution is overwhelmingly one-dimensional, but it is
**not exactly one-dimensional**.

That distinction is preserved.

## 5. Shared History coordinate

Let `v_H` be the first unit direction and define:

`q_k = <x_k,v_H>`.

Orient `v_H` so `q_1>0`.

Normalize:

`qhat_k = q_k/q_1`.

The recovered sequence begins:

- `E1`: `qhat=1`
- `E2`: `qhat=0.262967715191`
- `E3`: `qhat=0.0642797698935`
- `E4`: `qhat=0.0150749980999`
- `E5`: `qhat=0.00346784577164`
- `E6`: `qhat=0.000790238578469`
- `E7`: `qhat=0.000181212882863`
- `E8`: `qhat=4.42010712553e-05`
- `E9`: `qhat=1.26258164372e-05`
- `E10`: `qhat=2.52465488543e-06`

The coordinate decreases monotonically toward zero:

`True`.

At the stored array precision, the exact E* tree-weight vector is reached at depths:

`[13, 14, 15, 16]`.

This late exact equality is a property of the stored finite-precision arrays, not a
claim of exact continuum-time convergence.

## 6. Geometric interpretation

The hidden History state now admits the approximation:

`w(E_k) ~= w_* + q_k v_H`.

Thus the reconstructed corridor ecology separates into:

1. a fixed combinatorial merge tree;
2. a fixed driven weight vector `w_*`;
3. one dominant relaxation direction `v_H`;
4. a small orthogonal residual.

This is a much stronger compression than the full 32^3 History field.

## 7. The one-coordinate model is not exact

The strongest one-dimensional model leaves a global relative residual of:

`1.45965626%`.

The largest single-history orthogonal departure, measured relative to the E1-to-E*
tree displacement, is:

`1.30775525%`.

Therefore E055 does NOT replace the full weighted tree by a literal scalar state.

The correct statement is:

**one dominant shared History coordinate plus small transverse corrections.**

That agrees with E053's independent branch-strength result without assuming it.

## 8. Geometry-first hierarchy recovered so far

The hidden substrate can now be compressed in stages:

`full ER History fields`

-> `domain topography quotient`

-> `persistent local defect branches`

-> `History-invariant corridor merge tree`

-> `weighted merge tree`

-> `dominant one-dimensional relaxation direction`.

Different levels retain different amounts of information.

None is silently identified with the full state.

## 9. Dark-sector consequence

The same-Q hidden History family has acquired a compact reduced geometry:

`fixed defect architecture + low-dimensional internal state`.

That is the sort of object that can later be handed to a gravitational/readout map
without replaying every microscopic History step.

It remains an internal pre-gravitational result.

## 10. Next handle

Do not optimize the 1D reduction further.

The next useful question is whether the direct-flow quotient response from E043 can be
read from this reduced weighted-tree geometry.

Test:

`weighted tree coordinate -> direct-flow quotient response`.

If the reduced tree predicts the response up to the already-known small transverse
corrections, we have a genuine geometric sufficient statistic candidate.

If not, keep the tree as morphology only and move on.
