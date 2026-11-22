#!/usr/bin/env python3
import argparse, json, sqlite3
from pathlib import Path

DB = Path(__file__).with_name("QMO.sqlite")

def connect():
    return sqlite3.connect(DB)

def rows(cur):
    names=[d[0] for d in cur.description]
    return [dict(zip(names,r)) for r in cur.fetchall()]

p=argparse.ArgumentParser(description="MK43 Transduction QMO query API")
sp=p.add_subparsers(dest="cmd",required=True)

a=sp.add_parser("object"); a.add_argument("handle")
a=sp.add_parser("neighbors"); a.add_argument("handle"); a.add_argument("--direction",choices=["out","in","both"],default="both")
a=sp.add_parser("search"); a.add_argument("query"); a.add_argument("--limit",type=int,default=20)
a=sp.add_parser("ledger"); a.add_argument("ledger_id")
a=sp.add_parser("equation"); a.add_argument("handle")
a=sp.add_parser("path"); a.add_argument("source"); a.add_argument("target"); a.add_argument("--depth",type=int,default=6)

args=p.parse_args()
con=connect(); cur=con.cursor()

if args.cmd=="object":
    cur.execute("SELECT * FROM objects WHERE handle=? OR canonical_handle=?",(args.handle,args.handle))
    out=rows(cur)
elif args.cmd=="neighbors":
    out=[]
    if args.direction in ("out","both"):
        cur.execute("SELECT * FROM edges WHERE source=?",(args.handle,)); out+=rows(cur)
    if args.direction in ("in","both"):
        cur.execute("SELECT * FROM edges WHERE target=?",(args.handle,)); out+=rows(cur)
elif args.cmd=="search":
    q=args.query.replace('"',' ')
    try:
        cur.execute("SELECT handle,text FROM search_fts WHERE search_fts MATCH ? LIMIT ?",(q,args.limit))
    except sqlite3.OperationalError:
        cur.execute("SELECT handle,text FROM search_fts WHERE text LIKE ? LIMIT ?",(f"%{q}%",args.limit))
    out=rows(cur)
elif args.cmd=="ledger":
    cur.execute("SELECT * FROM ledger WHERE ledger_id=?",(args.ledger_id,)); out=rows(cur)
elif args.cmd=="equation":
    cur.execute("SELECT * FROM equations WHERE equation_handle=?",(args.handle,)); out=rows(cur)
elif args.cmd=="path":
    # BFS over typed directed edges.
    from collections import deque
    cur.execute("SELECT source,relation,target FROM edges")
    graph={}
    for s,r,t in cur.fetchall():
        graph.setdefault(s,[]).append((r,t))
    q=deque([(args.source,[])])
    seen={args.source}
    found=None
    while q:
        node,path=q.popleft()
        if len(path)>=args.depth: continue
        for rel,nxt in graph.get(node,[]):
            np=path+[(node,rel,nxt)]
            if nxt==args.target:
                found=np; q.clear(); break
            if nxt not in seen:
                seen.add(nxt); q.append((nxt,np))
    out={"path":found,"found":found is not None}

print(json.dumps(out,indent=2,ensure_ascii=False))
