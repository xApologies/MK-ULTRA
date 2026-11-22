# 57 — HIDDEN \(S^3\) STATE AND RUNTIME TRANSITION CAPACITY

R46 recovers the first sufficiently concrete localized hidden-state family.

The source state is

\[
R_H(t)=(V_t,E_t,w_t,\chi_t,H_t)_R
\]

over a hidden continuity network

\[
G_H^R=(V_H,E_H,w).
\]

This state family explicitly carries:

- vertices;
- relationships;
- weights;
- chirality;
- History;
- Resolution indexing.

## Runtime Transition Capacity

For persistent relationship \(e\), the source supplies

\[
T_{\rm run}(e)
=
\sup_{\Phi\in\mathcal F_{\rm run}(G_*)}\Phi(e),
\]

interpreted as the maximum globally feasible continuity flow supported by that relationship under the active constraints.

## History-support preorder

The source also carries History-support predicates/orderings for testing whether an operative continuation is backed by retained lineage.

## Consequence

The localization problem is not purely geometric. A concrete candidate lift must survive capacity, History-support, projection residue, and Watcher gates.
