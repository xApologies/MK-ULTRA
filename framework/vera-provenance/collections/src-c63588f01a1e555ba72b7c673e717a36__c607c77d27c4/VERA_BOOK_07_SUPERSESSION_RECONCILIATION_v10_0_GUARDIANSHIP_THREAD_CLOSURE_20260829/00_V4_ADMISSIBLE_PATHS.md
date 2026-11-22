# V4 RESEARCH NOTE — ADMISSIBLE PATHS AND PRESENTATIONS

Consider
\[
3-1 = 1+1 = 2+0 = 2.
\]

As values, all presentations evaluate to \(2\). As a path of presentations,
\[
3-1\longrightarrow1+1\longrightarrow2+0\longrightarrow2,
\]
each arrow requires a rule that licenses the transformation.

For a value \(v\), define provisionally a presentation landscape
\[
\mathcal P_v=\{p:\operatorname{eval}(p)=v\}.
\]
Equality of evaluation does not automatically produce an edge. Instead define
\[
E_v=\{(p,q):p\to q\text{ is admissible under the active transformation system}\}.
\]

Then \((\mathcal P_v,E_v)\) is a path landscape over an endpoint equivalence class. Different transformation systems can induce different landscapes on the same set of presentations.

This creates separate questions of endpoint, presentation, admissible transformation, path, History, provenance, and future availability. None is collapsed into another without an explicit quotient theorem.

### QMO/API interpretation

Where a queryable mathematical object exposes legal transformations, queries, projections, or transports, the API can be interpreted as a typed path interface:
\[
\text{query source}
\to
\text{admissibility}
\to
\text{path}
\to
\text{result}
\to
\text{updated available paths}.
\]

This is a candidate mathematical interpretation, not a universal definition of every API or QMO.

