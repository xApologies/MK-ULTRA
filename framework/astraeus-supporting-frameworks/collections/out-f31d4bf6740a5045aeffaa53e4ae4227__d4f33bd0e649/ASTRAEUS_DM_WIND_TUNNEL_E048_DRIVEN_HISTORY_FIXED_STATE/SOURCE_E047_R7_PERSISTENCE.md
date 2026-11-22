# E047 — R7 Projective History Persistence

## 1. Question

E043-E046 showed a same-Q hidden History family approaching a stable topographic basin.

Now stop adding new H2 History writes.

Does the retained substrate state persist, or is it only a driven transient?

There is no fully source-defined "empty environment time evolution" runner in the
mounted corpus.

Therefore E047 does **not** invent one.

Instead it isolates the only reconstructed operator explicitly labeled as slow
environmental relaxation: the R7 environment step.

This is an operator-isolation diagnostic.

## 2. Recovered R7 relaxation operator

The reconstructed runner applies at R7:

`E -> 0.90 E`

simultaneously to:

`chi`,
`adj_memory`,
`corridor_memory`,
`persistent_memory`.

Call this isolated map:

`R(E)=rE`, with `r=0.90`.

Starting from the saturated E043 state `E_16`:

`E_16^(n)=R^n(E_16)=r^n E_16`.

No new T-stage write, H2 traversal, corridor formation, or R0-R6 ecology update is
applied in this isolate.

## 3. Geometry-first result: the relaxation orbit is one ray

The sequence:

`E_16, rE_16, r^2E_16, ...`

lies on one positive ray in ER state space.

Define positive-scale equivalence:

`E ~_+ E'`

iff:

`E'=aE` for some `a>0`.

Then for every finite `n`:

`[R^n(E_16)]_+ = [E_16]_+`.

So the R7-isolated relaxation is a **fixed point in projective state space** even
though its amplitude contracts in the full vector space.

This is exact finite geometry.

No calculus is required.

## 4. E044 topography quotient

E044 normalizes every ER field before reading its domain topography.

Positive uniform scaling therefore cancels exactly.

Across all tested R7-isolate steps:

`n=0...128`,

the E044 topology-only fingerprint and the complete positioned threshold-mask
fingerprint remain identical to E16.

Result:

`environment topography invariant = True`.

Thus:

`pi_top(R^n(E_16)) = pi_top(E_16)`

for every tested finite `n`.

In fact this follows symbolically from positive-scale invariance, subject only to
nonzero finite amplitude.

## 5. Cross-probe readout

The source-neutral E008 H/O readout is linear in the three structural memory fields:

`R_A(E)=A*(A_mem+K_mem+P_mem)`.

Therefore under the isolated R7 map:

`R_A(R^n(E_16)) = r^n R_A(E_16)`.

All seven H/O views satisfy this scalar-ray law numerically with maximum L2 error:

`2.693299013657489e-15`.

After normalizing away amplitude, every tested H/O readout retains exactly the same
topographic threshold masks through all `128` isolate steps.

Maximum normalized-shape error:

`4.440892098500626e-16`.

## 6. Persistence ruling

The retained state has **two different persistence statuses**.

### Full-amplitude state

NOT persistent.

Its magnitude contracts as:

`||R^n(E)|| = r^n ||E||`.

For example:
- <= 50% amplitude after 7 isolated R7 steps;
- <= 10% after 22 steps;
- <= 1% after 44 steps.

These are operator-step counts, not physical times.

### Projective/topographic state

Persistent for every finite isolated step.

Its domain shape, normalized field organization, and all tested normalized H/O
readout topographies are unchanged.

So E047 recovers:

**amplitude relaxation + projective shape memory.**

## 7. Important limit boundary

As:

`n -> infinity`,

the full-amplitude state tends toward the zero state.

At exactly zero, a projective class is undefined.

Therefore E047 does NOT establish eternal frozen memory.

It establishes finite-step preservation of the normalized/topographic organization
along a contracting ray.

## 8. Dark-matter consequence

The current reconstructed substrate does not support the claim:

"stop all writing and the full hidden response remains forever."

Instead it supports a more precise architecture:

`ongoing write ecology`
-> `saturated hidden state`

and, after writes stop:

`saturated state`
-> `amplitude relaxation along a topology-preserving ray`.

Thus a persistent macroscopic effect in this reconstruction would require either:
- continuing environmental writes / dynamic equilibrium;
- a source-native nondecaying component not yet recovered;
- or a different physical relaxation rule.

This is a valuable negative boundary.

## 9. Next handle

Return to the driven orbit.

Ask whether E043 saturation is a genuine balance between:
- History injection;
- R7 relaxation.

If yes, characterize the saturated dark-defect state as a **driven geometric fixed
class** rather than a fossil memory state.
