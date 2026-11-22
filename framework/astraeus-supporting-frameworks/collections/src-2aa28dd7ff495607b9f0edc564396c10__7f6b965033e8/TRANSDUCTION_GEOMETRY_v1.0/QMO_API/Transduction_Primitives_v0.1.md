# TRANSDUCTION PRIMITIVES v0.1

Status: PROVISIONAL / MINIMALITY-AUDITED

## P0 — Dependency Category
Symbol: D
Type: Category.
Role: Dependency objects, identity arrows, and composable dependency morphisms.
Dependencies: None.

## P1 — State-Fiber Assignment
Symbol: F
Type: Indexed assignment U -> F(U) over objects U of D.
Role: Local state domain associated with each dependency object.
Dependencies: P0.

## P2 — Chirality / Admissibility Space
Symbol: Omega
Role: Organizational/admissibility domain from which local admissibility constraints may be constructed.
Dependencies: None presently promoted.

## P3 — Resolution Structure
Symbol: R
Role: Distinguishability/readout structure. Resolution equivalence is defined later.
Dependencies: None presently promoted.

## P4 — Bandwidth Structure
Symbol: B
Role: Specifies which formally admissible states/transformations are operationally available.
Dependencies: None presently promoted.

## P5 — Identity Structure
Symbol: Id
Role: Data/criteria required to discuss identity independently of presentation and history.
Dependencies: None presently promoted.

## P6 — History Structure
Symbol: H
Role: Ordered/recursive ancestry or path history.
Dependencies: None presently promoted.

## P7 — Local Transition / Gluing Data
Symbol: G
Role: Local overlap/transition information required to assemble distributed structure globally.
Dependencies: P0, P1.

## Minimality Rule
An object is primitive only if the framework requires it, it is not currently constructed from earlier framework objects, its type can be stated independently, and it does not smuggle later behavioral claims into the foundations.

## Explicit Non-Primitives
Dependency Arrow is a morphism of P0 rather than a separate primitive.
Admissibility Relation, lift families, Connection, Transport, Transduction, Holonomy, Curvature, Persistence, Derivation Paths, Derivation Macros, Trust objects, and Dependency Cones are constructed/defined objects.
