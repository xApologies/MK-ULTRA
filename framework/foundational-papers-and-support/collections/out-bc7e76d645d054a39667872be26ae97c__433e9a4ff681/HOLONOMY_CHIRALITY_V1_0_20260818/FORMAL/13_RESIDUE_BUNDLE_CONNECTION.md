# 13 — Residue Bundle Connection and Differential Interface

## 1. Canonical quantum-field handoff

The QFT bridge defines an invariant-residue fiber

```text
F_p=Inv(Pi^(-1)(p))
```

assembled into a complex bundle

```text
pi_F:F->M.
```

The bundle carries a Hermitian metric `h` and Hermitian connection

```text
nabla:Gamma(F)->Gamma(T*M tensor F)
```

with curvature

```text
R_nabla=nabla^2.
```

## 2. Standard differential geometry is inherited here

The source explicitly says no alternative differential connection/curvature theory is introduced at this layer. The novelty is application to the residue/quantum-field bundle.

## 3. Interface to pre-differential Transduction Connection

The Transduction Connection is pathwise/algebraic and can exist before a smooth differential structure is established.

The Hermitian connection is a downstream smooth-bundle structure.

Do not identify them automatically.

## 4. Candidate compatibility problem

A future interface map should ask whether selected Transduction transports are represented by parallel transport of `nabla` after projection into the residue bundle.

Candidate condition:

```text
Phi(P_gamma^Conn(x))
 ~
PT_nabla(gamma)(Phi(x))
```

for a typed representation `Phi`.

This condition is OPEN.

## 5. Curvature correspondence

If such an interface is constructed, pre-differential same-endpoint defects may acquire a differential curvature interpretation. Until then, `K_Conn` and `R_nabla` remain distinct objects.
