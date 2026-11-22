# MK43 Collapse Intelligence Port 1.0

This package is the standalone **AI port** for BRANE 1.1. It is loaded into BRANE through the AI port and is not part of BRANE core.

## Public contract

- `compile_request(request)` converts the runtime request into a canonical recovery instruction.
- `realize(graph, request)` collapses a recursive canonical graph into a finite traversal realization.
- `create_port()` returns the port instance declared by `brane_port.json`.

The port may control traversal, branch ordering, termination, frontier recording, and continuation handles. It may not alter canonical API mathematics, handles, or edges.
