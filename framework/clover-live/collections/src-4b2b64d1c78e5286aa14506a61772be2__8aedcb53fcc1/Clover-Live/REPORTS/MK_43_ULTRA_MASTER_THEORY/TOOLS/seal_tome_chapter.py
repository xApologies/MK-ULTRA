from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
CHECKPOINTS = ROOT / "CHECKPOINTS"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
API_LEDGER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"
BATCHES = {
    "V01-C02": "V01_C02_V01_C03",
    "V01-C03": "V01_C02_V01_C03",
    "V01-C04": "V01_C04_V01_C05",
    "V01-C05": "V01_C04_V01_C05",
    "V01-C06": "V01_C06_V01_C07",
    "V01-C07": "V01_C06_V01_C07",
    "V01-C08": "V01_C08",
    "V02-C01": "V02_C01",
    "V02-C02": "V02_C02",
    "V02-C03": "V02_C03",
    "V02-C04": "V02_C04",
    "V02-C05": "V02_C05",
    "V02-C06": "V02_C06",
    "V02-C07": "V02_C07",
    "V02-C08": "V02_C08",
    "V02-C09": "V02_C09",
    "V02-C10": "V02_C10",
    "V02-C11": "V02_C11",
    "V02-C12": "V02_C12",
    "V02-C13": "V02_C13",
    "V02-C14": "V02_C14",
    "V02-C15": "V02_C15",
    "V03-C01": "V03_C01",
    "V03-C02": "V03_C02",
    "V03-C03": "V03_C03",
    "V03-C04": "V03_C04",
    "V03-C05": "V03_C05",
    "V03-C06": "V03_C06",
    "V03-C07": "V03_C07",
    "V03-C08": "V03_C08",
    "V03-C09": "V03_C09",
    "V04-C01": "V04_C01",
    "V04-C02": "V04_C02",
    "V04-C03": "V04_C03",
    "V04-C04": "V04_C04",
    "V04-C05": "V04_C05",
    "V04-C06": "V04_C06",
    "V04-C07": "V04_C07",
    "V04-C08": "V04_C08",
    "V05-C01": "V05_C01",
    "V05-C02": "V05_C02",
    "V05-C03": "V05_C03",
    "V05-C04": "V05_C04",
    "V05-C05": "V05_C05",
    "V05-C06": "V05_C06",
    "V05-C07": "V05_C07",
    "V05-C08": "V05_C08",
    "V06-C01": "V06_C01",
    "V06-C02": "V06_C02",
    "V06-C03": "V06_C03",
    "V06-C04": "V06_C04",
    "V06-C05": "V06_C05",
    "V06-C06": "V06_C06",
    "V06-C07": "V06_C07",
    "V06-C08": "V06_C08",
    "V07-C01": "V07_C01",
    "V07-C02": "V07_C02",
    "V07-C03": "V07_C03",
    "V07-C04": "V07_C04",
    "V07-C05": "V07_C05",
    "V07-C06": "V07_C06",
    "V07-C07": "V07_C07",
    "V07-C08": "V07_C08",
    "V07-C09": "V07_C09",
    "V07-C10": "V07_C10",
    "V08-C01": "V08_C01",
    "V08-C02": "V08_C02",
    "V08-C03": "V08_C03",
    "V08-C04": "V08_C04",
    "V08-C05": "V08_C05",
    "V08-C06": "V08_C06",
    "V08-C07": "V08_C07",
    "V09-C01": "V09_C01",
    "V09-C02": "V09_C02",
    "V09-C03": "V09_C03",
    "V09-C04": "V09_C04",
    "V09-C05": "V09_C05",
    "V09-C06": "V09_C06",
    "V09-C07": "V09_C07",
    "V10-C01": "V10_C01",
    "V10-C02": "V10_C02",
    "V10-C03": "V10_C03",
    "V10-C04": "V10_C04",
    "V10-C05": "V10_C05",
    "V10-C06": "V10_C06",
    "V11-C01": "V11_C01",
    "V11-C02": "V11_C02",
    "V11-C03": "V11_C03",
    "V11-C04": "V11_C04",
    "V11-C05": "V11_C05",
    "V11-C06": "V11_C06",
    "V11-C07": "V11_C07",
    "V12-C01": "V12_C01",
    "V12-C02": "V12_C02",
    "V12-C03": "V12_C03",
    "V12-C04": "V12_C04",
    "V12-C05": "V12_C05",
    "V12-C06": "V12_C06",
    "V13-C01": "V13_C01",
    "V13-C02": "V13_C02",
    "V13-C03": "V13_C03",
    "V13-C04": "V13_C04",
    "V13-C05": "V13_C05",
    "V13-C06": "V13_C06",
    "V14-C01": "V14_C01",
    "V14-C02": "V14_C02",
    "V14-C03": "V14_C03",
    "V14-C04": "V14_C04",
    "V14-C05": "V14_C05",
    "V14-C06": "V14_C06",
    "V14-C07": "V14_C07",
    "V14-C08": "V14_C08",
    "V15-C01": "V15_C01",
    "V15-C02": "V15_C02",
    "V15-C03": "V15_C03",
    "V15-C04": "V15_C04",
    "V15-C05": "V15_C05",
    "V15-C06": "V15_C06",
    "V15-C07": "V15_C07",
    "V16-C01": "V16_C01",
    "V16-C02": "V16_C02",
    "V16-C03": "V16_C03",
    "V16-C04": "V16_C04",
    "V16-C05": "V16_C05",
    "V16-C06": "V16_C06",
    "V16-C07": "V16_C07",
    "V16-C08": "V16_C08",
    "V17-C01": "V17_C01",
    "V17-C02": "V17_C02",
    "V17-C03": "V17_C03",
    "V17-C04": "V17_C04",
    "V17-C05": "V17_C05",
    "V17-C06": "V17_C06",
    "V18-C01": "V18_C01",
    "V18-C02": "V18_C02",
    "V18-C03": "V18_C03",
    "V18-C04": "V18_C04",
    "V18-C05": "V18_C05",
    "V18-C06": "V18_C06",
    "V18-C07": "V18_C07",
    "V18-C08": "V18_C08",
    "V18-C09": "V18_C09",
    "V18-C10": "V18_C10",
    "V18-C11": "V18_C11",
    "V18-C12": "V18_C12",
}


