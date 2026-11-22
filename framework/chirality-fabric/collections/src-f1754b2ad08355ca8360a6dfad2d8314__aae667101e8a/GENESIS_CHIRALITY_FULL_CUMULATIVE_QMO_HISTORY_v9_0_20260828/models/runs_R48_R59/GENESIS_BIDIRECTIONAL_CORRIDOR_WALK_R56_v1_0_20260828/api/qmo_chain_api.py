#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"R56_BIDIRECTIONAL_CORRIDOR.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(x):return [dict(r) for r in x.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x):
  b=json.dumps(x,indent=2).encode();self.send_response(200);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"tool":"@qmo/bidirectional_corridor_walk","next":"@qmo/hidden_carrier_binding_corridor_join","state":"TOOL_CLOSURE"})
   if p=="/operators":return self.out(rr(c.execute("select * from operators")))
   if p=="/stats":return self.out(rr(c.execute("select * from corridor_stats")))
   if p=="/members":return self.out(rr(c.execute("select * from corridor_members order by target,forward_depth,backward_depth")))
   return self.out({"error":"not found"})
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8792),H).serve_forever()
