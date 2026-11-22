# Current API companion mapping

> Current API: [GR/QMO](../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/638dd45226a195dea4d59055ea1225d2f4fe4fc9d441941d2df2be7f25d6d870/README.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# Genesis–GR endpoint closure assessment

**The full requested native equivalence has not been established.** This is not a final release of a total native Genesis↔GR solver.

This continuation completes the variation of the source's real phase–chromatic interaction action. It supplies its stress tensor, all scalar variational residuals, and a conservation-identity check. It also identifies a mismatch with the printed coupled equations, tests the actual ER metric factorization against its graph dynamics, and derives the action-chain-rule terms that a physical equivalence proof must retain.

The calculations are source-grounded. The original source is unchanged. Neither the unknown ER covectors, chromatic metric contribution, nor ER action is filled by a convenient choice. Action-derived repairs are proposals conditional on adopting the displayed action, not silent canon edits.

> Current API: [GR/QMO](../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/638dd45226a195dea4d59055ea1225d2f4fe4fc9d441941d2df2be7f25d6d870/README.md).

## Run

Python with SymPy 1.14.0:

    python code/checks.py
    python verify.py

The current run passes 15 named exact checks. Several are negative controls that successfully detect discrepancies, not confirmations that the source equations coincide. No check is labeled a full native gravity simulation.

`code/coupled_source.py` evaluates a fully specified scalar-sector action on a supplied metric. It does not generate the actual native metric or solve the total native dynamics.