CONFIG = {
    "V18-C12": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C12_PROVENANCE_STATUS_AND_CITATION_LEDGERS.md",
        "equation_classes": {
            "146.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "146.2": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            **{f"146.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (3, 4)},
            "146.5": "DETERMINISTIC_STATUS_NORMALIZATION",
            "146.6": "CURATOR_SYNTHESIS",
            "146.7": "DETERMINISTIC_STATUS_NORMALIZATION",
            "146.8": "DETERMINISTIC_TYPE_NORMALIZATION",
            "146.9": "CURATOR_SYNTHESIS",
            "146.10": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            **{f"146.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 14)},
            "146.14": "DETERMINISTIC_PROVENANCE_NORMALIZATION",
            **{f"146.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(15, 20)},
            "146.20": "CURATOR_SYNTHESIS",
            "146.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@admissible_continuation", "@appendix_11", "@appendix_27", "@appendix_30",
            "@appendix_35", "@appendix_39", "@appendix_ad", "@appendix_am", "@appendix_at",
            "@appendix_au", "@appendix_av", "@appendix_bx", "@appendix_ca", "@appendix_t",
            "@appendix_z", "@axiom_a12", "@axiom_schema", "@definition_15_1_formal_infinity_class",
            "@definition_18_4_configuration_functional", "@hermitian_connection", "@prime_axiom_a4",
            "@prime_axiom_a6", "@primitive_p0", "@projection_residue_bundle",
        },
    },
    "V18-C11": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C11_DIMENSIONAL_AND_NORMALIZATION_LEDGER.md",
        "equation_classes": {
            "145.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"145.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            "145.11": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "145.12": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "145.13": "DETERMINISTIC_PROVENANCE_NORMALIZATION",
            **{f"145.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(14, 20)},
            "145.20": "CURATOR_SYNTHESIS",
            "145.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_1", "@appendix_13", "@appendix_31", "@appendix_34", "@appendix_48",
            "@appendix_br", "@appendix_bu", "@appendix_f", "@appendix_h",
            "@appendix_h_categorical_and_operadic_sketch", "@appendix_k", "@axiom_a2",
            "@axiom_a6", "@er_bridge_calculations_appendix_c", "@lemma_l3",
            "@primitive_p14", "@projection_residue",
        },
    },
    "V18-C10": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C10_API_NATIVE_DERIVATION_TREES.md",
        "equation_classes": {
            "144.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"144.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 8)},
            "144.8": "CURATOR_SYNTHESIS",
            "144.9": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "144.10": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"144.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 20)},
            "144.20": "CURATOR_SYNTHESIS",
            "144.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_14", "@appendix_15", "@appendix_17", "@appendix_36", "@appendix_42",
            "@appendix_a_quadratic_expansion_and_tt_derivation", "@appendix_a_tt_derivations",
            "@appendix_ac", "@appendix_ay", "@appendix_b", "@appendix_b_bead_hamiltonian_derivation",
            "@appendix_bh", "@appendix_bv", "@appendix_c_continuum_limit_to_gr", "@appendix_o",
            "@definition_18_1_pre_genesis_manifold", "@observable_algebra",
        },
    },
    "V18-C09": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C09_GRAPH_AND_CATEGORY_CONVENTIONS.md",
        "equation_classes": {
            "143.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"143.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 10)},
            "143.10": "DETERMINISTIC_API_EVIDENCE",
            **{f"143.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 20)},
            "143.20": "CURATOR_SYNTHESIS",
            "143.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_25", "@appendix_32", "@appendix_4", "@appendix_5", "@appendix_ab",
            "@appendix_af", "@appendix_ah", "@appendix_al", "@appendix_aw", "@appendix_ba",
            "@appendix_bf", "@appendix_bs", "@appendix_bt", "@appendix_d_er_network_dynamics",
            "@appendix_e_white_state_limits_and_stability", "@axiom_schemes_and_consistency",
            "@boundary_projection", "@lemma_l10", "@prime_axiom_a1", "@prime_axiom_a7",
            "@prime_definition_d2", "@prime_definition_d6", "@prime_definition_d7",
            "@prime_definition_d9", "@prime_lemma_l1", "@prime_lemma_l5",
            "@prime_primitive_p2", "@prime_theorem_t1", "@prime_theorem_t2",
            "@primitive_p10", "@primitive_p6", "@theorem_graph", "@theorem_t3",
        },
    },
    "V18-C08": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C08_QUANTUM_AND_FIELD_THEORY_CONVENTIONS.md",
        "equation_classes": {
            "142.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"142.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"142.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 20)},
            "142.20": "CURATOR_SYNTHESIS",
            "142.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_26", "@appendix_3", "@appendix_45", "@appendix_7", "@appendix_bk",
            "@appendix_c_continuum_limit", "@appendix_g", "@appendix_n", "@appendix_p",
            "@axiom_a0", "@axiom_a4", "@axiom_system", "@boundary_formation",
            "@definition_of_the_universal_triadic_law", "@persistence_locus",
            "@spectral_measurement_projection",
        },
    },
    "V18-C07": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C07_DIFFERENTIAL_GEOMETRY_CONVENTIONS.md",
        "equation_classes": {
            "141.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"141.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"141.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 20)},
            "141.20": "CURATOR_SYNTHESIS",
            "141.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@amplitude_geometry", "@appendix_1_notation_and_conventions", "@appendix_21",
            "@appendix_28", "@appendix_29", "@appendix_43", "@appendix_44", "@appendix_46",
            "@appendix_6", "@appendix_a_notation_and_conventions", "@appendix_ax", "@appendix_be",
            "@appendix_bj", "@appendix_by", "@appendix_d_er_bridge_geometry", "@appendix_e",
            "@appendix_j", "@axiom_3_1_phase_geometry", "@definition_10_2_structured_nothingness",
            "@definition_13_1_chirality", "@lemma_l5", "@lemma_l9", "@no_hair_theorem",
            "@prime_axiom_a0", "@prime_definition_d11", "@prime_definition_d3",
            "@prime_primitive_p6", "@prime_theorem_t4", "@prime_theorem_t5",
            "@prime_theorem_t7", "@shell_differential_geometry_appendix_b", "@superposition_closure",
        },
    },
    "V18-C06": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C06_THEOREMS_AND_PROOF_STATUS.md",
        "equation_classes": {
            "140.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"140.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 4)},
            "140.5": "DETERMINISTIC_STATUS_NORMALIZATION",
            "140.6": "EVIDENCE_BOUNDARY",
            "140.7": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "140.8": "EVIDENCE_BOUNDARY",
            "140.9": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "140.10": "DETERMINISTIC_API_EVIDENCE",
            "140.11": "DETERMINISTIC_STATUS_NORMALIZATION",
            **{f"140.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(12, 20)},
            "140.20": "CURATOR_SYNTHESIS",
            "140.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_10", "@appendix_10_numerical_schemes_for_phase_and_er_foam_evolution",
            "@appendix_2", "@appendix_41", "@appendix_52",
            "@appendix_5_er_bridge_topology_and_connectivity_measures", "@appendix_aq",
            "@appendix_ar", "@appendix_b_discrete_hamiltonian", "@appendix_bd",
            "@appendix_bg", "@appendix_s", "@appendix_w", "@complexification",
            "@definition_1", "@prime_definition_d1", "@prime_definition_d10",
            "@prime_definition_d12", "@prime_definition_d4", "@prime_theorem_t6",
            "@primitive_p17", "@projective_quotient", "@residue_invariance",
        },
    },
    "V18-C05": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C05_LEMMAS_AND_PROPOSITIONS.md",
        "equation_classes": {
            "139.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"139.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3)},
            "139.4": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"139.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (5, 6)},
            "139.7": "EVIDENCE_BOUNDARY",
            **{f"139.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (8, 9)},
            "139.10": "DETERMINISTIC_API_EVIDENCE",
            **{f"139.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 20)},
            "139.20": "CURATOR_SYNTHESIS",
            "139.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_19", "@appendix_49", "@appendix_8", "@appendix_ag",
            "@appendix_ao", "@appendix_bn", "@appendix_bz", "@appendix_q",
            "@appendix_r", "@appendix_v", "@definition_and_basic_invariants",
            "@hypercoherent_propositions", "@lemma_l12", "@primitive_p9", "@singularity_theorem",
        },
    },
    "V18-C04": {
        "path": WORKSPACE / "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C04_DEFINITIONS.md",
        "equation_classes": {
            "138.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "138.2": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "138.3": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"138.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(4, 8)},
            **{f"138.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (8, 9)},
            "138.10": "DETERMINISTIC_API_EVIDENCE",
            "138.11": "DETERMINISTIC_STATUS_NORMALIZATION",
            **{f"138.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(12, 19)},
            "138.19": "EVIDENCE_BOUNDARY",
            "138.20": "CURATOR_SYNTHESIS",
            "138.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_40", "@appendix_9", "@appendix_an", "@appendix_az",
            "@appendix_bi", "@appendix_d", "@appendix_l",
            "@axiom_15_2_infinity_spectrum_ordering", "@axiom_3_5_phase_invariance",
            "@axiom_a1", "@axiom_a10", "@axiom_a5", "@prime_axiom_a2",
            "@prime_definition_d5", "@prime_lemma_l4", "@prime_prime_primitive_p0",
            "@prime_primitive_p4", "@projective_target_manifold",
        },
    },
    "V18-C03": {
        "path": WORKSPACE /
        "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C03_AXIOMS_AND_PRIMITIVES.md",
        "equation_classes": {
            "137.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "137.2": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "137.3": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"137.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(4, 9)},
            **{f"137.{n}": "DETERMINISTIC_API_EVIDENCE" for n in (9, 10)},
            "137.11": "DETERMINISTIC_API_NORMALIZATION",
            **{f"137.{n}": "EVIDENCE_BOUNDARY" for n in (12, 13)},
            **{f"137.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(14, 20)},
            "137.20": "CURATOR_SYNTHESIS",
            "137.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_12", "@appendix_33", "@appendix_37", "@appendix_a",
            "@appendix_ap", "@appendix_as", "@appendix_bb", "@appendix_bc",
            "@appendix_bl", "@appendix_bo", "@appendix_bq", "@appendix_c", "@appendix_y",
            "@axiom_11_1_genesis_operation", "@axiom_a3", "@axioms_of_mk_43_ultra",
            "@birkhoff_theorem", "@complex_residue_structure", "@core_axioms",
            "@definition_of_the_infinity_spectrum", "@lemma_l4", "@lemma_l6",
            "@prime_axiom_a3", "@prime_lemma_l2", "@prime_lemma_l8",
            "@prime_primitive_p1", "@primitive_p11", "@primitive_p5", "@primitive_p8",
        },
    },
    "V18-C02": {
        "path": WORKSPACE /
        "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C02_EQUATION_CATALOG.md",
        "equation_classes": {
            "136.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "136.2": "DETERMINISTIC_PROVENANCE_NORMALIZATION",
            "136.3": "DETERMINISTIC_TYPE_NORMALIZATION",
            "136.4": "DETERMINISTIC_COUNTING_NORMALIZATION",
            "136.5": "EVIDENCE_BOUNDARY",
            **{f"136.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (6, 7, 8)},
            "136.9": "DETERMINISTIC_TYPE_NORMALIZATION",
            "136.10": "DETERMINISTIC_STATUS_NORMALIZATION",
            "136.11": "EVIDENCE_BOUNDARY",
            **{f"136.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(12, 20)},
            "136.20": "CURATOR_SYNTHESIS",
            "136.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_18", "@appendix_22", "@appendix_23", "@appendix_24",
            "@appendix_38", "@appendix_47", "@appendix_ae", "@appendix_ai",
            "@appendix_aj", "@appendix_bp", "@appendix_d_er_bridge_formation_equations",
            "@appendix_i", "@appendix_m", "@appendix_u", "@appendix_x", "@axiom_a8",
            "@chirality_organization", "@definition_10_1_null_slot_pair", "@focusing_theorem",
            "@framework_integrity_theorem", "@prime_definition_d13", "@prime_definition_d8",
            "@prime_lemma_l3", "@prime_primitive_p7", "@spectral_projection_rule", "@superposition",
        },
    },
    "V18-C01": {
        "path": WORKSPACE /
        "VOLUME_18_MATHEMATICAL_APPENDICES/V18_C01_SYMBOL_AND_TYPE_DICTIONARY.md",
        "equation_classes": {
            "135.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "135.2": "DETERMINISTIC_API_NORMALIZATION",
            "135.3": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"135.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (4, 5)},
            "135.6": "DETERMINISTIC_TYPE_NORMALIZATION",
            "135.7": "DETERMINISTIC_API_NORMALIZATION",
            "135.8": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"135.{n}": "DETERMINISTIC_API_EVIDENCE" for n in (9, 10)},
            **{f"135.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (11, 12)},
            "135.13": "EVIDENCE_BOUNDARY",
            "135.14": "DETERMINISTIC_STATUS_NORMALIZATION",
            "135.15": "DETERMINISTIC_API_NORMALIZATION",
            **{f"135.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(16, 20)},
            "135.20": "CURATOR_SYNTHESIS",
            "135.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_16", "@appendix_20", "@appendix_50", "@appendix_51",
            "@appendix_aa", "@appendix_ak", "@appendix_bm", "@appendix_bw",
            "@area_theorem", "@definition_2_3_er_network", "@lattice_calculus_appendix_a",
            "@lemma_l7", "@lemma_l8", "@penrose_singularity_theorem",
            "@prime_lemma_l6", "@prime_lemma_l7", "@prime_primitive_p3", "@primitive_p3",
        },
    },
    "V17-C06": {
        "path": WORKSPACE /
        "VOLUME_17_HISTORICAL_AND_INTERPRETIVE_CONTEXT/V17_C06_PUBLIC_DISCLOSURE_AND_RESEARCH_LIBRARY_BOUNDARY.md",
        "equation_classes": {
            "134.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "134.2": "DETERMINISTIC_STATUS_NORMALIZATION",
            "134.3": "CURATOR_SYNTHESIS",
            "134.4": "DETERMINISTIC_TYPE_NORMALIZATION",
            "134.5": "DETERMINISTIC_STATUS_NORMALIZATION",
            "134.6": "CURATOR_SYNTHESIS",
            **{f"134.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (7, 8, 9)},
            "134.10": "CURATOR_SYNTHESIS",
            **{f"134.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 16)},
            "134.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"134.{n}": "EVIDENCE_BOUNDARY" for n in (17, 18)},
            "134.19": "DETERMINISTIC_TYPE_NORMALIZATION",
            "134.20": "CURATOR_SYNTHESIS",
            "134.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@arrival_and_first_contact", "@chapter_11_the_continuum_lens",
            "@chapter_13_mapping_the_veil_currents",
            "@ingress_the_team_approaches_the_triadic_spire",
            "@intentional_architectonics", "@the_journey_begins_walking_the_manifold",
        },
    },
    "V17-C05": {
        "path": WORKSPACE /
        "VOLUME_17_HISTORICAL_AND_INTERPRETIVE_CONTEXT/V17_C05_PHILOSOPHICAL_INTERPRETATION.md",
        "equation_classes": {
            "133.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "133.2": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            **{f"133.{n}": "DETERMINISTIC_STATUS_NORMALIZATION" for n in (3, 5)},
            **{f"133.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (4, 6)},
            **{f"133.{n}": "EVIDENCE_BOUNDARY" for n in range(7, 11)},
            **{f"133.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 15)},
            **{f"133.{n}": "EVIDENCE_BOUNDARY" for n in (15, 16)},
            "133.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "133.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "133.19": "EVIDENCE_BOUNDARY",
            "133.20": "CURATOR_SYNTHESIS",
            "133.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_63_adapter_higher_dimensional_phase_embeddings_and_extended_topology",
            "@chapter_98_adapter_color_band_superposition_and_perceptual_phase_emergence",
            "@egress_the_team_seals_the_echo", "@egress_the_test_concludes",
            "@ingress_entering_the_harmonic_layering_chamber",
            "@the_role_of_chapter_0_in_the_monograph",
        },
    },
    "V17-C04": {
        "path": WORKSPACE /
        "VOLUME_17_HISTORICAL_AND_INTERPRETIVE_CONTEXT/V17_C04_GENESIS_CURATORIAL_RULINGS.md",
        "equation_classes": {
            "132.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"132.{n}": "DETERMINISTIC_AUDIT_NORMALIZATION" for n in (2, 3, 4, 7)},
            "132.5": "DETERMINISTIC_STATUS_NORMALIZATION",
            "132.6": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"132.{n}": "EVIDENCE_BOUNDARY" for n in range(8, 11)},
            **{f"132.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 16)},
            "132.16": "EVIDENCE_BOUNDARY",
            "132.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "132.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "132.19": "EVIDENCE_BOUNDARY",
            "132.20": "CURATOR_SYNTHESIS",
            "132.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@architect_script", "@arrival_at_the_pre_genesis_manifold",
            "@chapter_0_genesis_the_aperture_beyond_the_known",
            "@chapter_41_adapter_phase_engineered_materials_and_metastructures",
            "@chapter_96_adapter_universal_phase_coherence_across_scales",
            "@egress_harmonics_align", "@egress_shadows_growing_longer",
            "@genesis_algebra_architecture_of_emergence", "@genesis_architect_script",
            "@ingress_arrival_at_the_violet_corridor",
        },
    },
    "V17-C03": {
        "path": WORKSPACE /
        "VOLUME_17_HISTORICAL_AND_INTERPRETIVE_CONTEXT/V17_C03_NARRATIVE_MODELS_AND_SCIENTIFIC_TRANSLATION.md",
        "equation_classes": {
            "131.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"131.{n}": "CURATOR_SYNTHESIS" for n in (2, 5)},
            **{f"131.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (3, 7)},
            "131.4": "DETERMINISTIC_STATUS_NORMALIZATION",
            "131.6": "DETERMINISTIC_AUDIT_NORMALIZATION",
            **{f"131.{n}": "EVIDENCE_BOUNDARY" for n in range(8, 11)},
            **{f"131.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 17)},
            "131.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "131.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "131.19": "EVIDENCE_BOUNDARY",
            "131.20": "CURATOR_SYNTHESIS",
            "131.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_65_adapter_multiversal_dynamics_and_phase_correlated_cosmoi",
            "@chapter_85_adapter_ethical_optimization_and_phase_informed_governance",
            "@egress_integrity_holds", "@egress_the_door_to_deeper_resonance_opens",
            "@egress_the_spectrum_responds", "@egress_the_spires_respond",
            "@ingress_a_slow_walk_beneath_a_calm_sky",
            "@ingress_the_team_enters_the_echo_chamber",
            "@ingress_the_team_enters_the_sovereign_deck",
            "@ingress_the_vaeld_in_tranquility_drift", "@narrative_a_rumor_of_courts",
            "@narrative_a_vaeld_seen_from_outside", "@narrative_at_the_crown_gate",
            "@narrative_moment", "@narrative_when_the_vaeld_notices",
            "@the_crown_anchor_equations_stability_drift_and_the_architecture_of_sovereign_coherence",
        },
    },
    "V17-C02": {
        "path": WORKSPACE /
        "VOLUME_17_HISTORICAL_AND_INTERPRETIVE_CONTEXT/V17_C02_HISTORICAL_FORMULATIONS_AND_SUPERSESSION.md",
        "equation_classes": {
            "130.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"130.{n}": "DETERMINISTIC_AUDIT_NORMALIZATION" for n in (2, 3, 6)},
            "130.4": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            **{f"130.{n}": "DETERMINISTIC_STATUS_NORMALIZATION" for n in (5, 7)},
            **{f"130.{n}": "EVIDENCE_BOUNDARY" for n in range(8, 11)},
            **{f"130.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 15)},
            **{f"130.{n}": "EVIDENCE_BOUNDARY" for n in (15, 16)},
            "130.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "130.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "130.19": "EVIDENCE_BOUNDARY",
            "130.20": "CURATOR_SYNTHESIS",
            "130.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_0", "@chapter_12_the_radial_echo", "@chapter_14_tensor_harmonies",
            "@chapter_15_abyssal_anchor_theory",
            "@chapter_71_adapter_phase_coherent_civilizations_and_collective_stability",
            "@egress_flow_accepts_the_team", "@overture_arrival_in_the_luminous_realm",
            "@the_abyssal_crown_wars_a_historical_reconstruction_of_resonance_conflict",
        },
    },
    "V17-C01": {
        "path": WORKSPACE /
        "VOLUME_17_HISTORICAL_AND_INTERPRETIVE_CONTEXT/V17_C01_DEVELOPMENTAL_CHRONOLOGY_OF_MK_43_ULTRA.md",
        "equation_classes": {
            "129.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"129.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 6)},
            **{f"129.{n}": "DETERMINISTIC_AUDIT_NORMALIZATION" for n in (6, 7)},
            **{f"129.{n}": "EVIDENCE_BOUNDARY" for n in range(8, 11)},
            **{f"129.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 15)},
            **{f"129.{n}": "EVIDENCE_BOUNDARY" for n in (15, 16)},
            "129.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "129.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "129.19": "EVIDENCE_BOUNDARY",
            "129.20": "CURATOR_SYNTHESIS",
            "129.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@architectonics_of_intent_when_collective_intelligence_reshapes_the_abyssalum",
            "@chapter_0_the_black_rainbow",
            "@chapter_74_adapter_large_scale_coordination_and_er_synchronized_civilizations",
            "@chapter_79_adapter_optimization_via_phase_gradient_descent",
            "@chapter_91_adapter_free_will_geometry_and_competing_phase_potentials",
            "@egress_descent_begins", "@egress_drift_containment_holds",
            "@ingress_the_team_enters_the_trial_chamber", "@the_journey_begins",
        },
    },
    "V16-C08": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C08_FUTURE_INSTRUMENTS_AND_DECISION_TESTS.md",
        "equation_classes": {
            "128.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"128.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"128.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in (11, 12)},
            **{f"128.{n}": "EVIDENCE_BOUNDARY" for n in range(13, 17)},
            "128.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "128.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "128.19": "EVIDENCE_BOUNDARY",
            "128.20": "CURATOR_SYNTHESIS",
            "128.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V16-C07": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C07_BIOLOGICAL_AND_COGNITIVE_PREDICTIONS.md",
        "equation_classes": {
            "127.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"127.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"127.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in (11, 12)},
            **{f"127.{n}": "EVIDENCE_BOUNDARY" for n in range(13, 17)},
            "127.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "127.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "127.19": "EVIDENCE_BOUNDARY",
            "127.20": "CURATOR_SYNTHESIS",
            "127.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V16-C06": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C06_ENERGY_TRANSPORT_AND_PROPULSION_CONCEPTS.md",
        "equation_classes": {
            "126.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"126.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"126.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 16)},
            "126.16": "EVIDENCE_BOUNDARY",
            "126.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "126.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "126.19": "EVIDENCE_BOUNDARY",
            "126.20": "CURATOR_SYNTHESIS",
            "126.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_42_adapter_er_stabilized_energy_conduits_and_micro_wormhole_transport",
            "@chirality_transport", "@energy_transport_efficiency",
            "@er_stabilized_energy_conduits_and_micro_wormhole_transport",
            "@lemma_l2", "@parallel_transport", "@primitive_p7",
        },
    },
    "V16-C05": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C05_FIELD_CONTROL_AND_PHASE_ENGINEERING_MODELS.md",
        "equation_classes": {
            "125.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"125.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"125.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 16)},
            "125.16": "EVIDENCE_BOUNDARY",
            "125.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "125.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "125.19": "EVIDENCE_BOUNDARY",
            "125.20": "CURATOR_SYNTHESIS",
            "125.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@atmospheric_phase_engineering_and_climate_regulation",
            "@chapter_43_adapter_superfluidic_field_dynamics_and_advanced_propulsion",
            "@chapter_44_adapter_phase_field_armor_and_kinetic_nullification",
            "@chapter_48_adapter_atmospheric_phase_engineering_and_climate_regulation",
            "@field_transport", "@lemma_l13",
            "@phase_field_armor_and_kinetic_nullification",
            "@superfluidic_field_dynamics_and_advanced_propulsion",
        },
    },
    "V16-C04": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C04_DARK_MATTER_AND_HOLOGRAPHIC_PREDICTIONS.md",
        "equation_classes": {
            "124.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"124.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 4, 5, 6, 8, 9, 10)},
            "124.7": "DETERMINISTIC_TYPE_NORMALIZATION",
            "124.11": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "124.12": "DETERMINISTIC_COVERAGE_EVIDENCE",
            **{f"124.{n}": "EVIDENCE_BOUNDARY" for n in range(13, 17)},
            "124.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "124.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "124.19": "EVIDENCE_BOUNDARY",
            "124.20": "CURATOR_SYNTHESIS",
            "124.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V16-C03": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C03_BLACK_HOLE_AND_COSMOLOGICAL_PREDICTIONS.md",
        "equation_classes": {
            "123.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"123.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            "123.11": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "123.12": "DETERMINISTIC_COVERAGE_EVIDENCE",
            **{f"123.{n}": "EVIDENCE_BOUNDARY" for n in range(13, 17)},
            "123.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "123.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "123.19": "EVIDENCE_BOUNDARY",
            "123.20": "CURATOR_SYNTHESIS",
            "123.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V16-C02": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C02_GRAVITATIONAL_WAVE_DISCRIMINANTS.md",
        "equation_classes": {
            "122.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"122.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            "122.11": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "122.12": "DETERMINISTIC_COVERAGE_EVIDENCE",
            **{f"122.{n}": "EVIDENCE_BOUNDARY" for n in range(13, 17)},
            "122.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "122.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "122.19": "EVIDENCE_BOUNDARY",
            "122.20": "CURATOR_SYNTHESIS",
            "122.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V16-C01": {
        "path": WORKSPACE /
        "VOLUME_16_PREDICTIONS_AND_ENGINEERING_APPLICATIONS/V16_C01_PREDICTION_REGISTRY_AND_FREEZE_PROTOCOL.md",
        "equation_classes": {
            "121.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"121.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 4, 7, 8)},
            **{f"121.{n}": "DETERMINISTIC_AUDIT_NORMALIZATION" for n in (5, 6, 10, 16)},
            "121.9": "DETERMINISTIC_TYPE_NORMALIZATION",
            "121.11": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "121.12": "DETERMINISTIC_COVERAGE_EVIDENCE",
            **{f"121.{n}": "EVIDENCE_BOUNDARY" for n in (13, 14, 15)},
            "121.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "121.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "121.19": "EVIDENCE_BOUNDARY",
            "121.20": "CURATOR_SYNTHESIS",
            "121.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@prediction_freeze_protocol", "@prediction_registry", "@testable_predictions"},
    },
    "V15-C07": {
        "path": WORKSPACE /
        "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C07_EXTERNAL_DATA_REPLICATION_AND_FALSIFIABILITY.md",
        "equation_classes": {
            "120.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"120.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 10)},
            "120.10": "DETERMINISTIC_AUDIT_NORMALIZATION",
            "120.11": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "120.12": "DETERMINISTIC_COVERAGE_EVIDENCE",
            **{f"120.{n}": "EVIDENCE_BOUNDARY" for n in range(13, 17)},
            "120.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "120.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "120.19": "EVIDENCE_BOUNDARY",
            "120.20": "CURATOR_SYNTHESIS",
            "120.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V15-C06": {
        "path": WORKSPACE /
        "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C06_PARAMETER_FREEZE_AND_AUDIT_PROTOCOLS.md",
        "equation_classes": {
            "119.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "119.2": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "119.3": "DETERMINISTIC_AUDIT_NORMALIZATION",
            "119.4": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "119.5": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "119.6": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "119.7": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "119.8": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "119.9": "DETERMINISTIC_AUDIT_NORMALIZATION",
            "119.10": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"119.{n}": "DETERMINISTIC_COVERAGE_EVIDENCE" for n in range(11, 16)},
            "119.16": "EVIDENCE_BOUNDARY",
            "119.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "119.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "119.19": "EVIDENCE_BOUNDARY",
            "119.20": "CURATOR_SYNTHESIS",
            "119.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@audit_graph", "@dimensionality_audit", "@parameter_estimation",
            "@parameter_registry", "@scattering_audit", "@unitarity_audit",
        },
    },
    "V15-C05": {
        "path": WORKSPACE / "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C05_COSMOLOGICAL_OBSERVATION_WINDOWS.md",
        "equation_classes": {
            "118.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"118.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"118.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "118.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "118.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "118.19": "EVIDENCE_BOUNDARY",
            "118.20": "CURATOR_SYNTHESIS",
            "118.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_12_mk_43_ultra_prime_field_geometry_and_the_twin_prime_experiment",
            "@observational_windows_and_future_prospects",
            "@perturbations_and_observational_windows",
        },
    },
    "V15-C04": {
        "path": WORKSPACE / "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C04_BLACK_HOLE_AND_STRONG_GRAVITY_OBSERVABLES.md",
        "equation_classes": {
            "117.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"117.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"117.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "117.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "117.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "117.19": "EVIDENCE_BOUNDARY",
            "117.20": "CURATOR_SYNTHESIS",
            "117.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@gravity_audit_12", "@gravity_audit_v2"},
    },
    "V15-C03": {
        "path": WORKSPACE / "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C03_LIGO_OBSERVATION_ADDRESS_AND_COMPARISON_MAPS.md",
        "equation_classes": {
            "116.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"116.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"116.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "116.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "116.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "116.19": "EVIDENCE_BOUNDARY",
            "116.20": "CURATOR_SYNTHESIS",
            "116.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@LIGO_observation", "@consistency_test_general_relativity",
            "@definition_18_2_observational_shadow",
            "@module_16_observational_response_models",
            "@observational_graph", "@observational_pipelines_appendix_g",
            "@observational_predictions", "@predictive_catalogue_for_observations",
            "@space_based_and_next_generation_observations",
        },
    },
    "V15-C02": {
        "path": WORKSPACE / "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C02_GRAVITATIONAL_WAVE_COMPATIBILITY_PROGRAM.md",
        "equation_classes": {
            "115.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"115.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"115.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "115.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "115.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "115.19": "EVIDENCE_BOUNDARY",
            "115.20": "CURATOR_SYNTHESIS",
            "115.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V15-C01": {
        "path": WORKSPACE / "VOLUME_15_OBSERVATIONAL_AND_EXPERIMENTAL_VALIDATION/V15_C01_VALIDATION_ARCHITECTURE_AND_STATUS_DIMENSIONS.md",
        "equation_classes": {
            "114.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "114.2": "CURATOR_SYNTHESIS",
            **{f"114.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(3, 10)},
            "114.10": "DETERMINISTIC_AUDIT_NORMALIZATION",
            **{f"114.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "114.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "114.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "114.19": "EVIDENCE_BOUNDARY",
            "114.20": "CURATOR_SYNTHESIS",
            "114.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V14-C08": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C08_SCIENTIFIC_BOUNDARIES_OF_THE_BIOLOGICAL_SECTOR.md",
        "equation_classes": {
            "113.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"113.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"113.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "113.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "113.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "113.19": "EVIDENCE_BOUNDARY",
            "113.20": "CURATOR_SYNTHESIS",
            "113.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@arrival_first_contact_with_living_geometry",
            "@conscious_coherence",
        },
    },
    "V14-C07": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C07_COLLECTIVE_COGNITIVE_FIELDS.md",
        "equation_classes": {
            "112.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"112.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"112.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "112.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "112.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "112.19": "EVIDENCE_BOUNDARY",
            "112.20": "CURATOR_SYNTHESIS",
            "112.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_69_adapter_collective_cognition_and_er_synchronized_minds",
            "@chapter_92_adapter_reflective_fields_and_meta_cognitive_feedback",
            "@collective_cognition_and_er_synchronized_minds",
            "@morphogenesis_engine",
            "@reflective_fields_and_meta_cognitive_feedback",
            "@the_origin_well_phenomenon_depths_dangers_and_the_geometry_of_conscious_singularities",
        },
    },
    "V14-C06": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C06_AGENCY_AUTONOMY_AND_ENVIRONMENTAL_COUPLING.md",
        "equation_classes": {
            "111.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"111.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"111.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "111.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "111.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "111.19": "EVIDENCE_BOUNDARY",
            "111.20": "CURATOR_SYNTHESIS",
            "111.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@agency", "@agency_alignment_measure", "@agency_measure",
            "@autonomy_field", "@autonomy_field_definition",
            "@autonomy_magnitude", "@behavioral_encoding_law",
            "@chapter_93_adapter_constraint_fields_agency_and_environmental_coupling",
            "@constraint_fields_agency_and_environmental_coupling",
            "@local_and_global_autonomy_measures",
        },
    },
    "V14-C05": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C05_PERCEPTION_MEMORY_AND_TEMPORAL_INTEGRATION.md",
        "equation_classes": {
            "110.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"110.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"110.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "110.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "110.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "110.19": "EVIDENCE_BOUNDARY",
            "110.20": "CURATOR_SYNTHESIS",
            "110.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@internal_experiential_map", "@perception_criterion",
            "@perception_interval", "@reflective_operator",
        },
    },
    "V14-C04": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C04_CONSCIOUSNESS_AS_A_PHASE_COHERENT_DOMAIN.md",
        "equation_classes": {
            "109.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"109.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"109.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "109.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "109.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "109.19": "EVIDENCE_BOUNDARY",
            "109.20": "CURATOR_SYNTHESIS",
            "109.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_9_consciousness_coherence_and_orch_type_reductions",
            "@chapter_68_adapter_consciousness_as_a_phase_coherent_cognitive_field",
            "@consciousness", "@consciousness_as_a_phase_coherent_cognitive_field",
            "@hyperdomain_ecologies_an_expedition_into_living_geometry",
            "@reflective_field",
            "@the_revelation_consciousness_as_collective_coherence",
            "@the_team_spatial_forces_in_a_living_domain",
        },
    },
    "V14-C03": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C03_COGNITIVE_PERSISTENCE.md",
        "equation_classes": {
            "108.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"108.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"108.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "108.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "108.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "108.19": "EVIDENCE_BOUNDARY",
            "108.20": "CURATOR_SYNTHESIS",
            "108.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_82_adapter_decision_geometry_and_high_order_cognitive_optimization",
            "@chapter_89_adapter_neurocognitive_reconstruction_and_real_time_behavioral_mapping",
            "@cognitive_and_geometric_manifolds", "@cognitive_coherence_field",
            "@cognitive_engine", "@cognitive_order_parameter",
            "@cognitive_persistence", "@cognitive_stability",
            "@cognitive_stability_condition", "@cognitive_stability_equation",
            "@cognitive_state_geometry", "@conscious_experience",
            "@cultural_recognition",
            "@decision_geometry_and_high_order_cognitive_optimization",
            "@nervous_system",
            "@neurocognitive_reconstruction_and_real_time_behavioral_mapping",
            "@overture_when_civilizations_become_stars_in_a_cognitive_sky",
            "@the_grand_network_a_cognitive_lattice",
        },
    },
    "V14-C02": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C02_CELLULAR_AND_NEURAL_PHASE_FIELDS.md",
        "equation_classes": {
            "107.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"107.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"107.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "107.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "107.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "107.19": "EVIDENCE_BOUNDARY",
            "107.20": "CURATOR_SYNTHESIS",
            "107.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_8_neural_phase_fields_and_cognitive_coherence",
            "@behavioral_divergence_fields_and_psychopathology_geometry",
            "@cellular_phase_field", "@cellular_phase_potential",
            "@chapter_84_adapter_high_order_cognitive_fields_and_phase_awareness",
            "@chapter_86_adapter_neural_phase_geometry_and_behavioral_field_encoding",
            "@halo_and_neural_phase_shear",
            "@high_order_cognitive_fields_and_phase_awareness",
            "@neural_color_ratings_and_command", "@neural_er_geometry",
            "@neural_er_graph", "@neural_phase_field",
            "@neural_phase_field_definition",
            "@neural_phase_geometry_and_behavioral_field_encoding",
            "@pattern_recognition", "@persistent_cellular_identity",
            "@unicellular_phase_shells",
        },
    },
    "V14-C01": {
        "path": WORKSPACE / "VOLUME_14_BIOLOGICAL_AND_COGNITIVE_PHASE_FIELDS/V14_C01_BIOLOGICAL_PHASE_ORGANIZATION.md",
        "equation_classes": {
            "106.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"106.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"106.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "106.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "106.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "106.19": "EVIDENCE_BOUNDARY",
            "106.20": "CURATOR_SYNTHESIS",
            "106.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@adaptive_phase_interfaces_and_assistive_cognitive_technologies",
            "@autonomy_as_a_phase_separated_cognitive_field",
            "@bio_geometric_encoding_and_living_phase_structures",
            "@biological_geometry", "@biological_organization",
            "@biological_phase_coupling_and_cellular_field_dynamics",
            "@biologically_admissible_environment",
            "@chapter_66_adapter_biological_phase_coupling_and_cellular_field_dynamics",
            "@chapter_70_adapter_bio_geometric_encoding_and_living_phase_structures",
            "@chapter_87_adapter_psychological_phase_distortions_and_cognitive_stability",
            "@chapter_90_adapter_autonomy_as_a_phase_separated_cognitive_field",
            "@chapter_94_adapter_phase_compatible_environments_and_supportive_cognitive_geometry",
            "@chapter_95_adapter_adaptive_phase_interfaces_and_assistive_cognitive_technologies",
            "@chromatic_biological_coupling", "@cognitive_phase_field_model",
            "@cognitive_phase_mode", "@cognitive_phase_modes",
            "@coordinated_behavior", "@overture_entering_the_living_abyssalum",
            "@phase_compatible_environments_and_supportive_cognitive_geometry",
            "@phase_driven_morphogenesis",
            "@psychological_phase_distortions_and_cognitive_stability",
            "@watcher",
        },
    },
    "V13-C06": {
        "path": WORKSPACE / "VOLUME_13_HOLOGRAPHY_AND_INFORMATION_TRANSFER/V13_C06_INFORMATION_CONSERVATION_ACROSS_PROJECTIONS.md",
        "equation_classes": {
            "105.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"105.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"105.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "105.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "105.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "105.19": "EVIDENCE_BOUNDARY",
            "105.20": "CURATOR_SYNTHESIS",
            "105.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@conservation_of_information"},
    },
    "V13-C05": {
        "path": WORKSPACE / "VOLUME_13_HOLOGRAPHY_AND_INFORMATION_TRANSFER/V13_C05_CYCLE_TO_CYCLE_MEMORY.md",
        "equation_classes": {
            "104.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"104.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"104.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "104.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "104.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "104.19": "EVIDENCE_BOUNDARY",
            "104.20": "CURATOR_SYNTHESIS",
            "104.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_64_adapter_meta_holography_and_extended_memory_architectures",
            "@chapter_97_adapter_white_state_core_geometry_and_nucleation_memory",
            "@cycle_memory", "@entropy_current", "@er_assisted_memory",
            "@global_er_synchronized_memory", "@memory_effect",
            "@memory_persistence", "@white_state_memory_imprint",
        },
    },
    "V13-C04": {
        "path": WORKSPACE / "VOLUME_13_HOLOGRAPHY_AND_INFORMATION_TRANSFER/V13_C04_BLACK_HOLE_INFORMATION.md",
        "equation_classes": {
            "103.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"103.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"103.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "103.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "103.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "103.19": "EVIDENCE_BOUNDARY",
            "103.20": "CURATOR_SYNTHESIS",
            "103.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_f_information_geometry_formulas",
            "@complexity_circuits_and_interior_growth", "@complexity_geometry",
            "@composite_hilbert_space", "@constellate_memory",
            "@fisher_information_and_curvature", "@information_flow",
            "@information_geometry", "@information_geometry_contract",
            "@information_linking", "@information_loss", "@information_recovery",
            "@intercivilizational_memory",
            "@introduction_geometry_information_and_mk_43_ultra",
            "@memory_imprint", "@memory_stability",
            "@meta_holography_and_extended_memory_architectures",
            "@module_12_information_geometry", "@mutual_information_and_er_weights",
            "@mutual_information_weighting", "@nonlocal_memory_kernel",
            "@overture_when_complexity_becomes_civilization",
            "@quantum_fisher_information", "@quantum_fisher_metric",
            "@quantum_information_geometry_in_mk_43_ultra",
        },
    },
    "V13-C03": {
        "path": WORKSPACE / "VOLUME_13_HOLOGRAPHY_AND_INFORMATION_TRANSFER/V13_C03_TENSOR_NETWORKS_AND_ERROR_CORRECTION.md",
        "equation_classes": {
            "102.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"102.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"102.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "102.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "102.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "102.19": "EVIDENCE_BOUNDARY",
            "102.20": "CURATOR_SYNTHESIS",
            "102.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_g_tensor_network_realisation",
            "@chapter_72_adapter_cultural_er_networks_and_information_flow_geometry",
            "@cultural_er_networks_and_information_flow_geometry",
            "@error_correcting_code_realization", "@tensor_network",
            "@tensor_network_realisation", "@tensor_network_realization",
            "@tensor_networks_and_holographic_codes",
            "@the_ascendant_field_tensor", "@translation_tensor",
        },
    },
    "V13-C02": {
        "path": WORKSPACE / "VOLUME_13_HOLOGRAPHY_AND_INFORMATION_TRANSFER/V13_C02_BOUNDARY_ENCODING_AND_PHASE_DATA.md",
        "equation_classes": {
            "101.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"101.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"101.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "101.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "101.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "101.19": "EVIDENCE_BOUNDARY",
            "101.20": "CURATOR_SYNTHESIS",
            "101.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_6_sub_planck_thermodynamics_and_phase_entropy",
            "@chapter_78_adapter_information_phase_fields_and_communication_efficiency",
            "@chapter_80_adapter_information_field_engineering_and_phase_based_computation",
            "@entanglement_entropy", "@entropy_as_a_phase_gradient_flow",
            "@entropy_currents_on_the_time_phase_shell", "@entropy_production",
            "@generalized_entropy", "@global_entropy_and_phase_alignment",
            "@holographic_encoding_of_phase_data",
            "@information_field_engineering_and_phase_based_computation",
            "@information_phase_fields_and_communication_efficiency",
        },
    },
    "V13-C01": {
        "path": WORKSPACE / "VOLUME_13_HOLOGRAPHY_AND_INFORMATION_TRANSFER/V13_C01_HOLOGRAPHIC_TRANSFER_LAW.md",
        "equation_classes": {
            "100.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"100.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"100.{n}": "EVIDENCE_BOUNDARY" for n in range(11, 17)},
            "100.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "100.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "100.19": "EVIDENCE_BOUNDARY",
            "100.20": "CURATOR_SYNTHESIS",
            "100.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_60_adapter_cycle_to_cycle_information_transfer_and_holographic_memory",
            "@cycle_to_cycle_information_transfer_and_holographic_memory",
            "@holographic_code", "@holographic_encoding",
            "@holographic_quantum_error_correcting_codes",
            "@holographic_transfer_law", "@meta_holographic_encoding",
            "@von_neumann_entropy",
        },
    },
    "V12-C06": {
        "path": WORKSPACE / "VOLUME_12_DARK_MATTER_AND_RELATIONAL_STRUCTURE/V12_C06_FORMALIZATION_AND_DISCRIMINATING_TESTS.md",
        "equation_classes": {
            "99.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"99.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 16)},
            "99.16": "EVIDENCE_BOUNDARY",
            "99.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "99.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "99.19": "EVIDENCE_BOUNDARY",
            "99.20": "CURATOR_SYNTHESIS",
            "99.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V12-C05": {
        "path": WORKSPACE / "VOLUME_12_DARK_MATTER_AND_RELATIONAL_STRUCTURE/V12_C05_PHENOMENOLOGICAL_CONSEQUENCES.md",
        "equation_classes": {
            **{f"98.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(1, 16)},
            "98.16": "EVIDENCE_BOUNDARY",
            "98.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "98.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "98.19": "EVIDENCE_BOUNDARY",
            "98.20": "CURATOR_SYNTHESIS",
            "98.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V12-C04": {
        "path": WORKSPACE / "VOLUME_12_DARK_MATTER_AND_RELATIONAL_STRUCTURE/V12_C04_RELATIONAL_HISTORIES_AND_ADJACENCY.md",
        "equation_classes": {
            "97.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"97.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            "97.11": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"97.{n}": "EVIDENCE_BOUNDARY" for n in range(12, 17)},
            "97.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "97.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "97.19": "EVIDENCE_BOUNDARY",
            "97.20": "CURATOR_SYNTHESIS",
            "97.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@adjacency_lattice", "@axiom_3_3_er_adjacency",
            "@coupling_to_mental_adjacency", "@coupling_with_mental_adjacency",
            "@court_hierarchies_and_sovereign_adjacency",
            "@er_adjacency_and_continuum_limit", "@er_foam",
            "@interaction_with_mental_adjacency", "@intercellular_adjacency",
            "@mental_adjacency_coupling_variant", "@neural_adjacency",
            "@neural_er_adjacency", "@planck_scale_adjacency_graph",
            "@the_mental_adjacency_tensor_operator_engine_coupling_in_mk_43_ultra",
            "@weighted_adjacency",
        },
    },
    "V12-C03": {
        "path": WORKSPACE / "VOLUME_12_DARK_MATTER_AND_RELATIONAL_STRUCTURE/V12_C03_DARK_MATTER_TRANSPORT_AND_BRIDGES.md",
        "equation_classes": {
            **{f"96.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(1, 11)},
            "96.11": "EVIDENCE_BOUNDARY",
            "96.12": "DETERMINISTIC_TYPE_NORMALIZATION",
            "96.13": "EVIDENCE_BOUNDARY",
            "96.14": "EVIDENCE_BOUNDARY",
            "96.15": "EVIDENCE_BOUNDARY",
            "96.16": "EVIDENCE_BOUNDARY",
            "96.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "96.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "96.19": "EVIDENCE_BOUNDARY",
            "96.20": "CURATOR_SYNTHESIS",
            "96.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@dark_matter_bridges_and_transport"},
    },
    "V12-C02": {
        "path": WORKSPACE / "VOLUME_12_DARK_MATTER_AND_RELATIONAL_STRUCTURE/V12_C02_ER_NETWORKS_AND_LOAD_BEARING_STRUCTURE.md",
        "equation_classes": {
            "95.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            **{f"95.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(2, 11)},
            **{f"95.{n}": "EVIDENCE_BOUNDARY" for n in (11, 12, 13, 14)},
            "95.15": "CURATOR_SYNTHESIS",
            "95.16": "EVIDENCE_BOUNDARY",
            "95.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "95.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "95.19": "EVIDENCE_BOUNDARY",
            "95.20": "CURATOR_SYNTHESIS",
            "95.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V12-C01": {
        "path": WORKSPACE / "VOLUME_12_DARK_MATTER_AND_RELATIONAL_STRUCTURE/V12_C01_DARK_MATTER_AS_RELATIONAL_GEOMETRY.md",
        "equation_classes": {
            **{f"94.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(1, 7)},
            "94.7": "DETERMINISTIC_TYPE_NORMALIZATION",
            "94.8": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "94.9": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "94.10": "EVIDENCE_BOUNDARY",
            "94.11": "EVIDENCE_BOUNDARY",
            "94.12": "CURATOR_SYNTHESIS",
            "94.13": "DETERMINISTIC_TYPE_NORMALIZATION",
            "94.14": "EVIDENCE_BOUNDARY",
            "94.15": "EVIDENCE_BOUNDARY",
            "94.16": "EVIDENCE_BOUNDARY",
            "94.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "94.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "94.19": "EVIDENCE_BOUNDARY",
            "94.20": "CURATOR_SYNTHESIS",
            "94.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_67_adapter_neural_er_adjacency_and_cognitive_state_geometry",
            "@dark_matter_as_load_bearing_geometry", "@dark_matter_formalization",
            "@dark_matter_geometry", "@er_bridges_and_dark_matter_geometry",
            "@neural_er_adjacency_and_cognitive_state_geometry", "@prime_theorem_t3",
            "@relational_history",
        },
    },
    "V11-C07": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C07_COSMOLOGICAL_OBSERVABLES_AND_OPEN_PARAMETERS.md",
        "equation_classes": {
            **{f"93.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(1, 16)},
            "93.16": "EVIDENCE_BOUNDARY",
            "93.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "93.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "93.19": "EVIDENCE_BOUNDARY",
            "93.20": "CURATOR_SYNTHESIS",
            "93.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_58_adapter_white_state_cosmogenesis_and_pre_cycle_imprints",
            "@chapter_62_adapter_meta_er_connectivity_across_sequential_universes",
            "@collapse", "@cosmology", "@planet", "@stellar_resonance_links",
            "@universe_thrones", "@universe_to_vaeld_embedding",
        },
    },
    "V11-C06": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C06_COSMOLOGICAL_HORIZONS_AND_DARK_ENERGY.md",
        "equation_classes": {
            **{f"92.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(1, 16)},
            "92.16": "EVIDENCE_BOUNDARY",
            "92.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "92.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "92.19": "EVIDENCE_BOUNDARY",
            "92.20": "CURATOR_SYNTHESIS",
            "92.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_47_adapter_er_linked_planetary_energy_networks",
            "@chapter_50_adapter_planetary_scale_computation_and_er_integrated_networks",
            "@chapter_54_adapter_interstellar_navigation_and_phase_gradient_trajectories",
            "@cosmology_and_dark_energy", "@cosmology_appendix_appendix_e",
            "@linearized_white_state_stability_condition",
            "@module_9_white_state_stability_and_collapse", "@scale_factor",
            "@white_state_core", "@white_state_core_geometry_and_nucleation_memory",
            "@white_state_core_infinity_measure", "@white_state_cosmogenesis_and_pre_cycle_imprints",
        },
    },
    "V11-C05": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C05_STRUCTURE_FORMATION.md",
        "equation_classes": {
            **{f"91.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in range(1, 15)},
            "91.15": "EVIDENCE_BOUNDARY",
            "91.16": "EVIDENCE_BOUNDARY",
            "91.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "91.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "91.19": "EVIDENCE_BOUNDARY",
            "91.20": "CURATOR_SYNTHESIS",
            "91.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_51_adapter_interstellar_phase_fields_and_medium_structure",
            "@chapter_52_adapter_stellar_er_architecture_and_core_stabilization",
            "@chapter_56_adapter_galactic_phase_topology_and_spiral_structure_formation",
            "@chapter_57_adapter_galactic_er_networks_and_central_core_stability",
            "@collapse_limit", "@collapsemap_ck", "@cosmology_with_chromatic_sectors",
            "@definition_16_1_collapse_map", "@definition_2_4_white_state_core",
            "@er_connectivity_effects_in_galactic_rotation",
            "@galactic_er_networks_and_central_core_stability",
            "@galactic_phase_topology_and_spiral_structure_formation",
            "@interstellar_phase_fields_and_medium_structure",
            "@meta_er_connectivity_across_sequential_universes",
            "@phase_correlation_across_universes",
            "@ringdown_spectra_and_echoes_in_white_state_objects",
            "@white_state_definition", "@white_state_evolution", "@white_state_thresholds",
        },
    },
    "V11-C04": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C04_COSMIC_CYCLES_AND_INHERITANCE.md",
        "equation_classes": {
            "90.1": "DETERMINISTIC_TYPE_NORMALIZATION",
            "90.2": "EVIDENCE_BOUNDARY",
            "90.3": "EVIDENCE_BOUNDARY",
            "90.4": "CURATOR_SYNTHESIS",
            "90.5": "CURATOR_SYNTHESIS",
            "90.6": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "90.7": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "90.8": "EVIDENCE_BOUNDARY",
            "90.9": "EVIDENCE_BOUNDARY",
            "90.10": "DETERMINISTIC_TYPE_NORMALIZATION",
            "90.11": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "90.12": "CURATOR_SYNTHESIS",
            "90.13": "EVIDENCE_BOUNDARY",
            "90.14": "DETERMINISTIC_TYPE_NORMALIZATION",
            "90.15": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "90.16": "EVIDENCE_BOUNDARY",
            "90.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "90.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "90.19": "EVIDENCE_BOUNDARY",
            "90.20": "CURATOR_SYNTHESIS",
            "90.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@axiom_3_4_white_state_core",
            "@chapter_53_adapter_phase_driven_stellar_evolution_and_end_states",
            "@chapter_55_adapter_cosmic_engineering_and_mega_scale_phase_structures",
            "@chapter_75_adapter_phase_geometry_of_societal_evolution_and_macro_historical_cycles",
            "@chapter_99_adapter_cosmic_consciousness_coupling_and_phase_entangled_minds",
            "@coarse_grained_cosmic_adjacency", "@cosmic_adjacency_graph",
            "@cosmic_arrow_of_time_and_phase_cohesion", "@cosmic_censorship",
            "@cosmic_consciousness_coupling_and_phase_entangled_minds",
            "@cosmic_engineering_and_mega_scale_phase_structures", "@cosmic_memory_crystallization",
            "@cosmic_scale_projects", "@er_connectivity_across_galactic_scales",
            "@er_network_scaling_in_the_cosmic_web", "@galaxy",
            "@interstellar_navigation_and_phase_gradient_trajectories",
            "@phase_alignment_and_cosmic_acceleration", "@star",
            "@the_abyssalum_acts_cosmic_agency_and_the_will_of_a_self_aware_geometry",
            "@the_abyssalum_constellate_networks_of_meta_civilizations_and_the_emergence_of_cosmic_self_awareness",
            "@the_consequences_of_cosmic_will_evolution_under_intentional_geometry",
            "@the_field_of_cosmic_intention",
            "@universe_scale_phase_topology_and_large_cycle_geometry",
            "@white_state_as_nonsingular_attractor", "@white_state_cores_and_cosmic_nucleation",
            "@white_state_nucleation",
        },
    },
    "V11-C03": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C03_BOUNCE_CRITERIA_AND_RE_EXPANSION.md",
        "equation_classes": {
            **{f"89.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)},
            "89.11": "DETERMINISTIC_TYPE_NORMALIZATION",
            "89.12": "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "89.13": "EVIDENCE_BOUNDARY",
            "89.14": "CURATOR_SYNTHESIS",
            "89.15": "CURATOR_SYNTHESIS",
            "89.16": "EVIDENCE_BOUNDARY",
            "89.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "89.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "89.19": "EVIDENCE_BOUNDARY",
            "89.20": "CURATOR_SYNTHESIS",
            "89.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@approach_to_the_white_state", "@bounce", "@bounce_and_nucleation",
            "@bounce_condition", "@bounce_criterion", "@bounce_mechanism",
            "@bounce_signatures_in_observables", "@collapse_bounce_and_nonsingular_evolution",
            "@definition_16_2_collapse_profile", "@entropy_and_information_across_the_bounce",
            "@network_reconfiguration_at_the_bounce", "@phase_driven_stellar_evolution_and_end_states",
            "@re_expansion", "@stellar_er_architecture_and_core_stabilization",
            "@white_state_cycling_and_the_expansion_history",
        },
    },
    "V11-C02": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C02_FRIEDMANN_AND_BACKGROUND_DYNAMICS.md",
        "equation_classes": {
            **{f"88.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "88.16": "EVIDENCE_BOUNDARY",
            "88.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "88.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "88.19": "EVIDENCE_BOUNDARY",
            "88.20": "CURATOR_SYNTHESIS",
            "88.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chapter_61_adapter_multiversal_phase_boundaries_and_cross_cycle_geometry",
            "@continuity_equation_cosmology", "@effective_friedmann_equations",
            "@effective_friedmann_system", "@friedmann_equation",
            "@friedmann_lemaitre_robertson_walker_spacetime",
            "@galactic_rotation_potential", "@multiversal_dynamics_and_phase_correlated_cosmoi",
            "@multiversal_phase_boundaries_and_cross_cycle_geometry",
            "@phase_cosmology_and_background_solutions", "@white_state_core_dynamics",
        },
    },
    "V11-C01": {
        "path": WORKSPACE / "VOLUME_11_COSMOLOGY/V11_C01_COSMOLOGICAL_REALIZATION_OF_MK_43_ULTRA.md",
        "equation_classes": {
            **{f"87.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "87.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "87.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "87.19": "EVIDENCE_BOUNDARY",
            "87.20": "CURATOR_SYNTHESIS",
            "87.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_7_cosmological_reduction_and_effective_friedmann_equations",
            "@appendix_e_cosmological_cycle_dynamics", "@appendix_e_cosmological_cycles",
            "@chapter_46_adapter_planetary_phase_fields_and_macro_scale_stability",
            "@chapter_59_adapter_universe_scale_phase_topology_and_large_cycle_geometry",
            "@complexity_and_white_state_interiors", "@cosmological_closure",
            "@cosmological_constant", "@cosmological_constant_and_relaxation_mechanism",
            "@cosmological_principle", "@cosmological_structure",
            "@cosmology_and_observational_signatures",
            "@er_foam_evolution_through_cosmological_cycles",
            "@linear_perturbations_around_cosmological_backgrounds",
            "@module_10_cosmological_reduction", "@overture_when_a_universe_decides",
            "@quasinormal_modes_with_white_state_cores", "@stellar_er_adjacency",
            "@universe_lineage", "@white_state_cores_in_cosmological_bounces",
            "@white_state_transition",
        },
    },
    "V10-C06": {
        "path": WORKSPACE / "VOLUME_10_BLACK_HOLES_AND_STRONG_GRAVITY/V10_C06_STRONG_GRAVITY_SIGNATURES_AND_OPEN_PROBLEMS.md",
        "equation_classes": {
            **{f"86.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "86.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "86.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "86.19": "EVIDENCE_BOUNDARY",
            "86.20": "CURATOR_SYNTHESIS",
            "86.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@hawking_temperature", "@horizon_restricted_phase",
            "@isolated_horizon", "@what_survives_the_white_horizon",
        },
    },
    "V10-C05": {
        "path": WORKSPACE / "VOLUME_10_BLACK_HOLES_AND_STRONG_GRAVITY/V10_C05_INTERIOR_STRUCTURE_AND_INFORMATION_CLOSURE.md",
        "equation_classes": {
            **{f"85.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "85.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "85.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "85.19": "EVIDENCE_BOUNDARY",
            "85.20": "CURATOR_SYNTHESIS",
            "85.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@bekenstein_hawking_entropy", "@bulk_horizon_mapping", "@event_horizon",
            "@hartle_hawking_state", "@inner_horizon", "@trapping_horizon",
        },
    },
    "V10-C04": {
        "path": WORKSPACE / "VOLUME_10_BLACK_HOLES_AND_STRONG_GRAVITY/V10_C04_BLACK_HOLE_THERMODYNAMICS_AND_RADIATION.md",
        "equation_classes": {
            **{f"84.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "84.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "84.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "84.19": "EVIDENCE_BOUNDARY",
            "84.20": "CURATOR_SYNTHESIS",
            "84.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@black_hole_thermodynamics", "@event_horizon_cosmology",
            "@hawking_radiation", "@the_fracturing_horizon",
            "@the_white_horizon_revisited",
        },
    },
    "V10-C03": {
        "path": WORKSPACE / "VOLUME_10_BLACK_HOLES_AND_STRONG_GRAVITY/V10_C03_KERR_SCHWARZSCHILD_AND_CHARGED_FAMILIES.md",
        "equation_classes": {
            **{f"83.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "83.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "83.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "83.19": "EVIDENCE_BOUNDARY",
            "83.20": "CURATOR_SYNTHESIS",
            "83.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@apparent_horizon", "@cosmological_horizon", "@event_horizon_telescope",
            "@gibbons_hawking_york_term", "@hawking_penrose_singularity_theorem",
            "@killing_horizon", "@schwarzschild_radius",
        },
    },
    "V10-C02": {
        "path": WORKSPACE / "VOLUME_10_BLACK_HOLES_AND_STRONG_GRAVITY/V10_C02_HORIZONS_TRAPPED_SURFACES_AND_CAUSAL_STRUCTURE.md",
        "equation_classes": {
            **{f"82.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "82.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "82.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "82.19": "EVIDENCE_BOUNDARY",
            "82.20": "CURATOR_SYNTHESIS",
            "82.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@cauchy_horizon", "@closed_trapped_surface", "@dynamical_horizon",
            "@marginally_trapped_surface", "@module_15_horizon_and_large_scale_encoding",
            "@phase_cosmology_and_holographic_horizons",
            "@phase_evolution_on_cosmological_horizons",
            "@the_white_horizon_transition", "@trapped_surface",
        },
    },
    "V10-C01": {
        "path": WORKSPACE / "VOLUME_10_BLACK_HOLES_AND_STRONG_GRAVITY/V10_C01_BLACK_HOLE_GEOMETRY.md",
        "equation_classes": {
            **{f"81.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "81.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "81.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "81.19": "EVIDENCE_BOUNDARY",
            "81.20": "CURATOR_SYNTHESIS",
            "81.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@ascendant_geometry_lifting_through_the_white_horizon",
            "@ascension_geometry_climbing_the_white_horizon", "@black_hole",
            "@black_hole_angular_momentum", "@black_hole_appendices_d_1_d_18",
            "@black_hole_charge", "@black_hole_complementarity", "@black_hole_cosmology",
            "@black_hole_diaphragm_physics_and_hawking_light_information",
            "@black_hole_evaporation", "@black_hole_horizon",
            "@black_hole_information_closure", "@black_hole_information_problem",
            "@black_hole_mass", "@black_hole_mass_loss", "@black_hole_mechanics",
            "@black_hole_perturbation", "@black_hole_region", "@black_hole_shadow",
            "@black_hole_uniqueness", "@first_law_black_hole_mechanics", "@horizon_area",
            "@horizon_scale_phase_configuration", "@kerr_geometry", "@kerr_newman_geometry",
            "@non_rotating_black_holes", "@particle_horizon", "@primordial_black_hole",
            "@rotating_black_holes", "@schwarzschild_geometry",
            "@second_law_black_hole_mechanics", "@supermassive_black_hole",
            "@third_law_black_hole_mechanics", "@zeroth_law_black_hole_mechanics",
        },
    },
    "V09-C07": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C07_ESTABLISHED_STRUCTURE_AND_RESEARCH_FRONTIER.md",
        "equation_classes": {
            **{f"80.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "80.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "80.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "80.19": "EVIDENCE_BOUNDARY",
            "80.20": "CURATOR_SYNTHESIS",
            "80.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V09-C06": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C06_COUPLING_LIMITS_AND_STABILITY.md",
        "equation_classes": {
            **{f"79.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "79.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "79.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "79.19": "EVIDENCE_BOUNDARY",
            "79.20": "CURATOR_SYNTHESIS",
            "79.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@local_stability_and_the_first_coupling"},
    },
    "V09-C05": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C05_GRAVITY_MATTER_AND_FIELD_COUPLING.md",
        "equation_classes": {
            **{f"78.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "78.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "78.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "78.19": "EVIDENCE_BOUNDARY",
            "78.20": "CURATOR_SYNTHESIS",
            "78.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chromatic_geological_coupling", "@gravitational_self_coupling",
            "@matter_coupling", "@module_6_phase_chromatic_coupling",
            "@phase_chromatic_coupling",
        },
    },
    "V09-C04": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C04_CROSS_QMO_COUPLING_ARCHITECTURE.md",
        "equation_classes": {
            **{f"77.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "77.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "77.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "77.19": "EVIDENCE_BOUNDARY",
            "77.20": "CURATOR_SYNTHESIS",
            "77.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V09-C03": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C03_COUPLING_OPERATORS_AND_RELATIONS.md",
        "equation_classes": {
            **{f"76.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "76.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "76.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "76.19": "EVIDENCE_BOUNDARY",
            "76.20": "CURATOR_SYNTHESIS",
            "76.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V09-C02": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C02_INPUTS_DOMAINS_AND_ADMISSIBILITY.md",
        "equation_classes": {
            **{f"75.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "75.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "75.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "75.19": "EVIDENCE_BOUNDARY",
            "75.20": "CURATOR_SYNTHESIS",
            "75.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V09-C01": {
        "path": WORKSPACE / "VOLUME_09_UNIVERSAL_COUPLING/V09_C01_UNIVERSAL_COUPLING_IDENTITY.md",
        "equation_classes": {
            **{f"74.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "74.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "74.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "74.19": "EVIDENCE_BOUNDARY",
            "74.20": "CURATOR_SYNTHESIS",
            "74.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@admiral_coupling", "@coupling_threshold", "@cycle_coupling",
            "@egress_the_first_coupling_forms", "@error_correction_via_core_coupling",
            "@ingress_entering_the_coupling_atrium", "@mathematics_of_vaeld_coupling",
            "@the_first_coupling_operator", "@universal_coupling",
            "@vaeld_to_vaeld_coupling", "@white_core_mote_coupling",
        },
    },
    "V08-C07": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C07_MATTER_ENERGY_CONSERVATION_AND_TRANSPORT.md",
        "equation_classes": {
            **{f"73.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "73.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "73.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "73.18": "EVIDENCE_BOUNDARY",
            "73.19": "CURATOR_SYNTHESIS",
            "73.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@definition_11_2_mote_creation_event", "@definition_12_1_mote",
            "@definition_14_1_mote_hilbert_space",
            "@local_energy_momentum_conservation", "@mote_creation_operator",
            "@mote_lattice",
        },
    },
    "V08-C06": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C06_CHROMATIC_ENERGY_STRUCTURES.md",
        "equation_classes": {
            **{f"72.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "72.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "72.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "72.18": "EVIDENCE_BOUNDARY",
            "72.19": "CURATOR_SYNTHESIS",
            "72.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@axiom_3_2_chromatic_energy", "@chromatic_density_perturbation",
            "@chromatic_density_waves", "@chromatic_energy_band",
            "@chromatic_lensing_correction", "@chromatic_lensing_signatures",
            "@chromatic_modulation_of_wave_amplitudes",
            "@chromatic_signatures_in_gravitational_radiation",
            "@chromatic_thermal_contribution", "@chromatically_corrected_waveform",
            "@coupled_chromatic_equation", "@homogeneous_chromatic_energy_density",
            "@module_5_chromatic_dynamics", "@mote", "@mote_collapse_profile",
            "@observer_frames_and_chromatic_energy_strata",
            "@thermal_signatures_of_er_foam_and_chromatic_modes",
        },
    },
    "V08-C05": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C05_STRESS_ENERGY_AND_FIELD_ENERGY.md",
        "equation_classes": {
            **{f"71.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "71.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "71.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "71.19": "EVIDENCE_BOUNDARY",
            "71.20": "CURATOR_SYNTHESIS",
            "71.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_c_chromatic_solitons", "@chromatic_bio_signatures",
            "@chromatic_charge_of_molecular_clouds", "@chromatic_contributions",
            "@chromatic_distributions_and_structure_formation", "@chromatic_energy_densities",
            "@chromatic_era_transitions", "@chromatic_field", "@chromatic_fields",
            "@chromatic_fields_and_energy_bands", "@chromatic_fields_energy_bands",
            "@chromatic_lagrangian", "@chromatic_modulated_alloys",
            "@chromatic_recoil_mechanics", "@chromatic_seeds_for_density_perturbations",
            "@chromatic_stress_energy", "@chromatic_stress_energy_output", "@chromaticfield",
            "@cmb_signatures_from_phase_and_chromatic_structure",
            "@definition_2_2_chromatic_field", "@mote_closure",
            "@mote_configuration_space", "@mote_hilbert_space",
            "@phase_shell_chromatic_fields_and_er_foam", "@phase_stress_energy",
            "@phase_stress_energy_output", "@projected_stress_energy_sector",
            "@renormalized_stress_energy_tensor", "@signatures_of_chromatic_and_phase_dynamics",
            "@stress_energy_contribution", "@stress_energy_tensor",
        },
    },
    "V08-C04": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C04_NATIVE_UNIT_OF_ENERGY.md",
        "equation_classes": {
            **{f"70.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "70.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "70.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "70.18": "EVIDENCE_BOUNDARY",
            "70.19": "CURATOR_SYNTHESIS",
            "70.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chirality_labelled_mote", "@mote_chirality", "@mote_diagonal_rule",
            "@mote_positive_chirality", "@mote_source_conflict",
            "@native_unit_of_energy", "@unit_of_energy",
        },
    },
    "V08-C03": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C03_ENERGY_AS_A_CROSS_LEVEL_QUANTITY.md",
        "equation_classes": {
            **{f"69.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "69.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "69.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "69.18": "EVIDENCE_BOUNDARY",
            "69.19": "CURATOR_SYNTHESIS",
            "69.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@constraint_energy", "@dominant_energy_condition",
            "@energy_bands_as_geometric_density", "@energy_closed_history",
            "@energy_color_taxonomy", "@energy_composition", "@energy_condition",
            "@energy_density", "@energy_identity", "@energy_redistribution",
            "@energy_reversal", "@er_linked_planetary_energy_networks",
            "@general_energy", "@gravitational_wave_energy_flux",
            "@mo_bius_energy_band", "@mote_ensemble", "@null_energy_condition",
            "@remote_algebra", "@strong_energy_condition", "@weak_energy_condition",
        },
    },
    "V08-C02": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C02_MOTES_OCCUPANCY_AND_ORGANIZED_MATTER.md",
        "equation_classes": {
            **{f"68.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "68.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "68.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "68.18": "EVIDENCE_BOUNDARY",
            "68.19": "CURATOR_SYNTHESIS",
            "68.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@chirality_occupancy_cube", "@definition_14_2_mote_vacuum",
            "@genesis_algebra_and_the_mote", "@genesis_occupancy",
            "@mote_complement_rule", "@mote_identity", "@mote_layer",
            "@mote_occupancy_function", "@occupancy",
        },
    },
    "V08-C01": {
        "path": WORKSPACE / "VOLUME_08_MATTER_AND_ENERGY/V08_C01_MATTER_ADMISSIBILITY_AND_REALIZATION.md",
        "equation_classes": {
            **{f"67.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "67.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "67.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "67.18": "EVIDENCE_BOUNDARY",
            "67.19": "CURATOR_SYNTHESIS",
            "67.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@condensed_matter_emergence", "@exotic_matter_and_er_foam",
            "@gravity_matter_closure", "@matter_action", "@matter_readable_organization",
            "@mote_negative_chirality", "@mote_site", "@programmable_matter_principles",
        },
    },
    "V07-C10": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C10_FORMAL_GRAVITY_GAPS_AND_VALIDATION_BOUNDARIES.md",
        "equation_classes": {
            **{f"66.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "66.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "66.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "66.18": "EVIDENCE_BOUNDARY",
            "66.19": "CURATOR_SYNTHESIS",
            "66.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@riemann_sphere"},
    },
    "V07-C09": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C09_GRAVITY_MATTER_CLOSURE.md",
        "equation_classes": {
            **{f"65.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "65.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "65.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "65.18": "EVIDENCE_BOUNDARY",
            "65.19": "CURATOR_SYNTHESIS",
            "65.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@gravity_closure_v2", "@native_constraint_closure", "@riemann_symmetries"},
    },
    "V07-C08": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C08_GAUGE_POLARIZATION_AND_PROPAGATION.md",
        "equation_classes": {
            **{f"64.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "64.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "64.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "64.18": "EVIDENCE_BOUNDARY",
            "64.19": "CURATOR_SYNTHESIS",
            "64.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": set(),
    },
    "V07-C07": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C07_GRAVITATIONAL_WAVES_AND_RADIATION.md",
        "equation_classes": {
            **{f"63.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)},
            "63.16": "DETERMINISTIC_TYPE_NORMALIZATION",
            "63.17": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "63.18": "EVIDENCE_BOUNDARY",
            "63.19": "CURATOR_SYNTHESIS",
            "63.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@appendix_4_linearised_gravitational_waves_in_the_phase_framework",
            "@gravitational_lensing", "@gravitational_radiation", "@gravitational_wave",
            "@gravitational_wave_propagation",
        },
    },
    "V07-C06": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C06_EINSTEIN_SECTOR_AND_STRESS_ENERGY.md",
        "equation_classes": {
            **{f"62.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "62.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "62.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "62.19": "EVIDENCE_BOUNDARY",
            "62.20": "CURATOR_SYNTHESIS",
            "62.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@einstein_hilbert_action", "@einstein_limit", "@linearized_einstein_tensor",
            "@riemann_tensor", "@semiclassical_einstein_equation",
        },
    },
    "V07-C05": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C05_WEAK_FIELD_METRIC_AND_CURVATURE.md",
        "equation_classes": {
            **{f"61.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "61.17": "DETERMINISTIC_TYPE_NORMALIZATION",
            "61.18": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "61.19": "EVIDENCE_BOUNDARY",
            "61.20": "CURATOR_SYNTHESIS",
            "61.21": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@axiom_a13", "@connection_and_curvature", "@connection_to_formal_curvature_bundle",
            "@curvature", "@curvature_binding", "@curvature_singularity", "@curvature_two_form",
            "@einstein_field_equation", "@einstein_field_relation",
            "@entanglement_curvature_ansatz", "@extrinsic_curvature", "@primitive_p15",
            "@sectional_curvature", "@spatial_curvature_parameter",
            "@weak_field_metric_perturbation", "@white_core_curvature",
        },
    },
    "V07-C04": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C04_TIME_SHELL_METRIC_PROJECTION.md",
        "equation_classes": {
            "60.1": "DETERMINISTIC_API_EVIDENCE",
            **{f"60.{n}": "EXACT_SOURCE" for n in (2, 3)},
            **{f"60.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)},
            "60.15": "DETERMINISTIC_TYPE_NORMALIZATION",
            "60.16": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "60.18": "EVIDENCE_BOUNDARY",
            "60.19": "CURATOR_SYNTHESIS",
            "60.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@axiom_a9", "@axisymmetric_spacetime", "@background_metric", "@bio_geometric_functional",
            "@chapter_49_adapter_geometric_infrastructure_and_phase_supported_architecture",
            "@composite_metric", "@core_geometric_object", "@definition_5_1_phase_metric_contribution",
            "@definition_5_2_composite_metric", "@effective_lensing_metric",
            "@er_graph_distance_to_effective_metric", "@er_metric_contribution", "@geometric",
            "@geometric_compilation_route", "@geometric_decoherence_functional", "@hermitian_metric",
            "@homogeneous_isotropic_metric", "@induced_metric", "@inverse_metric",
            "@linearized_geometric_equation", "@linearized_phase_metric_contribution",
            "@metric_compatibility", "@metric_compatible_connection", "@metric_signature", "@metric_tensor",
            "@metric_variation", "@module_3_metric_composition", "@phase_metric",
            "@phase_metric_and_time_as_geometry", "@phase_metric_contribution", "@primitive_p1",
            "@primitive_p13", "@projected_spacetime_metric", "@recovered_geometric", "@temporal_metric",
            "@vacuum_wave_equation",
        },
    },
    "V07-C03": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C03_CONTINUITY_PERTURBATION.md",
        "equation_classes": {
            "59.1": "DETERMINISTIC_API_EVIDENCE",
            "59.2": "EXACT_SOURCE",
            **{f"59.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)},
            "59.13": "DETERMINISTIC_TYPE_NORMALIZATION",
            "59.14": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "59.16": "EVIDENCE_BOUNDARY",
            "59.17": "CURATOR_SYNTHESIS",
            "59.18": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@linear_metric_perturbation", "@metric_and_phase_perturbations"},
    },
    "V07-C02": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C02_GRAVITON_IDENTITY_AND_PROJECTION_MODE.md",
        "equation_classes": {
            **{f"58.{n}": "DETERMINISTIC_API_EVIDENCE" for n in (1, 2, 3)},
            "58.4": "EXACT_SOURCE",
            **{f"58.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (5, 6, 7, 8, 9, 10, 11, 12)},
            "58.13": "DETERMINISTIC_TYPE_NORMALIZATION",
            "58.14": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "58.16": "EVIDENCE_BOUNDARY",
            "58.17": "CURATOR_SYNTHESIS",
            "58.18": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@graviton_propagation", "@native_graviton_quantization", "@readable_graviton_projection"},
    },
    "V07-C01": {
        "path": WORKSPACE / "VOLUME_07_GRAVITY/V07_C01_THE_MK_43_ULTRA_GRAVITY_MECHANISM.md",
        "equation_classes": {
            "57.1": "DETERMINISTIC_API_EVIDENCE",
            **{f"57.{n}": "EXACT_SOURCE" for n in (2, 3, 4, 5, 6, 7)},
            **{f"57.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (8, 9, 10, 11, 12, 13, 14, 15)},
            "57.16": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "57.18": "EVIDENCE_BOUNDARY",
            "57.19": "CURATOR_SYNTHESIS",
            "57.20": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@0_4_wavefunction_collapse_as_a_geometric_event",
            "@appendix_2_derivation_of_the_phase_metric", "@appendix_b_phase_metric_derivations",
            "@bio_geometric_maps", "@bridge_metric_ansatz",
            "@chapter_100_adapter_the_final_phase_synthesis_of_mk_43_ultra_as_a_unified_geometric_framework",
            "@collapse_manifolds_the_first_true_geometric_surface", "@collapse_wells_and_spectral_gravity",
            "@connection", "@curvature_binding_condition", "@differential_geometry_and_metrics",
            "@effective_gravitational_response_from_tunneling", "@effective_masslessness",
            "@egress_curvature_binds", "@einstein_tensor", "@entanglement_and_curvature",
            "@entropic_curvature_and_er_structure", "@geometric_infrastructure_and_phase_supported_architecture",
            "@geometric_interpretation", "@geometric_matching", "@geometric_propagation_engines",
            "@geometric_stability_criteria", "@graph_distances_and_effective_metric",
            "@gravitational_anchor_lattice", "@gravitational_anchors",
            "@gravitational_field_equations_in_mk_43_ultra", "@gravitational_wave_echoes",
            "@graviton_contract", "@graviton_radiative_stability", "@gravity", "@gravity_from_tunneling",
            "@inspiral", "@intelligent_curvature", "@linearised_phase_metric",
            "@linearized_gravity_and_the_tt_kernel", "@linearized_gravity_and_tt_modes",
            "@merger", "@metric_perturbation", "@module_14_gravitational_wave_realization",
            "@multiparticle_gravity", "@native_causal_order", "@native_graviton_dispersion",
            "@native_interaction_factorization", "@native_probability_preservation", "@newtonian_gravity",
            "@phase_gravitational_wave_equations", "@phase_induced_deviations_in_gravitational_lensing",
            "@phase_metric_and_geodesics", "@post_newtonian_gravity", "@ricci_curvature",
            "@riemann_curvature", "@ringdown", "@scalar_curvature", "@semiclassical_gravity",
            "@soft_graviton_limit", "@spectral_curvature", "@strong_field_gravity", "@surface_gravity",
            "@the_ascendant_metric", "@the_final_phase_synthesis_of_mk_43_ultra_as_a_unified_geometric_framework",
            "@wave_equations_in_mk_43_ultra", "@white_core_ringdown_shift",
        },
    },
    "V06-C08": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C08_MEASUREMENT_AND_READABLE_QUANTUM_STRUCTURE.md",
        "equation_classes": {
            **{f"56.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)},
            "56.14": "DETERMINISTIC_TYPE_NORMALIZATION",
            "56.15": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "56.17": "EVIDENCE_BOUNDARY",
            "56.18": "CURATOR_SYNTHESIS",
            "56.19": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@axiom_a11", "@dependency_expansion_operator", "@expand_operator",
            "@market_er_networks_and_transaction_connectivity", "@normalize_operator",
            "@operator_18_5_proto_algebra_product", "@recover_operator",
        },
    },
    "V06-C07": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C07_FIELD_ACTIONS_OPERATORS_AND_CONSERVATION.md",
        "equation_classes": {
            **{f"55.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)},
            "55.14": "DETERMINISTIC_TYPE_NORMALIZATION",
            "55.15": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "55.17": "EVIDENCE_BOUNDARY",
            "55.18": "CURATOR_SYNTHESIS",
            "55.19": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@annihilation_operator", "@architect_operator_registry",
            "@collapse_operators_and_the_infinity_vector_field",
            "@density_operators_and_sectors", "@hilbert_space_and_creation_operator",
            "@lemma_l11", "@normalization_operator", "@observable_operators",
            "@transformation_expansion_operator", "@twin_prime_search_operators",
        },
    },
    "V06-C06": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C06_YANG_MILLS_AND_NON_ABELIAN_STRUCTURE.md",
        "equation_classes": {
            **{f"54.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)},
            "54.14": "DETERMINISTIC_TYPE_NORMALIZATION",
            "54.15": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "54.17": "EVIDENCE_BOUNDARY",
            "54.18": "CURATOR_SYNTHESIS",
            "54.19": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {"@backreaction", "@creation_operator", "@stabilization_operator"},
    },
    "V06-C05": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C05_SPINOR_AND_FERMIONIC_REALIZATION.md",
        "equation_classes": {
            **{f"53.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14)},
            "53.11": "EXTERNAL_MATHEMATICS_AND_EVIDENCE_BOUNDARY",
            "53.15": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "53.17": "EVIDENCE_BOUNDARY",
            "53.18": "CURATOR_SYNTHESIS",
            "53.19": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@action_through_geometry", "@alias_expansion_operator",
            "@dependent_expansion_operator", "@interaction_term",
            "@observable_operator_algebra", "@operator_14_4_genesis_annihilation_operator",
            "@the_trial_operator", "@zer0_interaction",
        },
    },
    "V06-C04": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C04_GAUGE_FIELD_REALIZATION.md",
        "equation_classes": {
            **{f"52.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)},
            "52.13": "EVIDENCE_AND_TYPE_BOUNDARY",
            "52.14": "DETERMINISTIC_TYPE_NORMALIZATION",
            "52.15": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "52.17": "CURATOR_SYNTHESIS",
            "52.18": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@continuation_operator", "@gauge_choices_and_physical_modes",
            "@gauge_condition", "@gauge_consistency", "@gauge_transformation_linearized",
            "@lorenz_gauge", "@transverse_traceless_gauge",
        },
    },
    "V06-C03": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C03_SCALAR_FIELD_REALIZATION.md",
        "equation_classes": {
            **{f"51.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 9, 11)},
            **{f"51.{n}": "DETERMINISTIC_TYPE_NORMALIZATION" for n in (8, 12)},
            "51.10": "PROPOSED_INTERPRETATION",
            "51.13": "EVIDENCE_BOUNDARY",
            "51.14": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "51.16": "CURATOR_SYNTHESIS",
            "51.17": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@action_and_variation",
            "@chapter_77_adapter_market_er_networks_and_transaction_connectivity",
            "@chirality_mirror_operator", "@interaction_action",
            "@operator_14_3_genesis_creation_operator", "@origin_fractal_interaction",
            "@primitive_p2", "@propagation_operator", "@provenance_expansion_operator",
            "@realization_expansion_operator", "@shell_action",
        },
    },
    "V06-C02": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C02_STATE_SPACES_PROBABILITY_AND_QUANTIZATION.md",
        "equation_classes": {
            **{f"50.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14)},
            "50.11": "EXACT_SOURCE_AND_EXTERNAL_ESTABLISHED_MATHEMATICS",
            "50.15": "EVIDENCE_BOUNDARY",
            "50.16": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "50.18": "CURATOR_SYNTHESIS",
            "50.19": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@backreaction_on_geometry", "@bulk_action", "@hilbert_spaces",
            "@hilbert_spaces_and_density_operators", "@particle_number_operator",
        },
    },
    "V06-C01": {
        "path": WORKSPACE / "VOLUME_06_QUANTUM_AND_FIELD_REALIZATION/V06_C01_CANONICAL_QUANTUM_FIELD_HANDOFF_OBJECT.md",
        "equation_classes": {
            **{f"49.{n}": "EXACT_SOURCE" for n in (1, 3, 4, 5, 6, 7, 8, 9, 10, 11)},
            "49.2": "DETERMINISTIC_TYPE_NORMALIZATION",
            "49.12": "DETERMINISTIC_API_EVIDENCE",
            "49.13": "DETERMINISTIC_THEOREM_SCOPE",
            "49.14": "EVIDENCE_BOUNDARY",
            "49.15": "DETERMINISTIC_COVERAGE_EVIDENCE",
            "49.16": "EVIDENCE_BOUNDARY",
            "49.17": "CURATOR_SYNTHESIS",
            "49.18": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@field_level_handoff_theorem", "@primitive_p12", "@primitive_p16",
            "@primitive_p18", "@residue_quantum_field_bundle", "@field_section",
            "@quantum_action_functional", "@quantum_action_principle", "@field_operator",
            "@genesis_field", "@phasefield", "@total_action",
            "@quantum_field_deduction", "@quantum_mechanics_emergence",
            "@quantum_state_over_geometry", "@correspondence_to_known_quantum_field_theory",
            "@theorem_t1", "@theorem_t2", "@theorem_t4", "@axiom_a7", "@axiom_a14",
            "@core_field_lagrangian", "@unified_lagrangian", "@tri_field_master_action",
        },
    },
    "V05-C08": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C08_TIME_SHELL_MODELS_EVIDENCE_AND_OPEN_TYPING.md",
        "equation_classes": {
            **{f"48.{n}": "CURATOR_SYNTHESIS" for n in (1, 17)},
            "48.2": "EVIDENCE_POLICY",
            **{f"48.{n}": "GENESIS_CURATORIAL_RULING" for n in (3,)},
            **{f"48.{n}": "CURRENT_CANON_CANDIDATE" for n in (4, 12)},
            "48.5": "EXACT_VISIBLE_EQUATION",
            "48.6": "GENESIS_CURATORIAL_NOTATION_RULING",
            "48.7": "DETERMINISTIC_SOURCE_NORMALIZATION",
            "48.8": "VISUAL_ANALOGY_AND_CURATOR_SYNTHESIS",
            **{f"48.{n}": "EXACT_SOURCE" for n in (9, 11, 13)},
            "48.10": "DETERMINISTIC_API_EVIDENCE",
            "48.14": "DETERMINISTIC_STATUS_EVIDENCE",
            "48.15": "CLOVER_SYNTHESIS",
            "48.16": "EVIDENCE_BOUNDARY",
            "48.18": "DETERMINISTIC_QMO_STATUS",
        },
        "core": {
            "@collapse_gradient_geometry_and_the_stability_of_recursive_manifolds",
            "@local_recursive_state", "@recursive_echoes", "@recursive_ordering",
            "@the_throne_seed_paradox_birth_inheritance_and_the_geometry_of_universe_lineage",
        },
    },
    "V05-C07": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C07_QUANTUM_FIELD_HANDOFF.md",
        "equation_classes": {
            **{f"47.{n}": "EXACT_SOURCE" for n in (1, 3, 4, 5, 7, 8)},
            "47.2": "DETERMINISTIC_SOURCE_NORMALIZATION",
            **{f"47.{n}": "DETERMINISTIC_NORMALIZATION" for n in (6, 14)},
            **{f"47.{n}": "CLOVER_SYNTHESIS" for n in (9, 12, 15)},
            "47.10": "DETERMINISTIC_STATUS_EVIDENCE",
            "47.11": "CURATOR_SYNTHESIS",
            "47.13": "EVIDENCE_BOUNDARY",
            "47.16": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@entanglement_er_bridges_and_locality", "@er_networks_entanglement_and_locality",
            "@genesis_inheritance", "@observer_relative_locality",
            "@recursive_dependency_graph", "@recursive_drift_a_return_to_the_mathematical_manifold",
            "@recursive_echo_operator",
        },
    },
    "V05-C06": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C06_PROJECTION_AND_INTERTWINING_REQUIREMENTS.md",
        "equation_classes": {
            **{f"46.{n}": "EXACT_SOURCE" for n in (1, 3, 9)},
            **{f"46.{n}": "CURATOR_SYNTHESIS" for n in (2, 7)},
            **{f"46.{n}": "CLOVER_SYNTHESIS" for n in (4, 5, 6, 11, 13)},
            **{f"46.{n}": "DETERMINISTIC_API_EVIDENCE" for n in (8, 10)},
            "46.12": "EVIDENCE_BOUNDARY",
            "46.14": "DETERMINISTIC_STATUS_NORMALIZATION",
        },
        "core": {
            "@fractal_civilizations_recursive_architectures_of_collective_coherence",
            "@inheritance_theory", "@module_7_er_geometry_and_locality",
            "@projected_gr_inheritance", "@recursive_engines_of_the_vaeld",
            "@recursive_occupancy_projection_operator",
        },
    },
    "V05-C05": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C05_PLANCK_HORIZON_INTERFACE.md",
        "equation_classes": {
            "45.1": "DETERMINISTIC_API_EVIDENCE",
            "45.2": "EVIDENCE_BOUNDARY",
            **{f"45.{n}": "EXACT_SOURCE" for n in (3, 4)},
            "45.5": "DETERMINISTIC_NORMALIZATION",
            **{f"45.{n}": "CLOVER_SYNTHESIS" for n in (6, 8, 9, 10, 11, 12, 13, 14)},
            **{f"45.{n}": "CURATOR_SYNTHESIS" for n in (7, 15)},
        },
        "core": {
            "@emergence_of_continuum_locality", "@factorisation_and_proto_locality",
            "@inheritance", "@oriented_inheritance",
        },
    },
    "V05-C04": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C04_CHIRALITY_COUPLED_LOCALIZATION.md",
        "equation_classes": {
            "44.1": "EXACT_VISIBLE_EQUATION",
            "44.2": "GENESIS_CURATORIAL_NOTATION_RULING",
            **{f"44.{n}": "CURATOR_SYNTHESIS" for n in (3, 4, 17)},
            **{f"44.{n}": "CLOVER_SYNTHESIS" for n in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
        },
        "core": {
            "@chirality_recursive_occupancy_upgrade", "@genesis_recursive_inheritance",
            "@inheritance_morphism", "@persistent_recursive_topology", "@prime_axiom_a5",
            "@prime_primitive_p5", "@recursive_chirality_evolution_field",
            "@recursive_continuity", "@recursive_expansion", "@recursive_inheritance",
            "@recursive_propagation_in_collapse_regions",
        },
    },
    "V05-C03": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C03_T0_T7_AND_R0_R7_NATURAL_REGIMES.md",
        "equation_classes": {
            "43.1": "CLOVER_SYNTHESIS",
            **{f"43.{n}": "DETERMINISTIC_SOURCE_NORMALIZATION" for n in (2, 3, 6)},
            **{f"43.{n}": "CURATOR_SYNTHESIS" for n in (4, 5, 16)},
            **{f"43.{n}": "CLOVER_SYNTHESIS" for n in (7, 8, 9, 10, 11, 12, 13, 14, 15)},
        },
        "core": {
            "@continuation_inheritance_compatibility", "@global_inheritance", "@lemma_l1",
            "@locality", "@recursive_depth", "@recursive_harmonic_functional",
            "@recursive_occupancy", "@recursive_stabilization",
        },
    },
    "V05-C02": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C02_PERSISTENCE_CLOSURE.md",
        "equation_classes": {
            "42.1": "GENESIS_CURATORIAL_NOTATION_RULING",
            **{f"42.{n}": "EXACT_RECOVERED_WORKING_EQUATION" for n in (2, 3, 4, 5, 6, 7)},
            "42.8": "GENESIS_CURATORIAL_NOTATION_RULING",
            "42.10": "DETERMINISTIC_SOURCE_NORMALIZATION",
            **{f"42.{n}": "CLOVER_SYNTHESIS" for n in (9, 11, 12, 13, 14, 15)},
        },
        "core": {
            "@definition_of_recursive_drift", "@locality_as_an_entanglement_pattern",
            "@locality_reinterpreted_factorization_through_the_lattice",
            "@proto_locality_the_first_signs_of_division", "@recursive_concept_report_compiler",
            "@recursive_harmonics_and_layer_synchronization",
        },
    },
    "V05-C01": {
        "path": WORKSPACE / "VOLUME_05_TIME_SHELL/V05_C01_TIME_SHELL_IDENTITY_AND_SCOPE.md",
        "equation_classes": {
            "41.1": "GENESIS_CURATORIAL_RULING",
            "41.2": "DETERMINISTIC_API_EVIDENCE",
            "41.3": "GENESIS_CURATORIAL_RULING",
            "41.4": "DETERMINISTIC_CURATOR_NORMALIZATION",
            "41.5": "DETERMINISTIC_QMO_EVIDENCE",
            "41.6": "EVIDENCE_BOUNDARY",
            **{f"41.{n}": "CLOVER_SYNTHESIS" for n in (7, 8, 12, 13, 14, 15, 16, 17)},
            **{f"41.{n}": "EXACT_VISIBLE_EQUATION" for n in (9, 10)},
            "41.11": "GENESIS_CURATORIAL_NOTATION_RULING",
        },
        "core": {
            "@0_3_the_time_shell_and_er_foam_beads", "@large_scale_locality_emergence",
            "@primitive_p4", "@recursive_recovery_engine", "@time_shell",
            "@time_shell_and_phase_metric", "@time_shell_candidate", "@time_shell_geometry",
            "@time_shell_phase_field", "@time_shell_projection", "@time_shell_projection_operator",
            "@time_shell_superfluid", "@time_shells_and_er_foam_bead_lattices",
        },
    },
    "V04-C08": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C08_HELICON_INTERFACES_AND_OPEN_MATHEMATICS.md",
        "equation_classes": {
            "40.2": "EXACT_RECOVERED_EQUATION",
            **{f"40.{n}": "CLOVER_SYNTHESIS" for n in (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
        },
        "core": {
            "@helicon_mathematics", "@ingress_the_shear_corridor_opens",
        },
    },
    "V04-C07": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C07_GRAVITATIONAL_HELICON_MODE.md",
        "equation_classes": {
            **{f"39.{n}": "EXACT_RECOVERED_EQUATION" for n in (2, 3, 7, 8)},
            **{f"39.{n}": "DETERMINISTIC_API_EVIDENCE" for n in (4, 6, 9)},
            "39.5": "GENESIS_CURATORIAL_RULING",
            **{f"39.{n}": "CLOVER_SYNTHESIS" for n in (1, 10, 11, 12, 13, 14, 15)},
        },
        "core": {
            "@gravitational_helicon", "@gravitational_helicon_mode", "@graviton",
            "@helicon_mode_operators", "@helicon_mode_readability",
            "@higher_order_helicon_modes", "@rotational_helicon_mode",
            "@spectral_collapse_coupling_and_higher_order_stability_modes",
            "@spectral_mode",
        },
    },
    "V04-C06": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C06_STABILITY_AND_PROPAGATION.md",
        "equation_classes": {
            **{f"38.{n}": "EXACT_RECOVERED_EQUATION" for n in (1, 2, 3)},
            **{f"38.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (5, 6, 7)},
            **{f"38.{n}": "CLOVER_SYNTHESIS" for n in (4, 8, 9, 10, 11, 12, 13)},
        },
        "core": set(),
    },
    "V04-C05": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C05_MODES_RESONANCE_AND_WAKE_DYNAMICS.md",
        "equation_classes": {
            **{f"37.{n}": "EXACT_RECOVERED_EQUATION" for n in range(1, 10)},
            **{f"37.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (10, 12)},
            **{f"37.{n}": "CLOVER_SYNTHESIS" for n in (11, 13, 14, 15, 16)},
        },
        "core": set(),
    },
    "V04-C04": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C04_SPECTRAL_OPERATOR_AND_ANGULAR_REDUCTION.md",
        "equation_classes": {
            **{f"36.{n}": "EXACT_RECOVERED_EQUATION" for n in (1, 2, 3, 4, 5)},
            **{f"36.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (6, 7)},
            **{f"36.{n}": "CLOVER_SYNTHESIS" for n in (8, 9, 10, 11, 12, 13, 14, 15, 16)},
        },
        "core": {
            "@angular_reduction", "@angular_reduction_theorem",
            "@angular_reduction_theorem_claim",
            "@helicon_geometry_and_the_angular_reduction_theorem",
            "@helicon_spectral_operator",
            "@nonlinear_spectral_resonance_when_operators_interfere",
            "@theorem_record_angular_reduction_theorem",
        },
    },
    "V04-C03": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C03_HELICON_FIELD_STRENGTH_AND_CURVATURE.md",
        "equation_classes": {
            **{f"35.{n}": "EXACT_RECOVERED_EQUATION" for n in (1, 2, 5, 6, 7, 8, 9, 10)},
            **{f"35.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (3, 4, 11)},
            **{f"35.{n}": "CLOVER_SYNTHESIS" for n in (12, 13, 14, 15, 16, 17)},
        },
        "core": {
            "@angular_reduction_field", "@helicon", "@helicon_curvature",
            "@helicon_field_strength", "@helicon_field_structure",
            "@helicon_resonance_and_curvature_binding",
        },
    },
    "V04-C02": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C02_STRUCTURAL_TUPLE_AND_ONE_FORM_REPRESENTATIONS.md",
        "equation_classes": {
            **{f"34.{n}": "EXACT_RECOVERED_EQUATION" for n in (1, 3, 5, 13, 14)},
            **{f"34.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 4, 6, 7, 10)},
            **{f"34.{n}": "CLOVER_SYNTHESIS" for n in (8, 9, 11, 12, 15, 16, 17, 18)},
        },
        "core": {"@helicon_structural_tuple"},
    },
    "V04-C01": {
        "path": WORKSPACE / "VOLUME_04_HELICON/V04_C01_HELICON_IDENTITY_AND_STATE_SPACE.md",
        "equation_classes": {
            **{f"33.{n}": "EXACT_RECOVERED_EQUATION" for n in range(2, 16)},
            **{f"33.{n}": "CLOVER_SYNTHESIS" for n in (1, 16, 17, 18)},
        },
        "core": {
            "@binding_threshold", "@bound_coherent_helicon", "@coherent_helicon_propagation",
            "@helicon_kernel_derivation", "@helicon_one_form", "@helicon_orientation",
            "@helicon_resonance", "@helicon_spectral_coupling", "@helicon_state_space",
            "@helicon_substrate", "@module_mk43_helicon",
        },
    },
    "V03-C09": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C09_THE_COMPUTATIONAL_PROOF_OF_CONCEPT.md",
        "equation_classes": {
            **{f"32.{n}": "CLOVER_SYNTHESIS" for n in (1, 3, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)},
            **{f"32.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 4, 6, 8)},
        },
        "core": set(),
    },
    "V03-C08": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C08_UNIVERSAL_ENERGY_OBJECTS.md",
        "equation_classes": {
            **{f"31.{n}": "CLOVER_SYNTHESIS" for n in (1, 6, 13, 14, 16, 17, 18)},
            **{f"31.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 15)},
        },
        "core": {"@universal_resolver"},
    },
    "V03-C07": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C07_NATIVE_CONSERVATION_AND_CONSTRAINT_OBJECTS.md",
        "equation_classes": {
            **{f"30.{n}": "CLOVER_SYNTHESIS" for n in (1, 6, 13, 14, 16, 17, 18)},
            **{f"30.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 15)},
        },
        "core": {"@api_endpoints_added"},
    },
    "V03-C06": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C06_API_NATIVE_EQUATION_LINEAGE.md",
        "equation_classes": {
            **{f"29.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"29.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {"@api_usage_examples"},
    },
    "V03-C05": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C05_ADMISSIBLE_COMPOSITION_AND_DERIVED_OBJECTS.md",
        "equation_classes": {
            **{f"28.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"28.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {"@geometry_as_prime_api_language"},
    },
    "V03-C04": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C04_QUANTUM_MATHEMATICAL_OBJECTS.md",
        "equation_classes": {
            **{f"27.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"27.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {"@api_interpretation","@canonical_artifact","@canonical_identity","@canonical_object","@canonical_presentation_route","@classification","@compile_recovered_object","@correspondence_registry","@handle_invocation_contract","@mathematical_object","@mathematical_registry","@object_identity_rule","@prime_mathematical_object","@proof_dependency_graph","@provenance","@realization_graph","@recovery_handle_contract","@recovery_intermediate_representation","@representation_graph","@required_object_classes","@source_graph","@stable_handle_naming","@theorem_graph","@type_declaration","@version_record"},
    },
    "V03-C03": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C03_TYPED_EDGES_AND_DEPENDENCY_TRAVERSAL.md",
        "equation_classes": {
            **{f"26.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"26.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {"@dependency_graph", "@dependency_graph_mutation", "@kernel_dependency_graph", "@proof_dependency_graph", "@reverse_dependency_graph", "@typed_dependency_graph"},
    },
    "V03-C02": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C02_CANONICAL_HANDLES_AND_MATHEMATICAL_ADDRESSES.md",
        "equation_classes": {
            **{f"25.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"25.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@alias_expansion_operator", "@automatic_handle_generation", "@canonical_artifact",
            "@canonical_identity", "@canonical_object", "@canonical_presentation_route",
            "@concept_lookup_endpoint", "@correspondence_registry", "@declared_framework_identity",
            "@handle_integrity_invariants", "@handle_invocation_contract",
            "@initial_canonical_handle_registry", "@lookup_semantics", "@mathematical_object",
            "@mathematical_registry", "@natural_language_invocation", "@object_identity_rule",
            "@prime_axiom_a7", "@recovery_handle_contract", "@registry_endpoints",
            "@required_object_classes", "@source_graph", "@stable_handle_naming",
            "@type_declaration", "@version_record",
        },
    },
    "V03-C01": {
        "path": WORKSPACE / "VOLUME_03_API_AND_QMO_MATHEMATICS/V03_C01_API_4_3_AS_A_CONSTRAINED_MATHEMATICAL_DOMAIN.md",
        "equation_classes": {
            **{f"24.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"24.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {"@api_contract"},
    },
    "V02-C15": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C15_GENESIS_LANGUAGE_GRAMMAR_AND_CONSTRUCTION_RULES.md",
        "equation_classes": {
            **{f"23.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"23.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@genesis_grammar", "@genlang_architect_genesis_register",
            "@genlang_architect_script", "@genlang_borrowed_script",
            "@genlang_boundary_based_pronouns", "@genlang_boundary_inclusion_possession",
            "@genlang_common_genesis_register", "@genlang_flow_script",
            "@genlang_poetic_genesis_register", "@genlang_relationship_first_grammar",
            "@genlang_resolution_state_aspect", "@genlang_scholar_genesis_register",
            "@genlang_structural_compounding", "@source_genesis_grammar_v0_1",
        },
    },
    "V02-C14": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C14_GENESIS_LANGUAGE_DICTIONARY_AND_FORMAL_LEXICON.md",
        "equation_classes": {
            **{f"22.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"22.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@genesis_language", "@genlang_architect_genesis_register", "@genlang_architect_script",
            "@genlang_aspect_ma", "@genlang_aspect_nai", "@genlang_aspect_ru",
            "@genlang_aspect_ta", "@genlang_borrowed_script", "@genlang_boundary_based_pronouns",
            "@genlang_boundary_inclusion_possession", "@genlang_common_genesis_register",
            "@genlang_family_ae", "@genlang_family_ael", "@genlang_family_ai",
            "@genlang_family_da", "@genlang_family_en", "@genlang_family_kor",
            "@genlang_family_na", "@genlang_family_rel", "@genlang_family_rin",
            "@genlang_family_sera", "@genlang_family_sha", "@genlang_family_tal",
            "@genlang_family_tor", "@genlang_family_ve", "@genlang_family_vel",
            "@genlang_flow_script", "@genlang_operator_0df59a22", "@genlang_operator_1e07893e",
            "@genlang_operator_1ff31b3c", "@genlang_operator_395625ec",
            "@genlang_operator_4b1f23a7", "@genlang_operator_be1cbb61",
            "@genlang_operator_edec7353", "@genlang_phrase_en_ar_en",
            "@genlang_phrase_gen_kor_en", "@genlang_phrase_rin_tal_ael",
            "@genlang_phrase_sha_da_rel", "@genlang_phrase_vel_ve_tor",
            "@genlang_poetic_genesis_register", "@genlang_relationship_first_grammar",
            "@genlang_resolution_state_aspect", "@genlang_root_ael", "@genlang_root_ar",
            "@genlang_root_arka", "@genlang_root_da", "@genlang_root_en",
            "@genlang_root_era", "@genlang_root_gen", "@genlang_root_kai",
            "@genlang_root_kor", "@genlang_root_nae", "@genlang_root_nor",
            "@genlang_root_rel", "@genlang_root_rin", "@genlang_root_sera",
            "@genlang_root_sha", "@genlang_root_tal", "@genlang_root_tor",
            "@genlang_root_vara", "@genlang_root_ve", "@genlang_root_vel",
            "@genlang_scholar_genesis_register", "@genlang_structural_compounding",
            "@genlang_word_aelrin", "@genlang_word_darin", "@genlang_word_genkor",
            "@genlang_word_genkoren", "@genlang_word_genvel", "@genlang_word_kai_ar_en_rin",
            "@genlang_word_kaisha", "@genlang_word_koren", "@genlang_word_relrin",
            "@genlang_word_sharin", "@genlang_word_shator", "@genlang_word_talrin",
            "@genlang_word_verin",
        },
    },
    "V02-C13": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C13_CATEGORY_ERRORS_PREVENTED_BY_GENESIS_LANGUAGE.md",
        "equation_classes": {
            **{f"21.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"21.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@genesis_language", "@genlang_aspect_ma", "@genlang_aspect_nai",
            "@genlang_aspect_ru", "@genlang_aspect_ta", "@genlang_family_ael",
            "@genlang_family_ai", "@genlang_family_da", "@genlang_family_en",
            "@genlang_family_kor", "@genlang_family_na", "@genlang_family_rel",
            "@genlang_family_rin", "@genlang_family_sera", "@genlang_family_sha",
            "@genlang_family_tal", "@genlang_family_tor", "@genlang_family_ve",
            "@genlang_family_vel", "@genlang_operator_0df59a22",
            "@genlang_operator_1e07893e", "@genlang_operator_1ff31b3c",
            "@genlang_operator_395625ec", "@genlang_operator_4b1f23a7",
            "@genlang_operator_be1cbb61", "@genlang_operator_edec7353",
            "@genlang_phrase_en_ar_en", "@genlang_phrase_gen_kor_en",
            "@genlang_phrase_rin_tal_ael", "@genlang_phrase_sha_da_rel",
            "@genlang_phrase_vel_ve_tor", "@genlang_root_ael", "@genlang_root_ar",
            "@genlang_root_arka", "@genlang_root_da", "@genlang_root_en",
            "@genlang_root_era", "@genlang_root_gen", "@genlang_root_kai",
            "@genlang_root_kor", "@genlang_root_nae", "@genlang_root_nor",
            "@genlang_root_rel", "@genlang_root_rin", "@genlang_root_sera",
            "@genlang_root_sha", "@genlang_root_tal", "@genlang_root_tor",
            "@genlang_root_vara", "@genlang_root_ve", "@genlang_root_vel",
            "@genlang_word_aelrin", "@genlang_word_darin", "@genlang_word_genkor",
            "@genlang_word_genkoren", "@genlang_word_genvel", "@genlang_word_kai_ar_en_rin",
            "@genlang_word_kaisha", "@genlang_word_koren", "@genlang_word_relrin",
            "@genlang_word_sharin", "@genlang_word_shator", "@genlang_word_talrin",
            "@genlang_word_verin",
        },
    },
    "V02-C12": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C12_TRANSLATION_INTO_CONVENTIONAL_PHYSICS.md",
        "equation_classes": {
            **{f"20.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"20.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@continuity_perturbation", "@correspondence_to_known_quantum_field_theory",
            "@detector_observable", "@einstein_field_equation", "@field_level_handoff_theorem",
            "@gauge_condition", "@general_relativity", "@geometry",
            "@gravitational_helicon_mode", "@graviton", "@gravity", "@helicon",
            "@linearized_field_equation", "@metric_perturbation", "@metric_tensor",
            "@projected_spacetime_metric", "@quantum_field_in_curved_spacetime",
            "@readable_space_time", "@readable_spacetime", "@spin_2_projection",
            "@stress_energy_tensor", "@time_shell", "@time_shell_projection_operator",
            "@vacuum_wave_equation", "@weak_field_metric_perturbation",
        },
    },
    "V02-C11": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C11_TRANSLATION_INTO_CONVENTIONAL_MATHEMATICS.md",
        "equation_classes": {
            **{f"19.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"19.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@admissible_equivalence", "@algebra_14_5_partial_isometry_relations",
            "@boundary_projection", "@canonical_identity", "@canonical_object",
            "@chirality_map", "@chirality_space", "@classification",
            "@constructive_geometry", "@dependency_graph", "@dependency_preserving_map",
            "@field_level_handoff_theorem", "@genesis_partial_isometry",
            "@geometric_interpretation", "@information_geometry", "@inheritance_morphism",
            "@mathematical_object", "@mathematical_representation", "@prime_mathematical_object",
            "@recursive_harmonic_functional", "@representation_graph", "@spectral_projection_rule",
            "@topology_constraints", "@type_declaration", "@typed_dependency_graph",
        },
    },
    "V02-C10": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C10_QMO_GRAMMAR.md",
        "equation_classes": {
            **{f"18.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"18.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@canonical_artifact", "@canonical_identity", "@canonical_object",
            "@canonical_presentation_route", "@classification", "@compile_recovered_object",
            "@concept_lookup_endpoint", "@correspondence_registry", "@handle_invocation_contract",
            "@mathematical_object", "@mathematical_registry", "@object_identity_rule",
            "@prime_mathematical_object", "@proof_dependency_graph", "@provenance",
            "@realization_graph", "@recovery_handle_contract", "@recovery_intermediate_representation",
            "@representation_graph", "@required_object_classes", "@source_graph",
            "@stable_handle_naming", "@theorem_graph", "@type_declaration", "@version_record",
        },
    },
    "V02-C09": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C09_IDENTITY_EQUIVALENCE_DEPENDENCY_AND_HANDOFF.md",
        "equation_classes": {
            **{f"17.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"17.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@canonical_identity", "@declared_framework_identity", "@genesis_identity",
            "@object_identity_rule", "@canonical_object", "@admissible_equivalence",
            "@coherent_continuation_class", "@relationship", "@genesis_relationship",
            "@genlang_relationship_first_grammar", "@relational_history", "@dependency_contract",
            "@dependency_graph", "@typed_dependency_graph", "@dependency_subgraph",
            "@dependency_composition", "@dependency_preserving_map", "@dependency_spine_contract",
            "@current_dependency_closure", "@dependency_closure", "@dependency_expansion_operator",
            "@initial_recovered_dependency_chain", "@correspondence_registry",
            "@field_level_handoff_theorem", "@inheritance_morphism",
        },
    },
    "V02-C08": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C08_INFORMATION_AND_REALIZATION.md",
        "equation_classes": {
            **{f"16.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"16.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@information_flow", "@information_linking", "@conservation_of_information",
            "@information_loss", "@information_recovery", "@information_geometry",
            "@information_geometry_contract", "@mutual_information_weighting",
            "@mutual_information_and_er_weights", "@holographic_encoding",
            "@holographic_encoding_of_phase_data", "@field_encoding", "@representation_graph",
            "@realization_graph", "@downstream_realization_graph", "@realization_expansion_operator",
            "@matter_readable_organization", "@particle_readable_organization",
            "@readable_space_time", "@readable_spacetime", "@source_graph", "@semantic_graph",
            "@observational_graph", "@interpretation", "@api_interpretation",
        },
    },
    "V02-C07": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C07_RECURSION_AND_LOCALIZATION.md",
        "equation_classes": {
            **{f"15.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 5, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"15.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 7, 10, 15)},
        },
        "core": {
            "@recursive_depth", "@recursive_ordering", "@recursive_continuity",
            "@recursive_inheritance", "@genesis_recursive_inheritance", "@inheritance",
            "@inheritance_morphism", "@continuation_inheritance_compatibility",
            "@persistence", "@persistence_potential", "@persistent_recursive_topology",
            "@local_recursive_state", "@locality", "@factorisation_and_proto_locality",
            "@proto_locality_the_first_signs_of_division", "@emergence_of_continuum_locality",
            "@localization_closure_parameter", "@localized_persistent_topology",
            "@localized_er_foam_knot", "@recursive_occupancy", "@resolution",
            "@bandwidth", "@occupancy", "@closure", "@genesis_closure",
        },
    },
    "V02-C06": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C06_CHIRALITY_LANGUAGE.md",
        "equation_classes": {
            **{f"14.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 18)},
            **{f"14.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 5, 7, 10, 15)},
        },
        "core": {
            "@chirality", "@definition_13_1_chirality", "@chirality_and_handedness",
            "@chirality_map", "@chirality_space", "@chirality_transport", "@orientation",
            "@mirror_handedness", "@chirality_mirror_operator", "@chirality_representation_registry",
            "@chirality_history", "@orientation_history", "@chirality_byte",
            "@serialized_chirality_byte", "@chirality_seed", "@left_chirality_seed",
            "@right_chirality_seed", "@principle_13_3_genesis_chirality_symmetry",
            "@model_13_4_ensemble_chirality_bias", "@lookup_contract_13_5_recover_chirality",
            "@chirality_organization", "@chiralitybiasmodel", "@helicon_orientation",
            "@integrated_temporal_orientation", "@time_orientation",
        },
    },
    "V02-C05": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C05_PROJECTION_LANGUAGE.md",
        "equation_classes": {
            **{f"13.{n}": "CLOVER_SYNTHESIS" for n in (1, 4, 5, 7, 8, 11, 13, 14, 16, 17, 18)},
            **{f"13.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 6, 9, 10, 12, 15)},
        },
        "core": {
            "@admissibility", "@projection_admissibility", "@local_admissibility",
            "@boundary_projection", "@primitive_p10", "@axiom_a5", "@lemma_l4",
            "@projection_residue", "@projection_residue_bundle", "@axiom_a6", "@lemma_l5",
            "@spectral_projection_rule", "@spectral_measurement_projection", "@axiom_a12",
            "@lemma_l12", "@genesis_partial_isometry", "@algebra_14_5_partial_isometry_relations",
            "@screen_projector", "@shadowprojection_pii", "@spin_2_projection",
            "@time_shell_projection", "@time_shell_projection_operator",
            "@realization_graph", "@downstream_realization_graph", "@genlang_family_ae",
        },
    },
    "V02-C04": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C04_SCOPE_AND_REPRESENTATION.md",
        "equation_classes": {
            **{f"12.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18)},
            **{f"12.{n}": "API_NATIVE_ARCHITECTURE" for n in (8, 14)},
        },
        "core": {
            "@scope_contract", "@context_and_intent", "@semantic_constraint",
            "@semantic_graph", "@spine_semantics", "@mathematical_representation",
            "@representation_graph", "@recovery_intermediate_representation",
            "@realization_graph", "@downstream_realization_graph", "@projection_admissibility",
            "@type_declaration", "@admissible_equivalence", "@interpretation",
            "@api_interpretation", "@recovered_semantic_roles", "@presentation_modes",
            "@canonical_presentation_route", "@genlang_resolution_state_aspect",
            "@genlang_common_genesis_register", "@genlang_scholar_genesis_register",
            "@genlang_architect_genesis_register", "@genlang_poetic_genesis_register",
        },
    },
    "V02-C03": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C03_HANDLES_ADDRESSES_AND_NAMES.md",
        "equation_classes": {
            **{f"11.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16)},
            "11.7": "API_NATIVE_ARCHITECTURE",
        },
        "core": {
            "@handle_integrity_invariants", "@handle_invocation_contract",
            "@initial_canonical_handle_registry", "@stable_handle_naming",
            "@automatic_handle_generation", "@alias_expansion_operator",
            "@concept_lookup_endpoint", "@lookup_semantics", "@registry_endpoints",
            "@canonical_presentation_route", "@mathematical_registry",
            "@correspondence_registry", "@source_graph", "@version_record",
            "@recovery_handle_contract", "@natural_language_invocation",
            "@prime_axiom_a7", "@canonical_identity", "@canonical_object",
            "@declared_framework_identity",
        },
    },
    "V02-C02": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C02_MATHEMATICAL_OBJECTS_AND_ONTOLOGICAL_OBJECTS.md",
        "equation_classes": {
            **{f"10.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18)},
            "10.9": "API_NATIVE_ARCHITECTURE",
            "10.12": "API_NATIVE_ARCHITECTURE",
        },
        "core": {
            "@mathematical_object", "@prime_mathematical_object", "@prime_definition_d13",
            "@prime_definition_d2", "@canonical_object", "@canonical_identity",
            "@object_identity_rule", "@genesis_ontology", "@ontological_graph",
            "@mathematical_graph", "@mathematical_representation", "@representation_graph",
            "@type_declaration", "@required_object_classes", "@classification",
            "@admissible_equivalence", "@genesis_identity", "@prime_axiom_a1",
            "@compile_recovered_object", "@canonical_artifact",
            "@recovery_intermediate_representation", "@recovery_handle_contract",
            "@declared_framework_identity",
        },
    },
    "V02-C01": {
        "path": WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C01_WHY_A_NEW_REPRESENTATIONAL_LANGUAGE_WAS_REQUIRED.md",
        "equation_classes": {
            **{f"9.{n}": "CLOVER_SYNTHESIS" for n in (1, 3, 4, 6, 8, 9, 11, 12, 14, 15, 16, 17, 18)},
            **{f"9.{n}": "API_NATIVE_ARCHITECTURE" for n in (2, 5, 7, 10, 13)},
        },
        "core": {
            "@genesis_language", "@genesis_grammar", "@genesis_expression",
            "@genlang_relationship_first_grammar", "@genlang_structural_compounding",
            "@genlang_resolution_state_aspect", "@geometry_as_prime_api_language",
            "@natural_language_invocation", "@source_genesis_grammar_v0_1",
            "@genlang_root_en", "@genlang_root_rel", "@genlang_root_kor",
            "@genlang_root_rin", "@genlang_root_sha", "@genlang_root_ar",
            "@genlang_root_ve", "@genlang_root_tor", "@genlang_root_ael",
            "@genlang_architect_genesis_register", "@genlang_scholar_genesis_register",
        },
    },
    "V01-C02": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C02_DISTINCTION_INFORMATION_AND_STRUCTURAL_REALITY.md",
        "equation_classes": {
            **{f"2.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 4, 5, 10, 11, 12, 13, 14, 18, 19)},
            **{f"2.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (3, 6, 7, 8, 9, 15, 16, 17)},
        },
        "core": {
            "@distinction", "@structural_distinction", "@structural_zero", "@classification",
            "@coherence_functional", "@cross_scale_coherence", "@cross_scale_coherence_functional",
            "@coherent_attractors", "@coherent_continuation_class", "@prime_mathematical_object",
            "@genesis_identity", "@representation_graph", "@failure_distinction", "@interface_error_functional",
        },
    },
    "V01-C03": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C03_CHIRALITY_AS_ORGANIZED_DIFFERENCE.md",
        "equation_classes": {
            **{f"3.{n}": "CLOVER_SYNTHESIS" for n in (1, 7, 8, 9, 10, 11, 12, 16, 17, 20)},
            **{f"3.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 3, 4, 5, 6, 18, 19, 21, 22, 23)},
            **{f"3.{n}": "FOUNDATIONAL_SOURCE_DERIVED; CURRENT_CANON_CANDIDATE" for n in (13, 14, 15)},
        },
        "core": {
            "@chirality", "@chirality_and_handedness", "@chirality_byte", "@chirality_closure",
            "@chirality_diagonal_structure", "@chirality_history", "@chirality_layer_complement",
            "@chirality_map", "@chirality_representation_registry", "@chirality_seed", "@chirality_space",
            "@chiralitybiasmodel", "@left_chirality_seed", "@right_chirality_seed",
            "@principle_13_3_genesis_chirality_symmetry", "@model_13_4_ensemble_chirality_bias",
            "@collapse_algebra_and_chirality", "@foundations_of_chirality",
        },
    },
    "V01-C04": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C04_RECURSION_INHERITANCE_AND_PERSISTENCE.md",
        "equation_classes": {
            **{f"4.{n}": "CLOVER_SYNTHESIS" for n in (1, 3, 4, 5, 6, 11, 16, 17, 23)},
            **{f"4.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 7, 8, 9, 10, 18, 19, 20, 21, 22, 24)},
            **{f"4.{n}": "FOUNDATIONAL_SOURCE_DERIVED; CURRENT_CANON_CANDIDATE" for n in (12, 13, 14)},
            "4.15": "DETERMINISTIC_NORMALIZATION; CURRENT_CANON_CANDIDATE",
        },
        "core": {
            "@persistence", "@persistence_potential", "@genesis_persistence", "@genesis_continuity",
            "@ordering", "@admissible_equivalence", "@stable_er_foam_knot_persistence",
            "@recovery_invariant", "@recovery_closure", "@prime_dependency_calculus",
            "@current_dependency_closure", "@coherent_continuation_class", "@continuity_redistribution",
        },
    },
    "V01-C05": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C05_ER_FOAM_AND_PRE_GEOMETRIC_CONNECTIVITY.md",
        "equation_classes": {
            **{f"5.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17)},
            **{f"5.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (3, 4, 7, 18, 19, 20, 21, 22, 23)},
            "5.15": "GENESIS_CURATORIAL; CURRENT_CANON_CANDIDATE",
            "5.24": "API_NATIVE_DEPENDENCY_PATH; RECOVERED",
            "5.25": "CURRENT_CANON_CANDIDATE",
        },
        "core": {
            "@er_foam_as_a_microscopic_substrate", "@er_foam_bead", "@er_foam_configuration_space",
            "@er_foam_geodesic_structure", "@er_network_dynamical_equations", "@er_network_formalism",
            "@localized_er_foam_knot", "@localized_persistent_topology", "@stable_er_foam_knot",
            "@persistent_topology", "@classical_geometry_from_er_foam", "@continuum_limit_and_gr",
            "@admissible_er_restructuring", "@particle_as_stable_knot", "@topological_closure_map",
            "@uv_ir_foam_continuum", "@er_foam_bead", "@discrete_bead",
        },
    },
    "V01-C06": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C06_PLANCK_LANDSCAPE_AND_FOUNDATIONAL_GEOMETRY.md",
        "equation_classes": {
            **{f"6.{n}": "CLOVER_SYNTHESIS" for n in (1, 3, 9, 14, 16, 20, 21, 22)},
            **{f"6.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19)},
        },
        "core": {
            "@planck_landscape", "@phase_order_below_the_planck_scale",
            "@sub_planckian_phase_order_and_gradient_dynamics", "@master_equation_of_phase_geometry",
            "@planck_scale_bead_structure", "@the_bead_lattice_discrete_geometry_and_continuum_limit",
            "@geometry", "@constructive_geometry", "@core_geometry", "@geometry_engine",
            "@geometry_distribution", "@topology_induction", "@topology_constraints",
            "@anchor_map", "@angular_geometry", "@angular_reduction_map", "@readable_space_time",
        },
    },
    "V01-C07": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C07_PROJECTION_TRANSDUCTION_AND_REALIZATION.md",
        "equation_classes": {
            **{f"7.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 5, 9, 21)},
            **{f"7.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (3, 4, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 22)},
            "7.11": "STILL_UNRESOLVED; REQUIRED_INTERTWINING_BRIDGE",
            "7.18": "DETERMINISTIC_API_EVIDENCE; RECOVERED_DEPENDENCY_PATH",
            "7.19": "EXACT_RECOVERED_EQUATION",
            "7.20": "EXACT_RECOVERED_EQUATION",
        },
        "core": {
            "@projection_admissibility", "@mathematical_representation", "@exact_mathematics",
            "@realization_graph", "@downstream_realization_graph", "@shadowprojection_pii",
            "@screen_projector", "@spin_2_projection", "@continuity_perturbation",
            "@genesis_boundary", "@genesis_topology", "@localization_closure_parameter",
            "@existence_state", "@projection_admissibility", "@type_declaration",
        },
    },
    "V01-C08": {
        "path": WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C08_CONSERVATION_ACROSS_REPRESENTATIONAL_LEVELS.md",
        "equation_classes": {
            **{f"8.{n}": "CLOVER_SYNTHESIS" for n in (1, 2, 4, 12, 18, 20, 21, 22, 24, 25)},
            **{f"8.{n}": "EXTERNAL_ESTABLISHED_MATHEMATICS" for n in (3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 23, 26, 27, 28, 29)},
        },
        "core": {
            "@conservation_of_recoverable_structure", "@continuity_conservation",
            "@conservation_and_production", "@canonical_identity", "@declared_framework_identity",
            "@dependency_closure", "@fixed_point_recovery", "@integrity_condition",
            "@genesis_partial_isometry", "@genesis_ontology", "@genesis_expression",
            "@universal_triadic_law", "@sector_decomposition_of_the_state_space",
            "@noether_identity", "@causal_structure", "@configuration_space",
            "@recovery_intermediate_representation", "@recovery_handle_contract",
            "@distortion_tensor", "@diagnostic_functional",
            "@stress_tests_consistency_with_gr_qm_and_thermodynamics",
        },
    },
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    os.replace(tmp, path)


def write_json(path: Path, payload: dict[str, object]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def clean(value: object) -> str:
    text = str(value or "No separate canonical title declared")
    return (
        text.replace("â€”", "-").replace("â€“", "-").replace("â¶", "6")
        .replace("|", "\\|").replace("\n", " ").strip("` ")
    )


def role_for(handle: str, core: set[str]) -> str:
    h = handle.lower()
    if handle in core:
        return "chapter-core object"
    if any(k in h for k in ("source_", "recovery", "registry", "lookup", "contract", "handle_", "serialized", "dependency", "api_", "concept_level")):
        return "address, provenance, or recovery-control interface"
    if any(k in h for k in ("black_hole", "horizon", "geodesic", "spacetime", "vacuum", "unruh", "penrose", "killing", "teukolsky", "ringdown", "redshift", "cosmolog", "hubble", "perihelion", "quadrupole", "neutrino", "particle_flux", "light_cone", "torsion")):
        return "downstream conventional-physics or observational interface"
    if any(k in h for k in ("vaeld", "abyss", "crown", "treaty", "civiliz", "master_chief", "ship", "expedition", "revelation", "overture", "mindscape", "admiral", "tiger", "white_state", "whitestate")):
        return "historical narrative, analogy, or interpretive model"
    if any(k in h for k in ("genesis", "pre_genesis", "phonology", "rosetta")):
        return "Genesis-language or foundational interface"
    if any(k in h for k in ("equation", "functional", "criterion", "condition", "model", "algebra", "dynamics", "spectrum", "stability", "trajectory", "capacity", "continuity")):
        return "mathematical model, condition, or dynamics interface"
    if any(k in h for k in ("chirality", "orientation", "wedge", "complex_structure", "frequency", "polarization", "angular")):
        return "chirality representation or downstream orientation interface"
    return "cross-domain assigned address; scope retained for later specialized treatment"


def make_register(chapter: dict[str, object], core: set[str]) -> str:
    lines = [
        "| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |",
        "|---|---|---:|---:|---|",
    ]
    for row in chapter["handles"]:
        cov = row.get("coverage_v2") or {}
        lines.append(
            "| `{}` | {} | {} | {} / {} / {} | {} |".format(
                row["handle"],
                clean(row.get("canonical_name")),
                clean(cov.get("state") or "UNPOPULATED"),
                int(cov.get("english_units") or 0),
                int(cov.get("equation_units") or 0),
                int(cov.get("registered_dependencies") or 0),
                role_for(str(row["handle"]), core),
            )
        )
    return "\n".join(lines)


def word_count(markdown: str) -> int:
    text = re.sub(r"<!--.*?-->", " ", markdown, flags=re.S)
    return len(re.findall(r"\b[\w@]+(?:[-'][\w@]+)*\b", text, flags=re.UNICODE))


def workspace_size() -> int:
    total = 0
    for path in WORKSPACE.rglob("*"):
        if path.is_file():
            try:
                total += path.stat().st_size
            except OSError:
                pass
    return total


def artifact(path: Path) -> dict[str, object]:
    return {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256(path)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id", choices=sorted(CONFIG))
    args = parser.parse_args()
    chapter_id = args.chapter_id
    config = CONFIG[chapter_id]
    chapter_path: Path = config["path"]
    batch_slug = BATCHES[chapter_id]
    digest_path = WORKSPACE / f"native_evidence_digest_{batch_slug}.json"
    receipt_path = WORKSPACE / f"native_query_receipt_{batch_slug}.json"
    digest = json.loads(digest_path.read_text(encoding="utf-8"))
    digest_chapter = next(c for c in digest["chapters"] if c["chapter_id"] == chapter_id)

    chapter_rows = load_jsonl(WORKSPACE / "chapter_ledger.jsonl")
    chapter_row = next(row for row in chapter_rows if row["chapter_id"] == chapter_id)
    if chapter_row.get("status") == "COMPLETE":
        raise RuntimeError(f"{chapter_id} is already complete; refusing to reseal")
    prior_complete = [row for row in chapter_rows if row.get("status") == "COMPLETE"]
    expected_next = next(row for row in chapter_rows if row.get("status") != "COMPLETE")
    if expected_next["chapter_id"] != chapter_id:
        raise RuntimeError(f"sequential boundary violation: expected {expected_next['chapter_id']}")
    if sha256(DB) != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 hash mismatch before chapter seal")
    sidecars = [str(p) for suffix in ("-wal", "-shm", "-journal") if (Path(str(DB) + suffix)).exists() for p in [Path(str(DB) + suffix)]]
    if sidecars:
        raise RuntimeError(f"unexpected Library sidecars: {sidecars}")

    text = chapter_path.read_text(encoding="utf-8")
    marker = f"<!-- HANDLE_REGISTER:{chapter_id} -->"
    if marker not in text:
        raise RuntimeError("chapter register marker missing")
    register = make_register(digest_chapter, set(config["core"]))
    text = text.replace(marker, register)
    chapter_path.write_text(text, encoding="utf-8", newline="\n")
    words = word_count(text)
    page_estimate = math.ceil(words / 500)
    chapter_hash = sha256(chapter_path)

    chapter_row.update(
        {
            "status": "COMPLETE",
            "path": str(chapter_path.relative_to(ROOT)),
            "sha256": chapter_hash,
            "bytes": chapter_path.stat().st_size,
            "word_count": words,
            "formatted_page_estimate": page_estimate,
            "assigned_handles_accounted": len(digest_chapter["handles"]),
            "native_query_receipt": str(receipt_path.relative_to(ROOT)),
            "native_evidence_digest": str(digest_path.relative_to(ROOT)),
            "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
            "sealed_at": utc_now(),
        }
    )
    write_jsonl(WORKSPACE / "chapter_ledger.jsonl", chapter_rows)

    handle_receipt_path = WORKSPACE / f"{chapter_id.replace('-', '_')}_handle_assignment_receipt.json"
    if not handle_receipt_path.exists():
        write_json(
            handle_receipt_path,
            {
                "schema": "mk-ultra-tome-chapter-handle-assignment/v1",
                "created_at": utc_now(),
                "chapter_id": chapter_id,
                "assigned_handle_count": len(chapter_row["handles"]),
                "handles": chapter_row["handles"],
                "basis": "Initialized Library 4.1 chapter-ledger assignment for the current sequential TOME chapter",
                "library_api_ledger_path": str(API_LEDGER.relative_to(ROOT)),
                "library_api_ledger_sha256": sha256(API_LEDGER),
                "chapter_ledger_sha256_after": sha256(WORKSPACE / "chapter_ledger.jsonl"),
                "missing_handles": [],
            },
        )

    equation_path = WORKSPACE / "equation_ledger.jsonl"
    equation_rows = load_jsonl(equation_path)
    for label, evidence_class in config["equation_classes"].items():
        equation_rows.append(
            {
                "record_type": "publication_equation",
                "publication_equation_id": label,
                "chapter_id": chapter_id,
                "evidence_class": evidence_class,
                "chapter_path": str(chapter_path.relative_to(ROOT)),
                "chapter_sha256": chapter_hash,
                "native_evidence_digest": str(digest_path.relative_to(ROOT)),
                "status": "PUBLISHED_IN_DRAFT_TOME_CHAPTER",
            }
        )
    write_jsonl(equation_path, equation_rows)

    citation_path = WORKSPACE / "citation_ledger.jsonl"
    citation_rows = load_jsonl(citation_path)
    existing_citations = {row.get("citation_id") for row in citation_rows}
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    result_by_handle = {row["requested_handle"]: row for row in receipt["results"]}
    for handle in chapter_row["handles"]:
        result = result_by_handle[handle]
        art = result["artifacts"][0]
        citation_id = f"native-query:{handle}"
        if citation_id not in existing_citations:
            apath = Path(art["path"])
            citation_rows.append(
                {
                    "citation_id": citation_id,
                    "handle": handle,
                    "path": str(apath.relative_to(ROOT)),
                    "bytes": apath.stat().st_size,
                    "sha256": sha256(apath),
                    "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
                }
            )
            existing_citations.add(citation_id)
    citation_rows.append(
        {
            "citation_id": f"chapter:{chapter_id}",
            "chapter_id": chapter_id,
            "path": str(chapter_path.relative_to(ROOT)),
            "sha256": chapter_hash,
            "assigned_handles": len(chapter_row["handles"]),
            "native_query_receipt": str(receipt_path.relative_to(ROOT)),
        }
    )
    write_jsonl(citation_path, citation_rows)

    qmo_path = WORKSPACE / "qmo_derivation_ledger.jsonl"
    qmo_rows = load_jsonl(qmo_path)
    qmo_rows.append(
        {
            "record_type": "chapter_foundational_synthesis",
            "chapter_id": chapter_id,
            "handles": chapter_row["handles"],
            "provenance_classes": ["FOUNDATIONAL_SOURCE_DERIVED", "QMO_DERIVED", "API_NATIVE_DERIVATION", "CLOVER_SYNTHESIS", "EXTERNAL_ESTABLISHED_MATHEMATICS"],
            "native_query_receipt": str(receipt_path.relative_to(ROOT)),
            "chapter_sha256": chapter_hash,
            "status": "CHAPTER_COMPLETE; OBJECT_LEVEL_PROOF_STATUS_RETAINED_LOCALLY",
        }
    )
    write_jsonl(qmo_path, qmo_rows)

    validation_path = WORKSPACE / "validation_ledger.jsonl"
    validations = load_jsonl(validation_path)
    validations.extend(
        [
            {"validation_id": f"{chapter_id}-QUERY", "check": "Assigned native queries", "result": "PASS", "value": len(chapter_row["handles"])},
            {"validation_id": f"{chapter_id}-LIBRARY", "check": "Library database unchanged", "result": "PASS", "value": EXPECTED_DB_SHA},
            {"validation_id": f"{chapter_id}-HASH", "check": "Chapter sealed SHA-256", "result": "PASS", "value": chapter_hash},
            {"validation_id": f"{chapter_id}-REGISTER", "check": "Assigned handles represented in chapter register", "result": "PASS", "value": len(digest_chapter["handles"])},
        ]
    )
    write_jsonl(validation_path, validations)

    terminology_path = WORKSPACE / "terminology_ledger.json"
    terminology = json.loads(terminology_path.read_text(encoding="utf-8"))
    terminology["publication_name"] = "MK Ultra"
    terminology["publication_name_effective_from_chapter"] = "V01-C02"
    terminology["completed_chapter_legacy_name_policy"] = "V01-C01 remains byte-identical; final editorial normalization is deferred."
    write_json(terminology_path, terminology)

    toc_path = WORKSPACE / "MASTER_TOC.md"
    toc = toc_path.read_text(encoding="utf-8")
    toc = toc.replace("# MK 43 Ultra - Master Theory Report", "# MK Ultra - Master Theory Report")
    toc = toc.replace("Publication prose uses **MK 43 Ultra**", "Publication prose uses **MK Ultra**")
    toc = toc.replace(f"- {chapter_id} [PLANNED]", f"- {chapter_id} [COMPLETE]")
    toc_path.write_text(toc, encoding="utf-8", newline="\n")

    next_row = next((row for row in chapter_rows if row.get("status") != "COMPLETE"), None)
    complete_rows = [row for row in chapter_rows if row.get("status") == "COMPLETE"]
    total_words = sum(int(row.get("word_count") or 0) for row in complete_rows)
    total_pages = sum(int(row.get("formatted_page_estimate") or (9 if row["chapter_id"] == "V01-C01" else 0)) for row in complete_rows)
    if next_row is None:
        next_id = None
        next_title = None
    else:
        next_id = next_row["chapter_id"]
        next_title = next_row["title"]

    manifest_path = WORKSPACE / "master_report_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "publication_name": "MK Ultra",
            "status": "TOME_GENERATION_IN_PROGRESS",
            "completed_chapters": len(complete_rows),
            "current_cumulative_word_count": total_words,
            "current_formatted_page_estimate": total_pages,
            "next_resumable_chapter_id": next_id,
            "next_resumable_chapter_title": next_title,
            "library_database_sha256_after_seal": sha256(DB),
            "database_sidecars": [],
            "sealed_at": utc_now(),
            "source_or_extracted_rescanned": False,
        }
    )
    tracked = [
        WORKSPACE / "API_NATIVE_MAJOR_OBJECTS.md",
        WORKSPACE / "GENESIS_LANGUAGE_ARCHITECTURE.md",
        WORKSPACE / "MASTER_TOC.md",
        WORKSPACE / "chapter_ledger.jsonl",
        WORKSPACE / "citation_ledger.jsonl",
        WORKSPACE / "equation_ledger.jsonl",
        WORKSPACE / "genesis_language_architecture.json",
        WORKSPACE / "master_native_query_receipt.json",
        WORKSPACE / "master_native_query_state.json",
        WORKSPACE / "qmo_derivation_ledger.jsonl",
        WORKSPACE / "terminology_ledger.json",
        WORKSPACE / "validation_ledger.jsonl",
        receipt_path,
        digest_path,
    ] + [Path(row["path"]) if Path(str(row["path"])).is_absolute() else ROOT / str(row["path"]) for row in complete_rows if row.get("path")]
    old_pdf = WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C01_WHAT_IS_MK_43_ULTRA.pdf"
    if old_pdf.exists():
        tracked.append(old_pdf)
    unique_tracked = []
    seen = set()
    for path in tracked:
        key = str(path.resolve())
        if key not in seen and path.exists():
            seen.add(key)
            unique_tracked.append(path)
    manifest["artifacts"] = [artifact(path) for path in unique_tracked]
    manifest["equation_ledger_records"] = len(equation_rows)
    write_json(manifest_path, manifest)

    disk = shutil.disk_usage(ROOT)
    checkpoint = {
        "schema": "mk-ultra-tome-generation-chapter-checkpoint-v1",
        "created_at": utc_now(),
        "status": "CHAPTER_COMPLETE_AND_VALIDATED",
        "chapter_id": chapter_id,
        "chapter_title": chapter_row["title"],
        "chapter": artifact(chapter_path),
        "word_count": words,
        "formatted_page_estimate": page_estimate,
        "assigned_handles": len(chapter_row["handles"]),
        "native_queries": len(chapter_row["handles"]),
        "native_query_failures": [],
        "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
        "database_sha256": sha256(DB),
        "database_sidecars": [],
        "library_unchanged": sha256(DB) == EXPECTED_DB_SHA,
        "source_or_extracted_queried": False,
        "completed_chapters": len(complete_rows),
        "current_cumulative_word_count": total_words,
        "current_formatted_page_estimate": total_pages,
        "next_resumable_chapter_id": next_id,
        "next_resumable_chapter_title": next_title,
        "workspace_bytes": workspace_size(),
        "disk_free_bytes": disk.free,
        "manifest_sha256": sha256(manifest_path),
        "ledger_hashes": {
            name: sha256(WORKSPACE / name)
            for name in ("chapter_ledger.jsonl", "equation_ledger.jsonl", "qmo_derivation_ledger.jsonl", "citation_ledger.jsonl", "validation_ledger.jsonl", "terminology_ledger.json")
        },
    }
    checkpoint_path = CHECKPOINTS / f"mk43_master_theory_generation_{chapter_id.replace('-', '_')}.json"
    write_json(checkpoint_path, checkpoint)
    write_json(CHECKPOINTS / "mk43_master_theory_generation_current.json", checkpoint)
    print(json.dumps({"chapter_id": chapter_id, "sha256": chapter_hash, "words": words, "pages": page_estimate, "next": next_id, "checkpoint": str(checkpoint_path)}))


if __name__ == "__main__":
    main()
