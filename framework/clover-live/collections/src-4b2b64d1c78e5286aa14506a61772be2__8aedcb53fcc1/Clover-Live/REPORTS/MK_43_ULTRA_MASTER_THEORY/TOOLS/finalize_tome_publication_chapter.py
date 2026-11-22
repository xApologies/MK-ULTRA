from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
PUBLICATION = ROOT / "REPORTS/MK_ULTRA_MASTER_THEORY"
CHECKPOINTS = ROOT / "CHECKPOINTS"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"
RENDERER_MANIFEST = ROOT / "TOOLS/TOME_PUBLICATION_RENDERER_V1/renderer_manifest.json"
VOLUME_I_PDF = PUBLICATION / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_VOLUME_01_FOUNDATIONS_COMPLETE_RENDERED.pdf"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    os.replace(temporary, path)


def artifact(path: Path) -> dict[str, object]:
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def workspace_size() -> int:
    total = 0
    for path in WORKSPACE.rglob("*"):
        if path.is_file():
            try:
                total += path.stat().st_size
            except OSError:
                pass
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id")
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--validation", required=True, type=Path)
    parser.add_argument("--run-chapters", required=True)
    args = parser.parse_args()
    now = utc_now()
    pdf = args.pdf.resolve()
    validation_path = args.validation.resolve()
    run_chapters = [value for value in args.run_chapters.split(",") if value]

    if sha256(DB) != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 changed before publication finalization")
    sidecars = [str(Path(str(DB) + suffix)) for suffix in ("-wal", "-shm", "-journal") if Path(str(DB) + suffix).exists()]
    if sidecars:
        raise RuntimeError(f"unexpected Library sidecars: {sidecars}")
    uri = "file:" + DB.as_posix() + "?mode=ro&immutable=1"
    connection = sqlite3.connect(uri, uri=True)
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    foreign_keys = len(connection.execute("PRAGMA foreign_key_check").fetchall())
    connection.close()
    if integrity != "ok" or foreign_keys:
        raise RuntimeError(f"Library validation failed: integrity={integrity}, foreign_keys={foreign_keys}")

    renderer = json.loads(RENDERER_MANIFEST.read_text(encoding="utf-8"))
    if renderer.get("renderer_id") != "TOME_PUBLICATION_RENDERER_V1" or renderer.get("status") != "FROZEN_VALIDATED":
        raise RuntimeError("frozen publication renderer boundary is invalid")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("renderer") != "TOME_PUBLICATION_RENDERER_V1":
        raise RuntimeError("chapter was not rendered with the frozen renderer")
    if validation["output"]["sha256"] != sha256(pdf):
        raise RuntimeError("publication PDF hash does not match validation")
    if validation.get("blank_pages") != 0 or validation.get("raw_latex_guard", {}).get("hits"):
        raise RuntimeError("publication structural validation failed")
    if validation.get("sealed_chapter_content_change_count") != 0:
        raise RuntimeError("sealed chapter changed during rendering")
    if validation.get("engine_metrics", {}).get("mathLayout", {}).get("remainingOverflow"):
        raise RuntimeError("display-math overflow remains")
    if validation.get("visual_qa", {}).get("result") != "PASS":
        raise RuntimeError("complete visual QA has not been recorded")

    ledger_path = WORKSPACE / "chapter_ledger.jsonl"
    rows = read_jsonl(ledger_path)
    chapter = next(row for row in rows if row["chapter_id"] == args.chapter_id)
    chapter_source = ROOT / str(chapter["path"])
    if chapter.get("status") != "COMPLETE" or chapter.get("sha256") != sha256(chapter_source):
        raise RuntimeError("chapter is not at the sealed source boundary")
    expected_publication = {
        "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
        "publication_pdf": pdf.relative_to(ROOT).as_posix(),
        "publication_pdf_sha256": sha256(pdf),
        "publication_actual_pages": int(validation["actual_pages"]),
        "publication_validation": validation_path.relative_to(ROOT).as_posix(),
        "publication_validation_sha256": sha256(validation_path),
        "publication_raw_latex_guard": "PASS_ZERO_HITS",
        "publication_visual_qa": validation["visual_qa"]["pages_inspected"],
    }
    if chapter.get("publication_pdf"):
        mismatches = {
            key: {"expected": value, "found": chapter.get(key)}
            for key, value in expected_publication.items()
            if chapter.get(key) != value
        }
        if mismatches:
            raise RuntimeError(f"inconsistent partial publication commit: {mismatches}")
    else:
        chapter.update(expected_publication)
        chapter["publication_finalized_at"] = now
        write_jsonl(ledger_path, rows)

    validation_ledger_path = WORKSPACE / "validation_ledger.jsonl"
    validation_rows = read_jsonl(validation_ledger_path)
    validation_id = f"{args.chapter_id}-PUBLICATION-RENDER"
    existing_validation_rows = [row for row in validation_rows if str(row.get("validation_id")) == validation_id]
    expected_validation_value = {
        "renderer": "TOME_PUBLICATION_RENDERER_V1",
        "pages": int(validation["actual_pages"]),
        "sha256": sha256(pdf),
        "source_changes": 0,
        "visual_qa": validation["visual_qa"]["pages_inspected"],
    }
    if existing_validation_rows:
        if len(existing_validation_rows) != 1 or existing_validation_rows[0].get("result") != "PASS" or existing_validation_rows[0].get("value") != expected_validation_value:
            raise RuntimeError("inconsistent partial publication validation commit")
    else:
        validation_rows.append({
            "validation_id": validation_id,
            "check": f"{args.chapter_id} frozen-renderer publication and visual QA",
            "result": "PASS",
            "value": expected_validation_value,
        })
        write_jsonl(validation_ledger_path, validation_rows)

    complete = [row for row in rows if row.get("status") == "COMPLETE"]
    next_row = next((row for row in rows if row.get("status") != "COMPLETE"), None)
    next_id = next_row["chapter_id"] if next_row else None
    next_title = next_row["title"] if next_row else None
    complete_volumes = sum(
        all(row.get("status") == "COMPLETE" for row in rows if row["volume_id"] == volume)
        for volume in sorted({row["volume_id"] for row in rows})
    )
    total_words = sum(int(row.get("word_count") or 0) for row in complete)
    actual_pages = 81 + sum(int(row.get("publication_actual_pages") or 0) for row in complete if row["volume_id"] != "V01")

    manifest_path = WORKSPACE / "master_report_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "status": "TOME_GENERATION_COMPLETE" if next_row is None else "TOME_GENERATION_IN_PROGRESS",
        "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
        "completed_chapters": len(complete),
        "completed_volumes": complete_volumes,
        "current_cumulative_word_count": total_words,
        "current_actual_publication_pages": actual_pages,
        "next_resumable_chapter_id": next_id,
        "next_resumable_chapter_title": next_title,
        "library_database_sha256_after_seal": sha256(DB),
        "database_sidecars": [],
        "source_or_extracted_rescanned": False,
        "publication_finalized_at": now,
    })
    additions = [
        chapter_source,
        pdf,
        validation_path,
        WORKSPACE / f"{args.chapter_id.replace('-', '_')}_handle_assignment_receipt.json",
        WORKSPACE / f"native_query_receipt_{args.chapter_id.replace('-', '_')}.json",
        WORKSPACE / f"native_evidence_digest_{args.chapter_id.replace('-', '_')}.json",
    ]
    artifact_rows = {str(row["path"]).replace("\\", "/"): row for row in manifest.get("artifacts", []) if row.get("path")}
    for path in additions:
        item = artifact(path)
        artifact_rows[str(item["path"])] = item
    manifest["artifacts"] = [artifact_rows[key] for key in sorted(artifact_rows)]
    write_json(manifest_path, manifest)

    ledgers = (
        "chapter_ledger.jsonl", "equation_ledger.jsonl", "qmo_derivation_ledger.jsonl",
        "citation_ledger.jsonl", "validation_ledger.jsonl", "terminology_ledger.json",
    )
    disk = shutil.disk_usage(ROOT)
    checkpoint = {
        "schema": "mk-ultra-tome-generation-run-checkpoint-v1",
        "created_at": now,
        "status": "TOME_GENERATION_COMPLETE" if next_row is None else "TOME_GENERATION_CHECKPOINTED",
        "chapters_completed_this_run": run_chapters,
        "completed_chapters": len(complete),
        "total_planned_chapters": len(rows),
        "completed_volumes": complete_volumes,
        "total_planned_volumes": len({row["volume_id"] for row in rows}),
        "current_cumulative_word_count": total_words,
        "current_actual_publication_pages": actual_pages,
        "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
        "last_chapter": artifact(chapter_source),
        "last_chapter_publication_pdf": artifact(pdf),
        "last_chapter_publication_validation": artifact(validation_path),
        "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
        "library_database_sha256": sha256(DB),
        "library_unchanged": True,
        "sqlite_integrity_check": integrity,
        "foreign_key_violations": foreign_keys,
        "database_sidecars": [],
        "source_or_extracted_queried": False,
        "next_resumable_chapter_id": next_id,
        "next_resumable_chapter_title": next_title,
        "workspace_bytes": workspace_size(),
        "disk_free_bytes": disk.free,
        "renderer_manifest_sha256": sha256(RENDERER_MANIFEST),
        "manifest_sha256": sha256(manifest_path),
        "ledger_hashes": {name: sha256(WORKSPACE / name) for name in ledgers},
    }
    checkpoint_path = CHECKPOINTS / f"mk43_master_theory_generation_after_{args.chapter_id.replace('-', '_')}.json"
    write_json(checkpoint_path, checkpoint)
    write_json(CHECKPOINTS / "mk43_master_theory_generation_current.json", checkpoint)
    report = f"""# MK Ultra TOME Generation Checkpoint After {args.chapter_id}

- Chapters completed this run: {', '.join(run_chapters)}
- Cumulative chapters: {len(complete)} / {len(rows)}
- Completed volumes: {complete_volumes} / {len({row['volume_id'] for row in rows})}
- Cumulative word count: {total_words:,}
- Cumulative actual rendered pages: {actual_pages}
- Next unfinished chapter: {next_id or 'NONE'}{(' - ' + next_title) if next_title else ''}
"""
    report_path = WORKSPACE / f"TOME_GENERATION_CHECKPOINT_AFTER_{args.chapter_id.replace('-', '_')}.md"
    report_path.write_text(report, encoding="utf-8", newline="\n")
    print(json.dumps({
        "chapter": args.chapter_id,
        "chapters_completed_this_run": run_chapters,
        "complete": len(complete),
        "volumes": complete_volumes,
        "words": total_words,
        "actual_pages": actual_pages,
        "next": next_id,
        "checkpoint": str(checkpoint_path),
    }))


if __name__ == "__main__":
    main()
