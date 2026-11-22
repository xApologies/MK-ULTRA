#!/usr/bin/env python3
import json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(rel):return json.loads((ROOT/rel).read_text())
objs=load("registry/DM_OBJECT_REGISTRY.json")
edges=load("registry/DM_DIRECT_EDGE_REGISTRY.json")
idx=load("DM20_DEPENDENCY_INDEX.json")
sup=load("registry/SUPERSEDED_REGISTRY.json")
errors=[]
hs={o["handle"] for o in objs}
if "@dm_hidden_boundary_realization" in hs:errors.append("superseded umbrella still active")
if any(e["source"]=="@dm_continuity_laplacian" and e["target"]=="@dm_runtime_transition_capacity" for e in edges):
    errors.append("old circular laplacian/capacity edge remains")
if idx["child_nontrivial_scc_count"]!=0:errors.append("child SCC remains")
if idx["active_geometry"]!="S4 -> S3 -> S2":errors.append("geometry mismatch")
if errors:
    print("FAIL");[print("-",x) for x in errors];sys.exit(1)
print("PASS")
print("dm_objects",len(objs))
print("dm_direct_edges",len(edges))
print("fixed_point_dependencies",idx["fixed_point_dependency_pair_count"])
