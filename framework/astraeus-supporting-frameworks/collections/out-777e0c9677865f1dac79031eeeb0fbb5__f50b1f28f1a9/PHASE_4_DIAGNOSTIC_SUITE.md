# Phase 4 Diagnostic Suite

## Purpose

This file defines the diagnostic tests required to declare Pipeline 2 Phase 4 complete.

These diagnostics do not alter the pipeline.

They evaluate whether the locked Pipeline 2 architecture is stable under perturbation and oscillatory exposure.

## Diagnostic Class A — Roundtrip Ancestry Recovery

Run a manifold forward and backward:

R0 -> R7 -> R0

Required:
- high recovery correlation
- bounded drift
- ancestry identifiable
- no invalid topology replacement

Required cases:
- H
- N
- C6H6
- C6H6 + C6H6

## Diagnostic Class B — Valid Topology Survivability

Run stable manifolds forward:

R0 -> R7

Required:
- topology remains coherent
- no disassembly
- no generic attractor collapse

Required cases:
- H
- N
- N2 if available
- C6H6

## Diagnostic Class C — Invalid Topology Suppression

Run multi-manifold cases:

- H + H + H
- N + N + N

Required:
- overoccupied ecology suppresses,
- constrained pairwise topology may emerge when recoverability supports it,
- third manifold ancestry remains identifiable,
- no hardcoded element rule is used.

Expected observed examples:
- H + H + H may resolve toward H2 + H.
- N + N + N may resolve toward N2 + N.

These are not explicit rules. They are expected topology outcomes if recoverability supports them.

## Diagnostic Class D — Aromatic Independence

Run:

C6H6 + C6H6

Required:
- manifolds remain independent,
- pair overlap does not amplify into artificial corridor formation,
- both manifolds survive forward traversal,
- both manifolds survive roundtrip traversal.

## Diagnostic Class E — Perturbation Response

Inject bounded perturbations at R3, R4, R5, R6, and R7.

Required:
- perturbations damp, persist, amplify, or fail explainably,
- failure must localize to a domain,
- no unexplained ancestry loss.

## Diagnostic Class F — Excitation Spectra

Apply amplitude bands:

- low amplitude
- medium amplitude
- high amplitude
- boundary amplitude
- failure amplitude

Required:
- detect response class,
- record stability threshold,
- record coherence retention,
- record ancestry retention.

## Diagnostic Class G — Resonance Modes

Repeat oscillatory exposure across R7.

Required:
- detect stable response bands,
- detect metastable response bands,
- detect resonance-like amplification,
- detect catastrophic instability if present,
- preserve explainability.

## Diagnostic Class H — Oscillatory Instability Cascades

Push manifolds until instability begins.

Required:
- identify onset domain,
- identify whether failure begins in R4, R5, R6, or R7,
- identify whether ancestry survives failure,
- identify whether collapse is ordered or destructive.

## Diagnostic Class I — Chirality Imbalance Propagation

Introduce asymmetric chirality-access perturbation.

Required:
- chirality is read only,
- imbalance response is recorded,
- propagation pathway is tracked,
- damping or amplification is explainable,
- no chirality writing occurs.

## Diagnostic Class J — Stress-Frequency Behavior

Repeat stress cycles.

Required:
- detect fatigue,
- detect recovery,
- detect hysteresis,
- detect recursive topology fidelity amplification,
- detect whether topology improves, degrades, or saturates.

## Phase 4 Completion Audit

A Phase 4 completion audit must include all diagnostic classes A through J.
