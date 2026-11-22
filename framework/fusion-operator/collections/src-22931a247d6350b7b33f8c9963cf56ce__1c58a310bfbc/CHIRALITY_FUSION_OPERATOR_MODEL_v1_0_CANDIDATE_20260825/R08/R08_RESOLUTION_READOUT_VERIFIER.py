# R08 Resolution / Readout verifier
from copy import deepcopy

F_AB = {
    "carrier":"Q7",
    "counts":(3,4),
    "source_order":(("A","L"),("B","R")),
    "chirality_multiset":tuple(sorted(("L","R"))),
    "parity":-1,
    "balance":0,
    "content":2,
    "seam":"q",
    "witness":"eta_AB",
}
F_BA = deepcopy(F_AB)
F_BA["source_order"] = (("B","R"),("A","L"))
F_BA["witness"] = "eta_BA"

# synthetic arrangement record: same populations, different formal arrangement marker
F_SYN = deepcopy(F_AB)
F_SYN["carrier"] = "Q7_alt_arrangement"
F_SYN["chirality_multiset"] = tuple(sorted(("X","Y")))
F_SYN["parity"] = None
F_SYN["balance"] = 0
F_SYN["content"] = 2
F_SYN["witness"] = "eta_SYN"

def R0(F): return (F["balance"],)
def R1(F): return (F["chirality_multiset"], F["parity"], F["balance"], F["content"])
def R2(F): return R1(F)+(F["seam"],)
def R3(F): return (F["source_order"],F["chirality_multiset"],F["parity"],F["balance"],F["content"],F["seam"],F["witness"])
def ROCC(F): return (F["counts"],)

assert F_AB != F_BA
assert R0(F_AB)==R0(F_BA)
assert R1(F_AB)==R1(F_BA)
assert R2(F_AB)==R2(F_BA)
assert R3(F_AB)!=R3(F_BA)
assert ROCC(F_AB)==ROCC(F_BA)==ROCC(F_SYN)

# Coarsening consistency for the nested chain
c32=lambda x: (x[1],x[2],x[3],x[4],x[5])  # R3 -> R2 shape: multiset,parity,balance,content,seam
c21=lambda x: x[:4]
c10=lambda x: (x[2],)
assert c32(R3(F_AB))==R2(F_AB)
assert c21(R2(F_AB))==R1(F_AB)
assert c10(R1(F_AB))==R0(F_AB)

# Declared bijective display reindexing: diagonal -> row-like
x=(1,0,0,1)
sigma=(0,3,1,2)
y=tuple(x[i] for i in sigma)
assert y==(1,1,0,0)
# invert sigma
inv=[None]*4
for out_i,in_i in enumerate(sigma): inv[in_i]=out_i
x_recovered=tuple(y[inv[i]] for i in range(4))
assert x_recovered==x
identity_contract_failure=(y!=x)

# Simple visibility matrix for declared feature chain
visibility={
    "R0_balance":{"balance":1,"local_chirality":0,"seam":0,"source_order":0,"witness":0},
    "R1_chi":{"balance":1,"local_chirality":1,"seam":0,"source_order":0,"witness":0},
    "R2_seam":{"balance":1,"local_chirality":1,"seam":1,"source_order":0,"witness":0},
    "R3_full":{"balance":1,"local_chirality":1,"seam":1,"source_order":1,"witness":1},
    "R_occ":{"balance":0,"local_chirality":0,"seam":0,"source_order":0,"witness":0},
}
assert visibility["R0_balance"]["local_chirality"]==0
assert visibility["R1_chi"]["local_chirality"]==1
assert visibility["R2_seam"]["seam"]==1
assert visibility["R3_full"]["source_order"]==1

print("R08 Resolution / Readout Verifier")
print("F_AB != F_BA:",F_AB!=F_BA)
print("R0 aliases source order:",R0(F_AB)==R0(F_BA),R0(F_AB))
print("R1 aliases source order:",R1(F_AB)==R1(F_BA),R1(F_AB))
print("R2 aliases source order while showing seam:",R2(F_AB)==R2(F_BA),R2(F_AB))
print("R3 separates ordered provenance:",R3(F_AB)!=R3(F_BA))
print("occupancy aliases distinct arrangement:",ROCC(F_AB)==ROCC(F_SYN),ROCC(F_AB))
print("coarsening R3->R2 pass:",c32(R3(F_AB))==R2(F_AB))
print("coarsening R2->R1 pass:",c21(R2(F_AB))==R1(F_AB))
print("coarsening R1->R0 pass:",c10(R1(F_AB))==R0(F_AB))
print("display permutation diagonal->row:",x,"->",y)
print("display inverse recovery pass:",x_recovered==x)
print("identity contract would flag mismatch:",identity_contract_failure)
print("visibility:",visibility)
