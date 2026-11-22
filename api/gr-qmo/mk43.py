#!/usr/bin/env python3
"""Local query surface for the complete active GR/QMO. No network access."""
from pathlib import Path
import argparse,json,sqlite3,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('status');sub.add_parser('verify')
    obj=sub.add_parser('object');obj.add_argument('handle');obj.add_argument('--limit',type=int,default=12)
    find=sub.add_parser('find');find.add_argument('text');find.add_argument('--limit',type=int,default=30)
    sub.add_parser('demo')
    args=parser.parse_args()
    if args.command=='verify':
        from tools.integrity import verify
        result=verify(ROOT);print(json.dumps(result,indent=2));return 0 if result['ok'] else 1
    if args.command=='demo':
        from examples.evaluated_handoff import main as run
        run();return 0
    con=sqlite3.connect((ROOT/'registry/GR_QMO.sqlite').as_uri()+'?mode=ro',uri=True);con.row_factory=sqlite3.Row
    if args.command=='status':
        result={'entrypoints':json.loads((ROOT/'registry/ENTRYPOINTS.json').read_text()),
          'registry':{row['key']:json.loads(row['value']) for row in con.execute('SELECT * FROM meta')},
          'active_checkpoints':[dict(r) for r in con.execute("SELECT id,activation,scope FROM checkpoints WHERE activation='active'")],
          'installation_results':json.loads((ROOT/'results/INSTALLATION_VALIDATION.json').read_text()) if (ROOT/'results/INSTALLATION_VALIDATION.json').exists() else 'build in progress'}
    elif args.command=='find':
        term='%'+args.text+'%';limit=max(1,min(args.limit,200))
        result=[dict(r) for r in con.execute('SELECT handle,kind,title,status,source FROM objects WHERE handle LIKE ? OR title LIKE ? ORDER BY handle LIMIT ?',(term,term,limit))]
    else:
        row=con.execute('SELECT * FROM objects WHERE handle=?',(args.handle,)).fetchone()
        if not row:
            print(json.dumps({'error':'unknown handle','handle':args.handle}));return 2
        result=dict(row); result['hypotheses']=json.loads(result['hypotheses']);limit=max(1,min(args.limit,200))
        result['outgoing']=[dict(r) for r in con.execute('SELECT relation,target,origin FROM edges WHERE source=? ORDER BY origin,relation,target LIMIT ?',(args.handle,limit))]
        result['incoming']=[dict(r) for r in con.execute('SELECT source,relation,origin FROM edges WHERE target=? ORDER BY origin,relation,source LIMIT ?',(args.handle,limit))]
        result['source_locations']=[dict(r) for r in con.execute('SELECT source,line FROM occurrences WHERE handle=? ORDER BY line LIMIT ?',(args.handle,limit))]
        result['truncation_limit']=limit
    print(json.dumps(result,indent=2,ensure_ascii=False));con.close();return 0
if __name__=='__main__':raise SystemExit(main())
