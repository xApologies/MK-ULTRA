# Step 02 — Exact source excerpts

Original API 4.3 canonical Markdown. These are source premises, not certification of their proofs.

## S1_NATIVE_DISPERSION

Original canonical lines 53544–53664.

```text
53544: ```
53545: 
53546: URI:
53547: 
53548: ```text
53549: mk43://recover/gravity/closure-v2
53550: ```
53551: 
53552: # 2. Native Graviton Dispersion
53553: 
53554: ## Handle
53555: 
53556: ```text
53557: @native_graviton_dispersion
53558: ```
53559: 
53560: ## Type
53561: 
53562: ```text
53563: Type: NativeDispersionLaw
53564: Domain: admissible gravitational helicon modes on the ER adjacency graph
53565: Codomain: native update-frequency spectrum
53566: DependsOn:
53567:     @gravitational_helicon_mode
53568:     @er_network
53569:     @helicon_spectral_operator
53570: UsedBy:
53571:     @graviton
53572:     @effective_masslessness
53573:     @gravitational_wave_propagation
53574:     @radiative_stability
53575: ```
53576: 
53577: ## ER Adjacency Laplacian
53578: 
53579: For a scalar or mode amplitude \(f_i\) on the ER adjacency network,
53580: 
53581: \[
53582: (\mathcal{L}_{\mathrm{ER}} f)_i
53583: =
53584: \sum_j W_{ij}(f_i-f_j).
53585: \]
53586: 
53587: The spectral modes satisfy
53588: 
53589: \[
53590: \mathcal{L}_{\mathrm{ER}}u_\alpha
53591: =
53592: \lambda_\alpha u_\alpha.
53593: \]
53594: 
53595: ## Native Update Law
53596: 
53597: Let \(n\in\mathbb{Z}\) denote recursive update depth. The gravitational helicon mode obeys
53598: 
53599: \[
53600: H_g[n+1]
53601: -
53602: 2H_g[n]
53603: +
53604: H_g[n-1]
53605: +
53606: c_A^2\mathcal{L}_{\mathrm{ER}}H_g[n]
53607: =
53608: 0.
53609: \]
53610: 
53611: For
53612: 
53613: \[
53614: H_g[n]
53615: =
53616: q_\alpha e^{-i\omega_\alpha n}u_\alpha,
53617: \]
53618: 
53619: the exact discrete dispersion relation is
53620: 
53621: \[
53622: 4\sin^2\!\left(\frac{\omega_\alpha}{2}\right)
53623: =
53624: c_A^2\lambda_\alpha.
53625: \]
53626: 
53627: In the long-wavelength limit,
53628: 
53629: \[
53630: \omega_\alpha^2
53631: =
53632: c_A^2\lambda_\alpha
53633: +
53634: \mathcal{O}(\lambda_\alpha^2).
53635: \]
53636: 
53637: No additive native mass term occurs:
53638: 
53639: \[
53640: \omega_\alpha^2
53641: \neq
53642: c_A^2\lambda_\alpha+\mu_g^2,
53643: \qquad
53644: \mu_g=0.
53645: \]
53646: 
53647: ## Mass-Protection Constraint
53648: 
53649: Let \(P_g\) project onto the gravitational helicon sector and
53650: \(P_{\mathrm{lock}}\) project onto localized continuity-lock modes.
53651: For every admissible recursive correction operator \(\mathcal{R}\),
53652: 
53653: \[
53654: [\mathcal{R},P_g]=0,
53655: \]
53656: 
53657: and
53658: 
53659: \[
53660: P_{\mathrm{lock}}\mathcal{R}P_g=0.
53661: \]
53662: 
53663: A freely propagating gravitational helicon cannot acquire a localized
53664: continuity-lock mass without leaving the gravitational mode class.
```

## S2_NATIVE_FIXED_POINT

Original canonical lines 53666–53771.

```text
53666: # 3. Gravitational Self-Coupling and Nonlinear Closure
53667: 
53668: ## Handle
53669: 
53670: ```text
53671: @gravitational_self_coupling
53672: ```
53673: 
53674: ## Type
53675: 
53676: ```text
53677: Type: NativeFixedPointClosure
53678: Domain: continuity perturbations and gravitational helicon responses
53679: Codomain: self-consistent nonlinear gravitational state
53680: DependsOn:
53681:     @continuity_perturbation
53682:     @continuity_redistribution
53683:     @gravitational_helicon_mode
53684:     @time_shell
53685: UsedBy:
53686:     @gravity
53687:     @einstein_limit
53688:     @black_hole
53689:     @cosmology
53690: ```
53691: 
53692: Matter and gravity contribute to the total native continuity perturbation:
53693: 
53694: \[
53695: \delta C_{\mathrm{tot}}
53696: =
53697: \delta C_{\mathrm{m}}
53698: +
53699: \delta C_{\mathrm{g}}.
53700: \]
53701: 
53702: The gravitational contribution is geometry-dependent:
53703: 
53704: \[
53705: \delta C_{\mathrm{g}}
53706: =
53707: \mathcal{F}_g[\delta C].
53708: \]
53709: 
53710: Let \(\mathcal{R}_C\) be the continuity-redistribution operator.
53711: The closed gravitational state is the fixed point
53712: 
53713: \[
53714: \delta C_\star
53715: =
53716: \mathcal{R}_C
53717: \left[
53718: \delta C_{\mathrm{m}}
53719: +
53720: \mathcal{F}_g[\delta C_\star]
53721: \right].
53722: \]
53723: 
53724: Its constructive iteration is
53725: 
53726: \[
53727: \delta C^{(0)}
53728: =
53729: \mathcal{R}_C[\delta C_{\mathrm{m}}],
53730: \]
53731: 
53732: \[
53733: \delta C^{(n+1)}
53734: =
53735: \mathcal{R}_C
53736: \left[
53737: \delta C_{\mathrm{m}}
53738: +
53739: \mathcal{F}_g[\delta C^{(n)}]
53740: \right].
53741: \]
53742: 
53743: The readable metric sequence is
53744: 
53745: \[
53746: g_{\mu\nu}^{(n)}
53747: =
53748: \bar g_{\mu\nu}
53749: +
53750: \Pi_T\!\left(\delta C^{(n)}\right).
53751: \]
53752: 
53753: When the admissible iteration converges,
53754: 
53755: \[
53756: g_{\mu\nu}
53757: =
53758: \lim_{n\to\infty}g_{\mu\nu}^{(n)}.
53759: \]
53760: 
53761: The readable nonlinear closure is
53762: 
53763: \[
53764: G_{\mu\nu}[g]
53765: =
53766: 8\pi G\,
53767: T_{\mu\nu}[g,\mathrm{matter}],
53768: \]
53769: 
53770: where the gravitational organization contributes through the phase,
53771: chirality, ER, and geometry-dependent source sectors.
```

## S3_NATIVE_READOUT_ISOMETRY

Original canonical lines 53850–53935.

```text
53850: # 5. Native Probability Preservation
53851: 
53852: ## Handle
53853: 
53854: ```text
53855: @native_probability_preservation
53856: ```
53857: 
53858: ## Type
53859: 
53860: ```text
53861: Type: AdmissibleStateNormClosure
53862: Domain: optional quantized representation of native helicon modes
53863: Codomain: preserved physical norm or trace
53864: DependsOn:
53865:     @native_graviton_quantization
53866:     @helicon_state_space
53867:     @time_shell
53868: UsedBy:
53869:     @unitarity_audit
53870:     @graviton
53871:     @readable_graviton_projection
53872: ```
53873: 
53874: Let \(\mathcal{H}_A\) be the admissible helicon state space and \(P_A\) its projector.
53875: The native update operator
53876: 
53877: \[
53878: U_A:\mathcal{H}_A\to\mathcal{H}_A
53879: \]
53880: 
53881: satisfies
53882: 
53883: \[
53884: U_A^\dagger U_A=P_A.
53885: \]
53886: 
53887: Therefore, for every physical state \(|\psi\rangle\in\mathcal{H}_A\),
53888: 
53889: \[
53890: \langle\psi|U_A^\dagger U_A|\psi\rangle
53891: =
53892: \langle\psi|\psi\rangle.
53893: \]
53894: 
53895: Let the gravitational transduction map be
53896: 
53897: \[
53898: \mathcal{T}_g
53899: =
53900: \Pi_T P_{\mathrm{TT}}.
53901: \]
53902: 
53903: On the native physical gravitational sector,
53904: 
53905: \[
53906: \mathcal{T}_g^\dagger\mathcal{T}_g=P_g.
53907: \]
53908: 
53909: Hence
53910: 
53911: \[
53912: \|\mathcal{T}_g\psi_g\|^2
53913: =
53914: \|\psi_g\|^2.
53915: \]
53916: 
53917: When unreadable degrees of freedom are traced out, the readable state is
53918: 
53919: \[
53920: \rho_{\mathrm{readable}}
53921: =
53922: \mathcal{E}_T(\rho_{\mathrm{native}}),
53923: \]
53924: 
53925: with
53926: 
53927: \[
53928: \operatorname{Tr}
53929: \mathcal{E}_T(\rho_{\mathrm{native}})
53930: =
53931: \operatorname{Tr}\rho_{\mathrm{native}}.
53932: \]
53933: 
53934: This record governs the optional quantized representation. It does not redefine
53935: the native transduction framework as fundamentally quantum.
```

## S4_CONFIG_AND_COORDINATE_MAP

Original canonical lines 54276–54360.

```text
54276: # 10. Configuration-Space Dimensional Projection
54277: 
54278: ## Handle
54279: 
54280: ```text
54281: @configuration_space_3_1_1
54282: ```
54283: 
54284: ## Type
54285: 
54286: ```text
54287: Type: GeometricConfigurationSpace
54288: Native form: 3 + 1 + 1
54289: Readable projection: 1 + 3
54290: DependsOn:
54291:     @geometric
54292:     @chirality_history
54293:     @artifact_coordinate
54294:     @time_shell
54295: UsedBy:
54296:     @readable_spacetime
54297:     @lorentz_signature
54298:     @dimensionality_audit
54299: ```
54300: 
54301: The native geometric is represented as
54302: 
54303: \[
54304: \mathcal{G}_{\mathrm{geo}}
54305: =
54306: (X,Y,Z;A;\chi),
54307: \]
54308: 
54309: with
54310: 
54311: \[
54312: \mathcal{G}_{\mathrm{geo}}
54313: \in
54314: \mathbb{R}^3
54315: \times
54316: \mathcal{A}
54317: \times
54318: \Chi.
54319: \]
54320: 
54321: The three coordinates \(X,Y,Z\) are readable orientation axes,
54322: \(A\) is the artifact or admissible-expression coordinate, and
54323: \(\chi\) is chirality history.
54324: 
54325: The Time-Shell projection is
54326: 
54327: \[
54328: \Pi_T:
54329: \mathbb{R}^3\times\mathcal{A}\times\Chi
54330: \longrightarrow
54331: \mathcal{M}_{1,3},
54332: \]
54333: 
54334: \[
54335: \Pi_T(X,Y,Z;A;\chi)
54336: =
54337: (T,X,Y,Z).
54338: \]
54339: 
54340: Finite expression-capacity accounting yields
54341: 
54342: \[
54343: \Delta\Sigma^2
54344: =
54345: c_A^2\Delta T^2
54346: -
54347: \Delta X^2
54348: -
54349: \Delta Y^2
54350: -
54351: \Delta Z^2.
54352: \]
54353: 
54354: The readable metric signature is therefore
54355: 
54356: \[
54357: (+,-,-,-)
54358: \]
54359: 
54360: up to sign convention.
```

