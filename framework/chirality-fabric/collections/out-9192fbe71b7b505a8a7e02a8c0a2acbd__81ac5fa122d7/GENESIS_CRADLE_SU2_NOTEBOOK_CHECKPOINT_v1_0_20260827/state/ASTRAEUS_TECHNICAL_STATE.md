# Astraeus Technical State

## Core candidate
Let the Genesis Field be `𝒢`. The first fold is the boundary `|`. The primitive Cradle is `𝔠 = 0|0`.

For occupied basin addresses `a,b`, retain the ordered Cradle: `C(a,b)=a|b`.
Introduce a separate readout: `r(a|b)`.

Genesis-supplied examples:
- `❤️|💛 : 🧡`
- `💜|💚 : 💙`

Under basin indexing `R=1,O=2,Y=3,G=4,B=5,V=6`, both are compatible with midpoint readout: `r(a|b)=(a+b)/2`.

## Passed properties of midpoint candidate
- commutative readout: `r(a|b)=r(b|a)`
- idempotent: `r(a|a)=a`
- medial/entropic identity
- nonassociative under recursive bracketing, so history/order of grouping can matter

## Failed property
Six coarse basin labels are not closed under all midpoint pairs. Examples: `R|O -> 1.5`, `R|V -> 3.5`.
Do not round or truncate by default. Genesis has historically truncated in some contexts, but the next hack must compare truncation, basin-pair superposition, finer Resolution / continuous readout, and unresolved admissibility.

## Chirality result
The ordered Cradle retains information that symmetric readout loses: `a|b != b|a` formally, while `r(a|b)=r(b|a)`.
Reflection `ρ(a|b)=b|a`, with `ρ²=id`, gives a native Z2 chirality/orientation structure.

## Recursive closure
Once admissible recursive communication is assumed, reachability closure satisfies topological closure axioms and recursive finite closure terminates under the existing sandbox hypotheses.

## Open upstream theorem
Cradle Recursive Realizability: prove lawful self-inheritance/recursion of Cradle addresses rather than assuming a Cradle can recur inside its own address.

## SU(2)
Not proved. Current mathematics earns a discrete mirror involution / Z2 action. To derive SU(2), additional continuous complex two-component structure and preserved unitary invariants must arise from the Genesis axioms rather than be imported.
