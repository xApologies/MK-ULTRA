#!/usr/bin/env python3
import sqlite3,json,re,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"GENESIS_FIELD_RESOLUTION_BANDWIDTH.sqlite"
def cx():
    c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(c):return [dict(x) for x in c.fetchall()]
class H(BaseHTTPRequestHandler):
    def out(self,x,code=200):
        b=json.dumps(x,indent=2).encode();self.send_response(code);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
    def do_GET(self):
        p=urllib.parse.urlparse(self.path).path;c=cx()
        try:
            if p=="/":return self.out({"name":"Genesis Field Resolution Bandwidth QMO API","routes":["/colors","/bandwidths","/resolution","/resolution/R_O","/transitions/R_O","/laws","/open","/closure"]})
            if p=="/colors":return self.out(rr(c.execute("SELECT * FROM colors ORDER BY ordinal")))
            if p=="/bandwidths":return self.out(rr(c.execute("SELECT * FROM bandwidths ORDER BY color_code")))
            if p=="/resolution":return self.out(rr(c.execute("SELECT * FROM resolution_profiles ORDER BY left_color,right_color")))
            m=re.fullmatch(r"/resolution/([ROYGBV])_([ROYGBV])",p)
            if m:return self.out(dict(c.execute("SELECT * FROM resolution_profiles WHERE left_color=? AND right_color=?",m.groups()).fetchone()))
            m=re.fullmatch(r"/transitions/([ROYGBV])_([ROYGBV])",p)
            if m:
                q=f"@resolution/{m.group(1)}_{m.group(2)}"
                return self.out(rr(c.execute("SELECT * FROM structural_transitions WHERE source_profile=? ORDER BY qmo_address",(q,))))
            if p=="/laws":return self.out(rr(c.execute("SELECT * FROM laws ORDER BY qmo_address")))
            if p=="/open":return self.out(rr(c.execute("SELECT * FROM open_debt ORDER BY priority")))
            if p=="/closure":
                return self.out({"profiles":36,"structural_transitions":360,"maximal_structural_graph_strongly_connected":True,"operative_closure":"OPEN: requires basin-specific Bandwidth rule"})
            return self.out({"error":"not found"},404)
        finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8771),H).serve_forever()
