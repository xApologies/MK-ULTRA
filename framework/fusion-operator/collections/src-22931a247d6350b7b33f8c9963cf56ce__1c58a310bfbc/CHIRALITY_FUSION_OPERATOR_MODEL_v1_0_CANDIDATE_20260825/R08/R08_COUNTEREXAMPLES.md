# R08 — Counterexample Ledger
## Resolution / Readout

### CE8-01 — Zero readout does not mean zero chirality
Current `R0_balance` returns `0`, but R07 proves `C_chi=2` and sourcewise L/R chirality survives. Therefore scalar zero cannot be read as annihilation.

### CE8-02 — Same counts do not mean same arrangement
Two 7-locus records can share `(n_N,n_E)=(3,4)` while differing in the placement of labels and thus in arrangement-sensitive chirality. Population equality is insufficient.

### CE8-03 — Same coarse output does not mean same provenance
`F_AB` and `F_BA` are distinct ordered provenance records but alias under any readout that forgets source order.

### CE8-04 — Hidden seam does not mean no Fusion seam
A seam-blind readout can quotient away the marker `q` while `q` remains in the formal pushout carrier.

### CE8-05 — Finer visibility is not formal creation
When `R1` separates local chirality that `R0` conflates, no new chirality is created. The distinction leaves the kernel of the finer quotient.

### CE8-06 — Row-like display is not automatically corruption
The coordinate permutation `sigma=(0,3,1,2)` maps `[1,0,0,1]` to `[1,1,0,0]` bijectively. Under that declared representation map, the row-like form is lossless.

### CE8-07 — The same row-like display can be wrong under an identity contract
If coordinates are declared fixed, receiving `[1,1,0,0]` from source `[1,0,0,1]` violates the contract. Therefore corruption is contract-relative, not appearance-relative.

### CE8-08 — Low Resolution is not low Bandwidth
A system may have enough Bandwidth to support the formal transformation while lacking Resolution to distinguish the seam. Conversely, an archived formal record can be read at high Resolution even if current Bandwidth does not support executing a new Fusion operation.

### CE8-09 — Seeing `q` does not recover `eta_F`
A readout that exposes the shared locus but discards witness/provenance does not prove which source history generated the seam.

### CE8-10 — Readout cannot manufacture whole-carrier chirality
A rendered image may look left- or right-biased. Without a formal `chi(Q)` observable, that visual bias is not a proof of emergent fused handedness.

### CE8-11 — Readout equality cannot prove physical identity
Two formal records can lie in the same observational fiber. Therefore one readout class cannot be substituted for formal identity without an injectivity proof.

### CE8-12 — Resolution blindness cannot prove nonexistence
If a feature lies in the blind core of the modeled readout family, that means no modeled readout distinguishes it. It does not prove the formal feature is absent.

### CE8-13 — A representation map may preserve information without preserving geometry as drawn
A bijection of display coordinates can preserve recoverable information while changing adjacency on the page. Whether such a map preserves *physical/geometric chirality* is a separate contract requirement. R08 therefore distinguishes representation invertibility from structure-preservation.

### CE8-14 — Quantum interference is not silently imported
R04 defined an interference-sensitive quantum basis. R08's structural Resolution quotient does not automatically guarantee that such a quantum measurement channel exists or remains coherent. Quantum visibility remains separately typed.
