#!/usr/bin/env python3
import argparse,json,sqlite3
from pathlib import Path
from collections import deque
DB=Path(__file__).with_name("UNIFIED_QMO.sqlite")

def dictrows(cur):
    cols=[d[0] for d in cur.description]
    return [dict(zip(cols,r)) for r in cur.fetchall()]

def resolve(cur,h):
    cur.execute("SELECT canonical FROM aliases WHERE alias=?",(h,))
    r=cur.fetchone()
    return r[0] if r else h

def edge_allowed(row,mode):
    layer=row["layer"]; rel=row["relation"]; ce=row["closure_eligible"]
    if not ce: return False
    if mode=="navigation": return True
    if mode=="typed": return layer not in ("XAPI_RAW","SOURCE_BACKFILL")
    if mode=="direct":
        if layer in ("XAPI_RAW","SOURCE_BACKFILL"): return False
        if rel=="COMPOSED_DEPENDENCY": return False
        if rel in ("BLACK_HOLE_MODEL_REACHES","BLACK_HOLE_GLOBAL_REACHES","GLOBALLY_FEEDS_BLACK_HOLE"): return False
        return True
    return False

p=argparse.ArgumentParser(description="MK43 Ultra Unified QMO API v1.0")
sp=p.add_subparsers(dest="cmd",required=True)

a=sp.add_parser("object"); a.add_argument("handle")
a=sp.add_parser("neighbors"); a.add_argument("handle"); a.add_argument("--direction",choices=["out","in","both"],default="both"); a.add_argument("--mode",choices=["direct","typed","navigation"],default="typed")
a=sp.add_parser("path"); a.add_argument("source"); a.add_argument("target"); a.add_argument("--direction",choices=["out","both"],default="out"); a.add_argument("--mode",choices=["direct","typed","navigation"],default="typed"); a.add_argument("--depth",type=int,default=20)
a=sp.add_parser("recover"); a.add_argument("seed"); a.add_argument("--direction",choices=["out","in","both"],default="both"); a.add_argument("--mode",choices=["direct","typed","navigation"],default="typed")
a=sp.add_parser("search"); a.add_argument("query"); a.add_argument("--limit",type=int,default=20)
a=sp.add_parser("source-search"); a.add_argument("query"); a.add_argument("--limit",type=int,default=20)
a=sp.add_parser("equation"); a.add_argument("query")
a=sp.add_parser("debt"); a.add_argument("query",nargs="?")
a=sp.add_parser("closure"); a.add_argument("query",nargs="?")
a=sp.add_parser("models")
a=sp.add_parser("stats")

args=p.parse_args()
con=sqlite3.connect(DB)
con.row_factory=sqlite3.Row
cur=con.cursor()

if args.cmd=="object":
    h=resolve(cur,args.handle)
    cur.execute("SELECT * FROM objects WHERE handle=?",(h,))
    out=dictrows(cur)
elif args.cmd=="neighbors":
    h=resolve(cur,args.handle)
    out=[]
    if args.direction in ("out","both"):
        cur.execute("SELECT * FROM edges WHERE source=?",(h,))
        out += [dict(r) for r in cur.fetchall() if edge_allowed(r,args.mode)]
    if args.direction in ("in","both"):
        cur.execute("SELECT * FROM edges WHERE target=?",(h,))
        out += [dict(r) for r in cur.fetchall() if edge_allowed(r,args.mode)]
