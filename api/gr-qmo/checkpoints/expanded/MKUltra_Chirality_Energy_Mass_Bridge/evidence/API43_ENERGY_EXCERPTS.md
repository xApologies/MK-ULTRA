# API 4.3 exact energy excerpts

Source: `4.3(20261031-233418).zip` / `MK43_Ultra_API_FULL_CURRENT/MK43_Ultra_API_CURRENT_CANONICAL.md`.

SHA-256: `0071c1d9d6a89c283f57a9c225857fa8f49a63f8caff86d83cca4a66896b0259`. Original line numbers below. No formula is silently repaired.

## Persistence, native energy unit, history energy

```text
56248: ## RP-30.6 Persistence Functional
56249: 
56250: Depth contribution:
56251: 
56252: ```text
56253: Π_d
56254: =
56255: I_d B_d R_d O_d C_d
56256: ```
56257: 
56258: Total persistence:
56259: 
56260: ```text
56261: Π
56262: =
56263: Σ_d I_d B_d R_d O_d C_d
56264: ```
56265: 
56266: where:
56267: 
56268: ```text
56269: I_d = inheritance
56270: B_d = bandwidth
56271: R_d = resolution
56272: O_d = occupancy
56273: C_d = closure
56274: ```
56275: 
56276: Persistence is the scalar functional used by the recovered energy construction.
56277: 
56278: ## RP-30.7 Native Unit of Energy
56279: 
56280: ```text
56281: HANDLE:
56282:     @native_unit_of_energy
56283: 
56284: ALIASES:
56285:     @unit_of_energy
56286:     ε_MK
56287: 
56288: STATUS:
56289:     recovered by dependency inference
56290:     mathematically closed
56291:     linked
56292: ```
56293: 
56294: The native energy unit is the minimum admissible persistence difference:
56295: 
56296: ```text
56297: ε_MK
56298: =
56299: ΔΠ_min
56300: ```
56301: 
56302: Equivalent unit realization:
56303: 
56304: ```text
56305: ε_MK
56306: =
56307: Π(U₁) - Π(U₀)
56308: ```
56309: 
56310: for a primitive admissible transition carrying one native persistence increment.
56311: 
56312: Native normalization:
56313: 
56314: ```text
56315: ε_MK = 1
56316: ```
56317: 
56318: Interpretation:
56319: 
56320: ```text
56321: The statement ε_MK = 1 does not assert that all energy equals one.
56322: 
56323: It establishes the invariant native energy measure against which
56324: all other energy values are expressed.
56325: ```
56326: 
56327: Unit analogy:
56328: 
56329: ```text
56330: Unit circle:
56331:     r = 1
56332: 
56333: Unit String:
56334:     ℓ(γ_U) = 1
56335: 
56336: Native Unit of Energy:
56337:     ε_MK = 1
56338: ```
56339: 
56340: ## RP-30.8 General Energy
56341: 
56342: ```text
56343: HANDLE:
56344:     @general_energy
56345: 
56346: STATUS:
56347:     recovered by dependency inference
56348:     mathematically closed
56349:     linked
56350: ```
56351: 
56352: For an admissible history:
56353: 
56354: ```text
56355: H:
56356: U₀ → U₁ → ... → Uₙ
56357: ```
56358: 
56359: General energy is:
56360: 
56361: ```text
56362: E_MK(H)
56363: =
56364: [Π(Uₙ) - Π(U₀)] / ε_MK
56365: ```
56366: 
56367: Equivalent telescoping form:
56368: 
56369: ```text
56370: E_MK(H)
56371: =
56372: Σ_{j=0}^{n-1}
56373: [Π(U_{j+1}) - Π(U_j)] / ε_MK
56374: ```
56375: 
56376: In native units:
56377: 
56378: ```text
56379: ε_MK = 1
56380: ```
56381: 
56382: therefore:
56383: 
56384: ```text
56385: E_MK(H)
56386: =
56387: Π(Uₙ) - Π(U₀)
56388: ```
56389: 
56390: ### Derived energy laws
56391: 
56392: Composition:
56393: 
56394: ```text
56395: E(H₂ ∘ H₁)
56396: =
56397: E(H₁) + E(H₂)
56398: ```
56399: 
56400: Identity:
56401: 
56402: ```text
56403: E(id) = 0
56404: ```
56405: 
56406: Reversal:
56407: 
56408: ```text
56409: E(H⁻¹) = -E(H)
56410: ```
56411: 
56412: Closed history:
56413: 
56414: ```text
56415: E(H_closed) = 0
56416: ```
56417: 
56418: Subdivision invariance:
56419: 
56420: ```text
56421: Π(Uₙ)-Π(U₀)
56422: =
56423: Σ_{j=0}^{n-1}
56424: [Π(U_{j+1})-Π(U_j)]
56425: ```
56426: 
56427: These laws are derived from the endpoint-difference construction and
56428: the composability of admissible histories.
56429: 
56430: ## RP-30.9 Energy Density
56431: 
56432: ```text
56433: HANDLE:
56434:     @energy_density
56435: 
56436: STATUS:
56437:     recovered
56438:     linked
56439: ```
56440: 
56441: Canonical equation:
56442: 
56443: ```text
56444: ρ_E
56445: =
```

## Energy-density and conservation distinction

```text
56446: RT / V
56447: ```
56448: 
56449: where:
56450: 
56451: ```text
56452: R = Relationship
56453: T = Transition Capacity
56454: V = Containment Volume
56455: ```
56456: 
56457: Dependency trace:
56458: 
56459: ```text
56460: @relationship
56461: ↓
56462: @transition_capacity
56463: ↓
56464: @containment_volume
56465: ↓
56466: @energy_density
56467: ```
56468: 
56469: ## RP-30.10 Conservation-of-Information Inheritance
56470: 
56471: ```text
56472: HANDLE:
56473:     @conservation_of_information
56474: 
56475: STATUS:
56476:     maintained canonical model
56477:     dedicated full-handle recovery remains available
56478: ```
56479: 
56480: Canonical project placement:
56481: 
56482: ```text
56483: @time_space
56484: ↓
56485: @conservation_of_information
56486: ↓
56487: @global_inheritance
56488: ↓
56489: downstream conservation laws
56490: ```
56491: 
56492: Model statement:
56493: 
56494: ```text
56495: Conservation of Information is the global inheritance condition
56496: established at the Time-Space level.
56497: 
56498: Downstream conservation laws inherit from this global condition.
56499: ```
56500: 
56501: Recoverability corridor:
56502: 
56503: ```text
56504: @local_admissibility
56505: ↓
56506: @global_inheritance
56507: ↓
56508: @recursive_continuity
56509: ↓
56510: @persistence
56511: ↓
56512: @recoverability
56513: ↓
56514: @conservation_of_recoverable_structure
56515: ```
56516: 
56517: Energy inheritance corridor:
56518: 
56519: ```text
56520: @conservation_of_information
56521: ↓
56522: @global_inheritance
56523: ↓
56524: @persistence
56525: ↓
56526: @native_unit_of_energy
56527: ↓
56528: @general_energy
56529: ```
56530: 
56531: This records the intended primitive ancestry without identifying
56532: the native energy equation itself as the conservation law.
56533: 
56534: ## RP-30.11 Updated Dependency Landscape
```
