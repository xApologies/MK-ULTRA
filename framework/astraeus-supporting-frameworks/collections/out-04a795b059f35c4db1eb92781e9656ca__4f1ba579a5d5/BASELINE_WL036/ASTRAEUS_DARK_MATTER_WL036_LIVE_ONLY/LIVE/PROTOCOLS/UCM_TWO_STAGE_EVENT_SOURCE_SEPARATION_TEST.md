# AST-DM-WL-P010 — UCM Two-Stage Dynamic-Event / Source-Separation Test

**Work layer:** WL-016  
**Status:** SOURCE-SIDE PAIRWISE TEST — NOT PARENT PROMOTED

## Goal

Test one controlled rotational/shear History pair through the two parent UCM source gates without inventing a global `Pi_U` formula.

## P010-0 — Select controlled History pair

Choose

```text
H0,H1
```

with the same declared ordinary S2 matter/QFT readout and a typed History/corridor distinction.

Prefer a source-native pair; WL-v138 may be used only as a finite structural witness.

## P010-1 — Realize UCM transaction states

Recover/admit

```text
x0,x1 in X_U
```

whose controlled difference is the selected History/corridor organization.

If no transaction realization exists, classify `NO_UCM_TRANSACTION_REALIZATION`.

## P010-2 — Dynamic-event gate

Evaluate/recover

```text
e0=U_dyn(x0),
e1=U_dyn(x1).
```

Classify:

- `DYNAMIC_MERGED` if `e0=e1`;
- `DYNAMIC_SEPARATED` if `e0!=e1`;
- `DYNAMIC_UNTYPED` if either event cannot be recovered.

A `DYNAMIC_MERGED` pair cannot close the UCM energetic source route.

## P010-3 — Optional incidence branch witness

For one fixed target `M`, record

```text
J(M,e0), J(M,e1).
```

If

```text
J(M,e0)=0,
J(M,e1)=1,
Respond(M,e1)!=M,
```

record `INCIDENCE_RESPONSE_SEPARATED` by parent v29.

Do not rename this as stress-energy separation.

## P010-4 — Pairwise source projection

For dynamically separated events test only

```text
P_T(e0), P_T(e1).
```

Classify:

- `SOURCE_MERGED` if equal;
- `SOURCE_SEPARATED` if unequal;
- `SOURCE_PROJECTION_UNTYPED` if the pair cannot be evaluated.

No global injectivity theorem is required.

## P010-5 — Source quotient / tensor witness

If `SOURCE_SEPARATED`, record

```text
[L0]_(U,R) != [L1]_(U,R)
```

and, in the common tensor representation,

```text
Delta T_U^R != 0.
```

This closes only the source-side separation gate.

## P010-6 — Gate-B handoff

Pass the source target into the existing source-matched family

```text
C_Q,T^R(B_res,Delta T_U^R;g)
```

only if a legitimate parent residue-bundle instance and conservation/exchange data exist.

Then apply the rotational refinement separately.

## P010-7 — Physical GR admission

Under fixed `beta_ext`, test the selected source distinction with the declared GR solution/readout map. Require nondegenerate gravity response before calling the pair a physical dark-readout witness.

## Firewalls

```text
finite Kron response != UCM event separation != source-tensor separation != physical dark matter.
```

```text
P_T pairwise separation does not imply global P_T injectivity.
```
