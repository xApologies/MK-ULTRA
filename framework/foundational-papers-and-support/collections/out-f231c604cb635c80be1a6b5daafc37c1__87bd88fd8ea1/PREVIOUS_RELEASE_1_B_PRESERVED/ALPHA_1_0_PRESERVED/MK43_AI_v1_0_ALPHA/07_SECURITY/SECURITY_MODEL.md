# Security Model

- Capability-based access only.
- Read-only canonical inputs.
- Derived-only output construction.
- Request-isolated mutable state.
- Bounded recursion, time, nodes, edges, and memory.
- Stable validation before return.
- No dynamic code execution from recovered content.
- No filesystem traversal beyond declared module assets.
- No network access unless BRANE explicitly grants a separately governed capability.
- No persistence of private request content by default.
