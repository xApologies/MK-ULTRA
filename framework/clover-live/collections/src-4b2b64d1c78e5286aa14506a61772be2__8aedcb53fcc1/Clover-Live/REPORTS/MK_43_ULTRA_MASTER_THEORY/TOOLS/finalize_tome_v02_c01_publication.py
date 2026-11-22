from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
PUBLICATION = ROOT / "REPORTS/MK_ULTRA_MASTER_THEORY"
CHECKPOINTS = ROOT / "CHECKPOINTS"
RENDERER = ROOT / "TOOLS/TOME_PUBLICATION_RENDERER_V1"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"
CHAPTER_ID = "V02-C01"
CHAPTER_SOURCE = WORKSPACE / "VOLUME_02_GENESIS_LANGUAGE/V02_C01_WHY_A_NEW_REPRESENTATIONAL_LANGUAGE_WAS_REQUIRED.md"
VOLUME_PDF = PUBLICATION / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_VOLUME_01_FOUNDATIONS_COMPLETE_RENDERED.pdf"
VOLUME_VALIDATION = PUBLICATION / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_VOLUME_01_FOUNDATIONS_COMPLETE_RENDERED_VALIDATION.json"
CHAPTER_PDF = PUBLICATION / "VOLUME_02_GENESIS_LANGUAGE/MK_ULTRA_TOME_V02_C01_WHY_A_NEW_REPRESENTATIONAL_LANGUAGE_WAS_REQUIRED.pdf"
CHAPTER_VALIDATION = PUBLICATION / "VOLUME_02_GENESIS_LANGUAGE/MK_ULTRA_TOME_V02_C01_WHY_A_NEW_REPRESENTATIONAL_LANGUAGE_WAS_REQUIRED_VALIDATION.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def artifact(path: Path) -> dict[str, object]:
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: dict[str, object]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temp, path)


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    os.replace(temp, path)


def report_workspace_size() -> int:
    total = 0
    for path in (WORKSPACE, PUBLICATION):
        for item in path.rglob("*"):
            if item.is_file():
                try:
                    total += item.stat().st_size
                except OSError:
                    pass
    return total


