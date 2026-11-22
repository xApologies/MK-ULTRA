#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer

DB=Path(__file__).resolve().parent.parent/"database"/"PROPAGATION_GIRL_PROJECT_QMO.sqlite"

def cx():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def rr(q): return [dict(r) for r in q.fetchall()]

class H(BaseHTTPRequestHandler):
    def out(self,x,code=200):
        b=json.dumps(x,indent=2).encode()
        self.send_response(code); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        p=urllib.parse.unquote(urllib.parse.urlparse(self.path).path)
        c=cx()
        try:
            if p=="/":
                return self.out({
                    "name":"GENESIS Propagation Girl Project QMO API",
                    "version":"2.0",
                    "scope":"unbounded-environment-forward-only",
                    "status":"NOTEBOOK_CONTINUITY_READY",
                    "central_result":"Relationship propagates first. Motion is a resolved description of that propagation.",
                    "resume":"@qmo/shared_relational_resolution_transport"
                })
            static={
                "/metadata":"select * from metadata order by address",
                "/qmos":"select * from qmos order by address",
                "/edges":"select * from edges order by id",
                "/results":"select * from results order by address",
                "/sources":"select * from sources order by address",
                "/runs":"select * from runs order by address",
                "/artifacts":"select * from artifacts order by address",
                "/json":"select * from json_docs order by address",
                "/aliases":"select * from aliases order by alias",
            }
            if p in static: return self.out(rr(c.execute(static[p])))
            if p.startswith("/address/"):
                addr=p[len("/address/"):]
                a=c.execute("select address from aliases where alias=?",(addr,)).fetchone()
                if a: addr=a["address"]
                for table in ["qmos","results","metadata","sources","runs","artifacts","json_docs"]:
                    r=c.execute(f"select * from {table} where address=?",(addr,)).fetchone()
                    if r: return self.out({"table":table,"record":dict(r)})
                return self.out({"error":"address not found","address":addr},404)
            return self.out({"error":"not found","path":p},404)
        finally:
            c.close()

if __name__=="__main__":
    ThreadingHTTPServer(("127.0.0.1",8799),H).serve_forever()
