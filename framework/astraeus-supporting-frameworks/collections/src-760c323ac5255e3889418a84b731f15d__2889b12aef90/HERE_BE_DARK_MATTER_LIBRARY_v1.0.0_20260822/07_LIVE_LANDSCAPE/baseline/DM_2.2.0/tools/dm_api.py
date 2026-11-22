#!/usr/bin/env python3
import argparse,json,pathlib,collections
ROOT=pathlib.Path(__file__).resolve().parents[1]

def load(rel):return json.loads((ROOT/rel).read_text(encoding="utf-8"))
HANDLES={x["handle"]:x for x in load("DM20_HANDLE_REGISTRY.json")}
DIRECT=load("registry/PARENT_DIRECT_EDGE_REGISTRY.json")+load("registry/DM_DIRECT_EDGE_REGISTRY.json")
COMPOSED=load("registry/DM_COMPOSED_DEPENDENCY_INDEX.json")
OPEN=load("registry/OPEN_HANDLE_REGISTRY.json")
CONS=load("registry/CONSTRAINT_REGISTRY.json")
LIVE=load("runtime/LIVE_RUNTIME_STATE.json")
ALIASES=load("registry/ALIAS_REGISTRY.json").get("aliases",{})

OUT=collections.defaultdict(list)
for e in DIRECT:OUT[e["source"]].append(e)

def canon(h):return ALIASES.get(h,{}).get("canonical",h)

def summary(_):
    print(json.dumps({
      "release":LIVE["release"],
      "active_geometry":LIVE["active_geometry"],
      "current_primary_handle":LIVE["current_primary_handle"],
      "formal_status":LIVE["formal_status"],
      "physical_status":LIVE["physical_status"],
      "handles":len(HANDLES),
      "direct_edges":len(DIRECT),
      "composed_dependencies":len(COMPOSED),
      "child_circularity":LIVE["child_circularity"],
    },indent=2))

def recover(a):
    h=canon(a.handle)
    print(json.dumps({
      "handle":h,
      "record":HANDLES.get(h),
      "incoming":[e for e in DIRECT if e["target"]==h],
      "outgoing":[e for e in DIRECT if e["source"]==h],
      "composed_in":[e for e in COMPOSED if e["target"]==h][:50],
      "composed_out":[e for e in COMPOSED if e["source"]==h][:50],
    },indent=2,ensure_ascii=False))

def path(a):
    s=canon(a.source);t=canon(a.target)
    rec=next((e for e in COMPOSED if e["source"]==s and e["target"]==t),None)
    direct=next((e for e in DIRECT if e["source"]==s and e["target"]==t),None)
    print(json.dumps({"source":s,"target":t,"direct":direct,"composed":rec},indent=2,ensure_ascii=False))

def crawl(a):
    start=canon(a.handle)
    seen={start};front={start};edges=[]
    for _ in range(a.depth):
        nxt=set()
        for h in front:
            for e in OUT[h]:
                edges.append(e)
                if e["target"] not in seen:
                    seen.add(e["target"]);nxt.add(e["target"])
        front=nxt
        if not front:break
    print(json.dumps({"start":start,"depth":a.depth,"handles":sorted(seen),"edges":edges},indent=2,ensure_ascii=False))

def openh(_):print(json.dumps(OPEN,indent=2,ensure_ascii=False))
def constraints(_):print(json.dumps(CONS,indent=2,ensure_ascii=False))
def selfclosure(_):
    idx=load("DM21_DEPENDENCY_INDEX.json")
    print(json.dumps({k:idx[k] for k in [
      "composable_node_count","primitive_dependency_pair_count",
      "fixed_point_dependency_pair_count","fixed_point_edge_density",
      "closure_growth_factor","child_nontrivial_scc_count","generation_records"
    ]},indent=2))

def main():
    ap=argparse.ArgumentParser()
    sp=ap.add_subparsers(dest="cmd",required=True)
    p=sp.add_parser("summary");p.set_defaults(func=summary)
    p=sp.add_parser("recover");p.add_argument("handle");p.set_defaults(func=recover)
    p=sp.add_parser("path");p.add_argument("source");p.add_argument("target");p.set_defaults(func=path)
    p=sp.add_parser("crawl");p.add_argument("handle");p.add_argument("--depth",type=int,default=2);p.set_defaults(func=crawl)
    p=sp.add_parser("open");p.set_defaults(func=openh)
    p=sp.add_parser("constraints");p.set_defaults(func=constraints)
    p=sp.add_parser("selfclosure");p.set_defaults(func=selfclosure)
    a=ap.parse_args();a.func(a)
if __name__=="__main__":main()
