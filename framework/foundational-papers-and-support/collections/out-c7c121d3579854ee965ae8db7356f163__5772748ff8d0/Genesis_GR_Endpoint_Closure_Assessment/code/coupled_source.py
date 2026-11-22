"""Action-derived phase/chromatic sector, not a full native Genesis solver.

The input metric and local real scalar-field lifts must already be specified.
Nothing here supplies ER covectors, the chromatic metric contribution, S_ER,
or the missing native physical equivalence relation. No source is defined
from an Einstein tensor.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import sympy as s

@dataclass(frozen=True)
class ScalarSectorResult:
    lagrangian: s.Expr
    stress_covariant: s.ImmutableMatrix
    euler_lagrange: s.ImmutableMatrix
    kinetic_matrix: s.ImmutableMatrix


def phase_chromatic_model(
    tau: s.Symbol,
    chi: Sequence[s.Symbol],
    G: s.MatrixBase,
    beta: s.Expr,
    gamma: s.Expr,
    phase_potential: s.Expr,
    chromatic_potential: s.Expr,
    potential_coefficient: s.Expr,
) -> tuple[s.ImmutableMatrix, s.Expr]:
    """Return the field-space kinetic matrix and potential.

    All parameters are explicit. In the archived phase action the potential
    coefficient is 1/2; another archived action uses 1. No reconciliation is
    made by choosing a default. G must be symmetric and depend only on chi.
    """
    n = len(chi)
    if n == 0 or G.shape != (n, n):
        raise ValueError('G must be square with one row per chromatic field')
    if len(set((tau, *chi))) != n + 1:
        raise ValueError('Field symbols must be distinct')
    if any(s.simplify(v) != 0 for v in G - G.T):
        raise ValueError('The kinetic field-space metric must be symmetric')
    if any(s.diff(v, tau) != 0 for v in G):
        raise ValueError('This source branch assumes G depends on chi, not tau')
    B = G * s.Matrix(chi)
    K = s.zeros(n + 1)
    K[0, 0] = beta
    for a in range(n):
        K[0, a + 1] = K[a + 1, 0] = gamma * B[a]
        for b in range(n):
            K[a + 1, b + 1] = G[a, b]
    potential = potential_coefficient * phase_potential + chromatic_potential
    return s.ImmutableMatrix(K), s.sympify(potential)


def evaluate_scalar_action(
    coords: Sequence[s.Symbol],
    metric_covariant: s.MatrixBase,
    field_symbols: Sequence[s.Symbol],
    field_values: Sequence[s.Expr],
    kinetic_matrix: s.MatrixBase,
    potential: s.Expr,
    volume_density: s.Expr | None = None,
) -> ScalarSectorResult:
    """Evaluate T_munu and scalar EL residuals from one stated action.

    L = -K_IJ g^munu (d_mu phi^I)(d_nu phi^J)/2 - P(phi).
    EL_I = div(K_IJ grad phi^J) - (d_I K_JK)grad phi^J.grad phi^K/2
           - d_I P.

    A provided volume_density must be the admitted positive sqrt(-det g).
    This symbolic routine is not a domain/signature/regularity proof engine.
    """
    d, n = len(coords), len(field_symbols)
    if d == 0 or n == 0 or len(field_values) != n:
        raise ValueError('Coordinates and field lists must have consistent sizes')
    g = s.Matrix(metric_covariant)
    K = s.Matrix(kinetic_matrix)
    if g.shape != (d, d) or K.shape != (n, n):
        raise ValueError('Metric or kinetic-matrix dimensions do not match')
    if any(s.simplify(v) != 0 for v in g - g.T):
        raise ValueError('Metric must be symmetric')
    if any(s.simplify(v) != 0 for v in K - K.T):
        raise ValueError('Kinetic matrix must be symmetric')
    det = s.simplify(g.det())
    if det == 0:
        raise ValueError('Metric must be nondegenerate')
    gi = g.inv()
    vol = s.sqrt(-det) if volume_density is None else s.sympify(volume_density)
    if s.simplify(vol) == 0:
        raise ValueError('Volume density cannot be zero')
    substitution = dict(zip(field_symbols, map(s.sympify, field_values)))
    def sub(expr: s.Expr) -> s.Expr:
        return s.sympify(expr).subs(substitution, simultaneous=True)
    Kx, Px = K.applyfunc(sub), sub(potential)
    grad = s.Matrix(n, d, lambda I, mu: s.diff(field_values[I], coords[mu]))
    inner = grad * gi * grad.T
    L = s.simplify(-sum(Kx[I,J] * inner[I,J] for I in range(n) for J in range(n))/2 - Px)
    T = (grad.T * Kx * grad + g * L).applyfunc(s.simplify)
    equations=[]
    for I in range(n):
        div = sum(s.diff(vol * sum(Kx[I,J] * gi[mu,nu] * grad[J,nu]
                                  for J in range(n) for nu in range(d)), coords[mu])
                  for mu in range(d)) / vol
        correction = sum(sub(s.diff(K[J,K_], field_symbols[I])) * inner[J,K_]
                         for J in range(n) for K_ in range(n))/2
        equations.append(s.simplify(div-correction-sub(s.diff(potential,field_symbols[I]))))
    return ScalarSectorResult(L,s.ImmutableMatrix(T),s.ImmutableMatrix(equations),s.ImmutableMatrix(Kx))


def covariant_stress_divergence(coords: Sequence[s.Symbol], metric: s.MatrixBase,
                                stress: s.MatrixBase) -> s.ImmutableMatrix:
    """Return nabla^mu T_{mu nu}; independent coordinate calculation."""
    g=s.Matrix(metric);gi=g.inv();d=len(coords)
    if stress.shape != (d,d):
        raise ValueError('Stress tensor dimensions do not match coordinates')
    Gamma=[[[s.simplify(sum(gi[a,k]*(s.diff(g[k,c],coords[b])+s.diff(g[k,b],coords[c])
                                     -s.diff(g[b,c],coords[k])) for k in range(d))/2)
              for c in range(d)] for b in range(d)] for a in range(d)]
    return s.ImmutableMatrix([s.simplify(sum(gi[mu,rho]*(
        s.diff(stress[mu,nu],coords[rho])-sum(Gamma[k][rho][mu]*stress[k,nu]
                                           +Gamma[k][rho][nu]*stress[mu,k] for k in range(d)))
        for mu in range(d) for rho in range(d))) for nu in range(d)])
