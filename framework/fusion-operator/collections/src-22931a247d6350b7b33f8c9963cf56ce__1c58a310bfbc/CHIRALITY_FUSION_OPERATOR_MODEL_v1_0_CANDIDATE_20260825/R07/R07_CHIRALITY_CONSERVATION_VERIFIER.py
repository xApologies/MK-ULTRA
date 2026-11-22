from itertools import product

# Convention only: L=+1, R=-1. Swapping this convention changes no parity conclusions.
sgn={"L":1,"R":-1}
mirror={"L":"R","R":"L"}

def parity(a,b): return sgn[a]*sgn[b]
def balance(a,b): return sgn[a]+sgn[b]
def content(a,b): return abs(sgn[a])+abs(sgn[b])
def current_admissible(a,b): return parity(a,b)==-1

cases=[]
for a,b in product(["L","R"], repeat=2):
    cases.append((a+b, parity(a,b), balance(a,b), content(a,b), current_admissible(a,b)))

# Exact finite mirror-pair carrier. L and R matrices are used only as a concrete
# mirror pair; the sign convention is not identified with external +/- naming.
L=((1,0),(0,1))
R=((0,1),(1,0))
assert all(R[r][c]==L[r][1-c] for r in range(2) for c in range(2))

A=[("A",r,c) for r in range(2) for c in range(2)]
B=[("B",r,c) for r in range(2) for c in range(2)]
a_star=("A",0,1) # null in L
b_star=("B",0,0) # mirror null in R

# quotient representatives: replace selected interface pair by q
q=("Q","q")
def qrep(x):
    return q if x in {a_star,b_star} else x
Q=set(qrep(x) for x in A+B)
assert len(Q)==7

# induced mirror/source-swap map on quotient
# A(r,c)->B(r,1-c), B(r,c)->A(r,1-c)
def M_raw(x):
    side,r,c=x
    if side=="A": return ("B",r,1-c)
    return ("A",r,1-c)

def M_Q(x):
    if x==q: return q
    return qrep(M_raw(x))

# map closes on Q, is involutive and fixes q
assert all(M_Q(x) in Q for x in Q)
assert all(M_Q(M_Q(x))==x for x in Q)
assert M_Q(q)==q

# label check under mirror pair: use matrix occupancy/null labels
# label 1=singleton-empty/existence marker, 0=null marker in current diagram abstraction
def label_raw(x):
    side,r,c=x
    return L[r][c] if side=="A" else R[r][c]
def label_Q(x):
    if x==q: return 0
    return label_raw(x)
assert all(label_Q(M_Q(x))==label_Q(x) for x in Q)

print("R07 Chirality Conservation Verifier")
print("pair, parity, signed_balance, unsigned_content, current_admissible")
for row in cases: print(*row, sep=", ")
print("Q_cardinality=",len(Q))
print("mirror_involution_pass=",all(M_Q(M_Q(x))==x for x in Q))
print("mirror_label_preservation_pass=",all(label_Q(M_Q(x))==label_Q(x) for x in Q))
print("q_fixed=",M_Q(q)==q)
print("LR_zero_balance_nonzero_content=",balance("L","R")==0 and content("L","R")==2)
print("LL_RR_outside_current_domain=",not current_admissible("L","L") and not current_admissible("R","R"))
