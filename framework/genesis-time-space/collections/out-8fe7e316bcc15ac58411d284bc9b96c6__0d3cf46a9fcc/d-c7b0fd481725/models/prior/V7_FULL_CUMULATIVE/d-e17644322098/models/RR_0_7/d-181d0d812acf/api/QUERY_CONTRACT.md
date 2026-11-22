# Query Contract — v0.6.0

The JSON registries and canonical live model are authoritative recovery surfaces. SQLite is a rebuildable query index.

Core object queries remain stable. Additional Rainbow Road surfaces:

- `domain` — current recursive domain contract;
- `closure-contract` — semantic closure and self-promotion rules;
- `certificates` — closure certificates;
- `perturbations` — registered sandbox probes;
- `runtime-state` — current Road presentation/history state.

Canonical mutation is permitted only by:

1. certified internal closure under the current domain contract; or
2. explicit audited domain extension.

Perturbation branches never overwrite canon automatically.


## Structural command namespace / Dependency Landscape

- `@help` — canonical command discovery surface; returns every structural command implemented by the API.
- `@help dependency_landscape` — explain the landscape constructor.
- `/help` remains a deprecated compatibility alias only.
- `dependency-landscape INPUT...` — transiently construct a landscape from QMO/Landscape inputs.
- `landscape @handle` — query a registered landscape QMO.
- `landscapes` — list registered landscapes.
- `landscape-history [@handle]` — read landscape History.

Registered Dependency Landscapes are QMOs. They retain their own provenance, History, Resolution context, and Bandwidth context. QMO↔QMO, QMO↔Landscape, and Landscape↔Landscape composition is permitted. Inclusion in a landscape never promotes the truth/status of a member QMO.


## @ command namespace

The first token of an invocation may resolve against `api/COMMAND_REGISTRY.json`. Commands are structural implementations, not mathematical objects by default. QMO addresses are resolved in argument position. Thus:

- `@help` is a command and is **not** a QMO;
- `@qmo @resolution` invokes the QMO-query command on the mathematical object `@resolution`;
- `@dependency_landscape @a @b --register --handle @L` invokes a structural constructor whose backing constructor object is also registered as the QMO `@dependency_landscape`; the output `@L` is a QMO.

The `@` glyph is therefore an address syntax shared by separate typed registries; registry/type and invocation position determine whether an address is a command or a mathematical object.
