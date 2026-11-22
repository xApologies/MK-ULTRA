# AST-DM-WL-P007 — Sector-Relative Holonomy Visibility / Dark Resolution Window Test

**Work layer:** WL-011  
**Status:** EXECUTABLE STRUCTURAL PROTOCOL CANDIDATE — NOT PARENT PROMOTED

## Goal

Given one admitted formal History/holonomy class, determine the Resolutions at which it is visible to the QFT/matter sector and the GR/gravity sector separately.

## P007-0 — Select the formal pair

Prefer the black-hole anchored local domain:

```text
p_H in S3,
Sigma_H=pi^-1(p_H)~=S2.
```

Choose a closed admissible continuity loop `gamma_H` and formal return transport

```text
h_H=Hol_H(gamma_H).
```

Select `x` and form

```text
x0=x,
x1=h_H.x.
```

Require `h_H!=id` formally.

## P007-1 — Build the modeled Resolution index

Use the declared Resolution family `Res` and compatible coarsening maps. Do not invent a scalar Resolution value if the source uses algebraic quotients/filters.

## P007-2 — QFT/matter visibility profile

For each `R`, record whether

```text
rho_Q,p_H,R(x1)=rho_Q,p_H,R(x0)
```

or not.

Collect

```text
Pers_Q(h_H;x).
```

If only an ordinary matter readout `M_R` is available for the witness, record that separately and state the factorization assumption linking it to the QFT side.

## P007-3 — GR/gravity visibility profile

For each same `R`, record whether

```text
rho_G,p_H,R(x1)=rho_G,p_H,R(x0)
```

or not.

Collect

```text
Pers_G(h_H;x).
```

Do not infer a gravity distinction from the name of a GR handle. Require an admitted representation or downstream nondegenerate gravity readout.

## P007-4 — Dark Resolution Window

Compute set difference

```text
DarkRes(h_H;x)=Pers_G(h_H;x)\Pers_Q(h_H;x).
```

Classify:

- `EMPTY`: no sector-relative dark window in the modeled Resolution family;
- `NONEMPTY_STRUCTURAL`: at least one Resolution merges the History in QFT/matter but resolves it in GR/gravity;
- `PHYSICAL_CANDIDATE`: only after the parent dark-qualification and observational gates also pass.

## P007-5 — Identity/zero firewall

If a formal transport is readout-trivial, record it as readout identity/equivalence.

Do not write additive zero unless a typed additive/linearized difference representation exists.

## P007-6 — Cross-check against Bandwidth Algebra

For any nontrivial formal corridor/history class, verify provenance in `A_B` and its Resolution images. Record whether the class becomes merged, partially merged, or fully distinguishable under each quotient.

## P007-7 — Optional incidence/Kron branch

If the same History class is independently shown to change `E_oper(H)` or corridor incidence, attach WL-v126/v121 response evidence. Do not use the finite dark-window witness itself as proof that History causes incidence change.

## Pass labels

- `P007-H`: formal nontrivial History/holonomy selected.
- `P007-Q`: QFT/matter visibility profile recovered.
- `P007-G`: GR/gravity visibility profile recovered.
- `P007-D`: `DarkRes` nonempty.
- `P007-PHYS`: downstream physical dark qualification passes.
