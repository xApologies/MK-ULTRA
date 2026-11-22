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


## D15 — Overlap Domain
O_ij is the domain on which local presentations i and j are simultaneously valid and mutually comparable.

## D16 — Transition Map
On O_ij, g_ij is a typed map relating local state presentations across charts/presentations. Universal invertibility is not assumed.

## D17 — Valid Triple Overlap
O_ijk is the domain on which three local presentations and required pairwise transitions coexist.

## D18 — Descent Defect
On O_ijk:
D_ijk = g_ij compose g_jk compose g_ki.
This is a typed composite, not automatically a scalar or failure.

## D19 — Descent Equivalence
~_D is the declared equivalence under which transition composites count as the same gluing/descent result.

## D20 — Transition-Compatible State Family
A local family {x_i} is transition-compatible when x_i ~_D g_ij(x_j) on each declared valid overlap.

## D21 — Descent-Compatible Local Family
A transition-compatible local family is descent-compatible when pairwise transition relations remain coherent on every valid triple overlap relative to ~_D. This does not assert existence of a global glued object.


## D22 — Global Realization Object
For a descent-compatible local family X, a Global Realization Object G(X) is a candidate global carrier whose local recoveries reproduce X up to declared equivalences. Existence is not guaranteed by definition.

## D23 — Gluing / Realization Operator
Glue is a partial operator from descent-compatible local families to global realizations.

## D24 — Global Equivalence
~_G is the declared equivalence under which global realizations count as the same global object.

## D25 — Gluing Witness
W_G(X,G) is recoverable witness data certifying that global realization G realizes local family X under the declared formal rules.

## D26 — Realizable Local Family
Realizable(X) iff there exists G with a valid gluing witness W_G(X,G).

## D27 — Global Realization Class
[G]_G is the equivalence class of G under ~_G. RealClass(X) is the set of global realization classes realized by valid witnesses for X.


## D28 — Realization-Complete Scope
A scope S is Realization-Complete when every descent-compatible local family admitted by S possesses at least one valid global realization witness.

## D29 — Realization-Separated Scope
A scope S is Realization-Separated when any two valid global realizations of the same descent-compatible local family are equivalent under Global Equivalence ~_G.


## D30 — Controlled Cover
A local cover is Controlled when all required overlaps and triple overlaps are represented, required transition maps are available, and the gluing order is finite or otherwise well-founded.

## D31 — Quotient-Constructible Local Family
A descent-compatible local family is Quotient-Constructible when the disjoint local carrier admits a transition-generated equivalence relation whose quotient belongs to the allowed Global Realization class.

## D32 — Recovery-Compatible Quotient
A quotient-constructed global candidate is Recovery-Compatible when its local recovery maps reproduce the local family up to the declared Descent Equivalence.

## D33 — Witness-Closed Realization Class
A realization class is Witness-Closed when every quotient-constructed candidate satisfying the declared recovery conditions admits a valid Gluing Witness.
