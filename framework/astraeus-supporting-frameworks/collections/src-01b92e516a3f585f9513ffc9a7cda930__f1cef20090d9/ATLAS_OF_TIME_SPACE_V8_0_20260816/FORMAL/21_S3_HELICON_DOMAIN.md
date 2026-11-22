# 21 — Candidate S³ Helicon Domain

## Status

**MAJOR ATLAS CANDIDATE / CROSSROAD.**

This file does not assert that `S3 = Helicon`. It formalizes the stronger candidate that the **primary global domain of coherent Helicon organization is the S³ continuity base** of five-dimensional Time-Space, while localized `S2` spacetime projections receive Helicon realizations through transduction.

## Existing Time-Space scaffold

The standard Atlas branch is

```text
S2  -->  T5  --pi-->  S3
```

with

```text
T5_std ~= S3 x S2
```

under the standard smooth oriented `SO(3)` sphere-bundle hypotheses.

For `p in S3`, the localized readable spacetime projection is

```text
Sigma_p = pi^(-1)(p) ~= S2.
```

## Helicon carrier bundle

Introduce a Helicon bundle

```text
pi_H : E_H -> S3
```

with typical fiber `H_p`, the admissible coherent-mode space over continuity address `p`.

A global Helicon configuration is a section

```text
H_3 in Gamma_adm(E_H).
```

The section is not required to be a conventional particle field. It represents coherent restructuring / ordering modes carried by the S3 continuity domain.

## Chirality orientation input

Let

```text
pi_chi3 : E_chi3 -> S3
chi_3 in Gamma_adm(E_chi3).
```

The recovered API relation

```text
@chirality --CONTRIBUTES_TO--> @helicon_orientation
```

motivates a typed orientation morphism

```text
O_H : E_chi3 -> Orient(E_H)
```

or, more generally, an admissible map

```text
J_H : E_chi3 x E_H -> E_H
```

that constrains the local Helicon orientation class without identifying chirality with Helicon.

## Helicon connection

Introduce a connection

```text
nabla^H
```

on `E_H`. Along a path `gamma:I->S3`, coherent transport satisfies

```text
nabla^H_(gamma_dot) H = 0
```

when no local transduction/source term is active.

The induced transport is

```text
P_gamma^H : H_alpha -> H_beta.
```

## Chirality-Helicon compatibility

The minimal compatibility requirement is that chirality transport and Helicon orientation transport commute on the admitted sector:

```text
O_H(P_gamma^chi chi_alpha)
~=
P_gamma^Orient(O_H(chi_alpha)).
```

A stronger intertwining target is

```text
P_gamma^H J_H(chi,H)
=
J_H(P_gamma^chi chi, P_gamma^H H)
```

whenever all terms are defined.

## Spectral structure

The recovered Phase III Helicon spectral law is retained as a local/induced spectral representation:

```text
L_H(H_a) = lambda_a H_a.
```

In the S3-domain candidate, `L_H` becomes a family of local operators or one globally defined operator compatible with the S3 connection:

```text
L_H,p : H_p -> H_p
```

or

```text
L_H : Gamma_adm(E_H) -> Gamma_adm(E_H).
```

A required consistency condition is

```text
P_gamma^H L_H,alpha = L_H,beta P_gamma^H
```

for exact spectral transport, or a controlled defect operator when the spectrum changes along the corridor.

## Atlas interpretation

```text
S3 continuity
    carries
Helicon coherent organization
    constrained by
chirality orientation/history
    and transduces into
local S2 Helicon / ER / QFT / GR representations.
```

This is the first precise statement of the `S3 Helicon Domain` candidate.
