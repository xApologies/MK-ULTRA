# Implementation

The baseline implementation is deterministic and breadth-first. It applies stable edge ordering, cycle detection, a depth limit, an edge budget, explicit termination handles, frontier recording, and continuation-handle preservation.

It is intentionally machine-facing. Human-language generation belongs to the Library/report path, not this port.