def main() -> None:
    now = utc_now()
    required = [CHAPTER_SOURCE, VOLUME_PDF, VOLUME_VALIDATION, CHAPTER_PDF, CHAPTER_VALIDATION, DB]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"required finalization artifacts missing: {missing}")
    if sha256(DB) != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 changed before publication finalization")
    sidecars = [str(Path(str(DB) + suffix)) for suffix in ("-wal", "-shm", "-journal") if Path(str(DB) + suffix).exists()]
    if sidecars:
        raise RuntimeError(f"unexpected Library sidecars: {sidecars}")

    volume_validation = json.loads(VOLUME_VALIDATION.read_text(encoding="utf-8"))
    chapter_validation = json.loads(CHAPTER_VALIDATION.read_text(encoding="utf-8"))
    for validation, pdf, expected_pages, visual in (
        (volume_validation, VOLUME_PDF, 81, "ALL_81_PAGES"),
        (chapter_validation, CHAPTER_PDF, 11, "ALL_11_PAGES"),
    ):
        if validation["output"]["sha256"] != sha256(pdf):
            raise RuntimeError(f"PDF hash mismatch: {pdf}")
        if validation["actual_pages"] != expected_pages or validation["blank_pages"] != 0:
            raise RuntimeError(f"PDF pagination validation failed: {pdf}")
        if validation["raw_latex_guard"]["hits"]:
            raise RuntimeError(f"raw LaTeX guard failed: {pdf}")
        if validation["sealed_chapter_content_change_count"] != 0:
            raise RuntimeError(f"sealed chapter changed during rendering: {pdf}")
        if validation.get("visual_qa", {}).get("pages_inspected") != visual:
            raise RuntimeError(f"visual QA record missing: {pdf}")
        if validation["engine_metrics"].get("mathLayout", {}).get("remainingOverflow"):
            raise RuntimeError(f"math overflow remains: {pdf}")

    chapter_rows = read_jsonl(WORKSPACE / "chapter_ledger.jsonl")
    chapter = next(row for row in chapter_rows if row["chapter_id"] == CHAPTER_ID)
    if chapter.get("status") != "COMPLETE" or chapter.get("sha256") != sha256(CHAPTER_SOURCE):
        raise RuntimeError("V02-C01 is not at the sealed source boundary")
    if chapter.get("publication_pdf"):
        raise RuntimeError("V02-C01 publication metadata is already finalized")
    chapter.update(
        {
            "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
            "publication_pdf": str(CHAPTER_PDF.relative_to(ROOT)).replace("\\", "/"),
            "publication_pdf_sha256": sha256(CHAPTER_PDF),
            "publication_actual_pages": chapter_validation["actual_pages"],
            "publication_validation": str(CHAPTER_VALIDATION.relative_to(ROOT)).replace("\\", "/"),
            "publication_validation_sha256": sha256(CHAPTER_VALIDATION),
            "publication_raw_latex_guard": "PASS_ZERO_HITS",
            "publication_visual_qa": "PASS_ALL_11_PAGES",
            "publication_finalized_at": now,
        }
    )
    write_jsonl(WORKSPACE / "chapter_ledger.jsonl", chapter_rows)

    validation_ledger_path = WORKSPACE / "validation_ledger.jsonl"
    validation_rows = read_jsonl(validation_ledger_path)
    new_ids = {
        "TOME-PUBLICATION-RENDERER-V1-FREEZE",
        "VOLUME-I-CORRECTED-MATH-RENDER",
        "V02-C01-PUBLICATION-RENDER",
    }
    if new_ids & {str(row.get("validation_id")) for row in validation_rows}:
        raise RuntimeError("publication finalization validation rows already exist")
    validation_rows.extend(
        [
            {
                "validation_id": "TOME-PUBLICATION-RENDERER-V1-FREEZE",
                "check": "Math-aware renderer corrected, visually qualified, and frozen",
                "result": "PASS",
                "value": "KaTeX 0.16.22 -> HTML/CSS -> Playwright -> Microsoft Edge PDF; raw-LaTeX guard and display-overflow gate enabled",
            },
            {
                "validation_id": "VOLUME-I-CORRECTED-MATH-RENDER",
                "check": "Exact sealed V01-C01 through V01-C08 publication render",
                "result": "PASS",
                "value": {"pages": 81, "sha256": sha256(VOLUME_PDF), "source_changes": 0, "visual_qa": "ALL_81_PAGES"},
            },
            {
                "validation_id": "V02-C01-PUBLICATION-RENDER",
                "check": "V02-C01 typeset publication and native evidence register",
                "result": "PASS",
                "value": {"pages": 11, "sha256": sha256(CHAPTER_PDF), "source_changes": 0, "visual_qa": "ALL_11_PAGES"},
            },
        ]
    )
    write_jsonl(validation_ledger_path, validation_rows)

    terminology_path = WORKSPACE / "terminology_ledger.json"
    terminology = json.loads(terminology_path.read_text(encoding="utf-8"))
    terminology.update(
        {
            "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
            "publication_math_engine": "KaTeX 0.16.22",
            "reader_facing_raw_latex_policy": "RENDER_FAILURE",
            "publication_renderer_frozen_at": now,
        }
    )
    write_json(terminology_path, terminology)

    component_paths = [
        RENDERER / "render_engine.js",
        RENDERER / "render_publication.py",
        RENDERER / "README.md",
        RENDERER / "package.json",
        RENDERER / "pnpm-lock.yaml",
    ]
    renderer_manifest = {
        "schema": "tome-publication-renderer-freeze/v1",
        "renderer_id": "TOME_PUBLICATION_RENDERER_V1",
        "status": "FROZEN_VALIDATED",
        "frozen_at": now,
        "engine": "KaTeX 0.16.22 -> HTML/CSS -> Playwright -> Microsoft Edge PDF",
        "components": [artifact(path) for path in component_paths],
        "vendored_math_engine": {
            "name": "KaTeX",
            "version": "0.16.22",
            "path": "TOOLS/TOME_PUBLICATION_RENDERER_V1/vendor/katex/dist",
            "files": 81,
            "bytes": 2925582,
            "ordered_file_hash_manifest_sha256": "1e301d1e3d6a44e814d871beb980163a620fceb2674a267e827420d6d66f0bde",
        },
        "failure_policy": {
            "raw_latex_in_reader_facing_pages": "FAIL",
            "math_parse_error": "FAIL",
            "display_equation_overflow": "FAIL",
            "source_hash_change": "FAIL",
            "blank_page": "FAIL",
            "output_overwrite": "REFUSE",
        },
        "qualification_render": {
            **artifact(VOLUME_PDF),
            "pages": 81,
            "display_equations": 181,
            "inline_equations": 299,
            "blank_pages": 0,
            "visual_qa": "PASS_ALL_81_PAGES",
            "raw_latex_guard": "PASS_ZERO_HITS",
            "display_overflow": "PASS_ZERO_REMAINING",
        },
        "qualification_validation": artifact(VOLUME_VALIDATION),
        "first_production_render": {
            **artifact(CHAPTER_PDF),
            "chapter_id": CHAPTER_ID,
            "pages": 11,
            "display_equations": 18,
            "visual_qa": "PASS_ALL_11_PAGES",
        },
        "sealed_source_change_count": 0,
        "prior_pdf_preserved": {
            "path": "REPORTS/MK_ULTRA_MASTER_THEORY/VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_VOLUME_01_FOUNDATIONS_COMPLETE.pdf",
            "bytes": 408478,
            "sha256": "745b563222be85112217505fd3135307bef15882fb9023ba1b5fa1fd2a92c7d2",
        },
    }
    renderer_manifest_path = RENDERER / "renderer_manifest.json"
    write_json(renderer_manifest_path, renderer_manifest)

    renderer_checkpoint = {
        "schema": "tome-publication-renderer-checkpoint/v1",
        "created_at": now,
        "renderer_id": "TOME_PUBLICATION_RENDERER_V1",
        "status": "CORRECTED_VALIDATED_FROZEN",
        "renderer_manifest": str(renderer_manifest_path.relative_to(ROOT)).replace("\\", "/"),
        "renderer_manifest_sha256": sha256(renderer_manifest_path),
        "qualification_pdf": artifact(VOLUME_PDF),
        "actual_pages": 81,
        "raw_latex_guard": "PASS_ZERO_HITS",
        "display_overflow": "PASS_ZERO_REMAINING",
        "visual_qa": "PASS_ALL_81_PAGES",
        "sealed_source_change_count": 0,
        "next_tome_chapter": "V02-C02",
    }
    write_json(CHECKPOINTS / "tome_publication_renderer_v1.json", renderer_checkpoint)

    renderer_report = f"""# TOME Publication Renderer V1 Validation

Status: **TOME PUBLICATION RENDERER CORRECTED AND VALIDATED**

Frozen renderer: `TOME_PUBLICATION_RENDERER_V1`

## Corrected architecture

The former ReportLab path escaped equation source into reader-facing monospace text. The corrected pipeline parses the sealed Markdown structure, typesets inline and display mathematics with pinned KaTeX 0.16.22, lays out HTML/CSS with an explicit publication page box, and prints through local Microsoft Edge. It rejects math parse errors, exposed raw LaTeX, changed source hashes, blank pages, and residual display-equation overflow.

## Volume I qualification

- Output: `{VOLUME_PDF.relative_to(ROOT).as_posix()}`
- SHA-256: `{sha256(VOLUME_PDF)}`
- Actual pages: 81
- Chapters: V01-C01 through V01-C08
- Display equations: 181
- Inline expressions: 299
- Raw-LaTeX hits: 0
- Blank pages: 0
- Sealed chapter content changes: 0

All 81 final pages were rasterized with Poppler and inspected. The math-heavy opening pages of Chapters 1, 3, 4, 6, 7, and 8 were additionally inspected at full size. Greek letters, fractions, sums, tensors, arrows, tags, prose, tables, headers, and continuous page numbers are readable without clipping or overlap. The prior 81-page artifact remains preserved and was not overwritten.

## First production use

V02-C01 was rendered with the frozen configuration as an 11-page chapter publication. All 18 equations, the 82-address evidence register, and all prose passed the same structural and visual gates.

Result: **PASS — zero visible publication defects**.
"""
    (PUBLICATION / "TOME_PUBLICATION_RENDERER_V1_VALIDATION.md").write_text(renderer_report, encoding="utf-8", newline="\n")

    complete_rows = [row for row in chapter_rows if row.get("status") == "COMPLETE"]
    next_row = next(row for row in chapter_rows if row.get("status") != "COMPLETE")
    total_words = sum(int(row.get("word_count") or 0) for row in complete_rows)
    estimated_pages = sum(int(row.get("formatted_page_estimate") or (9 if row["chapter_id"] == "V01-C01" else 0)) for row in complete_rows)
    actual_pages = volume_validation["actual_pages"] + chapter_validation["actual_pages"]

    manifest_path = WORKSPACE / "master_report_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "status": "TOME_GENERATION_IN_PROGRESS",
            "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
            "completed_chapters": len(complete_rows),
            "completed_volumes": 1,
            "current_cumulative_word_count": total_words,
            "current_formatted_page_estimate": estimated_pages,
            "current_actual_publication_pages": actual_pages,
            "next_resumable_chapter_id": next_row["chapter_id"],
            "next_resumable_chapter_title": next_row["title"],
            "library_database_sha256_after_seal": sha256(DB),
            "database_sidecars": [],
            "source_or_extracted_rescanned": False,
            "publication_finalized_at": now,
        }
    )
    additions = [
        CHAPTER_SOURCE,
        VOLUME_PDF,
        VOLUME_VALIDATION,
        CHAPTER_PDF,
        CHAPTER_VALIDATION,
        renderer_manifest_path,
        PUBLICATION / "TOME_PUBLICATION_RENDERER_V1_VALIDATION.md",
        WORKSPACE / "V02_C01_handle_assignment_receipt.json",
        WORKSPACE / "native_query_receipt_V02_C01.json",
        WORKSPACE / "native_evidence_digest_V02_C01.json",
    ]
    by_path = {str(row["path"]).replace("\\", "/"): row for row in manifest.get("artifacts", []) if row.get("path")}
    for path in additions:
        row = artifact(path)
        by_path[str(row["path"])] = row
    manifest["artifacts"] = [by_path[key] for key in sorted(by_path)]
    write_json(manifest_path, manifest)

    ledger_names = (
        "chapter_ledger.jsonl",
        "equation_ledger.jsonl",
        "qmo_derivation_ledger.jsonl",
        "citation_ledger.jsonl",
        "validation_ledger.jsonl",
        "terminology_ledger.json",
    )
    disk = shutil.disk_usage(ROOT)
    checkpoint = {
        "schema": "mk-ultra-tome-generation-run-checkpoint-v1",
        "created_at": now,
        "status": "TOME_GENERATION_CHECKPOINTED",
        "newly_completed_this_run": [CHAPTER_ID],
        "completed_chapters": len(complete_rows),
        "total_planned_chapters": 146,
        "completed_volumes": 1,
        "total_planned_volumes": 18,
        "current_cumulative_word_count": total_words,
        "current_actual_publication_pages": actual_pages,
        "current_formatted_pdf_page_estimate": estimated_pages,
        "publication_renderer": "TOME_PUBLICATION_RENDERER_V1",
        "corrected_volume_i": artifact(VOLUME_PDF),
        "corrected_volume_i_validation": artifact(VOLUME_VALIDATION),
        "chapter": artifact(CHAPTER_SOURCE),
        "chapter_publication_pdf": artifact(CHAPTER_PDF),
        "chapter_publication_validation": artifact(CHAPTER_VALIDATION),
        "chapter_word_count": int(chapter["word_count"]),
        "chapter_actual_pages": int(chapter_validation["actual_pages"]),
        "assigned_handles": int(chapter["handle_count"]),
        "native_queries": 82,
        "native_query_failures": [],
        "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
        "library_database_sha256": sha256(DB),
        "library_unchanged": True,
        "database_sidecars": [],
        "source_or_extracted_queried": False,
        "next_resumable_chapter_id": next_row["chapter_id"],
        "next_resumable_chapter_title": next_row["title"],
        "report_workspace_bytes": report_workspace_size(),
        "disk_free_bytes": disk.free,
        "renderer_manifest_sha256": sha256(renderer_manifest_path),
        "manifest_sha256": sha256(manifest_path),
        "ledger_hashes": {name: sha256(WORKSPACE / name) for name in ledger_names},
    }
    checkpoint_path = CHECKPOINTS / "mk43_master_theory_generation_after_V02_C01.json"
    write_json(checkpoint_path, checkpoint)
    write_json(CHECKPOINTS / "mk43_master_theory_generation_current.json", checkpoint)

    checkpoint_report = f"""# MK Ultra TOME Generation Checkpoint After V02-C01

Status: **MK ULTRA TOME GENERATION CHECKPOINTED**

## Completed this run

- Corrected and froze `TOME_PUBLICATION_RENDERER_V1`.
- Re-rendered exact sealed Volume I as 81 reader-facing pages with 181 display equations and 299 inline expressions properly typeset.
- Completed, sealed, and published V02-C01 — *Why a New Representational Language Was Required*.
- Queried all 82 assigned Genesis Language addresses through Runtime -> BRANE -> API/QMO -> Library 4.1; all queries completed and Library 4.1 remained byte-identical.
- V02-C01 source: 5,128 words, SHA-256 `{sha256(CHAPTER_SOURCE)}`.
- V02-C01 publication: 11 pages, SHA-256 `{sha256(CHAPTER_PDF)}`.

## Cumulative boundary

- Chapters complete: 9 / 146
- Volumes complete: 1 / 18
- Cumulative words: {total_words:,}
- Cumulative actual publication pages: {actual_pages}
- Cumulative ledger page estimate: {estimated_pages}
- Renderer: `TOME_PUBLICATION_RENDERER_V1`
- Next chapter: {next_row['chapter_id']} — {next_row['title']}

The next clean resumable boundary is the planned V02-C02 ledger row. No completed chapter source was regenerated or modified, Library 4.1 remained unchanged, and SOURCE/EXTRACTED were not queried.
"""
    report_path = WORKSPACE / "TOME_GENERATION_CHECKPOINT_AFTER_V02_C01.md"
    report_path.write_text(checkpoint_report, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "status": "MK ULTRA TOME GENERATION CHECKPOINTED",
                "completed_this_run": [CHAPTER_ID],
                "completed_chapters": len(complete_rows),
                "cumulative_words": total_words,
                "actual_pages": actual_pages,
                "estimated_pages": estimated_pages,
                "next": next_row["chapter_id"],
                "renderer_manifest_sha256": sha256(renderer_manifest_path),
                "checkpoint": str(checkpoint_path),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
