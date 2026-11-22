from __future__ import annotations
import argparse,json
from .library import MK43Library

def main():
 p=argparse.ArgumentParser();p.add_argument('--db',required=True);s=p.add_subparsers(dest='cmd',required=True)
 a=s.add_parser('add');a.add_argument('file')
 r=s.add_parser('recover');r.add_argument('handle')
 u=s.add_parser('purge');u.add_argument('handle');u.add_argument('--reason',default='accidental_admission')
 args=p.parse_args();lib=MK43Library(args.db)
 if args.cmd=='add':
  payload=json.load(open(args.file)); receipt=lib.add_package(payload) if 'addresses' in payload else lib.add_address(payload);print(json.dumps(receipt.__dict__,indent=2))
 elif args.cmd=='recover':
  x=lib.recover(args.handle);print(json.dumps({'handle':x.handle,'resolved':x.resolved,'chunks':[c.__dict__ for c in x.chunks],'reason':x.unresolved_reason},indent=2))
 elif args.cmd=='purge':print(json.dumps(lib.purge_address(args.handle,args.reason).__dict__,indent=2))
if __name__=='__main__':main()
