# Stable Runtime Identity

The Library runtime identity is permanent and release-independent.

```text
module_id:  mk43.library
package:    mk43_library
entrypoint: mk43_library:create_module
role:       library
```

Release labels such as `1.D`, `2.A`, or `4.D` are tracking metadata only.
They must never require renaming the Python package, module ID, or entry point.
