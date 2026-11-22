#!/usr/bin/env python3
import sqlite3,json,urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
DB=Path(__file__).resolve().parent.parent/"database"/"GENESIS_CHIRALITY_TORUS_LIVE.sqlite"
def cx():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def rows(c):return [dict(r) for r in c.fetchall()]
class H(BaseHTTPRequestHandler):
 def out(self,x,code=200):
  b=json.dumps(x,indent=2).encode();self.send_response(code);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  p=urllib.parse.urlparse(self.path).path;c=cx()
  try:
   if p=="/":return self.out({"name":"Genesis Chirality Torus Live QMO API","resume":"@open/torus_continuity_crawl","routes":["/qmo","/open","/chronology","/library","/failures"]})
   if p=="/qmo":return self.out(rows(c.execute("SELECT * FROM qmo_objects ORDER BY qmo_address")))
   if p=="/open":return self.out(rows(c.execute("SELECT * FROM open_debt ORDER BY priority")))
   if p=="/chronology":return self.out(rows(c.execute("SELECT * FROM chronology ORDER BY sequence_no")))
   if p=="/library":return self.out(rows(c.execute("SELECT * FROM library ORDER BY qmo_address")))
   if p=="/failures":return self.out(rows(c.execute("SELECT * FROM failures ORDER BY qmo_address")))
   return self.out({"error":"not found"},404)
  finally:c.close()
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8772),H).serve_forever()
