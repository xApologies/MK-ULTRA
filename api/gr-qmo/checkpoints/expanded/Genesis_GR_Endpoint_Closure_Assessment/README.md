# Genesis–GR endpoint closure assessment

**The full requested native equivalence has not been established.** This is not a final release of a total native Genesis↔GR solver.

This continuation completes the variation of the source's real phase–chromatic interaction action. It supplies its stress tensor, all scalar variational residuals, and a conservation-identity check. It also identifies a mismatch with the printed coupled equations, tests the actual ER metric factorization against its graph dynamics, and derives the action-chain-rule terms that a physical equivalence proof must retain.

The calculations are source-grounded. The original source is unchanged. Neither the unknown ER covectors, chromatic metric contribution, nor ER action is filled by a convenient choice. Action-derived repairs are proposals conditional on adopting the displayed action, not silent canon edits.

Read `DERIVATION.md`, then `evidence/API43_ACTION_SOURCE.md`. The prior ER-attachment ZIP is in `prior_checkpoint/` unchanged. `STATUS.json` gives the exact determination.

## Run

Python with SymPy 1.14.0:

    python code/checks.py
    python verify.py

The current run passes 15 named exact checks. Several are negative controls that successfully detect discrepancies, not confirmations that the source equations coincide. No check is labeled a full native gravity simulation.

`code/coupled_source.py` evaluates a fully specified scalar-sector action on a supplied metric. It does not generate the actual native metric or solve the total native dynamics.
