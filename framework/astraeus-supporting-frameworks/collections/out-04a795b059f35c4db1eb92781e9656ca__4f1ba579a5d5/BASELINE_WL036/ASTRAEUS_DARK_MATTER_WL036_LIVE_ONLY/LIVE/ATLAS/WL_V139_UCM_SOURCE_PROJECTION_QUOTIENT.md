# Work-Layer Atlas v139 — UCM Source-Projection Quotient and History Visibility Gate

**Work layer:** WL-015  
**Date:** 2026-08-17  
**Status:** SOURCE-COMPOSED ALGEBRAIC REFORMULATION / NO PARENT PROMOTION

## 1. Why this gate is next

WL-v138 supplies a finite structural witness in which History changes operative hidden-corridor incidence and therefore changes the reduced S2 continuity operator.

Parent Atlas v24 already states the next required sequence:

```text
DeltaLambda != 0
-> full UCM ledger differs in a Pi_read-sensitive component
-> Delta T_U != 0
-> same beta_ext
-> gravity difference.
```

The first arrow is now explicit in the finite work-layer witness. The second must not be replaced by the invalid inference:

```text
changed adjacency input => changed stress-energy output.
```

A projection can have nontrivial fibers. Therefore the correct next object is the **quotient induced by the UCM source projection**.

## 2. UCM ledger object

Use the recovered full UCM coupling ledger schematically as

```text
L_U
=
(O,Chi,A,P,Rred,S,B,corridor,ancestry,residual,...).
```

The source projection is

```text
Pi_U^R := Pi_read^UCM
```

with

```text
T_U^R(L) = Pi_U^R(L).
```

`R` is shown explicitly in the work layer because the ordinary visible reconstruction is Resolution-qualified and comparison conventions must be fixed.

## 3. Source-projection equivalence

Define the UCM source-readout equivalence relation

```text
L0 ~_(U,R) L1
iff
Pi_U^R(L0)=Pi_U^R(L1).
```

Let

```text
K_U^R
=
{(L0,L1) | L0 ~_(U,R) L1}
```

be the projection kernel-equivalence relation in the set/quotient sense.

Do not call this a linear kernel unless an additive linear ledger representation is separately typed.

Define the source quotient

```text
Q_U^R
=
L_U / ~_(U,R).
```

Two ledger states occupy different source classes exactly when the readable UCM stress-energy projection distinguishes them.

## 4. History-induced ledger pair

Let `H0,H1` be the selected control/test Histories and suppose a source-admissible transaction construction yields ledgers

```text
L0 = Ledger_U(H0),
L1 = Ledger_U(H1).
```

The map `Ledger_U` is not yet recovered as one universal source operator. For the current branch it is a typed target relation between the admitted History/corridor transaction and the existing UCM ledger object.

WL-v138 establishes only a finite change in the operative adjacency/corridor structure. Therefore a candidate pair may satisfy

```text
A(L0) != A(L1)
```

while all declared non-History comparison inputs are held fixed.

This proves `L0!=L1` as ledger objects if `A` is a typed ledger coordinate, but **does not prove** their UCM source projections differ.

## 5. Definition — UCM History visibility

Define

```text
Vis_U^R(H0,H1)
=
1
```

iff

```text
[L0]_(U,R) != [L1]_(U,R),
```

or equivalently

```text
Pi_U^R(L0) != Pi_U^R(L1).
```

Otherwise set `Vis_U^R=0`.

This is the source-side analogue of sector visibility in WL-v135/v136.

## 6. Theorem V139-T1 — Source-quotient gate

For any admissible History-induced ledger pair:

```text
Vis_U^R(H0,H1)=1
```

if and only if

```text
Delta T_U^R
:=
T_U^R(L1)-T_U^R(L0)
```

is nonzero in the declared common tensor/readout representation.

### Proof

