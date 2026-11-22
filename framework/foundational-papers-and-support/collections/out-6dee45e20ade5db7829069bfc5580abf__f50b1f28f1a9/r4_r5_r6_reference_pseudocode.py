"""
Reference pseudocode for R4-R6 behavior.
No element-specific chemistry hardcoding is allowed.
"""

def R4_corridor_formation(state):
    chi = read_chirality(state.manifolds)  # read-only
    adjacency = read_adjacency(state.manifolds)
    strain = estimate_elastic_strain(state.manifolds, adjacency)
    candidates = build_corridor_candidates(state.manifolds, chi, adjacency, strain, state.ancestry)
    return state.with_R4_outputs(
        corridor_candidates=candidates,
        chirality_alignment_scores=score_chirality_alignment(candidates, chi),
        elastic_strain_map=strain,
        bandwidth_preload=estimate_bandwidth_preload(candidates),
        topology_overlap_regions=extract_overlap_regions(candidates),
    )

def R5_ordered_topology_resolution(state):
    scored = []
    for topology in enumerate_accessible_topologies(state.R4.corridor_candidates):
        score = recoverability_score(
            topology=topology,
            chirality=state.R4.chirality_alignment_scores,
            bandwidth=state.R4.bandwidth_preload,
            strain=state.R4.elastic_strain_map,
            ancestry=state.ancestry,
        )
        scored.append((score, topology))
    resolved = select_lowest_recoverable_topology(scored)
    return state.with_R5_outputs(
        resolved_topology_graph=resolved.graph,
        selected_corridors=resolved.selected_corridors,
        non_surviving_corridors=resolved.rejected_corridors,
        chirality_occupancy_record=resolved.chirality_occupancy,
        bandwidth_occupancy_record=resolved.bandwidth_occupancy,
        ordered_transformation_trace=resolved.trace,
        ancestry_preservation_record=resolved.ancestry_record,
    )

def R6_constrained_survivability_stabilization(state):
    damped = apply_recursive_recovery_damping(
        topology=state.R5.resolved_topology_graph,
        chirality_occupancy=state.R5.chirality_occupancy_record,
        bandwidth_occupancy=state.R5.bandwidth_occupancy_record,
        ancestry=state.ancestry,
    )
    survival = evaluate_survivability(damped)
    return state.with_R6_outputs(
        survivable_topology_state=damped if survival.passed else survival.relaxed_state,
        stabilized_corridor_set=survival.stabilized_corridors,
        damping_record=survival.damping_record,
        recoverability_residuals=survival.residuals,
        ancestry_preservation_report=survival.ancestry_report,
    )
