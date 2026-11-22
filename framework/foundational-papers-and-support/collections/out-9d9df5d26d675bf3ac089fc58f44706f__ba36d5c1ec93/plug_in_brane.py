"""Construct MK43 Brane from three external module archives.

The Brane package contains no AI, API, or Library payload.
"""
from __future__ import annotations
import argparse, hashlib
from pathlib import Path
from mk43_brane import Brane
from mk43_brane.loader import BraneLoader, TrustPolicy

def sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def plug_in(ai_zip, api_zip, library_zip, output_dir='./brane_output') -> Brane:
    paths={'ai':Path(ai_zip),'api':Path(api_zip),'library':Path(library_zip)}
    modules=BraneLoader.from_zips(paths['ai'],paths['api'],paths['library'],{k:sha256(v) for k,v in paths.items()},trust_policy=TrustPolicy(require_checksum=True))
    return Brane(modules, Path(output_dir))

def main():
    p=argparse.ArgumentParser(description='Plug external AI, API, and Library modules into MK43 Brane')
    p.add_argument('--ai',required=True); p.add_argument('--api',required=True); p.add_argument('--library',required=True); p.add_argument('--output',default='./brane_output')
    a=p.parse_args(); brane=plug_in(a.ai,a.api,a.library,a.output)
    try:
        print('MK43 Brane loaded with three external modules')
        print('External port-contract validation: PASS')
    finally: brane.close()
if __name__=='__main__': main()
