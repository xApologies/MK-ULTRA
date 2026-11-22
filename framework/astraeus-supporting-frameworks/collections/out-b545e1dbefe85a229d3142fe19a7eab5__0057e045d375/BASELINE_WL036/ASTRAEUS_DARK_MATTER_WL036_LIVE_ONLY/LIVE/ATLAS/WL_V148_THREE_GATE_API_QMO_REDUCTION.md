# WL-v148 — Three-Gate API QMO Reduction

## Status

- Work layer: WL-024
- Parent promotions: 0
- Method: API-first QMO pair generation and exact-handle landscape composition

## Result

The second QMO generation round was targeted at the open objects exposed by WL-v147. Three small pair landscapes were generated rather than writing a new global bridge.

## Gate E — state admission / embedding

Pair:

`@dm_hidden_state_embedding` x `@native_constraint_closure`

At radius 2 on each parent API, the exact shared-handle interface is:

`['@native_constraint_closure']`

Thus the hidden-state QMO attaches to the parent constraint landscape through one canonical hub at this radius: `@native_constraint_closure`. This does not construct the embedding; it localizes the selection problem.

## Gate A — metric/action selection

Pair:

`@dm_metric_action_selection` x `@total_action`

Radius-2 exact interface:

`['@total_action', '@diffeomorphism_invariance', '@matter_action', '@metric_variation', '@stress_energy_tensor']`

The open dark action-selection object is therefore already embedded in the accepted action/variation landscape through `@total_action`, `@diffeomorphism_invariance`, `@matter_action`, `@metric_variation`, and `@stress_energy_tensor`. No new action formalism should be invented before crawling this interface.

## Gate R — dark readout / Time Shell

Pair:

`@dm_dark_matter_qualification_locus` x `@time_shell`

Radius-2 exact interface:

`['@time_shell', '@er_foam', '@graviton', '@gravity']`

So the qualification object and the Time-Shell/gravity object already overlap at `@time_shell`, `@er_foam`, `@graviton`, and `@gravity`. This sharply confirms that gravity is not the missing bridge.

## Three-gate landscape

Define the work-layer dependency-landscape object

`L_DM^(3) = L_embed union L_action union L_readout`

with every edge inherited from its API source and every gluing performed only on exact canonical handles.

The remaining problem is no longer “derive gravity from dark matter.” It is:

> find one compatible hidden-state witness that is admitted by the embedding/constraint gate, admitted by the covariant action/source gate, and occupies the dark readout qualification locus.

This is a constrained existence/selection problem over already-connected API mathematics.

## Consequence for the rotational/S3 candidate

The rotational/shear/holonomy candidate should be introduced only as candidate data for the hidden-state witness. It does not get its own gravity law. The QMO runtime should test whether that candidate can inhabit Gate E, Gate A, and Gate R simultaneously.

## Next API operation

Generate a QMO chain beginning at the existing candidate/open handle `@dm_hidden_state_embedding`, crawl through `@dm_constraint_preserving_embedding_family`, then compose it with the action-selection QMO and the readout QMO. If the combined object exposes a single remaining typed incompatibility, formalize only that incompatibility. If the intersection is empty, retain the null result.

## Guardrails

- State-admission interface != existence of an embedding.
- Action interface != existence/uniqueness of the selected action.
- Readout interface != nonempty dark-matter qualification locus.
- QMO composition != parent promotion.
