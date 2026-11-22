# AST-DM-WL-P002 — Cross-Resolution Rotational Frame / Time-Shell Test

**Status:** WORK-LAYER PROTOCOL  
**Revision:** WL-005  
**Purpose:** Test whether the v128 rotating-galaxy self-corridor can support a nontrivial cross-Resolution rotational frame readout at a black-hole-anchored localized shell without hardcoding a GR frame-dragging result.

## Inputs

1. Marked black-hole continuity address `b_H -> [H]_R -> p_H in S3`.
2. Localized readout family `Sigma_R` associated with the marked address.
3. One formal Bandwidth Algebra `A_B` with compatible Resolution quotients `rho_R` and coarsening maps `q_ji`.
4. `H0`: reference/common-mode self-corridor History.
5. `H1`: persistent nontrivial rotational shear/holonomy self-corridor History.
6. Abstract conserved rotational invariant class `J_*` for `H1`.
7. Matter readout held fixed at each compared Resolution wherever the dark test is attempted.

## Test A — anchor persistence

Require for compatible finer/coarser resolutions:

`r_R'R([H]_(R'))=[H]_R`.

Failure stops the black-hole anchored branch.

## Test B — Bandwidth cross-Resolution provenance

Require:

`rho_Ri = q_ji o rho_Rj`.

Track the same formal rotational element:

`u_R=rho_R(u_J)`.

If the coarse quotient kills the rotational distinction, record that Resolution as outside its persistence profile rather than declaring the formal structure destroyed.

## Test C — local frame representation

Construct or source a typed map:

`varphi_R:A_B^R->Aut(Fr(Sigma_R))`.

No physical frame-dragging claim is permitted before this map is typed.

Define:

`FD_R=varphi_R(u_R)o varphi_R(u_0)^(-1)`.

Record `FD_R=id` or `FD_R!=id`.

## Test D — shear

For neighboring radial/readout subdomains `a,b`, compute finite relative transport:

`Sh_R(a,b)=FD_R(b)oFD_R(a)^(-1)`.

Require at least one nontrivial `Sh_R` for the differential-rotation branch.

## Test E — vorticity/holonomy

For a closed loop `gamma`, compute:

`Vor_R(gamma)=Hol_gamma(FD_R)`.

Record the Resolution persistence profile of nontrivial loop transport.

## Test F — Time-Shell persistence

Test whether the frame-transport section is stable on the localized persistent boundary under the existing Time-Shell Resolution/Bandwidth/persistence conditions.

Do not infer `Sigma_R=TimeShell` merely from being an S2 fiber.

## Test G — dark readout separation

Require the selected hidden-History difference to remain matter-null:

`q_matter,R(DeltaW)=0_matter`.

A rotational frame witness is:

`Phi_FD,R(DeltaW)!=id`.

This closes only an internal frame-non-null witness, not physical dark matter.

## Test H — downstream GR admission

Construct or recover:

`Phi_GR,R:FD_R->accepted rotating-spacetime frame observable`.

The accepted comparison neighborhood may include the local frame/tetrad, ADM shift, Kerr geometry, Komar/black-hole angular momentum, and horizon angular velocity, but no identity may be inferred by name or symbol.

A physical frame-dragging claim requires this bridge plus the ordinary assumptions of the selected GR comparison model.

## Falsifiers / failure conditions

- black-hole marked address fails cross-Resolution compatibility;
- rotational formal element is not supported by the selected Bandwidth Algebra;
- all `u_R` become observationally trivial in the modeled Resolution family;
- no typed local-frame representation exists;
- frame transport is common-mode everywhere (`FD_R=id` or all `Sh_R=id`);
- loop holonomy is trivial at all relevant Resolutions;
- Time-Shell persistence conditions fail;
- matter readout changes, defeating the intended hidden-history comparison;
- downstream GR map produces no accepted rotational-frame response;
- predicted effect is already fully accounted for by the conventional null model with no discriminating residual.

