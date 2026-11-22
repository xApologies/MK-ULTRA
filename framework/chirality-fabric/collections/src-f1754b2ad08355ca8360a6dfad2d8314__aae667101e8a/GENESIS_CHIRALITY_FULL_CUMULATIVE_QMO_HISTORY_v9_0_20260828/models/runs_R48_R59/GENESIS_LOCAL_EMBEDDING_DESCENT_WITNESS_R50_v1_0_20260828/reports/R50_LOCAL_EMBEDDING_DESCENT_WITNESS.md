# R50 — LOCAL EMBEDDING DESCENT-WITNESS CRAWL

## Target

R49 forced the constructive witness:

`W_emb(t) = (F_t, K_t, s_t, Sep_t, Eq_I,t)`

with:

`F_t = pi_H^{-1}(t)`

and:

`K_t = ker(C) ∩ pi_E^{-1}(j_T(t))`.

The goal of R50 is to recover as much of those five components as the mounted source architecture actually provides.

## 1. F_t is source-backed as a fiber, but not enumerated

The hidden-state source already gives the bundle:

`pi_H:E_H^R -> T_H`

and therefore the hidden fiber at base address `t` is legitimately:

`F_t := pi_H^{-1}(t)`.

This closes the **type** of the first witness component.

What the source does not currently provide is a finite explicit enumeration or coordinatization of every member of `F_t` for an arbitrary `t`.

So:

`F_t` = CLOSED TYPE / OPEN INSTANCE.

## 2. K_t is also source-backed as an intersection object

R49 reduced the target to:

`K = ker(C)`.

The source-defined physical embedding family already requires:

`iota_H(E_H^R) subseteq ker(C)`

and base compatibility:

`pi_E o iota_H = j_T o pi_H`.

Therefore the compatible target fiber:

`K_t := ker(C) ∩ pi_E^{-1}(j_T(t))`

is not an arbitrary invention. It is exactly the intersection forced by the source constraints.

So:

`K_t` = CLOSED DERIVED TYPE / OPEN INSTANCE.

Again, the missing data are the concrete members/coordinates of that intersection.

## 3. Eq_I,t is already almost completely typed

The source embedding family requires:

`I o iota_H = iota_H o I_H`.

Restricting to one fiber gives the local equivariance certificate:

`Eq_I,t(x) : I(s_t(x)) = s_t'(I_H(x))`

for the appropriate target base fiber `t'`.

Therefore the form of the inheritance-equivariance witness is source-forced.

This is a major simplification:

`Eq_I,t` does not need a new law.

It needs only a concrete candidate `s_t` to evaluate.

## 4. Sep_t is only required where the base map collides

R49 identified the base-collision condition:

if `j_T(t1)=j_T(t2)` for `t1!=t2`, then images of the two hidden fibers must remain disjoint.

Therefore define:

`Sep_t` = certificate that the image of `s_t` is disjoint from images of other hidden fibers sharing the same native base address.

If `j_T` is injective on the relevant hidden support, `Sep_t` becomes trivial.

So the next useful source question is no longer vague "separation."

It is:

**Is the hidden base embedding `j_T` injective on the relevant support?**

That question can eliminate an entire witness component if the answer is yes.

## 5. The only truly missing constructive component is s_t

The other four witness fields are now typed:

- `F_t`: hidden source fiber;
- `K_t`: compatible native constraint-kernel fiber;
- `Sep_t`: cross-fiber disjointness condition only when base collisions exist;
- `Eq_I,t`: inheritance-equivariance equation inherited directly from the global embedding law.

The nontrivial constructive object is:

`s_t:F_t -> K_t`.

It must be injective and inheritance-compatible.

Therefore the R49 witness collapses to a much sharper core problem:

**construct one local injective equivariant fiber map.**

## 6. Can the source provide s_t indirectly?

The source architecture contains the already-typed global family:

`Emb_H,phys^R`.

Any member `iota_H` of that family restricts to a local map:

`s_t := iota_H|_{F_t}`.

So local descent witnesses and global embeddings are mutually related:

- a global embedding gives all local `s_t` by restriction;
- a compatible family of local `s_t` reconstructs a global embedding.

This is a descent/gluing equivalence.

It means R50 should not invent a second map family independent of `iota_H`.

The local witness is the **restriction data of a candidate global embedding**.

## 7. New theorem: local-global descent equivalence

Let a candidate family `{s_t}` satisfy:

1. `s_t:F_t -> K_t` injective for each `t`;
2. inheritance equivariance;
3. cross-fiber separation whenever distinct hidden bases share one native base.

Then the piecewise map:

`iota_H(x) := s_{pi_H(x)}(x)`

is a global physical hidden-state embedding.

Conversely, every global physical embedding restricts to such a family.

Therefore:

`Emb_H,phys^R`

is equivalent to the space of compatible local descent-witness families.

This does not prove nonemptiness, but it changes the search problem from one opaque global QMO into a family of local construction problems.

## 8. The next source crawl is now precise

There are only two high-value branches:

### Branch A — attack j_T
Recover the hidden-base/native-base map `j_T`.

Questions:
- Is it injective?
- What are its fibers?
- Does it collapse hidden base addresses?

If injective, the global-separation burden collapses substantially.

### Branch B — attack the local fiber map
Find any source object that already maps hidden relational states into the native inherited bundle locally.

Candidates:
- hidden-base embedding;
- inherited-state realization;
- continuation / inheritance morphism;
- state-bundle inclusion;
- constraint-kernel inclusion;
- portal/native realization map.

If one of those restricts to an injective map `F_t -> K_t`, then `s_t` is recovered.

## 9. Roadblock status

The tree moved.

R49 roadblock:
"construct all of W_emb(t)."

R50 roadblock:
"recover or construct s_t, and audit j_T for collisions."

Everything else in `W_emb(t)` is now typed by existing source constraints.

## Final status

- `F_t`: TYPE CLOSED.
- `K_t`: TYPE CLOSED.
- `Eq_I,t`: TYPE CLOSED.
- `Sep_t`: TYPE CLOSED, conditionally trivial if `j_T` injective.
- `s_t`: OPEN CONSTRUCTIVE CORE.
- local-global gluing theorem: CLOSED DERIVED.
- global embedding nonemptiness: still OPEN.

Next frontier:

`@open/local_hidden_fiber_injection`

with immediate side query:

`@open/hidden_base_embedding_injectivity`.
