#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"PROPAGATION_GIRL_PROJECT_v3.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(q):return [dict(r) for r in q.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x,code=200):
  b=json.dumps(x,indent=2).encode();self.send_response(code);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"version":"3.0","status":"CLOSED_THROUGH_R68_TO_ROADBLOCK","current_qmo":"@qmo/canonical_closed_fractal_profile_match"})
   if p=="/qmos":return self.out(rr(c.execute("select * from qmos")))
   if p=="/results":return self.out(rr(c.execute("select * from results")))
   if p=="/roadblocks":return self.out(rr(c.execute("select * from roadblocks")))
   if p=="/runs":return self.out(rr(c.execute("select * from run_receipts")))
   if p=="/sources":return self.out(rr(c.execute("select * from source_receipts")))
   return self.out({"error":"not found"},404)
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8804),H).serve_forever()
