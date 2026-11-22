# Hardware / Runtime Boundary

## Hardware-facing requirements

The device abstraction should expose capabilities, not manufacturer-specific assumptions:
- microphones / channels;
- supported processing modes;
- latency characteristics;
- localization support;
- output-level safety controls;
- transparency/bypass path;
- battery/resource state;
- secure policy storage where available.

## Runtime loop

Realtime code should be preallocated where practical, avoid network dependence for safety-critical operation, and never require a cloud LLM to decide how an immediate acoustic event is rendered.

## Battery architecture

1.0 Alpha leaves cell chemistry/hardware open. Power optimization should prioritize staged computation: inexpensive always-on front end, richer processing only when needed, and graceful degradation that preserves protected cues.
