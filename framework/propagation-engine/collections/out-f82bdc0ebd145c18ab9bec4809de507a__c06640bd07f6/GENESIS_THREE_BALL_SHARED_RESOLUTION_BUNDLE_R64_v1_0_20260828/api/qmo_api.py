#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"R64_THREE_BALL_RESOLUTION.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(q):return [dict(r) for r in q.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x,code=200):
  b=json.dumps(x,indent=2).encode();self.send_response(code);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"run":"R64","status":"CLOSED_STRONG_5D_CANDIDATE","chart":"(d12,d23,d31,rho,eta)","next":"@qmo/finite_system_resolution_sheaf_test"})
   if p=="/qmos":return self.out(rr(c.execute("select * from qmos")))
   if p=="/results":return self.out(rr(c.execute("select * from results")))
   if p=="/branches":return self.out(rr(c.execute("select * from branches")))
   if p=="/sources":return self.out(rr(c.execute("select * from source_roles")))
   return self.out({"error":"not found"},404)
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8801),H).serve_forever()
