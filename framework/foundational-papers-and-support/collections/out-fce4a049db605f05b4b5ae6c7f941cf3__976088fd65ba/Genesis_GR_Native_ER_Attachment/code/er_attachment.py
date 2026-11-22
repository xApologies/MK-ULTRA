"""Recovered API 4.3 ER metric map and its explicitly scoped inverse.

Xi contains the supplied ER covectors as columns. Xi is NOT the tangent-frame
anchor used by the earlier tensor translator. Its native construction is open
in the source and is not supplied by this implementation.

A fixed finite network has one W across the domain. Treating W as a smooth
field W(x) is a separately declared resolved-field model, NOT a recovered
coarse-graining theorem. No function here certifies all native constraints.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import sympy as sp


class UnsupportedSector(ValueError):
    """The requested inverse is outside the explicitly supported sector."""


def simplify_matrix(a: sp.MatrixBase) -> sp.ImmutableMatrix:
    return sp.ImmutableMatrix(a.applyfunc(sp.simplify))


def equal(a: sp.MatrixBase, b: sp.MatrixBase) -> bool:
    return a.shape == b.shape and all(sp.simplify(x-y) == 0 for x,y in zip(a,b))


def require_symmetric(a: sp.MatrixBase, name: str) -> None:
    if a.rows != a.cols or not equal(a,a.T):
        raise ValueError(f'{name} must be a symmetric square matrix')


def weights_admission(w: sp.MatrixBase) -> dict:
    """Check the two recovered graph conditions; unknown is not certified true."""
    require_symmetric(w, 'ER weights')
    bad=[]; unknown=[]
    for i in range(w.rows):
        for j in range(i,w.cols):
            x=sp.simplify(w[i,j])
            if x.is_real is False or x.is_nonnegative is False:
                bad.append([i,j,str(x)])
            elif x.is_real is not True or x.is_nonnegative is not True:
                unknown.append([i,j,str(x)])
    return {'status':'REJECTED' if bad else ('UNRESOLVED_SIGN' if unknown else 'NONNEGATIVE_SYMMETRIC'),
            'negative_or_nonreal':bad, 'unknown_entries':unknown,
            'scope':'Only entrywise nonnegativity and symmetry, not all native laws.'}


def er_contribution(xi: sp.MatrixBase, w: sp.MatrixBase, lam: sp.Expr) -> sp.ImmutableMatrix:
    """Exactly g_ER = lambda Xi W Xi^T, as recovered; algebra only."""
    require_symmetric(w,'ER weights')
    if xi.rows != 4 or w.shape != (xi.cols,xi.cols):
        raise ValueError('Expected four spacetime rows and matching ER indices')
    if weights_admission(w)['status']=='REJECTED':
        raise ValueError('Recovered ER weight conditions fail')
    return simplify_matrix(sp.sympify(lam)*xi*w*xi.T)


@dataclass(frozen=True)
class ReferenceContext:
    """Fixed reference data for an archived composite metric.

    phase_reference is d tau_ref. chromatic_delta is an explicitly supplied
    difference, NOT a new rule that calculates g_chi from a raw chi field.
    The full background term cancels by reference subtraction; it is not set
    equal to the full target metric. Coordinates label the admitted chart.
    """
    coordinates: tuple[sp.Symbol,...]
    xi: sp.ImmutableMatrix
    lam: sp.Expr
    reference_metric: sp.ImmutableMatrix
    reference_weights: sp.ImmutableMatrix
    alpha: sp.Expr
    phase_reference: sp.ImmutableMatrix
    chromatic_delta: sp.ImmutableMatrix

    def __post_init__(self) -> None:
        if len(self.coordinates)!=4 or self.xi.rows!=4:
            raise ValueError('The declared spacetime sector is four-dimensional')
        if self.reference_metric.shape!=(4,4) or self.chromatic_delta.shape!=(4,4):
            raise ValueError('Metric contributions must be four by four')
        require_symmetric(self.reference_metric,'Reference metric')
        require_symmetric(self.chromatic_delta,'Chromatic increment')
        if self.phase_reference.shape!=(4,1):
            raise ValueError('Reference phase gradient must be a four-component covector')
        if self.reference_weights.shape!=(self.xi.cols,self.xi.cols):
            raise ValueError('Reference network size mismatch')
        require_symmetric(self.reference_weights,'Reference ER weights')
        if weights_admission(self.reference_weights)['status']=='REJECTED':
            raise ValueError('Invalid reference ER weights')

    def non_er_increment(self, phase_gradient: sp.MatrixBase) -> sp.ImmutableMatrix:
        if phase_gradient.shape!=(4,1):
            raise ValueError('Phase gradient must be a four-component covector')
        u0=self.phase_reference;u=phase_gradient
        return simplify_matrix(self.alpha*(u*u.T-u0*u0.T)+self.chromatic_delta)

    def forward(self, w: sp.MatrixBase, phase_gradient: sp.MatrixBase) -> sp.ImmutableMatrix:
        """Reference-subtracted form of the archived composite metric.

        Xi and lambda must be the SAME in the target and reference records.
        No assumptions about native W dynamics are made by this evaluation.
        """
        if weights_admission(w)['status']=='REJECTED':
            raise ValueError('Native ER weights violate nonnegative symmetry')
        return simplify_matrix(self.reference_metric+self.non_er_increment(phase_gradient)
                               +self.lam*self.xi*(w-self.reference_weights)*self.xi.T)

    def inverse4(self,g: sp.MatrixBase,phase_gradient: sp.MatrixBase) -> tuple[sp.ImmutableMatrix,dict]:
        """Unique algebraic inverse for four independent supplied ER covectors.

        Returning a matrix does not certify target coverage. Admission diagnostics
        accompany it, including whether the recovered weights vary across a chart.
        """
        require_symmetric(g,'Target metric')
        if g.shape!=(4,4):raise ValueError('Target must be four by four')
        if self.xi.shape!=(4,4):raise UnsupportedSector('Four independent ER channels required for this unique inverse')
        if sp.simplify(self.lam)==0:raise UnsupportedSector('Zero ER coupling has no weight inverse')
        if sp.simplify(self.xi.det())==0:raise UnsupportedSector('Rank-deficient ER covectors have no unique four-channel inverse')
        inv=self.xi.inv()
        residual=g-self.reference_metric-self.non_er_increment(phase_gradient)
        w=simplify_matrix(self.reference_weights+inv*residual*inv.T/self.lam)
        diag=weights_admission(w)
        derivatives=[sp.simplify(sp.diff(v,x)) for v in w for x in self.coordinates]
        if all(v==0 for v in derivatives):constant='CONSTANT_ON_CHART'
        elif any(v.is_zero is False or (v.is_polynomial(*self.coordinates) and not sp.Poly(v,*self.coordinates).is_zero) for v in derivatives):constant='VARIES_ON_CHART'
        else:constant='NOT_CERTIFIED_CONSTANT'
        diag.update({'fixed_network_check':constant,
                     'nonzero_conditions':[str(self.lam)+' != 0',str(self.xi.det())+' != 0'],
                     'lorentzian_signature':'MUST_BE_CHECKED_ON_DECLARED_DOMAIN',
                     'native_basis_origin':'NOT_SUPPLIED_BY_THIS_ADAPTER',
                     'full_native_admission':'NOT_CERTIFIED'})
        return w,diag


def right_inverse(xi: sp.MatrixBase) -> sp.ImmutableMatrix:
    """A real full-row-rank matrix right inverse; not an added physical gauge."""
    if xi.rows!=4 or xi.rank()!=4:raise UnsupportedSector('Four-dimensional row rank required')
    return simplify_matrix(xi.T*(xi*xi.T).inv())


def rectangular_fiber(xi:sp.MatrixBase,w:sp.MatrixBase) -> tuple[sp.ImmutableMatrix,sp.ImmutableMatrix]:
    """Split W into a chosen representative and the exact invisible remainder.

    The representative need not satisfy nonnegative ER weights. Neither piece is
    proclaimed physical gauge. Retaining the remainder gives recovery, not GR-only
    equivalence of all the weights.
    """
    require_symmetric(w,'ER weights')
    r=right_inverse(xi); d=xi*w*xi.T
    selected=simplify_matrix(r*d*r.T)
    return selected,simplify_matrix(w-selected)


def phase_stress(g:sp.MatrixBase,u:sp.MatrixBase,beta:sp.Expr,V:sp.Expr) -> sp.ImmutableMatrix:
    """The phase stress tensor actually displayed in API 4.3, fixed-g convention.

    This is one source contribution, not total stress and not an ER source law.
    """
    require_symmetric(g,'Metric')
    if g.shape!=(4,4) or u.shape!=(4,1):raise ValueError('Phase stress shape mismatch')
    if sp.simplify(g.det())==0:raise ValueError('Degenerate metric')
    norm=(u.T*g.inv()*u)[0]
    return simplify_matrix(beta*u*u.T-g*(beta*norm+V)/2)


def raw_native_to_er_inputs(state:object)->None:
    raise UnsupportedSector('No recovered map from raw (D,relational structure,R,B,H,chi) to Xi, chromatic metric and full sources is asserted.')


def recover_constant_network(xi_samples: Sequence[sp.MatrixBase],
                             metric_remainders: Sequence[sp.MatrixBase],
                             lam: sp.Expr,
                             reference_weights: sp.MatrixBase) -> tuple[sp.ImmutableMatrix,dict]:
    """Recover ONE constant network from a jointly separating metric readout family.

    Inputs are the corrected metric differences at specified spacetime points:
    Delta g_a = lambda Xi_a (W-W_ref) Xi_a^T. This does not reinterpret W as
    independently variable at each point. The algebra must have full column rank.
    A finite sample certificate is NOT an all-domain metric-image certificate.
    """
    if not xi_samples or len(xi_samples)!=len(metric_remainders):
        raise ValueError('Matching nonempty observation families required')
    if sp.simplify(lam)==0:raise UnsupportedSector('Zero coupling')
    require_symmetric(reference_weights,'Reference weights')
    n=reference_weights.rows;pairs=[(i,j) for i in range(n) for j in range(i,n)]
    basis=[]
    for i,j in pairs:
        e=sp.zeros(n);e[i,j]=e[j,i]=1;basis.append(e)
    rows=[];rhs=[]
    for xi,dg in zip(xi_samples,metric_remainders):
        if xi.shape!=(4,n) or dg.shape!=(4,4):raise ValueError('Sample dimensions differ')
        require_symmetric(dg,'Metric remainder')
        images=[lam*xi*e*xi.T for e in basis]
        for a in range(4):
            for b in range(a,4):
                rows.append([im[a,b] for im in images]);rhs.append(dg[a,b])
    M=sp.Matrix(rows);r=sp.Matrix(rhs);rank=M.rank();aug_rank=M.row_join(r).rank()
    if aug_rank>rank:raise UnsupportedSector('Metric observations are inconsistent with one constant network')
    if rank<len(pairs):raise UnsupportedSector(f'Nonunique native network: observation rank {rank}, unknown count {len(pairs)}')
    solution,parameters=M.gauss_jordan_solve(r)
    if parameters.rows:raise UnsupportedSector('An unresolved inverse family remains')
    if not equal(M*solution,r):raise UnsupportedSector('Algebraic sample residual failed')
    dw=sp.zeros(n)
    for value,(i,j) in zip(solution,pairs):dw[i,j]=dw[j,i]=sp.simplify(value)
    w=simplify_matrix(reference_weights+dw);report=weights_admission(w)
    report.update({'sample_points':len(xi_samples),'scalar_equations':M.rows,'unknown_symmetric_weights':len(pairs),
                   'observation_rank':rank,'sample_residual':'ZERO',
                   'full_domain_metric_identity':'REQUIRES_SEPARATE_ALL_POINT_CHECK',
                   'full_native_admission':'NOT_CERTIFIED'})
    return w,report
