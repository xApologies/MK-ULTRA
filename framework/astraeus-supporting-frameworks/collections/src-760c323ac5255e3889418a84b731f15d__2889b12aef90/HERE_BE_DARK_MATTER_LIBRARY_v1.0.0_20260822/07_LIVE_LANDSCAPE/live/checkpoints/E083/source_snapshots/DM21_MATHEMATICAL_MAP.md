# Dark Matter API 2.1 — Brute-Force Mathematical Map

## Status

```text
Dark-matter qualification:
DEFINED

Existence of a qualifying realization:
OPEN

Empirical identification with physical dark matter:
OPEN
```

## Active geometry

```text
S4 -> S3 -> S2
```

## 1. Hidden relational state

The TOME's relational-state normalization motivates the typed hidden bundle:

```text
pi_H : E_H^R -> T_H

R_H(t)
=
(V_t,E_t,w_t,chi_t,H_t)_R.
```

The current primary open object is the bundle embedding:

```text
iota_H : E_H^R -> E
```

with required commuting conditions:

```text
pi_E o iota_H
=
j_T o pi_H

I o iota_H
=
iota_H o I_H.
```

The existence of this embedding is not proved.

## 2. Formal persistence

Once iota_H exists, the framework already supplies the exact test:

```text
exists n >= 1 :
I^n(iota_H(x))
~
iota_H(x).
```

Define:

```text
Xi_H^R
=
{
  iota_H(x)
  |
  iota_H(x) in Xi
}
subseteq Xi.
```

## 3. Boundary contact — CLOSED IN 2.1

No arbitrary incidence map is needed.

Define:

```text
B_H^R
=
cl_E(Xi_H^R)
intersect
dXi.
```

If:

```text
B_H^R = empty
```

the residue route fails at Resolution R.

If nonempty, the global Time-Space boundary and projection machinery
already apply to the relevant contact support.

## 4. Projection residue

```text
Pi : dXi -> M

F_p
=
Inv(Pi^(-1)(p))

pi_F : F -> M.
```

Full/visible residue-bundle non-isomorphism is a sufficient field-bundle
survival witness.

## 5. Q completion — CLOSED IN 2.1

Define the conditional completion family:

```text
C_Q(B)
=
{
 Q=(M,F,pi_F,h,nabla,R_nabla,Gamma,A,P,S)
 |
 Q extends B and satisfies the current field axioms
}.
```

For residue bundles produced under the complete current Time-Space
formal assumptions:

```text
C_Q(B) != empty
```

by the Quantum Field Deduction and Field-Level Handoff theorems.

Moreover:

```text
B_full not_isomorphic B_vis
```

implies that a Q-isomorphism preserving the residue-bundle constituent
cannot identify the corresponding Q objects.

Thus the hidden distinction, once it survives to the residue bundle,
cannot be lost merely because the standard Q structure is appended.

## 6. Stress-energy — NARROWED TO ONE PRIMARY OPEN OBJECT

The former arbitrary map:

```text
Residue -> T_mn
```

is removed.

The only legitimate downstream construction is conditional on a
metric-coupled action/constitutive sector.

Open:

```text
@dm_metric_action_selection
```

Then define the realization family:

```text
T_H(Q,g)
=
{
 -(2/sqrt(-g)) delta S_H / delta g^(mu nu)
 |
 S_H in S_adm(Q_H,g)
}.
```

The family is mathematically typed.

The physical selection of S_H is not yet closed.

## 7. Conservation — CLOSED IN 2.1

Let:

```text
T_full
=
T_vis
+
T_H
```

and impose total conservation:

```text
nabla_mu T_full^(mu nu)
=
0.
```

Define:

```text
J^nu
=
nabla_mu T_vis^(mu nu).
```

Then identically:

```text
nabla_mu T_H^(mu nu)
=
-J^nu.
```

If the visible sector is separately conserved, J=0 and the hidden
sector is separately conserved.

## 8. Dark-matter qualification locus — DEFINED IN 2.1

Let the full and visible constructions be matched under the same
external comparison data.

Define DM_R as the set of pairs (u_full,u_vis) satisfying:

```text
1. full state contains an admissible hidden S3 multi-port organization;
2. formal persistence / boundary-contact / Q-survival gates pass;
3. M_R(u_full) = M_R(u_vis);
4. T_H = T_full - T_vis != 0;
5. g_full != g_vis;
6. Ein(g_full) = kappa T_full;
7. Ein(g_vis)  = kappa T_vis;
8. hidden/visible source balance satisfies the exchange-current identity.
```

This is the exact internal meaning of a qualifying dark-matter
realization in the present architecture.

The remaining existence problem is:

```text
DM_R != empty ?
```

## 9. Primary blockers after brute force

Only three primary blockers remain:

```text
A. @dm_hidden_state_embedding
   Does the hidden S3 relational-state bundle embed into E?

B. @dm_metric_action_selection
   Which metric-coupled action/constitutive sector does the hidden Q
   realization carry?

C. @dm_dark_matter_qualification_nonempty
   Does at least one matched full/visible state satisfy every qualification
   condition?
```

Mode-0 selection, history-to-strength, native-density calibration, and
chromatic representation remain supporting/optional branches rather than
critical-path blockers.
