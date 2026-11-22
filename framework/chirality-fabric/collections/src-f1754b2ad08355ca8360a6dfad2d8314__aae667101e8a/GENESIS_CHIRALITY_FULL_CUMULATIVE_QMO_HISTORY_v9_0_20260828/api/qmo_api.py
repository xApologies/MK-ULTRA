#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer

DB=Path(__file__).resolve().parent.parent/"database"/"GENESIS_CHIRALITY_FULL_CUMULATIVE_v9.sqlite"

def cx():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def rows(q): return [dict(r) for r in q.fetchall()]

class H(BaseHTTPRequestHandler):
    def out(self,x,code=200):
        b=json.dumps(x,indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b)))
        self.end_headers()
        self.wfile.write(b)
    def do_GET(self):
        p=urllib.parse.urlparse(self.path).path
        c=cx()
        try:
            if p=="/":
                return self.out({
                    "name":"GENESIS Chirality Full Cumulative QMO API",
                    "version":"9.0",
                    "status":"SEALED_FOR_TANGENT",
                    "routes":["/qmos","/edges","/chronology","/debt","/collaboration","/resume","/json"]
                })
            if p=="/qmos": return self.out(rows(c.execute("select * from qmos order by address")))
            if p=="/edges": return self.out(rows(c.execute("select * from edges order by address")))
            if p=="/chronology": return self.out(rows(c.execute("select * from chronology order by seq")))
            if p=="/debt": return self.out(rows(c.execute("select * from open_debt order by priority")))
            if p=="/collaboration": return self.out(rows(c.execute("select * from collaboration")))
            if p=="/resume": return self.out(rows(c.execute("select * from resume_points")))
            if p=="/json": return self.out(rows(c.execute("select * from json_registry order by address")))
            return self.out({"error":"not found"},404)
        finally:
            c.close()

if __name__=="__main__":
    ThreadingHTTPServer(("127.0.0.1",8795),H).serve_forever()
