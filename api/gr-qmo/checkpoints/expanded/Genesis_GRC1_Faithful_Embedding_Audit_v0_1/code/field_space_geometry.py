import sympy as s
from functools import lru_cache

def geometry_from_jets(g, dg, ddg):
    n=g.rows; inv=g.inv()
    zero=s.S.Zero
    def d(a,i,j):return dg.get((a,i,j),zero)
    def dd(a,b,i,j):return ddg.get((a,b,i,j),zero)
    lower={}
    dlower={}
    for i in range(n):
      for j in range(n):
       for k in range(n):
        v=(d(j,i,k)+d(k,i,j)-d(i,j,k))/2
        if v:lower[i,j,k]=v
        for a in range(n):
         v=(dd(a,j,i,k)+dd(a,k,i,j)-dd(a,i,j,k))/2
         if v:dlower[a,i,j,k]=v
    dinv=[-inv*s.Matrix(n,n,lambda i,j:d(a,i,j))*inv for a in range(n)]
    G={}; DG={}
    for i in range(n):
      for j in range(n):
       for k in range(n):
        v=s.factor(sum(inv[i,l]*lower.get((l,j,k),zero) for l in range(n)))
        if v:G[i,j,k]=v
        for a in range(n):
         v=s.factor(sum(dinv[a][i,l]*lower.get((l,j,k),zero)+inv[i,l]*dlower.get((a,l,j,k),zero) for l in range(n)))
         if v:DG[a,i,j,k]=v
    R={}
    for i in range(n):
      for j in range(n):
       for k in range(n):
        for l in range(n):
         v=DG.get((k,i,l,j),zero)-DG.get((l,i,k,j),zero)
         v+=sum(G.get((i,k,m),zero)*G.get((m,l,j),zero)-G.get((i,l,m),zero)*G.get((m,k,j),zero) for m in range(n))
         v=s.factor(v)
         if v:R[i,j,k,l]=v
    ric=s.Matrix(n,n,lambda j,l:s.factor(sum(R.get((i,j,i,l),zero) for i in range(n))))
    scalar=s.factor(s.trace(inv*ric))
    return {'R':R,'Ric':ric,'scalar':scalar,'g':g,'inverse':inv}

def model_jets(chis,beta,gamma,completed=False):
    n=len(chis); d=n+1; a=gamma**2/beta
    chi=s.Matrix(chis)
    g=s.diag(beta,*([1]*n))
    for i in range(n): g[0,i+1]=g[i+1,0]=gamma*chi[i]
    if completed:
      for i in range(n):
       for j in range(n):g[i+1,j+1]+=a*chi[i]*chi[j]
    dg={};ddg={}
    for k in range(n):
      dg[k+1,0,k+1]=gamma; dg[k+1,k+1,0]=gamma
      if completed:
       for i in range(n):
        for j in range(n):
         v=a*((1 if i==k else 0)*chi[j]+chi[i]*(1 if j==k else 0))
         if v:dg[k+1,i+1,j+1]=v
         for l in range(n):
          v=a*((1 if i==k and j==l else 0)+(1 if i==l and j==k else 0))
          if v:ddg[k+1,l+1,i+1,j+1]=v
    return g,dg,ddg

if __name__=='__main__':
 b=s.symbols('beta',positive=True);c=s.symbols('gamma',nonzero=True,real=True)
 for n,chs in [(2,[s.Rational(1,4),s.Rational(1,5)]),(7,[0]*7),(7,[s.Rational(1,4)]+[0]*6)]:
  beta,gamma=(b,c) if not any(chs) else (s.S(2),s.S(3))
  for completed in [False,True]:
   geo=geometry_from_jets(*model_jets(chs,beta,gamma,completed))
   print(n,chs,completed,geo['scalar'],len(geo['R']))
   if not completed:
    a=gamma**2/beta;r2=sum(x*x for x in chs)
    expected=-a*(n-1)*(n-(n-2)*a*r2)/(1-a*r2)**2
    print('formula residual',s.factor(geo['scalar']-expected))
