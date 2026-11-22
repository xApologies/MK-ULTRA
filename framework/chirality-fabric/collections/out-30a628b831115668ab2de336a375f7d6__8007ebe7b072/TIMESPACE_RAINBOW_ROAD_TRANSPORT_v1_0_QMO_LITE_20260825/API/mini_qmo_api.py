#!/usr/bin/env python3
"""QMO-Lite recovery API for the Time-Space Rainbow Road package.

Commands:
  resolve <alias-or-uri>
  recover <alias-or-uri>
  neighbors <alias-or-uri>
  search <fts-query>
  roadmap
  open
"""
import sqlite3,sys,json
from pathlib import Path
DB=Path(__file__).resolve().parents[1]/"DATABASE"/"transport.sqlite3"

def conn():
    c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c

def resolve_row(c,key):
    r=c.execute("SELECT * FROM qmo_addresses WHERE uri=? OR qmo_id=?",(key,key)).fetchone()
    if r:return r
    r=c.execute("""SELECT q.* FROM qmo_aliases a JOIN qmo_addresses q ON q.qmo_id=a.qmo_id
                   WHERE lower(a.alias)=lower(?) LIMIT 1""",(key,)).fetchone()
    if r:return r
    return c.execute("SELECT * FROM qmo_addresses WHERE lower(canonical_name)=lower(?) LIMIT 1",(key,)).fetchone()

def resolve(key):
    c=conn();r=resolve_row(c,key);print(json.dumps(dict(r) if r else {"error":"not_found","query":key},indent=2));c.close()

def neighbors(key):
    c=conn();q=resolve_row(c,key)
    if not q:
        print(json.dumps({"error":"not_found","query":key},indent=2));return
    rows=c.execute("""SELECT e.edge_id,s.uri source_uri,s.canonical_name source_name,e.relation,
                     t.uri target_uri,t.canonical_name target_name,e.status
                     FROM qmo_edges e
                     JOIN qmo_addresses s ON s.qmo_id=e.source_qmo_id
                     JOIN qmo_addresses t ON t.qmo_id=e.target_qmo_id
                     WHERE e.source_qmo_id=? OR e.target_qmo_id=? ORDER BY e.edge_id""",
                   (q["qmo_id"],q["qmo_id"])).fetchall()
    print(json.dumps([dict(r) for r in rows],indent=2));c.close()

def recover(key):
    c=conn();q=resolve_row(c,key)
    if not q:
        print(json.dumps({"error":"not_found","query":key},indent=2));return
    out={"qmo":dict(q)}
    if q["object_id"]:
        r=c.execute("SELECT * FROM objects WHERE id=?",(q["object_id"],)).fetchone()
        out["object"]=dict(r) if r else None
    out["aliases"]=[r["alias"] for r in c.execute("SELECT alias FROM qmo_aliases WHERE qmo_id=?",(q["qmo_id"],))]
    out["neighbors"]=[dict(r) for r in c.execute("""SELECT e.edge_id,s.uri source_uri,e.relation,t.uri target_uri,e.status
        FROM qmo_edges e JOIN qmo_addresses s ON s.qmo_id=e.source_qmo_id
        JOIN qmo_addresses t ON t.qmo_id=e.target_qmo_id
        WHERE e.source_qmo_id=? OR e.target_qmo_id=?""",(q["qmo_id"],q["qmo_id"]))]
    eqs=[];ths=[];oqs=[]
    for b in c.execute("SELECT * FROM qmo_bindings WHERE qmo_id=? ORDER BY binding_id",(q["qmo_id"],)):
        if b["binding_type"]=="equation":
            r=c.execute("SELECT * FROM equations WHERE id=?",(b["binding_key"],)).fetchone()
            if r:eqs.append(dict(r))
        elif b["binding_type"]=="theorem":
            r=c.execute("SELECT * FROM theorems WHERE id=?",(b["binding_key"],)).fetchone()
            if r:ths.append(dict(r))
        elif b["binding_type"]=="open_question":
            r=c.execute("SELECT * FROM open_questions WHERE id=?",(b["binding_key"],)).fetchone()
            if r:oqs.append(dict(r))
    out["equations"]=eqs;out["theorems"]=ths;out["open_questions"]=oqs
    print(json.dumps(out,indent=2));c.close()

def search(q):
    c=conn()
    rows=c.execute("SELECT kind,key,title,body,tags FROM search_fts WHERE search_fts MATCH ? LIMIT 30",(q,)).fetchall()
    print(json.dumps([dict(r) for r in rows],indent=2));c.close()

def roadmap():
    c=conn()
    rows=c.execute("SELECT * FROM roadmap_steps ORDER BY ordinal").fetchall()
    print(json.dumps([dict(r) for r in rows],indent=2));c.close()

def openq():
    c=conn()
    rows=c.execute("SELECT * FROM open_questions ORDER BY id").fetchall()
    print(json.dumps([dict(r) for r in rows],indent=2));c.close()

if __name__=="__main__":
    if len(sys.argv)<2:
        print(__doc__);raise SystemExit(2)
    cmd=sys.argv[1].lower()
    if cmd=="resolve" and len(sys.argv)>2:resolve(" ".join(sys.argv[2:]))
    elif cmd=="recover" and len(sys.argv)>2:recover(" ".join(sys.argv[2:]))
    elif cmd=="neighbors" and len(sys.argv)>2:neighbors(" ".join(sys.argv[2:]))
    elif cmd=="search" and len(sys.argv)>2:search(" ".join(sys.argv[2:]))
    elif cmd=="roadmap":roadmap()
    elif cmd=="open":openq()
    else:
        print(__doc__);raise SystemExit(2)
