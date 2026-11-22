#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"R52_CANDIDATE_MAP_SIEVE.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(x):return [dict(r) for r in x.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x):
  b=json.dumps(x,indent=2).encode();self.send_response(200);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"terminal":"@open/exhaustive_source_map_certification","state":"POPULATION_METHOD_CLOSED"})
   if p=="/candidates":return self.out(rr(c.execute("select * from candidates order by rank")))
   if p=="/gates":return self.out(rr(c.execute("select * from certification_gates")))
   if p=="/roadblocks":return self.out(rr(c.execute("select * from roadblocks")))
   return self.out({"error":"not found"})
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8788),H).serve_forever()
