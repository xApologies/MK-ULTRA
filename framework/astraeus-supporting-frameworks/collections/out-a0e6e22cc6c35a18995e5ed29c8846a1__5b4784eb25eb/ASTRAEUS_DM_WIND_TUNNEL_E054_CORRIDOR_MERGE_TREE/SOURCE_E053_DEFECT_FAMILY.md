# E053 — Local History-Defect Family

## 1. Question

E052 established one History-created local bottleneck.

E053 asks whether it is exceptional or whether the driven fixed corridor landscape
contains a family of such local topographic defects.

No arbitrary "dominant peak" threshold is introduced.

Instead enumerate **every strict six-neighbor local maximum** of the normalized E048
fixed-state corridor field.

## 2. Fixed-state branch catalog

The fixed corridor landscape contains:

`8` strict local maxima.

One is the global root:

`R = (14, 16, 15)`

with normalized height:

`1`.

The remaining:

`7`

are secondary lobe addresses.

For each secondary maximum `p_j`, define its root-merge strength:

`tau_j`
`= max_(paths gamma:p_j->R) min_(x in gamma) K_hat(x)`.

This is the same geometry-first widest-path quantity used in E049-E052.

Define branch topographic persistence:

`pi_j = K_hat(p_j)-tau_j`.

The seven branches, ranked by `pi_j`, are:

- `B1` peak=(17, 16, 15), peak=0.912248279, tau*=0.604379076, pi=0.307869203
- `B2` peak=(15, 17, 15), peak=0.691478788, tau*=0.625612985, pi=0.065865804
- `B4` peak=(21, 17, 17), peak=0.554762381, tau*=0.504886330, pi=0.049876051
- `B3` peak=(11, 15, 15), peak=0.622227574, tau*=0.593166379, pi=0.029061195
- `B6` peak=(22, 16, 17), peak=0.480666561, tau*=0.455032656, pi=0.025633905
- `B5` peak=(20, 18, 16), peak=0.511328332, tau*=0.504886330, pi=0.006442002
- `B7` peak=(23, 15, 16), peak=0.379267292, tau*=0.374720587, pi=0.004546705

No persistence cutoff is imposed; the two weakest branches are retained rather than
silently discarded.

## 3. Fresh null state

At `E0`:

`corridor_memory = 0`.

Therefore none of these positive-corridor lobe branches exists in the fresh substrate.

They are History-created.

## 4. Family persistence after the first write

Track the same seven secondary peak addresses through `E1...E16`.

Results:

- every secondary address remains a strict local maximum at every nonfresh depth:
  `True`;
- every branch has unit min-cut `1` at its own merge threshold for every nonfresh
  depth:
  `True`;
- every branch's merge threshold relaxes monotonically toward its driven fixed-state
  value:
  `True`.

So **all seven** branches share the same qualitative defect architecture:

`fresh absence`
-> `History-created local maximum`
-> `one-edge merge throat`
-> `persistent branch`
-> `relaxing merge strength`.

This closes the family question in the reconstructed corridor landscape.

## 5. Discrete geometry locks after the earliest transient

At `E1` the global corridor maximum sits one voxel away from its later location:

`R_1 = (14, 16, 16)`.

By `E2` it has moved to:

`R = (14, 16, 15)`

and remains there.

From `E2...E16`:

- all seven maximin paths equal their E* path:
  `True`;
- all seven merge cuts equal their E* merge cut:
  `True`.

Thus the local defect **combinatorics lock by the second History write**.

E1 is a formation transient.

## 6. Shared strength relaxation

The seven discrete branch skeletons are separate, but their merge strengths do not
relax independently.

Form the branch-error matrix:

`epsilon_j(k)=tau_j(k)-tau_j(*)`.

Its first singular direction carries:

`99.9634127947%`

of total squared variation.

The minimum pairwise correlation between branch error sequences is:

`0.995855047757`.

So the seven local branches ride an overwhelmingly common relaxation coordinate while
retaining different fixed merge strengths and different local paths.

This suggests the geometry naturally decomposes into:

`local discrete defect skeletons`
+
`shared environmental relaxation coordinate`.

That statement is numerical for this reconstructed orbit, not a promoted universal
law.

## 7. Local-defect family object

Define branch `j` at History depth `k` by:

`D_j(E_k)`
`= (p_j, P_j, Cut_j, tau_j(k))`

where:
- `p_j` is its local-maximum address;
- `P_j` is its stabilized maximin corridor path;
- `Cut_j` is its one-edge merge cut;
- `tau_j(k)` is the History-dependent merge strength.

For all tested branches:

`(p_j,P_j,Cut_j)`

is fixed from E2 onward, while:

`tau_j(k) -> tau_j(*)`.

Thus the driven corridor supports a **family of local persistent defect skeletons**,
not just the original A-B throat.

## 8. Important boundary

These are local topographic defects of the reconstructed hidden corridor field.

E053 does NOT establish:
- physical dark-matter particles;
- independent gravitational sources;
- canonical numerical `T_run`;
- readable gravity.

It establishes multiplicity and persistence of local substrate geometry.

## 9. Next hunt

The family result makes the next question sharper:

**Do these seven local defect branches form a coherent higher-level network under their
merge relations?**

Construct the finite branch/merge tree of the driven corridor landscape and compare it
against the E043 History orbit.

If the merge tree itself stabilizes after the early transient, it gives a compact
geometry-first state descriptor for the local hidden-defect ecology.
