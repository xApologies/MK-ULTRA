from __future__ import annotations
import sqlite3, json, hashlib
from pathlib import Path
from .models import KnowledgeChunk, KnowledgePackage
from .schema import SCHEMA

class TransductionLibrary:
    version = "0.1.0"
    module_id = "mk43.transduction.library"
    role = "metadata_library"
    domain_ids = ("transduction-math",)

    def __init__(self, db_path):
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def healthcheck(self):
        return self.conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"

    def resolve_handle(self, handle):
        row=self.conn.execute("SELECT handle FROM aliases WHERE alias=?",(handle,)).fetchone()
        if row: return row["handle"]
        row=self.conn.execute("SELECT handle FROM objects WHERE handle=?",(handle,)).fetchone()
        return row["handle"] if row else None

    def export_address(self, handle):
        h=self.resolve_handle(handle)
        if not h:
            return {"handle":handle,"resolved":False,"unresolved_reason":"address_not_found"}
        obj=self.conn.execute("SELECT * FROM objects WHERE handle=?",(h,)).fetchone()
        ver=self.conn.execute("SELECT * FROM versions WHERE handle=? AND version=?",(h,obj["active_version"])).fetchone()
        blocks=[dict(r) for r in self.conn.execute(
            "SELECT content_type,title,body,body_format,ordinal,provenance_json FROM blocks WHERE handle=? AND version=? ORDER BY ordinal",
            (h,obj["active_version"])
        )]
        prov=[json.loads(r["record_json"]) if r["record_json"].startswith(("{","[")) else r["record_json"]
              for r in self.conn.execute("SELECT record_json FROM provenance WHERE handle=? AND version=? ORDER BY ordinal",(h,obj["active_version"]))]
        rels=[dict(r) for r in self.conn.execute("SELECT relation_type,target_handle,model_handle,ordinal,required,metadata_json FROM relations WHERE source_handle=? ORDER BY ordinal",(h,))]
        aliases=[r["alias"] for r in self.conn.execute("SELECT alias FROM aliases WHERE handle=? ORDER BY alias",(h,))]
        return {
            "handle":h,
            "resolved":True,
            "object_type":obj["object_type"],
            "status":obj["status"],
            "active_version":obj["active_version"],
            "package_hash":ver["package_hash"],
            "canonical_math":json.loads(ver["canonical_math_json"]),
            "metadata":json.loads(ver["metadata_json"]),
            "aliases":aliases,
            "content_blocks":blocks,
            "relations":rels,
            "provenance":prov,
        }

    def recover(self, handle, content_types=None):
        a=self.export_address(handle)
        if not a.get("resolved"):
            return KnowledgePackage(handle,handle,unresolved_reason=a.get("unresolved_reason"))
        chunks=[]
        allowed=set(content_types or [])
        for b in a["content_blocks"]:
            if allowed and b["content_type"] not in allowed:
                continue
            chunks.append(KnowledgeChunk(
                b["content_type"], b["title"], b["body"], b["ordinal"],
                provenance=tuple(json.loads(b["provenance_json"]))
            ))
        return KnowledgePackage(a["handle"],a["handle"],chunks,metadata=a["metadata"],package_hash=a["package_hash"])

    def recover_model(self, model_handle):
        m=self.conn.execute("SELECT * FROM models WHERE model_handle=?",(model_handle,)).fetchone()
        if not m: return {"model_handle":model_handle,"resolved":False}
        members=[r["handle"] for r in self.conn.execute(
            "SELECT handle FROM model_membership WHERE model_handle=? ORDER BY ordinal",(model_handle,)
        )]
        return {
            "model_handle":model_handle,
            "resolved":True,
            "root_handle":m["root_handle"],
            "members":[self.export_address(h) for h in members],
            "metadata":json.loads(m["metadata_json"]),
        }

    def pull_qmo(self, ordered_handles):
        recovered=[]
        unresolved=[]
        for h in ordered_handles:
            a=self.export_address(h)
            (recovered if a.get("resolved") else unresolved).append(a)
        order_hash=hashlib.sha256(json.dumps(ordered_handles,separators=(",",":")).encode()).hexdigest()
        return {"recovered":recovered,"unresolved":unresolved,"order_hash":order_hash}

    def search(self, text, limit=50):
        q=f"%{text}%"
        rows=self.conn.execute("""
            SELECT DISTINCT o.handle,o.object_type,o.status
            FROM objects o
            LEFT JOIN versions v ON v.handle=o.handle AND v.version=o.active_version
            LEFT JOIN blocks b ON b.handle=o.handle AND b.version=o.active_version
            WHERE o.handle LIKE ? OR v.metadata_json LIKE ? OR b.body LIKE ?
            ORDER BY o.handle LIMIT ?
        """,(q,q,q,limit)).fetchall()
        return [dict(r) for r in rows]
