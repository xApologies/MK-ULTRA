from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def block_after(text: str, marker: str) -> dict[str, object]:
    start = text.find(marker)
    if start < 0:
        return {}
    start = text.find("{", start + len(marker))
    if start < 0:
        return {}
    try:
        value, _ = json.JSONDecoder().raw_decode(text[start:])
        return value if isinstance(value, dict) else {}
    except json.JSONDecodeError:
        return {}


def compact_record(record: dict[str, object], text_keys: tuple[str, ...]) -> dict[str, object]:
    keep = {
        key: record.get(key)
        for key in (
            "definition_id",
            "equation_id",
            "environment",
            "evidence_class",
            "classification",
            "statement_id",
            "record_id",
            "source_unit_id",
            "source_content_hash",
            "source_occurrence_id",
            "provenance",
        )
        if key in record
    }
    for key in text_keys:
        value = record.get(key)
        if isinstance(value, str) and len(value) <= 4000 and "Canonical source window" not in value:
            keep[key] = value
    return keep


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_ids", nargs="+")
    args = parser.parse_args()
    batch_slug = "_".join(cid.replace("-", "_") for cid in args.chapter_ids)
    receipt_path = WORKSPACE / f"native_query_receipt_{batch_slug}.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    chapter_rows = {row["chapter_id"]: row for row in load_jsonl(WORKSPACE / "chapter_ledger.jsonl")}
    result_by_handle = {row["requested_handle"]: row for row in receipt["results"]}

    chapters: list[dict[str, object]] = []
    for chapter_id in args.chapter_ids:
        chapter = chapter_rows[chapter_id]
        handle_records: list[dict[str, object]] = []
        for handle in chapter["handles"]:
            result = result_by_handle[handle]
            artifact = result["artifacts"][0]
            path = Path(artifact["path"])
            text = path.read_text(encoding="utf-8", errors="replace")
            identity = block_after(text, f"API 4.3 identity")
            graph = block_after(text, f"API 4.3 graph neighborhood")
            metadata = block_after(text, f"compiled metadata")
            coverage = metadata.get("coverage_v2", {}) if isinstance(metadata, dict) else {}
            definitions = metadata.get("definition_records", []) if isinstance(metadata, dict) else []
            equations = metadata.get("equation_records", []) if isinstance(metadata, dict) else []
            handle_records.append(
                {
                    "handle": handle,
                    "canonical_name": identity.get("canonical_name"),
                    "canonical_uri": identity.get("canonical_uri"),
                    "api_status": identity.get("api_status"),
                    "object_class": identity.get("object_class"),
                    "incoming_relation_types": graph.get("incoming_relation_types", {}),
                    "outgoing_relation_types": graph.get("outgoing_relation_types", {}),
                    "coverage_v2": coverage,
                    "definitions": [
                        compact_record(row, ("exact_text", "exact_source_text", "definition_text", "normalized_text"))
                        for row in definitions[:50]
                        if isinstance(row, dict)
                    ],
                    "equations": [
                        compact_record(row, ("exact_math_text", "equation_text", "normalized_latex"))
                        for row in equations[:50]
                        if isinstance(row, dict)
                    ],
                    "native_report": {
                        "path": str(path.relative_to(ROOT)),
                        "sha256": sha256(path),
                        "bytes": path.stat().st_size,
                        "reused_master_query": bool(result.get("reused_master_query")),
                    },
                }
            )
        chapters.append(
            {
                "chapter_id": chapter_id,
                "title": chapter["title"],
                "assigned_handle_count": len(chapter["handles"]),
                "handles": handle_records,
            }
        )

    payload = {
        "schema": "mk-ultra-tome-native-evidence-digest-v1",
        "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
        "database_sha256": receipt["database_sha256_after"],
        "database_unchanged": receipt["database_unchanged"],
        "chapter_ids": args.chapter_ids,
        "query_receipt": str(receipt_path.relative_to(ROOT)),
        "chapters": chapters,
    }
    out = WORKSPACE / f"native_evidence_digest_{batch_slug}.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(out), "chapters": args.chapter_ids, "handles": sum(c["assigned_handle_count"] for c in chapters), "sha256": sha256(out)}))


if __name__ == "__main__":
    main()
