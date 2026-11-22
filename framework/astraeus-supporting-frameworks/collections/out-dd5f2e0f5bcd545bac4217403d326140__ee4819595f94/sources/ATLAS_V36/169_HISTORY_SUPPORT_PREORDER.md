# History-Support Preorder — Atlas v26

## Status

New derived mathematics, source-constrained by Genesis-Language Chapter One, the runtime environment observations, the formal Chirality Corridor, and the previously recovered ER edge type.

This note does **not** identify history with mass, energy, gravity, or dark matter.

## 1. Motivation

V25 introduced the finite diagnostic count

```text
K_e^R = |H_e^R|
```

for invariant-preserving histories sharing relation `e` at Resolution `R`.

That count is useful, but it hides information: two relations can have the same number of supporting histories while being supported by different histories. The source material repeatedly emphasizes preserved relation and shared traversal, not merely raw multiplicity.

The parameter-free object should therefore be the **support set itself**.

## 2. Admissible history family

At declared Resolution `R`, let

```text
H_R
```

be a family of admissible S3-class histories already satisfying the corridor conditions:

- continuation/inheritance compatibility;
- coherent chirality transport;
- persistent identity;
- invariant-residue preservation;
- Resolution threshold;
- Bandwidth threshold;
- recursive closure.

For a persistent relation `e`, define

```text
S_R(e)
=
{ h in H_R : h traverses e while preserving the required invariant }.
```

`S_R(e)` is the **history-support set** of `e`.

## 3. History-support equivalence

Define

```text
e ≡_H f
iff
S_R(e) = S_R(f).
```

This is an equivalence relation on the selected relation set.

Two relations are history-support equivalent when the currently distinguishable admissible histories support them identically.

## 4. Reinforcement preorder

Define

```text
e <=_H f
iff
S_R(e) subseteq S_R(f).
```

This is reflexive and transitive, hence a preorder.

After quotienting by `≡_H`, the induced relation on equivalence classes is antisymmetric and therefore a partial order:

```text
E / ≡_H , <=_H
```

is a poset.

Interpretation:

```text
e <=_H f
```

means every retained admissible history that supports `e` also supports `f`.

This is stronger than the scalar statement

```text
|S_R(e)| <= |S_R(f)|.
```

## 5. What the sources authorize

The Chapter-One source states that repeated/shared surviving histories make a relation harder to alter, while the runtime source independently reports previously traversed pathways influencing future propagation preference, adjacency thickening, recursive pathway reinforcement, corridor stabilization, and temporary topology-memory traces.

A separate boundary investigation includes agreement count/density as a stabilizing contribution to coherence while explicitly leaving numerical coefficients for later calibration.

Therefore the source-grounded constitutive statement is **order-valued**, not a fixed scalar formula.

## 6. Continuity-strength monotonicity requirement

Let

```text
k_R : E -> R_nonnegative
```

be any proposed numerical continuity-strength realization on one fixed edge/type class with all non-history local constraints held equal.

History reinforcement requires isotonicity:

```text
e <=_H f
=>
k_R(e) <= k_R(f).
```

This is a **necessary compatibility condition** for a history-sensitive continuity strength.

It is not sufficient to determine `k_R` uniquely.

## 7. Important correction to v25

V25 wrote the open target schematically as

```text
K_e^R ->? k_e.
```

V26 sharpens this.

The recovered ER substrate can possess adjacency/continuity organization before a particular retained history family is accumulated. History therefore need not create continuity strength from zero. The safer constitutive decomposition is

```text
k_e^eff
=
k_e^base + Delta k_e^H,
```

where `Delta k_e^H` is a possible history-sensitive reinforcement/degradation contribution.

At fixed local type and constraints, added retained agreement support may not lower `Delta k_e^H`:

```text
S_R(e) subseteq S_R(f)
=>
Delta k_e^H <= Delta k_f^H.
```

Global temporal monotonicity is **not** asserted because the recovered runtime also permits topology-memory traces to decay and the narrative permits branches to dim/fail.

## 8. Finite scalar diagnostic

If `H_R` is finite and every retained history is weighted uniformly, define

```text
khat_e^R
=
|S_R(e)| / |H_R|.
```

Then

```text
0 <= khat_e^R <= 1
```

and

```text
e <=_H f
=>
khat_e^R <= khat_f^R.
```

`khat` is a parameter-free **diagnostic scalar representation** of the history-support order.

It is not promoted to physical `k_e`.

Equal `khat` values do not imply identical history-support sets.

## 9. Falsifier

If recovered physical continuity strength is proven independent of retained history support under otherwise identical conditions, then

```text
Delta k_e^H = 0
```

and the history-strength branch is killed without affecting the history-support poset itself.
