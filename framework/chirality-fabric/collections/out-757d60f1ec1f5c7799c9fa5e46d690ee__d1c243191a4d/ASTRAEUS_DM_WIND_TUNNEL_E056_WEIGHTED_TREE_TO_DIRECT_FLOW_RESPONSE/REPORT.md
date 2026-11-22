# ASTRAEUS Dark-Matter Wind Tunnel E056
## Weighted Tree -> Direct-Flow Quotient Response

**Status:** CLOSED — MODERATE SUCCESS  
**Full weighted tree response map:** PASS across tested orbit to E043 archival precision  
**Dominant scalar q as sufficient linear response state:** FAIL  
**Readable gravity:** NOT YET  
**Parent promotions:** 0

E056 answered the handoff question.

The weighted corridor tree is not merely morphology.

After reconstructing the E043 Hydrogen direct-flow responses against the E048 driven
fixed state, the response-distance orbit and tree-distance orbit preserve the same
History order from E1 through E16.

But the surprising part is the transverse information.

E055's dominant tree coordinate carries **99.978694% of tree displacement energy**.
If I keep only that scalar and fit the minimal fixed-origin linear map into the E043
direct-flow response, the response-vector residual is still **15.6419%**.

Adding the tiny transverse tree coordinates collapses that residual rapidly:

- 1 tree coordinate -> 15.6419%
- 2 -> 1.63981%
- 3 -> 0.282759%
- 4 -> 0.0274413%
- full weighted tree -> `5.66e-08` relative residual

The transverse tree space contains only about **0.021306%** of tree displacement
energy, yet it accounts for about **2.446706%** of response energy missed by the
one-coordinate map — a leverage ratio of about **114.84x**.

So we do **not** get to throw away the small E055 transverse corrections.

The correct compression is:

`fixed tree + dominant q + small but response-bearing transverse coordinates`.

The full tree map is accurate below the E043 stored-response reconstruction floor
across the tested orbit. That is enough to classify E056 as the handoff's **moderate
success** case: the full 14-weight tree carries the response information, while q alone
does not.

This remains a controlled reconstructed-sandbox result. It does not close the readable
gravity gate.

### Next

Cross-probe the weighted-tree/response relation with the already recovered
source-neutral Oxygen views. That is the clean test of whether this compact response
state is substrate-native rather than Hydrogen-specific.
