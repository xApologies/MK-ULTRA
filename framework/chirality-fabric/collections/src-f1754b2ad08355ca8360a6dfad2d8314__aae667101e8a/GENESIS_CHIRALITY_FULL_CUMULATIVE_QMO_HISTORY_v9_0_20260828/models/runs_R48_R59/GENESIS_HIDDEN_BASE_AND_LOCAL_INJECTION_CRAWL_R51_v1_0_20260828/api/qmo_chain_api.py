#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"R51_HIDDEN_BASE_LOCAL_INJECTION.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(x):return [dict(r) for r in x.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x):
  b=json.dumps(x,indent=2).encode();self.send_response(200);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"terminal":"@open/hidden_base_embedding_definition","branch":"@open/local_candidate_map_sieve_population","state":"SOURCE_DATA_ROADBLOCK"})
   if p=="/qmos":return self.out(rr(c.execute("select * from qmos")))
   if p=="/theorems":return self.out(rr(c.execute("select * from theorems")))
   if p=="/roadblocks":return self.out(rr(c.execute("select * from roadblocks")))
   return self.out({"error":"not found"})
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8787),H).serve_forever()
