#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"GENESIS_S2_PREIMAGE_QMO_CHAIN.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rr(c):return [dict(r) for r in c.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x,code=200):
  b=json.dumps(x,indent=2).encode();self.send_response(code);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"landscape":"@dl_s2_preimage_realization","chain":"@dc_s2_preimage_to_connection","terminal":"@chain/connection","state":"OPEN_FORK"})
   if p=="/chain":return self.out(rr(c.execute("SELECT * FROM chain_steps ORDER BY step_no")))
   if p=="/qmos":return self.out(rr(c.execute("SELECT * FROM qmos ORDER BY address")))
   if p=="/sources":return self.out(rr(c.execute("SELECT * FROM source_qmos ORDER BY address")))
   if p=="/roadblocks":return self.out(rr(c.execute("SELECT * FROM roadblocks")))
   return self.out({"error":"not found"},404)
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8773),H).serve_forever()
