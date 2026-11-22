# 120 — Native Energy Role Separation

## Purpose

Follow the fresh 4.3 API energy branch without collapsing distinct mathematical roles.

The critical correction is that the API contains **two different energy constructions**:

1. a history-relative energy functional built from persistence differences; and
2. a local energy-density relation built from Relationship, Transition Capacity, and Containment Volume.

They must not be silently identified.

---

## 1. Recovered persistence functional

The fresh API defines the depth contribution

```text
Pi_d = I_d B_d R_d O_d C_d
```

and total persistence

```text
Pi = SUM_d I_d B_d R_d O_d C_d
```

with

```text
I_d = inheritance
B_d = Bandwidth
R_d = Resolution
O_d = occupancy
C_d = closure
```

Symbol firewall:

```text
C_d here = closure, not chirality.
R_d here = Resolution.
```

This is the scalar persistence functional used by the recovered native-energy construction.

---

## 2. Recovered native energy unit

```text
epsilon_MK = Delta Pi_min
```

or for one primitive admissible persistence transition

```text
epsilon_MK = Pi(U_1) - Pi(U_0).
```

Native normalization:

```text
epsilon_MK = 1.
```

The value `1` fixes the native unit. It does not say every physical energy state equals one.

---

## 3. History-relative general energy

For an admissible history

```text
H : U_0 -> U_1 -> ... -> U_n
```

the API defines

```text
E_MK(H)
=
[Pi(U_n) - Pi(U_0)] / epsilon_MK.
```

In native units:

```text
E_MK(H) = Pi(U_n) - Pi(U_0).
```

Recovered consequences:

```text
E(H_2 o H_1) = E(H_1) + E(H_2)
E(id) = 0
E(H^-1) = -E(H)
E(H_closed) = 0.
```

### Interpretation discipline

`E_MK(H)` is an oriented **history difference**. Therefore

```text
E_MK(H_closed) = 0
```

means that the endpoint persistence difference of a closed history vanishes.

It does **not** imply that every state encountered by the closed history has zero local energetic content.

This distinction is mandatory for dark-matter work.

---

## 4. Recovered local energy density

The same API separately defines

```text
rho_E = Rel * Tcap / V
```

where this document renames source symbols to prevent collisions:

```text
Rel  = Relationship
Tcap = Transition Capacity
V    = Containment Volume.
```

The source writes `R*T/V`; `Rel` is used here because `R` already denotes Resolution elsewhere in the Atlas.

Recovered dependency:

```text
Relationship
-> Transition Capacity
-> Containment Volume
-> Energy Density.
```

### Hard separation

```text
Resolution R_d != Relationship Rel
Bandwidth B_d != Transition Capacity Tcap
```

The framework may later recover a translator between Bandwidth and Transition Capacity, but v15 does not invent one.

---

## 5. Why this matters for dark matter

A closed persistent geometric organization may have

```text
E_MK(H_closed) = 0
```

while still admitting a nonzero local energy-density representation

```text
rho_E != 0.
```

Therefore the dark sector must not be modeled by treating the endpoint-history difference as the static energy stored in a halo/network.

For a stationary or persistent dark configuration, the more relevant recovered energy role is the local/contained relation-and-transition structure represented by `rho_E`, together with whatever total stress-energy realization the API supplies downstream.

---

## 6. Resolution and Bandwidth enter upstream of energy

The persistence scalar contains both

```text
B_d = Bandwidth
R_d = Resolution.
```

Therefore the native energy unit and general history energy inherit explicit dependence on Bandwidth and Resolution through `Pi`.

This does **not** prove that dark matter is Bandwidth or Resolution.

It does establish that an energy-based dark-sector interpretation cannot consistently treat Resolution and Bandwidth as unrelated decorations.

---

## Status

```text
Persistence functional                         RECOVERED
Native energy unit                            RECOVERED
History-relative general energy               RECOVERED
Local energy density                          RECOVERED
Closed-history role separation                V15 DERIVED
Bandwidth = Transition Capacity               REJECTED / NOT RECOVERED
Static dark matter = E_MK(H_closed)            REJECTED
```
