from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
LEDGER = WORKSPACE / "chapter_ledger.jsonl"
ARCHITECTURE = WORKSPACE / "genesis_language_architecture.json"
API_LEDGER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    os.replace(temp, path)


def main() -> None:
    rows = read_jsonl(LEDGER)
    chapter = next(row for row in rows if row["chapter_id"] == "V02-C01")
    if chapter.get("status") != "PLANNED":
        raise RuntimeError("V02-C01 is not at the planned assignment boundary")

    architecture = json.loads(ARCHITECTURE.read_text(encoding="utf-8"))
    if architecture.get("total_addresses") != 82 or len(architecture.get("addresses", [])) != 82:
        raise RuntimeError("Genesis Language architecture is not the validated 82-address set")
    handles = sorted(str(record["handle"]) for record in architecture["addresses"])
    if len(handles) != len(set(handles)):
        raise RuntimeError("Genesis Language architecture contains duplicate handles")

    api_handles = {str(row["short_handle"]) for row in read_jsonl(API_LEDGER)}
    missing = sorted(set(handles) - api_handles)
    if missing:
        raise RuntimeError(f"Genesis Language handles missing from Library 4.1: {missing}")

    existing = list(chapter.get("handles") or [])
    if existing and existing != handles:
        raise RuntimeError("V02-C01 already has a different handle assignment")
    chapter["handles"] = handles
    chapter["handle_count"] = len(handles)
    chapter["assignment_basis"] = "Validated Library 4.1 Genesis Language architecture; 82 native API/QMO addresses"
    chapter["assignment_architecture_sha256"] = sha256(ARCHITECTURE)
    write_jsonl(LEDGER, rows)

    toc_path = WORKSPACE / "MASTER_TOC.md"
    toc = toc_path.read_text(encoding="utf-8")
    old = "- V02-C01 [PLANNED] Why a New Representational Language Was Required - 0 assigned handles"
    new = "- V02-C01 [PLANNED] Why a New Representational Language Was Required - 82 assigned handles"
    if old in toc:
        toc_path.write_text(toc.replace(old, new), encoding="utf-8", newline="\n")
    elif new not in toc:
        raise RuntimeError("V02-C01 TOC assignment boundary is unexpected")

    receipt = {
        "schema": "mk-ultra-tome-chapter-handle-assignment/v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "chapter_id": "V02-C01",
        "assigned_handle_count": len(handles),
        "handles": handles,
        "basis": "Complete validated Genesis Language address inventory already derived through Runtime -> BRANE -> API/QMO -> Library 4.1",
        "architecture_path": str(ARCHITECTURE.relative_to(ROOT)),
        "architecture_sha256": sha256(ARCHITECTURE),
        "library_api_ledger_path": str(API_LEDGER.relative_to(ROOT)),
        "library_api_handle_count": len(api_handles),
        "missing_handles": [],
        "chapter_ledger_sha256_after": sha256(LEDGER),
    }
    out = WORKSPACE / "V02_C01_handle_assignment_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"chapter_id": "V02-C01", "assigned": len(handles), "receipt": str(out), "ledger_sha256": sha256(LEDGER)}))


if __name__ == "__main__":
    main()
