# AI 1.0 → AI 1.B Acceptance Matrix

AI 1.B is complete only when all tests pass.

1. **BRANE manifest validates as AI role** — PASS required.
2. **all common module declarations match BRANE 2.1** — PASS required.
3. **all ten required methods are callable** — PASS required.
4. **dimension model returns exactly five declared coordinates** — PASS required.
5. **request context is isolated** — PASS required.
6. **canonical fingerprint is stable** — PASS required.
7. **health check validates policy assets** — PASS required.
8. **interpret preserves request ID and constraints** — PASS required.
9. **root candidates come only from API** — PASS required.
10. **ambiguous roots return structured ambiguity** — PASS required.
11. **ranking returns every candidate exactly once** — PASS required.
12. **ranking is stable under identical inputs** — PASS required.
13. **ranking reasons are recorded** — PASS required.
14. **decision domain is closed to four values** — PASS required.
15. **termination creates a leaf cluster** — PASS required.
16. **termination creates continuation when enabled** — PASS required.
17. **defer creates frontier entry** — PASS required.
18. **invalid references include evidence** — PASS required.
19. **cycle references do not recurse infinitely** — PASS required.
20. **depth budget is enforced** — PASS required.
21. **node budget is enforced** — PASS required.
22. **edge budget is enforced** — PASS required.
23. **time budget is enforced** — PASS required.
24. **every encountered branch is accounted for** — PASS required.
25. **collapse preserves root and branch ownership** — PASS required.
26. **collapse contains decision provenance** — PASS required.
27. **canonical claims retain provenance** — PASS required.
28. **API fingerprint remains unchanged** — PASS required.
29. **Library fingerprint remains unchanged** — PASS required.
30. **QMO internals are not exposed** — PASS required.
31. **deterministic replay matches fingerprint** — PASS required.
32. **parallel contexts do not leak state** — PASS required.
33. **malformed request fails closed** — PASS required.
34. **API failure returns structured error** — PASS required.
35. **Library failure permits explicit partial result** — PASS required.
36. **learned strategy can fall back deterministically** — PASS required.
37. **module ZIP loads through BRANE 2.1** — PASS required.
38. **end-to-end fixture request succeeds** — PASS required.
39. **artifact ordering is reproducible** — PASS required.
40. **all Alpha requirements map to code and tests** — PASS required.
