# Determinism and Learning Contract

AI 1.B begins with a deterministic policy implementation. Learned components may later replace ranking or termination strategies only behind the same contracts.

A learned strategy must:

- never alter API truth;
- emit reasons and policy identity;
- permit deterministic replay when configured;
- fall back to deterministic baseline;
- be bounded by the same traversal and security policies;
- pass the same acceptance suite.
