# NEXT HUNT — E056
## Weighted-tree geometry -> direct-flow quotient response

### Question

The current dark-defect state has two descriptions:

1. source-native response:
   `r_k in im(D_C) ~= Flow/ker(D_C)`;

2. compact morphology:
   `w_k = fixed corridor tree weights`
   with dominant reduced coordinate `q_k`.

Does the compact tree state predict the direct-flow quotient response?

### Recommended geometry-first procedure

1. Recover the exact E043 response vectors `r_k`.
2. Recompute or recover the same-H response at the E048 driven fixed state `E_*` if
   needed, so both tree and response spaces share the same fixed-state origin.
3. Define response displacement from saturation:
   `y_k = r_k-r_*`.
4. Test **order and incidence before regression**:
   - does tree-distance order imply response-distance order?
   - do equal/near-equal tree states imply equal/near-equal response states?
   - does the first tree coordinate preserve the response-orbit ordering?
5. Compare the geometry:
   - rank of the response displacement orbit;
   - rank of the weighted-tree displacement orbit;
   - principal angles / alignment between their History-coordinate sequences;
   - nearest-neighbor ordering in History depth.
6. Only then test a minimal finite map:
   `Psi_tree:w_k -> r_k`
   or, if justified,
   `Psi_q:q_k -> r_k`.
7. Quantify what is lost:
   `epsilon_response = r_k - Psi_tree(w_k)`.
8. Do not call the tree a sufficient statistic unless the residual is bounded at a
   meaningfully small level across the whole tested orbit.

### Success outcomes

Strong:
`fixed tree + q` predicts the direct-flow quotient to small controlled residual.

Moderate:
full 14-weight tree predicts response, but q alone does not.

Negative:
tree geometry is morphology only; response needs information outside the corridor tree.

Any of these is useful. Do not force success.

### If E056 self-terminates

Move away from reduced-state compression.

Return to the main physical frontier and use the now-established same-Q,
multi-History, local-defect family as the upstream witness when a new source-valid
gravitational transmission handle appears.
