# Bounded Recursive Iteration / Black Rainbow Closure Architecture

## Governing retyping

- **Black Rainbow** = closed mathematical landscape / closure envelope.
- **Rainbow Road** = recursive runtime inside that landscape.
- **Möbius** = recursive presentation carrier.
- The API may iterate deeply without licensing mathematical escape from the closed landscape.

## Mathematical functional

`@bounded_recursive_iteration`

`X_(i+1) = Cl_BR(Phi_(B,R)(X_i))`, for `i < N`, with append-only History.

`N` is a finite search/iteration ceiling. It does not force `N` transitions. Early termination is canonical.

### Default stop predicates

- TARGET_RECOVERED
- CLOSED_FIXED_POINT
- OPEN_FORK / FORK
- CYCLE_DETECTED
- NO_NEW_STRUCTURE
- HARD_DEFECT
- BANDWIDTH_EXHAUSTED
- DOMAIN_BOUNDARY
- MAX_ITERATIONS

## Dependency specialization

`@bounded_dependency_crawl` applies the functional to registered QMO dependency structure and can build/query Dependency Graphs, Landscapes, and Chains.

## Consistency guard

A closed landscape bounds admissible derivation; it does not by itself prove consistency. Hard guards, typed transformations, provenance, recovery witnesses, and Closure Certificates remain mandatory.
