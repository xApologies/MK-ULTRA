# Engine Query Contract v1.1

The engine-facing object remains exactly one QMO: `@stonewake_physics`.

## Calls

- `search(term)` — precision ladder: exact -> phrase -> token AND -> OR fallback.
- `object(handle)` — inspect namespaced object records.
- `equations(query|owner|domain)` — retrieve equations.
- `route(source,target)` — shortest directed route over the typed dependency fabric.
- `local_qmo([concepts...], depth)` — resolve concepts and expand a bounded local dependency neighborhood.
- `templates([name])` — inspect derived child-QMO templates.
- `derive(name)` — materialize a bounded LocalPhysicsQMO for a known template such as `plasma_channel` or `poison_cloud`.

## Runtime rule

The master QMO owns mathematics and routing. A derived LocalPhysicsQMO owns only the mathematics needed for one request. The fixed-step physics kernel owns numerical integration. Readout maps solved state to Metal/audio/haptics.
