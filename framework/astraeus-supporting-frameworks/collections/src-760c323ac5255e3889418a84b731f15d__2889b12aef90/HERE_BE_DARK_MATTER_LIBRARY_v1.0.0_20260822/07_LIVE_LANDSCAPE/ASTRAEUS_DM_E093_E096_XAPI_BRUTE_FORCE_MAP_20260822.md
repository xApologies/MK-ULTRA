# Astraeus Dark Matter — E093–E096 API 4.3 × DM 2.2 Brute-Force Map

## Status

**COMPLETED CROSS-API FIXED-POINT MAP — APPEND-ONLY LIVE LANDSCAPE UPDATE**

- API 4.3 source SHA-256: `0010a4de99d78748ede57670b3bca1df6185b7ba8dd0faf266cc3ba1a4ccf752`
- Dark Matter 2.2 source SHA-256: `ee4819595f94a52565ab21c832c902ea4040e315f3f575b203c61e53740ed63a`
- immutable DM rollback baseline mutated: **no**
- API 4.3 mutated: **no**
- physical dark-matter promotion: **no**
- canonical-edge promotion: **no**

## E093 — mount the two APIs as one QMO

`QMO-XAPI-002` mounts the complete API 4.3 handle universe and Dark Matter 2.2 child API as one finite dependency object while preserving source domains and edge types.

```text
API 4.3 handles                     2384
API 4.3 typed edge records          75432
DM 2.2 child objects                38
DM 2.2 open handles                 7
combined unique nodes               2422
combined semantic primitive pairs   6489
```

API 4.3's RP42 index contains a stale embedded `handle_count=2362` while its handle list and the current RP53 release manifest contain `2384` unique handles. The combined landscape uses the current manifest/list value and records the discrepancy rather than silently rewriting the source.

## E094 — brute-force closure

A one-billion-iteration ceiling was allowed:

```text
ceiling             1,000,000,000
iterations used     8
terminal            NO_NEW_STRUCTURE
wave counts         [38, 33, 54, 49, 48, 16, 8, 1, 1]
```

The finite landscape reached fixed point after eight expansion waves, so spending the remaining 999,999,992 iterations would only repeat an unchanged frontier.

The exhaustive all-pairs semantic crawl produced:

```text
primitive pairs                6,489
fixed-point reachability pairs 72,564
closure growth                 11.18x
maximum shortest-path depth    18
DM -> API reachability pairs   4,391
API -> DM reachability pairs   0
```

The zero API→DM count under forward semantic orientation is useful: the child API depends into the parent universe without forcing the parent to acquire definitions from the child.

API 4.3 self-crawl, independently:

```text
semantic primitive pairs       6,399
semantic fixed-point pairs     68,054
growth                         10.64x
max shortest-path depth        18
```

DM 2.2's own source-validated self closure remains:

```text
primitive dependency pairs     315
fixed-point dependency pairs   5769
growth                         18.31x
validation                     PASS 16/16
```

## E095 — the energy-density bridge closes structurally

The combined QMO exposes the direct source-backed corridor:

```text
@dm_resolution_density_profile
    --REALIZES-->
@energy_density
    --ENTERS-->
@stress_energy_tensor
```

This is not an inferred shortcut. Both edges already exist in the mounted APIs.

The longer registered corridor is:

```text
@dm_resolution_density_profile
 -> @energy_density
 -> @stress_energy_tensor
 -> @einstein_field_equation
 -> @gravity
```

The exact relation/provenance records are retained in `QMO-XAPI-002` and the SQLite landscape.

This changes the old open object `@dm_native_density_to_readable_source`. It is no longer one undifferentiated missing bridge. It factors into:

```text
DM Resolution density profile
    -> API 4.3 energy-density object          CLOSED STRUCTURALLY
    -> stress-energy density component        CLOSED STRUCTURALLY
    -> chosen readable observer/calibration   OPEN NUMERIC/TYPING DEBT
```

The existing DM theorem remains intact: one scalar density does **not** reconstruct a whole stress-energy tensor. The corridor only supplies a component route, which is enough for a separation witness if one nonzero component survives readable normalization.

New residual proof debt: **PD-DM-014**.

## E096 — Dark Matter map reranked

The shortest current energy/gravity route is now:

```text
@dm_native_hidden_witness
 -> @dm_resolution_density_profile
 -> @energy_density
 -> @stress_energy_tensor
 -> @einstein_field_equation
 -> @gravity
```

Shortest depths from the finite witness are:

```text
energy density       2
stress-energy        3
gravity              5
```

`PD-DM-012` (the custom Time-Shell gravity-fiber test) is therefore retained as a return lane but is no longer required by the shortest energy-density/Einstein corridor. `PD-DM-003` and `PD-DM-011` are refactored into the much smaller `PD-DM-014` observer/calibration gate.

The APIs did what the combined-QMO method was supposed to do: the bridge was already present; exhaustive closure exposed the factorization without inventing a new mechanism.

## Current frontier

```text
@dm_xapi_density_component_calibration
```

Question:

> For one declared Resolution cell and one fixed normalized readable observer, does the already-registered nonzero hidden energy-density component remain nonzero in the readable stress-energy slot?

Everything before that component calibration is now structurally mapped across the two APIs.
