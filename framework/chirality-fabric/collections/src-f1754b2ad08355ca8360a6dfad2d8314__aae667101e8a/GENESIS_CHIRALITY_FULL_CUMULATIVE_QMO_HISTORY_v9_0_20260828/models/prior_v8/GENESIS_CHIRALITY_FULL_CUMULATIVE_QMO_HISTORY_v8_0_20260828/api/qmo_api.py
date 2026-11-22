#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"GENESIS_CHIRALITY_FULL_CUMULATIVE_v8.sqlite"
def cx():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def rows(cur): return [dict(r) for r in cur.fetchall()]
class H(BaseHTTPRequestHandler):
    def out(self,x,code=200):
        b=json.dumps(x,indent=2).encode()
        self.send_response(code); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p=urllib.parse.urlparse(self.path).path; c=cx()
        try:
            if p=="/":
                return self.out({"name":"Genesis Chirality Full Cumulative QMO API","version":"8.0","resume":"@open/portal_to_hidden_edge","routes":["/qmos","/edges","/chronology","/sources","/runs","/open","/resume"]})
            if p=="/qmos": return self.out(rows(c.execute("select * from qmos order by address")))
            if p=="/edges": return self.out(rows(c.execute("select * from edges order by address")))
            if p=="/chronology": return self.out(rows(c.execute("select * from chronology order by seq")))
            if p=="/sources": return self.out(rows(c.execute("select * from source_archives order by address")))
            if p=="/runs": return self.out(rows(c.execute("select * from run_packages order by address")))
            if p=="/open": return self.out(rows(c.execute("select * from open_debt order by priority")))
            if p=="/resume":
                q=rows(c.execute("select * from qmos where address='@open/portal_to_hidden_edge'"))
                deps=rows(c.execute("select * from edges where source='@open/portal_to_hidden_edge' or target='@open/portal_to_hidden_edge'"))
                return self.out({"qmo":q,"dependencies":deps})
            return self.out({"error":"not found"},404)
        finally: c.close()
if __name__=="__main__":
    ThreadingHTTPServer(("127.0.0.1",8783),H).serve_forever()
