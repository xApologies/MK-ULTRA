"""Exact algebra for a *specified* smooth metric/transport/flux realization.

This module does not implement Q_R, native lift selection, or native dynamics.
Its functions reject missing/rank-deficient data rather than filling them in.
SymPy expressions are exact; continuum existence and physical validity are not
certified by the matrix operations here.
"""
from __future__ import annotations
from collections.abc import Mapping, Sequence
import sympy as sp


def _square(value: sp.MatrixBase, name: str) -> sp.Matrix:
    result = sp.Matrix(value)
    if result.rows != result.cols or result.rows == 0:
        raise ValueError(f"{name} must be a nonempty square matrix")
    return result


def _inverse(value: sp.Matrix, name: str) -> sp.Matrix:
    determinant = sp.simplify(value.det())
    if determinant == 0:
        raise ValueError(f"{name} is singular")
    # A nonzero symbolic determinant gives a conditional inverse, valid where
    # it is nonzero. No domain/regularity theorem is inferred from this call.
    return value.inv()


def metric_from_transport(seed: sp.MatrixBase,
                          transport: sp.MatrixBase) -> sp.Matrix:
    """Return P^(-T) K P^(-1).

    Caller must supply the Lorentzian seed K and an invertible path transport P.
    Path independence additionally requires invariance under the complete
    relevant holonomy group; this function does not establish that requirement.
    """
    k = _square(seed, "seed")
    p = _square(transport, "transport")
    if p.shape != k.shape:
        raise ValueError("seed and transport dimensions differ")
    if sp.simplify(k-k.T) != sp.zeros(k.rows):
        raise ValueError("seed must be symmetric")
    _inverse(k, "seed")
    inv = _inverse(p, "transport")
    return (inv.T*k*inv).applyfunc(sp.trigsimp)


def seed_from_quadratic_probes(diagonal: Sequence[sp.Expr],
                               pair_sums: Mapping[tuple[int, int], sp.Expr]
                               ) -> sp.Matrix:
    """Recover a symmetric form from q(e_i) and q(e_i+e_j).

    This recovers a form only when q is known to be quadratic on the whole
    vector space. Ten values alone do not prove that a general function is
    quadratic, nondegenerate, or Lorentzian.
    """
    n = len(diagonal)
    if n == 0:
        raise ValueError("at least one diagonal probe is required")
    expected = {(i,j) for i in range(n) for j in range(i+1,n)}
    if set(pair_sums) != expected:
        raise ValueError("exactly one pair-sum probe is required for every i<j")
    k = sp.zeros(n)
    for i in range(n):
        k[i,i] = sp.sympify(diagonal[i])
    for i,j in sorted(expected):
        k[i,j] = k[j,i] = sp.simplify(
            (sp.sympify(pair_sums[i,j])-k[i,i]-k[j,j])/2)
    return k


def invariant_symmetric_forms(holonomies: Sequence[sp.MatrixBase],
                              dimension: int = 4) -> list[sp.Matrix]:
    """Basis of K=K^T satisfying H^T K H=K for the SUPPLIED matrices.

    The list is a full-holonomy test only with a separate completeness proof
    for the supplied generators. Signature and calibration remain separate.
    """
    if dimension < 1:
        raise ValueError("dimension must be positive")
    basis = []
    for i in range(dimension):
        for j in range(i,dimension):
            m = sp.zeros(dimension)
            m[i,j] = 1
            m[j,i] = 1
            basis.append(m)
    if not holonomies:
        return basis
    hs = [_square(h,"holonomy") for h in holonomies]
    if any(h.rows != dimension for h in hs):
        raise ValueError("holonomy dimensions differ")
    for h in hs:
        _inverse(h,"holonomy")
    columns = []
    for b in basis:
        col = []
        for h in hs:
            col.extend(list(h.T*b*h-b))
        columns.append(sp.Matrix(col))
    system = sp.Matrix.hstack(*columns)
    return [sum((coefficient*b for coefficient,b in zip(v,basis)),
                sp.zeros(dimension)) for v in system.nullspace()]


def source_from_flux(normals: sp.MatrixBase, fluxes: sp.MatrixBase,
                     *, require_symmetric: bool = True) -> sp.Matrix:
    """Recover contravariant T from V=T N, where columns of N are conormals.

    Columns of V are local four-momentum flux DENSITIES, not unnormalized
    integrals over finite cells. Geometry and continuum-density existence must
    be established before interpreting the result as a physical stress tensor.
    """
    n = _square(normals,"normal covectors")
    v = sp.Matrix(fluxes)
    if v.shape != n.shape:
        raise ValueError("one complete flux vector is required per conormal")
    t = (v*_inverse(n,"normal covectors")).applyfunc(sp.simplify)
    if require_symmetric and sp.simplify(t-t.T) != sp.zeros(n.rows):
        raise ValueError("fluxes do not give a symmetric source tensor")
    return t


def flux_from_source(source: sp.MatrixBase, normals: sp.MatrixBase) -> sp.Matrix:
    t = _square(source,"source")
    n = sp.Matrix(normals)
    if t.cols != n.rows:
        raise ValueError("source and conormal dimensions differ")
    return (t*n).applyfunc(sp.simplify)


def lower_source(source_up: sp.MatrixBase, metric: sp.MatrixBase) -> sp.Matrix:
    t, g = _square(source_up,"source"), _square(metric,"metric")
    if t.shape != g.shape:
        raise ValueError("source and metric dimensions differ")
    return (g*t*g.T).applyfunc(sp.simplify)
