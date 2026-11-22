# Dark Matter API 2.0 — Mathematical Map

## Active geometry

```text
S4 -> S3 -> S2
```

## Primary formal route

```text
Mode-0 access
  ->
@dm_mode0_network_selection_rule ?
  ->
hidden S3 multi-port network X_H^R
  ->
@dm_hidden_state_embedding
    iota_HE^R : X_H^R ⇀ E
  ->
@dm_formal_persistence_qualification
    exists n>=1 : I^n(iota_HE^R(x)) ~ iota_HE^R(x)
  ->
Xi
  ->
@dm_persistent_boundary_incidence
    R_Xi,dXi^R subseteq Xi x dXi
  ->
dXi
  ->
Pi
  ->
M
  ->
F_p = Inv(Pi^(-1)(p))
  ->
Residue/QFT bundle F
  ->
@dm_field_handoff_from_residue ?
  ->
@dm_residue_to_stress_energy ?
  ->
T_mn
  ->
@dm_hidden_sector_conservation ?
  ->
@dm_energy_gravity_consistency_filter
  ->
S2 gravitational readout
```

## Finite-response branch

```text
w_e = kappa_ij A_ij

W_N = diag(w_e)

L_N = B_N W_N B_N^T

deltaC = -L_N c

Lambda_N
=
L_PP - L_PI L_II^(-1) L_IP

B_H([x],[y])
=
x^T Lambda_H y
```

Runtime capacity is separate:

```text
T_run(e)
=
sup_{Phi in F_run} Phi(e)

T_run(e_ij)
<=
U_ij^+
=
kappa_ij A_ij DeltaC_ij^+
```

The self-crawl correction is:

```text
local response coefficient
!=
runtime capacity ceiling
```

so no definition cycle remains.

## Static hidden-load branch

```text
L_H(U)
=
sum_{e in E_H(U)} r(e) T_run(e)

rho_{H,a}^R
=
L_H(U_a) / V_a

Delta boldrho_H^R
=
(Delta rho_{H,a}^R)_a
```

This profile is not a full stress-energy tensor.

## History branch

```text
S_R(e)
=
invariant-preserving admissible histories supporting e

e <=_H f
iff
S_R(e) subseteq S_R(f)
```

The quantitative history-to-strength map remains:

```text
@dm_history_to_continuity_strength ?
```

## Dark readout condition

```text
D_R
=
{(x,y): M_R(x)=M_R(y), G_R(x)!=G_R(y)}
```

## Exact no-go constraints

```text
free hidden one-port appendage
  -> zero effective port response

pure divergence-free cycle
  -> zero direct deltaC gravitational source

regional scalar density
  -/-> unique spatial density profile

scalar energy density
  -/-> unique full stress-energy tensor
```

No theorem above terminates the multi-port hidden-network branch as a whole.

## API self-closure

Composable nodes:

`192`

Primitive dependency pairs:

`251`

Fixed-point dependency pairs:

`4856`

Closure growth:

`18.40x`

Child nontrivial SCCs after cleanup:

`1`

The direct API remains lean; recursive consequences live in the composed-dependency index.
