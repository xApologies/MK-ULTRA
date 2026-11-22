# E050 — Local Corridor-Stress Composition Test

## 1. Why this test is source-valid as a diagnostic

Pipeline 2 explicitly permits:

- Local Topology Stress;
- Corridor Stress at R4;
- localized bounded deformation;
- recovery/survivability testing through R5-R7.

It prohibits:
- new domains;
- chirality writes;
- ancestry overwrite;
- hardcoded element outcomes.

E050 therefore adds no new pipeline operator.

It applies one transparent bounded diagnostic exposure to the already-emitted R4
corridor candidate:

`candidate' = candidate * (1 - epsilon M)`,

with:

`epsilon = 0.25`,

for one R4 exposure at cycle:

`1`.

`M` is a local 0/1 mask.

The deformation only suppresses existing candidate amplitude.
It creates no corridor support where none existed.

## 2. Geometry from E049

Use the two E049 driven-fixed-state corridor peaks:

`A = (17, 16, 15)`

`B = (14, 16, 15)`.

Their Manhattan separation is:

`3`.

Two mask scales are tested.

### Separated case

Radius-1 graph balls:

`A_1`, `B_1`.

Sites:
- A: `7`
- B: `7`
- overlap: `0`.

### Overlap case

Radius-2 graph balls:

`A_2`, `B_2`.

Sites:
- A: `25`
- B: `25`
- overlap: `2`.

Thus the perturbation geometry crosses from disjoint support to overlapping support
without changing the stress law or amplitude.

## 3. Composition residual

Let `F_M(E_*)` be one complete pair-enabled H2 traversal/ecology with local R4 stress
mask `M`.

Let the unstressed fixed-map output be:

`F_0(E_*)`.

Define the environment perturbation response:

`d_M = F_M(E_*) - F_0(E_*)`.

For two masks define the composition residual:

`I(A,B)`
`= d_(A union B) - d_A - d_B`.

If the two perturbations compose independently:

`I=0`.

## 4. Separated result

For disjoint radius-1 masks:

Environment composition residual:

`||I_sep|| = 0.0143505824237412`

Relative residual:

`0.05271400135067`.

The downstream same-H continuity readout gives:

`||I_sep^H|| = 1.139314328543643e-06`

relative:

`0.03178164031835917`.

So separated localized stresses are **not exactly additive** in the complete
reconstructed ecology.

This is important.

The nonadditivity cannot come from the direct `D_C` layer, because E049 proved that
layer is linear.

It must arise in the reconstructed state-dependent/global ecology:
candidate weighting, normalization, recoverability scoring, persistent imprinting,
or their composition.

## 5. Overlap result

For overlapping radius-2 masks:

Environment composition residual:

`||I_overlap|| = 0.237799509880273`

Relative residual:

`0.7771786736631802`.

Same-H continuity readout residual:

`||I_overlap^H|| = 1.094144171994734e-05`

relative:

`0.294632491281914`.

Thus overlap changes the nonadditive residual, but nonadditivity does **not first turn
on at geometric overlap**.

The reconstruction therefore fails the strongest locality hypothesis:

"separated local stresses compose exactly and interaction begins only on overlap."

## 6. Why this does not invalidate the dark-defect family

The failure is localized to the current reconstructed ecology implementation.

The runner contains explicitly global operations such as:
- `normalize01(...)` over the whole 32^3 domain;
- weighted global R4/R5 recoverability summaries;
- one global pair-edge selection bit.

Those operations can couple separated perturbations without local support contact.

Therefore E050 does not prove that the underlying MK43 source geometry is nonlocal.

It proves that this **particular reconstructed runner is not suitable as a clean
local-interaction witness**.

That is exactly the kind of Clover self-termination result we wanted.

## 7. Preserved result

The exact source-native direct-flow quotient from E049 remains local/additive.

What self-terminates is the attempt to infer physical defect-defect locality from this
global-summary reconstructed H2 ecology.

## 8. Next handle

Park the multi-writer interaction test at this runner layer.

Return to source-level geometry and use the recovered S3/continuity network locality
objects—especially bounded hidden-network patches, admissible nerves, and
maximum-flow/minimum-cut capacity—to ask whether localized dark-defect regions compose
through explicit connecting corridors.

That avoids importing the reconstructed runner's global normalization artifacts.
