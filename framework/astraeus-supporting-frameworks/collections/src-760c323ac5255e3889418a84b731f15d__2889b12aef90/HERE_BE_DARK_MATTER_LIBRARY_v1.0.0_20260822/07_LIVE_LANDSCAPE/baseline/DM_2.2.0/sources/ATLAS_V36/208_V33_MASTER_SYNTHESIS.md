# V33 — Master Synthesis

## Main correction

The v32 primary gate was written schematically as

    T_rho,R(Delta rho_H) ?= 0.

V33 proves that one scalar regional density cannot be the universal input to a spatial field-intensity translation.

The corrected gate is profile-valued:

    Delta bold_rho_H^R
    -> Beta_R
    -> BasinOrg_R
    -> F_TS^B
    -> FieldIntensity_R
    -> C_rho,u
    -> Delta rho_read[u].

## Recovered handle spine

    @relationship
    -> @transition_capacity
    -> @containment_volume
    -> @energy_density
    -> @stress_energy_tensor.

Separately:

    @persistence
    -> @native_unit_of_energy
    -> @general_energy
    -> @stress_energy_tensor.

The first branch is the static/local density branch.
The second is the ordered-history/general-energy branch.

They must not be silently identified.

## New no-go

    scalar average density
    !=
    spatial density profile.

Therefore:

    regional Delta rho_H > 0

proves hidden supported load exists, but does not determine its readable spatial profile.

## New positive result

Under nonnegative local hidden-load contributions,

    regional hidden load > 0
    =>
    Delta bold_rho_H^R != 0.

Thus the native hidden sector already has a nonzero Resolution-level density profile before calibration, provided the chosen Resolution cover contains its support.

## Remaining exact gates

1. Basin-domain gate:
   Is Delta bold_rho_H^R in Dom(Beta_R)?

2. Basin-distinction gate:
   Does the hidden profile alter BasinOrg_R?

3. Time-Shell fidelity gate:
   Does basin distinction survive as field-intensity distinction?

4. Calibration gate:
   Does the readable observer/unit map preserve nonzero intensity distinction?

5. Stress-energy consistency:
   Once a readable density distinction exists, complete T_mn must still satisfy the appropriate total conservation / exchange-current law.

## Geometry lock

    S4 -> S3 -> S2

No extra sphere level is introduced.
