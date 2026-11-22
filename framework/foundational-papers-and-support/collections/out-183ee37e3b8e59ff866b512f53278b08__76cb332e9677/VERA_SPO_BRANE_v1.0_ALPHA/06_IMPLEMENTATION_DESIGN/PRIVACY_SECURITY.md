# Privacy and Security

Design defaults:
- raw environmental audio is not retained by default;
- decision telemetry should prefer event labels/receipts over waveform capture;
- profiles are sensitive user data and require access controls;
- policy packages are fingerprinted/signed when deployment infrastructure permits;
- corrupt or unverifiable policies are not executed in transformed mode;
- canonical API and Library sources are immutable during runtime requests;
- archive/package loading inherits BRANE traversal/size/integrity defenses where applicable;
- cloud authoring is separable from on-device execution.
