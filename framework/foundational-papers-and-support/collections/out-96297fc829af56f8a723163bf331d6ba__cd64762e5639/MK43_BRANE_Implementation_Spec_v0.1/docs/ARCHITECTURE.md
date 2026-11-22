# BRANE Architecture

## Public architecture

The runtime sees BRANE as one queryable module.

```text
Runtime ── request ──> BRANE
Runtime <─ artifact ── BRANE
```

The runtime does not receive references to internal components. It cannot call the API directly, browse the library, inspect the collapse intelligence, or query the QMO workspace.

## Internal architecture

```text
BRANE
├── Public Gateway
├── Module Loader
├── Collapse Intelligence
├── API Adapter
├── Canonical API Package
├── QMO Workspace
├── Library Adapter
├── Knowledge Library Package
├── Report Assembler
├── Validator
└── Artifact Egress
```

## Module collaboration around the QMO

```text
                  Collapse Intelligence
                         │
                         ▼
Canonical API ─────── Ephemeral QMO ─────── Knowledge Library
                         │
                         ▼
                   Report Assembler
```

The QMO is a private transient object. It coordinates API structure with library recovery requirements. It is not returned unless a future diagnostic mode explicitly permits it.

## Ownership

### Runtime

- load and unload a BRANE package;
- send requests;
- receive status and artifacts;
- enforce transport limits;
- preserve artifact bytes exactly as returned.

### BRANE gateway

- authenticate or validate requests;
- normalize request envelope;
- assign request identity;
- invoke internal workflow;
- return artifact and receipt.

### Collapse Intelligence

- resolve natural-language domain intent into API crawl intent;
- choose finite traversal realization;
- order branches and layers;
- mark terminal leaf clusters and continuation handles;
- request library recovery coverage;
- never modify canonical mathematics.

### Canonical API

- own handles, definitions, equations, typed edges, aliases, provenance, and recursive graph recovery;
- construct the structural QMO representation requested by Collapse Intelligence;
- remain independently replaceable and versioned.

### Knowledge Library

- resolve handles into typed knowledge chunks;
- preserve exact equations and source provenance;
- supply models, analogies, explanations, and report-ready prose;
- remain independently replaceable and versioned.

### Report Assembler

- preserve all recovered content;
- arrange content according to QMO traversal order and requested report mode;
- generate Markdown or other supported formats;
- never silently drop unresolved or oversized sections.
