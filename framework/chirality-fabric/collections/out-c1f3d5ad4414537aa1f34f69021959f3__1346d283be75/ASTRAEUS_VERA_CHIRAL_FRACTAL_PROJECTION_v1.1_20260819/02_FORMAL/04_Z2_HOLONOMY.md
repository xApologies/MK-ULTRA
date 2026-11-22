# 04 - Z2 Chirality Holonomy on Finite Graphs

## 1. Signed transport

Let a connected graph G=(V,E) carry an edge sign `sigma_e in {+1,-1}`. For an oriented path gamma, define

`H(gamma) = product_{e in gamma} sigma_e`.

For Z2 signs, orientation reversal does not change the product because `sigma_e^{-1}=sigma_e`.

## 2. Vertex gauge transformation

Choose `g_v in {+1,-1}` at every vertex. Transform edge states by

`sigma_uv' = g_u sigma_uv g_v`.

For a closed loop, all vertex factors cancel, so

`H'(gamma)=H(gamma)`.

Loop products are therefore gauge-invariant.

## 3. Cycle rank

For a connected finite graph,

`beta_1 = |E|-|V|+1`

is the number of independent graph cycles.

The Z2 edge-sign states modulo vertex gauge contain `2^{beta_1}` gauge classes. A cycle-basis holonomy signature supplies beta_1 independent bits and recovers the class.

## 4. CFP-001 K4 enumeration

K4 has 4 vertices and 6 edges, so beta_1=3.

- edge-sign assignments: 2^6 = 64;
- effective vertex-gauge transformations: 2^(4-1)=8;
- gauge classes: 64/8 = 8 = 2^3;
- independent cycle-holonomy signatures: 8.

The package enumerates all 64 assignments and verifies this exactly.

## 5. MK43 interpretation boundary

This finite construction supplies a rigorous toy model for path-dependent information hidden from an unsigned geometric projection. It does not prove that the source-valid MK43 chirality transport is Z2, that a physical ER connection is this sign model, or that dark matter is holonomy.
