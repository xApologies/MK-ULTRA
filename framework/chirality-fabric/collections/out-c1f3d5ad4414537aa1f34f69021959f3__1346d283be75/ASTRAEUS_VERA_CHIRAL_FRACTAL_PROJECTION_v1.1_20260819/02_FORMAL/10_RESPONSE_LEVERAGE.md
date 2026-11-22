# 10 - Response-Bearing Transverse Information

## General diagnostic

Suppose a state x is decomposed into dominant and a transverse state residue,

`x = x_parallel + r_perp`.

Let a downstream response be y=F(x), and let a reduced model using only x_parallel miss response-energy fraction `E_resp_miss`. Let the state-energy fraction in r_perp be `E_state_res`.

Define the finite diagnostic

`Lambda_res = E_resp_miss / E_state_res`.

A large Lambda means a small state component has disproportionate downstream response relevance.

This is not a universal invariant; it depends on the chosen norms, decomposition, orbit, and response.

## E056 value

E056 reports:

- transverse state-residue weighted-tree energy fraction = `0.00021305963963369479`;
- response energy missed by PC1 = `0.02446705664866089`;
- `Lambda_res = 114.83665649076548`.

Thus a visually/energetically tiny state residue is response-bearing in the controlled E1-E16 orbit.

## Projection interpretation

The fractal package reads this as an identifiability warning: a dominant projection coordinate can preserve order while discarding directions that have large derivative leverage in the response map.

It does **not** identify those residue directions with chirality, holonomy, hidden fractal dimension, or dark matter without further tests.
