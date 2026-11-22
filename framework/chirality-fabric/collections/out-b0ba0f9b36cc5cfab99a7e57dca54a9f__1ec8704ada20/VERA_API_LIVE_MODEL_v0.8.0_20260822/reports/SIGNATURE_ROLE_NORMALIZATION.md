# Signature Role Normalization — Self-Build Pass 006

## Source tuple
`Sig_Hol(h)=(src,tgt,[h],Hol_Conn,Hol_chi,Hol_Id,scope,provenance)`.

## Result
The eight entries are not semantically homogeneous. In the Astraeus API a lossless normal form is

`<src(h),tgt(h); scope, provenance | [h], Hol_Conn, Hol_chi, Hol_Id>`

where the left side is the recoverable type/context envelope and the right side is the structural payload. This does **not** prove any field redundant; it only prevents payload-width reduction from being confused with mathematical information loss.

## Source typing defect
D57 does not declare which equivalence relation is denoted by `[h]`. Identity Through History separately uses `[h]_Id`; the recovery program later derives `[h]_Rec`. Neither identification with D57 `[h]` is licensed by the mounted source.

## Realization blocker
The Recovery Test Family currently exists as an abstract schema, not an enumerated complete test basis. Therefore exact kernel equality for a concrete source projection is not operationally certifiable yet.

## Next frontier
`@recovery_test_family_instantiation`.
