#!/usr/bin/env python3
import sqlite3, json, urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DB = Path(__file__).resolve().parent.parent / "database" / "GENESIS_PROPAGATION_GIRL_PROJECT_QMO.sqlite"

def cx():
    c=sqlite3.connect(DB)
    c.row_factory=sqlite3.Row
    return c

def rows(q):
    return [dict(r) for r in q.fetchall()]

TABLES = {
    "metadata":"metadata",
    "qmos":"qmos",
    "theorems":"theorems",
    "sources":"sources",
    "runs":"runs",
    "artifacts":"artifacts",
}

class H(BaseHTTPRequestHandler):
    def sendj(self,obj,code=200):
        b=json.dumps(obj,indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        path=urllib.parse.unquote(urllib.parse.urlparse(self.path).path)
        c=cx()
        try:
            if path=="/":
                return self.sendj({
                    "name":"GENESIS Propagation Girl Project QMO API",
                    "checkpoint":"R61",
                    "status":"STRONG_CANDIDATE_SOLUTION__HANDOFF_READY",
                    "resume":"@qmo/propagation_morphism_vector_bridge",
                    "central_result":"Relationship propagates first. Motion is a resolved description of that propagation.",
                    "routes":[r["route"] for r in rows(c.execute("SELECT route FROM api_routes ORDER BY route"))]
                })
            static = {
                "/metadata":"SELECT * FROM metadata ORDER BY address",
                "/qmos":"SELECT * FROM qmos ORDER BY address",
                "/edges":"SELECT * FROM edges ORDER BY id",
                "/theorems":"SELECT * FROM theorems ORDER BY address",
                "/sources":"SELECT * FROM sources ORDER BY address",
                "/runs":"SELECT * FROM runs ORDER BY address",
                "/artifacts":"SELECT * FROM artifacts ORDER BY address",
                "/json":"SELECT * FROM json_docs ORDER BY address",
                "/collaboration":"SELECT * FROM collaboration ORDER BY role",
                "/aliases":"SELECT * FROM aliases ORDER BY alias",
            }
            if path in static:
                return self.sendj(rows(c.execute(static[path])))
            if path.startswith("/address/"):
                addr=path[len("/address/"):]
                # Resolve aliases first.
                a=c.execute("SELECT * FROM aliases WHERE alias=?",(addr,)).fetchone()
                if a:
                    addr=a["address"]
                for table in ["qmos","theorems","metadata","sources","runs","artifacts","json_docs"]:
                    col="address"
                    r=c.execute(f"SELECT * FROM {table} WHERE {col}=?",(addr,)).fetchone()
                    if r:
                        return self.sendj({"table":table,"record":dict(r)})
                return self.sendj({"error":"address not found","address":addr},404)
            return self.sendj({"error":"not found","path":path},404)
        finally:
            c.close()

if __name__=="__main__":
    ThreadingHTTPServer(("127.0.0.1",8797),H).serve_forever()
