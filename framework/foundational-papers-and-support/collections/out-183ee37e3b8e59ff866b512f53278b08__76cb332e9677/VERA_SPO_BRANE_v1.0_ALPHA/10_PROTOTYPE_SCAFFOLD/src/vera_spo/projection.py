from __future__ import annotations
import hashlib, json, uuid

def canonical_hash(obj) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()
    return hashlib.sha256(payload).hexdigest()

def project_spo(*, qmo_receipt: dict, profile_package: dict, parent_api_fingerprint: str, device_target: str | None = None) -> dict:
    """Illustrative π_SPO projection. Input QMO internals are represented only by a receipt in this scaffold."""
    out = {
        "instance_id": str(uuid.uuid4()),
        "parent_spo_api_fingerprint": parent_api_fingerprint,
        "profile_revision": int(profile_package.get("profile_revision", 1)),
        "rules": list(profile_package.get("rules", [])),
        "protected_events": list(profile_package.get("protected_events", [])),
        "safety_constraints": dict(profile_package.get("safety_constraints", {})),
        "device_target": device_target,
        "provenance": {
            "profile_package_fingerprint": canonical_hash(profile_package),
            "qmo_receipt_fingerprint": canonical_hash(qmo_receipt),
        },
    }
    out["fingerprint"] = canonical_hash(out)
    return out
