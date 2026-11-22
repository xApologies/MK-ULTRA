# ASTRAEUS — FULL HACK R5
## Square-Root Inheritance → Riemann Sphere → Conserved Complex Lift → SU(2) Selection Audit

**Date:** 2026-08-27
**Scope:** Genesis theoretical mathematics
**Stopping rule:** stop at first genuine failure or mathematically meaningful closure.
**Final verdict:** **FAIL TO FORCE SU(2); NEW RIEMANN/HOPF REPRESENTATION CLOSURE EARNED**

---

# 0. Correction to R4

R4 used the generic equation

`x^2+y^2+z^2+w^2=1`

too early and therefore erased the ancestry of the coordinates.

The current construction requires:

1. `S^0={-1,+1}`;
2. local square-root admission of complex identity;
3. inheritance of that complex identity through every later representation;
4. compactification into the Riemann sphere;
5. a constrained lift from that Riemann sphere into the next carrier;
6. exact/recoverable ancestry under the global conservation contract.

The sphere equation may appear downstream as an envelope, but it may not replace the construction history.

---

# 1. Genesis-language contract

The source-faithful order is relationship-first:

`Environment/Field -> Boundary -> Occupancy -> Relationship -> Identity -> Inheritance/History/Persistence -> Closure`.

The Genesis/TOME source also supplies:

- ordered structural compounding;
- `A|B` is not assumed equivalent to `B|A`;
- same readout may preserve different formal History;
- History concatenation is associative at the path level;
- representation changes may not silently erase formal distinctions;
- operators require typed signatures;
- grammar may not manufacture a mathematical operator.

These rules are used as firewalls throughout.

---

# 2. Square-root inheritance law

Start with

`S^0={-1,+1}`.

The local square-root operation opens the complex branch:

`sqrt(-1)=±i`,
`sqrt(+1)=±1`.

The operative Genesis rule is not "take a square root again at every dimension."

It is:

> the complex identity admitted by the square-root step remains recoverable through every lawful descendant projection/lift.

Denote the forward representation ladder by `P_n` and recovery back to the originating S^0 distinction by `R_n`.

The conservation contract is:

`R_n(P_n(s)) = s`

for each admitted `s in S^0`, at least on the declared recoverable code/domain.

This is a provenance/recoverability law, not merely equality of coordinate formulas.

---

# 3. Riemann sphere is the constrained S^2

Let the admitted complex address be

`zeta = u + i v`.

Inverse stereographic projection gives the Riemann-sphere coordinates

`X = 2u / (1+u^2+v^2)`,
`Y = 2v / (1+u^2+v^2)`,
`Z = (u^2+v^2-1)/(1+u^2+v^2)`.

Then

`X^2+Y^2+Z^2=1`

is a derived closure identity, not the foundational definition.

Away from the compactification point,

`zeta = (X+iY)/(1-Z)`

for this convention.

Therefore the complex address is recoverable from the sphere presentation.

**PASS.**

The S^2 stage is specifically

`CP^1 = C ∪ {∞} ≅ S^2`,

not an arbitrary unlabeled real sphere.

---

# 4. Ordered homogeneous lift

A Riemann-sphere point can be represented by an ordered nonzero complex pair

`U|V`

through the projective ratio

`zeta = U/V`

when `V != 0`, with the point at infinity represented by `V=0`.

Projective equivalence is

`U|V ~ λU|λV`, `λ in C*`.

Thus the Riemann sphere is the projective quotient

`CP^1 = (C^2 \ {0}) / C*`.

The boundary/order remains explicit in the Genesis carrier even though the projective readout identifies common nonzero complex scaling.

---

# 5. Conserved phase-decorated lift

Choose a norm-one representative of each projective ray:

`|U|^2+|V|^2=1`.

For finite `zeta`, all such representatives are

`U = e^{i theta} zeta / sqrt(1+|zeta|^2)`,
`V = e^{i theta}       / sqrt(1+|zeta|^2)`.

The square root appears explicitly in the normalization of the Riemann lift.

The residual parameter

`e^{i theta} in S^1`

is the phase fiber.

Hence:

`S^1 -> S^3 -> CP^1 ≅ S^2`.

This is the Hopf bundle.

The S^3 carrier is therefore not introduced as a generic four-real-coordinate sphere. It is reconstructed as the set of phase-decorated norm-one ordered complex lifts of the Riemann sphere.

**NEW REPRESENTATION CLOSURE: PASS.**

This is the corrected form of the S^3 stage.

---

# 6. Genesis interpretation of the fiber

The Riemann readout forgets the common phase:

`(U|V) -> (e^{i theta}U | e^{i theta}V)`

projects to the same point of `CP^1`.

Genesis Resolution rules say that equal readout does not imply formal identity.

Therefore the phase fiber may remain formal History/inherited information even when the S^2 readout cannot see it.

This is compatible with the global conservation-of-recoverable-structure rule.

However:

**Conservation does not, by itself, prove that every phase value represents a distinct Genesis identity.**

That requires an explicit invariant/identity contract.

Status: **COMPATIBLE / NOT FULLY IDENTIFIED.**

---

# 7. Ordered reversal test

The ordered lift keeps

`U|V != V|U`

generically.

Under the Hopf readout

`X = 2 Re(U conj(V))`,
`Y = 2 Im(U conj(V))`,
`Z = |U|^2-|V|^2`,

reversal gives

`U|V -> V|U`

and therefore

`X -> X`,
`Y -> -Y`,
`Z -> -Z`.

