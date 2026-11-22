# AST-DM-WL-P012 — Rotation-Adjacency / UCM Telemetry / Density Source Test

**Work layer:** WL-020  
**Status:** PAIRWISE CONDITIONAL SOURCE TEST — NOT PARENT PROMOTED

## Goal

For one controlled pair, test the smallest source route from a rotation-generated adjacency distinction to readable stress-energy separation.

## P012-0 — Pair requirements

Choose `H0,H1` with:

```text
same declared localized matter/QFT readout,
controlled orientation/adjacency difference,
same normalization/observer for density comparison.
```

If no same-readout pair exists, classify `MATTER_PAIR_OPEN` and do not claim a dark witness.

## P012-1 — Scale lift

Require the P011 S3/UCM scale-lift result for the selected adjacency distinction.

If absent: `S3_SCALE_LIFT_BLOCKED`.

## P012-2 — Dynamic event

Recover

```text
e_i=U_dyn(x_i).
```

Require `Sep_dyn=1`.

An incidence branch witness may be used only with the parent v29 conditions.

## P012-3 — Telemetry extraction

Recover

```text
theta_i=Theta_R(e_i).
```

Require the selected relation/corridor/load distinction to survive telemetry extraction.

## P012-4 — Native relational load

If the v17 additive-channel realization is admitted, evaluate the controlled relation contribution

```text
Delta rho_E^R=r_*Tcap_R(e_*)/V_R.
```

Require `r_*>0`, `Tcap_R(e_*)>0`, `V_R>0`.

If `Tcap_R(e_*)=0`, classify `CHANNEL_SATURATED_ZERO_LOAD`.

## P012-5 — Readable density

Test only

```text
T_rho,R(Delta rho_E^R).
```

Classify:

- `DENSITY_PRESERVED` if nonzero;
- `DENSITY_ANNIHILATED` if zero;
- `DENSITY_TRANSDUCTION_UNTYPED` otherwise.

## P012-6 — Stress-energy separation

If `DENSITY_PRESERVED`, invoke the parent v32 conditional theorem and record

```text
Delta T_U^R != 0.
```

This closes pairwise source separation only.

## P012-7 — Gate B / GR

Proceed to source-matched Q/action Gate B and fixed-boundary GR nondegeneracy only after P012-6 passes.
