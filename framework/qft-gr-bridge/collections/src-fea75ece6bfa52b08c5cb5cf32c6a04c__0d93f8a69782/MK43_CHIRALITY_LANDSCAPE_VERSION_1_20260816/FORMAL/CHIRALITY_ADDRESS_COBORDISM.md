# Chirality Address Cobordism — Formal Construction v0.1

## Definition CAC-1 — Address Object

An Address Object is:

```text
A_i = (
  Sigma_i,
  a_i,
  chi_i,
  Inv_i,
  R_i,
  B_i,
  H_i,
  O_i
)
```

with:

```text
Sigma_i ~= S2.
```

The fields inherit the existing Chirality Address source semantics.

## Definition CAC-2 — Corridor Morphism

A Corridor Morphism from `A_a` to `A_b` is an oriented compact 3-cobordism:

```text
W_ab^3 : Sigma_a -> Sigma_b
```

with:

```text
dW_ab^3 = Sigma_a union (-Sigma_b),
```

plus:

```text
P_W^chi   chirality/history transport
W_Inv     invariant-residue witness
W_Id      identity witness
B/R       operative admissibility data
```

satisfying the source corridor preservation conditions.

## Definition CAC-3 — Identity Corridor

```text
id_A ~= Sigma_A x [0,1]
```

with trivial formal transport up to declared identity equivalence.

## Definition CAC-4 — Composition

Given:

```text
W_ab : A_a -> A_b
W_bc : A_b -> A_c,
```

with matching intermediate boundary and compatible chirality/invariant witness data:

```text
W_bc o W_ab
:=
W_ab glue_(Sigma_b) W_bc.
```

## Proposition CAC-P1 — Associativity up to admissible equivalence

Cobordism gluing is associative up to the declared equivalence/isomorphism class when all intermediate gluing data are compatible. Therefore corridor composition inherits a category-like associative law rather than requiring path collapse.

## Proposition CAC-P2 — Bandwidth Algebra representation

Every admissible corridor morphism determines a typed operator word/path in the Transduction Geometry Bandwidth Algebra `A_B`. Composition of corridor morphisms maps to typed operator composition when defined.

## Proposition CAC-P3 — Resolution quotient

Two formally distinct corridors can satisfy:

```text
c1 != c2
rho_R(c1) = rho_R(c2),
```

so observational path multiplicity need not equal formal corridor multiplicity.

## Decorated category notation

Use:

```text
Cob^3_chi,R,B
```

for the controlled category/subcategory of S2 address objects and admissible chirality-decorated 3-cobordisms at declared Bandwidth/Resolution scope.

This construction does not require every arbitrary 3-cobordism to be physically admissible. MK43 admissibility selects the operative morphism class.