Thus boundary reversal has a visible, structured action on the Riemann/Hopf readout.

**PASS.**

The order is not an idle label.

---

# 8. The SU(2) selection question

Now ask:

> Does inherited complex identity + Riemann compactification + exact recoverability force the admissible transformation group to be SU(2)?

The answer is **NO**.

As a complex manifold, the Riemann sphere `CP^1` has a much larger biholomorphic automorphism group:

`Aut(CP^1) ≅ PGL(2,C) ≅ PSL(2,C)`.

A general Möbius transformation is

`zeta -> (a zeta + b)/(c zeta + d)`

with `ad-bc != 0`, modulo common nonzero scalar multiplication of the coefficients.

These transformations are invertible and preserve the complex-projective structure.

Therefore **recoverability plus complex/Riemann identity alone allows more transformations than SU(2).**

This is the decisive failure.

---

# 9. Where SU(2) sits

SU(2) appears when one preserves an additional positive Hermitian structure.

For an ordered pair

`Q=U|V`

define the standard Hermitian norm

`h(Q,Q)=|U|^2+|V|^2`.

Complex-linear transformations preserving this norm form `U(2)`.

Adding determinant one gives `SU(2)`.

Projectively, the induced transformations on the Riemann sphere are

`PSU(2) ≅ SO(3)`,

the orientation-preserving isometries of the round sphere.

Therefore:

`Riemann complex structure alone -> PSL(2,C)`,

while

`Riemann complex structure + chosen round/Hermitian metric -> PSU(2)` downstairs,

and its norm-one double-cover lift is

`SU(2)` upstairs.

---

# 10. Why global conservation is not yet enough

The source conservation law requires explicit:

- source;
- projection;
- target;
- invariant;
- recovery;
- tolerance/domain.

It does not declare that the invariant is specifically the standard Hermitian form

`|U|^2+|V|^2`.

Exact recoverability can hold under many invertible projective transformations that are not unitary.

Therefore the inference

`conservation of recoverable structure => unitary norm preservation`

is invalid without another witness.

This firewall is source-required.

---

# 11. Can 🤍|🤍 supply the missing invariant?

The global rule

`🤍|🤍`

is reversal-fixed and expresses a symmetric global carrier.

That is highly suggestive of equal treatment of the two Cradle roles.

But Genesis Layer Nonpromotion blocks the step

`🤍|🤍 -> h(U,V)=|U|^2+|V|^2`

unless a mathematical witness types the White rule as that Hermitian form.

Many Hermitian forms and many symmetric bilinear structures can respect a swap symmetry.

Therefore White symmetry alone does not uniquely select the standard norm.

**FAIL TO DERIVE HERMITIAN FORM FROM WHITE ALONE.**

---

# 12. Can History composition supply SU(2) multiplication?

Genesis History concatenation is associative and ordered.

But a path-category law is not automatically a binary multiplication on the state carrier.

No inverse History is assumed.

Therefore History provides the right *shape* of noncommutative ordered composition but does not yet create a group law on `S^3`.

**FAIL TO PROMOTE PATH COMPOSITION TO STATE-GROUP COMPOSITION WITHOUT A WITNESS.**

---

# 13. Conditional uniqueness theorem

If Genesis later earns the following additional contract:

1. the Riemann lift is the ordered complex carrier `C^2`;
2. the conserved global invariant is a positive-definite Hermitian form `h`;
3. the two Cradle roles are normalized symmetrically so that, in the chosen Genesis basis,
   `h(U|V,U|V)=|U|^2+|V|^2`;
4. admissible transformations are complex-linear and preserve `h`;
5. orientation/global phase normalization requires determinant one;

then the admissible transformation group is exactly

`SU(2)`.

This is a standard consequence, not a new axiom.

But items 2–5 are not all presently derived from the Genesis source grammar.

Thus this is a **conditional recovery theorem**, not an unconditional Genesis derivation.

---

# 14. Strongest new result

The corrected square-root/Riemann conservation chain earns:

`S^0`
`-> complex admission`
`-> C`
`-> CP^1 ≅ S^2`
`-> phase-decorated ordered lift`
`-> S^3`
`-> Hopf projection back to S^2`.

The S^3 is now properly constrained by its Riemann ancestry.

The unresolved selection problem is sharply identified:

> Which Genesis invariant reduces the full complex-projective automorphism freedom from PSL(2,C) to the unitary subgroup PSU(2), and which retained lift promotes that projective action to SU(2)?

---

# 15. Final verdict

## NEW CLOSURE

**Riemann/Hopf constrained S^3 reconstruction: EARNED AS A REPRESENTATION.**

The square-root complex identity can be carried coherently into the Riemann sphere and lifted as an ordered phase-decorated complex carrier whose total space is S^3.

This repairs the generic-sphere error in R4.

## FAILURE

**SU(2) IS NOT FORCED BY CONSERVATION OF RECOVERABILITY ALONE.**

The Riemann sphere admits the larger transformation group `PSL(2,C)`.

To isolate `SU(2)`, Genesis must additionally derive the preserved positive Hermitian/round metric structure (and determinant-one lift/orientation normalization) rather than importing it.

## Exact stopping point

The missing object is now:

**Genesis Hermitian Invariant Theorem**

Derive, from Genesis-native structure, a positive Hermitian invariant on the ordered complex Cradle that is preserved by admissible transformations and is symmetric in the global White carrier.

If that theorem is earned, the remaining reduction to `SU(2)` becomes nearly mechanical.

No stronger claim is authorized by this audit.
