from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
LEDGER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
CHAPTER_LEDGER = WORKSPACE / "chapter_ledger.jsonl"
ADAPTER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/runtime_mount/Library_4_1_Live_State_Adapter.zip"
RUNTIME_PACKAGE = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08l/runtime_package"
BRANE = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08k/modules/BRANE_3.1.zip"
API = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08k/modules/API_2.0.zip"
AI = ROOT / "MODEL/LIVE_MODEL/BRANE/runtime_08k/modules/AI_2.1.zip"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def prior_master_results() -> dict[str, dict[str, object]]:
    path = WORKSPACE / "master_native_query_receipt.json"
    if not path.exists():
        return {}
    receipt = json.loads(path.read_text(encoding="utf-8"))
    return {
        row["requested_handle"]: row
        for row in receipt.get("results", [])
        if row.get("status") == "complete"
        and all(Path(a["path"]).exists() for a in row.get("artifacts", []))
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_ids", nargs="+")
    args = parser.parse_args()
    chapter_ids = list(dict.fromkeys(args.chapter_ids))
    batch_slug = "_".join(cid.replace("-", "_") for cid in chapter_ids)
    out = WORKSPACE / "NATIVE_QUERY" / batch_slug
    state_path = WORKSPACE / f"native_query_state_{batch_slug}.json"
    receipt_path = WORKSPACE / f"native_query_receipt_{batch_slug}.json"
    out.mkdir(parents=True, exist_ok=True)

    library_rows = load_jsonl(LEDGER)
    all_handles = [str(row["short_handle"]) for row in library_rows]
    handle_set = set(all_handles)
    if len(all_handles) != 2384 or len(handle_set) != 2384:
        raise RuntimeError("authoritative API address ledger is not the expected 2,384-handle set")

    chapter_rows = {str(row["chapter_id"]): row for row in load_jsonl(CHAPTER_LEDGER)}
    missing_chapters = [cid for cid in chapter_ids if cid not in chapter_rows]
    if missing_chapters:
        raise RuntimeError(f"unknown chapter IDs: {missing_chapters}")
    requested = sorted({str(h) for cid in chapter_ids for h in chapter_rows[cid]["handles"]})
    missing_handles = sorted(set(requested) - handle_set)
    if missing_handles:
        raise RuntimeError(f"chapter ledger contains unknown handles: {missing_handles}")

    before = sha256(DB)
    if before != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 hash mismatch before native chapter query")

    reusable = prior_master_results()
    existing_results: dict[str, dict[str, object]] = {}
    if state_path.exists():
        prior = json.loads(state_path.read_text(encoding="utf-8"))
        if prior.get("database_sha256_before") != before:
            raise RuntimeError("chapter query state belongs to a different Library state")
        existing_results = {
            row["requested_handle"]: row
            for row in prior.get("results", [])
            if row.get("status") == "complete"
            and all(Path(a["path"]).exists() for a in row.get("artifacts", []))
        }

    checksums = {"ai": sha256(AI), "api": sha256(API), "library": sha256(ADAPTER)}
    results: list[dict[str, object]] = []
    runtime = None
    sys.path.insert(0, str(RUNTIME_PACKAGE))
    try:
        from mk43_runtime import MK43Runtime

        runtime = MK43Runtime(
            BRANE,
            modules={"ai": AI, "api": API, "library": ADAPTER},
            checksums=checksums,
            output_dir=out,
            development_mode=False,
        )
        for ordinal, handle in enumerate(requested):
            if handle in existing_results:
                row = dict(existing_results[handle])
                row["resumed_without_requery"] = True
                results.append(row)
                continue
            if handle in reusable:
                row = dict(reusable[handle])
                row["ordinal"] = ordinal
                row["reused_master_query"] = True
                row["resumed_without_requery"] = True
                results.append(row)
                continue

            started = time.perf_counter()
            before_files = set(out.glob("*.md"))
            try:
                response = runtime.submit(
                    {
                        "operation": "generate_report",
                        "subject": handle,
                        "request_id": f"mk-ultra-tome-{batch_slug}-{ordinal:04d}",
                        "depth": "structural",
                        "direction": "both",
                        "coverage_mode": "annotated",
                        "title": f"MK ULTRA TOME NATIVE QUERY - {handle}",
                        "options": {"defer_handles": all_handles},
                    }
                )
            except Exception as exc:
                response = {"status": "failed", "errors": [{"type": type(exc).__name__, "message": str(exc)}]}
            new_files = sorted(set(out.glob("*.md")) - before_files)
            row = {
                "ordinal": ordinal,
                "requested_handle": handle,
                "status": response.get("status"),
                "response": response,
                "artifacts": [
                    {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)}
                    for path in new_files
                ],
                "elapsed_seconds": round(time.perf_counter() - started, 6),
                "reused_master_query": False,
                "resumed_without_requery": False,
            }
            results.append(row)
            write_json(
                state_path,
                {
                    "schema": "mk-ultra-tome-native-chapter-query-state-v1",
                    "updated_at": utc_now(),
                    "chapter_ids": chapter_ids,
                    "database_sha256_before": before,
                    "requested_handles": requested,
                    "results": results,
                    "next_handle": requested[ordinal + 1] if ordinal + 1 < len(requested) else None,
                },
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
        "schema": "mk-ultra-tome-native-chapter-query-receipt-v1",
        "created_at": utc_now(),
        "chapter_ids": chapter_ids,
        "database_sha256_before": before,
        "database_sha256_after": after,
        "database_unchanged": before == after,
        "api_address_count": len(all_handles),
        "requested_handles": requested,
        "successful_queries": [r["requested_handle"] for r in results if r.get("status") == "complete"],
        "failed_queries": [r["requested_handle"] for r in results if r.get("status") != "complete"],
        "reused_master_queries": [r["requested_handle"] for r in results if r.get("reused_master_query")],
        "results": results,
        "runtime_info": runtime_info,
        "runtime_validation": runtime_validation,
    }
    write_json(receipt_path, receipt)
    write_json(state_path, {**receipt, "next_handle": None, "complete": True})
    if before != after:
        raise RuntimeError("Library 4.1 changed during native chapter queries")
    if receipt["failed_queries"]:
        raise RuntimeError(f"native chapter queries failed: {receipt['failed_queries']}")
    print(json.dumps({"chapters": chapter_ids, "queried": len(requested), "reused": len(receipt["reused_master_queries"]), "database_unchanged": True}))


if __name__ == "__main__":
    main()
