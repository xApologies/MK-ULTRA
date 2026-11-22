from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
CHECKPOINTS = ROOT / "CHECKPOINTS"
SOURCE = WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C03_HANDLES_ADDRESSES_AND_NAMES.md"
PDF = ROOT / "REPORTS/MK_ULTRA_MASTER_THEORY/VOLUME_02_GENESIS_LANGUAGE/MK_ULTRA_TOME_V02_C03_HANDLES_ADDRESSES_AND_NAMES.pdf"
OLD = "acddc0017647bf81bb261925294f2435d3e5372fa81064028d2afccf09ca04a2"

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
    if PDF.exists():
        raise RuntimeError("refusing correction after publication PDF creation")
    text = SOURCE.read_text(encoding="utf-8")
    if "For record \\(r\\) and presentation scope \\(s\\), write" not in text:
        raise RuntimeError("expected corrected delimiter is absent")
    new = sha256(SOURCE)
    if new == OLD:
        raise RuntimeError("source hash did not change")
    now = datetime.now(timezone.utc).isoformat()
    ledger_names = ("chapter_ledger.jsonl", "equation_ledger.jsonl", "qmo_derivation_ledger.jsonl", "citation_ledger.jsonl", "validation_ledger.jsonl")
    for name in ledger_names:
        path = WORKSPACE / name
        rows = read_jsonl(path)
        changed = 0
        for row in rows:
            if row.get("chapter_id") == "V02-C03":
                for key in ("sha256", "chapter_sha256"):
                    if row.get(key) == OLD:
                        row[key] = new
                        changed += 1
                if name == "chapter_ledger.jsonl":
                    if row.get("sha256") != new:
                        raise RuntimeError("chapter ledger was not at expected prior seal")
                    row["bytes"] = SOURCE.stat().st_size
                    row["sealed_at"] = now
                    row["prepublication_correction"] = {
                        "reason": "frozen renderer caught one malformed inline-math closing delimiter before PDF creation",
                        "prior_sha256": OLD,
                        "semantic_content_change": False,
                    }
                if name == "validation_ledger.jsonl" and row.get("validation_id") == "V02-C03-HASH":
                    if row.get("value") != OLD:
                        raise RuntimeError("validation hash row had unexpected value")
                    row["value"] = new
                    changed += 1
        if name != "validation_ledger.jsonl" and not changed:
            raise RuntimeError(f"no V02-C03 hash references updated in {name}")
        write_jsonl(path, rows)

    manifest_path = WORKSPACE / "master_report_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source_rel = SOURCE.relative_to(ROOT).as_posix()
    for item in manifest.get("artifacts", []):
        if str(item.get("path", "")).replace("\\", "/") == source_rel:
            item.update({"bytes": SOURCE.stat().st_size, "sha256": new})
    write_json(manifest_path, manifest)

    for checkpoint_path in (
        CHECKPOINTS / "mk43_master_theory_generation_V02_C03.json",
        CHECKPOINTS / "mk43_master_theory_generation_current.json",
    ):
        checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
        if checkpoint.get("chapter_id") != "V02-C03":
            raise RuntimeError(f"unexpected checkpoint boundary: {checkpoint_path}")
        checkpoint["chapter"].update({"bytes": SOURCE.stat().st_size, "sha256": new})
        checkpoint["created_at"] = now
        checkpoint["prepublication_correction"] = "ONE_CHARACTER_MATH_DELIMITER_CORRECTION_BEFORE_RENDER"
        checkpoint["manifest_sha256"] = sha256(manifest_path)
        for name in ("chapter_ledger.jsonl", "equation_ledger.jsonl", "qmo_derivation_ledger.jsonl", "citation_ledger.jsonl", "validation_ledger.jsonl"):
            checkpoint["ledger_hashes"][name] = sha256(WORKSPACE / name)
        write_json(checkpoint_path, checkpoint)

    receipt = {
        "schema": "tome-prepublication-correction/v1",
        "chapter_id": "V02-C03",
        "created_at": now,
        "prior_sha256": OLD,
        "corrected_sha256": new,
        "correction": "Added the missing backslash to one inline-math closing delimiter.",
        "semantic_content_change": False,
        "publication_pdf_existed_before_correction": False,
        "previously_completed_chapters_modified": False,
    }
    output = WORKSPACE / "V02_C03_prepublication_correction_receipt.json"
    write_json(output, receipt)
    print(json.dumps(receipt))

if __name__ == "__main__":
    main()
