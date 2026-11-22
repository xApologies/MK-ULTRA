# R4 -> R5 -> R6 Handoff Protocol

## Purpose

This file defines how the R4, R5, and R6 domains communicate without collapsing into one blanket macro-domain.

Each domain performs a distinct role.

## R4 Emits

- corridor_candidates
- chirality_alignment_scores
- elastic_strain_map
- topology_overlap_regions
- corridor_bandwidth_preload
- ancestry_map

## R5 Consumes

R5 consumes all R4 outputs.

R5 resolves corridor candidates into constrained topology.

## R5 Emits

- resolved_topology_graph
- selected_corridors
- non_surviving_corridors
- chirality_occupancy_record
- bandwidth_occupancy_record
- ordered_transformation_trace
- ancestry_preservation_record

## R6 Consumes

R6 consumes all R5 outputs.

R6 stabilizes or rejects resolved topology.

## R6 Emits

- survivable_topology_state
- stabilized_corridor_set
- damping_record
- recoverability_residuals
- R7_ready_manifold_ecology
- ancestry_preservation_report

## Core Handoff Law

R4 forms possibility.
R5 resolves possibility.
R6 stabilizes survivability.

No domain may erase another domain's role.
