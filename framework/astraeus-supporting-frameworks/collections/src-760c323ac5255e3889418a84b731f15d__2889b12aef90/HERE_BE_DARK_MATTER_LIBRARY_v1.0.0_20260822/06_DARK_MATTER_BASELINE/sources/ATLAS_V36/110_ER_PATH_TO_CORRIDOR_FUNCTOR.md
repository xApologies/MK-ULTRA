# 110 — ER Path Category to S3 Corridor Category

## Purpose

A successful `Theta_ER->S3` must preserve not only adjacency but **composition of continuation**.

The Chirality Corridor source already requires ordered composition and explicitly does not assume that every corridor has a global inverse. Therefore v13 uses a path **category** first and restricts to a groupoid only on reversible sectors.

---

## 1. ER path category

Let

```text
Path_ER^R
```

have:

- objects: coarse persistent ER vertices / address classes `v_alpha`;
- generating morphisms: admissible directed ER relations `e_alpha_beta`;
- morphisms: finite composable ER paths;
- identity: empty path at each vertex;
- composition: concatenation.

---

## 2. S3 admissible path category

Reuse the established Atlas object

```text
Path_adm,B(S3)
```

whose objects are continuity addresses and whose morphisms are Bandwidth-admissible S3 paths / corridors.

---

## 3. Translation functor

Define the candidate functor

```text
F_Theta^R : Path_ER^R -> Path_adm,B(S3)
```

by

```text
F_Theta^R(v_alpha) = p_alpha
F_Theta^R(e_alpha_beta) = gamma_alpha_beta.
```

The defining composition condition is

```text
F_Theta^R(e_beta_gamma o e_alpha_beta)
=
F_Theta^R(e_beta_gamma) * F_Theta^R(e_alpha_beta)
```

up to the path equivalence already admitted by the corridor category.

Identity preservation requires

```text
F_Theta^R(id_alpha) = id_p_alpha.
```

---

## 4. Chirality compatibility

The translated route must commute with the already-established chirality transport functor:

```text
P^chi : Path_adm(S3) -> ChirTransport.
```

For every ER generator `e_alpha_beta`, require

```text
chi_beta
~=
P^chi_(F_Theta^R(e_alpha_beta))(chi_alpha)
```

in the admissible-equivalence sense.

For a composed ER path `q`, this gives

```text
P^chi_(F_Theta^R(q))
=
composition of the stage transports.
```

This directly matches the corridor inheritance law rather than adding a new dark-sector transport rule.

---

## 5. Invariant-residue compatibility

Let `Inv_ER(q)` denote the recoverable invariant residue carried through an ER path and `Inv_corr(F_Theta^R(q))` the residue of the corresponding corridor transport.

A valid translation requires

```text
Inv_ER(q) ~= Inv_corr(F_Theta^R(q)).
```

The admissible invariant set is constrained by the Time-Shell translation contract and current energy-transduction candidate.

---

## 6. Conditional functorial closure

### Proposition V13-P110.1

If:

1. every recovered coarse ER generator is assigned an admissible S3 corridor path;
2. endpoint types agree;
3. chirality transport agrees on generators;
4. invariant residue is preserved;
5. the assignment respects ER path relations;

then the generator assignment extends to a functor

```text
F_Theta^R : Path_ER^R -> Path_adm,B(S3).
```

### Status

**PROVED AS A CATEGORY-THEORETIC EXTENSION STATEMENT, CONDITIONAL ON THE FIVE TRANSLATION CONDITIONS.**

This does not prove that the physical ER network satisfies those conditions. It tells Watcher exactly what has to be checked.

---

## 7. Cartographic meaning

The translation target is no longer:

```text
edge -> arbitrary curve drawn in S3.
```

It is:

```text
ER continuation composition
->
S3 corridor continuation composition
->
chirality / identity preserving transport.
```

That is a materially stronger translation criterion.
