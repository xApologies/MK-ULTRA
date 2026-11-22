"""Integrity and graph-boundary verification for the complete GR/QMO release."""

from pathlib import Path
import hashlib
import json
import sqlite3


CORRECT = (
    "@time_shell_projection",
    "REALIZES",
    "@metric_perturbation",
)
CORRECT_INVERSE = (
    "@metric_perturbation",
    "REALIZED_BY",
    "@time_shell_projection",
)
FORBIDDEN = {
    ("@metric_perturbation", "REALIZES", "@time_shell_projection"),
    ("@time_shell_projection", "REALIZED_BY", "@metric_perturbation"),
    ("@graviton", "PROJECTS_TO", "@time_shell_projection"),
    ("@linear_metric_perturbation", "REALIZES", "@time_shell_projection"),
    ("@spin_2_projection", "PROJECTS_TO", "@time_shell_projection"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _manifest_key(value: str) -> str:
    """Normalize representation only; never rename or case-fold a member."""
    value = value.replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return value


def verify(root: Path, *, manifest: bool = True) -> dict:
    root = root.resolve()
    failures = []
    checked = 0
    api = root / "api" / "GR_QMO_API_FULL_CURRENT"
    canonical = api / "GR_QMO_API_CURRENT_CANONICAL.md"
    index_path = api / "GR_QMO_DEPENDENCY_INDEX.json"
    database = root / "registry" / "GR_QMO.sqlite"

    for path in (canonical, index_path, database, root / "registry" / "OMITTED_HISTORICAL_MATERIAL.json"):
        checked += 1
        if not path.is_file():
            failures.append("Missing required file: " + str(path.relative_to(root)))

    index = json.loads(index_path.read_text()) if index_path.is_file() else {}
    parent_edges = {
        (row["source"], row["relation"], row["target"])
        for row in index.get("edge_records", [])
    }
    if len(index.get("handles", [])) != 2384:
        failures.append({"active_handle_count": len(index.get("handles", []))})
    if len(index.get("edge_records", [])) != 75429:
        failures.append({"active_parent_edge_count": len(index.get("edge_records", []))})
    if CORRECT not in parent_edges or CORRECT_INVERSE not in parent_edges:
        failures.append("Corrected Time-Shell direction or reverse lookup is missing")
    leaked = sorted(parent_edges & FORBIDDEN)
    if leaked:
        failures.append({"forbidden_active_parent_edges": leaked})

    dependency_path = root / "registry" / "INTEGRATION_DEPENDENCIES.json"
    dependencies = json.loads(dependency_path.read_text()).get("edges", [])
    if len(dependencies) != 28:
        failures.append({"integration_dependency_count": len(dependencies)})
    if any(not row.get("conditions") for row in dependencies):
        failures.append("One or more integration dependencies lacks conditions")

    source_path = root / "registry" / "SOURCE_FILES.json"
    if source_path.is_file():
        for row in json.loads(source_path.read_text()):
            path = root / row["path"]
            checked += 1
            if not path.is_file() or sha256(path) != row["sha256"]:
                failures.append(row["path"])

    counts = {}
    dangling = None
    database_edges = set()
    if database.is_file():
        connection = sqlite3.connect(database.as_uri() + "?mode=ro", uri=True)
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            failures.append("SQLite integrity")
        counts = {
            "objects": connection.execute("SELECT COUNT(*) FROM objects").fetchone()[0],
            "edges": connection.execute("SELECT COUNT(*) FROM edges").fetchone()[0],
            "occurrences": connection.execute("SELECT COUNT(*) FROM occurrences").fetchone()[0],
            "checkpoints": connection.execute("SELECT COUNT(*) FROM checkpoints").fetchone()[0],
        }
        dangling = connection.execute(
            """
            SELECT COUNT(*) FROM edges e
            LEFT JOIN objects a ON a.handle=e.source
            LEFT JOIN objects b ON b.handle=e.target
            WHERE a.handle IS NULL OR b.handle IS NULL
            """
        ).fetchone()[0]
        database_edges = set(
            connection.execute("SELECT source,relation,target FROM edges")
        )
        metadata = {
            key: json.loads(value)
            for key, value in connection.execute("SELECT key,value FROM meta")
        }
        connection.close()
        if counts["objects"] != 2397 or counts["edges"] != 75457:
            failures.append({"database_counts": counts})
        if dangling:
            failures.append({"dangling_dependencies": dangling})
        if database_edges & FORBIDDEN:
            failures.append({"forbidden_database_edges": sorted(database_edges & FORBIDDEN)})
        if CORRECT not in database_edges or CORRECT_INVERSE not in database_edges:
            failures.append("Corrected Time-Shell records are absent from SQLite")
        if metadata.get("legacy_api_4_3_graph_loaded") is not False:
            failures.append("Database does not declare the legacy graph inactive")

    legacy_names = {
        "MK43_Ultra_API_CURRENT_CANONICAL.md",
        "MK43_Ultra_API_INTEGRATED_WITH_GENESIS_GR.md",
        "RP42_DEPENDENCY_INDEX.json",
    }
    present = sorted(name for name in legacy_names if (api / name).exists())
    if present:
        failures.append({"legacy_files_on_active_api_path": present})

    if manifest:
        manifest_path = root / "MANIFEST.json"
        spec = json.loads(manifest_path.read_text())
        expected = set()
        for row in spec["files"]:
            expected.add(_manifest_key(row["path"]))
            path = root / row["path"]
            checked += 1
            if not path.is_file() or sha256(path) != row["sha256"]:
                failures.append(row["path"])
        actual = {
            _manifest_key(path.relative_to(root).as_posix())
            for path in root.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and "reruns" not in path.relative_to(root).parts
            and path.name != "MANIFEST.json"
            and not path.name.endswith(".pyc")
        }
        if actual != expected:
            failures.append(
                {
                    "unlisted": sorted(actual - expected),
                    "missing": sorted(expected - actual),
                }
            )

    return {
        "ok": not failures,
        "active_api": "GR_QMO",
        "legacy_api_4_3_graph_loaded": False,
        "hashes_checked": checked,
        "database": counts,
        "native_handles": len(index.get("handles", [])),
        "active_parent_edges": len(index.get("edge_records", [])),
        "integration_edges": len(dependencies),
        "unchanged_parent_edge_records": 75419,
        "corrected_parent_edge_records": 2,
        "retired_parent_edge_records": 3,
        "dangling_dependencies": dangling,
        "failures": failures,
        "scope": "complete QMO integrity and active graph boundary",
    }
