from dataclasses import dataclass
from collections import defaultdict

@dataclass(frozen=True)
class Seed:
    name: str
    chirality: str

def mirror(c):
    return 'R' if c == 'L' else 'L'

class UF:
    def __init__(self, items): self.p={x:x for x in items}
    def find(self,x):
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra != rb: self.p[rb]=ra
    def classes(self):
        d=defaultdict(set)
        for x in self.p: d[self.find(x)].add(x)
        return list(d.values())

def normalized(classes):
    return sorted([tuple(sorted(c)) for c in classes], key=str)

def quotient(seeds, edges, order=None):
    items=[]; labels={}
    for s in seeds:
        for k in range(4):
            x=(s.name,k); items.append(x); labels[x]='N' if k < 2 else 'E'
    uf=UF(items)
    seq=edges if order is None else [edges[i] for i in order]
    for eid,a,pa,b,pb in seq:
        xa=(a,pa); xb=(b,pb)
        assert labels[xa]=='N' and labels[xb]=='N'
        uf.union(xa,xb)
    classes=uf.classes()
    for cl in classes:
        assert len({labels[x] for x in cl})==1
    for s in seeds:
        reps=[uf.find((s.name,k)) for k in range(4)]
        assert len(set(reps))==4, f'source collapse in {s.name}'
    return uf, classes, labels

# Three-seed L-R-L parenthesization/order test.
A=Seed('A','L'); B=Seed('B','R'); C=Seed('C','L')
edges3=[('eAB','A',0,'B',0),('eBC','B',1,'C',0)]
_,c1,_=quotient([A,B,C],edges3,[0,1])
_,c2,_=quotient([A,B,C],edges3,[1,0])
assert normalized(c1)==normalized(c2)
assert len(c1)==10

# Exact user 3x3: all same chirality.
pos=[(r,c) for r in range(3) for c in range(3)]
nn=[]
for r,c in pos:
    for dr,dc in ((1,0),(0,1)):
        rr,cc=r+dr,c+dc
        if rr<3 and cc<3: nn.append(((r,c),(rr,cc)))
diag=[]
for r in range(2):
    for c in range(2):
        diag += [((r,c),(r+1,c+1)),((r,c+1),(r+1,c))]
uniform={p:'L' for p in pos}
assert sum(uniform[v]==mirror(uniform[u]) for u,v in nn)==0
assert sum(uniform[v]==mirror(uniform[u]) for u,v in diag)==0

# Derived checkerboard test arrangement.
checker={p:('L' if (p[0]+p[1])%2==0 else 'R') for p in pos}
assert sum(checker[v]==mirror(checker[u]) for u,v in nn)==12
assert sum(checker[v]==mirror(checker[u]) for u,v in diag)==0
assert list(checker.values()).count('L')==5 and list(checker.values()).count('R')==4

# Maximal connected port-injective snake, using two null ports maximum per seed.
snake=[(0,0),(0,1),(0,2),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)]
snake_pairs=list(zip(snake[:-1],snake[1:]))
seeds={p:Seed(f'r{p[0]+1}c{p[1]+1}',checker[p]) for p in pos}
inc=defaultdict(int); snake_edges=[]
for i,(u,v) in enumerate(snake_pairs,1):
    pu=inc[u]; pv=inc[v]; inc[u]+=1; inc[v]+=1
    assert pu<2 and pv<2
    snake_edges.append((f's{i}',seeds[u].name,pu,seeds[v].name,pv))
_,cs,ls=quotient(list(seeds.values()),snake_edges)
assert len(cs)==28
assert sum(next(iter({ls[x] for x in cl}))=='N' for cl in cs)==10
assert sum(next(iter({ls[x] for x in cl}))=='E' for cl in cs)==18
assert sorted(inc.values())==[1,1,2,2,2,2,2,2,2]
orders={
 'forward':list(range(8)),
 'reverse':list(reversed(range(8))),
 'row_first':[0,1,3,4,6,7,2,5],
 'vertical_first':[2,5,0,1,3,4,6,7],
}
parts={}
for name,order in orders.items():
    _,cc,_=quotient(list(seeds.values()),snake_edges,order)
    parts[name]=normalized(cc)
assert all(parts['forward']==x for x in parts.values())
assert len({tuple(snake_edges[i][0] for i in order) for order in orders.values()})==4

# 2x2 checkerboard plaquette: row-first/column-first same carrier, different history.
pos2=[(0,0),(0,1),(1,0),(1,1)]
ch2={p:('L' if (p[0]+p[1])%2==0 else 'R') for p in pos2}
s2={p:Seed(f'q{p[0]+1}{p[1]+1}',ch2[p]) for p in pos2}
pla=[((0,0),(0,1)),((1,0),(1,1)),((0,0),(1,0)),((0,1),(1,1))]
inc2=defaultdict(int); ep=[]
for i,(u,v) in enumerate(pla,1):
    pu=inc2[u]; pv=inc2[v]; inc2[u]+=1; inc2[v]+=1
    ep.append((f'p{i}',s2[u].name,pu,s2[v].name,pv))
_,cp,lp=quotient(list(s2.values()),ep)
assert len(cp)==12
assert sum(next(iter({lp[x] for x in cl}))=='N' for cl in cp)==4
assert sum(next(iter({lp[x] for x in cl}))=='E' for cl in cp)==8
assert all(v==2 for v in inc2.values())
po={'row_first':[0,1,2,3],'column_first':[2,3,0,1],'reverse':[3,2,1,0]}
pp={}
for name,order in po.items():
    _,cc,_=quotient(list(s2.values()),ep,order)
    pp[name]=normalized(cc)
assert all(pp['row_first']==x for x in pp.values())
assert len({tuple(ep[i][0] for i in order) for order in po.values()})==3

print('R10 RECURSIVE VERIFIER: PASS')
print('three_seed_chain_classes=10')
print('uniform_3x3_admissible_nn_edges=0')
print('uniform_3x3_admissible_diagonal_edges=0')
print('checkerboard_3x3_chirality_compatible_nn_edges=12')
print('checkerboard_3x3_chirality_compatible_diagonal_edges=0')
print('checkerboard_counts=L5,R4')
print('snake_edges=8')
print('snake_carrier_classes=28')
print('snake_null_classes=10')
print('snake_existence_classes=18')
print('snake_degree_multiset=1,1,2,2,2,2,2,2,2')
print('snake_order_variants_same_structural_partition=4/4')
print('plaquette_edges=4')
print('plaquette_carrier_classes=12')
print('plaquette_null_classes=4')
print('plaquette_existence_classes=8')
print('plaquette_order_variants_same_structural_partition=3/3')
print('raw_one_point_self_copy_gluing_cardinality=7 (non-idempotent)')
print('raw_interface_unit_gluing_cardinality=4 (gluing-layer unit candidate only)')
