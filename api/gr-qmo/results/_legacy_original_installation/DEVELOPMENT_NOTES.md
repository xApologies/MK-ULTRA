# Installation development record

An initial demonstration reported a false symbolic codec comparison: SymPy kept
sinh(log(1+sqrt(2))) unevaluated rather than simplifying it to 1. The newly written
metric decoder now explicitly rewrites sinh in exponential form before exact
simplification. The complete metric-code round trip passes after that change.
The original translator and checkpoint code were not modified.

The original API does not list the separately supplied v3.0 `@mass` object in its
2,384-handle array. It has been imported as a separately labeled source object,
not fabricated as a historical native API entry. All dependencies resolve.

Source metadata differences (RP42 runtime pointer and stored count fields) are
recorded in registry/BASE_METADATA_NOTES.json. Original source bytes remain intact.
