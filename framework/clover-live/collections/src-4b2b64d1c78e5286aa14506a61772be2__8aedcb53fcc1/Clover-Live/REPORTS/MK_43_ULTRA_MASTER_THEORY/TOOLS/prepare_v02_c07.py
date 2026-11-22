from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
LEDGER = WORKSPACE / "chapter_ledger.jsonl"
API_LEDGER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
CHAPTER_ID = "V02-C07"
HANDLES = sorted({
    "@bandwidth", "@closure", "@continuation_inheritance_compatibility",
    "@emergence_of_continuum_locality", "@factorisation_and_proto_locality",
    "@genesis_closure", "@genesis_recursive_inheritance", "@inheritance",
    "@inheritance_morphism", "@local_recursive_state", "@locality",
    "@localization_closure_parameter", "@localized_er_foam_knot",
    "@localized_persistent_topology", "@occupancy", "@persistence",
    "@persistence_potential", "@persistent_recursive_topology",
    "@proto_locality_the_first_signs_of_division", "@recursive_continuity",
    "@recursive_depth", "@recursive_inheritance", "@recursive_occupancy",
    "@recursive_ordering", "@resolution",
})


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    os.replace(temporary, path)


def main() -> None:
    rows = read_jsonl(LEDGER)
    chapter = next(row for row in rows if row["chapter_id"] == CHAPTER_ID)
    if chapter.get("status") != "PLANNED" or chapter.get("path") is not None:
        raise RuntimeError(f"{CHAPTER_ID} is not at the untouched planned boundary")
    api_handles = {str(row["short_handle"]) for row in read_jsonl(API_LEDGER)}
    missing = sorted(set(HANDLES) - api_handles)
    if missing:
        raise RuntimeError(f"handles absent from Library 4.1: {missing}")
    chapter.update({
        "handles": HANDLES,
        "handle_count": len(HANDLES),
        "assignment_basis": "Library 4.1 recursion, inheritance, persistence, closure, occupancy, resolution, bandwidth, proto-locality, and localization address set",
        "assignment_api_ledger_sha256": sha256(API_LEDGER),
    })
    write_jsonl(LEDGER, rows)
    toc_path = WORKSPACE / "MASTER_TOC.md"
    toc = toc_path.read_text(encoding="utf-8")
    old = f"- {CHAPTER_ID} [PLANNED] Recursion and Localization - 0 assigned handles"
    new = f"- {CHAPTER_ID} [PLANNED] Recursion and Localization - {len(HANDLES)} assigned handles"
    if old in toc:
        toc_path.write_text(toc.replace(old, new), encoding="utf-8", newline="\n")
    elif new not in toc:
        raise RuntimeError("TOC assignment boundary is unexpected")
    receipt = {
        "schema": "mk-ultra-tome-chapter-handle-assignment/v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "chapter_id": CHAPTER_ID,
        "assigned_handle_count": len(HANDLES),
        "handles": HANDLES,
        "basis": "Native Library 4.1 address selection for recursive organization, inherited continuity, persistence, closure, and emergence of locality",
        "library_api_ledger_path": API_LEDGER.relative_to(ROOT).as_posix(),
        "library_api_ledger_sha256": sha256(API_LEDGER),
        "missing_handles": [],
        "chapter_ledger_sha256_after": sha256(LEDGER),
    }
    output = WORKSPACE / "V02_C07_handle_assignment_receipt.json"
    output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"chapter_id": CHAPTER_ID, "assigned": len(HANDLES)}))


if __name__ == "__main__":
    main()
