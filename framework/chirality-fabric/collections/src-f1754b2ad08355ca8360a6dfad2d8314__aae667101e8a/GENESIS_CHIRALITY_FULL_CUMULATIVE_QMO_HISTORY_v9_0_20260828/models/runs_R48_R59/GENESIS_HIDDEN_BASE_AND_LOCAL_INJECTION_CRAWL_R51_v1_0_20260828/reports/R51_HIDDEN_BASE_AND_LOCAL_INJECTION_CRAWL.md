# R51 — HIDDEN BASE + LOCAL INJECTION CRAWL

## Objective

R50 left two branches:

1. recover the hidden-base map `j_T` and determine whether it is injective;
2. recover an already-existing local map that can serve as `s_t:F_t->K_t`.

The mounted Unified/QMO registry was crawled for hidden-base, state-bundle, continuation, inheritance, and embedding objects.

## 1. Hidden-base map status

The source embedding family uses:

`pi_E o iota_H = j_T o pi_H`.

So `j_T` is definitely part of the source-native embedding contract.

However, in the currently recovered registry material, the crawl does **not** expose enough concrete object data to certify the following:

- an explicit standalone definition of `j_T`;
- its domain/codomain beyond the role implied by the commuting diagram;
- injectivity on the relevant hidden support;
- fibers of `j_T`.

Therefore:

`@open/hidden_base_embedding_injectivity`

remains open.

This means R50's cross-fiber separation witness `Sep_t` cannot yet be discarded.

## 2. Search for an existing local map s_t

Several nearby source objects exist around:

- inherited state bundle;
- continuation operator;
- inheritance morphism;
- recursive inheritance;
- hidden-state embedding family.

But the currently recovered source material does **not** provide a local map already satisfying all of:

`F_t -> K_t`

with:

- injectivity;
- image in `ker(C)`;
- base compatibility;
- inheritance equivariance.

In particular, inheritance/continuation morphisms are organizational transport objects, not automatically fiber embeddings into the native constraint kernel.

So no source object can yet be promoted directly to `s_t`.

## 3. Important closure: the search space is narrower

Any viable candidate local map must factor through two filters:

### Filter A — base compatibility
For `x in F_t`:

`pi_E(s_t(x)) = j_T(t)`.

### Filter B — physical kernel
For `x in F_t`:

`C(s_t(x)) = 0`.

Only after these pass do injectivity and inheritance equivariance matter.

So instead of searching all inheritance morphisms, the candidate-map search can be restricted to maps landing in:

`K_t = ker(C) ∩ pi_E^-1(j_T(t))`.

That rules out any continuation object whose codomain is not already constrained to the correct base/kernel sector.

## 4. New forced QMO: candidate-map sieve

Define the candidate-map sieve:

`S_t = { f:F_t->E | pi_E o f = j_T(t), C o f = 0 }`.

Then the physical local injections are:

`S_t^phys = { f in S_t | f injective and I o f = f' o I_H }`

with the obvious fiber-to-fiber target adjustment under inheritance.

This makes the local injection problem an admissibility sieve rather than an unconstrained map search.

## 5. Branch result

The crawl reaches a genuine branch:

### Branch A — recover `j_T`
Without a concrete `j_T`, `K_t` cannot be instantiated and cross-fiber collisions cannot be audited.

### Branch B — populate the candidate-map sieve
Search only maps already compatible with the native base projection and constraint kernel.

Neither branch closes from the current source registry alone.

## 6. Stop condition

This is a real source/data roadblock.

We now know exactly why R50 cannot proceed further:

- the source embedding law references `j_T`, but the mounted registry does not expose enough detail to audit its injectivity;
- no existing continuation/inheritance object has been shown to land in `K_t` injectively and equivariantly.

Therefore the next work should not invent `s_t`.

It should recover either:
1. a more explicit source definition of `j_T`, or
2. a source map whose codomain already lies in `K_t`.

## Final status

- `F_t`: TYPE CLOSED.
- `K_t`: TYPE CLOSED but not instantiated.
- `j_T` injectivity: OPEN.
- existing source map equal to `s_t`: NOT FOUND / NOT EARNED.
- candidate-map sieve: NEW DERIVED CLOSURE.
- global embedding nonemptiness: OPEN.

### New exact frontier

`@open/hidden_base_embedding_definition`

and

`@open/local_candidate_map_sieve_population`.
