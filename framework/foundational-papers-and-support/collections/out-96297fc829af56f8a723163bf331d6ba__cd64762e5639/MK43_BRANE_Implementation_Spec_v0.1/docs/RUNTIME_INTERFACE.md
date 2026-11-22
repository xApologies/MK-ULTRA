# Runtime Interface

## Principle

The runtime is the fence. It transports requests and artifacts but does not manage the API, Collapse Intelligence, Library, or QMO.

## Runtime-visible operations

```text
load_brane(package)
unload_brane(brane_id)
describe_brane(brane_id)
request(brane_id, request_envelope)
cancel(request_id)
health(brane_id)
```

## Runtime-visible response

The normal response includes only:

- request identifier;
- status;
- returned artifact reference or bytes;
- artifact metadata;
- validation receipt;
- non-sensitive error information.

It excludes:

- QMO contents;
- API paths;
- library paths;
- internal prompts or reasoning traces;
- traversal internals;
- private module state.

## Push-pull contract

```text
PUSH: runtime sends a complete immutable request envelope.
PULL: runtime accepts a complete immutable response envelope.
```

The runtime must not rewrite the report. Personalization belongs to the human-facing AI after receipt, and the original artifact remains available unchanged.
