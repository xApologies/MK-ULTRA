from itertools import product

N='N'; E='E'
A={'l11':E,'l12':N,'l21':N,'l22':E}
B={'r11':N,'r12':E,'r21':E,'r22':N}
a='l12'; b='r11'

# quotient classes as frozensets of tagged points
points=[('A',x) for x in A]+[('B',x) for x in B]
classes=[]
shared=frozenset({('A',a),('B',b)})
classes.append(shared)
for p in points:
    if p not in shared:
        classes.append(frozenset({p}))
assert len(classes)==7

def label_of_point(p):
    side,x=p
    return A[x] if side=='A' else B[x]

def label_of_class(c):
    labs={label_of_point(p) for p in c}
    assert len(labs)==1, labs
    return next(iter(labs))

labels=[label_of_class(c) for c in classes]
assert labels.count(N)==3
assert labels.count(E)==4
assert label_of_class(shared)==N

# Representative universal-property check over a finite target with two nodes per label.
Z={'n0':N,'n1':N,'e0':E,'e1':E}
Akeys=list(A); Bkeys=list(B)
Achoices=[[z for z,l in Z.items() if l==A[x]] for x in Akeys]
Bchoices=[[z for z,l in Z.items() if l==B[x]] for x in Bkeys]
checked=0
for av in product(*Achoices):
    fA=dict(zip(Akeys,av))
    for bv in product(*Bchoices):
        fB=dict(zip(Bkeys,bv))
        if fA[a] != fB[b]:
            continue
        checked += 1
        h={}
        for c in classes:
            vals=set()
            for side,x in c:
                vals.add(fA[x] if side=='A' else fB[x])
            assert len(vals)==1
            h[c]=next(iter(vals))
        # label preserving
        for c,z in h.items():
            assert Z[z]==label_of_class(c)
        # the quotient classes jointly determine h uniquely
        assert len(h)==7

print({'status':'PASS','Q_size':len(classes),'N_classes':labels.count(N),'E_classes':labels.count(E),'compatible_target_pairs_checked':checked})
