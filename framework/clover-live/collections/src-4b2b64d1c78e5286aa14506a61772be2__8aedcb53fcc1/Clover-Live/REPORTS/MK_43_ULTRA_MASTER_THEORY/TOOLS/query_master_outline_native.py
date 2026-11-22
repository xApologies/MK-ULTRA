from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
OUT = WORKSPACE / "NATIVE_QUERY"
STATE = WORKSPACE / "master_native_query_state.json"
RECEIPT = WORKSPACE / "master_native_query_receipt.json"
LIVE = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1"
DB = LIVE / "state/library.sqlite3"
LEDGER = LIVE / "full_api_handle_ledger_08m.jsonl"
ADAPTER = LIVE / "runtime_mount/Library_4_1_Live_State_Adapter.zip"
RUNTIME_PACKAGE = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08l/runtime_package"
BRANE = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08k/modules/BRANE_3.1.zip"
API = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08k/modules/API_2.0.zip"
AI = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08k/modules/AI_2.1.zip"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"


CORE_HANDLES = [
    # Foundations and information architecture.
    "@distinction",
    "@structural_distinction",
    "@information_geometry",
    "@information_flow",
    "@conservation_of_information",
    "@conservation_of_recoverable_structure",
    "@chirality",
    "@chirality_space",
    "@chirality_map",
    "@chirality_transport",
    "@orientation",
    "@orientation_history",
    "@recursive_depth",
    "@recursive_ordering",
    "@recursive_continuity",
    "@recursive_inheritance",
    "@recursive_stabilization",
    "@persistent_recursive_topology",
    "@persistence",
    "@persistence_potential",
    "@genesis_field",
    "@genesis_inheritance",
    "@global_inheritance",
    "@inheritance",
    "@inheritance_morphism",
    "@inheritance_theory",
    "@er_foam",
    "@er_foam_configuration_space",
    "@classical_geometry_from_er_foam",
    "@stable_er_foam_knot",
    "@localized_er_foam_knot",
    "@planck_landscape",
    "@locality",
    "@observer_relative_locality",
    "@time_orientation",
    "@projection_admissibility",
    "@realization_graph",
    "@mathematical_representation",
    # Primary QMOs and interfaces.
    "@helicon",
    "@helicon_state_space",
    "@helicon_structural_tuple",
    "@helicon_spectral_operator",
    "@helicon_spectral_coupling",
    "@helicon_resonance",
    "@gravitational_helicon_mode",
    "@time_shell",
    "@time_shell_projection",
    "@time_shell_projection_operator",
    "@graviton",
    "@continuity_perturbation",
    "@readable_graviton_projection",
    "@weak_field_metric_perturbation",
    "@projected_spacetime_metric",
    "@readable_space_time",
    # API-native and QMO-derived mathematics.
    "@native_unit_of_energy",
    "@unit_of_energy",
    "@general_energy",
    "@universal_coupling",
    "@native_causal_order",
    "@native_constraint_closure",
    "@native_graviton_dispersion",
    "@native_graviton_quantization",
    "@native_interaction_factorization",
    "@native_probability_preservation",
    "@continuity_conservation",
    "@local_energy_momentum_conservation",
    "@energy_composition",
    # Quantum and field realization.
    "@field_level_handoff_theorem",
    "@klein_gordon_field",
    "@quantum_field_in_curved_spacetime",
    "@field_operator",
    "@tensor_field",
    "@total_action",
    "@gauge_consistency",
    "@matter_action",
    "@matter_coupling",
    "@matter_readable_organization",
    # Gravity, strong field, cosmology, information transfer.
    "@gravity",
    "@einstein_field_equation",
    "@metric_perturbation",
    "@riemann_curvature",
    "@gravitational_radiation",
    "@black_hole",
    "@strong_field_gravity",
    "@black_hole_cosmology",
    "@cosmology",
    "@bounce_criterion",
    "@dark_matter_geometry",
    "@holographic_transfer_law",
    "@holographic_encoding",
    "@consciousness",
    # Validation and predictions.
    "@LIGO_observation",
    "@prediction_registry",
    "@prediction_freeze_protocol",
    "@observational_graph",
    "@observational_predictions",
    "@testable_predictions",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_state(payload: dict[str, object]) -> None:
    STATE.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ledger_rows = [
        json.loads(line)
        for line in LEDGER.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    all_handles = [row["short_handle"] for row in ledger_rows]
    handle_set = set(all_handles)
    if len(all_handles) != 2384 or len(handle_set) != 2384:
        raise RuntimeError("authoritative API address ledger is not the expected 2,384-handle set")

    genesis_handles = []
    for row in ledger_rows:
        searchable = " ".join(
            [
                str(row.get("short_handle", "")),
                str(row.get("canonical_name", "")),
                str(row.get("canonical_api_uri", "")),
            ]
        ).lower()
        if (
            "genlang" in searchable
            or row["short_handle"] in {
                "@genesis_language",
                "@genesis_grammar",
                "@genesis_expression",
                "@source_genesis_grammar_v0_1",
                "@geometry_as_prime_api_language",
                "@natural_language_invocation",
            }
        ):
            genesis_handles.append(row["short_handle"])

    qmo_handles = [
        row["short_handle"]
        for row in ledger_rows
        if int(row.get("compiled_qmo_records") or 0) > 0
    ]
    requested = sorted(
        set(genesis_handles)
        | set(qmo_handles)
        | {handle for handle in CORE_HANDLES if handle in handle_set}
    )
    missing_requested = sorted(set(CORE_HANDLES) - handle_set)

    before = sha256(DB)
    if before != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 hash mismatch before native master query")

    prior_results: dict[str, dict[str, object]] = {}
    if STATE.exists():
        prior = json.loads(STATE.read_text(encoding="utf-8"))
        if prior.get("database_sha256_before") != before:
            raise RuntimeError("resumable query state belongs to a different Library state")
        prior_results = {
            row["requested_handle"]: row
            for row in prior.get("results", [])
            if row.get("status") == "complete"
            and all(Path(a["path"]).exists() for a in row.get("artifacts", []))
        }

    sys.path.insert(0, str(RUNTIME_PACKAGE))
    from mk43_runtime import MK43Runtime

    checksums = {"ai": sha256(AI), "api": sha256(API), "library": sha256(ADAPTER)}
    results: list[dict[str, object]] = []
    runtime = None
    try:
        runtime = MK43Runtime(
            BRANE,
            modules={"ai": AI, "api": API, "library": ADAPTER},
            checksums=checksums,
            output_dir=OUT,
            development_mode=False,
        )
        for ordinal, handle in enumerate(requested):
            if handle in prior_results:
                result = dict(prior_results[handle])
                result["resumed_without_requery"] = True
                results.append(result)
                continue

            started = time.perf_counter()
            before_files = set(OUT.glob("*.md"))
            try:
                response = runtime.submit(
                    {
                        "operation": "generate_report",
                        "subject": handle,
                        "request_id": f"mk43-master-outline-{ordinal:03d}",
                        "depth": "structural",
                        "direction": "both",
                        "coverage_mode": "annotated",
                        "title": f"MK 43 ULTRA MASTER QUERY - {handle}",
                        "options": {"defer_handles": all_handles},
                    }
                )
            except Exception as exc:
                response = {
                    "status": "failed",
                    "errors": [{"type": type(exc).__name__, "message": str(exc)}],
                }
            new_files = sorted(set(OUT.glob("*.md")) - before_files)
            result = {
                "ordinal": ordinal,
                "requested_handle": handle,
                "status": response.get("status"),
                "response": response,
                "artifacts": [
                    {
                        "path": str(path),
                        "bytes": path.stat().st_size,
                        "sha256": sha256(path),
                    }
                    for path in new_files
                ],
                "elapsed_seconds": round(time.perf_counter() - started, 6),
                "resumed_without_requery": False,
            }
            results.append(result)
            write_state(
                {
                    "schema": "mk43-master-native-query-state-v1",
                    "updated_at": utc_now(),
                    "database_sha256_before": before,
                    "requested_handles": requested,
                    "missing_requested_handles": missing_requested,
                    "genesis_language_handles": genesis_handles,
                    "qmo_record_handles": qmo_handles,
                    "results": results,
                    "next_handle": requested[ordinal + 1] if ordinal + 1 < len(requested) else None,
                }
            )

        runtime_info = runtime.info()
        runtime_validation = runtime.validate()
    finally:
        if runtime is not None:
            runtime.close()
        if str(RUNTIME_PACKAGE) in sys.path:
            sys.path.remove(str(RUNTIME_PACKAGE))

    after = sha256(DB)
    receipt = {
        "schema": "mk43-master-native-query-receipt-v1",
        "created_at": utc_now(),
        "database_sha256_before": before,
        "database_sha256_after": after,
        "database_unchanged": before == after,
        "api_address_count": len(all_handles),
        "requested_handles": requested,
        "missing_requested_handles": missing_requested,
        "genesis_language_handles": sorted(genesis_handles),
        "qmo_record_handles": sorted(qmo_handles),
        "successful_queries": [r["requested_handle"] for r in results if r["status"] == "complete"],
        "failed_queries": [r["requested_handle"] for r in results if r["status"] != "complete"],
        "results": results,
        "runtime_info": runtime_info,
        "runtime_validation": runtime_validation,
    }
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_state({**receipt, "next_handle": None, "complete": True})
    if before != after:
        raise RuntimeError("Library 4.1 changed during native master queries")
    if receipt["failed_queries"]:
        raise RuntimeError(f"native master queries failed: {receipt['failed_queries']}")
    print(
        json.dumps(
            {
                "api_addresses": len(all_handles),
                "queried": len(requested),
                "genesis_language_handles": len(genesis_handles),
                "qmo_record_handles": qmo_handles,
                "database_unchanged": before == after,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
