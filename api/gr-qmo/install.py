#!/usr/bin/env python3
"""Install the complete GR/QMO release into a new versioned subdirectory.

No network, pip, Git, existing canonical-file edits, or destructive updates.
Existing matching installations are verified; differing content is refused.
"""
from pathlib import Path
import argparse,json,sys,tempfile,shutil,os
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from tools.integrity import verify


def install(target: Path, dry_run: bool=False) -> dict:
    source=verify(ROOT)
    if not source['ok']:raise ValueError('Source verification failed: '+repr(source['failures']))
    target=target.expanduser().resolve()
    destination=target/'integrations'/'gr_qmo'/'1.0.0'
    if destination==ROOT or ROOT in destination.parents:
        raise ValueError('Install destination must not be inside the source package')
    for p in [target/'integrations',target/'integrations/gr_qmo',destination]:
        if p.is_symlink():raise ValueError('Refusing an installation through a symbolic-link destination')
    if destination.exists():
        existing=verify(destination)
        if not existing['ok'] or (destination/'MANIFEST.json').read_bytes()!=(ROOT/'MANIFEST.json').read_bytes():
            raise FileExistsError('The versioned destination contains different or modified content; nothing was overwritten')
        return {'status':'already_installed_verified','destination':str(destination),'modified_existing_files':False,'verification':existing}
    if dry_run:
        return {'status':'dry_run_verified','destination':str(destination),'action':'copy this release only; no Git commit or canonical overwrite','source_verification':source}
    destination.parent.mkdir(parents=True,exist_ok=True)
    staging=Path(tempfile.mkdtemp(prefix='.mk43-staging-',dir=destination.parent))
    try:
        payload=staging/'payload'
        shutil.copytree(ROOT,payload,ignore=shutil.ignore_patterns('__pycache__','*.pyc','reruns'))
        checked=verify(payload)
        if not checked['ok']:raise ValueError('Staged installation failed verification')
        if destination.exists():raise FileExistsError('Destination appeared during installation; refusing overwrite')
        os.rename(payload,destination)
    finally:shutil.rmtree(staging,ignore_errors=True)
    return {'status':'installed_verified','destination':str(destination),'modified_existing_files':False,'verification':checked,'remote_writes':False}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--target',required=True,type=Path);ap.add_argument('--dry-run',action='store_true');args=ap.parse_args()
    try:result=install(args.target,args.dry_run)
    except Exception as exc:
        print(json.dumps({'status':'not_installed','error':str(exc),'overwrites_performed':False},indent=2));return 1
    print(json.dumps(result,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
