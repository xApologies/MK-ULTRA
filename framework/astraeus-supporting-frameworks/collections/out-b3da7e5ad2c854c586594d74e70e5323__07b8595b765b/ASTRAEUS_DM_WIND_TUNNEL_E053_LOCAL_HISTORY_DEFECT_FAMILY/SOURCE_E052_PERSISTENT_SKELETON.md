# E052 — History-Persistent Local Min-Cut Skeleton

## 1. Question

E051 recovered one bounded A-B corridor skeleton in the final driven state.

E052 asks whether that skeleton is an accident of `E_*`, or whether it is organized by
the endogenous History orbit itself.

Use exactly the same:
- bounded patch;
- A and B addresses;
- six-neighbor adjacency;
- scale-free corridor normalization.

No new thresholds or capacities are fitted.

## 2. Fresh state

At `E0`:

`corridor_memory = 0`.

So there is no positive-support A-B corridor skeleton.

This gives a clean null state.

## 3. First History write creates the skeleton

At `E1`, the local corridor becomes nonzero.

Its normalized widest-path merge threshold is:

`tau_1=0.6069518491234811`.

At that threshold:
- A and B are connected;
- the unit min-cut is exactly `1`;
- the shortest path has `5` edges.

The merge path is:

`[(17, 16, 15), (17, 15, 15), (16, 15, 15), (15, 15, 15), (14, 15, 15), (14, 16, 15)]`.

The unique one-edge bottleneck cut is:

`[((16, 15, 15), (15, 15, 15))]`.

## 4. Exact skeleton persistence across E1...E16

Across every nonfresh History state:

- the merge path is identical: `True`;
- the merge cut edge is identical: `True`;
- the unit min-cut at each state's own merge threshold is always `1`: `True`;
- the unit min-cut at normalized `t=0.60` is always `2`: `True`;
- the unit min-cut at normalized `t=0.58` is always `6`: `True`.

Thus the entire local channel-multiplicity skeleton:

`1 -> 2 -> 6`

appears after the first endogenous History write and persists through the full E043
orbit.

This is much stronger than persistence only at the final fixed state.

## 5. What History changes

History does not change the combinatorial bottleneck skeleton after E1.

It changes the **merge level** carried by that skeleton.

The normalized merge thresholds are:

- `E1`: `0.6069518491234811`
- `E2`: `0.6048584027353938`
- `E3`: `0.6044602372693719`
- `E4`: `0.6043926844540433`
- `E5`: `0.6043814886260889`
- `E6`: `0.6043795587436535`
- `E7`: `0.604379215193767`
- `E8`: `0.6043791225662505`
- `E9`: `0.6043791225662505`
- `E10`: `0.604379076252503`

The sequence is monotone toward the fixed-state value:

`tau_*=0.604379076252503`.

Monotone convergence in the tested orbit:

`True`.

By E10 the stored float representation has reached the final merge value exactly.

So History has two layers here:

1. a discrete local corridor skeleton established immediately;
2. a continuously relaxing merge-strength coordinate on that fixed skeleton.

## 6. Relation to E044 topographic basin

E044's whole-substrate topography changes through:

`T1,T2,T3,T4,T5`

and then enters:

`T6={6,7,8,9,10,11,12,13,14,15,16}`.

But the local A-B min-cut skeleton is already invariant from `E1`.

Therefore the local bottleneck skeleton is a **coarser and earlier invariant** than the
full E044 History-topography class.

This gives a hierarchy:

`fresh null state`
-> `local corridor skeleton appears`
-> `global/topographic transient evolves`
-> `topographic basin stabilizes`
-> `exact amplitude/merge level finishes relaxing`.

## 7. Geometry-first History invariant

Define the local skeleton signature:

`Sigma_AB(E)`
`= (P_merge, K_merge, lambda_0.60, lambda_0.58)`,

where:
- `P_merge` is the projective/undirected maximin path geometry;
- `K_merge` is the one-edge bottleneck cut;
- `lambda_t` is unit edge connectivity at threshold `t`.

For every tested `E_k`, `k>=1`:

`Sigma_AB(E_k)=Sigma_AB(E_1)`.

So `Sigma_AB` is an exact finite combinatorial invariant of the nonfresh E043 History
orbit in this bounded patch.

The scalar merge level `tau_k` is not invariant; it is the relaxing coordinate carried
by that skeleton.

## 8. Dark-sector consequence

The hidden History family now contains a persistent local network skeleton that:
- is absent in the fresh state;
- is created by the first endogenous write;
- remains fixed through all later History depths;
- supports a one-throat -> two-route -> six-route connectivity hierarchy;
- carries a History-dependent merge strength converging to the driven fixed value.

This is still a pre-gravitational substrate result.

## 9. Next handle

The highest-value next question is whether this local skeleton is **portable**.

Take other strong corridor-lobe pairs in the same driven fixed state and test whether
the same pattern occurs:

`History-created persistent bottleneck skeleton + relaxing merge level`.

If it does, we have a family of local defects.

If it does not, this A-B skeleton is a special local feature and should not be
generalized.
