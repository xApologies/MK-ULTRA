#!/usr/bin/env python3
"""
Rebuild QMO.sqlite from JSON registries.
Run from the API package directory.
"""
from pathlib import Path
import json, sqlite3

root=Path(__file__).parent
objects=json.loads((root/"QMO_OBJECT_REGISTRY.json").read_text())["objects"]
edges=json.loads((root/"QMO_EDGE_REGISTRY.json").read_text())["edge_records"]
equations=json.loads((root/"QMO_EQUATION_REGISTRY.json").read_text())["equations"]
ledger=json.loads((root/"QMO_LEDGER_REGISTRY.json").read_text())["entries"]

db=root/"QMO.sqlite"
if db.exists(): db.unlink()
con=sqlite3.connect(db); cur=con.cursor()
cur.executescript("""
CREATE TABLE objects(handle TEXT PRIMARY KEY, canonical_handle TEXT, status TEXT, type TEXT, definition TEXT, provenance_json TEXT);
CREATE TABLE edges(edge_id TEXT PRIMARY KEY, source TEXT, relation TEXT, target TEXT, graph_family TEXT, confidence TEXT, audit_status TEXT, provenance TEXT);
CREATE INDEX idx_edges_source ON edges(source);
CREATE INDEX idx_edges_target ON edges(target);
CREATE INDEX idx_edges_relation ON edges(relation);
CREATE TABLE equations(equation_handle TEXT PRIMARY KEY, kind TEXT, expression_text TEXT, status TEXT, symbols_json TEXT, provenance_json TEXT);
CREATE TABLE ledger(ledger_id TEXT PRIMARY KEY, status TEXT, summary TEXT, body_markdown TEXT, provenance TEXT);
CREATE VIRTUAL TABLE search_fts USING fts5(handle,text);
""")
for o in objects:
    cur.execute("INSERT INTO objects VALUES(?,?,?,?,?,?)",(o["model_handle"],o["canonical_handle"],o["status"],o["type"],o["definition"],json.dumps(o["provenance"])))
    cur.execute("INSERT INTO search_fts VALUES(?,?)",(o["model_handle"],f'{o["type"]} {o["definition"]} {o["status"]}'))
for e in edges:
    cur.execute("INSERT INTO edges VALUES(?,?,?,?,?,?,?,?)",(e["edge_id"],e["source"],e["relation"],e["target"],e["graph_family"],e["confidence"],e["audit_status"],e["provenance"]))
for q in equations:
    cur.execute("INSERT INTO equations VALUES(?,?,?,?,?,?)",(q["equation_handle"],q["kind"],q["expression_text"],q["status"],json.dumps(q["symbols"]),json.dumps(q["provenance"])))
    cur.execute("INSERT INTO search_fts VALUES(?,?)",(q["equation_handle"],f'{q["kind"]} {q["expression_text"]} {q["status"]}'))
for l in ledger:
    cur.execute("INSERT INTO ledger VALUES(?,?,?,?,?)",(l["ledger_id"],l["status"],l["summary"],l["body_markdown"],l["provenance"]))
    cur.execute("INSERT INTO search_fts VALUES(?,?)",(l["ledger_id"],f'{l["status"]} {l["summary"]} {l["body_markdown"][:4000]}'))
con.commit(); con.close()
print("rebuilt",db)
