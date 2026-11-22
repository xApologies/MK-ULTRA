"""Verify checkpoint file integrity. This is not mathematical validation."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for record in manifest['files']:
    p=root/record['path']
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=record['sha256']:
        raise SystemExit('Integrity failure: '+record['path'])
print(f"Verified {len(manifest['files'])} payload hashes.")
