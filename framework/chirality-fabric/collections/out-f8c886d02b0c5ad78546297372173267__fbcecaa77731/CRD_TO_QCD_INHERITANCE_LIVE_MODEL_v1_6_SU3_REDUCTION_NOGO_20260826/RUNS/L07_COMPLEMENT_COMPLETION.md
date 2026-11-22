# L07 — Complement Completion / SU(3) Algebra

**Verdict:** PASS AS DOWNSTREAM TARGET ALGEBRA / CRD REALIZATION CONDITIONAL

The L06 dimension no-go is retained.

For the standard `su(2)+u(1)` embedding in `su(3)`, take

`g0=span_R{T1,T2,T3,T8}` and `m=span_R{T4,T5,T6,T7}`.

Direct symbolic verification gives:

- `[g0,g0] subset g0`;
- `[g0,m] subset m`;
- `[m,m] subset g0`.

Thus the missing complement has exactly four real dimensions and is isomorphic to a complex doublet.

A second derivation uses the six directed `K3` edge operators. Choosing any one inverse pair as the embedded `su(2)` root pair leaves two inverse pairs, i.e. four real off-diagonal directions, as `m_RH`. All three pair choices are Weyl-equivalent.

**What is not yet proved:** that Road/Helicon/Q data supply the required rank-two complex sector or equivalent six-edge operator representation with the required algebra. Therefore L07 is not a physical QCD pass.
