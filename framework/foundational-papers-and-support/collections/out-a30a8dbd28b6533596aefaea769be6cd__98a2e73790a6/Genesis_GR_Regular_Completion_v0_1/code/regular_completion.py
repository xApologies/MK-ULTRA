"""GRC-1: NEW regular positive-pair reformulation of classical metric GR.

Not an implementation of the unchanged archived microscopic Genesis model.
All matrix functions in this file, except .inv(), are ELEMENTWISE.
The source/target matter theory and boundary data must be identical.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import numpy as np
import sympy as sp


def elementwise(matrix: sp.MatrixBase, function) -> sp.ImmutableMatrix:
    return sp.ImmutableMatrix(matrix.applyfunc(function))


def _symmetric(matrix: sp.MatrixBase) -> sp.ImmutableMatrix:
    m = sp.ImmutableMatrix(matrix)
    if m.shape != (4, 4):
        raise ValueError('A four-by-four matrix is required.')
    if any(sp.simplify(m[i,j]-m[j,i]) != 0 for i in range(4) for j in range(4)):
        raise ValueError('The matrix must be provably symmetric.')
    return m


def _positive_constant(value: sp.Expr, name: str) -> sp.Expr:
    x=sp.sympify(value)
    if x.is_positive is not True:
        raise ValueError(f'{name} must be provably positive.')
    return x


@dataclass(frozen=True)
class PositivePair:
    """Canonical symmetric eight-channel weights, with ten free components.

    This algebraic record does not on its own certify Lorentzian signature or a
    field equation. Positivity is strict; no extra variables are stored in W.
    """
    P: sp.ImmutableMatrix
    Q: sp.ImmutableMatrix
    sigma: sp.Expr = sp.S.One
    coupling: sp.Expr = sp.S.One

    def decode(self) -> sp.ImmutableMatrix:
        return elementwise(2*self.coupling*(self.P-self.Q), sp.simplify)

    def network(self) -> sp.ImmutableMatrix:
        return sp.ImmutableMatrix.vstack(
            sp.ImmutableMatrix.hstack(self.P,self.Q),
            sp.ImmutableMatrix.hstack(self.Q,self.P))

    def normalization_residual(self) -> sp.ImmutableMatrix:
        c=self.sigma**2/(16*self.coupling**2)
        return sp.ImmutableMatrix(4,4,lambda i,j:sp.simplify(self.P[i,j]*self.Q[i,j]-c))


def encode_metric(g: sp.MatrixBase, sigma=sp.S.One, coupling=sp.S.One) -> PositivePair:
    """Exact algebraic encoder, valid for any real symmetric g; require Lorentz
    signature separately when admitting a gravitational configuration.
    """
    g=_symmetric(g)
    sigma=_positive_constant(sigma,'sigma')
    coupling=_positive_constant(coupling,'coupling')
    r=elementwise(g,lambda x:sp.sqrt(x*x+sigma*sigma))
    return PositivePair(elementwise((r+g)/(4*coupling),sp.simplify),
                        elementwise((r-g)/(4*coupling),sp.simplify),sigma,coupling)


def encode_z(z: sp.MatrixBase, sigma=sp.S.One, coupling=sp.S.One) -> PositivePair:
    z=_symmetric(z)
    sigma=_positive_constant(sigma,'sigma')
    coupling=_positive_constant(coupling,'coupling')
    return PositivePair(elementwise(z,lambda x:sigma*sp.exp(x)/(4*coupling)),
                        elementwise(z,lambda x:sigma*sp.exp(-x)/(4*coupling)),sigma,coupling)


def metric_from_z(z: sp.MatrixBase, sigma=sp.S.One) -> sp.ImmutableMatrix:
    return elementwise(_symmetric(z),lambda x:sp.sympify(sigma)*sp.sinh(x))


def z_from_metric(g: sp.MatrixBase, sigma=sp.S.One) -> sp.ImmutableMatrix:
    sigma=_positive_constant(sigma,'sigma')
    return elementwise(_symmetric(g),lambda x:sp.asinh(x/sigma))


def rechart(pair: PositivePair, J: sp.MatrixBase) -> PositivePair:
    """New coordinates: g_new=J.T*g_old*J, J=dx_old/dx_new.
    All fields must also be evaluated at the matching spacetime point.
    """
    if J.shape != (4,4) or sp.simplify(J.det())==0:
        raise ValueError('A nonsingular four-by-four coordinate Jacobian is required.')
    return encode_metric(J.T*pair.decode()*J,pair.sigma,pair.coupling)


def phase_forward(tau: sp.Expr, chi: Sequence[sp.Expr], beta=sp.S.One,
                  gamma=sp.S.One) -> sp.Expr:
    """Local real lift of Theta=tau+gamma*sum(chi^2)/(2 beta) mod 2 pi."""
    beta=_positive_constant(beta,'beta')
    return sp.sympify(tau)+sp.sympify(gamma)*sum(x*x for x in chi)/(2*beta)


def phase_inverse(theta: sp.Expr, chi: Sequence[sp.Expr], beta=sp.S.One,
                  gamma=sp.S.One) -> sp.Expr:
    beta=_positive_constant(beta,'beta')
    return sp.sympify(theta)-sp.sympify(gamma)*sum(x*x for x in chi)/(2*beta)


def field_space_metric(chi: Sequence[sp.Expr], beta=sp.S.One,
                       gamma=sp.S.One) -> sp.ImmutableMatrix:
    """Squared-completion scalar metric. v.K.v=beta(v0+gamma chi.v/beta)^2+v.v."""
    beta=_positive_constant(beta,'beta'); gamma=sp.sympify(gamma)
    v=sp.ImmutableMatrix(chi); n=len(chi)
    return sp.ImmutableMatrix.vstack(
        sp.ImmutableMatrix.hstack(sp.ImmutableMatrix([[beta]]),gamma*v.T),
        sp.ImmutableMatrix.hstack(gamma*v,sp.eye(n)+gamma**2*v*v.T/beta))


def scalar_source(coords, g, theta, chi, beta=sp.S.One, potential=sp.S.Zero):
    """Source of the SPECIFIED target scalar action, not stress inferred from curvature."""
    u=sp.ImmutableMatrix([sp.diff(theta,x) for x in coords])
    vs=[sp.ImmutableMatrix([sp.diff(c,x) for x in coords]) for c in chi]
    k=beta*u*u.T
    for v in vs:k+=v*v.T
    lag=sp.simplify(-sp.trace(g.inv()*k)/2-potential)
    T=elementwise(k+g*lag,sp.simplify)
    return lag,T


def lorentzian_numeric(g: np.ndarray, tol=1e-11) -> bool:
    g=np.asarray(g,dtype=float)
    if g.shape != (4,4) or not np.all(np.isfinite(g)) or not np.allclose(g,g.T,atol=tol):
        return False
    e=np.linalg.eigvalsh(g)
    return np.count_nonzero(e < -tol)==1 and np.count_nonzero(e > tol)==3


def encode_numeric(g, sigma=1.0, coupling=1.0):
    g=np.asarray(g,dtype=float)
    if sigma<=0 or coupling<=0 or not np.isfinite(sigma+coupling):
        raise ValueError('Positive finite normalization constants are required.')
    if not lorentzian_numeric(g):
        raise ValueError('Input is not a numerically certified (-+++) metric.')
    z=np.arcsinh(g/sigma)
    with np.errstate(over='raise',under='raise',invalid='raise'):
        try:
            P=sigma*np.exp(z)/(4*coupling)
            Q=sigma*np.exp(-z)/(4*coupling)
        except FloatingPointError as exc:
            raise ArithmeticError('Finite precision range exceeded; use exact/high-precision arithmetic.') from exc
    return P,Q


def decode_numeric(P,Q,sigma=1.0,coupling=1.0,tol=1e-10):
    P=np.asarray(P,dtype=float);Q=np.asarray(Q,dtype=float)
    if P.shape!=(4,4) or Q.shape!=(4,4) or sigma<=0 or coupling<=0:
        raise ValueError('Invalid dimensions or constants.')
    if not np.all(np.isfinite(P)) or not np.all(np.isfinite(Q)) or np.any(P<=0) or np.any(Q<=0):
        raise ValueError('Weights must be positive and finite.')
    if not np.allclose(P,P.T,atol=tol) or not np.allclose(Q,Q.T,atol=tol):
        raise ValueError('Weights must be symmetric.')
    if not np.allclose(P*Q,sigma**2/(16*coupling**2),rtol=tol,atol=tol):
        raise ValueError('Noncanonical pair: product normalization fails.')
    g=2*coupling*(P-Q)
    if not lorentzian_numeric(g):
        raise ValueError('Decoded metric fails the declared Lorentzian-domain check.')
    return g


def native_connection(coords: Sequence[sp.Symbol], z: sp.MatrixBase,
                      sigma=sp.S.One) -> tuple[sp.ImmutableMatrix,...]:
    """Levi-Civita coefficients computed directly with the Z-field chain rule.

    Gamma[mu][rho,nu]. Invertible h(Z) and a stated smooth Lorentzian domain
    must be checked by the caller; this routine does not impose field equations.
    """
    if len(coords)!=4:
        raise ValueError('Four coordinates are required.')
    z=_symmetric(z);sigma=_positive_constant(sigma,'sigma')
    h=metric_from_z(z,sigma);inv=h.inv()
    def dh(mu,a,b):return sigma*sp.cosh(z[a,b])*sp.diff(z[a,b],coords[mu])
    return tuple(sp.ImmutableMatrix(4,4,lambda r,n:sp.simplify(sum(
        inv[r,l]*(dh(mu,l,n)+dh(n,l,mu)-dh(l,mu,n))/2
        for l in range(4)))) for mu in range(4))
