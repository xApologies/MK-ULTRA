#!/usr/bin/env python3
import json, sys
from pathlib import Path
import networkx as nx

root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
reg=root/'registry'
alg=json.load(open(reg/'RELATION_COMPOSITION_ALGEBRA.json'))['orientation']
edges=json.load(open(reg/'DM_DIRECT_EDGE_REGISTRY.json'))
opens={r['handle'] for r in json.load(open(reg/'OPEN_HANDLE_REGISTRY.json'))}
G=nx.DiGraph(); C=nx.DiGraph()
for e in edges:
    o=alg.get(e['relation'])
    if o=='forward': u,v=e['source'],e['target']
    elif o=='reverse': u,v=e['target'],e['source']
    else: continue
    G.add_edge(u,v,relation=e['relation'])
    if u not in opens: C.add_edge(u,v,relation=e['relation'])
print('query_nontrivial_sccs', [sorted(c) for c in nx.strongly_connected_components(G) if len(c)>1])
print('closure_eligible_nontrivial_sccs', [sorted(c) for c in nx.strongly_connected_components(C) if len(c)>1])
seed='@dm_hidden_state_embedding'
visited={seed}; frontier={seed}; discovered=nx.DiGraph()
for i in range(1,17):
    new=set(); hits=[]
    for u in sorted(frontier):
        for v in sorted(G.successors(u)):
            closes=(u==v) or (v in discovered and u in discovered and nx.has_path(discovered,v,u))
            if closes: hits.append((u,G[u][v]['relation'],v))
            discovered.add_edge(u,v)
            if v not in visited: new.add(v)
    print(i,'frontier',sorted(frontier),'new',sorted(new),'cycle_hits',hits)
    visited |= new
    if hits:
        print('terminal CYCLE_DETECTED'); break
    if not new:
        print('terminal NO_NEW_STRUCTURE'); break
    frontier=new
