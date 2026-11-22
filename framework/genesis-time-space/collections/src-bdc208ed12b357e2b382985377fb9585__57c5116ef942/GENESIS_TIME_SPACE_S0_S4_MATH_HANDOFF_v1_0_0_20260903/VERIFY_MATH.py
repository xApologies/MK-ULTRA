import math, random

def s2(u,v):
    D=1+u*u+v*v
    return (2*u/D, 2*v/D, (u*u+v*v-1)/D)

def l23(n,tau):
    c=math.cos(tau)
    return (c*n[0],c*n[1],c*n[2],math.sin(tau))

def l34(q,sigma):
    c=math.cos(sigma)
    return (c*q[0],c*q[1],c*q[2],c*q[3],math.sin(sigma))

def norm2(x): return sum(v*v for v in x)

def pi43(Q):
    d=math.sqrt(1-Q[4]*Q[4])
    return tuple(Q[i]/d for i in range(4))

def pi32(q):
    d=math.sqrt(1-q[3]*q[3])
    return tuple(q[i]/d for i in range(3))

mx=0.0; inv=0.0
for _ in range(10000):
    u=random.uniform(-10,10); v=random.uniform(-10,10)
    tau=random.uniform(-1.4,1.4); sigma=random.uniform(-1.4,1.4)
    n=s2(u,v); q=l23(n,tau); Q=l34(q,sigma)
    mx=max(mx,abs(norm2(n)-1),abs(norm2(q)-1),abs(norm2(Q)-1))
    q2=pi43(Q); n2=pi32(q2)
    inv=max(inv,max(abs(a-b) for a,b in zip(q,q2)),max(abs(a-b) for a,b in zip(n,n2)))
print('samples=10000')
print('max_normalization_error=',repr(mx))
print('max_inverse_recovery_error=',repr(inv))
assert mx < 1e-12
assert inv < 1e-10
print('PASS: algebraic coordinate identities numerically verified.')
