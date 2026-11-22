# L08 — Six-Basin / A2 Root-System Test

**Verdict:** CONDITIONAL PASS — PROVISIONAL C6 ROAD GRAMMAR

Recovered provisional Road rotation:

`kappa=(1 3 2 6 4 5)`, equivalently `kappa(k)=3k mod 7`.

Because `3^3=-1 mod 7`, the half-turn is

`kappa^3(k)=7-k`.

Hence the opposite-pair quotient is

`{1,6}, {2,5}, {3,4}`.

This matches the inverse-pair geometry required by the six A2 roots under a 180-degree root-space rotation. It does not use chirality mirror and therefore does not violate the earlier mirror/basin firewall.

A C6-equivariant bijection from the six Road states to the six A2 roots exists. For fixed orientation it has six phase choices; with orientation reversal, twelve. These choices are related by root-system automorphisms, so the structural result does not privilege a named color.

Representative map:

`1->E12, 3->E13, 2->E23, 6->E21, 4->E31, 5->E32`.

Important firewall: the scalar basin states `k/7` themselves remain six amplitudes along the recovered diagnostic chirality contrast direction; they are **not** six root vectors. The root candidate belongs to the **directed Portal/Road lane representation**.
