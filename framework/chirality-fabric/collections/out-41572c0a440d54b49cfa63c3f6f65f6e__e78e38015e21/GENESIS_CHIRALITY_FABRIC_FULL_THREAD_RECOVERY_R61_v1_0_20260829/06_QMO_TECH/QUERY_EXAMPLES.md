# QUERY EXAMPLES

```bash
# Package metadata and row counts
python 07_MACHINE/qmo_api.py info

# One object/equation/QMO by address
python 07_MACHINE/qmo_api.py address @object/chirality_seed
python 07_MACHINE/qmo_api.py address @eq/domain_color_readout
python 07_MACHINE/qmo_api.py address @qmo/native_update_mechanism_r61

# Typed neighborhood
python 07_MACHINE/qmo_api.py neighbors @object/chirality_tile --direction out
python 07_MACHINE/qmo_api.py neighbors @object/chirality_block --direction both

# Search definitions, claims, equations, and debt
python 07_MACHINE/qmo_api.py search "torus"
python 07_MACHINE/qmo_api.py search "Bandwidth two"
python 07_MACHINE/qmo_api.py search "Lambda_HQ"

# Enumerate a ledger
python 07_MACHINE/qmo_api.py list equations
python 07_MACHINE/qmo_api.py list claims
python 07_MACHINE/qmo_api.py list open_debt
python 07_MACHINE/qmo_api.py list sources
```
