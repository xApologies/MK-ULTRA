# E049 — Local Defect Algebra and Corridor Merge Seam

## 1. Question

E048 recovered a nonzero driven substrate fixed state `E_*`.

The next hunt asked whether hidden History defects can behave locally:
separated regions should compose independently, with genuine interaction appearing only
where their substrate/corridor organizations actually couple.

The direct-flow quotient can answer part of this exactly.

## 2. Exact local direct-flow algebra

The source-native continuity map is linear in edge flow:

`D_C : Flow -> Continuity`.

Therefore:

`D_C(phi_A+phi_B)`
`= D_C(phi_A)+D_C(phi_B)`.

Passing to the E042 quotient:

`Flow/ker(D_C)`

preserves addition:

`[phi_A]+[phi_B]=[phi_A+phi_B]`.

If the vertex supports of the two continuity responses are disjoint, then they are
orthogonal in the ordinary finite-array inner product:

`||D_C(phi_A+phi_B)||^2`
`= ||D_C(phi_A)||^2 + ||D_C(phi_B)||^2`.

This is an exact localizable defect algebra at the direct continuity layer.

No calculus is used.

## 3. Important negative result

Overlap does **not** make the direct continuity operator nonlinear.

Even when the two response supports overlap:

`D_C(phi_A+phi_B)`
still equals:
`D_C(phi_A)+D_C(phi_B)`.

So genuine interaction cannot be created by the incidence/divergence map itself.

If two defects influence one another nonadditively, that interaction must enter
upstream or downstream through structures such as:
- state-dependent edge weights `W_N`;
- corridor selection;
- pair-closure ecology;
- admissibility/supportability;
- a later nonlinear projection.

This sharply localizes the next search.

## 4. The actual E_* corridor geometry contains two high-intensity lobes

Normalize the E048 fixed-state corridor field:

`K_hat = K / max(K)`.

At threshold:

`t_seed = 0.85`

the superlevel domain contains two dominant seed components of sizes:

`4` and `4` sites.

Their peak coordinates are:

`A = (17, 16, 15)`

`B = (14, 16, 15)`.

The two high-intensity regions are therefore genuinely separated in the finite
six-neighbor domain.

## 5. Geometry-first merge threshold

For two seed regions, define their topographic coupling level as the widest-path value:

`tau_merge`
`= max_(paths gamma:A->B) min_(x in gamma) K_hat(x)`.

This is the highest superlevel threshold at which a connecting path exists.

It is a maximin path problem on a finite adjacency graph.

No differential geometry or calculus is needed.

Recovered value:

`tau_merge = 0.604379076252503`.

A maximin path contains:

`6` sites.

Its bottleneck/saddle value is:

`0.604379076252503`.

Thus the two high-intensity corridor lobes remain distinct above `tau_merge` and become
one connected corridor organization at and below that level.

This supplies an actual **topographic interaction seam** in the driven fixed state.

## 6. Same-H direct response on the seam

Using the E043 depth-16 same-H continuity response, the merge geometry has:

- `lobe_A_seed_core`: sites=4, mean |DeltaC|=0.00059124891, enrichment=113.53x
- `lobe_B_seed_core`: sites=4, mean |DeltaC|=0.00059017551, enrichment=113.32x
- `maximin_merge_path`: sites=6, mean |DeltaC|=0.00050643717, enrichment=97.242x
- `merge_path_interior_excluding_seed_cores`: sites=2, mean |DeltaC|=0.00033774067, enrichment=64.85x
- `two_cores_plus_merge_path`: sites=10, mean |DeltaC|=0.0005401179, enrichment=103.71x

This does not prove the seam causes the response.

It establishes that the source-derived response can be spatially compared to the
topographic coupling seam without inventing a new field law.

## 7. Correct locality statement

E049 therefore separates two notions that should not be conflated.

### Direct-flow locality

Exact:

`separated quotient defects add independently`.

### Environmental interaction

Not defined by `D_C`.

The fixed-state corridor topography supplies a candidate geometric seam where the
upstream ecology may couple otherwise separated regions.

So the correct next test is not:

"does overlap break linear divergence?"

It cannot.

The correct next test is:

**does the state-dependent History-write map acquire a measurable composition residual
when two localized inputs cross the recovered corridor merge seam?**

That is where nonadditive interaction is allowed to live.

## 8. Boundary

E049 does not yet instantiate two physically independent H2 writers in one box.

It establishes:
- an exact local additive algebra for the direct-flow quotient;
- a real two-lobe corridor topology in `E_*`;
- an exact graph-theoretic merge seam;
- the correct location of any future nonlinear interaction test.

That is enough to advance without fabricating a multi-source runner.
