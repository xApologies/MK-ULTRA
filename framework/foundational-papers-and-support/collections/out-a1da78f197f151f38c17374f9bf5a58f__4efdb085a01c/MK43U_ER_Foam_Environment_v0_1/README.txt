MK43 Ultra — ER Foam Environment v0.1
======================================

Purpose
-------
This package defines the first ER foam environment artifact for MK43 Ultra.

The environment:

- inherits the ER foam tile
- contains Pipeline 1
- contains Pipeline 2
- accepts manifold inputs
- expands according to manifold ecology
- provides the substrate through which manifolds propagate

This is not a software wrapper in the ordinary programming sense.

It is an MK43U environmental model:
the ER foam is the inherited substrate, the pipelines are static domain laws, and
the manifold is the recursive topology object entering the environment.

Core Architecture
-----------------

Environment
    inherits ER foam tile
    contains Pipeline 1
    contains Pipeline 2
    accepts manifolds

ER tile
    primitive chirality-continuity substrate

Pipeline 1 / Pipeline 2
    static domain pathways/rules from T0 through R7

Manifold
    recursive topology object propagated through the environment

Key Rule
--------

The pipeline files are not modified.

The environment contains them.

The environment expands, not the pipelines.

The ER foam tile is inherited into the environment as the lowest permissible
continuity substrate.

Coupling Law
------------

M perturbs ER
ER redistributes
ER modifies M
M propagates

Pipeline Domains
----------------

T0–T4:
    time-independent chirality / geometric adjacency traversal

T5:
    persistence-thickening threshold where temporal continuity begins to emerge

T6–T7:
    stabilization retention and closure preparation

R4–R6:
    corridor arbitration and topology-collapse regulation

R7:
    normalized bounded equilibrium

Component Files
---------------

components/Pipeline.zip
components/Pipeline 2.zip
components/ER Foam.zip

Manifolds are intentionally not bundled here.
They are accepted by the environment as external inputs.
