"""Rebuild the complete active GR/QMO SQLite registry.

The builder consumes the repaired GR/QMO dependency index, never the historical
API 4.3 index. It preserves the complete handle population and attaches the
declared conditions to every integration dependency record.
"""

from pathlib import Path
import argparse
import hashlib
import json
import re
import sqlite3


ROOT = Path(__file__).resolve().parents[1]
API = ROOT / "api" / "GR_QMO_API_FULL_CURRENT"
CANONICAL = API / "GR_QMO_API_CURRENT_CANONICAL.md"
INDEX = API / "GR_QMO_DEPENDENCY_INDEX.json"


def build(output: Path) -> dict:
    if output.exists():
        raise FileExistsError("Choose a new output path; existing databases are not overwritten")

    index = json.loads(INDEX.read_text())
    objects = json.loads((ROOT / "registry" / "INTEGRATION_OBJECTS.json").read_text())
    dependencies = json.loads(
        (ROOT / "registry" / "INTEGRATION_DEPENDENCIES.json").read_text()
    )["edges"]
    checkpoints = json.loads((ROOT / "registry" / "CHECKPOINTS.json").read_text())
    base = set(index["handles"])
    new = {row["handle"] for row in objects}
    if base & new:
        raise ValueError("Integration records collide with inherited handles")
    universe = base | new
    for edge in dependencies:
        if edge["source"] not in universe or edge["target"] not in universe:
            raise ValueError("Unresolved integration dependency: " + repr(edge))
        if not edge.get("conditions"):
            raise ValueError("Integration dependency lacks exposed conditions: " + repr(edge))

    output.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(output)
    connection.executescript(
        """
        CREATE TABLE objects(
          handle TEXT PRIMARY KEY,
          kind TEXT,
          title TEXT,
          status TEXT,
          equation TEXT,
          source TEXT,
          hypotheses TEXT
        );
        CREATE TABLE edges(
          id INTEGER PRIMARY KEY,
          source TEXT,
          relation TEXT,
          target TEXT,
          origin TEXT,
          metadata TEXT
        );
        CREATE INDEX edges_source ON edges(source);
        CREATE INDEX edges_target ON edges(target);
        CREATE INDEX edges_typed ON edges(source, relation, target);
        CREATE TABLE occurrences(handle TEXT, source TEXT, line INTEGER);
        CREATE INDEX occurrences_handle ON occurrences(handle);
        CREATE TABLE checkpoints(
          id TEXT PRIMARY KEY,
          activation TEXT,
          scope TEXT,
          archive TEXT,
          sha256 TEXT
        );
        CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT);
        """
    )

    canonical_path = "api/GR_QMO_API_FULL_CURRENT/GR_QMO_API_CURRENT_CANONICAL.md"
    for handle in sorted(base):
        connection.execute(
            "INSERT INTO objects VALUES(?,?,?,?,?,?,?)",
            (
                handle,
                "inherited_handle",
                handle,
                "preserved_in_full_gr_qmo",
                None,
                canonical_path,
                "[]",
            ),
        )
    for row in objects:
        connection.execute(
            "INSERT INTO objects VALUES(?,?,?,?,?,?,?)",
            (
                row["handle"],
                row.get("kind", "integration_object"),
                row["title"],
                row["status"],
                row["equation"],
                row["source"],
                json.dumps(row["hypotheses"], ensure_ascii=False),
            ),
        )

    for edge in index["edge_records"]:
        connection.execute(
            "INSERT INTO edges(source,relation,target,origin,metadata) VALUES(?,?,?,?,?)",
            (
                edge["source"],
                edge["relation"],
                edge["target"],
                "GR_QMO_ACTIVE_GRAPH",
                json.dumps(edge, ensure_ascii=False),
            ),
        )
    for edge in dependencies:
        connection.execute(
            "INSERT INTO edges(source,relation,target,origin,metadata) VALUES(?,?,?,?,?)",
            (
                edge["source"],
                edge["relation"],
                edge["target"],
                "GR_QMO_INTEGRATION",
                json.dumps(
                    {
                        "scope": edge["scope"],
                        "conditions": edge["conditions"],
                        "source_record": edge["source_record"],
                    },
                    ensure_ascii=False,
                ),
            ),
        )

    for line_number, line in enumerate(CANONICAL.read_text().splitlines(), 1):
        for handle in sorted(set(re.findall(r"@[A-Za-z0-9_]+", line)) & base):
            connection.execute(
                "INSERT INTO occurrences VALUES(?,?,?)",
                (handle, canonical_path, line_number),
            )
    for row in checkpoints:
        connection.execute(
            "INSERT INTO checkpoints VALUES(?,?,?,?,?)",
            (row["id"], row["activation"], row["scope"], row["archive"], row["sha256"]),
        )

    imported = sum(row.get("kind") == "imported_source_object" for row in objects)
    metadata = {
        "version": "1.0.0",
        "active_api": "GR_QMO",
        "canonical_sha256": hashlib.sha256(CANONICAL.read_bytes()).hexdigest(),
        "native_handles": len(base),
        "integration_handles": len(objects) - imported,
        "imported_source_handles": imported,
        "object_count": len(base) + len(objects),
        "active_parent_edges": len(index["edge_records"]),
        "integration_edges": len(dependencies),
        "active_edge_count": len(index["edge_records"]) + len(dependencies),
        "unchanged_parent_edge_records": 75419,
        "corrected_parent_edge_records": 2,
        "retired_parent_edge_records": 3,
        "legacy_api_4_3_graph_loaded": False,
        "database_role": "complete active GR/QMO query object",
    }
    for key, value in metadata.items():
        connection.execute("INSERT INTO meta VALUES(?,?)", (key, json.dumps(value)))
    connection.commit()

    if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        raise RuntimeError("SQLite integrity check failed")
    dangling = connection.execute(
        """
        SELECT COUNT(*)
        FROM edges e
        LEFT JOIN objects a ON a.handle=e.source
        LEFT JOIN objects b ON b.handle=e.target
        WHERE a.handle IS NULL OR b.handle IS NULL
        """
    ).fetchone()[0]
    if dangling:
        raise RuntimeError(f"Registry contains {dangling} dangling edge endpoints")
    actual = connection.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    if actual != 75457:
        raise RuntimeError(f"Expected 75,457 active edges; found {actual}")
    connection.close()
    return metadata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "reruns" / "GR_QMO.sqlite",
    )
    args = parser.parse_args()
    print(json.dumps(build(args.output), indent=2))
