#!/usr/bin/env python3
import sqlite3,json
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"R59_PROVISIONAL_CLOSURE.sqlite"
def cx():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def rows(q): return [dict(r) for r in q.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x):
  b=json.dumps(x,indent=2).encode()
  self.send_response(200);self.send_header("Content-Type","application/json")
  self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  c=cx()
  try:
   if self.path=="/": return self.out({"status":"SEALED_FOR_TANGENT","scope":"T0-T5","routes":["/locks","/debt","/resume"]})
   if self.path=="/locks": return self.out(rows(c.execute("select * from locked_results")))
   if self.path=="/debt": return self.out(rows(c.execute("select * from open_debt order by priority")))
   if self.path=="/resume": return self.out(rows(c.execute("select * from resume_points")))
   return self.out({"error":"not found"})
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8794),H).serve_forever()
