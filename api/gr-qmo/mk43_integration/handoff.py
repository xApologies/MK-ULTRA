"""Compose a supplied original Time-Shell output with the evaluated GR translator.

No default microscopic Pi_T, continuity generator, source action or clock is
invented. Signature/regularity records distinguish a declaration from a proof.
The imported translator.py is a byte-identical prior implementation.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Sequence
import json
import sympy as s
from .translator import (Frame, GREndpoint, EvaluatedGenesisEndpoint,
    christoffel, curvature_gr, scalar_and_einstein, mat_simp)


class MissingNativeOperator(ValueError):
    pass


def zero_matrix(m: s.MatrixBase) -> bool:
    return all(s.simplify(v) == 0 for v in m)


def symmetric4(m: Any, name: str) -> s.ImmutableMatrix:
    m = s.ImmutableMatrix(m)
    if m.shape != (4, 4) or not zero_matrix(m-m.T):
        raise ValueError(f'{name} must be an exactly symmetric 4x4 matrix')
    if any(v.is_real is False or v.has(s.nan, s.zoo, s.oo, -s.oo) for v in m):
        raise ValueError(f'{name} contains non-real or non-finite components')
    return m


def _scope_status(g: s.MatrixBase, declared_domain: str) -> dict[str, str]:
    if not declared_domain.strip():
        raise ValueError('A domain/smoothness/signature scope record is required')
    determinant = s.simplify(g.det())
    if determinant == 0 or determinant.is_zero is True:
        raise ValueError('Degenerate metric: inverse representation is undefined')
    # Exact checks where possible; an undecidable sign is never recorded as proof.
    signs = []
    eigen = list(g.diagonal()) if g.is_diagonal() else []
    if not eigen and not g.free_symbols:
        for value, count in g.eigenvals().items():
            eigen.extend([s.simplify(value)]*count)
    for v in eigen:
        signs.append(-1 if v.is_negative is True else 1 if v.is_positive is True else 0)
    if len(signs) == 4 and 0 not in signs:
        if signs.count(-1) != 1:
            raise ValueError('Metric does not have the declared (-,+,+,+) signature')
        signature = 'exact_sign_check_in_symbol_assumptions'
    else:
        signature = 'conditional_on_supplied_domain_witness_not_machine_proved'
    return {'signature': signature,
            'nondegeneracy': 'symbolically_proved' if determinant.is_zero is False else 'conditional_on_supplied_domain_witness',
            'domain': declared_domain}


@dataclass(frozen=True)
class AttachedHandoff:
    """The preserved readable packet and its evaluated Genesis representative."""
    readable: GREndpoint
    genesis: EvaluatedGenesisEndpoint
    assumptions: Mapping[str, str]
    source_reference: str

    def roundtrip(self) -> GREndpoint:
        return self.genesis.to_gr()

    def geometry(self) -> dict[str, Any]:
        g = self.readable.metric
        gamma = christoffel(self.readable.frame.coordinates, g)
        riemann = curvature_gr(self.readable.frame.coordinates, gamma)
        ricci, scalar, einstein = scalar_and_einstein(riemann, g)
        t_lower = mat_simp(g*self.readable.source_upper*g.T)
        residual = mat_simp(einstein.matrix() + self.readable.cosmological_constant*g
                            - self.readable.coupling*t_lower)
        return {'connection': gamma, 'riemann': riemann, 'ricci': ricci,
                'scalar_curvature': scalar, 'einstein': einstein,
                'source_lower': t_lower, 'field_equation_residual': residual,
                'residual_identically_zero': zero_matrix(residual),
                'scope': 'geometry of supplied shell output; not an independent native solution certificate'}


def attach_evaluated_readout(*, background: Any, perturbation: Any,
        source_upper: Any, frame: Frame, probe_normals: Any,
        cosmological_constant: Any, coupling: Any, retained_data: Mapping[str, Any],
        source_reference: str, domain_witness: str) -> AttachedHandoff:
    """All original matter/gauge/unit/boundary data are preserved, not generated.

    `source_upper` is an independent source input. In the non-spin sector it must
    be symmetric. It is never deduced by solving Einstein's equation for T.
    """
    if not source_reference.strip():
        raise ValueError('Supply provenance for the evaluated Time-Shell output')
    required = {'matter_fields', 'boundary_data', 'gauge_conventions', 'units'}
    if not required.issubset(retained_data):
        raise ValueError('Retain matter_fields, boundary_data, gauge_conventions and units explicitly')
    if frame.n != 4:
        raise ValueError('This installed readable branch has four dimensions')
    bg = symmetric4(background, 'background')
    h = symmetric4(perturbation, 'perturbation')
    g = mat_simp(bg+h)
    status = _scope_status(g, domain_witness)
    t = symmetric4(source_upper, 'source_upper')
    normals = s.ImmutableMatrix(probe_normals)
    if normals.shape != (4,4) or s.simplify(normals.det()) == 0:
        raise ValueError('Supply four independent calibrated conormals')
    kappa = s.sympify(coupling)
    if kappa.is_real is False or kappa == 0:
        raise ValueError('Supply a nonzero real gravitational coupling')
    # JSON retains a structured readout record without mutating the input mapping.
    metadata = json.dumps(retained_data, sort_keys=True, ensure_ascii=False, allow_nan=False)
    endpoint = GREndpoint(frame, g, t, normals, s.sympify(cosmological_constant), kappa,
                          (('original_retained_data_json', metadata), ('source_reference', source_reference)))
    genesis = endpoint.to_genesis_endpoint()
    return AttachedHandoff(endpoint, genesis, status, source_reference)


def attach_native_continuity(*, continuity: Any,
        time_shell: Callable[[Any], Any] | None, **kwargs: Any) -> AttachedHandoff:
    """Evaluate an explicitly supplied original shell implementation, then attach.

    A missing callback is rejected. This function does not solve for continuity
    or claim that a caller's callback has independently established MK43 physics.
    """
    if not callable(time_shell):
        raise MissingNativeOperator('No evaluated original Pi_T was supplied; no replacement is inserted')
    return attach_evaluated_readout(perturbation=time_shell(continuity), **kwargs)


def metric_code(g: Any, sigma: Any = s.S.One) -> s.ImmutableMatrix:
    sigma = s.sympify(sigma)
    if sigma.is_positive is not True:
        raise ValueError('sigma must be explicitly positive')
    return symmetric4(g, 'metric').applyfunc(lambda v:s.asinh(v/sigma))


def decode_metric_code(z: Any, sigma: Any = s.S.One) -> s.ImmutableMatrix:
    sigma = s.sympify(sigma)
    if sigma.is_positive is not True:
        raise ValueError('sigma must be explicitly positive')
    return symmetric4(z, 'metric code').applyfunc(lambda v:s.simplify(sigma*s.sinh(v).rewrite(s.exp)))


def recover_mode_on_image(S: Any, readable_mode: Any) -> s.ImmutableMatrix:
    S=s.ImmutableMatrix(S); y=s.ImmutableMatrix(readable_mode)
    if not zero_matrix(S.H*S-s.eye(S.cols)):
        raise ValueError('The supplied mode map fails its exact isometry contract')
    if y.shape != (S.rows,1):
        raise ValueError('Readable mode dimensions do not match')
    if not zero_matrix(S*S.H*y-y):
        raise ValueError('Readable mode lies outside the represented image')
    return mat_simp(S.H*y)


def fixed_point_response(A: Any, B: Any, projection_derivative: Any,
        delta_source: Any) -> s.ImmutableMatrix:
    """Finite exact realization of J (I-A)^(-1) B delta_source.

    The caller supplies evaluated derivatives; differentiability, bounded inverse
    and any further explicit source dependencies remain applicability conditions.
    """
    A=s.ImmutableMatrix(A); B=s.ImmutableMatrix(B)
    J=s.ImmutableMatrix(projection_derivative); dm=s.ImmutableMatrix(delta_source)
    if A.rows != A.cols or B.rows != A.rows or J.cols != A.rows or dm.shape != (B.cols,1):
        raise ValueError('Derivative domains/codomains do not compose')
    gate=s.eye(A.rows)-A
    if s.simplify(gate.det()) == 0:
        raise ValueError('Singular I-A: the regular response formula does not apply')
    return mat_simp(J*gate.inv()*B*dm)


def history_energy(persistence_values: Sequence[Any], epsilon_p: Any) -> s.Expr:
    if not persistence_values:
        raise ValueError('A history requires at least one state value')
    epsilon_p=s.sympify(epsilon_p)
    if epsilon_p.is_positive is not True:
        raise ValueError('The shared native persistence unit must be positive')
    return s.simplify((s.sympify(persistence_values[-1])-s.sympify(persistence_values[0]))/epsilon_p)
