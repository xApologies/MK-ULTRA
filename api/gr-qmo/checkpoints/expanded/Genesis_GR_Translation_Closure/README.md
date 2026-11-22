# Genesis–GR Translation Closure — research checkpoint

## Read this status first

The **operation-preserving translation of evaluated smooth endpoint fields is proved and implemented in a restricted symbolic reference model**. The original native metric/source attachment and its full physical inverse are **not established**. The user's complete native endpoint objective therefore remains incomplete. See `STATUS.json`.

This checkpoint replaces neither the original sources nor the previous exhaustive recovery. It adds a proof that the existing smooth Genesis connection/curvature/source definitions agree operationally with GR when a faithful differential realization and evaluated inputs are supplied. It also records the exact remaining unsupported boundary; no guessed Q_R, artificial native state, or new upstream update law is introduced.

## Contents

- `DERIVATION.md`: full assumptions, source attachment, inverse maps, connection proof, differential-expression induction, field-equation corollary, global qualifications and test interpretation.
- `TRANSLATION_DICTIONARY.md`: source-backed types, operations, inverses and limits.
- `SOURCE_ATTACHMENT_AUDIT.md`: the native metric/connection/source distinction, bounded source scan, and why no full native certificate is issued.
- `code/translator.py`: typed local tensor calculations, independent native Koszul and coordinate Christoffel routes, inverse endpoint records, input rejection.
- `code/checks.py`: 52 named checks. All passed in the final recorded run. Results are finite/symbolic implementation checks, not a universal native realization proof.
- `results/CHECK_RESULTS.json`: final results, versions and symbolic output expressions.
- `results/DEVELOPMENT_RUN_01.*`: retained first-run indexing error; repaired without changing mathematical definitions.
- `evidence/`: byte-identical recovered module documents, archive paths/hashes, bounded text-search log.
- `BASE_CHECKPOINT.json`: hash identifying the preceding exhaustive ZIP, left unchanged and not duplicated here.
- `MANIFEST.json`, `SHA256SUMS.txt`, `verify.py`: integrity controls for this incremental package.

## Run

Use Python with SymPy installed (`requirements.txt` pins the tested version):

```text
python code/checks.py
python verify.py
```

Tests rewrite their result and execution data when run; the distributed manifest identifies the original packaged bytes. A later rerun changes `CHECK_RESULTS.json` (including execution time), so a subsequent integrity check will correctly report that this generated file differs from the archived version. Keep the original package intact when reproducing.

## Interface example

An `EvaluatedGenesisEndpoint` requires an explicit metric, selected smooth connection, frame anchor, flux probes, constants and retained data. Its `to_gr()` validates the smooth selected connection and produces a `GREndpoint`. `to_genesis_endpoint()` returns the original evaluated endpoint representation in the fixed frame/probe context.

This is **not** a parser for arbitrary handwritten Genesis formulas. It is not a solver for Q_R on `(D,ℛ,R,B,H,χ,C,P)`. Raw native state input deliberately raises `UnresolvedNativeAttachment`.

For a supplied metric and anchor, `koszul_native` computes the unique smooth connection satisfying the source's torsion-free/metric-compatible restriction. That is useful for verifying an evaluated endpoint. It must not be confused with proving that the original finite connection selector produces that connection.

## Scope

Smooth Lorentzian four-dimensional tensor/source geometry; faithful anchored representation; matched units, signs, orientation and domains. The written theorem is intrinsic and can be patched with actual compatible transition data. The executable reference is local and symbolic. It assumes the declared symbolic regions and does not prove global signature, smoothness, native attainability, arbitrary matter-generation, PDE well-posedness, or empirical compatibility.

Native records are never erased by redefining invisible differences as gauge. Physically complete native reconstruction remains a separate unestablished requirement.
