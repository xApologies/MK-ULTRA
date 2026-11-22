# V33 — Time-Shell Density Factorization

## Status

PARTLY RECOVERED TYPE STRUCTURE + NEW DERIVED FACTORIZATION TARGET.

The sources recover:
- native energy density as relationship x transition-capacity / containment-volume;
- energy-density states as structured occupancy in chirality topology in an older basin representation;
- Resolution as distinguishable organization;
- Time-Shell translation: basin organization -> field intensity;
- @energy_density ENTERS @stress_energy_tensor;
- @native_unit_of_energy REALIZES @unit_of_energy.

They do not recover one complete calibrated numerical formula from arbitrary native density profile to measured SI energy density.

## Corrected factorization target

Define the native Resolution profile

    bold_rho_E^R.

Define a partial basin-organization map

    Beta_R :
    Dom(Beta_R) subset DensityProfile_R
    ->
    BasinOrg_R.

It is partial because the archive does not prove that every admissible native density profile has the old chromatic/basin representation.

Define the Time-Shell basin translation

    F_TS^B :
    BasinOrg_R
    ->
    FieldIntensity_R.

Define the final readable calibration / observer realization

    C_rho,u :
    FieldIntensity_R
    ->
    ReadableDensity_u.

Then the density-specific transduction target is

    T_rho,R,u
    =
    C_rho,u o F_TS^B o Beta_R.

The earlier Resolution quotient is understood to have been applied before or inside Beta_R.

## Structural versus calibrated closure

The chain separates two questions.

1. Structural readability:

    Delta bold_rho_H^R
    -> distinct BasinOrg_R
    -> distinct FieldIntensity_R ?

2. Numerical physical calibration:

    FieldIntensity_R
    -> rho_read[u] in declared physical units ?

The first can, in principle, be decided before the second.

## Fidelity target

For two gravitationally admissible density profiles x,y in Dom(Beta_R), define the density-translation fidelity condition:

    Beta_R(x) != Beta_R(y)
    =>
    F_TS^B(Beta_R(x)) != F_TS^B(Beta_R(y)).

This is a TARGET, not yet a recovered theorem.

If fidelity holds and the final calibration is zero-reflecting on the resulting intensity difference, then

    Delta rho_read[u] != 0

and therefore

    Delta T_mn != 0

for that observer.

## Important no-claim

A basin label is not automatically a measured field amplitude.
The numerical formula and calibration remain open.
