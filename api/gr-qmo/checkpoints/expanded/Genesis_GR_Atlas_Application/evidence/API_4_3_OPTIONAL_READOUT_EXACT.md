# Exact API 4.3 excerpt

Source: MK43_Ultra_API_FULL_CURRENT/MK43_Ultra_API_CURRENT_CANONICAL.md

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
