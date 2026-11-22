# Atlas Query Routes — v3

Recommended live-model routes:

```text
ATLAS.resolve("S3_Helicon_Domain")
  -> E_H -> H_3 -> Tau_H,p -> H_p^loc

ATLAS.trace("chirality","helicon")
  -> chi_3 -> O_H/J_H -> H_3

ATLAS.trace("helicon","graviton")
  -> H_3 -> delta H_R -> H_g -> graviton -> metric perturbation

ATLAS.trace("helicon","dark_matter_candidate")
  -> H_3 -> H_D -> transient ER ensemble -> ER load -> T^H -> GR

ATLAS.resolve("transient_ER_event")
  -> a_ij[n] -> nucleate/persist/transfer/reconnect/close

ATLAS.audit("dark_sector")
  -> rho_vis(H)=0
  -> rho_G(H)!=0
  -> Bianchi/source exchange
  -> old rotation/lensing/filament observables
```

Status rule: candidate routes must never be returned as recovered direct API edges unless promoted by a later audit/recovery pass.
