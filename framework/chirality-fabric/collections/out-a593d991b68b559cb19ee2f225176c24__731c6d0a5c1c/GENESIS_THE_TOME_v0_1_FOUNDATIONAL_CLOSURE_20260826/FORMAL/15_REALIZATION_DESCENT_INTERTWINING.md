# GENESIS — 15 REALIZATION / DESCENT / INTERTWINING

This chapter is the principal mathematical firewall that motivated the current Genesis formalization, but it is stated generically.

## Realization

A realization `Λ:X⇀Y` is a typed partial map plus witness `η_Λ` describing what source structure determines the target representation, what is forgotten, what equivalence is used, and whether any target structure is supplied externally.

## Descent

When `Y` is defined on quotient/readout classes, `Λ` must factor through the quotient or satisfy the appropriate equivariance. For an ordinary quotient `q:X→X/~`, a map descends iff it is constant on equivalence classes. For associated-bundle settings, equivariance may replace literal constancy.

## Representative independence

A quotient-level realization is meaningless if different representatives of the same quotient class produce inequivalent target objects without a declared target symmetry. Genesis records such a construction as boundary-level, not quotient-level.

## Intertwining

For source transport `T_X` and target transport `T_Y`, the square

`Λ∘T_X  ?=  T_Y∘Λ`

requires a witness. Exact equality, canonical isomorphism, gauge equivalence, unitary equivalence, or a numerical defect are different claims and may not be substituted.

## Anti-insertion law

A target property is source-derived only if the realization witness shows that the source determines every structural distinction required by the property. A convenient target carrier can contain extra structure; that extra structure is not thereby inherited.

This is the core theorem preventing a downstream theory from being installed and then retroactively called emergent.
