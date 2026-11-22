# Dark Matter API 2.2 — Bidirectional Cross-Crawl Mathematical Map

## Status

```text
Time-Space -> Dark Matter cross-crawl:
COMPLETE

Dark Matter -> Time-Space cross-crawl:
COMPLETE

Cross-links promoted:
SOURCE/TYPE AUDITED ONLY

Physical dark-matter identification:
OPEN
```

## Active geometry

```text
S4 -> S3 -> S2
```

# 1. Bidirectional interface

The current Dark Matter API touches the Time-Space API directly through:

```text
27 parent handles
```

Starting from those Time-Space interface handles and crawling the child
graph reaches:

```text
35 / 38 dark objects
```

So the current dark API is fully attached to the parent mathematical
universe; no child object is an isolated island.

# 2. Reverse crawl: Dark Matter -> full Time-Space

The reverse expansion finds parent structure that the smaller Dark Matter
parent subgraph had never imported:

```text
depth 1: 17 novel parent handles
depth 2: 101 novel parent handles
depth 3: 279 novel parent handles
```

The crawl intentionally does NOT import all of them.

Only four source/type-audited handles are promoted in 2.2:

```text
@native_constraint_closure
@total_action
@diffeomorphism_invariance
@particle_readable_organization
```

# 3. Hidden-state embedding is now a constrained family

API 4.3 supplies the native constraint algebra:

```text
C_a |Psi_phys> = 0

[C_a,C_b]_U
=
sum_c f_ab^c C_c

U ker(C)
subseteq
ker(C)

C_read Pi_T
=
Pi_T C_native.
```

Combine it with the existing hidden bundle embedding laws:

```text
pi_E o iota_H
=
j_T o pi_H

I o iota_H
=
iota_H o I_H.
```

Define:

```text
Emb_H,phys^R
=
{
 iota_H:E_H^R -> E
 |
 pi_E o iota_H = j_T o pi_H,
 I o iota_H = iota_H o I_H,
 iota_H(E_H^R) subseteq ker(C)
}.
```

This family is mathematically defined.

The remaining open question is now:

```text
Emb_H,phys^R != empty ?
```

and, if nonempty, which embedding is physically realized.

# 4. Hidden action selection is now a covariant family

The reverse crawl connected the existing action problem to:

```text
@matter_action
@metric_variation
@total_action
@diffeomorphism_invariance
@noether_identity
```

Define:

```text
S_H^cov(Q_H,g)
=
{
 S_H in S_adm(Q_H,g)
 |
 S_tot = S_EH + S_vis + S_H
 is compatible with the parent total-action /
 diffeomorphism-invariance architecture
}.
```

For a selected member:

```text
T_H_mn
=
-(2/sqrt(-g))
delta S_H / delta g^(mn).
```

So `@dm_metric_action_selection` is no longer an unconstrained search over
arbitrary hidden actions. It is a selection problem inside the covariant
family.

# 5. The parent API exposes the matter/gravity readout split explicitly

API 4.3 already preserves the ER-Foam branch split:

```text
ER Foam
|
|-- localized knot branch
|   -> stable ER-foam knot
|   -> localized persistent topology
|   -> particle-readable organization
|   -> matter-readable organization
|   -> matter / fields
|
`-- propagating mode branch
    -> helicon
    -> graviton
    -> Time-Shell translation
    -> gravity
```

The branches later reconverge at gravity-matter closure.

This gives a source-backed structural realization of the already-defined
dark readout defect.

Define the ER-restricted comparison:

```text
D_R^ER
=
{
 (x,y)
 |
 M_R(x)=M_R(y),
 G_R(x)!=G_R(y),
 x,y belong to the same admitted ER-origin comparison class
}.
```

This does not prove nonemptiness.

It does explain why "matter-unreadable but gravity-readable" is a lawful
branch question inside the parent architecture rather than an ad hoc extra
readout.

# 6. Nonemptiness got a new construction strategy

The reverse crawl also exposes the GR initial-value cluster:

```text
@initial_data_set
@hamiltonian_constraint
@momentum_constraint
@cauchy_problem
```

This is retained as:

```text
QMO-XAPI-CAND-001
```

rather than promoted into the API.

The candidate strategy is:

```text
construct one matched full/visible initial-data witness
satisfying:
  - Dark-Matter Qualification Locus conditions
  - parent GR initial-data constraints
then test continuation through the parent Cauchy/evolution architecture.
```

The API graph supports this strategy; the cross-crawl does not yet prove
such initial data exist.

# 7. Cross-crawl fixed point after promotion

```text
DM objects: 38
Open handles: 7

Composable nodes: 215
Primitive dependency pairs: 315
Fixed-point dependency pairs: 5769
Closure growth: 18.31x
Dark Matter child SCCs: 0
```

# 8. Current three primary questions

The cross-crawl did not manufacture fake closures. It made the three
remaining questions smaller:

```text
A. @dm_hidden_state_embedding

   Is Emb_H,phys^R nonempty?
   If yes, select/identify iota_H.

B. @dm_metric_action_selection

   Which member/equivalence class of S_H^cov(Q_H,g)
   is realized?

C. @dm_dark_matter_qualification_nonempty

   Can one witness in DM_R be constructed?
   QMO-XAPI-CAND-001 supplies an initial-data strategy.
```

That is the current frontier.
