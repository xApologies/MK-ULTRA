# 138 — R4-R6 Black-Hole Corridor Selector Recovery

## Central closure

V14-V17 carried an open constitutive selector:

```text
R_cont(H;R) -> Phi_H^*.
```

The recovered black-hole archive contains the exact pre-existing architecture needed to type that selector more sharply.

## 1. Black-hole marked neighborhood

Let

```text
N_H^R
```

be the Resolution-qualified black-hole ER/S3 neighborhood represented by the recovered chirality/adjacency field.

Chirality is read-only:

```text
chi_H : V_H -> Chi.
```

Let

```text
A_H
```

be its admissible local adjacency structure.

## 2. R4 — form possibility

The recovered operator model states:

```text
M_R4 = E_corridor(M_R3, chi_read, A_local, ancestry).
```

Define the candidate family

```text
C4_H
:=
Corr_R4(N_H^R; chi_H, A_H, strain, ancestry).
```

R4 may form corridor candidates but may not decide final topology.

## 3. R5 — resolve possibility

The recovered R5 operator is

```text
M_R5 = R_ordered(M_R4, chi_read, B_occ, S_strain, R_rec).
```

Its declared target is the **lowest-strain recoverable constrained topology** under:

```text
chirality
Bandwidth occupancy
strain
recoverability
ancestry.
```

Define

```text
C5_H
:=
Argmin_{C in Recoverable(C4_H)} Strain(C)
```

subject to those recovered guards.

The set-valued form preserves possible ties.

## 4. R6 — stabilize survivability

Recovered R6:

```text
M_R6 = S_survive(M_R5, D_rec, chi_occ, B_occ, ancestry).
```

Define

```text
E_H^surv
:=
Surv_R6(C5_H).
```

Only corridors that retain ancestry, bounded strain, recoverable chirality occupancy, admissible Bandwidth occupancy, damping recovery, and recursive coherence survive.

## 5. R7 — persistent topology

R7 receives the R6-ready ecology and tests persistent bounded oscillatory/recovery behavior.

Define the persistent corridor support

```text
E_H^*
:=
Persist_R7(E_H^surv).
```

## 6. Flow support closure

The constitutive continuity flow may now be restricted to the stabilized support:

```text
supp(Phi_H^*) subseteq E_H^*.
```

Equivalently:

```text
Phi_H^*(e)=0
for e not in E_H^*.
```

This is stronger than the earlier unconstrained `Flow(N)` formulation.

## 7. What is actually solved

```text
R4 candidate-generation type        RECOVERED
R5 selection objective class        RECOVERED
R6 survivability guards             RECOVERED
R7 persistence role                 RECOVERED
support(Phi_H^*) restriction        V18 DERIVED
numeric Phi_H^* on this BH lattice  OPEN
```

The archive does not provide a fully evaluated numerical recoverability/strain functional for every candidate corridor. V18 therefore does not manufacture one.

## Interpretation

The missing flow was never meant to be guessed directly.

The recovered architecture says:

```text
possibility -> constrained resolution -> survivability -> persistence -> flow support.
```

That is Dynamic Closure Recursion applied to the black-hole neighborhood.
