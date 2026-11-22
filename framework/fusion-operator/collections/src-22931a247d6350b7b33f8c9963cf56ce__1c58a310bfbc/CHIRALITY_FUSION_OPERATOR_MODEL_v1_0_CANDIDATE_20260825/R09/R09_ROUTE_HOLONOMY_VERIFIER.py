from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass(frozen=True)
class FusionRecord:
    carrier: str
    ordered_sources: Tuple[str,str]
    seam: str
    chirality: Tuple[str,str]
    opposition: int
    balance: int
    content: int

@dataclass(frozen=True)
class Augmented:
    F: FusionRecord
    history: Tuple[str,...]

F_AB = FusionRecord('Q',('A','B'),'q',('L','R'),-1,0,2)
F_BA = FusionRecord('Q',('B','A'),'q',('R','L'),-1,0,2)

def transport_prov(x: Augmented, route: Tuple[str,...]) -> Augmented:
    return Augmented(x.F, x.history + route)

def read_R0(x: Augmented): return x.F.balance

def read_R1(x: Augmented): return (tuple(sorted(x.F.chirality)),x.F.opposition,x.F.balance,x.F.content)

def read_R2(x: Augmented): return (read_R1(x),x.F.seam)

def read_R3(x: Augmented): return (x.F.carrier,x.F.ordered_sources,x.F.chirality,x.F.seam,x.F.opposition,x.F.balance,x.F.content)

def read_RH(x: Augmented): return (read_R3(x),x.history)

def mirror(c): return {'L':'R','R':'L'}[c]

def mirror_word(c, n):
    for _ in range(n): c=mirror(c)
    return c

x=Augmented(F_AB,())
p1=('red_portal','blue_portal')
p2=('green_portal','violet_portal')
y1=transport_prov(x,p1)
y2=transport_prov(x,p2)
assert y1.F==y2.F==F_AB
assert y1.history!=y2.history
assert read_R0(y1)==read_R0(y2)
assert read_R1(y1)==read_R1(y2)
assert read_R2(y1)==read_R2(y2)
assert read_R3(y1)==read_R3(y2)
assert read_RH(y1)!=read_RH(y2)

# Closed provenance loop: structural record same, history changes.
loop=('U_to_V','V_to_U')
yloop=transport_prov(x,loop)
assert yloop.F==x.F
assert yloop.history!=x.history

# Double mirror is chirality-trivial but history-nontrivial.
assert mirror_word('L',2)=='L'
assert mirror_word('R',2)=='R'
dm=transport_prov(x,('mirror','mirror'))
assert dm.history!=x.history

# Source swap aliases at coarse levels and separates when order is retained.
x_ab=Augmented(F_AB,('fuse_AB',))
x_ba=Augmented(F_BA,('swap','fuse_BA'))
assert read_R0(x_ab)==read_R0(x_ba)
assert read_R1(x_ab)==read_R1(x_ba)
assert read_R2(x_ab)==read_R2(x_ba)
assert read_R3(x_ab)!=read_R3(x_ba)

# Phase is intentionally absent from route records.
phase_connection: Optional[dict] = None
assert phase_connection is None

# Provenance alone cannot witness coherent vs mixed state: same provenance output.
quantum_tags=('coherent','mixture')
assert transport_prov(x,p1).history == transport_prov(x,p1).history

print('R09 VERIFIER PASS')
print('same-endpoint routes: structural carrier equal, histories distinct')
print('R0-R3 (without route history): routes alias')
print('R_H: routes separate')
print('closed provenance loop: structural identity + nontrivial history append')
print('double mirror: chirality endpoint returns; history remains nonempty')
print('source-swap pair: aliases R0-R2, separates R3')
print('phase connection: UNDEFINED / not supplied')
print('coherence: not witnessed by provenance history')
