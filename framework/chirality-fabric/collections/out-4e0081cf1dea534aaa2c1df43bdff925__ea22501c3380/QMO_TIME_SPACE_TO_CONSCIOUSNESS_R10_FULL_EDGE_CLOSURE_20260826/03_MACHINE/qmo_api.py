#!/usr/bin/env python3
import sqlite3,json,argparse,os
DB=os.path.join(os.path.dirname(__file__),'QMO_TIME_SPACE_TO_CONSCIOUSNESS_R10.sqlite')
p=argparse.ArgumentParser(); sp=p.add_subparsers(dest='cmd',required=True)
sp.add_parser('stats'); a=sp.add_parser('neighbors'); a.add_argument('handle'); a.add_argument('--direction',choices=['out','in','both'],default='both'); a.add_argument('--canonical',action='store_true')
a=sp.add_parser('object'); a.add_argument('handle'); a=sp.add_parser('spine'); a=sp.add_parser('iterations')
args=p.parse_args(); con=sqlite3.connect(DB);con.row_factory=sqlite3.Row;c=con.cursor()
def rows(x):return [dict(r) for r in x.fetchall()]
if args.cmd=='stats':
 out={t:c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in ['canonical_handles','object_instances','edges','canonical_edges','equations']}
elif args.cmd=='neighbors':
 t='canonical_edges' if args.canonical else 'edges'; out=[]
 if args.direction in ('out','both'):out+=rows(c.execute(f'SELECT * FROM {t} WHERE source_handle=?',(args.handle,)))
 if args.direction in ('in','both'):out+=rows(c.execute(f'SELECT * FROM {t} WHERE target_handle=?',(args.handle,)))
elif args.cmd=='object':out={'canonical':rows(c.execute('SELECT * FROM canonical_handles WHERE handle=?',(args.handle,))),'instances':rows(c.execute('SELECT * FROM object_instances WHERE handle=?',(args.handle,))),'equations':rows(c.execute('SELECT * FROM equations WHERE owner_handle=?',(args.handle,)))}
elif args.cmd=='spine':out=rows(c.execute('SELECT * FROM core_spine ORDER BY ordinal'))
else:out=rows(c.execute('SELECT * FROM iterations ORDER BY iteration'))
print(json.dumps(out,indent=2,ensure_ascii=False))
