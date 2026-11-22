# Work-Layer Atlas v140 — UCM Two-Stage Dynamic-Event / Source-Separation Gate

**Work layer:** WL-016  
**Date:** 2026-08-17  
**Status:** SOURCE-COMPOSED TYPE REDUCTION / NO PARENT PROMOTION

## 1. Why this move

WL-v138 constructed a finite History-conditioned hidden-corridor witness with

```text
H0 -> E_oper(H0)={e_AC}       -> Lambda0=0,
H1 -> E_oper(H1)={e_AC,e_BC} -> Lambda1!=0.
```

WL-v139 then identified the correct source-level question:

```text
Does the corresponding UCM ledger pair survive Pi_read^UCM?
```

Dark Matter API 2.2 already contains a finer source factorization that localizes this question into two distinct gates.

Parent Atlas v29 defines

```text
U_dyn : X_U partial-> E_U
```

for the resolved Universal Coupling dynamic event and

```text
P_T : E_U partial-> T_read
```

for the readable source projection, with

```text
Pi_U = P_T o U_dyn
```

on the common admissible domain.

Therefore one does not need a global closed formula for `Pi_U` to test one History pair. One needs one admitted pair and two pairwise separation certificates.

## 2. History-conditioned transaction pair

Let

```text
x0,x1 in X_U
```

be UCM transaction states representing the selected control/test Histories

```text
H0,H1.
```

Require all deliberately controlled non-History comparison data to be held fixed.

Define

```text
e0 := U_dyn(x0),
e1 := U_dyn(x1)
```

when both dynamic events exist.

The work-layer finite network witness does **not** by itself establish these source transaction states. This remains a realization step.

## 3. Gate D — dynamic-event survival

Define the pairwise dynamic-event separation predicate

```text
Sep_dyn(x0,x1)=1
iff
U_dyn(x0) != U_dyn(x1).
```

If

```text
Sep_dyn=0,
```

then the upstream History/corridor distinction has been compressed before the readable source map is reached, and this pair cannot produce a UCM source distinction.

Parent v29 already distinguishes this as **dynamic blindness**.

### Incidence-specific sufficient witness

Parent v29 also gives the topology-sensitive receiving branch. For one fixed target `M`, define

```text
J(M,e)=1 iff Topology(M) intersects Corridor(e).
```

If

```text
J(M,e0)=0,
J(M,e1)=1,
Respond(M,e1) != M,
```

then the recovered receiving response differs:

```text
R_U(M,e0) != R_U(M,e1).
```

This is a source-backed finite witness that the UCM dynamics need not be blind to a corridor-incidence change. It is not yet the event-to-stress-energy separation.

## 4. Gate T — readable-source survival

For a dynamically separated pair define

```text
Sep_T(e0,e1)=1
iff
P_T(e0) != P_T(e1).
```

This is the **pairwise source-separation certificate**.

It is deliberately weaker than demanding that `P_T` be globally injective.

Only the selected two-event restriction matters:

```text
P_T |_{ {e0,e1} }.
```

A successful source witness requires this restriction to distinguish the pair.

## 5. Theorem V140-T1 — exact two-stage source criterion

On the common admissible domain,

```text
Pi_U(x0) != Pi_U(x1)
```

if and only if

```text
P_T(U_dyn(x0)) != P_T(U_dyn(x1)).
```

Consequently:

1. if `U_dyn(x0)=U_dyn(x1)`, source separation is impossible for the pair;
2. if `U_dyn(x0)!=U_dyn(x1)` but `P_T(e0)=P_T(e1)`, the distinction is dynamically real but source-projection-compressed;
3. if `U_dyn(x0)!=U_dyn(x1)` and `P_T(e0)!=P_T(e1)`, the UCM source tensors differ.

### Proof

The parent factorization is

```text
Pi_U=P_T o U_dyn.
```

Substitution gives the displayed equivalence. The three cases are the corresponding equality/inequality cases. QED.

## 6. Theorem V140-T2 — local certificate is sufficient; global P_T is unnecessary

Suppose the selected pair has admitted events `e0,e1` and

