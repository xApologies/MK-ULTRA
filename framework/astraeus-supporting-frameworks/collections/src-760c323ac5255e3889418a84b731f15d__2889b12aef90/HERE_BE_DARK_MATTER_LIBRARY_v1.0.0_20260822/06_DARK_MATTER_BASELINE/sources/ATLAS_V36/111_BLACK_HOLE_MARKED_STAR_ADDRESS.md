# 111 — Black Hole as a Marked Continuity-Star Address

## Status

**SOURCE-SUPPORTED HUB ROLE + V13 CARTOGRAPHIC TYPING.**

The historical black-hole object is already recovered as

```text
B_H = (K_H, Omega_H, C_H, W_H, R_out)
```

with information invariant

```text
I_BH = (Omega_H,C_H,W_H,chi_H,K_H).
```

V13 does not redefine the black hole as dark matter. It uses the recovered hub role to mark a distinguished address in the ER-to-S3 translation.

---

## 1. Marked vertex / neighborhood

Let `b_H` be the coarse ER representative carrying `I_BH` at Resolution `R`.

Under the admissible-nerve translation:

```text
b_H |-> [H] in N_R
```

and, after `h_R`,

```text
[H] |-> p_H in S3.
```

The associated continuity neighborhood is

```text
U_H subset S3.
```

This is the precise current meaning of the phrase **black-hole continuity address**.

---

## 2. Closed star and link

Define the standard simplicial closed star

```text
St_R(H)
```

as the union of simplices containing `[H]`, together with their faces.

Define the link

```text
Lk_R(H)
```

as the simplices adjacent to the marked vertex but not containing it after the usual link construction.

### Interpretation

```text
St_R(H)
=
all higher-order continuity neighborhoods jointly incident on the black-hole address at Resolution R.
```

This is **not** identified with a physical dark-matter halo.

It is a cartographic object describing how the black-hole hub participates in the translated continuity network.

---

## 3. Associated localized S2 domain

Let

```text
p_H in S3
```

be the translated continuity address. The ordinary Atlas fiber is

```text
Sigma_H = pi^(-1)(p_H) ~= S2.
```

The black-hole state is not equated with the entire fiber:

```text
B_H != Sigma_H.
```

Rather, `B_H` supplies distinguished persistent boundary / hub data associated with the continuity address whose localized readable domain is `Sigma_H`.

---

## 4. Resolution refinement condition

For a finer Resolution `R'`, let

```text
r_R'R : N_R' -> N_R
```

be the canonical coarse readout / forgetting map when it exists.

A stable black-hole address requires a compatible marked class:

```text
r_R'R([H]_(R')) = [H]_R
```

and the translated invariant must remain recoverable:

```text
Read_R(I_BH^(R')) ~= I_BH^R.
```

This gives a direct recursive-continuity test for the anchor intuition.

---

## 5. Why this matters for dark-matter localization

Atlas v4 proved that homogeneous S3 data cannot generate a localized halo under an equivariant local readout.

A marked black-hole star supplies **address dependence already recovered from the historical ER network** without adding an arbitrary localization scalar.

Therefore v13 replaces the phrase

```text
black hole anchors dark matter
```

with the more precise candidate:

> **The recovered black-hole saturation state defines a marked persistent continuity address whose star records the nonuniform relational environment available to the local S2 gravitational readout.**

The magnitude law is still open.
