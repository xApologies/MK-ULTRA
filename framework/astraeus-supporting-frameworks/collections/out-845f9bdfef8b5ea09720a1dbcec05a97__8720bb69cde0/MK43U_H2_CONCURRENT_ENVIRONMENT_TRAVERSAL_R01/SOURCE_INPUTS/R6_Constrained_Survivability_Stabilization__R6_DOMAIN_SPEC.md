# R6 Domain Specification
## Constrained Survivability Stabilization

R6 receives the resolved topology state from R5 and determines whether it remains stable under recovery pressure.

R6 is not where the corridor initially forms.
R6 is not where topology collapse is first selected.

R6 is where resolved topologies prove survivability.

## Domain Role

R6 performs:

1. damping recovery
2. survivability filtering
3. stability persistence testing
4. oscillatory pre-conditioning
5. ancestry-safe smoothing
6. post-collapse stabilization
7. rejection of unstable resolved configurations

## R6 Inputs

- R5 resolved topology graph
- selected corridor set
- rejected corridor list
- bandwidth occupancy record
- chirality occupancy record
- ordered transformation trace
- ancestry register

## R6 Outputs

- survivable topology state
- stabilized corridor set
- damping record
- recoverability residuals
- ancestry preservation report
- R7-ready manifold ecology

## R6 Interpretation

R6 asks:

Does the R5-resolved topology survive recursive recovery and damping without collapsing into either runaway ecology or total ancestry separation?

If yes, the topology is stabilized for R7.

If no, the topology is marked as unstable and should either:
- relax further
- reduce corridor occupancy
- revert to ancestry-preserving independent manifolds
- return to R5 for re-resolution in a later implementation