elif args.cmd=="path":
    s=resolve(cur,args.source); t=resolve(cur,args.target)
    cur.execute("SELECT * FROM edges WHERE closure_eligible=1")
    es=[dict(r) for r in cur.fetchall()]
    gout={}; gin={}
    for e in es:
        if not edge_allowed(e,args.mode): continue
        gout.setdefault(e["source"],[]).append(e)
        gin.setdefault(e["target"],[]).append(e)
    q=deque([(s,[])]); seen={s}; found=None
    while q:
        x,path=q.popleft()
        if len(path)>=args.depth: continue
        for e in gout.get(x,[]):
            y=e["target"]
            step={"source":x,"relation":e["relation"],"target":y,"reversed_for_navigation":False,"layer":e["layer"],"status":e["status"],"provenance":json.loads(e["provenance_json"]) if e["provenance_json"] else None}
            np=path+[step]
            if y==t: found=np; q.clear(); break
            if y not in seen: seen.add(y); q.append((y,np))
        if found: break
        if args.direction=="both":
            for e in gin.get(x,[]):
                y=e["source"]
                step={"source":x,"relation":"REVERSE("+e["relation"]+")","target":y,"reversed_for_navigation":True,"layer":e["layer"],"status":e["status"],"provenance":json.loads(e["provenance_json"]) if e["provenance_json"] else None}
                np=path+[step]
                if y==t: found=np; q.clear(); break
                if y not in seen: seen.add(y); q.append((y,np))
    out={"source":s,"target":t,"mode":args.mode,"direction":args.direction,"found":found is not None,"path":found}
elif args.cmd=="recover":
    seed=resolve(cur,args.seed)
    cur.execute("SELECT * FROM edges WHERE closure_eligible=1")
    es=[dict(r) for r in cur.fetchall()]
    gout={};gin={}
    for e in es:
        if not edge_allowed(e,args.mode): continue
        gout.setdefault(e["source"],set()).add(e["target"])
        gin.setdefault(e["target"],set()).add(e["source"])
    seen={seed}; waves=[[seed]]
    while True:
        nxt=set()
        for x in waves[-1]:
            if args.direction in ("out","both"): nxt.update(gout.get(x,set()))
            if args.direction in ("in","both"): nxt.update(gin.get(x,set()))
        nxt-=seen
        if not nxt: break
        seen|=nxt; waves.append(sorted(nxt))
    out={"seed":seed,"mode":args.mode,"direction":args.direction,"terminal":"NO_NEW_STRUCTURE","iterations_used":len(waves)-1,"wave_counts":[len(w) for w in waves],"recovered_count":len(seen),"recovered":sorted(seen)}
elif args.cmd=="search":
    q=args.query.replace('"',' ')
    cur.execute("SELECT handle,name,definition,math,status,domains FROM object_fts WHERE object_fts MATCH ? LIMIT ?",(q,args.limit))
    out=dictrows(cur)
elif args.cmd=="source-search":
    q=args.query.replace('"',' ')
    cur.execute("SELECT doc_id,domain,source_path,snippet(source_fts,3,'[',']','...',24) AS snippet FROM source_fts WHERE source_fts MATCH ? LIMIT ?",(q,args.limit))
    out=dictrows(cur)
elif args.cmd=="equation":
    q="%"+args.query+"%"
    cur.execute("SELECT * FROM equations WHERE id LIKE ? OR owner LIKE ? OR expression LIKE ? OR meaning LIKE ? LIMIT 100",(q,q,q,q))
    out=dictrows(cur)
elif args.cmd=="debt":
    if args.query:
        q="%"+args.query+"%"
        cur.execute("SELECT * FROM proof_debt WHERE id LIKE ? OR title LIKE ? OR status LIKE ? OR domain LIKE ?",(q,q,q,q))
    else:
        cur.execute("SELECT * FROM proof_debt")
    out=dictrows(cur)
elif args.cmd=="closure":
    if args.query:
        q="%"+args.query+"%"
        cur.execute("SELECT * FROM closures WHERE id LIKE ? OR object_handle LIKE ? OR decision LIKE ? OR domain LIKE ?",(q,q,q,q))
    else:
        cur.execute("SELECT * FROM closures")
    out=dictrows(cur)
elif args.cmd=="models":
    cur.execute("SELECT * FROM models ORDER BY model_handle")
    out=dictrows(cur)
elif args.cmd=="stats":
    out={}
    for table in ["objects","edges","equations","proof_debt","qmos","closures","models","reachability_summary"]:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        out[table]=cur.fetchone()[0]
    cur.execute("SELECT layer,COUNT(*) c FROM edges GROUP BY layer ORDER BY c DESC")
    out["edges_by_layer"]=dictrows(cur)
    cur.execute("SELECT domain,COUNT(*) c FROM proof_debt GROUP BY domain")
    out["proof_debt_by_domain"]=dictrows(cur)

print(json.dumps(out,indent=2,ensure_ascii=False))
