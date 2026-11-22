"""Exact finite ER modal evolution and causal shell elimination.

The frozen-weight recurrence is recovered from API 4.3. Choosing shell nodes is
an explicit finite interface realization, not a derivation of the microscopic
Time-Shell projector, a clock, spacetime, spin 2, or Einstein dynamics.
"""
from __future__ import annotations
import numpy as np


def laplacian(weights: np.ndarray) -> np.ndarray:
    w = np.asarray(weights, dtype=float)
    if w.ndim != 2 or w.shape[0] != w.shape[1]:
        raise ValueError('Weights must be square.')
    if not np.all(np.isfinite(w)) or not np.allclose(w, w.T, atol=1e-13):
        raise ValueError('Weights must be finite and symmetric.')
    if np.min(w) < 0:
        raise ValueError('Native weights must be nonnegative.')
    return np.diag(w.sum(axis=1)) - w


def split_indices(n: int, shell: list[int]):
    if not shell or len(set(shell)) != len(shell) or any(x < 0 or x >= n for x in shell):
        raise ValueError('Specify distinct valid shell indices.')
    s = np.array(shell, dtype=int)
    i = np.array([x for x in range(n) if x not in shell], dtype=int)
    return s, i


def full_trajectory(weights, h0, h1, steps: int, c2: float = 1.0, forcing=None):
    if steps < 1 or c2 <= 0:
        raise ValueError('Positive c_A^2 and at least one step required.')
    a = c2 * laplacian(weights)
    n = len(a)
    x = np.zeros((steps + 1, n))
    x[0], x[1] = np.asarray(h0), np.asarray(h1)
    j = np.zeros_like(x) if forcing is None else np.asarray(forcing, dtype=float)
    if j.shape != x.shape:
        raise ValueError('Forcing must have shape (steps+1, number of nodes).')
    m = 2*np.eye(n) - a
    for t in range(1, steps):
        x[t+1] = m @ x[t] - x[t-1] + j[t]
    return x


def reduced_trajectory(weights, shell, h0, h1, steps, c2=1.0, forcing=None):
    """Compute shell without stepping the bulk; reconstruct bulk from memory.

    All hidden initial data and the full graph remain retained. This is a
    lossless change of representation, not compression or a GR embedding.
    """
    a = c2 * laplacian(weights)
    n = len(a)
    s, i = split_indices(n, shell)
    m = 2*np.eye(n)-a
    mss, msi = m[np.ix_(s,s)], m[np.ix_(s,i)]
    mis, mii = m[np.ix_(i,s)], m[np.ix_(i,i)]
    h0, h1 = np.asarray(h0, dtype=float), np.asarray(h1, dtype=float)
    j = np.zeros((steps+1, n)) if forcing is None else np.asarray(forcing, dtype=float)
    if j.shape != (steps+1,n):
        raise ValueError('Invalid forcing shape.')
    g = [np.zeros((len(i),len(i))), np.eye(len(i))]
    for t in range(1, steps):
        g.append(mii @ g[t] - g[t-1])
    y = np.zeros((steps+1,len(s)))
    y[0],y[1]=h0[s],h1[s]
    b = np.zeros((steps+1,len(i)))
    b[0],b[1]=h0[i],h1[i]
    for t in range(1, steps):
        bt=g[t]@h1[i]-g[t-1]@h0[i]
        for k in range(1,t):
            bt += g[t-k] @ (mis @ y[k] + j[k,i])
        b[t]=bt
        y[t+1]=mss@y[t]-y[t-1]+msi@bt+j[t,s]
    bt=g[steps]@h1[i]-g[steps-1]@h0[i]
    for k in range(1,steps):
        bt+=g[steps-k]@(mis@y[k]+j[k,i])
    b[steps]=bt
    reconstructed=np.zeros((steps+1,n))
    reconstructed[:,s],reconstructed[:,i]=y,b
    return y,reconstructed,g


def shell_stiffness(weights, shell, z: complex, c2=1.0):
    """Schur complement D_S; response is its inverse, not D_S itself."""
    a=c2*laplacian(weights)
    s,i=split_indices(len(a),shell)
    ass=a[np.ix_(s,s)]
    if len(i)==0:
        return ass-z*np.eye(len(s))
    asi,aii=a[np.ix_(s,i)],a[np.ix_(i,i)]
    return ass-z*np.eye(len(s))-asi@np.linalg.solve(aii-z*np.eye(len(i)),asi.T)


def native_invariant(trajectory, weights, c2=1.0):
    """Exact quadratic invariant for fixed W and zero forcing; not physical time energy."""
    a=c2*laplacian(weights)
    return np.array([.5*np.dot(v-u,v-u)+.5*u@a@v
                     for u,v in zip(trajectory[:-1],trajectory[1:])])


def observation_matrix(weights,shell,c2=1.0):
    a=c2*laplacian(weights); n=len(a)
    s,_=split_indices(n,shell)
    m=np.block([[2*np.eye(n)-a,-np.eye(n)],[np.eye(n),np.zeros((n,n))]])
    c=np.concatenate([np.eye(n)[s],np.zeros((len(s),n))],axis=1)
    return np.vstack([c@np.linalg.matrix_power(m,k) for k in range(2*n)]),m,c


