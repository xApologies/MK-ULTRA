#!/usr/bin/env python3
import json, sqlite3, urllib.parse, re
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DB=Path(__file__).resolve().parent.parent/"database"/"thread_continuity_qmo.sqlite"
HOST="127.0.0.1"; PORT=8766

def cx():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def rows(c): return [dict(r) for r in c.fetchall()]
def resolve(con,s):
    s=urllib.parse.unquote(s)
    if not s.startswith("@"):
        r=con.execute("SELECT qmo_address FROM aliases WHERE alias=?",(s,)).fetchone()
        if r: return r["qmo_address"]
        s="@"+s
    return s

class H(BaseHTTPRequestHandler):
    def sendj(self,obj,status=200):
        b=json.dumps(obj,ensure_ascii=False,indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Length",str(len(b)))
        self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        u=urllib.parse.urlparse(self.path); p=u.path; q=urllib.parse.parse_qs(u.query); con=cx()
        try:
            if p=="/":
                return self.sendj({
                    "name":"Cradle/SU2/SU3 Thread Continuity QMO API",
                    "metadata":{r["key"]:r["value"] for r in con.execute("SELECT key,value FROM metadata")},
                    "routes":rows(con.execute("SELECT method,route,description FROM api_routes ORDER BY route"))
                })
            if p=="/health": return self.sendj({"ok":True,"database":str(DB)})
            if p=="/metadata": return self.sendj(rows(con.execute("SELECT * FROM metadata ORDER BY key")))
            if p=="/qmo":
                sql="SELECT * FROM qmo_objects WHERE 1=1"; args=[]
                if q.get("type"): sql+=" AND type=?"; args.append(q["type"][0])
                if q.get("status"): sql+=" AND status=?"; args.append(q["status"][0])
                if q.get("q"):
                    t="%"+q["q"][0]+"%"; sql+=" AND (name LIKE ? OR definition LIKE ? OR payload_json LIKE ?)"; args += [t,t,t]
                return self.sendj(rows(con.execute(sql+" ORDER BY qmo_address",args)))
            m=re.fullmatch(r"/qmo/(.+)/relations",p)
            if m:
                a=resolve(con,m.group(1))
                return self.sendj({
                    "qmo_address":a,
                    "outgoing":rows(con.execute("SELECT * FROM qmo_relations WHERE source_qmo=?",(a,))),
                    "incoming":rows(con.execute("SELECT * FROM qmo_relations WHERE target_qmo=?",(a,)))
                })
            m=re.fullmatch(r"/qmo/(.+)",p)
            if m:
                a=resolve(con,m.group(1))
                r=con.execute("SELECT * FROM qmo_objects WHERE qmo_address=?",(a,)).fetchone()
                if not r: return self.sendj({"error":"not found","qmo_address":a},404)
                o=dict(r)
                try:o["payload"]=json.loads(o.pop("payload_json"))
                except Exception:pass
                return self.sendj(o)
            if p=="/equations": return self.sendj(rows(con.execute("SELECT * FROM equations ORDER BY qmo_address")))
            if p=="/theorems": return self.sendj(rows(con.execute("SELECT * FROM theorems ORDER BY qmo_address")))
            if p=="/hypotheses": return self.sendj(rows(con.execute("SELECT * FROM hypotheses ORDER BY qmo_address")))
            if p=="/open": return self.sendj(rows(con.execute("SELECT * FROM open_questions ORDER BY priority,qmo_address")))
            if p=="/chronology": return self.sendj(rows(con.execute("SELECT * FROM chronology ORDER BY sequence_no")))
            if p=="/sources": return self.sendj(rows(con.execute("SELECT * FROM sources ORDER BY qmo_address")))
            if p=="/supersession": return self.sendj(rows(con.execute("SELECT * FROM supersession ORDER BY qmo_address")))
            if p=="/artifacts": return self.sendj(rows(con.execute("SELECT * FROM artifacts ORDER BY qmo_address")))
            if p=="/search":
                term="%"+(q.get("q") or [""])[0]+"%"
                return self.sendj({
                    "qmo":rows(con.execute("SELECT qmo_address,name,type,status,definition FROM qmo_objects WHERE name LIKE ? OR definition LIKE ? OR payload_json LIKE ?",(term,term,term))),
                    "equations":rows(con.execute("SELECT qmo_address,name,expression,status FROM equations WHERE name LIKE ? OR expression LIKE ? OR interpretation LIKE ?",(term,term,term))),
                    "theorems":rows(con.execute("SELECT qmo_address,name,statement,status FROM theorems WHERE name LIKE ? OR statement LIKE ? OR proof_note LIKE ?",(term,term,term))),
                    "open":rows(con.execute("SELECT qmo_address,question,status FROM open_questions WHERE question LIKE ? OR notes LIKE ?",(term,term)))
                })
            return self.sendj({"error":"unknown route","path":p},404)
        finally: con.close()

if __name__=="__main__":
    print(f"QMO API listening on http://{HOST}:{PORT}")
    ThreadingHTTPServer((HOST,PORT),H).serve_forever()
