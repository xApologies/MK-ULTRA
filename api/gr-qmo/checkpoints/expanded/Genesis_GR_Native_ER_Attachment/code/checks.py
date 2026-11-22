"""Checks of the recovered ER rule and derived inverse, not full native closure."""
from pathlib import Path
import json,platform,time
import sympy as s
from er_attachment import *
import prior_translator as tr

ROOT=Path(__file__).resolve().parent.parent
RESULTS=[];OBS=[];START=time.perf_counter()

def check(name,ok,scope=''):
    passed=bool(ok);RESULTS.append({'name':name,'passed':passed,'scope':scope})
    print(('PASS ' if passed else 'FAIL ')+name,flush=True)
    if not passed:raise AssertionError(name)

def rejects(name,fn):
    try:fn()
    except (ValueError,UnsupportedSector):check(name,True,'Negative control');return
    check(name,False)

def context(coords,xi,lam=s.Integer(1),Wref=None,alpha=s.Integer(1)):
    return ReferenceContext(tuple(coords),s.ImmutableMatrix(xi),lam,s.ImmutableMatrix(s.diag(-1,1,1,1)),
        s.ImmutableMatrix(s.eye(xi.cols) if Wref is None else Wref),alpha,s.ImmutableMatrix(s.zeros(4,1)),s.ImmutableMatrix(s.zeros(4)))

def divergence_down(tensor,g,G,coords):
    d=tr.covariant_derivative(tensor,G,lambda i,v:s.diff(v,coords[i]));inv=g.inv()
    return s.ImmutableMatrix([s.simplify(sum(inv[a,c]*d[a,b,c] for a in range(4) for c in range(4))) for b in range(4)])

