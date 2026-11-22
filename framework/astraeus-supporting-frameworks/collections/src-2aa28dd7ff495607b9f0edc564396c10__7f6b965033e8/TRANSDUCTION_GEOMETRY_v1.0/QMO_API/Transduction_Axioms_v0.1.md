# TRANSDUCTION AXIOMS v0.1

## A0 — Typed Admissibility
For f: U -> V, Adm_f is contained in F(U) x F(V).

## A1 — Identity Admissibility
For every U in D and x in F(U): Adm_id_U(x,x).

## A2 — Compositional Closure
For composable f: U -> V and g: V -> W:
Adm_f(x,y) and Adm_g(y,z) imply Adm_(g compose f)(x,z).

## Not assumed
- universal lift existence
- universal lift uniqueness
- composite-lift factorization
- fibration/opfibration universal properties
- Resolution or Bandwidth laws inside the admissibility core

## Independence
A0, A1, and A2 currently play distinct typing, identity, and composition roles; no redundancy has been identified.
