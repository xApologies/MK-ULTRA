# 146 — Transition Capacity Typing Correction: Free vs Committed Bandwidth

## Why v19 revisits this

V16 constructed a legitimate Atlas-derived type bridge

```text
Tcap_R^free(x)
=
tau_R(rho_R(Free_B(x)))
```

from **remaining Available Organizational Freedom** to a scalar valuation of still-supported nonidentity transitions.

That bridge proved, by construction,

```text
Free_B(x)=empty
=>
Tcap_R^free(x)=0.
```

The fresh API, however, never states that its canonical handle `@transition_capacity` is specifically this *free-bandwidth* valuation. The canonical API only recovers the chain

```text
@relationship
-> @transition_capacity
-> @containment_volume
-> @energy_density
```

with

```text
rho_E = Relationship * TransitionCapacity / ContainmentVolume.
```

The canonical `@transition_capacity` record has no recovered native formula in the current API crawl.

## Recovered Bandwidth distinction

Bandwidth is **Available Organizational Freedom**. The Bandwidth source also says:

```text
persistent structures consume capacity;
stable organization allocates bandwidth;
saturation means little or no remaining organizational freedom.
```

The Universal Coupling ledger independently records both

```text
bandwidth available
bandwidth demand
bandwidth commitment / occupancy.
```

Therefore the operative model must distinguish at least the following roles:

```text
B_free      = remaining organizational freedom
B_committed = organizational capacity already allocated into persistent support
```

This is a role distinction, not yet an asserted additive equation `B_total=B_free+B_committed`.

## Corrected typing fork

The v16 object remains valid as

```text
Tcap_R^free
=
valuation of still-available transitions.
```

But the canonical API `TransitionCapacity` may instead be, or may include, a capacity associated with already-realized relationships / committed persistent organization.

Therefore:

```text
Tcap_R^API != Tcap_R^free
```

unless an explicit source bridge proves the identification.

## Saturation correction

The valid v16 statement is now read narrowly:

```text
Bandwidth saturation
=>
no additional free nonidentity transitions
=>
Tcap_R^free = 0.
```

It does **not** imply:

```text
stored relational organization = 0
committed support = 0
native energetic load = 0
gravitational readout = 0.
```

This removes a false inference that a strongly constrained or saturated topology must be energetically/gravitationally empty.

## Dark-sector relevance

The historical dark-matter recovery describes the dark sector as highly constrained, load-bearing ER/worldweave geometry. Such a state can consistently have:

```text
low remaining B_free
high persistent relational organization
nonzero UCM source load.
```

Whether its API `TransitionCapacity` is supplied by committed bandwidth, an effective free+committed construction, or another recovered object remains open.

## Status

```text
V16 free-bandwidth valuation                    RETAINED / CONDITIONAL
canonical TransitionCapacity = free valuation   REVOKED AS OPERATIVE ASSUMPTION
free vs committed Bandwidth role split          V19 TYPE CORRECTION
numeric canonical TransitionCapacity            OPEN
```
