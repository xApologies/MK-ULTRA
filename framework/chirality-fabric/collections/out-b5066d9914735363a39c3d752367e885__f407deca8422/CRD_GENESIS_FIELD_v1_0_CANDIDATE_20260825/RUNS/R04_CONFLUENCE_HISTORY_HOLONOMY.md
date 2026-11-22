# R04 — Confluence, History, and CRD Holonomy
**Verdict: PASS**

For Q3, `H^1(Q3;Z2) ~= Z2^5`, giving 32 seam-defect classes.

Unweighted class minimum-frustration distribution: {0: 1, 1: 12, 2: 18, 3: 1}.

Minimum representatives need not be unique, so state convergence and History convergence are distinct. A canonical tie-breaker may choose one endpoint without erasing alternate valid Roads.

Explicit same-endpoint/different-History witness:
- initial residual mask 11, weight 3;
- final residual mask 16, weight 1;
- Road A cluster masks [11,8], cost sequence [3, 2, 1];
- Road B cluster masks [1,2], cost sequence [3, 2, 1].

Strict spontaneous relaxation has no nontrivial cycles. Event-driven CRD can revisit a readout only if constraint events change the sector; History remains nontrivial.

**Exit gate:** PASS.
