# WL-v173 — Hidden Response Operator / Galaxy Readout

**QMO:** QMO-AST-DM-WL-058  
**Status:** source-registered readout edge; not physical dark matter; no parent promotion.

The API gives the direct chain

`@dm_native_hidden_witness -> @dm_hidden_response_operator -> @galaxy`.

The response operator is the Schur/Kron object

`Lambda_N=L_PP-L_PI L_II^{-1} L_IP`

with `DeltaLambda_H=Lambda_full-Lambda_vis`. DM2.0 directly registers `@dm_hidden_response_operator READS_OUT_AT @galaxy`.

This means the multi-port hidden-network response already has a galaxy-level readout handle inside the Dark Matter API. It does **not** promote the Time-Space `@galaxy` object: API 4.3 still labels that parent handle `indexed-unlinked`.

## Next handle

`@dm_stress_energy_separation_gate`.
