from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
CHECKPOINTS = ROOT / "CHECKPOINTS"

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

def write_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id")
    parser.add_argument("--prior-sha256", required=True)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--reason", required=True)
    args = parser.parse_args()
    if args.pdf.exists():
        raise RuntimeError("refusing correction after publication PDF creation")
    ledger_path = WORKSPACE / "chapter_ledger.jsonl"
    chapter_rows = read_jsonl(ledger_path)
    chapter = next(row for row in chapter_rows if row["chapter_id"] == args.chapter_id)
    if chapter.get("status") != "COMPLETE" or chapter.get("sha256") != args.prior_sha256 or chapter.get("publication_pdf"):
        raise RuntimeError("chapter is not at the expected unpublished seal boundary")
    source = ROOT / str(chapter["path"])
    new = sha256(source)
    if new == args.prior_sha256:
        raise RuntimeError("source hash did not change")
    now = datetime.now(timezone.utc).isoformat()

    ledger_names = ("chapter_ledger.jsonl", "equation_ledger.jsonl", "qmo_derivation_ledger.jsonl", "citation_ledger.jsonl", "validation_ledger.jsonl")
    for name in ledger_names:
        path = WORKSPACE / name
        rows = chapter_rows if name == "chapter_ledger.jsonl" else read_jsonl(path)
        changed = 0
        for row in rows:
            if row.get("chapter_id") != args.chapter_id:
                continue
            for key in ("sha256", "chapter_sha256"):
                if row.get(key) == args.prior_sha256:
                    row[key] = new
                    changed += 1
            if name == "chapter_ledger.jsonl":
                row["bytes"] = source.stat().st_size
                row["sealed_at"] = now
                row["prepublication_correction"] = {
                    "reason": args.reason,
                    "prior_sha256": args.prior_sha256,
                    "semantic_content_change": False,
                }
            if name == "validation_ledger.jsonl" and row.get("validation_id") == f"{args.chapter_id}-HASH":
                if row.get("value") != args.prior_sha256:
                    raise RuntimeError("validation hash row had unexpected value")
                row["value"] = new
                changed += 1
        if name != "validation_ledger.jsonl" and not changed:
            raise RuntimeError(f"no chapter hash references updated in {name}")
        write_jsonl(path, rows)

    manifest_path = WORKSPACE / "master_report_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source_rel = source.relative_to(ROOT).as_posix()
    for item in manifest.get("artifacts", []):
        if str(item.get("path", "")).replace("\\", "/") == source_rel:
            item.update({"bytes": source.stat().st_size, "sha256": new})
    write_json(manifest_path, manifest)

    slug = args.chapter_id.replace("-", "_")
    for checkpoint_path in (
        CHECKPOINTS / f"mk43_master_theory_generation_{slug}.json",
        CHECKPOINTS / "mk43_master_theory_generation_current.json",
    ):
        checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
        if checkpoint.get("chapter_id") != args.chapter_id:
            raise RuntimeError(f"unexpected checkpoint boundary: {checkpoint_path}")
        checkpoint["chapter"].update({"bytes": source.stat().st_size, "sha256": new})
        checkpoint["created_at"] = now
        checkpoint["prepublication_correction"] = args.reason
        checkpoint["manifest_sha256"] = sha256(manifest_path)
        for name in ledger_names:
            checkpoint["ledger_hashes"][name] = sha256(WORKSPACE / name)
        write_json(checkpoint_path, checkpoint)

    receipt = {
        "schema": "tome-prepublication-correction/v1",
        "chapter_id": args.chapter_id,
        "created_at": now,
        "prior_sha256": args.prior_sha256,
        "corrected_sha256": new,
        "correction": args.reason,
        "semantic_content_change": False,
        "publication_pdf_existed_before_correction": False,
        "previously_completed_chapters_modified": False,
    }
    output = WORKSPACE / f"{slug}_prepublication_correction_receipt.json"
    write_json(output, receipt)
    print(json.dumps(receipt))

if __name__ == "__main__":
    main()
