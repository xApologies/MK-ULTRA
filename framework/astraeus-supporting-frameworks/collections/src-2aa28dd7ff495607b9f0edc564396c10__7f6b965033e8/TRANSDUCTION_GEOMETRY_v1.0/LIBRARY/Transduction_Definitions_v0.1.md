# TRANSDUCTION DEFINITIONS v0.1

## D0 — Admissibility Relation
For f: U -> V, x in F(U), y in F(V), Adm_f(x,y) means y is an admissible continuation/realization of x along f according to the Chirality/Admissibility structure and applicable transition data.

## D1 — Formal Lift Family
LiftSet(f,x) = { y in F(V) | Adm_f(x,y) }.

## D2 — Operative Lift Family
LiftSet_B(f,x) is the subset of LiftSet(f,x) operationally available under Bandwidth B. Exact Bandwidth selection law remains pending.

## D3 — Resolution Equivalence
y1 ~_R y2 iff R(y1) = R(y2).

## D4 — Resolution-Quotiented Lift Family
LiftSet^R(f,x) = LiftSet(f,x) / ~_R.

## D5 — Connection Selection
Conn_B(f,x) is a selected element of LiftSet_B(f,x) when the operative family is nonempty. This definition does not assert existence, uniqueness, smoothness, or coherence.

## D6 — Transport
Connection-selected state motion along a dependency arrow under a fixed declared dependency/base context. Transport != Transduction.

## D7 — Transduction
Admissible typed transformation that may change dependency/base context.

## D8 — Holonomy Diagnostic
Closed-loop connection-selected transport comparison/class. Holonomy is diagnostic and not a complete identity of the global fabric.

## D9 — Transduction Curvature
Typed coherence defect obtained by comparing admissible same-endpoint transport paths. Curvature != Connection and Curvature != Descent Defect.

## D10 — Lift Defect
Typed dispositions: NO_LIFT, UNIQUE_LIFT, MULTIPLE_LIFTS, TYPE_MISMATCH, ADMISSIBILITY_FAILURE, COMPOSITION_FAILURE, UNRESOLVED. MULTIPLE_LIFTS is branching information, not automatically failure.

## D11 — Persistence
Recoverability of declared Identity structure across admissible History/transition evolution. Precise persistence law remains for later formalization.

## D12 — Chirality Fabric
Status: STRONG_CANDIDATE_DEFINITION.
Distributed chirality/admissibility organization represented through local admissibility data plus transition/gluing structure.

## D13 — Derivation Path
Delta = (Nodes, Operators, Claims, Scope, Provenance, CompilerWitness).

## D14 — Derivation Macro
Typed reusable abstraction of a compiler-valid Derivation Path whose full expansion remains recoverable. Macro != Theorem.
