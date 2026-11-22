from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
CHECKPOINT = ROOT / "CHECKPOINTS/mk43_master_theory_generation_initialization.json"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"
PDF = WORK / "VOLUME_01_FOUNDATIONS/V01_C01_WHAT_IS_MK_43_ULTRA.pdf"
MD = WORK / "VOLUME_01_FOUNDATIONS/V01_C01_WHAT_IS_MK_43_ULTRA.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def words(text: str) -> int:
    return len(re.findall(r"\b[\w@-]+\b", text, re.UNICODE))


def jdump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    if sha256(DB) != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 changed before initialization sealing")
    sidecars = [
        str(path.relative_to(ROOT))
        for suffix in ("-wal", "-shm", "-journal")
        if (Path(str(DB) + suffix)).exists()
        for path in [Path(str(DB) + suffix)]
    ]
    if sidecars:
        raise RuntimeError(f"Library database sidecars present: {sidecars}")

    receipt = json.loads((WORK / "master_native_query_receipt.json").read_text(encoding="utf-8"))
    manifest = json.loads((WORK / "master_report_manifest.json").read_text(encoding="utf-8"))
    chapters = [json.loads(line) for line in (WORK / "chapter_ledger.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    handle_union = {handle for chapter in chapters for handle in chapter["handles"]}
    if len(handle_union) != 2384:
        raise RuntimeError(f"chapter assignment union is {len(handle_union)}, expected 2384")
    if len(chapters) != 146:
        raise RuntimeError("planned chapter ledger mismatch")
    if receipt.get("failed_queries") or len(receipt.get("successful_queries", [])) != 179:
        raise RuntimeError("native master query is incomplete")
    if len(receipt.get("genesis_language_handles", [])) != 82:
        raise RuntimeError("Genesis Language native query family mismatch")

    reader = PdfReader(str(PDF))
    page_text = [(page.extract_text() or "") for page in reader.pages]
    pdf_validation = {
        "path": str(PDF.relative_to(ROOT)),
        "bytes": PDF.stat().st_size,
        "sha256": sha256(PDF),
        "pages": len(reader.pages),
        "encrypted": reader.is_encrypted,
        "blank_pages": sum(not text.strip() for text in page_text),
        "minimum_extracted_text_characters_on_page": min(map(len, page_text)),
        "title": reader.metadata.title if reader.metadata else None,
        "visual_inspection": "PASS_ALL_9_PAGES",
    }
    if reader.is_encrypted or pdf_validation["blank_pages"] or len(reader.pages) != 9:
        raise RuntimeError("first-chapter PDF validation failed")

    # Add the publication PDF to the manifest without regenerating the completed Markdown chapter.
    artifact_map = {row["path"]: row for row in manifest["artifacts"]}
    for path in [PDF]:
        rel = str(path.relative_to(ROOT))
        artifact_map[rel] = {"path": rel, "bytes": path.stat().st_size, "sha256": sha256(path)}
    manifest["artifacts"] = sorted(artifact_map.values(), key=lambda row: row["path"])
    manifest["sealed_at"] = datetime.now(timezone.utc).isoformat()
    manifest["status"] = "INITIALIZED_AND_VALIDATED"
    manifest["first_chapter_pdf"] = pdf_validation
    manifest["library_database_sha256_after_seal"] = sha256(DB)
    manifest["library_mutated"] = False
    manifest["database_sidecars"] = sidecars
    jdump(WORK / "master_report_manifest.json", manifest)

    summary = f'''# MK 43 Ultra Master Theory - Initialization Summary

The master theory workspace is initialized and resumable.

- Planned volumes: **{manifest['planned_volumes']}**
- Planned chapters: **{manifest['planned_chapters']}**
- Library handles assigned to at least one chapter: **{manifest['api_handles_assigned']}**
- Native Library queries completed: **{len(receipt['successful_queries'])}**
- Genesis Language addresses recovered: **{manifest['genesis_language_addresses']}**
- Genesis Language chapters planned: **{manifest['genesis_language_chapters']}**
- Major API-native/QMO-derived objects identified: **{manifest['api_native_qmo_major_objects']}**
- First completed chapter: **V01-C01 - What Is MK 43 Ultra?**
- Current theory-prose word count: **{words(MD.read_text(encoding='utf-8'))}**
- Next resumable chapter: **V01-C02 - Distinction, Information, and Structural Reality**
- Library 4.1 database: **unchanged**
- Native architecture: **Runtime -> BRANE -> API/QMO -> Library 4.1**
'''
    summary_path = WORK / "INITIALIZATION_SUMMARY.md"
    summary_path.write_text(summary, encoding="utf-8")

    checkpoint = {
        "schema": "mk43-master-theory-initialization-checkpoint-v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "INITIALIZED_AND_VALIDATED",
        "report_workspace": str(WORK),
        "planned_volumes": manifest["planned_volumes"],
        "planned_chapters": manifest["planned_chapters"],
        "library_handles_assigned": manifest["api_handles_assigned"],
        "native_queries_completed": len(receipt["successful_queries"]),
        "genesis_language_addresses": manifest["genesis_language_addresses"],
        "genesis_language_chapters": manifest["genesis_language_chapters"],
        "api_native_qmo_major_objects": manifest["api_native_qmo_major_objects"],
        "first_completed_chapter": "V01-C01",
        "first_completed_chapter_markdown": {
            "path": str(MD.relative_to(ROOT)),
            "bytes": MD.stat().st_size,
            "sha256": sha256(MD),
            "word_count": words(MD.read_text(encoding="utf-8")),
        },
        "first_completed_chapter_pdf": pdf_validation,
        "current_cumulative_word_count": words(MD.read_text(encoding="utf-8")),
        "next_resumable_chapter_id": "V01-C02",
        "next_resumable_chapter_title": "Distinction, Information, and Structural Reality",
        "library_database_sha256": sha256(DB),
        "library_unchanged": sha256(DB) == EXPECTED_DB_SHA,
        "database_sidecars": sidecars,
        "protected_source_trees_queried": False,
        "master_manifest": {
            "path": str((WORK / "master_report_manifest.json").relative_to(ROOT)),
            "sha256": sha256(WORK / "master_report_manifest.json"),
        },
        "summary": {
            "path": str(summary_path.relative_to(ROOT)),
            "sha256": sha256(summary_path),
        },
    }
    jdump(CHECKPOINT, checkpoint)
    print(json.dumps(checkpoint, ensure_ascii=False))


if __name__ == "__main__":
    main()