```text
Sep_T(e0,e1)=1.
```

Then

```text
T_U(x0) != T_U(x1)
```

for that pair, regardless of whether `P_T` is injective, many-to-one, or otherwise unresolved elsewhere in `E_U`.

### Proof

`T_U=Pi_U=P_T o U_dyn` on the common domain. Pairwise inequality of the two `P_T` values is exactly pairwise inequality of the readable UCM source tensors. No statement about any third event is required. QED.

## 7. Relation to WL-v138/v139

The current structural chain is now:

```text
rotational/shear History pair
-> History-conditioned operative corridor mask          [work-layer source-backed factorization]
-> finite hidden-network / Kron response difference     [WL-v138 witness]
-> source UCM transaction realization x0,x1             [OPEN]
-> Sep_dyn                                              [OPEN for galaxy pair]
-> Sep_T                                                [OPEN]
-> UCM source quotient separation                       [WL-v139]
-> Delta T_U != 0                                       [if Sep_T passes]
-> source-matched Q/action Gate B                        [OPEN]
-> fixed-beta/nondegenerate GR response                 [OPEN]
-> physical dark readout                                [OPEN].
```

The first two levels prove structural model-class nonemptiness. The two new source gates identify exactly where the parent UCM can still erase the distinction.

## 8. Resolution-indexed version

For compatible Resolution-qualified UCM maps define

```text
Sep_dyn^R(H0,H1)
```

and

```text
Sep_T^R(H0,H1).
```

Then the UCM source-visibility profile from WL-v139 is

```text
Pers_U(H0,H1)
=
{
  R
  |
  Sep_T^R(U_dyn^R(x0),U_dyn^R(x1))=1
}.
```

Dynamic-event visibility may be tracked separately as

```text
Pers_dyn(H0,H1)
=
{
  R
  |
  U_dyn^R(x0) != U_dyn^R(x1)
}.
```

Necessarily, on the common domain,

```text
Pers_U subseteq Pers_dyn
```

because a readable-source distinction cannot survive if the dynamic event already merged the pair.

This is a clean order/readout relation and introduces no scalar Resolution profile.

## 9. Gate-B consequence

When `Sep_T=1`, define in the common tensor convention

```text
Delta T_U^R
=
T_U^R(x1)-T_U^R(x0)
!=0.
```

This gives a legitimate source target for the parent source-matched Gate-B family

```text
C_Q,T^R(B_res,Delta T_U^R;g)
```

subject to the existing residue-bundle instance, conservation/exchange, action-selection, and rotational-refinement requirements.

This does not solve Gate B; it prevents Gate B from being asked before the source tensor difference exists.

## 10. Highest-value next witness

Do **not** attempt to reconstruct a universal formula for `P_T`.

Search for one source-admitted galactic/rotational transaction pair satisfying:

```text
same ordinary S2 matter/QFT readout,
History/shear-conditioned corridor difference,
Sep_dyn=1,
Sep_T=1.
```

The pairwise `Sep_T` certificate is the smallest source object that closes the current source-side energetic gate.

## 11. Guardrails

- `DeltaLambda != 0` does not imply `Sep_dyn=1` until the finite witness is realized inside the UCM transaction domain.
- `Sep_dyn=1` does not imply `Sep_T=1`.
- changed receiving response does not automatically imply changed stress-energy source.
- `P_T` need not be globally injective.
- no scalar density or halo profile is introduced.
- no Helicon horizontal transport is required for this source-side reduction.
- no parent promotion.

## 12. Source anchors

Read-only parent/source anchors:

- Dark Matter API 2.2 Atlas v29 `182_V29_UCM_DYNAMIC_EVENT_FACTORIZATION.md`.
- Dark Matter API 2.2 Atlas v29 `183_V29_ADJACENCY_INCIDENCE_SENSITIVITY.md`.
- Dark Matter API 2.2 Atlas v28 `178_V28_UCM_SOURCE_FIBER.md`.
- Dark Matter API 2.2 v17 `132_UCM_FULL_VS_VISIBLE_SOURCE_PROJECTION.md`.
