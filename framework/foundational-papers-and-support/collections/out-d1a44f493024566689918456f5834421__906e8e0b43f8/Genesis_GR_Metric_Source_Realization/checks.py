"""Reproducible algebraic checks; fixtures are not native gravitational data."""
from __future__ import annotations
import json, platform
from pathlib import Path
import sympy as s
from realization import (metric_from_transport, seed_from_quadratic_probes,
                         invariant_symmetric_forms, source_from_flux,
                         flux_from_source, lower_source)

ROOT=Path(__file__).resolve().parent
results=[]
def verify(name, condition, scope):
    if not bool(condition):
        raise AssertionError(name)
    results.append({"name":name,"passed":True,"scope":scope})
def zero(m):
    return all(s.trigsimp(s.simplify(x))==0 for x in m)

def main():
    # 1. A symbolic identity for every symmetric rank-four quadratic form.
    symbols=s.symbols('k0:10'); K=s.zeros(4); it=iter(symbols)
    for i in range(4):
        for j in range(i,4): K[i,j]=K[j,i]=next(it)
    diagonal=[K[i,i] for i in range(4)]
    pairs={(i,j):K[i,i]+2*K[i,j]+K[j,j]
           for i in range(4) for j in range(i+1,4)}
    verify('all_symmetric_forms_quadratic_probe_decoder',
           zero(seed_from_quadratic_probes(diagonal,pairs)-K),
           'Symbolic tensor identity; does not establish native quadratic probes.')
    # 2. Full symbolic flux round trip under one fixed invertible conormal basis.
    N=s.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,2]])
    V=K*N
    verify('arbitrary_symmetric_source_flux_decoder',
           zero(source_from_flux(N,V)-K),
           'All ten symbolic source components; given exact local flux densities.')
    verify('flux_encoder_round_trip',zero(flux_from_source(source_from_flux(N,V),N)-V),
           'Exact local flux readout identity.')
    try:
        source_from_flux(s.zeros(4),s.zeros(4))
    except ValueError:
        rejected=True
    else: rejected=False
    verify('reject_rank_deficient_normal_data',rejected,'Negative control.')
    try:
        source_from_flux(s.eye(4),s.Matrix([[1,2,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]))
    except ValueError: rejected=True
    else: rejected=False
    verify('reject_nonsymmetric_flux_source',rejected,'Negative control for selected non-spin sector.')
    # 3. Holonomy invariants: declared rational boost generators.
    eta=s.diag(-1,1,1,1); boosts=[]
    for i in (1,2,3):
        H=s.eye(4); H[0,0]=H[i,i]=s.Rational(5,4)
        H[0,i]=H[i,0]=s.Rational(3,4); boosts.append(H)
    forms=invariant_symmetric_forms(boosts)
    verify('boost_invariants_one_dimensional',len(forms)==1 and zero(forms[0]-forms[0][1,1]*eta),
           'Declared matrix fixture, not a claim about native gravitational holonomy.')
    verify('trivial_holonomy_retains_ten_calibration_parameters',
           len(invariant_symmetric_forms([]))==10,'Algebraic calibration count.')
    # 4. A curved geometry reconstructed from independently provided connection
    # coefficients, seed metric, and two segment transports.
    t,x,y,z=s.symbols('t x y z',real=True); coords=(t,x,y,z)
    sn,cs=s.sin(x),s.cos(x); phase=y*cs
    Px=s.diag(1,1,1/sn,1)
    Py=s.eye(4)
    Py[1,1]=Py[2,2]=s.cos(phase)
    Py[1,2]=sn*s.sin(phase);Py[2,1]=-s.sin(phase)/sn
    G=[[[s.S.Zero for _ in range(4)] for _ in range(4)] for _ in range(4)]
    G[1][2][2]=-sn*cs;G[2][1][2]=G[2][2][1]=cs/sn
    Gamma_x=s.Matrix([[G[a][1][b] for b in range(4)] for a in range(4)])
    Gamma_y=s.Matrix([[G[a][2][b] for b in range(4)] for a in range(4)])
    verify('x_segment_parallel_transport',zero(Px.diff(x)+Gamma_x*Px),
           'Constructed curved test on 0<x<pi; base x=pi/2.')
    verify('y_segment_parallel_transport',zero(Py.diff(y)+Gamma_y*Py),
           'Constructed curved test at fixed x.')
    P=s.simplify(Py*Px)
    # Avoid a generic trig matrix inverse by using the directly verified inverse.
    Pinv=s.simplify(Px.inv()*Py.inv())
    g=(Pinv.T*eta*Pinv).applyfunc(s.trigsimp)
    target=s.diag(-1,1,sn**2,1)
    verify('curved_metric_from_seed_and_transport',zero(g-target),
           'Nonflat R x S^2 x R local chart fixture; not a native-corpus solution.')
    verify('seed_round_trip',zero(P.T*g*P-eta),'Exact metric calibration recovery.')
    metric_ok=True
    for mu in range(4):
        Gm=s.Matrix([[G[a][mu][b] for b in range(4)] for a in range(4)])
        metric_ok &= zero(g.diff(coords[mu])-Gm.T*g-g*Gm)
    verify('connection_metric_compatibility',metric_ok,'All four coordinate directions.')
    torsion_ok=all(G[a][b][c]==G[a][c][b]
                   for a in range(4) for b in range(4) for c in range(4))
    verify('connection_torsion_free',torsion_ok,'Constructed connection.')
    inv=g.inv();lc_ok=True
    for a in range(4):
      for b in range(4):
       for c in range(4):
        computed=sum(inv[a,d]*(s.diff(g[d,c],coords[b])+s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d]))/2 for d in range(4))
        lc_ok &= s.trigsimp(computed-G[a][b][c])==0
    verify('connection_recovered_from_metric',lc_ok,'All 64 Christoffel components.')
    Ric=s.zeros(4)
    for i in range(4):
     for j in range(4):
      Ric[i,j]=s.trigsimp(sum(s.diff(G[r][i][j],coords[r])-s.diff(G[r][i][r],coords[j])
        +sum(G[r][r][l]*G[l][i][j]-G[r][j][l]*G[l][i][r] for l in range(4)) for r in range(4)))
    scalar=s.simplify(sum(inv[i,j]*Ric[i,j] for i in range(4) for j in range(4)))
    verify('nonzero_curvature_scalar',scalar==2,'Constructed nonlinear curved fixture.')
    Einstein=s.simplify(Ric-scalar*g/2)
    kappa=s.symbols('kappa',nonzero=True)
    # Source is separately prescribed through directional fluxes, not defined
    # as Einstein/kappa inside the reconstruction code.
    source_prescribed=s.diag(1/kappa,0,0,-1/kappa)
    flux=source_prescribed*N
    recovered=source_from_flux(N,flux)
    verify('curved_einstein_residual_zero',zero(Einstein-kappa*lower_source(recovered,g)),
           'Designed metric/source fixture with Lambda=0; no native source-law claim.')
    div=[]
    for a in range(4):
        div.append(s.trigsimp(sum(s.diff(recovered[a,b],coords[b])+
              sum(G[a][b][c]*recovered[c,b]+G[b][b][c]*recovered[a,c] for c in range(4))
              for b in range(4))))
    verify('source_covariant_conservation',all(v==0 for v in div),'Constructed curved fixture.')
    # 5. Metric pullback under a holonomy-generated alternative path.
    A=s.Matrix([[1,1,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,3]])
    verify('holonomy_preserving_path_independence',
           zero(metric_from_transport(eta,A)-metric_from_transport(eta,A*boosts[0])),
           'Exact algebra; all-loop native invariance has not been verified.')
    report={"python":platform.python_version(),"sympy":s.__version__,
            "check_count":len(results),"checks":results,
            "native_Q_R_implemented":False,
            "native_flux_generation_implemented":False,
            "native_physical_inverse_established":False,
            "fixture_scope":"Algebraic and constructed smooth geometric data only."}
    (ROOT/'CHECK_RESULTS.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
