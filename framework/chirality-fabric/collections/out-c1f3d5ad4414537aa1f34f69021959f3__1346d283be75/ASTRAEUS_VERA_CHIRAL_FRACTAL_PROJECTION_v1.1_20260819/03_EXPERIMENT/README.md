# CFP-001 Experiment Runner

Run:

```bash
python run_all.py
python test_cfp001.py
```

The experiment has no network dependency and uses deterministic finite constructions.

## Components

1. `finite_histories`: all 4^6 symbolic histories.
2. `cantor_square_profile`: exact finite Cantor-dust coding from two ternary Cantor bits per branch symbol.
3. `triangle_profile` and `circle_profile`: visualization/readout maps of the same histories; not claimed as dimension-preserving theorems.
4. `hidden_chirality`: deterministic hidden +/-1 fiber deliberately ignored by shape readouts.
5. `z2_k4_experiment`: exhaustive 64-state edge-sign enumeration, vertex gauge quotient, three cycle-holonomy bits.
6. `projection_identifiability`: finite 8D rank/nullity experiment showing three shape probes share a 4D kernel; four targeted probes remove it.
7. `hidden_dimension_factorization`: exact C^5 -> C^3 Cantor-product coordinate-projection dimension ledger.
8. `e056_bridge`: reproduces the source E056 response-capture/leverage tables used in the report.

The code does not simulate physical dark matter and does not mutate any source package.
