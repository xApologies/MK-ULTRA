# WL-v225 — Mote Creation Recovers a Source-Level Chirality-Labelled Realization

**QMO:** QMO-AST-DM-WL-109  
**Work layer:** WL-036  
**Parent promotions:** 0  
**Status:** SOURCE REALIZATION ROLE RECOVERED / DIRECT HANDLE EDGE STILL ABSENT

API 4.3 already supplies a nontrivial mote creation/realization family:

```text
Nhat |Omega> = 0
Gdag |Omega> = (|+> + |->)/sqrt(2)
G |+> = G |-> = |Omega>/sqrt(2)
```

with the partial-isometry relations on the vacuum/single-mote sector.

It also supplies:

```text
C_k : I_k -> H_mote
C_k(I_k) = alpha_k |+> + beta_k |->
|alpha_k|^2 + |beta_k|^2 = 1.
```

Most importantly, the canonical source definition of `@white_core_mote_coupling` says that it is the Hamiltonian interaction **converting abstract source degrees into concrete chirality-labelled mote states**.

This sharpens WL-v213. There is still no registered direct edge or equivalence:

```text
@mote -> @chirality_labelled_mote
```

and none is promoted. But the source corpus does contain an explicit realization semantics for concrete chirality-labelled mote states.

The remaining controlled-witness problem is narrower: the rotational History pair H0/H1 has not been typed as the source input `I_k` of `C_k`.

**Next handle:** `@collapse_map`.
