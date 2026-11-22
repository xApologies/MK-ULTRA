from itertools import product

# Exact one-interface toy carrier consistent with the R05 count:
# each source has two N and two E labels; one N from each side is fused.
A = {"a00":"N", "a01":"E", "a10":"E", "a11":"N"}
B = {"b00":"E", "b01":"N", "b10":"N", "b11":"E"}
a_star = "a11"
b_star = "b01"

D = [("A",x) for x in A] + [("B",x) for x in B]

def qkey(tag, x):
    if (tag,x)==("A",a_star) or (tag,x)==("B",b_star):
        return ("Q","q")
    return (tag,x)

fibers = {}
for d in D:
    fibers.setdefault(qkey(*d), []).append(d)

Q = list(fibers)
assert len(A)==4 and len(B)==4 and len(D)==8 and len(Q)==7
assert sorted(len(v) for v in fibers.values()) == [1,1,1,1,1,1,2]

# A section chooses exactly one representative from each fiber.
section_count = 1
for v in fibers.values():
    section_count *= len(v)
assert section_count == 2

# A section cannot return both antecedents at q.
qfiber = fibers[("Q","q")]
assert set(qfiber)=={("A",a_star),("B",b_star)}

# Seam cut: recover two source-image copies and split q.
A_img = {qkey("A",x) for x in A}
B_img = {qkey("B",x) for x in B}
assert A_img | B_img == set(Q)
assert A_img & B_img == {("Q","q")}

A_cut = {("Acut", x if x != ("Q","q") else "q_A") for x in A_img}
B_cut = {("Bcut", x if x != ("Q","q") else "q_B") for x in B_img}
assert len(A_cut)==4 and len(B_cut)==4

# Re-fusing the two cut interface copies removes exactly one point again.
refused_cardinality = len(A_cut)+len(B_cut)-1
assert refused_cardinality == 7

print("R06_REVERSIBILITY_VERIFIER: PASS")
print("|A|=4 |B|=4 |D|=8 |Q|=7")
print("fiber_sizes=1,1,1,1,1,1,2")
print("quotient_sections=2")
print("seam_cut_sources=4+4")
print("refused_cardinality=7")
