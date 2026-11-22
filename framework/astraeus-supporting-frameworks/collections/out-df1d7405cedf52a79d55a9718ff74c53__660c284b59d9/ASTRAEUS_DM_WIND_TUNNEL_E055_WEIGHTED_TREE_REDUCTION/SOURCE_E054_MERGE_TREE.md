# E054 — History-Invariant Corridor Merge Tree

## 1. Question

E053 recovered seven local History-created defect branches.

E054 asks whether those branches form one coherent higher-level network whose
**combinatorial type** persists across History.

The natural geometry-first object is the superlevel-set merge tree of the normalized
corridor field.

No differential equation, continuum approximation, or fitted threshold is required.

## 2. Leaves

Every nonfresh History state `E1...E16` has exactly eight strict local corridor maxima:

- one global root maximum `R`;
- seven secondary branches `B1...B7`.

The secondary peak coordinates are exactly the E053 branch addresses.

At E1 the root is embedded at:

`(14, 16, 16)`.

From E2 onward the root is:

`(14, 16, 15)`.

So there is a one-voxel formation transient in the root embedding, while the branch
labels remain stable.

## 3. Merge relation

For any two peak addresses `p_i,p_j`, define:

`m(i,j)`
`= max_(paths gamma:i->j) min_(x in gamma) K_hat(x)`.

This is the exact finite widest-path merge level.

Two peaks belong to the same superlevel component at threshold `t` iff:

`m(i,j) >= t`.

Therefore the full pairwise matrix `m(i,j)` determines the finite merge tree.

## 4. Fixed-state merge grammar

For E* the nested superlevel clusters are:

- level `0.6256129848494253` -> `{B2,R}`
- level `0.604379076252503` -> `{B1,B2,R}`
- level `0.5931663789199267` -> `{B1,B2,B3,R}`
- level `0.5048863304589312` -> `{B1,B2,B3,B4,B5,R}`
- level `0.4550326559981976` -> `{B1,B2,B3,B4,B5,B6,R}`
- level `0.3747205868041107` -> `{B1,B2,B3,B4,B5,B6,B7,R}`

The event involving `B4` and `B5` is a genuine equal-level merge in the sampled field:
both attach at the same normalized corridor level.

The topology should therefore be represented with that equal-level branching preserved,
rather than forcing an arbitrary binary ordering.

## 5. History invariance

Remove the numerical merge levels and retain only the nested leaf-subset structure.

For every tested nonfresh state:

`E1,E2,...,E16`

the abstract merge-tree signature is identical to E*:

`True`.

Thus the **combinatorial branch/merge tree is created after the first endogenous
History write and is invariant through the entire tested History orbit**.

The spatial root embedding itself becomes identical to E* from E2 onward:

`True`.

So:
- E1 = formation geometry with the same abstract tree but shifted root location;
- E2 onward = same abstract tree and same peak embedding.

## 6. Weighted tree versus combinatorial tree

History does not alter the branch hierarchy.

It alters the scalar heights carried by the tree:
- peak heights;
- merge/saddle levels.

Those weights relax toward their E* values while the abstract tree stays fixed.

This gives a clean decomposition:

`History state`
`= (merge-tree topology, tree weights)`.

For the nonfresh E043 orbit:

`merge-tree topology = invariant`

while:

`tree weights = relaxing coordinates`.

## 7. Compact hidden-state descriptor

Define:

`T_corr(E)`

as the labeled corridor merge tree.

Let:

`|T_corr|`

denote its combinatorial type and:

`w_E`

the collection of its peak and merge weights.

Then:

`|T_corr(E_k)| = |T_corr(E_1)|`

for every:

`k=1...16`.

The evolving information lives in:

`w_(E_k)`.

This is substantially more compact than replaying the entire History or storing all
32^3 field values when the task is to recover the branch hierarchy.

It is not a complete invariant of the full substrate state.

## 8. Relation to previous results

E044:
the broad normalized field topography does not settle into one class until E6.

E052:
one local throat skeleton is already invariant from E1.

E053:
seven local branch skeletons persist.

E054:
those seven branches form one **History-invariant merge-tree architecture** from E1.

Thus the earliest stable object recovered so far is the combinatorial corridor tree.

The later History evolution primarily changes weights on that fixed tree.

## 9. Dark-sector consequence

The reconstructed hidden History sector is no longer described merely as:
"a field remembers something."

It has a finite geometric architecture:

`fresh null corridor`
-> `History-created branch tree`
-> `weight relaxation on a fixed combinatorial tree`
-> `driven fixed weighted tree`.

That is an internal MK43 substrate result, not a physical dark-matter identification.

## 10. Next handle

Do not make the tree more elaborate for its own sake.

The next useful question is whether the **tree weights themselves collapse to the same
shared relaxation coordinate** already seen in E053 branch strengths.

If the weighted merge tree is approximately:

`fixed combinatorial tree + one scalar History coordinate`

then the hidden History state admits a very compact reduced geometry.

If not, preserve the full weight vector and move on.
