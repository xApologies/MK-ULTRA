# 183 — Adjacency / Corridor Incidence Sensitivity of UCM Dynamics

## Status

```text
SOURCE-NORMALIZED BRANCH THEOREM / v29
Does not yet prove a Mode-0 dark-matter source.
```

## 1. Recovered receiving-manifold branch

The Universal Coupling recovery gives the receiving update in the form

```text
if not intersects(
    target.admissible_topology,
    coupling_event.resolution.corridor
):
    return target

updated_target = target.respond(...)
return updated_target
```

This is already an explicit topology-sensitive branch condition.

## 2. Incidence indicator

For target manifold `M` and resolved coupling event `e`, define

```text
J(M,e)
=
1  if Topology(M) intersects Corridor(e),
0  otherwise.
```

Define the receiving response map

```text
R_U(M,e)
=
M,                     if J(M,e)=0,
Respond(M,e),           if J(M,e)=1.
```

The `Respond` symbol abbreviates the recovered source response with the target's chirality, Bandwidth, ancestry, and resolved topology data.

## 3. V29-T2 — Incidence branch-separation theorem

Suppose two admissible events `e0,e1` are compared against the same target `M` and satisfy

```text
J(M,e0)=0,
J(M,e1)=1,
Respond(M,e1) != M.
```

Then

```text
R_U(M,e0) != R_U(M,e1).
```

### Proof

From `J(M,e0)=0`, the recovered branch gives

```text
R_U(M,e0)=M.
```

From `J(M,e1)=1`,

```text
R_U(M,e1)=Respond(M,e1).
```

The hypothesis `Respond(M,e1)!=M` therefore gives the result. QED.

## 4. What this proves

The UCM dynamics are not structurally required to be blind to adjacency/corridor incidence.

Topology can select a different branch of the recovered receiving update.

This is stronger than merely observing that `A` appears as an argument of a source projection.

It is an explicit conditional mechanism:

```text
hidden corridor changes intersection class
+
nontrivial response
->
different UCM dynamical response.
```

## 5. Independent nonidentity evidence

The Runtime Environment record independently states the transaction

```text
M -> ER
ER -> ER
ER -> M
```

and reports that the environment modifies local manifold admissibility and closure behavior. The stress tests also report adjacency reinforcement, selected/stabilized corridors, and topology-reactive response.

Therefore the recovered runtime does contain nontrivial response behavior somewhere in its tested domain; `Respond` is not merely required to be the identity map everywhere.

## 6. Critical scope boundary

The prior runtime witness is **not** a Mode-0 S3 dark-network witness.

V29 still requires, for the dark-sector application, a pair satisfying all of:

```text
same ordinary S2 matter readout,
hidden S3 corridor/incidence distinction,
nontrivial admissible target response,
and event-to-T source separation.
```

Thus the new result closes the *mechanism type* of adjacency sensitivity but not the dark-matter application.

## 7. Minimal hidden-corridor witness

A sufficient witness has the form

```text
M_R(x0)=M_R(x1),
J(M,e0)=0,
J(M,e1)=1,
Respond(M,e1)!=M,
P_T(e0)!=P_T(e1).
```

The first and last conditions remain the hard dark-sector/source gates.

## 8. Status

```text
intersection branch                         RECOVERED
incidence indicator                         V29 DERIVED
branch-separation theorem                    V29 PROVED
Respond globally identity                    REJECTED BY RUNTIME WITNESS
Mode-0 same-readout incidence pair           OPEN
Mode-0 nontrivial target response            OPEN
coupling-event -> stress-energy separation   OPEN
```