def main():
    t,x,y,z=s.symbols('t x y z',real=True);coords=(t,x,y,z);eta=s.diag(-1,1,1,1);zero4=s.zeros(4,1)
    lam=s.symbols('lambda',nonzero=True,real=True);alpha=s.symbols('alpha',real=True)
    xi=s.Matrix([[1,1,0,0],[0,2,1,0],[0,0,3,1],[0,0,0,1]])
    u=s.Matrix(s.symbols('u0:4',real=True))
    names=s.symbols('w00 w01 w02 w03 w11 w12 w13 w22 w23 w33',nonnegative=True)
    W=s.zeros(4);k=0
    for i in range(4):
        for j in range(i,4):W[i,j]=W[j,i]=names[k];k+=1
    c=context(coords,xi,lam,alpha=alpha)
    g=c.forward(W,u);back,diag=c.inverse4(g,u)
    check('Archived-field W -> metric -> W, all ten entries',equal(back,W))
    # An arbitrary symmetric target is an algebraic round trip; positivity is separate.
    G=s.zeros(4);sy=s.symbols('g00 g01 g02 g03 g11 g12 g13 g22 g23 g33',real=True);k=0
    for i in range(4):
        for j in range(i,4):G[i,j]=G[j,i]=sy[k];k+=1
    Wg,dg=c.inverse4(G,u)
    check('Symmetric target -> weights -> target algebraic identity',equal(c.forward(Wg,u),G),'Not a certification of nonnegative target coverage')
    check('Unknown native weight signs are not certified',dg['status']=='UNRESOLVED_SIGN')
    check('Reference white metric is recovered, not overcounted',equal(c.forward(s.eye(4),zero4),eta))
    g0=eta-lam*xi*xi.T
    raw=g0+alpha*u*u.T+lam*xi*W*xi.T
    check('Reference subtraction equals original additive formula',equal(raw,g))
    bad=s.eye(4);bad[0,1]=bad[1,0]=-1
    rejects('Reject negative native edge weights',lambda:er_contribution(s.eye(4),bad,1))
    nonsym=s.eye(4);nonsym[0,1]=1
    rejects('Reject nonsymmetric native adjacency',lambda:er_contribution(s.eye(4),nonsym,1))
    rejects('Reject unique inverse with singular covectors',lambda:context(coords,s.diag(1,1,1,0)).inverse4(eta,zero4))
    rejects('Reject zero-coupling inverse',lambda:context(coords,s.eye(4),s.S.Zero).inverse4(eta,zero4))
    indefinite=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
    check('Entrywise nonnegativity is not misread as PSD',weights_admission(indefinite)['status']=='NONNEGATIVE_SYMMETRIC' and indefinite.det()<0)
    cplain=context(coords,s.eye(4));target=eta.copy();target[0,1]=target[1,0]=-s.Rational(1,10)
    wr,dr=cplain.inverse4(target,zero4)
    check('Lorentzian target with negative recovered edge is not admitted',dr['status']=='REJECTED' and target[:2,:2].det()<0)
    varying=s.eye(4);varying[1,1]=1+x*x
    wv,dv=cplain.inverse4(cplain.forward(varying,zero4),zero4)
    check('Fixed-network target consistency detects spatially varying weights',dv['fixed_network_check']=='VARIES_ON_CHART')
    # Coordinate-covector transformation; site weights do not transform.
    J=s.Matrix([[1,1,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,3]])
    cp=ReferenceContext(coords,s.ImmutableMatrix(J.T*xi),lam,s.ImmutableMatrix(J.T*eta*J),s.ImmutableMatrix(s.eye(4)),alpha,s.ImmutableMatrix(zero4),s.ImmutableMatrix(s.zeros(4)))
    wprime,dp=cp.inverse4(J.T*g*J,J.T*u)
    check('ER weight recovery is coordinate covariant',equal(wprime,W))
    # Actual kernel of the recovered map, not an appended hidden label.
    xi5=s.eye(4).row_join(s.Matrix([1,0,0,0]));n=s.Matrix([-1,0,0,0,1]);K=n*n.T
    W5=s.ones(5)+2*s.eye(5);W5b=W5+K/2
    check('Five-channel kernel element annihilates metric contribution',equal(xi5*K*xi5.T,s.zeros(4)))
    check('Distinct positive networks have the same recovered metric',weights_admission(W5b)['status']=='NONNEGATIVE_SYMMETRIC' and W5!=W5b and equal(xi5*W5*xi5.T,xi5*W5b*xi5.T),'This is not a full physical collision without all native source/dynamics checks')
    chosen,rem=rectangular_fiber(xi5,W5)
    check('Rectangular representative plus remainder recovers network',equal(chosen+rem,W5) and equal(xi5*rem*xi5.T,s.zeros(4)))
    columns=[]
    for i in range(5):
        for j in range(i,5):
            b=s.zeros(5);b[i,j]=b[j,i]=1;q=xi5*b*xi5.T
            columns.append(s.Matrix([q[a,b] for a in range(4) for b in range(a,4)]))
    operator=s.Matrix.hstack(*columns)
    check('Five-channel linear kernel has dimension five',operator.rank()==10 and len(operator.nullspace())==5)
    # A whole metric field can separate a constant graph that one point cannot.
    sx=s.symbols('s',real=True);Xif=s.eye(4).row_join(s.Matrix([sx,0,0,0]))
    Wref5=s.eye(5);Wtrue=Wref5+s.ones(5)/20
    Dfield=s.simplify(Xif*(Wtrue-Wref5)*Xif.T)
    locations=(-1,0,1);Xs=[Xif.subs(sx,v) for v in locations];Ds=[Dfield.subs(sx,v) for v in locations]
    solved,cert=recover_constant_network(Xs,Ds,s.Integer(1),Wref5)
    check('Three spacetime readouts separate all fifteen constant graph weights',cert['observation_rank']==15 and cert['scalar_equations']==30)
    check('Overcomplete constant network is recovered without a side record',equal(solved,Wtrue))
    check('Recovered graph reproduces the entire symbolic metric field',equal(Xif*(solved-Wref5)*Xif.T,Dfield))
    check('Constant network recovery preserves native nonnegative symmetry',cert['status']=='NONNEGATIVE_SYMMETRIC')
    rejects('A single deficient snapshot does not masquerade as a complete inverse',lambda:recover_constant_network(Xs[:1],Ds[:1],s.Integer(1),Wref5))
    forged=s.Matrix(Dfield);forged[2,2]+=sx*(sx*sx-1)
    forged_samples=[forged.subs(sx,v) for v in locations]
    wf,cf=recover_constant_network(Xs,forged_samples,s.Integer(1),Wref5)
    check('Full-domain identity detects a target forged between sample points',equal(wf,Wtrue) and not equal(Xif*(wf-Wref5)*Xif.T,forged),'Finite sample matching is not complete target coverage')
    OBS.append({'fixture':'constant five-channel network','covectors':str(Xif),'readout_locations':list(locations),'operator_rank':cert['observation_rank'],'unknown_weights':15,'full_symbolic_identity':'ZERO','native_complete_solution':'NOT_CERTIFIED'})
    # Source-derived phase metric and stress; this input is off shell.
    cp=context(coords,s.eye(4));tau=x*y;grad=s.Matrix([s.diff(tau,q) for q in coords]);gp=cp.forward(s.eye(4),grad)
    D=1+x*x+y*y
    check('Phase primitive generates its non-flat metric without a supplied target',equal(gp,eta+grad*grad.T) and s.simplify(gp.det()+D)==0)
    Ts=phase_stress(gp,grad,1,0);Gamma=tr.christoffel(coords,gp)
    R=tr.curvature_gr(coords,Gamma);ric,scal,ein=tr.scalar_and_einstein(R,gp)
    check('Phase-induced scalar curvature computed exactly',s.simplify(scal+2/D**2)==0)
    box=s.simplify(sum(gp.inv()[i,j]*(s.diff(tau,coords[i],coords[j])-sum(Gamma[i][k,j]*grad[k] for k in range(4))) for i in range(4) for j in range(4)))
    div=divergence_down(tr.Tensor.from_matrix(Ts,(-1,-1)),gp,Gamma,coords)
    check('Recovered phase stress obeys its off-shell divergence identity',equal(div,box*grad))
    check('Non-solution phase input is not promoted to an Einstein solution',box!=0 and not equal(ein.matrix()-Ts,s.zeros(4)))
    OBS.append({'fixture':'tau=x*y','scalar_curvature':str(scal),'phase_box':str(box),'status':'SOURCE_FORMULA_TEST_OFF_SHELL'})
    # Curved metric from a constant finite ER network, with explicit supplied Xi(t).
    tp,H=s.symbols('t H',positive=True);cd=(tp,x,y,z);f=s.sqrt(s.exp(2*H*tp)-1)
    xid=s.diag(1,f,f,f);ct=context(cd,xid);wd=s.diag(1,2,2,2)
    gd=ct.forward(wd,zero4);expected=s.diag(-1,s.exp(2*H*tp),s.exp(2*H*tp),s.exp(2*H*tp))
    check('Constant ER network generates the curved test metric',equal(gd,expected),'Xi is supplied test data, not derived from raw native states')
    wback,db=ct.inverse4(gd,zero4)
    check('Curved GR metric returns the identical constant native weights',equal(wback,wd) and db['fixed_network_check']=='CONSTANT_ON_CHART')
    # Attach this computed metric to the unchanged reference translator.
    frame=tr.Frame(cd,s.ImmutableMatrix(s.eye(4)),('t>0,H>0; Xi invertible; Lorentzian by explicit diagonal form',))
    C=tr.koszul_native(frame,gd);endpoint=tr.EvaluatedGenesisEndpoint(frame,gd,C,s.ImmutableMatrix(s.eye(4)),s.ImmutableMatrix(s.zeros(4)),3*H*H,s.Integer(1))
    gr=endpoint.to_gr();returned=gr.to_genesis_endpoint()
    check('ER adapter composes with both existing tensor-translator directions',equal(gr.metric,gd) and equal(returned.metric,gd) and equal(returned.probe_flux,s.zeros(4)))
    RN=tr.curvature_native(frame,C);rn,scn,en=tr.scalar_and_einstein(RN,gd)
    GG=tr.christoffel(cd,gd);RG=tr.curvature_gr(cd,GG);rg,scg,eg=tr.scalar_and_einstein(RG,gd)
    check('Native and GR curvature calculations agree after ER attachment',RN.equals(RG) and s.simplify(scn-12*H*H)==0)
    residual=en.add(tr.Tensor.from_matrix(gd,(-1,-1)).scale(3*H*H))
    check('Curved endpoint obeys the vacuum Einstein equation with supplied Lambda',residual.equals(tr.Tensor(4,(-1,-1),{})),'The total zero flux is a test input; no claim that unspecified native S_ER yields it')
    target_after=returned.metric
    check('Calculation return path reconstructs ER weights exactly',equal(ct.inverse4(target_after,zero4)[0],wd))
    # Exact field-variation surjectivity, source map rather than an assumed metric lift.
    Dg=s.diag(1,2,3,4);du=s.Matrix([1,2,0,-1]);dv=Dg-alpha*(u*du.T+du*u.T)
    dW=xi.inv()*dv*xi.inv().T/lam
    check('Every target metric variation lifts in the open four-channel sector',equal(lam*xi*dW*xi.T+alpha*(u*du.T+du*u.T),Dg),'No assertion at inequality boundaries or under extra native constraints')
    rejects('Raw full-native attachment remains explicitly unsupported',lambda:raw_native_to_er_inputs({'R':'not evaluated'}))
    OBS.append({'fixture':'constant graph de Sitter','W':str(wd),'Xi':str(xid),'metric':str(gd),'scalar_curvature':str(scn),'Lambda':str(3*H*H),'native_complete_solution':'NOT_CERTIFIED'})

if __name__=='__main__':
    status='ERROR'
    try:main();status='PASS'
    except Exception as e:
        RESULTS.append({'name':'exception','passed':False,'scope':repr(e)});status='FAIL';raise
    finally:
        (ROOT/'results'/'CHECK_RESULTS.json').write_text(json.dumps({'status':status,'named_checks':len(RESULTS),'passed':sum(x['passed'] for x in RESULTS),'checks':RESULTS,'observations':OBS,'elapsed_seconds':time.perf_counter()-START,'python':platform.python_version(),'sympy':s.__version__,'scope':'Exact algebra of recovered API metric contributions, source-derived phase stress, and constructed continuum fixtures. No full native Q_R evaluator, independent ER action closure, or global physical equivalence.'},indent=2))
