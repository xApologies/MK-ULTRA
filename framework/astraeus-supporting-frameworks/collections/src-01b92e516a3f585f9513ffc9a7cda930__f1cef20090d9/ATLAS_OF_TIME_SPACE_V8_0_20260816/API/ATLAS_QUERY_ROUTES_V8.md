# Atlas Query Routes v8

## Native spectral route

```text
@admissibility
 -> @admissibility_transition_operator
 -> @unit_string_configuration_admissibility
 -> @helicon_partition
 -> @helicon_quotient_transition_operator
 -> @helicon_quotient_spectral_operator
```

## Recovered equations

```text
A_ij = alpha_ij theta_ij gamma_ij
A_ik = sum_j A_ij A_jk
sum_j A_ij = 1
```

## New handles

```text
@admissibility_transition_operator    T_A
@unit_string_admissibility_kernel     A_U
@unit_string_transition_operator      T_U
@helicon_quotient_kernel              A_H^Q
@helicon_quotient_transition          T_H^Q
@helicon_quotient_spectral_operator   L_H^Q = I-T_H^Q
@historical_helicon_operator          L_H
```
