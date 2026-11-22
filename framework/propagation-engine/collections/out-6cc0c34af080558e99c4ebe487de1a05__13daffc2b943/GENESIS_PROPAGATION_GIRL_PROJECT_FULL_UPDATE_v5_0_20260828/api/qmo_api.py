#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"PROPAGATION_GIRL_PROJECT_v5.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(q):return [dict(r) for r in q.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x,code=200):
  b=json.dumps(x,indent=2).encode();self.send_response(code);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"version":"5.0","status":"CLOSED_THROUGH_R73_MAJOR_PROPAGATION_ENGINE_CLOSURE","next":"@qmo/closed_fractal_engine_family_instantiation"})
   if p=="/qmos":return self.out(rr(c.execute("select * from qmos")))
   if p=="/results":return self.out(rr(c.execute("select * from results")))
   if p=="/runs":return self.out(rr(c.execute("select * from run_receipts")))
   return self.out({"error":"not found"},404)
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8806),H).serve_forever()
