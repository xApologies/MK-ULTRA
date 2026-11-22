#!/usr/bin/env python3
"""Rainbow Road Unified API Overlay helper.

Commands:
  roadmap
  coverage
  open
  six-to-three
  overlay <name-or-id>
  bindings <rainbow-role-fragment>
  native <@handle>
  neighbors <@handle>
  path <source> :: <target> [--directed]
  road-to <@target> [--directed]
  search <query>

The full immutable parent database is bundled at:
  PARENT_UNIFIED_API/UNIFIED_QMO.sqlite
"""
import sqlite3,sys,json
from pathlib import Path
from collections import deque

HERE=Path(__file__).resolve()
ROOT=HERE.parents[1]
ODB=ROOT/"DATABASE"/"overlay.sqlite3"
PDB=ROOT/"PARENT_UNIFIED_API"/"UNIFIED_QMO.sqlite"

def oc():
    c=sqlite3.connect(ODB);c.row_factory=sqlite3.Row;return c
def pc():
    c=sqlite3.connect(PDB);c.row_factory=sqlite3.Row;return c

def roadmap():
    c=oc();print(json.dumps([dict(r) for r in c.execute("SELECT * FROM roadmap_steps ORDER BY ordinal")],indent=2));c.close()
def coverage():
    c=oc();print(json.dumps([dict(r) for r in c.execute("SELECT * FROM coverage ORDER BY mode,domain")],indent=2));c.close()
def openq():
    c=oc();print(json.dumps([dict(r) for r in c.execute("SELECT * FROM open_edges ORDER BY id")],indent=2));c.close()
def six():
    p=ROOT/"MACHINE"/"SIX_TO_THREE_SEARCH_SPACE.json";print(p.read_text())
def overlay(q):
    c=oc()
    r=c.execute("""SELECT * FROM overlay_objects
                   WHERE lower(id)=lower(?) OR lower(uri)=lower(?) OR lower(name)=lower(?)""",(q,q,q)).fetchone()
    if not r:
        r=c.execute("SELECT * FROM overlay_objects WHERE lower(name) LIKE lower(?) LIMIT 1",("%"+q+"%",)).fetchone()
    if not r: print(json.dumps({"error":"not_found","query":q},indent=2));return
    out={"object":dict(r)}
    out["edges"]=[dict(x) for x in c.execute("SELECT * FROM overlay_edges WHERE source=? OR target=?",(r["id"],r["id"]))]
    print(json.dumps(out,indent=2));c.close()
def bindings(q):
    c=oc();rows=c.execute("SELECT * FROM native_bindings WHERE lower(rainbow_role) LIKE lower(?)",("%"+q+"%",)).fetchall()
    print(json.dumps([dict(r) for r in rows],indent=2));c.close()
def native(h):
    c=pc();r=c.execute("SELECT * FROM objects WHERE handle=?",(h,)).fetchone()
    print(json.dumps(dict(r) if r else {"error":"not_found","handle":h},indent=2));c.close()
def neighbors(h):
    c=pc();rows=c.execute("""SELECT source,relation,target,layer,status,trust_class,confidence
                             FROM edges WHERE source=? OR target=? ORDER BY edge_id LIMIT 250""",(h,h)).fetchall()
    print(json.dumps([dict(r) for r in rows],indent=2));c.close()

def build_graph(directed=True):
    c=pc()
    g={}
    for r in c.execute("""SELECT source,target,relation,layer,status
                          FROM edges WHERE closure_eligible=1 AND reverse_navigation_only=0"""):
        g.setdefault(r["source"],[]).append((r["target"],r["relation"],r["layer"],r["status"],"forward"))
        if not directed:
            g.setdefault(r["target"],[]).append((r["source"],"REVERSE("+r["relation"]+")",r["layer"],r["status"],"reverse"))
    c.close();return g

def shortest(starts,target,directed):
    g=build_graph(directed)
    prev={s:None for s in starts}; pe={}
    q=deque(starts)
    while q:
        u=q.popleft()
        if u==target:break
        for e in g.get(u,[]):
            v=e[0]
            if v not in prev:
                prev[v]=u;pe[v]=(u,e);q.append(v)
    if target not in prev:return None
    nodes=[];cur=target
    while cur is not None:nodes.append(cur);cur=prev[cur]
    nodes.reverse()
    out=[]
    for i,u in enumerate(nodes[:-1]):
        v=nodes[i+1];e=pe[v][1]
        out.append({"source":u,"relation":e[1],"target":v,"layer":e[2],"status":e[3],"direction":e[4]})
    return out

RR_CORE=[
"@geometric","@inherited_state_bundle","@admissible_continuation","@inheritance_morphism",
"@recursive_inheritance","@chirality_space","@chirality","@chirality_transport","@resolution",
"@bandwidth","@persistence","@persistent_locus","@persistent_boundary","@projection_admissibility",
"@native_constraint_closure","@relational_history","@admissible_equivalence","@genesis_field","@time_space"
]

def path(args):
    directed="--directed" in args
    args=[x for x in args if x!="--directed"]
    if "::" not in args: raise SystemExit("path requires: source :: target")
    k=args.index("::");s=" ".join(args[:k]);t=" ".join(args[k+1:])
    p=shortest([s],t,directed)
    print(json.dumps({"mode":"directed" if directed else "navigation","source":s,"target":t,"path":p},indent=2))
def roadto(args):
    directed="--directed" in args
    args=[x for x in args if x!="--directed"]
    t=" ".join(args)
    p=shortest(RR_CORE,t,directed)
    print(json.dumps({"mode":"directed" if directed else "navigation","source":"overlay://rainbow-road(core anchors)","target":t,"path":p},indent=2))
def search(q):
    co=oc();cp=pc()
    out={"overlay":[dict(r) for r in co.execute("SELECT kind,key,title,body,tags FROM search_fts WHERE search_fts MATCH ? LIMIT 25",(q,))]}
    pat="%"+q.lower()+"%"
    out["parent"]=[dict(r) for r in cp.execute("""SELECT handle,object_type,base_status,domains_json,names_json
        FROM objects WHERE lower(handle) LIKE ? OR lower(names_json) LIKE ? OR lower(definitions_json) LIKE ? LIMIT 50""",(pat,pat,pat))]
    print(json.dumps(out,indent=2));co.close();cp.close()

if __name__=="__main__":
    if len(sys.argv)<2: print(__doc__);raise SystemExit(2)
    cmd=sys.argv[1].lower();args=sys.argv[2:]
    if cmd=="roadmap":roadmap()
    elif cmd=="coverage":coverage()
    elif cmd=="open":openq()
    elif cmd=="six-to-three":six()
    elif cmd=="overlay" and args:overlay(" ".join(args))
    elif cmd=="bindings" and args:bindings(" ".join(args))
    elif cmd=="native" and args:native(" ".join(args))
    elif cmd=="neighbors" and args:neighbors(" ".join(args))
    elif cmd=="path" and args:path(args)
    elif cmd=="road-to" and args:roadto(args)
    elif cmd=="search" and args:search(" ".join(args))
    else: print(__doc__);raise SystemExit(2)
