# 178 — UCM Source-Fiber Criterion

## Status

New derived readout mathematics using the recovered Universal Coupling readable-source schema.

No new coupling law is invented here.

## 1. Recovered UCM input organization

The recovered Universal Coupling mechanism uses a readable source projection of the schematic form

```text
T_U
=
Pi_U(
  O,
  Chi,
  A,
  P,
  Rred,
  S,
  B
).
```

where the source recovery assigns the roles

```text
O     occupancy
Chi   chirality organization
A     adjacency / topology
P     persistence
Rred  redistribution
S     strain / survivability
B     Bandwidth allocation.
```

The exact final operator typing and physical calibration of `Pi_U` remain open, but the source projection architecture is recovered.

## 2. Full and ordinary-visible UCM states

Let

```text
u_full
=
(O_full,Chi_full,A_full,P_full,Rred_full,S_full,B_full)
```

and

```text
u_vis
=
(O_vis,Chi_vis,A_vis,P_vis,Rred_vis,S_vis,B_vis)
```

be the full and ordinary-visible source records corresponding to the same declared S2 observational situation.

Define

```text
T_full = Pi_U(u_full)
T_vis  = Pi_U(u_vis).
```

## 3. UCM projection fibers

Define

```text
u ~_U v
iff
Pi_U(u)=Pi_U(v).
```

This is the source-projection equivalence relation induced by the recovered UCM readout.

### V28-T1 — UCM hidden-source criterion

A hidden S3 distinction is source-visible to the downstream gravity sector precisely when

```text
u_full not~_U u_vis,
```

i.e.

```text
Pi_U(u_full) != Pi_U(u_vis).
```

No linearity assumption is required.

## 4. Matter-readout factorization test

Let

```text
M_R
```

be the ordinary S2 matter/radiation readout.

UCM factors through ordinary matter readout iff

```text
M_R(u)=M_R(v)
=>
Pi_U(u)=Pi_U(v).
```

If this implication holds on the relevant domain, then no hidden S3 organization inside one ordinary matter-readout class can generate a distinct UCM source.

If the implication fails, define the UCM dark-source defect

```text
D_U^R
=
{
 (u,v)
 |
 M_R(u)=M_R(v),
 Pi_U(u)!=Pi_U(v)
}.
```

This is a source-level specialization of the earlier general dark-readout factorization criterion.

## 5. What listing an input does not prove

The recovered UCM schema lists adjacency, persistence, redistribution, strain/survivability, and Bandwidth as source-projection inputs.

That is not yet a proof that `Pi_U` is nonconstant in each argument.

For adjacency sensitivity, for example, a witness must exist:

```text
u and v differ in admissible adjacency data
with all controlled comparison data fixed,

and

Pi_U(u) != Pi_U(v).
```

Analogous witnesses are required for persistence, redistribution, strain, and Bandwidth.

This prevents the project from inferring physical sensitivity merely from an argument label.

## Status

```text
UCM source-projection architecture      RECOVERED
UCM projection-fiber relation           V28 DERIVED
matter-readout factorization criterion  V28 DERIVED
component sensitivity witnesses         OPEN
hidden S3 -> nonzero T_U                OPEN UNTIL WITNESS
```
