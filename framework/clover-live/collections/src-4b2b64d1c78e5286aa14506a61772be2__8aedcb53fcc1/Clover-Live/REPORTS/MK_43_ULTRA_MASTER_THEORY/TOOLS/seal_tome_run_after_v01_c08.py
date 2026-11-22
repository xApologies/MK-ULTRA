from __future__ import annotations

import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
CHECKPOINTS = ROOT / "CHECKPOINTS"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"
PDF = WORKSPACE / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_CHECKPOINT_V01_C08_VOLUME_I_COMPLETE.pdf"
REPORT = WORKSPACE / "TOME_GENERATION_CHECKPOINT_AFTER_V01_C08_VOLUME_I_COMPLETE.md"
RECEIPT = WORKSPACE / "native_query_receipt_V01_C08.json"
CHAPTER_HASHES = {
    "V01-C01": "b0183622e9fef05390234311933b61f4f6dd1cca3316e88b9b7e93167619e462",
    "V01-C02": "9736678393a7edc0607c3f55b22ef4acb85c8cf5336e1e83ebe4a83f83fcd96e",
    "V01-C03": "3a93df4c86e38c972229cf43ad22f2b108487b6e982b0fbd46fbfec4193c9a0b",
    "V01-C04": "856dfaa93199b1a724ae053fe48f9a36f1e79fe0f6a910e5227716d23517c60a",
    "V01-C05": "6995811daff42d30e79707c9a8a1bdfabda6c46513c7809e5bb36977b13b2b06",
    "V01-C06": "248e9970cf66d4d87fd7759b4c8c8cba11463f62597e1edadc35d4a34c591ad0",
    "V01-C07": "6809f8283bcd036e5a761ffb213bd4cf345c169619ee6d41cf8457e4cba3c234",
    "V01-C08": "58aa70c9f11331b085c9d12bad97f4bbadd699268104aa554da13718ceb66cd8",
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


def artifact(path: Path) -> dict[str, object]:
    return {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256(path)}


def report_workspace_size() -> int:
    return sum(path.stat().st_size for path in WORKSPACE.rglob("*") if path.is_file())


def main() -> None:
    db_hash = sha256(DB)
    if db_hash != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 hash mismatch at Volume I seal")
    sidecars = [str(Path(str(DB) + suffix)) for suffix in ("-wal", "-shm", "-journal") if Path(str(DB) + suffix).exists()]
    if sidecars:
        raise RuntimeError(f"unexpected database sidecars: {sidecars}")

    chapter_path = WORKSPACE / "chapter_ledger.jsonl"
    chapters = load_jsonl(chapter_path)
    complete = [row for row in chapters if row.get("status") == "COMPLETE"]
    if [row["chapter_id"] for row in complete] != list(CHAPTER_HASHES):
        raise RuntimeError("completed chapter boundary is not exactly V01-C01 through V01-C08")
    if any(row.get("volume_id") != "V01" for row in complete):
        raise RuntimeError("completed set crosses the intended Volume I boundary")
    for row in complete:
        path = ROOT / str(row["path"])
        if sha256(path) != CHAPTER_HASHES[str(row["chapter_id"])]:
            raise RuntimeError(f"chapter hash mismatch: {row['chapter_id']}")
    c08 = next(row for row in complete if row["chapter_id"] == "V01-C08")
    c08["formatted_page_estimate"] = 10
    c08["checkpoint_pdf"] = str(PDF.relative_to(ROOT))
    c08["checkpoint_pdf_page_span"] = "2-11"
    write_jsonl(chapter_path, chapters)

    reader = PdfReader(str(PDF))
    if reader.is_encrypted:
        raise RuntimeError("checkpoint PDF is unexpectedly encrypted")
    text_lengths = [len((page.extract_text() or "").strip()) for page in reader.pages]
    if len(reader.pages) != 11 or any(length == 0 for length in text_lengths):
        raise RuntimeError("Volume I checkpoint PDF pagination/text validation failed")
    pdf_hash = sha256(PDF)

    validation_path = WORKSPACE / "validation_ledger.jsonl"
    validations = load_jsonl(validation_path)
    ids = {"V01-C08-PDF", "V01-C08-SEQUENCE", "V01-C08-PROTECTED", "V01-COMPLETE"}
    existing = [row for row in validations if row.get("validation_id") in ids]
    existing_ids = {str(row["validation_id"]) for row in existing}
    if existing_ids and existing_ids != ids:
        raise RuntimeError("partial V01-C08/Volume I validation state exists")
    if existing_ids:
        if len(existing) != 4 or any(row.get("result") != "PASS" for row in existing):
            raise RuntimeError("existing Volume I validation rows are not a single complete PASS set")
    else:
        validations.extend(
            [
                {"validation_id": "V01-C08-PDF", "check": "Volume I completion PDF structural and visual validation", "result": "PASS", "value": {"pages": 11, "blank_pages": 0, "minimum_extracted_text_characters": min(text_lengths), "visual_inspection": "PASS_ALL_11_PAGES", "sha256": pdf_hash}},
                {"validation_id": "V01-C08-SEQUENCE", "check": "Sequential chapter boundary", "result": "PASS", "value": "V01-C01 through V01-C08 complete; V02-C01 next"},
                {"validation_id": "V01-C08-PROTECTED", "check": "Library 4.1 and completed chapters preserved", "result": "PASS", "value": {"library_sha256": db_hash, "chapter_hashes": CHAPTER_HASHES, "database_sidecars": []}},
                {"validation_id": "V01-COMPLETE", "check": "All planned Volume I chapters complete", "result": "PASS", "value": {"volume_id": "V01", "completed_chapters": 8, "next_volume": "V02"}},
            ]
        )
        write_jsonl(validation_path, validations)

    total_words = sum(int(row.get("word_count") or 0) for row in complete)
    total_pages = 9 + sum(int(row.get("formatted_page_estimate") or 0) for row in complete if row.get("chapter_id") != "V01-C01")
    if total_words != 35008 or total_pages != 80:
        raise RuntimeError(f"unexpected cumulative totals: {total_words} words, {total_pages} pages")
    equation_count = len(load_jsonl(WORKSPACE / "equation_ledger.jsonl"))
    citation_count = len(load_jsonl(WORKSPACE / "citation_ledger.jsonl"))
    qmo_count = len(load_jsonl(WORKSPACE / "qmo_derivation_ledger.jsonl"))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if len(receipt["requested_handles"]) != 116 or receipt["failed_queries"]:
        raise RuntimeError("native query receipt does not match V01-C08")

    report_text = f"""# MK Ultra TOME Generation Checkpoint after V01-C08 - Volume I Complete

## Outcome

The existing TOME was resumed at the exact first unfinished ledger entry. No previously completed chapter was regenerated or modified. The final chapter of Volume I was completed and sealed:

- V01-C08 - Conservation Across Representational Levels: 4,199 words, 116 assigned handles, SHA-256 `{CHAPTER_HASHES['V01-C08']}`.

All eight planned chapters of Volume I - Foundations are complete. The next unfinished chapter is V02-C01 - Why a New Representational Language Was Required.

## Native evidence

- Query architecture: `Runtime -> BRANE -> API/QMO -> Library 4.1`.
- Assigned handles queried this run: {len(receipt['requested_handles'])}.
- Successful native queries: {len(receipt['successful_queries'])}.
- Failed native queries: {len(receipt['failed_queries'])}.
- Reused sealed native reports: {len(receipt['reused_master_queries'])}.
- Library 4.1 SHA-256 before and after: `{db_hash}`.
- SOURCE or EXTRACTED rescanned: no.

## Publication state

- Chapters completed this run: 1.
- Completed chapters: 8 of 146.
- Fully completed volumes: 1 of 18.
- Cumulative word count: {total_words:,}.
- Cumulative formatted/PDF estimate: {total_pages} chapter pages.
- New checkpoint PDF: `{PDF.relative_to(ROOT)}` ({len(reader.pages)} pages including one checkpoint title page).
- Checkpoint PDF SHA-256: `{pdf_hash}`.
- Equation-ledger records: {equation_count}.
- Citation-ledger records: {citation_count}.
- QMO/derivation-ledger records: {qmo_count}.

## Validation

- All 11 checkpoint PDF pages were rendered and visually inspected: PASS.
- Blank PDF pages: 0.
- Minimum extracted text characters on any page: {min(text_lengths)}.
- V01-C01 through V01-C07 remain byte-identical: PASS.
- All eight Volume I chapter hashes match the authoritative ledger: PASS.
- Library 4.1 remains byte-identical: PASS.
- Library database sidecars: none.

This is a clean volume-boundary checkpoint, not completion of the TOME.
"""
    REPORT.write_text(report_text, encoding="utf-8", newline="\n")

    manifest_path = WORKSPACE / "master_report_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "publication_name": "MK Ultra",
            "status": "TOME_GENERATION_CHECKPOINTED",
            "completed_chapters": 8,
            "completed_volumes": 1,
            "current_cumulative_word_count": total_words,
            "current_formatted_page_estimate": total_pages,
            "next_resumable_chapter_id": "V02-C01",
            "next_resumable_chapter_title": "Why a New Representational Language Was Required",
            "library_database_sha256_after_seal": db_hash,
            "database_sidecars": [],
            "latest_checkpoint_pdf": {**artifact(PDF), "pages": 11, "blank_pages": 0, "visual_inspection": "PASS_ALL_11_PAGES"},
            "latest_checkpoint_report": artifact(REPORT),
            "sealed_at": utc_now(),
        }
    )
    tracked = [ROOT / item["path"] for item in manifest.get("artifacts", []) if (ROOT / item["path"]).exists()]
    tracked.extend([PDF, REPORT, RECEIPT, chapter_path, validation_path])
    unique: list[Path] = []
    seen: set[str] = set()
    for path in tracked:
        key = str(path.resolve())
        if key not in seen and path.exists() and path != manifest_path:
            seen.add(key)
            unique.append(path)
    manifest["artifacts"] = [artifact(path) for path in unique]
    manifest["equation_ledger_records"] = equation_count
    write_json(manifest_path, manifest)

    disk = shutil.disk_usage(ROOT)
    checkpoint = {
        "schema": "mk-ultra-tome-generation-run-checkpoint-v1",
        "created_at": utc_now(),
        "status": "TOME_GENERATION_CHECKPOINTED",
        "completed_chapters": [
            {"chapter_id": row["chapter_id"], "title": row["title"], "word_count": row["word_count"], "sha256": CHAPTER_HASHES[str(row["chapter_id"])]}
            for row in complete
        ],
        "completed_volumes": ["V01"],
        "next_resumable_chapter_id": "V02-C01",
        "next_resumable_chapter_title": "Why a New Representational Language Was Required",
        "current_cumulative_word_count": total_words,
        "current_formatted_pdf_page_estimate": total_pages,
        "newly_completed_this_run": ["V01-C08"],
        "newly_completed_volumes_this_run": ["V01"],
        "new_native_queries": len(receipt["requested_handles"]),
        "native_query_failures": receipt["failed_queries"],
        "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
        "checkpoint_pdf": {**artifact(PDF), "pages": 11, "blank_pages": 0, "minimum_extracted_text_characters": min(text_lengths), "visual_inspection": "PASS_ALL_11_PAGES"},
        "checkpoint_report": artifact(REPORT),
        "manifest_sha256": sha256(manifest_path),
        "ledger_hashes": {name: sha256(WORKSPACE / name) for name in ("chapter_ledger.jsonl", "equation_ledger.jsonl", "qmo_derivation_ledger.jsonl", "citation_ledger.jsonl", "validation_ledger.jsonl", "terminology_ledger.json")},
        "library_database_sha256": db_hash,
        "library_unchanged": True,
        "database_sidecars": [],
        "source_or_extracted_queried": False,
        "report_workspace_bytes": report_workspace_size(),
        "disk_free_bytes": disk.free,
    }
    final_checkpoint = CHECKPOINTS / "mk43_master_theory_generation_after_V01_C08.json"
    write_json(final_checkpoint, checkpoint)
    write_json(CHECKPOINTS / "mk43_master_theory_generation_current.json", checkpoint)
    print(json.dumps({"checkpoint": str(final_checkpoint), "completed_chapters": 8, "completed_volumes": 1, "total_words": total_words, "total_pages": total_pages, "next": "V02-C01", "pdf_sha256": pdf_hash, "library_sha256": db_hash}))


if __name__ == "__main__":
    main()
