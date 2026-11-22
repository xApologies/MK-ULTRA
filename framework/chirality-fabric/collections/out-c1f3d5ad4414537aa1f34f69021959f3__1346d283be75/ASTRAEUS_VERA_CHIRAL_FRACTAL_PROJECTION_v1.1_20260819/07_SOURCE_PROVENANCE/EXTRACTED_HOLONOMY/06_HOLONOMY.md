# 06 — Holonomy

## 1. Closed loop

Let `gamma:U->U` be a closed admissible dependency path. The connection holonomy is the returned transport action

```text
Hol_Conn(gamma)=P_gamma^Conn:F(U)->F(U).
```

For a particular state `x`, the loop defect is

```text
K(gamma;x)=Def(Hol_Conn(gamma)(x),x).
```

## 2. Holonomy monoid versus group

Because inverse transports are not universally assumed, the native collection of loop actions is at minimum a **holonomy monoid** under composition.

If, on a declared subdomain, every selected loop transport is invertible, that subdomain admits a holonomy group.

This book never assumes group structure globally without the invertibility hypothesis.

## 3. Triviality is equivalence-relative

A loop may satisfy

```text
Hol_Conn(gamma)(x) ~ x
```

under one equivalence while remaining distinguishable under a finer one.

Therefore holonomy triviality must always declare its comparison scope.

## 4. Component holonomies

The Unified Transduction Object stores component records including:

```text
transport holonomy
chirality holonomy
Identity holonomy.
```

Nontriviality of one component does not force nontriviality of the total Identity action.

## 5. Holonomy signature

Book formalization: for a History path `h`, define a typed signature

```text
Sig_Hol(h)
 = (src,tgt,[h],Hol_Conn,Hol_chi,Hol_Id,scope,provenance).
```

This packages, but does not identify, the different loop effects.

## 6. Observational holonomy

Resolution may project a formal holonomy record:

```text
h_R=rho_R(h).
```

A formal nontrivial loop can therefore become observationally trivial when the quotient collapses its distinguishing action.
