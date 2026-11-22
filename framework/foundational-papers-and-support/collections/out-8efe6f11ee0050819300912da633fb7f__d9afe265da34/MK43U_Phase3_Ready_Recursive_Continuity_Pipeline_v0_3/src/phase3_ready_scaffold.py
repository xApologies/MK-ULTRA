"""
MK43U Phase 3-Ready Pipeline Scaffold v0.3

This file is not a full simulator.
It defines the environmental parameters that should be read by a runner
when applying the phase3_ready_pipeline.json to a manifold.

Primary rule:
    Do not alter the hydrogen manifold to force success.
    Alter/apply the environment, then audit how the manifold reacts.
"""

PHASE3_READY_DOMAINS = {
    "T4": {
        "knot_admissibility_gain": 0.16,
        "resolution_separation_pressure": 0.09,
        "persistence_bias_strength": 0.14,
    },
    "T5": {
        "shell_mobility_strength": 0.30,
        "occupancy_drift_strength": 0.26,
        "core_resistance_floor": 0.86,
        "shell_identity_guard": 0.78,
    },
    "T6": {
        "continuity_current_strength": 0.38,
        "shell_circulation_strength": 0.32,
        "closure_feedback_strength": 0.36,
        "coupling_interface_exposure": 0.12,
        "identity_preservation_floor": 0.90,
    },
}

AUDIT_TARGETS = [
    "recovered_correlation",
    "shell_redistribution_magnitude",
    "core_persistence_stability",
    "closure_compensation",
    "chirality_tension_balance",
    "dynamic_equilibrium_indicator",
]
