# MK43 Dark Matter - Recovered Source Spine

Mode: source-preserving recovery. This file maps recovered LaTeX; it does not reconcile historical formulations with later API/TOME canon.

## A. Direct historical dark-matter statements

### `0.tex` - Chapter 0 / The Black Rainbow
Recovered source framing:
- dark matter is described as invisible structure / the silent bulk of quantum geometry;
- the ER-foam lattice is described as an everywhere-present microscopic bridge scaffold;
- the source explicitly contrasts ordinary stress-energy with a deeper combinatorial curvature layer;
- the source calls this layer the "load-bearing geometry of reality";
- the Black Rainbow is described as a geometric spectrum of internal energy densities and is explicitly associated with dark matter.

### `A/block_A.tex`
Recovered source framing:
- "invisible mass" is described as inertia of the worldweave / cost of deforming the relational pattern;
- bead lattices encode curvature, energy density, and phase;
- dark matter is described as effective inertia of highly constrained ER-foam lattice regions;
- some ER-foam phases are described as dark, invisible scaffolding.

These are historical/source formulations, not silently promoted here.

## B. Core mathematical chain recovered from the canonical LaTeX

### 1. Field content and metric decomposition
From Chapters 2, 4, 5, 6:

```latex
\bm{\chi}(x) = (\chi_1, \dots, \chi_7)
```

```latex
W_{ij} \ge 0,\qquad W_{ij}=W_{ji}
```

```latex
g_{\mu\nu} 
= 
g^{(0)}_{\mu\nu}
+ g^{(\tau)}_{\mu\nu}
+ g^{(\chi)}_{\mu\nu}
+ g^{(ER)}_{\mu\nu}
```

```latex
g^{(ER)}_{\mu\nu} = \lambda 
\sum_{i,j} W_{ij}\, \xi^{(i)}_\mu \xi^{(j)}_\nu
```

### 2. Chromatic stress-energy
From Chapter 5:

```latex
\mathcal{L}_\chi
=
-\frac{1}{2}G^{ab}(\bm{\chi})\, g^{\mu\nu}\partial_\mu\chi_a\partial_\nu\chi_b
- U(\bm{\chi})
```

```latex
T^{(\chi)}_{\mu\nu}
=
G^{ab}\partial_\mu\chi_a\partial_\nu\chi_b
- g_{\mu\nu}\mathcal{L}_\chi
```

### 3. Explicit ER-sector Einstein source
From `tome_mk43_skeleton/tome_mk43.tex`:

```latex
S_{\mathrm{tot}} =
\frac{1}{16\pi G}\int d^4x \sqrt{-g}\, R
+ S_\tau + S_\chi + S_{ER} + S_{\mathrm{matter}}
```

```latex
G_{\mu\nu}
=
8\pi G\, \left(
T^{(\tau)}_{\mu\nu}
+ T^{(\chi)}_{\mu\nu}
+ T^{(ER)}_{\mu\nu}
+ T^{\mathrm{(matter)}}_{\mu\nu}
\right)
```

The same source says coarse-grained ER-connectivity variations induce metric corrections `g^(ER)_{mu nu}` and may be modeled phenomenologically by ER density and its gradients or by integrating out microscopic ER degrees of freedom.

### 4. Cosmological ER energy density
From Chapter 11:

```latex
H^2 =
\frac{8\pi G}{3}\left(\rho_\tau + \rho_\chi + \rho_{ER} + \rho_{\mathrm{m}}\right)
- \frac{k}{a^2}
```

```latex
\frac{\ddot{a}}{a} =
-\frac{4\pi G}{3}\left(
\rho_\tau + \rho_\chi + \rho_{ER} + \rho_{\mathrm{m}}
+ 3p_\tau + 3p_\chi + 3p_{ER} + 3p_{\mathrm{m}}
\right)
```

Chapter 14 introduces a coarse-grained ER density evolution:

```latex
\dot{\rho}_{ER}^{\mathrm{(eff)}}
=
\mathcal{F}\big(\rho_{ER}^{\mathrm{(eff)}}, \rho_\chi, \rho_\tau, a(t)\big)
```

### 5. Structure formation
From Chapter 32:

```latex
\delta \rho_\chi \approx G^{ab}\dot{\chi}_{a,0}\,\delta\dot{\chi}_b + \partial_a U(\bm{\chi}_0)\,\delta\chi_a
```

The chapter explicitly says these fluctuations seed density perturbations, are processed by gravitational dynamics, and can modify the power spectrum relative to standard LambdaCDM; ER connectivity can generate non-Gaussian correlations.

From Chapter 33:

```latex
\mathcal{W}_{IJ} \sim \langle W_{ij} \rangle_{\text{coarse-grained}}
```

The source maps the cosmic web (galaxies, clusters, filaments, voids) to a coarse-grained imprint of the underlying ER network.

### 6. Galactic observables
From Chapter 37:

```latex
\Phi_{\mathrm{eff}}(r)=\Phi_{\mathrm{GR}}(r)+\delta\Phi_{ER}(r)
```

```latex
v^2(r)=r\,\partial_r\Phi_{\mathrm{eff}}(r)
```

Chapter 40 explicitly lists "Rotation curve deviations linked to ER density" as a testable prediction.

### 7. Large-scale galactic structure
From Chapter 56:

```latex
\nabla_i \tau_{\mathrm{gal}} = \Omega\, \epsilon_{ij} x^j
```

```latex
\delta\rho = \sum_a \lambda_a \chi_a
```

From Chapter 57:

```latex
W_{IJ}^{\mathrm{gal}} = \exp\!\left(-\frac{d_{IJ}}{L_{\mathrm{gal}}}\right)
```

The supplied spine identifies Chapters 56-60 as a dark-matter-adjacent galactic/universe-scale recovery region.

## C. Additional explicit dark-matter targets whose bodies are absent here

### `MONOGRAPH 1/mk43_ultra_monograph.tex`
The monograph abstract explicitly says MK43 realizes dark matter as an effective gravitational imprint of an ER bridge network. Its chapter spine contains:
- `ER Bridges and Dark Matter Geometry`
- `Dark Matter Formalization`

However, this archived monograph file contains chapter placeholders rather than the full bodies of those two chapters.

### `THE_TOME/block_appendices.tex`
The appendix spine contains:
- `Dark Matter Bridges and Transport`
- `Bridge Metric Ansatz`
- `Helicon Transport Along Bridges`
- `Effective Medium Approximations`

This file preserves the appendix targets/headings, not their missing full derivations.

## D. Recovery interpretation

The recovered LaTeX supports a historical mathematical program in which:

```text
microscopic ER adjacency / chromatic density
    -> coarse-grained ER density / metric correction
    -> stress-energy / Einstein-sector contribution
    -> structure formation and cosmic-web imprint
    -> ER-modified galactic potential
    -> rotation-curve and lensing observables
```

This is a source map only. Later DM 2.2 / API 4.3 / Live Landscape status and promotion rulings remain separate.
