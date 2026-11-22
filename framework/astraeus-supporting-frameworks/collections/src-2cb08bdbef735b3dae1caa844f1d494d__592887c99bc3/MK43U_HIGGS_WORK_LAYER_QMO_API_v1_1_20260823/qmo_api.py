#!/usr/bin/env python3
import argparse, json, sqlite3
from pathlib import Path
from collections import deque
DB=Path(__file__).with_name("QMO.sqlite")
def rows(cur):
    cols=[d[0] for d in cur.description]
    return [dict(zip(cols,r)) for r in cur.fetchall()]
def resolve(cur,h):
    cur.execute("SELECT canonical_handle FROM aliases WHERE alias=?",(h,))
    r=cur.fetchone()
    return r[0] if r else h
p=argparse.ArgumentParser(description="MK43 Higgs Work-Layer QMO API v1.1")
sp=p.add_subparsers(dest="cmd",required=True)
a=sp.add_parser("object"); a.add_argument("handle")
a=sp.add_parser("neighbors"); a.add_argument("handle"); a.add_argument("--direction",choices=["out","in","both"],default="both")
a=sp.add_parser("search"); a.add_argument("query"); a.add_argument("--limit",type=int,default=20)
a=sp.add_parser("equation"); a.add_argument("handle")
a=sp.add_parser("path"); a.add_argument("source"); a.add_argument("target"); a.add_argument("--depth",type=int,default=20); a.add_argument("--direction",choices=["out","both"],default="out")
a=sp.add_parser("recover"); a.add_argument("seed"); a.add_argument("--direction",choices=["out","in","both"],default="both")
a=sp.add_parser("audit"); a.add_argument("handle",nargs="?",default="@higgs_field")
a=sp.add_parser("debt"); a.add_argument("id",nargs="?")
args=p.parse_args()
con=sqlite3.connect(DB); cur=con.cursor()
if args.cmd=="object":
    h=resolve(cur,args.handle); cur.execute("SELECT * FROM objects WHERE handle=?",(h,)); out=rows(cur)
elif args.cmd=="neighbors":
    h=resolve(cur,args.handle); out=[]
    if args.direction in ("out","both"):
        cur.execute("SELECT * FROM edges WHERE source=?",(h,)); out+=rows(cur)
    if args.direction in ("in","both"):
        cur.execute("SELECT * FROM edges WHERE target=?",(h,)); out+=rows(cur)
elif args.cmd=="search":
    q=args.query.replace('"',' ')
    cur.execute("SELECT handle,text FROM search_fts WHERE search_fts MATCH ? LIMIT ?",(q,args.limit)); out=rows(cur)
elif args.cmd=="equation":
    cur.execute("SELECT * FROM equations WHERE equation_handle=? OR owner=?",(args.handle,resolve(cur,args.handle))); out=rows(cur)
elif args.cmd=="path":
    s=resolve(cur,args.source); t=resolve(cur,args.target)
    cur.execute("SELECT source,relation,target,audit_status,provenance_json FROM edges WHERE closure_eligible=1")
    es=cur.fetchall(); g={}
    for S,R,T,A,P in es:
        g.setdefault(S,[]).append((R,T,A,P))
        if args.direction=="both":
            g.setdefault(T,[]).append(("REVERSE("+R+")",S,A,P))
    q=deque([(s,[])]); seen={s}; found=None
    while q:
        x,path=q.popleft()
        if len(path)>=args.depth: continue
        for rel,y,ast,pv in g.get(x,[]):
            np=path+[{"source":x,"relation":rel,"target":y,"audit_status":ast,"provenance":json.loads(pv)}]
            if y==t: found=np; q.clear(); break
            if y not in seen: seen.add(y); q.append((y,np))
    out={"source":s,"target":t,"found":found is not None,"path":found}
elif args.cmd=="recover":
    seed=resolve(cur,args.seed)
    cur.execute("SELECT source,target FROM edges WHERE closure_eligible=1")
    es=cur.fetchall(); g={}; inc={}
    for S,T in es:
        g.setdefault(S,[]).append(T); inc.setdefault(T,[]).append(S)
    seen={seed}; waves=[[seed]]
    while True:
        new=set()
        for x in waves[-1]:
            if args.direction in ("out","both"): new.update(g.get(x,[]))
            if args.direction in ("in","both"): new.update(inc.get(x,[]))
        new-=seen
        if not new: break
        seen|=new; waves.append(sorted(new))
    out={"seed":seed,"terminal":"NO_NEW_STRUCTURE","iterations_used":len(waves)-1,"wave_counts":[len(w) for w in waves],"recovered_count":len(seen),"waves":waves}
elif args.cmd=="audit":
    h=resolve(cur,args.handle); cur.execute("SELECT * FROM objects WHERE handle=?",(h,)); obj=rows(cur)
    cur.execute("SELECT * FROM proof_debt"); debt=rows(cur)
    cur.execute("SELECT COUNT(*) FROM objects"); oc=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM edges"); ec=cur.fetchone()[0]
    out={"object":obj,"counts":{"objects":oc,"edges":ec},"proof_debt":debt,"closure_ruling":"NATIVE_HIGGS_WORK_LAYER_CLOSED__PHYSICAL_IDENTIFICATION_OPEN"}
elif args.cmd=="debt":
    if args.id: cur.execute("SELECT * FROM proof_debt WHERE id=?",(args.id,))
    else: cur.execute("SELECT * FROM proof_debt")
    out=rows(cur)
print(json.dumps(out,indent=2,ensure_ascii=False))
