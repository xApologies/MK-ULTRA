# E010 Controlled Pipeline Robustness Filter

## Purpose

Filter the E009 exhaustive readout-degenerate state space using explicit Pipeline / ER
guards and test whether hidden distinctions can survive R4-R6 without depending on one
convenient scoring choice.

## Explicit guards used

- T0 topology must not be completely uniform.
- T2 must retain local differentiation (at least one neighboring state contrast).
- R4 candidates are bounded unit-edge local contrasts.
- Source ER destabilization channel must remain zero for an admitted candidate.
- Chirality is read-only.
- State identity / ancestry labels are preserved.
- R5 Bandwidth is finite.
- R6 is not permitted to invent a new corridor.

These are controlled local guards, not a claim that every surviving tile is a complete
physical MK43 manifold.

## R5 scoring family

The source gives R5 the ingredients:
- recoverability;
- chirality/inheritance organization;
- finite Bandwidth;
- strain.

For each R4 candidate edge define:

`score_e = Recoverability_e + w_I * Inherit_e - w_S * Strain_e`

where:

- `Recoverability_e = mean(stabilize, close, normalize)` from the source ER tensor;
- `Inherit_e` is the source ER inherit channel;
- `Strain_e = |state_a-state_b|/2`.

The propagate/redistribute ER channels are constant across this minimal p=1 tile and would
therefore only add a common ranking offset.

The exact formula is a controlled stress family, NOT a promoted canonical R5 equation.

## Deterministic stress grid

- both possible unlabeled ER chirality-index conventions;
- `w_I = {0, 0.5, 1, 2}`;
- `w_S = {0, 0.1, 0.25, 0.5, 1}`;
- Bandwidth corridor counts `B = 1..4`;
- all optimal tied top-B selections are enumerated.

A pair is called tie-independent robust only when the two states have **no common optimal
selected corridor set** under every tested condition.

## Symmetry filter

Pairs related by any of the 48 coordinate symmetries of the 2x2x2 cube are removed before
being counted as nontrivial survivors.

This is intentionally conservative.

## Random stress

The deterministic B=2..4 survivors are additionally tested under 10,000 random weight pairs:

- `w_I ~ Uniform(0,4)`
- `w_S ~ Uniform(0,4)`

for:
- both chirality-index conventions;
- B=2,3,4.

