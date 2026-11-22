# 202 — Static / Dynamic Dark-Source Split

## Status

```text
NEW_DERIVED_SOURCE_TYPING
```

## 1. Reason for the split

Native general energy and local energy density encode different data.

Recovered history energy:

```text
E_MK(H)
=
[Pi(U_n)-Pi(U_0)] / epsilon_MK,

E_MK(H_closed)=0.
```

Recovered local density:

```text
rho_E = R T / V.
```

Therefore a closed or equilibrium history may return to the same endpoint persistence while a persistent relationship network continues to carry positive supported load.

## 2. Exact compatibility example

It is mathematically consistent to have

```text
E_MK(H_closed) = 0
```

and simultaneously

```text
Delta rho_H > 0.
```

Hence

```text
zero net history energy difference
!=
zero static relational load.
```

## 3. Three independent hidden-network witnesses

V32 now tracks the diagnostic packet

```text
W_H
=
(
    Delta rho_H,
    Delta E_H,
    B_H
).
```

where:

```text
Delta rho_H
    = persistent local relationship-capacity load difference;

Delta E_H
    = native general-energy difference for a declared formation/reconfiguration history;

B_H
    = symmetric hidden boundary-response form on relative S2-port states.
```

This packet is a diagnostic compression only. It is not the full UCM ledger and not a stress-energy tensor.

## 4. Branch meanings

```text
STATIC SUPPORT BRANCH
hidden persistent S3 relationships
-> Delta rho_H
-> @energy_density
-> readable density component [transduction open]

DYNAMIC FORMATION / RECONFIGURATION BRANCH
history changes persistence endpoints
-> Delta E_H
-> @general_energy
-> @stress_energy_tensor [registered projection]

RELATIONAL RESPONSE BRANCH
hidden multi-port topology
-> Lambda_H
-> B_H
-> relative S2-port response
-> non-density stress/readout typing [open]
```

## 5. Why this matters

A static dark-network candidate should not be killed merely because its closed-history endpoint energy vanishes.

Likewise, a nonzero formation energy does not by itself establish a persistent equilibrium load.

The three witnesses answer different questions and must not be collapsed.
