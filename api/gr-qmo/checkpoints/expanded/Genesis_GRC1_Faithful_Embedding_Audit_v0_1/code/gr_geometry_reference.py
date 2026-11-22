"""Exact local tensor translator for an evaluated smooth Genesis-GR representation.

This is not a generator of native Q_R data, a proof assistant, or a global-domain
solver. The smooth metric, frame anchor, and flux data must be supplied. Native
connection coefficients are evaluated from the source's zero-torsion and metric-
compatibility requirements via Koszul's identity, not by relabelling a GR result.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable, Mapping, Sequence
import sympy as sp


def simp(x: sp.Expr) -> sp.Expr:
    return sp.simplify(x)


def mat_simp(m: sp.MatrixBase) -> sp.ImmutableMatrix:
    return sp.ImmutableMatrix(m.applyfunc(simp))


def zero(x: sp.Expr) -> bool:
    """Conservative exact check: UNKNOWN does not count as zero."""
    return simp(x) == 0


class UnresolvedNativeAttachment(RuntimeError):
    """Raw native data have no recovered evaluable Q_R/flux/anchor adapter."""


def attach_raw_native_state(state: object) -> object:
    raise UnresolvedNativeAttachment(
        'The recovered source names Q_R and selected lifts but this package does '
        'not implement their action on raw native states. Supply evaluated smooth '
        'records with independent provenance; do not treat this as a native inverse.'
    )


@dataclass(frozen=True)
class Tensor:
    """Tensor components. +1 is contravariant, -1 is covariant; rank zero allowed."""
    n: int
    variance: tuple[int, ...]
    values: Mapping[tuple[int, ...], sp.Expr]

    def __post_init__(self) -> None:
        if self.n < 1 or any(v not in (1, -1) for v in self.variance):
            raise ValueError('Invalid dimension or variance')
        for index in self.values:
            if len(index) != len(self.variance) or any(i < 0 or i >= self.n for i in index):
                raise ValueError('Component index out of range')

    def __getitem__(self, key: tuple[int, ...] | int) -> sp.Expr:
        if isinstance(key, int):
            if self.rank != 1: raise ValueError("Integer indexing requires rank one")
            key = (key,)
        return self.values.get(tuple(key), sp.S.Zero)

    @property
    def rank(self) -> int:
        return len(self.variance)

    @classmethod
    def from_matrix(cls, m: sp.MatrixBase, variance: tuple[int, int]) -> 'Tensor':
        if m.rows != m.cols:
            raise ValueError('Expected square component matrix')
        return cls(m.rows, variance, {(i, j): sp.sympify(m[i, j])
                                     for i in range(m.rows) for j in range(m.cols)
                                     if m[i, j] != 0})

    def matrix(self) -> sp.ImmutableMatrix:
        if self.rank != 2:
            raise ValueError('Only a rank-two tensor has this matrix view')
        return sp.ImmutableMatrix(self.n, self.n, lambda i, j: self[i, j])

    def scale(self, factor: sp.Expr) -> 'Tensor':
        return Tensor(self.n, self.variance, {i: simp(factor*v) for i, v in self.values.items()})

    def add(self, other: 'Tensor') -> 'Tensor':
        if (self.n, self.variance) != (other.n, other.variance):
            raise ValueError('Tensor addition requires equal types')
        keys = set(self.values) | set(other.values)
        return Tensor(self.n, self.variance, {i: simp(self[i]+other[i]) for i in keys})

    def product(self, other: 'Tensor') -> 'Tensor':
        if self.n != other.n:
            raise ValueError('Dimension mismatch')
        return Tensor(self.n, self.variance+other.variance,
                      {a+b: simp(x*y) for a,x in self.values.items() for b,y in other.values.items()})

    def contract(self, axis1: int, axis2: int) -> 'Tensor':
        if axis1 == axis2 or not (0 <= axis1 < self.rank and 0 <= axis2 < self.rank):
            raise ValueError('Invalid contraction axes')
        if self.variance[axis1] == self.variance[axis2]:
            raise ValueError('Use a metric to raise/lower before contracting equal variances')
        keep = [i for i in range(self.rank) if i not in (axis1, axis2)]
        result = {}
        for out in product(range(self.n), repeat=len(keep)):
            total = sp.S.Zero
            for k in range(self.n):
                idx = [0]*self.rank
                for axis, value in zip(keep, out): idx[axis] = value
                idx[axis1] = idx[axis2] = k
                total += self[tuple(idx)]
            result[out] = simp(total)
        return Tensor(self.n, tuple(self.variance[i] for i in keep), result)

    def equals(self, other: 'Tensor') -> bool:
        return ((self.n, self.variance) == (other.n, other.variance)
                and all(zero(self[i]-other[i]) for i in set(self.values)|set(other.values)))


@dataclass(frozen=True)
class Frame:
    """An invertible smooth anchor A: native-frame vectors -> coordinate vectors.

    domain is a record of assumed local conditions, not a machine proof that those
    conditions hold on a global set. Global charts/transition functions are separate.
    """
    coordinates: tuple[sp.Symbol, ...]
    A: sp.ImmutableMatrix
    domain: tuple[str, ...]

    def __post_init__(self) -> None:
        n = len(self.coordinates)
        if self.A.shape != (n, n): raise ValueError('Anchor dimension mismatch')
        if zero(self.A.det()): raise ValueError('Singular anchor: no two-sided translation')
        if not self.domain: raise ValueError('Record the admitted local domain explicitly')

    @property
    def n(self) -> int: return len(self.coordinates)

    @property
    def B(self) -> sp.ImmutableMatrix: return mat_simp(self.A.inv())

    def directional(self, a: int, f: sp.Expr) -> sp.Expr:
        return simp(sum(self.A[mu,a]*sp.diff(f,x) for mu,x in enumerate(self.coordinates)))

    def structure(self) -> Tensor:
        """f^c_ab, defined by [e_a,e_b] = f^c_ab e_c under the anchor."""
        n=self.n; B=self.B; out={}
        for c,a,b in product(range(n), repeat=3):
            out[c,a,b] = simp(sum(B[c,nu]*(self.directional(a,self.A[nu,b])
                              -self.directional(b,self.A[nu,a])) for nu in range(n)))
        return Tensor(n,(1,-1,-1),out)

    def translate(self, tensor: Tensor, *, to_gr: bool=True) -> Tensor:
        if tensor.n != self.n: raise ValueError('Tensor/frame dimension mismatch')
        current = tensor
        B=self.B
        # Transform one slot at a time; avoids a dense 2r-index intermediate.
        for axis, var in enumerate(tensor.variance):
            m = (self.A if var==1 else B.T) if to_gr else (B if var==1 else self.A.T)
            out={}
            for idx in product(range(self.n), repeat=tensor.rank):
                v=sp.S.Zero
                for j in range(self.n):
                    old=list(idx); old[axis]=j
                    v += m[idx[axis],j]*current[tuple(old)]
                v=simp(v)
                if v != 0: out[idx]=v
            current=Tensor(self.n,tensor.variance,out)
        return current


def koszul_native(frame: Frame, k: sp.MatrixBase) -> tuple[sp.ImmutableMatrix,...]:
    """C[a][c,b] means C_{e_a} e_b = C[a][c,b] e_c.

    This evaluates the source's smooth torsion-free metric-compatible restriction
    using the native metric and native-frame directional derivatives/brackets.
    It does not implement selection among the original finite admissible lifts.
    """
    n=frame.n
    if k.shape != (n,n) or any(not zero(k[i,j]-k[j,i]) for i in range(n) for j in range(n)):
        raise ValueError('Metric must be symmetric and correctly typed')
    if zero(k.det()): raise ValueError('Degenerate metric')
    ki=k.inv(); f=frame.structure(); C=[]
    for a in range(n):
        m=sp.zeros(n)
        for d,b in product(range(n), repeat=2):
            total=sp.S.Zero
            for c in range(n):
                rhs=frame.directional(a,k[b,c])+frame.directional(b,k[c,a])-frame.directional(c,k[a,b])
                rhs += sum(-k[a,j]*f[j,b,c]+k[b,j]*f[j,c,a]+k[c,j]*f[j,a,b] for j in range(n))
                total += ki[d,c]*rhs/2
            m[d,b]=simp(total)
        C.append(sp.ImmutableMatrix(m))
    return tuple(C)


def christoffel(coordinates: Sequence[sp.Symbol], g: sp.MatrixBase) -> tuple[sp.ImmutableMatrix,...]:
    """Independent coordinate-metric route: Gamma[mu][rho,sigma]."""
    n=len(coordinates); inv=g.inv(); out=[]
    if zero(g.det()): raise ValueError('Degenerate metric')
    for mu in range(n):
        m=sp.zeros(n)
        for r,s in product(range(n), repeat=2):
            m[r,s]=simp(sum(inv[r,l]*(sp.diff(g[l,s],coordinates[mu])
                        +sp.diff(g[l,mu],coordinates[s])-sp.diff(g[mu,s],coordinates[l]))/2
                        for l in range(n)))
        out.append(sp.ImmutableMatrix(m))
    return tuple(out)


def native_connection_to_gr(frame: Frame, C: Sequence[sp.MatrixBase]) -> tuple[sp.ImmutableMatrix,...]:
    n=frame.n; A=frame.A; B=frame.B
    return tuple(mat_simp(A*sum((B[a,mu]*C[a] for a in range(n)),sp.zeros(n))*B
                         -A.diff(frame.coordinates[mu])*B) for mu in range(n))


def gr_connection_to_native(frame: Frame, Gamma: Sequence[sp.MatrixBase]) -> tuple[sp.ImmutableMatrix,...]:
    n=frame.n; A=frame.A; B=frame.B
    Cmu=[B*Gamma[mu]*A+B*A.diff(frame.coordinates[mu]) for mu in range(n)]
    return tuple(mat_simp(sum((A[mu,a]*Cmu[mu] for mu in range(n)),sp.zeros(n))) for a in range(n))


def curvature_native(frame: Frame, C: Sequence[sp.MatrixBase]) -> Tensor:
    n=frame.n; f=frame.structure(); out={}
    for a,b in product(range(n), repeat=2):
        m=sp.Matrix(n,n,lambda c,d:frame.directional(a,C[b][c,d])-frame.directional(b,C[a][c,d]))
        m += C[a]*C[b]-C[b]*C[a]-sum((f[e,a,b]*C[e] for e in range(n)),sp.zeros(n))
        for c,d in product(range(n),repeat=2):
            v=simp(m[c,d])
            if v!=0: out[c,d,a,b]=v
    return Tensor(n,(1,-1,-1,-1),out)


def curvature_gr(coordinates: Sequence[sp.Symbol], Gamma: Sequence[sp.MatrixBase]) -> Tensor:
    n=len(coordinates); out={}
    for mu,nu in product(range(n),repeat=2):
        m=Gamma[nu].diff(coordinates[mu])-Gamma[mu].diff(coordinates[nu])+Gamma[mu]*Gamma[nu]-Gamma[nu]*Gamma[mu]
        for a,b in product(range(n),repeat=2):
            v=simp(m[a,b])
            if v!=0: out[a,b,mu,nu]=v
    return Tensor(n,(1,-1,-1,-1),out)


def covariant_derivative(tensor: Tensor, connection: Sequence[sp.MatrixBase],
                         derivative: Callable[[int,sp.Expr],sp.Expr]) -> Tensor:
    n=tensor.n; rank=tensor.rank; out={}
    for idx in product(range(n),repeat=rank):
        for a in range(n):
            value=derivative(a,tensor[idx])
            for slot,var in enumerate(tensor.variance):
                for j in range(n):
                    old=list(idx);old[slot]=j
                    value += (connection[a][idx[slot],j] if var==1 else -connection[a][j,idx[slot]])*tensor[tuple(old)]
            value=simp(value)
            if value!=0:out[idx+(a,)]=value
    return Tensor(n,tensor.variance+(-1,),out)


def scalar_and_einstein(riemann: Tensor, metric: sp.MatrixBase) -> tuple[Tensor,sp.Expr,Tensor]:
    ric=riemann.contract(0,2); inv=metric.inv(); n=metric.rows
    scalar=simp(sum(inv[a,b]*ric[a,b] for a in range(n) for b in range(n)))
    ein=ric.add(Tensor.from_matrix(metric,(-1,-1)).scale(-scalar/2))
    return ric,scalar,ein


def flux_to_source(normals: sp.MatrixBase, flux: sp.MatrixBase) -> sp.ImmutableMatrix:
    if normals.rows!=normals.cols or flux.shape!=normals.shape:
        raise ValueError('Expected matching square directional matrices')
    if zero(normals.det()): raise ValueError('Independent conormals are required')
    t=mat_simp(flux*normals.inv())
    if any(not zero(t[i,j]-t[j,i]) for i in range(t.rows) for j in range(t.cols)):
        raise ValueError('Source is not symmetric in the declared non-spin sector')
    return t


def validate_selected_connection(frame: Frame, k: sp.MatrixBase,
                                 C: Sequence[sp.MatrixBase]) -> None:
    """Check the selected smooth coefficients, not just generate convenient ones."""
    expected=koszul_native(frame,k)
    if len(C)!=frame.n or any(not zero(C[a][i,j]-expected[a][i,j])
                              for a,i,j in product(range(frame.n),repeat=3)):
        raise ValueError('Selected connection fails the admitted GR-sector restriction')

@dataclass(frozen=True)
class EvaluatedGenesisEndpoint:
    """Evaluated local fields, not the raw (D,R,R,B,H,chi,C,P) native state.

    The frame and probe basis are declared representation context. Recovering this
    record never claims to recover any omitted native History or Bandwidth.
    """
    frame: Frame
    metric: sp.ImmutableMatrix
    selected_connection: tuple[sp.ImmutableMatrix,...]
    probe_normals: sp.ImmutableMatrix
    probe_flux: sp.ImmutableMatrix
    cosmological_constant: sp.Expr
    coupling: sp.Expr
    retained_data: tuple[tuple[str,str], ...] = ()

    def to_gr(self) -> 'GREndpoint':
        validate_selected_connection(self.frame,self.metric,self.selected_connection)
        g=self.frame.translate(Tensor.from_matrix(self.metric,(-1,-1))).matrix()
        source_native=flux_to_source(self.probe_normals,self.probe_flux)
        source=self.frame.translate(Tensor.from_matrix(source_native,(1,1))).matrix()
        gamma=native_connection_to_gr(self.frame,self.selected_connection)
        expected=christoffel(self.frame.coordinates,g)
        if any(not zero(gamma[a][b,c]-expected[a][b,c])
               for a,b,c in product(range(self.frame.n),repeat=3)):
            raise ValueError('Differential compatibility failed')
        return GREndpoint(self.frame,g,source,self.probe_normals,
                          self.cosmological_constant,self.coupling,self.retained_data)


@dataclass(frozen=True)
class GREndpoint:
    """Metric/source presentation with fixed representation context and retained data."""
    frame: Frame
    metric: sp.ImmutableMatrix
    source_upper: sp.ImmutableMatrix
    probe_normals: sp.ImmutableMatrix
    cosmological_constant: sp.Expr
    coupling: sp.Expr
    retained_data: tuple[tuple[str,str], ...] = ()

    def to_genesis_endpoint(self) -> EvaluatedGenesisEndpoint:
        k=self.frame.translate(Tensor.from_matrix(self.metric,(-1,-1)),to_gr=False).matrix()
        t=self.frame.translate(Tensor.from_matrix(self.source_upper,(1,1)),to_gr=False).matrix()
        gamma=christoffel(self.frame.coordinates,self.metric)
        C=gr_connection_to_native(self.frame,gamma)
        validate_selected_connection(self.frame,k,C)
        return EvaluatedGenesisEndpoint(self.frame,k,C,self.probe_normals,
                                        mat_simp(t*self.probe_normals),
                                        self.cosmological_constant,self.coupling,self.retained_data)
