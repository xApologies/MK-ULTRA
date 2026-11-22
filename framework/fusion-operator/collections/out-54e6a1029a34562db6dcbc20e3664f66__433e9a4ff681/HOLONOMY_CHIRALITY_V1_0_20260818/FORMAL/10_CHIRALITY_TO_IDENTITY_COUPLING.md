# 10 — Chirality-to-Identity Coupling and Compensation

## 1. Source chain

Recovered D54-D56 provide:

```text
Identity Sensitivity to Chirality
Chirality-to-Identity Coupling [BRACED]
Compensated Holonomy.
```

## 2. Sensitivity relation

Book formalization defines a declared sensitivity predicate

```text
Sens_Id(Def_chi, I)=1
```

when the chirality defect acts on invariants used by the active Identity Witness/classifier.

Sensitivity is scope-dependent.

## 3. Chirality-to-Identity action

When sensitivity holds, define a typed candidate action

```text
A_chi->Id(Hol_chi)
```

on Identity-Witness data.

This is a book formalization of the BRACED source coupling, not a claim that an exact universal operator was recovered.

## 4. Conditional identity breaking

Recovered T7:

If a closed readable loop has nontrivial chirality holonomy, Identity is sensitive to the defect, and no compensating witness action cancels it, then Identity Holonomy is nontrivial.

## 5. Compensation

Multiple component actions may compose to the identity even when individual components are nontrivial.

Book notation:

```text
Hol_Id^tot
 = A_m o ... o A_2 o A_1.
```

Compensation occurs when

```text
Hol_Id^tot ~_Id id
```

while some `A_i !~ id`.

This is the correct algebraic meaning of compensated holonomy; no additive cancellation is assumed unless the codomain supplies additive structure.

## 6. Firewall

```text
nontrivial chirality holonomy
!=
automatic identity breaking.
```

The coupling and compensation conditions are load-bearing.