def decode_observed_initial(weights,shell,observations,c2=1.0):
    o,m,c=observation_matrix(weights,shell,c2)
    if np.linalg.matrix_rank(o)!=o.shape[1]:
        raise ValueError('Shell history does not distinguish all native initial states.')
    obs=np.asarray(observations).reshape(-1)
    if len(obs)!=o.shape[0]:
        raise ValueError('Provide exactly 2*N successive shell samples.')
    x,res,rank,sv=np.linalg.lstsq(o,obs,rcond=None)
    if not np.allclose(o@x,obs,rtol=1e-9,atol=1e-10):
        raise ValueError('History is inconsistent with this graph and recurrence.')
    return x


def time_varying_reduction(weight_sequence,shell,h0,h1,c2=1.0):
    """Ordered-product memory for a prescribed or retained graph history.

    Graph history is an input here, not inferred from shell samples.
    """
    steps=len(weight_sequence)-1; n=len(h0)
    s,i=split_indices(n,shell); ns,ni=len(s),len(i)
    matrices=[2*np.eye(n)-c2*laplacian(w) for w in weight_sequence]
    fs=[]; gs=[]; ds=[]
    for m in matrices:
        fs.append(np.block([[m[np.ix_(i,i)],-np.eye(ni)],
                            [np.eye(ni),np.zeros((ni,ni))]]))
        gs.append(np.vstack([m[np.ix_(i,s)],np.zeros((ni,ns))]))
        ds.append(np.hstack([m[np.ix_(s,i)],np.zeros((ns,ni))]))
    def phi(t,k):
        out=np.eye(2*ni)
        for j in range(k,t):out=fs[j]@out
        return out
    y=np.zeros((steps+1,ns));y[0]=np.asarray(h0)[s];y[1]=np.asarray(h1)[s]
    hidden=np.r_[np.asarray(h1)[i],np.asarray(h0)[i]]
    for t in range(1,steps):
        yhidden=phi(t,1)@hidden
        for k in range(1,t):yhidden+=phi(t,k+1)@gs[k]@y[k]
        y[t+1]=matrices[t][np.ix_(s,s)]@y[t]-y[t-1]+ds[t]@yhidden
    return y


class CandidateDynamicFoam:
    """NEW classical native-depth variational branch, not recovered canon.

    Each edge has a signed amplitude r; weight w=r^2 is nonnegative.
    Signed amplitudes are RETAINED, not decoded from weights at zero crossings.
    H is an admitted mode amplitude, not a derivation of spin-2 polarizations.
    """
    def __init__(self,n,edges,c2=1.0,inertia=1.0,nu=1.0,rstar=0.0):
        self.n=n;self.edges=list(edges);self.c2=float(c2)
        e=len(edges)
        if c2<=0 or inertia<=0 or nu<0:raise ValueError('Invalid couplings.')
        self.mass=np.r_[np.ones(n),np.full(e,inertia)]
        self.nu=float(nu);self.rstar=np.full(e,rstar,dtype=float)
        self.inc=np.zeros((n,e))
        for k,(i,j) in enumerate(edges):
            if i==j or min(i,j)<0 or max(i,j)>=n:raise ValueError('Invalid edge.')
            self.inc[i,k]=1;self.inc[j,k]=-1
    def weights(self,q):
        r=np.asarray(q)[self.n:];w=np.eye(self.n)
        for x,(i,j) in zip(r,self.edges):w[i,j]=w[j,i]=x*x
        return w
    def gradient(self,q):
        h,r=np.asarray(q)[:self.n],np.asarray(q)[self.n:]
        d=self.inc.T@h
        gh=self.c2*self.inc@(r*r*d)
        gr=self.c2*r*d*d+self.nu*r*(r*r-self.rstar*self.rstar)
        return np.r_[gh,gr]
    def step(self,previous,current):
        return 2*np.asarray(current)-np.asarray(previous)-self.gradient(current)/self.mass
    def reverse(self,current,next_state):
        return 2*np.asarray(current)-np.asarray(next_state)-self.gradient(current)/self.mass
    def potential(self,q):
        h,r=np.asarray(q)[:self.n],np.asarray(q)[self.n:]
        d=self.inc.T@h
        return .5*self.c2*np.dot(r*d,r*d)+.25*self.nu*np.sum((r*r-self.rstar*self.rstar)**2)

class BreathingFoam:
    """NEW fixed-shape ER branch with backreaction and preserved spectral sectors.

    W_ij=a^2 W0_ij for i!=j; self weights are retained separately.
    Every fixed spectral projector of L0 commutes with L_n=a_n^2 L0.
    This preserves the declared mode subspace; it does not derive a spin label.
    """
    def __init__(self,w0,c2=1.0,inertia=1.0,nu=1.0,astar=1.0):
        self.w0=np.asarray(w0,dtype=float);self.l0=laplacian(w0)
        self.n=len(self.l0);self.c2=c2;self.inertia=inertia
        self.nu=nu;self.astar=astar
        if min(c2,inertia)<=0 or nu<0:raise ValueError('Invalid couplings.')
        self.mass=np.r_[np.ones(self.n),inertia]
    def weights(self,a):
        w=a*a*self.w0.copy()
        np.fill_diagonal(w,np.diag(self.w0))
        return w
    def gradient(self,q):
        h=np.asarray(q)[:self.n];a=float(q[-1])
        return np.r_[self.c2*a*a*(self.l0@h),
                     self.c2*a*(h@self.l0@h)+self.nu*a*(a*a-self.astar**2)]
    def step(self,previous,current):
        return 2*np.asarray(current)-np.asarray(previous)-self.gradient(current)/self.mass
    def reverse(self,current,next_state):
        return 2*np.asarray(current)-np.asarray(next_state)-self.gradient(current)/self.mass
