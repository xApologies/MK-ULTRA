# A06 — Vera Safety Gate

Decision order:
1. User override active? → PRESERVE/TRANSPARENCY.
2. Event unknown or low confidence? → PRESERVE.
3. Protected/safety-critical event? → PRESERVE required semantics; transformation only if canonical rule explicitly allows and preservation proof passes.
4. Rule missing? → PRESERVE.
5. Rule prohibited? → PRESERVE.
6. Device capability insufficient? → PRESERVE.
7. Output safety bounds violated? → PRESERVE.
8. Otherwise approve requested bounded operation.
