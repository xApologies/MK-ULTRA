# E044 History Topography Quotient — Compact Definition

Domain:
`D = 32 x 32 x 32` finite six-neighbor adjacency grid.

Snapshot:
`E=(chi,A_mem,K_mem,P_mem)`.

Normalize each field independently by its infinity norm.

Thresholds:
`T={0.1,...,0.9}`.

For each normalized absolute field, and separately for positive/negative chirality,
form the thresholded induced subgraph and record its connected-component size multiset.

The resulting finite fingerprint is:

`Theta_T(E)`.

Equivalence:
`E ~_top E'` iff `Theta_T(E)=Theta_T(E')`.

Recovered E043 quotient:

`T0 = {0}`
`T1 = {1}`
`T2 = {2}`
`T3 = {3}`
`T4 = {4}`
`T5 = {5}`
`T6 = {6,7,8,9,10,11,12,13,14,15,16}`

Topographic stabilization depth:
`k=6`.

Late-class maximum exact `Delta C` spread:
`7.70934853358e-08`.

Late-class maximum relative spread:
`1.91621835372e-05`.

Interpretation:
`~_top` is a coarse snapshot geometry quotient, not equality of full ER History states.
