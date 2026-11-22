# Acoustic Event Model

Frequency alone is not the event object.

A candidate runtime event representation is:

```text
E = (
  event_class,
  confidence,
  spectrum,
  level,
  onset,
  duration,
  impulsiveness,
  repetition,
  direction,
  motion,
  semantic_tags,
  context_tags,
  source_count,
  timestamp
)
```

Not every implementation must populate every field. Missing features must remain explicitly unknown rather than fabricated.

## Event identity

An `event_class` is a canonical API handle such as a generic class or domain-defined subtype. The 1.0 Alpha package intentionally does not prescribe a complete taxonomy.

## Overlap

A frame may contain multiple concurrent event hypotheses:

```text
Scene_t = {E_1, E_2, ..., E_n}
```

Policy resolution must not assume a single dominant source when safety-relevant events overlap.
