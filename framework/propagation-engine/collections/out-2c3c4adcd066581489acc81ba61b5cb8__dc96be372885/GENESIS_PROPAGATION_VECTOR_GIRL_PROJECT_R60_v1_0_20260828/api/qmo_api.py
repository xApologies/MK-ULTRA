#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"R60_PROPAGATION_VECTOR.sqlite"
def cx():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def rows(q): return [dict(r) for r in q.fetchall()]
class H(BaseHTTPRequestHandler):
    def out(self,x):
        b=json.dumps(x,indent=2).encode()
        self.send_response(200); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p=urllib.parse.urlparse(self.path).path; c=cx()
        try:
            if p=="/": return self.out({"run":"R60","status":"STRONG_CANDIDATE_CLOSURE","next":"@qmo/propagation_morphism_vector_bridge"})
            if p=="/qmos": return self.out(rows(c.execute("select * from qmos")))
            if p=="/theorems": return self.out(rows(c.execute("select * from theorems")))
            if p=="/firewalls": return self.out(rows(c.execute("select * from firewalls")))
            if p=="/next": return self.out(rows(c.execute("select * from next_steps")))
            return self.out({"error":"not found"})
        finally: c.close()
if __name__=="__main__":
    ThreadingHTTPServer(("127.0.0.1",8796),H).serve_forever()
