# Method Contracts

## interpret(request, api)
Returns a structured `IntentModel` and resolved root candidates. Must preserve caller request ID and constraints.

## rank(candidates, context)
Returns every candidate exactly once with score, rank, and reason. Stable under identical inputs and policy version.

## continue_or_terminate(candidate, context)
Returns one of `CONTINUE`, `TERMINATE`, `DEFER`, `REJECT_INVALID` with a reason code.

## place_continuation(candidate, context)
Returns a continuation record preserving canonical handle, parent, reason, and resumable traversal receipt.

## collapse(realization, context)
Produces an ordered derived realization without mutating canonical inputs.

## validate_collapse(collapse, context)
Returns a validation receipt covering provenance, branch accounting, continuation accounting, deterministic ordering, and prohibited mutation checks.
