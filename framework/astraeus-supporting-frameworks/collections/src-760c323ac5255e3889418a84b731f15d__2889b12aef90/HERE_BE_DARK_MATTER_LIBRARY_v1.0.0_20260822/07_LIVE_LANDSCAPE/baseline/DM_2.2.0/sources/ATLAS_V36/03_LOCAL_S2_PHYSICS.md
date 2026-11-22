# 03 — Local S2 Physics

Select `p in S3` and its localized projection:

```text
Sigma_p ~= S2.
```

## Local chirality parent

```text
chi_p = i_p^*chi.
```

## Readable sectors

Define typed local readout maps:

```text
rho_Q,p  : C_p -> Q_p
rho_G,p  : C_p -> G_p
rho_ER,p : C_p -> ER_p
```

where `C_p` is the admissible local chirality state space.

The principal local structure is:

```text
             chi_p
           /   |   \
          /    |    \
       QFT_p  GR_p  ER_p
```

No equality between the codomains is asserted.

## Meaning of the bridge

QFT and GR are related by shared ancestry:

```text
R_QG,p := {(q,g) | exists c in C_p such that q=rho_Q,p(c), g=rho_G,p(c)}.
```

This relation avoids requiring a global inverse from QFT to GR or GR to QFT.
