# 3. Localized S2 address model

Let `M^3` be the connected continuity carrier. The current standard topology is:

```text
M^3 ~= S^3.
```

For localized address `alpha`, choose a closed 3-ball neighborhood:

```text
B_alpha^3 subset S^3
```

with boundary:

```text
Sigma_alpha := boundary(B_alpha^3) ~= S^2.
```

The black-hole anchor is represented by a distinguished core/point/object `p_alpha` contained in `B_alpha^3`; it is not silently equated with the entire S2 address.

Physical assignment:

```text
Sigma_MW ~= S^2    = Milky Way localized readable address
Sigma_A  ~= S^2    = Andromeda localized readable address
```

These are local projected domains of one connected carrier rather than independent universes.

# 4. The two-address corridor theorem

Define:

```text
W^3_ab
=
S^3 \ (int B_a^3 union int B_b^3).
```

For the standard two-ball configuration:

```text
boundary(W^3_ab)
=
Sigma_a union (-Sigma_b),
```

and:

```text
W^3_ab ~= S^2 x [0,1].
```

This is established topology for the standard unknotted configuration.

The supplied Chirality Corridor document independently defines the generic open corridor as:

```text
W^3_ab ~= S^2 x [0,1]
```

with the same oriented endpoint boundary.

Therefore the previously designed corridor object and the independently reconstructed address-complement geometry coincide in topological type.

## Corollary 4.1 — Portal-as-intervening-topology

The minimal portal between two standard localized S2 addresses need not be introduced as an additional geometric object. It can be identified with the connected 3-dimensional cobordism remaining between the two address neighborhoods.

# 5. Many-address universe/carrier

For `N` disjoint localized neighborhoods:

```text
C_N^3
=
S^3 \ union_(i=1..N) int(B_i^3).
```

Then:

```text
boundary(C_N^3)
=
disjoint_union_(i=1..N) Sigma_i.
```

The carrier is one connected 3-manifold with many boundary addresses.

Important non-collapse:

```text
N = 2 standard case -> S2 x I.
N > 2 global carrier -> not generally one product cylinder.
```

Pairwise portal/corridor objects are sub-cobordisms or selected traversals within the common carrier.

# 6. Why S3 is the continuity layer

S2 has the correct dimension to be a closed local boundary of a 3-dimensional neighborhood. S3 has the correct dimension to contain many such S2 boundaries while remaining connected. This gives S3 a mathematical job not supplied by S2 alone:

```text
S2 = local address
S3 = shared connectivity / traversal carrier.
```

This also resolves a codimension issue. An S2 directly embedded in S4 is codimension two and is not the natural global separator of S4. By using:

```text
S2 subset S3 subset S4,
```

both boundary steps are codimension one at the level where they perform localization:

```text
S2 = boundary of local B3 in S3
S3 = standard global slice/boundary inside S4 construction.
```

# 7. S4 as Time-Space / Force-Sphere

Use the standard 4-sphere as ambient Time-Space topology:

```text
S4 subset R5.
```

A standard height function:

```text
h : S4 -> [-1,1]
```

has regular level sets:

```text
h^-1(t) ~= S3    for -1 < t < 1.
```

Thus S4 admits a natural description as a one-parameter family of S3 slices that collapse at the two poles; equivalently, standard S4 is the suspension of S3.

Physical interpretation:

```text
S4 = complete Time-Space organization
S3_t = continuity carrier at an ordered/readable slice
```

The parameter is not automatically identified with ordinary clock time; Time-Shell transduction determines the readable temporal interpretation.

# 8. Chirality lives on the carrier

Transduction Geometry defines a Chirality Fabric as distributed chirality/admissibility organization plus local transition/gluing data.

Model it as a bundle/field over the carrier:

```text
pi_chi : E_chi -> S3
chi in Gamma(E_chi).
```

Each localized address sees a restriction:

```text
chi_i = i_i^*(chi),
```

where:

```text
i_i : Sigma_i -> S3.
```

Therefore local galaxy/address chirality is not an independent field; it is a readable restriction of one global carrier fabric.

# 9. Global fabric realization

Transduction Geometry supplies the formal local-to-global machinery:

```text
D12 Chirality Fabric
D21 Descent-Compatible Local Family
D22 Global Realization Object G(X)
D23 Glue
D25 Gluing Witness W_G
D27 Global Realization Class [G]_G
D37 Global Fabric Realization.
```

Define:

```text
Fabr_chi := [G_chi]_G.
```

This is the invariant global carrier of compatible local chirality/admissibility data.

The operative presentation is:

```text
Op(Fabr_chi; B,R,H_t).
```

This gives exact mathematical roles to the earlier intuition that the chirality field “has a container.” The container is not a separate material object. It is the global realization class produced when compatible local fabric data glue coherently.

