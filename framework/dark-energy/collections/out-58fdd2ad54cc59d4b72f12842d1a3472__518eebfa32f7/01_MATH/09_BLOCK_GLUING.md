# Byte → Block Gluing

Cover the block by compatible local chirality-byte charts \(\{U_i\}\).

Each local chart carries realized/Void partition, Resolution relation data, and History:

\[
G_i=(E_i,V_i,\rho_i,H_i).
\]

Require compatibility on overlaps:

\[
E_i|_{U_i\cap U_j}=E_j|_{U_i\cap U_j},
\]

\[
\rho_i|_{U_i\cap U_j}=\rho_j|_{U_i\cap U_j},
\]

with compatible History restriction.

Then the compatible family glues to a block-level state:

\[
\boxed{
G_B=\operatorname{Glue}\{G_i\}.
}
\]

The gluing law is closed. Particular candidate gluings may still pass or fail compatibility.

## Block parity

A chart presentation may use

\[
\epsilon(i,j,k)=i+j+k\pmod2.
\]

Then

\[
|E|=|V|=32
\]

and each elementary \(2\times2\times2\) cube inherits the local \(4/4\) byte parity rule.

Thus seed complementarity, byte half occupancy, and block half occupancy are recursively consistent.
