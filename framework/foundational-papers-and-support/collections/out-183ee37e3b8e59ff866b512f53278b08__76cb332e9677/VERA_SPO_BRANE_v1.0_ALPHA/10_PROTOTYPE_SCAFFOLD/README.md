# Prototype Scaffold

This scaffold proves only the control-plane safety semantics:
- unknown → preserve;
- low confidence → preserve;
- protected event → preserve;
- unsupported transform → preserve;
- user override → preserve;
- compiler rejects ordinary transformation rules for protected classes.

It intentionally contains no live audio capture, classifier, DSP, clinical thresholds, or medical behavior.

Run:

```bash
python -m pytest -q
python examples/demo.py
```
