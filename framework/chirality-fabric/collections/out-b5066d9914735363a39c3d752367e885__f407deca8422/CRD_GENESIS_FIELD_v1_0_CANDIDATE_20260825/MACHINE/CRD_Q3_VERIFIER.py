#!/usr/bin/env python3
"""Compact CRD Genesis-Field v1.0 Q3 verifier."""
import itertools
V=list(itertools.product([0,1], repeat=3)); I={v:i for i,v in enumerate(V)}
E=[]
for v in V:
    for k in range(3):
        w=list(v); w[k]^=1; w=tuple(w)
        if I[v]<I[w]: E.append((I[v],I[w]))
N={i:set() for i in range(8)}
for u,v in E:N[u].add(v);N[v].add(u)
def conn(m):
    if not m:return False
    ns=[i for i in range(8) if m>>i&1];s={ns[0]};st=[ns[0]]
    while st:
        u=st.pop()
        for v in N[u]:
            if m>>v&1 and v not in s:s.add(v);st.append(v)
    return len(s)==len(ns)
def d(m):
    z=0
    for i,(u,v) in enumerate(E):
        if ((m>>u)&1)^((m>>v)&1):z|=1<<i
    return z
C=sorted(set(d(m) for m in range(256)))
M=sorted(set(d(m) for m in range(1,256) if conn(m) and d(m)))
assert len(E)==12 and len(C)==128 and len(M)==103
def relax(weights):
    cost=[sum(weights[i] for i in range(12) if r>>i&1) for r in range(4096)]
    canon={r:min(r^c for c in C) for r in range(4096)}
    mins={q:min(cost[q^c] for c in C) for q in set(canon.values())}
    step={}
    for r in range(4096):
        opts=[(cost[r^m],m,r^m) for m in M if cost[r^m]<cost[r]]
        step[r]=min(opts)[2] if opts else r
    maxn=0
    for r in range(4096):
        x=r;n=0;seen=set()
        while step[x]!=x:
            assert x not in seen;seen.add(x);x=step[x];n+=1
        maxn=max(maxn,n);assert cost[x]==mins[canon[r]]
    return maxn
assert relax([1]*12)<=2
assert relax([1,5,3,2,6,3,4,4,1,5,2,6])<=2
assert len({min(r^c for c in C) for r in range(4096)})==32
print("PASS")
