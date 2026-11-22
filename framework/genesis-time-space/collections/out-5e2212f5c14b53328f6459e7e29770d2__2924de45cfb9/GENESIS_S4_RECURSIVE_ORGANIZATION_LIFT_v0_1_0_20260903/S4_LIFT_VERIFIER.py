import math
import random

TOL = 1e-12

def norm2(x):
    return sum(t*t for t in x)

def normalize(x):
    n = math.sqrt(norm2(x))
    return tuple(t/n for t in x)

def lift34(q, nu):
    if abs(nu) > 1:
        raise ValueError("nu must lie in [-1,1]")
    a = math.sqrt(max(0.0, 1.0-nu*nu))
    return tuple(a*t for t in q) + (nu,)

def pi43(Q):
    V = Q[4]
    a2 = 1.0-V*V
    if a2 <= 0:
        raise ValueError("pole: coordinate-only S3 recovery undefined")
    a = math.sqrt(a2)
    return tuple(t/a for t in Q[:4])

def nested(n, tau, sigma):
    a = math.cos(sigma)*math.cos(tau)
    return (
        a*n[0], a*n[1], a*n[2],
        math.cos(sigma)*math.sin(tau),
        math.sin(sigma),
    )

def close(a,b,tol=TOL):
    return abs(a-b) <= tol

for _ in range(10000):
    q = normalize(tuple(random.uniform(-1,1) for _ in range(4)))
    nu = random.uniform(-0.999999,0.999999)
    Q = lift34(q,nu)
    assert close(norm2(Q),1.0,1e-11)
    qr = pi43(Q)
    assert max(abs(a-b) for a,b in zip(q,qr)) < 1e-10

    n = normalize(tuple(random.uniform(-1,1) for _ in range(3)))
    tau = random.uniform(-math.pi/2,math.pi/2)
    sigma = random.uniform(-math.pi/2,math.pi/2)
    Q2 = nested(n,tau,sigma)
    assert close(norm2(Q2),1.0,1e-11)
    assert close(sum(t*t for t in Q2),1.0,1e-11)

# Equator recovery.
q=(0.5,0.5,0.5,0.5)
Q=lift34(q,0.0)
assert Q == q + (0.0,)

# Pole behavior.
for nu in (-1.0,1.0):
    Q=lift34(q,nu)
    assert all(abs(t) < TOL for t in Q[:4])
    assert Q[4] == nu
    try:
        pi43(Q)
    except ValueError:
        pass
    else:
        raise AssertionError("pole recovery should be guarded")

print("PASS: 10,000 random S3->S4 lifts normalized")
print("PASS: 10,000 interior local recoveries")
print("PASS: 10,000 nested S2->S3->S4 states normalized")
print("PASS: equator recovery")
print("PASS: pole-history guard")
