# L08B — Actual Road → Helicon Selector Typing

**Verdict: CLOSED — TYPED CORRESPONDENCE PASS / UNIQUE MODE SELECTOR NOT DERIVED**

## 1. Question

Type the Road→Helicon object `S_RH` from mounted source without:
- importing a basin cycle;
- pairing basins by hand;
- choosing an SU(3)/QCD outcome in advance;
- discarding Road History/provenance;
- pretending that a spectral family implies a unique mode.

## 2. Source-side Road state

The Portal source defines a transaction request containing:

`source_address, target_address, geometric_identity, occupancy, chirality,
 basin_distribution, persistence_contract, invariant_residue, ancestry,
 provenance, resolution_required, bandwidth_required, closure_target`.

A Road is an ordered composition of admitted Portals with concatenated witness History.

Define the complete Road-state carrier:

\[
\mathsf{RS}_\Gamma =
(
a_s,a_t,G,o,\chi,\beta,\mathsf P,\mathrm{Inv},
\mathrm{Anc},\mathrm{Prov},R_{\rm req},B_{\rm req},
C_{\rm tgt},H_\Gamma,\Gamma
).
\]

Here:
- `G` is the full terminal Geometric/payload;
- `β` is the structural-basin distribution/telemetry, not a cyclic order;
- `H_Γ` is append-only Road/Portal History;
- `Γ` is the ordered Portal path.

Let `R_adm` be the set of such states for which every Portal transaction succeeds under the source contract:
target resolution, chirality admissibility, invariant-residue preservation,
recoverable identity, persistence, sufficient Resolution/Bandwidth,
destination closure, and complete provenance.

## 3. Helicon codomain

The unified parent types Helicon as a coherent admissible restructuring **ModeFamily** of the chirality/ER substrate.

The parent also gives the Helicon spectral operator:

\[
L_H(H_\alpha)=\lambda_\alpha H_\alpha.
\]

Define the allowed spectral mode family only as the source-backed set

\[
\mathscr H_{\rm Hel}
=
\left\{
H_\alpha\;|\;L_H(H_\alpha)=\lambda_\alpha H_\alpha
\right\}.
\]

No vector-space span, rank, SU(3) structure, or unique eigenmode is assumed here.

## 4. Correct selector type

The mounted sources support a **partial, generally set-valued correspondence**

\[
\boxed{
\mathbb S_{RH}:
\mathcal R_{\rm adm}
\rightrightarrows
\mathscr H_{\rm Hel}.
}
\]

For a complete admitted Road state `RS_Γ`, `S_RH(RS_Γ)` is the set of Helicon spectral modes that satisfy the native Helicon constraints carried by the realized terminal chirality/ER state.

The native anchors are:

- `@helicon CONSTRAINED_BY @chirality`;
- `@helicon_spectral_operator SELECTS_ALLOWED_MODE @helicon`;
- Helicon is a coherent admissible restructuring mode of the chirality/ER substrate.

Therefore the Road can be handed to Helicon only after its transaction contract closes and its terminal chirality/ER realization exists.

## 5. Dependency audit

The source establishes different roles for the Road-state fields.

### Directly source-relevant to Helicon admission
- terminal chirality organization;
- terminal chirality/ER-substrate realization;
- the Helicon spectral eigenmode condition.

### Required to establish an admitted Road realization
- identity/invariant residue;
- persistence contract;
- Resolution;
- Bandwidth;
- closure;
- ancestry/provenance;
- ordered Portal path.

### Retained but **not yet proved to be direct spectral coordinates**
- basin label/distribution;
- Road History as such.

History and basin telemetry remain in the input object because deleting them would destroy the Road witness and may destroy distinctions needed downstream. But no mounted source gives a formula

\[
(H_\Gamma,\beta)\mapsto\alpha
\]

for a unique Helicon eigenmode index `α`.

Thus their direct spectral dependence is OPEN rather than silently assumed.

## 6. Deterministic-selector no-go

A single-valued rule

\[
S_{RH}(\mathsf{RS}_\Gamma)=H_{\alpha(\Gamma)}
\]

would require a source-defined map selecting one `α`.

No such map is mounted.

Therefore:

\[
\boxed{
\text{A deterministic one-mode Road→Helicon selector is not source-derived at L08B.}
}
\]

The maximum justified object is the allowed-mode set/sector.

If the returned set is a singleton on a later declared sector, the correspondence specializes to a function there.

## 7. Explicit failure / ambiguity cases

`S_RH` is undefined or returns failure when:
1. the Portal/Road transaction contract does not close;
2. terminal chirality transport is inadmissible;
3. required invariant residue / identity / persistence is not recoverable;
4. required Resolution or Bandwidth is unavailable;
5. no valid terminal chirality/ER realization reaches Helicon;
6. the allowed Helicon mode set is empty.

If multiple modes remain allowed, the result is the **mode sector/set**. No arbitrary tie-break is permitted.

## 8. Hard firewalls

- No basin cycle.
- No `142857` pattern completion.
- No basin→A2 root assignment.
- No QCD red/green/blue label substitution.
- No assumption that Road History is already a gauge observable.
- No use of `Γ_n=<∇Ψ_n,RH>` as a Road selector unless a source-derived Road→spectral-shell map is first established.
- No arbitrary mode choice when the spectral sector is degenerate.

## 9. L08B close result

The Road→Helicon bridge is now typed at the strongest level justified by the source:

\[
\boxed{
\mathcal R_{\rm adm}
\;\rightrightarrows\;
\mathscr H_{\rm Hel}.
}
\]

This closes L08B as a typed correspondence and simultaneously records a no-go against an unsupported unique mode selector.

The next run is L08C:

> Which distinctions in the complete Road state survive Time-Space boundary projection and appear in the invariant residue, and which are quotiented away?