`Vis_U^R=1` is defined by inequality of the two `Pi_U^R` images. Since `T_U^R=Pi_U^R`, this is exactly inequality of the source tensors. When the codomain admits subtraction, inequality is equivalent to nonzero `Delta T_U^R`. QED.

### Firewall

The quotient/equivalence statement is primary. `Delta T_U` is a downstream additive representation available only because the stress-energy codomain has the required tensor-space structure.

## 7. Theorem V139-T2 — Ordinary-GR dark implication

Assume:

```text
M_R(L0)=M_R(L1),
Vis_U^R(H0,H1)=1,
beta_ext^R(L0)=beta_ext^R(L1),
```

and the deterministic GR solution/readout map is nondegenerate on the selected source distinction:

```text
Gamma(T_U^R(L0),beta_ext)
!=
Gamma(T_U^R(L1),beta_ext).
```

Then

```text
(L0,L1) in D_R.
```

### Proof

The first hypothesis gives equal ordinary matter readout. The source-visibility and nondegeneracy hypotheses give unequal gravity readout under the same external GR data. The parent definition of `D_R` then applies. QED.

## 8. Application to the minimal hidden-corridor witness

WL-v138 gives

```text
E_oper(H0)={e_AC},
E_oper(H1)={e_AC,e_BC},
Lambda0=0,
Lambda1!=0.
```

A source-admissible UCM ledger representation of this pair must at least record the changed adjacency/corridor organization.

The next finite gate is therefore not another Kron calculation. It is:

```text
Are L0 and L1 in the same or different Pi_U^R fibers?
```

### If same fiber

```text
L0 ~_(U,R) L1.
```

Then this exact History-induced adjacency difference is erased by the UCM stress-energy source projection at that Resolution. The energetic branch fails for this pair, though a boundary/topology or other downstream representation branch may remain.

### If different fibers

```text
L0 !~_(U,R) L1.
```

Then the hidden structural difference survives to the UCM source tensor and can enter the source-matched Gate-B/GR chain.

## 9. Source visibility across Resolution

When the UCM source projections themselves form a compatible nested Resolution family, define

```text
Pers_U(H0,H1)
=
{R | Vis_U^R(H0,H1)=1}.
```

The same coarsening argument as WL-v136 makes `Pers_U` upward closed under the nested-filtration hypothesis.

One can then compare emergence thresholds:

```text
R_U^*     source/stress-energy emergence,
R_Q^*     matter/QFT emergence.
```

A source-dark Resolution band exists structurally when

```text
R_U^* < R_Q^*.
```

Physical dark gravity additionally requires the GR nondegeneracy gate.

## 10. Relation to scalar-load no-go

This quotient formulation directly respects V31:

```text
rho_E
```

is only one scalar compression of the UCM ledger and does not determine `Pi_U^R` on general ledger fibers.

The correct source question is whether the **full algebraic/organizational ledger pair** survives the source projection.

## 11. New primary structural target

Define the work-layer source-sensitivity relation

```text
R_HU^R
subseteq
HistoryPair_R x (Q_U^R x Q_U^R)
```

where

```text
(H0,H1; [L0],[L1]) in R_HU^R
```

means the admitted History pair realizes the corresponding UCM source-quotient pair.

For the rotational/shear branch, the highest-value witness is one with

```text
same matter/QFT readout,
[L0]_(U,R) != [L1]_(U,R).
```

This route does not require Helicon horizontal transport to establish a source-side tensor distinction. It still requires downstream Q/action/GR admission.

## 12. Guardrails

- Different UCM ledger inputs do not imply different `Pi_read^UCM` outputs.
- `K_U^R` is an equivalence relation, not automatically a linear kernel.
- `DeltaLambda != 0` does not by itself imply `Delta T_U != 0`.
- `Delta T_U != 0` does not automatically imply observable `Delta g != 0` without the nondegeneracy/GR comparison.
- No scalar source profile is introduced.
- No parent promotion.
