# Work-Layer Atlas v136 — Monotone Sector Visibility and the Anchored Dark Resolution Band

**Work layer:** WL-012  
**Date:** 2026-08-17  
**Status:** CONDITIONAL FINITE/ORDER-THEORETIC WORK-LAYER THEOREM / NO PARENT PROMOTION

## 1. Motivation

WL-v135 defined the sector-relative dark Resolution window

```text
DarkRes(h;x) = Pers_G(h;x) \ Pers_Q(h;x).
```

The finite three-Resolution witness showed that this set can be nonempty. The formal Resolution Landscape contains a stronger monotonicity statement that constrains the shape of the set whenever the sector readouts themselves form compatible nested Resolution systems.

This is an algebra/readout theorem. No scalar Resolution profile, density profile, differential equation, or fitted halo law is introduced.

## 2. Common formal feature

Let `h` be one nontrivial formal History/holonomy class acting on a formal state `x`, with

```text
x0 = x,
x1 = h.x,
h != id.
```

For the galactic specialization, use the recovered marked continuity address

```text
p_H in S3,
Sigma_H = pi^(-1)(p_H) ~= S2,
```

and let `h=h_H=Hol_H(gamma_H)` for a closed admissible S3 loop based at `p_H`.

## 3. Sector-specific Resolution systems

Let `Res` be a monotone Resolution index with

```text
R_i <= R_j
```

meaning `R_j` is at least as fine as `R_i`.

For each sector `s in {Q,G}`, assume a compatible Resolution presentation

```text
rho_s,R : X -> X_s^R
```

with coarsening maps

```text
q^s_ji : X_s^Rj -> X_s^Ri
```

such that

```text
rho_s,Ri = q^s_ji o rho_s,Rj
```

whenever `R_i <= R_j`.

This is the sector-specific analogue of the formal Resolution Landscape compatibility law. It is an explicit hypothesis: Chirality Landscape Version 1 supplies separate local QFT and GR readouts, while the Resolution Landscape supplies the generic nested-coarsening architecture; their complete sectorwise integration is not yet parent canon.

## 4. Sector visibility sets

Define

```text
Pers_s(h;x)
=
{
  R in Res
  |
  rho_s,R(x1) != rho_s,R(x0)
}.
```

Thus:

```text
Pers_Q = QFT/matter-side visibility,
Pers_G = GR/gravity-side visibility.
```

## 5. Theorem V136-T1 — Sector visibility is upward closed

Under the compatible nested-coarsening hypothesis, for either sector `s`,

```text
R_i in Pers_s(h;x)
and R_i <= R_j
=>
R_j in Pers_s(h;x).
```

### Proof

Suppose `rho_s,Ri(x0) != rho_s,Ri(x1)` but, contrary to the claim,

```text
rho_s,Rj(x0) = rho_s,Rj(x1).
```

Apply the coarsening map `q^s_ji` to both sides. Compatibility gives

```text
rho_s,Ri(x0) = rho_s,Ri(x1),
```

contradicting visibility at `R_i`. QED.

### Interpretation

A distinction already visible at a coarse Resolution cannot disappear solely by moving to a finer presentation in a nested quotient system. Fine Resolution can split an observational class; it cannot re-merge a distinction that was already separated below it.

## 6. Emergence thresholds

When `Res` is a finite or well-ordered monotone chain and `Pers_s` is nonempty, define

```text
R_s^* = min Pers_s(h;x).
```

Then V136-T1 gives

```text
Pers_s(h;x) = {R in Res | R >= R_s^*}
```

within the modeled chain, subject to the declared sector system.

Call:

```text
R_Q^* = QFT/matter emergence Resolution,
R_G^* = GR/gravity emergence Resolution.
```

## 7. Theorem V136-T2 — Dark Resolution Band

Assume both emergence thresholds exist on one monotone chain. Then

```text
DarkRes(h;x)
=
Pers_G(h;x) \ Pers_Q(h;x)
```

has the form

```text
DarkRes(h;x)
=
{R | R_G^* <= R < R_Q^*}
```

when

```text
R_G^* < R_Q^*.
```

If

```text
R_G^* >= R_Q^*,
```

then no Resolution in the modeled chain can belong to the sector-relative dark band.

### Proof

By V136-T1 each persistence set is an upward-closed tail beginning at its emergence threshold. Their set difference is therefore exactly the tail beginning at `R_G^*` truncated immediately before the QFT/matter tail begins. QED.

## 8. Extended cases

### QFT/matter never resolves the History

If

```text
Pers_Q = empty
```

but `Pers_G` is nonempty, then

```text
DarkRes = Pers_G.
```

The modeled dark band extends through every Resolution at which gravity/GR retains the distinction.

### Gravity/GR never resolves the History

If

```text
Pers_G = empty,
```

then

```text
DarkRes = empty.
```

The selected History class cannot witness the dark-readout defect through this sector pair.

### Non-monotone Resolution systems

If the sector readouts do not form nested compatible quotient systems, the interval/band theorem does not apply. Retain the general set-valued definition from v135.

## 9. Black-hole anchored specialization

For the current galactic candidate, `p_H` supplies a common marked S3 continuity address and `Sigma_H` the associated localized S2 domain.

Bandwidth Algebra and the Resolution Landscape allow one formal Bandwidth/History object to persist through many Resolution presentations. Therefore the black-hole anchor does not require a scalar `B(R)` profile.

The anchored algebraic object is instead:

```text
(A_B, h_H, p_H, {rho_R(h_H)}, {q_ji}).
```

The dark band records **where one anchored formal History distinction becomes readable to gravity before it becomes readable to the ordinary QFT/matter sector**.

This is a precise work-layer realization of the statement:

```text
Resolution is the domain in which the dark distinction appears.
```

It does not identify Resolution with dark matter.

## 10. Relation to the v135 witness

The three-Resolution witness

```text
R_c < R_d < R_f
```

with

```text
Pers_Q = {R_f},
Pers_G = {R_d,R_f}
```

is now recognized as the minimal finite instance of V136-T2:

```text
R_G^* = R_d,
R_Q^* = R_f,
DarkRes = {R_d}.
```

## 11. Physical admission remains separate

V136 constrains the Resolution geometry of sector visibility. It does not prove an astronomical dark-matter realization.

Physical admission still requires at least:

```text
1. one source-native rotational/S3 History class h_H;
2. a physically admitted QFT/matter readout family;
3. a physically admitted GR/gravity readout family;
4. same ordinary matter readout in the dark band;
5. nondegenerate gravity response;
6. downstream observational comparison.
```

## 12. Guardrails

- `R_G^*` and `R_Q^*` are order thresholds, not scalar field values.
- No numerical Resolution calibration is inferred.
- The theorem is conditional on nested sector-specific coarsening maps.
- The black hole is a marked anchor/specialization, not required by the abstract theorem.
- `h_R=id` at a readout means observational triviality/equivalence, not formal destruction.
- Composition identity is not additive zero.
- No parent promotion.
