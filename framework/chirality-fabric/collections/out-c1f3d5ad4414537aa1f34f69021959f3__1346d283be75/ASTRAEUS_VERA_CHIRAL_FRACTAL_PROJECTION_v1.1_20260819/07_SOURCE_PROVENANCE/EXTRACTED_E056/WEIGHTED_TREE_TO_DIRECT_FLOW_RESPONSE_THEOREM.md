# E056 — Weighted Corridor Tree to Direct-Flow Quotient Response

## 1. Question

E043 and E042 provide the source-native response coordinate

`r_k in im(D_C) ~= Flow/ker(D_C)`.

E054-E055 provide a compact morphology state

`w(E_k) = 8 peak heights + 6 merge levels`

on one fixed labeled corridor merge tree, with dominant History coordinate

`q_k = <w(E_k)-w_*, v_H>`.

E056 asks whether the compact weighted-tree state preserves the information needed to
predict the E043 direct-flow quotient response.

## 2. Common fixed-state origin

The E048 driven fixed environment `E_*` was probed with the exact E043
inherited-environment Hydrogen probe map.

The E043 response arrays were also replayed from their stored E043 environments in
float64 using that same source runner.

This validates the response reconstruction against the archived E043 float32 response
arrays. Across E1-E16 the replay/archived L2 discrepancy lies between approximately

`1.2700e-10` and `1.4782e-10`.

Use the latter only as an **archive reconstruction floor**, not as a physical error bar.

Define

`y_k = r_k - r_*`

and

`x_k = w(E_k) - w_*`.

The tested orbit is E1-E16.

## 3. Order and incidence before regression

Both the weighted-tree distance

`||x_k||`

and the recomputed direct-flow response distance

`||y_k||`

approach the fixed state without an ordering inversion over E1-E16.

Thus the dominant tree coordinate is a valid **History-order coordinate** for this
controlled orbit.

The leading tree-history score and leading response-history score have cosine

`0.9890792161`,

corresponding to an angle of about

`8.4754 degrees`.

So the two dominant relaxations are strongly aligned but not identical.

## 4. The dominant scalar q is not a sufficient linear response coordinate

E055 found that the first weighted-tree direction carries

`0.9997869403603663`

of total squared tree displacement.

However, when the response is predicted using only that one fixed-origin tree
coordinate, the best linear response map leaves relative Frobenius residual

`0.15641948935`

or about **15.64% in response-vector norm**.

Equivalently, the first tree coordinate captures only

`97.553294335%`

of the tested response-displacement energy.

Therefore the E055 statement

`fixed tree + q + small transverse corrections`

cannot be simplified to

`fixed tree + q`

when the target is the direct-flow quotient response.

`q` is an excellent ordering coordinate, but it is not by itself a sufficient linear
response coordinate.

## 5. The small transverse tree information is strongly response-bearing

The transverse weighted-tree subspace carries only

`1 - 0.9997869403603663 = 0.0002130596396`

of tree displacement energy, about **0.021306%**.

Yet the one-coordinate response map misses

`1 - 0.975532943351 = 0.02446705665`

of response displacement energy, about **2.446706%**.

The ratio is approximately

`114.84`.

Thus, within this controlled orbit, the transverse tree information is roughly two
orders of magnitude more important to the response than its tiny share of morphology
energy alone would suggest.

This is the central E056 result.

## 6. Response capture by successive tree coordinates

Using the fixed-origin principal coordinates of the weighted tree:

- tree PC1: response residual norm fraction `15.641949%`;
- tree PC1-2: `1.639810%`;
- tree PC1-3: `0.282759%`;
- tree PC1-4: `0.027441%`.

The corresponding response-energy capture is:

- 1 coordinate: `97.553294%`;
- 2 coordinates: `99.973110%`;
- 3 coordinates: `99.999200%`;
- 4 coordinates: `99.999992%`.

So the missing response information is not arbitrary full-field information. It is
organized along the small transverse weighted-tree directions.

However, do not over-promote the first 2-4 coordinates as an exact sufficient state.
To drive the maximum fitted residual below the E043 archive reconstruction floor, the
full tested tree-history rank of 12 is required.

## 7. Full weighted-tree map

The optimal fixed-origin linear map

`Psi_tree : x_k -> y_k`

using the full 14-weight vector gives global relative residual

`5.6574e-08`.

Its largest absolute residual is the E13 late-state mismatch, about

`2.3622e-11`,

which is below the E043 archived-response replay discrepancy.

Therefore, at the resolution actually preserved by the E043 response archive, the
full weighted tree preserves the tested direct-flow response information.

This is an **orbit-level controlled result**, not a universal response law.

## 8. Late equal-tree states

E055/E054 store E13-E16 at the exact stored fixed weighted-tree vector.

The recomputed response distances to `E_*` are:

- E13: `2.3622e-11`;
- E14: `1.0403e-11`;
- E15: `3.04e-17`;
- E16: `0`.

All are below the E043 archive reconstruction floor.

So the apparent equal-tree / unequal-response collision is not resolved at the
archived E043 response precision and must not be used as evidence for a missing
physical variable.

## 9. Predictive firewall

A leave-one-history-out linear audit is favorable for interior states but exposes the
expected endpoint problem:

- maximum LOO residual over E2-E12: about `0.6882%` of the E1-to-E* response scale;
- holding out E1 requires endpoint extrapolation and gives about `29.95%`.

Therefore E056 does **not** establish a universal extrapolative law from arbitrary
weighted trees to arbitrary direct-flow responses.

It establishes that the tested endogenous History orbit is response-coordinatized by
its weighted corridor tree to archival precision, and that the response-relevant
transverse information is real and quantifiable.

## 10. Result classification

E056 closes as **MODERATE** under the handoff success grammar:

`full 14-weight tree predicts response across the tested orbit`

while

`dominant q alone does not preserve the full response vector under the minimal linear map`.

The tree is therefore more than morphology, but the scalar reduction is too aggressive
for direct-flow response work.

Correct reduced object:

`fixed corridor merge tree`
`+ response-bearing weighted-tree state`
`+ dominant History coordinate q`
`+ necessary small transverse corrections`.

## 11. Boundary

No parent API promotion.

No readable gravitational separation has been established.

No external dark-matter witness has been established.

No claim is made that the fitted finite map is a continuum law or a species-independent
physical operator.

## 12. Next handle

The clean next test is cross-probe validation using already recovered source-neutral
Oxygen readouts:

`TEST_CROSS_PROBE_STABILITY_OF_THE_WEIGHTED_TREE_TO_RESPONSE_MAP_WITH_THE_EXISTING_SOURCE_NEUTRAL_OXYGEN_READOUTS`.

If the same response-bearing transverse tree coordinates survive an independent probe
view, the compact state is more plausibly substrate-native rather than a Hydrogen-only
encoding.
