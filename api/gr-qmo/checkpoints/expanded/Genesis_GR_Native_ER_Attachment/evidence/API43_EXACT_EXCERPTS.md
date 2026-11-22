# Exact API 4.3 source excerpts

These passages are copied unchanged from the archived canonical Markdown, not newly proposed equations. Line numbers refer to that original file.

Source SHA-256: `0071c1d9d6a89c283f57a9c225857fa8f49a63f8caff86d83cca4a66896b0259`.

Recovered source archive: `3 | .zip`; source text was accessed through the byte-identical expanded copy in `Genesis_GR_Full_Recovery_2026-10-31.zip` and cross-checked against the original QMO database record.

## S1: Native API field types and reference state

Original lines 150–281.

```text
150: - energy is organized into chromatic sectors;
151: - microscopic adjacency is encoded by an ER network;
152: - spacetime geometry is a composite realization of those structures;
153: - a white-state core acts as a compressed reference, collapse endpoint, and cosmological nucleation state.
154: 
155: ---
156: 
157: # 2. Recovered Core Types
158: 
159: ## Definition 2.1 — Phase Field
160: 
161: ```text
162: Type: PhaseField
163: Symbol: τ
164: Signature: τ : M → ℝ / 2πℤ
165: Domain: spacetime manifold M
166: Codomain: periodic phase space
167: Role: stores the local phase of the time shell
168: ```
169: 
170: Exact recovered declaration:
171: 
172: \[
173: \tau : M \to \mathbb{R}/2\pi\mathbb{Z}.
174: \]
175: 
176: ### API interpretation
177: 
178: ```text
179: interface PhaseField {
180:     domain: Manifold
181:     value_space: CircularPhase
182:     observable_data: RelativePhase | PhaseGradient
183: }
184: ```
185: 
186: The phase field is not merely a clock value. It is a geometry-bearing state object whose derivatives may contribute directly to the effective metric.
187: 
188: ## Definition 2.2 — Chromatic Field
189: 
190: ```text
191: Type: ChromaticField
192: Symbol: χ
193: Arity: 7
194: Signature: χ(x) = (χ₁(x), …, χ₇(x))
195: Role: decomposes local energy organization into chromatic bands
196: ```
197: 
198: Exact recovered declaration:
199: 
200: \[
201: \boldsymbol{\chi}(x)
202: =
203: \bigl(\chi_1(x),\ldots,\chi_7(x)\bigr).
204: \]
205: 
206: ### API interpretation
207: 
208: ```text
209: interface ChromaticField {
210:     components: Array<ChromaticMode, 7>
211:     scalar_type: Real | Complex | Multivector
212:     state_space: ChromaticManifold
213: }
214: ```
215: 
216: ## Definition 2.3 — ER Network
217: 
218: ```text
219: Type: ERNetwork
220: Symbol: W
221: Discrete signature: Wᵢⱼ ∈ ℝ≥0
222: Continuum signature: W(x,y)
223: Role: stores weighted Planck-scale adjacency
224: ```
225: 
226: Exact recovered declaration:
227: 
228: \[
229: W_{ij}\in\mathbb{R}_{\ge 0}.
230: \]
231: 
232: ### API interpretation
233: 
234: ```text
235: interface ERNetwork {
236:     nodes: PlanckSite[]
237:     weight(i,j): NonNegativeReal
238:     continuum_limit(): AdjacencyKernel
239: }
240: ```
241: 
242: The ER network is the substrate-level locality provider. Metric distance is downstream of adjacency rather than assumed at initialization.
243: 
244: ## Definition 2.4 — White-State Core
245: 
246: ```text
247: Type: WhiteStateCore
248: Symbol: ΩW
249: Role:
250:     compressed reference state
251:     collapse endpoint
252:     cycle nucleation state
253:     fixed-point candidate
254: ```
255: 
256: Recovered state tuple:
257: 
258: \[
259: \tau=\mathrm{const},
260: \qquad
261: \boldsymbol{\chi}=0,
262: \qquad
263: W_{ij}=\delta_{ij},
264: \qquad
265: g_{\mu\nu}=\eta_{\mu\nu}.
266: \]
267: 
268: Equivalent collapse-language form elsewhere in the same source:
269: 
270: \[
271: \boldsymbol{\chi}=0,
272: \qquad
273: \nabla_\mu\tau=0,
274: \qquad
275: W_{ij}\propto\delta_{ij}.
276: \]
277: 
278: ### API interpretation
279: 
280: ```text
281: struct WhiteStateCore {
```

## S2: Direct phase and composite metric rules

Original lines 414–474.

```text
414: # 5. Recovered Metric API
415: 
416: ## Definition 5.1 — Phase Metric Contribution
417: 
418: \[
419: g^{(\tau)}_{\mu\nu}
420: =
421: \alpha\,\partial_\mu\tau\,\partial_\nu\tau.
422: \]
423: 
424: ```text
425: function phaseMetric(
426:     τ: PhaseField,
427:     α: CouplingConstant
428: ) -> MetricContribution
429: ```
430: 
431: ### Input
432: 
433: - phase field `τ`;
434: - coupling `α`;
435: - local derivatives `∂μτ`.
436: 
437: ### Output
438: 
439: - rank-2 metric contribution `g^(τ)μν`.
440: 
441: ### Invariance compatibility
442: 
443: Because the output depends on derivatives, it preserves the global phase-shift invariant.
444: 
445: ## Definition 5.2 — Composite Metric
446: 
447: \[
448: g_{\mu\nu}
449: =
450: g^{(0)}_{\mu\nu}
451: +g^{(\tau)}_{\mu\nu}
452: +g^{(\chi)}_{\mu\nu}
453: +g^{(ER)}_{\mu\nu}.
454: \]
455: 
456: ### API interpretation
457: 
458: ```text
459: function realizeMetric(
460:     background: BackgroundMetric,
461:     phase: PhaseMetricContribution,
462:     chromatic: ChromaticMetricContribution,
463:     adjacency: ERMetricContribution
464: ) -> EffectiveMetric
465: ```
466: 
467: ### Dependency graph
468: 
469: ```text
470: BackgroundGeometry ───────────────┐
471: PhaseField → PhaseMetric ─────────┤
472: ChromaticField → Backreaction ────┼→ EffectiveMetric
473: ERNetwork → CoarseGrainedGeometry ┘
474: ```
```

## S3: ER restrictions and metric composition

Original lines 3528–3637.

```text
3528: ```text
3529: classification: seven-component field
3530: role: separated energy-band organization
3531: white-state limit: \bm{\chi}\to 0
3532: ```
3533: 
3534: ### ERNetwork
3535: 
3536: ```latex
3537: W_{ij}\in\mathbb{R}_{\ge 0},
3538: \qquad W_{ij}=W_{ji}
3539: ```
3540: 
3541: ```text
3542: classification: weighted undirected adjacency structure
3543: role: microscopic relational geometry
3544: invariant: nonnegative symmetric connectivity
3545: ```
3546: 
3547: ### WhiteStateCore
3548: 
3549: ```latex
3550: \Wcore:
3551: \qquad
3552: \bm{\chi}=0,
3553: \quad
3554: \nabla_\mu\tau=0,
3555: \quad
3556: W_{ij}=\delta_{ij}
3557: ```
3558: 
3559: ```text
3560: classification: joint fixed-point state
3561: role: maximally compressed symmetric configuration
3562: contains:
3563:     chromatic collapse
3564:     vanishing phase gradient
3565:     identity-like ER adjacency
3566: ```
3567: 
3568: ## Module 2 — Composite State Space
3569: 
3570: ```latex
3571: \mathcal H
3572: =
3573: \mathcal H_\tau
3574: \otimes
3575: \mathcal H_\chi
3576: \otimes
3577: \mathcal H_{ER}
3578: \otimes
3579: \mathcal H_g
3580: ```
3581: 
3582: ```text
3583: CompositeStateSpace.sectors = {
3584:     phase,
3585:     chromatic,
3586:     ER adjacency,
3587:     geometry
3588: }
3589: ```
3590: 
3591: A coarse-grained product-state model is also recovered:
3592: 
3593: ```latex
3594: \rho
3595: =
3596: \rho_\tau\otimes\rho_\chi\otimes\rho_{ER}\otimes\rho_g
3597: ```
3598: 
3599: ## Module 3 — Metric Composition
3600: 
3601: ### Phase metric contribution
3602: 
3603: ```latex
3604: g^{(\tau)}_{\mu\nu}
3605: =
3606: \alpha\,\partial_\mu\tau\,\partial_\nu\tau
3607: ```
3608: 
3609: ### Composite metric
3610: 
3611: ```latex
3612: g_{\mu\nu}
3613: =
3614: g^{(0)}_{\mu\nu}
3615: +g^{(\tau)}_{\mu\nu}
3616: +g^{(\chi)}_{\mu\nu}
3617: +g^{(ER)}_{\mu\nu}
3618: ```
3619: 
3620: ### ER metric contribution
3621: 
3622: ```latex
3623: g^{(ER)}_{\mu\nu}
3624: =
3625: \lambda\sum_{i,j}W_{ij}\,\xi^{(i)}_\mu\xi^{(j)}_\nu
3626: ```
3627: 
3628: ```text
3629: MetricBuilder.inputs = {
3630:     background geometry,
3631:     phase gradients,
3632:     chromatic sector,
3633:     ER adjacency
3634: }
3635: 
3636: MetricBuilder.output = effective readable metric
3637: ```
```

## S4: Phase action and stress tensor

Original lines 3639–3671.

```text
3639: ## Module 4 — Phase Dynamics
3640: 
3641: ### Phase action
3642: 
3643: ```latex
3644: S_\tau
3645: =
3646: -\frac12\int d^4x\sqrt{-g}
3647: \left(
3648: \beta g^{\mu\nu}\partial_\mu\tau\partial_\nu\tau
3649: +V(\tau)
3650: \right)
3651: ```
3652: 
3653: ### Phase equation of motion
3654: 
3655: ```latex
3656: \beta\Box\tau-V'(\tau)=0
3657: ```
3658: 
3659: ### Phase stress-energy
3660: 
3661: ```latex
3662: T^{(\tau)}_{\mu\nu}
3663: =
3664: \beta\partial_\mu\tau\partial_\nu\tau
3665: -
3666: \frac12g_{\mu\nu}
3667: \left(
3668: \beta g^{\rho\sigma}\partial_\rho\tau\partial_\sigma\tau
3669: +V(\tau)
3670: \right)
3671: ```
```

## S5: Explicit kernel open issues

Original lines 4254–4276.

```text
4254: MK43.recover("InformationGeometry")
4255: MK43.recover("PhaseThermodynamics")
4256: MK43.recover("GravitationalWaveRealization")
4257: MK43.recover("HorizonEncoding")
4258: MK43.recover("ObservationalResponse")
4259: ```
4260: 
4261: ## Open Reconciliation Tasks
4262: 
4263: ```text
4264: [OPEN] Distinguish the original phase field from the later Time-Shell API object.
4265: [OPEN] Reconcile phase metric g^(tau) with explicit Time-Shell projection Π_T.
4266: [OPEN] Reconcile G^(eff)_munu notation with Einstein tensor notation.
4267: [OPEN] Specify the functional form of g^(chi)_munu.
4268: [OPEN] Specify the ER basis covectors xi^(i)_mu.
4269: [OPEN] Recover the total master action joining all sectors.
4270: [OPEN] Recover exact variation steps for the coupled field equations.
4271: [OPEN] Reconcile white-state W_ij = delta_ij with ER-foam connectivity semantics.
4272: [OPEN] Type the coarse-graining map W_ij → W_IJ.
4273: [OPEN] Attach helicon/graviton modules to this kernel without reversing ancestry.
4274: [OPEN] Classify Chapters 41–100 as reuse, extension, specialization, or new primitive.
4275: ```
4276: 
```

## S6: Original equation provenance

Original lines 13198–13208.

```text
13198: ```
13199: 
13200: ### MATH-0390 `58f6d0b43a9d`
13201: 
13202: **Kinds:** `display`  
13203: **Sources:** `chapters_6_10/chapters_6_10.tex`
13204: 
13205: ```latex
13206: g^{(ER)}_{\mu\nu} = \lambda 
13207: \sum_{i,j} W_{ij}\, \xi^{(i)}_\mu \xi^{(j)}_\nu,
13208: ```
```

## S7: Existing total action

Original lines 580–633.

```text
580: 
581: ---
582: 
583: # 8. Recovered Integration Layer
584: 
585: ## Total Action
586: 
587: \[
588: S_{\mathrm{tot}}
589: =
590: \frac{1}{16\pi G}
591: \int d^4x\sqrt{-g}\,R
592: +S_{\tau}
593: +S_{\chi}
594: +S_{ER}
595: +S_{\mathrm{matter}}.
596: \]
597: 
598: ### API interpretation
599: 
600: ```text
601: function totalAction(
602:     geometry: EinsteinHilbertSector,
603:     phase: PhaseSector,
604:     chromatic: ChromaticSector,
605:     er: ERSector,
606:     matter: MatterSector
607: ) -> UnifiedAction
608: ```
609: 
610: ## Integrated Field Equation
611: 
612: \[
613: G_{\mu\nu}
614: =
615: 8\pi G
616: \left(
617: T^{(\tau)}_{\mu\nu}
618: +T^{(\chi)}_{\mu\nu}
619: +T^{(ER)}_{\mu\nu}
620: +T^{(\mathrm{matter})}_{\mu\nu}
621: \right).
622: \]
623: 
624: ### API interpretation
625: 
626: ```text
627: function solveGeometry(
628:     phaseStress: StressEnergyTensor,
629:     chromaticStress: StressEnergyTensor,
630:     erStress: StressEnergyTensor,
631:     matterStress: StressEnergyTensor
632: ) -> GeometricResponse
633: ```
```
