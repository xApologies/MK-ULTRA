# R05 Source Excerpt — Transduction Geometry v1.0

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


## D34 — Jointly Separating Recovery Family
A recovery family {rho_i} is Jointly Separating when local equivalence of all recoveries of two global realizations implies Global Equivalence of those realizations.

## D35 — Canonical Quotient Class
For Quotient-Constructible X, QClass(X)=[G_X]_G is the Global Equivalence class of the transition-generated quotient candidate.

## D36 — Quotient-Universal Realization
Status: BRACED.
A realization is Quotient-Universal when every other valid realization admits comparison compatible with the local recovery data and Global Equivalence. Full universal-property formalism is deferred.
