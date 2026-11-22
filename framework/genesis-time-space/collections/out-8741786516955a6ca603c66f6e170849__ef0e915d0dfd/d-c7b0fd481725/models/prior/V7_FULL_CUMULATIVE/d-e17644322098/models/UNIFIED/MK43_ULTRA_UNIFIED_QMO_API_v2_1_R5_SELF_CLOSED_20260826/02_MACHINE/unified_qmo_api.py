#!/usr/bin/env python3
import sqlite3,json,argparse,os
from collections import deque
DB=os.path.join(os.path.dirname(__file__),'MK43_UNIFIED_QMO_V2.sqlite')

def rows(c): return [dict(r) for r in c.fetchall()]
def resolve(cur,q):
    q=q.strip()
    cur.execute('SELECT canonical_handle FROM aliases WHERE alias=? ORDER BY namespace LIMIT 1',(q,))
    r=cur.fetchone(); return r[0] if r else q

def allowed(e,mode):
    if mode=='all': return True
    if mode=='navigation': return not e['navigation_only'] or True
    return bool(e['closure_eligible']) and not bool(e['navigation_only']) and e['trust_class'] not in ('METADATA_ONLY','NAVIGATION_ONLY_CROSS_CRAWL')

def main():
 p=argparse.ArgumentParser(description='MK43 Unified QMO API v2')
 sp=p.add_subparsers(dest='cmd',required=True)
 a=sp.add_parser('stats')
 a=sp.add_parser('sources')
 a=sp.add_parser('search'); a.add_argument('query'); a.add_argument('--limit',type=int,default=30)
 a=sp.add_parser('source-search'); a.add_argument('query'); a.add_argument('--limit',type=int,default=20)
 a=sp.add_parser('object'); a.add_argument('handle')
 a=sp.add_parser('instances'); a.add_argument('handle')
 a=sp.add_parser('equation'); a.add_argument('query'); a.add_argument('--limit',type=int,default=50)
 a=sp.add_parser('neighbors'); a.add_argument('handle'); a.add_argument('--direction',choices=['out','in','both'],default='both'); a.add_argument('--mode',choices=['strict','navigation','all'],default='strict'); a.add_argument('--limit',type=int,default=250)
 a=sp.add_parser('route'); a.add_argument('source'); a.add_argument('target'); a.add_argument('--depth',type=int,default=8); a.add_argument('--direction',choices=['out','both'],default='out'); a.add_argument('--mode',choices=['strict','navigation','all'],default='strict')
 a=sp.add_parser('recover'); a.add_argument('seed'); a.add_argument('--depth',type=int,default=5); a.add_argument('--direction',choices=['out','in','both'],default='both'); a.add_argument('--mode',choices=['strict','navigation','all'],default='strict'); a.add_argument('--limit',type=int,default=5000)
 a=sp.add_parser('local-qmo'); a.add_argument('seed'); a.add_argument('--depth',type=int,default=2); a.add_argument('--mode',choices=['strict','navigation','all'],default='strict'); a.add_argument('--limit',type=int,default=500)
 a=sp.add_parser('provenance'); a.add_argument('handle')
 a=sp.add_parser('closure-neighbors'); a.add_argument('handle'); a.add_argument('--direction',choices=['out','in','both'],default='both'); a.add_argument('--limit',type=int,default=250)
 a=sp.add_parser('closure-edge'); a.add_argument('source'); a.add_argument('target')
 a=sp.add_parser('self-closure-status')
 a=sp.add_parser('verify')
 args=p.parse_args()
 con=sqlite3.connect(DB); con.row_factory=sqlite3.Row; cur=con.cursor(); out=None
 if args.cmd=='stats':
  out={}
  for t in ['source_packages','source_files','canonical_handles','object_instances','edges','self_closure_nodes','self_closure_edges','equations','qmos','claims','theorems','proof_debt','closures','models','document_mentions','shared_handle_links']:
   out[t]=cur.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
  out['namespaces']=rows(cur.execute('SELECT namespace,COUNT(*) n FROM object_instances GROUP BY namespace ORDER BY n DESC'))
  out['edge_trust']=rows(cur.execute('SELECT trust_class,COUNT(*) n FROM edges GROUP BY trust_class ORDER BY n DESC'))
 elif args.cmd=='sources': out=rows(cur.execute('SELECT * FROM source_packages ORDER BY ordinal'))
 elif args.cmd=='search':
  q=args.query.replace('"',' ')
  try: out=rows(cur.execute('SELECT instance_id,handle,namespace,canonical_name,object_type,definition,status FROM object_fts WHERE object_fts MATCH ? LIMIT ?',(q,args.limit)))
  except sqlite3.OperationalError:
   like='%'+args.query+'%'; out=rows(cur.execute('SELECT instance_id,handle,namespace,canonical_name,object_type,definition,status FROM object_instances WHERE handle LIKE ? OR canonical_name LIKE ? OR definition LIKE ? LIMIT ?',(like,like,like,args.limit)))
 elif args.cmd=='source-search':
  q=args.query.replace('"',' ')
  try: out=rows(cur.execute("SELECT file_id,source_id,relative_path,snippet(source_fts,3,'[',']','...',32) snippet FROM source_fts WHERE source_fts MATCH ? LIMIT ?",(q,args.limit)))
  except sqlite3.OperationalError:
   like='%'+args.query+'%'; out=rows(cur.execute('SELECT file_id,source_id,relative_path,substr(text,1,500) snippet FROM source_files WHERE text LIKE ? LIMIT ?',(like,args.limit)))
 elif args.cmd in ('object','instances','provenance'):
  h=resolve(cur,args.handle)
  if args.cmd=='object':
   base=cur.execute('SELECT * FROM canonical_handles WHERE handle=?',(h,)).fetchone()
   out={'canonical':dict(base) if base else None,'instances':rows(cur.execute('SELECT * FROM object_instances WHERE handle=? ORDER BY namespace',(h,))),'aliases':rows(cur.execute('SELECT * FROM aliases WHERE canonical_handle=?',(h,))),'equations':rows(cur.execute('SELECT eq_id,namespace,kind,expression,meaning,status,source_id,source_path FROM equations WHERE owner_handle=? LIMIT 200',(h,)))}
  elif args.cmd=='instances': out=rows(cur.execute('SELECT * FROM object_instances WHERE handle=? ORDER BY namespace',(h,)))
  else:
   out={'handle':h,'instances':rows(cur.execute('SELECT instance_id,namespace,status,source_id,source_path,provenance_json FROM object_instances WHERE handle=?',(h,))),'edge_sources':rows(cur.execute('SELECT edge_id,namespace,relation,source_id,source_path,provenance_json FROM edges WHERE source_handle=? OR target_handle=? LIMIT 500',(h,h))),'documents':rows(cur.execute('SELECT sf.file_id,sf.source_id,sf.relative_path,dm.mention_count FROM document_mentions dm JOIN source_files sf ON sf.file_id=dm.file_id WHERE dm.handle=? ORDER BY dm.mention_count DESC LIMIT 100',(h,)))}
 elif args.cmd=='equation':
  like='%'+args.query+'%'; out=rows(cur.execute('SELECT * FROM equations WHERE eq_id LIKE ? OR owner_handle LIKE ? OR expression LIKE ? OR meaning LIKE ? LIMIT ?',(like,like,like,like,args.limit)))
 elif args.cmd=='neighbors':
  h=resolve(cur,args.handle); es=[]
  if args.direction in ('out','both'): es+=rows(cur.execute('SELECT * FROM edges WHERE source_handle=? LIMIT ?',(h,args.limit)))
  if args.direction in ('in','both'): es+=rows(cur.execute('SELECT * FROM edges WHERE target_handle=? LIMIT ?',(h,args.limit)))
  out=[e for e in es if allowed(e,args.mode)][:args.limit]
 elif args.cmd in ('route','recover','local-qmo'):
  mode=args.mode; cur.execute('SELECT * FROM edges'); all_edges=[dict(r) for r in cur.fetchall()]; all_edges=[e for e in all_edges if allowed(e,mode)]
  gout={};gin={}
  for e in all_edges: gout.setdefault(e['source_handle'],[]).append(e); gin.setdefault(e['target_handle'],[]).append(e)
  if args.cmd=='route':
   s=resolve(cur,args.source); t=resolve(cur,args.target); q=deque([(s,[])]); seen={s}; found=None
   while q:
    x,path=q.popleft()
    if len(path)>=args.depth: continue
    cand=[(e,e['target_handle'],False) for e in gout.get(x,[])]
    if args.direction=='both': cand += [(e,e['source_handle'],True) for e in gin.get(x,[])]
    for e,y,rev in cand:
     step={'source':x,'relation':('REVERSE('+e['relation']+')' if rev else e['relation']),'target':y,'namespace':e['namespace'],'trust_class':e['trust_class'],'status':e['status'],'source_id':e['source_id'],'source_path':e['source_path']}
     np=path+[step]
     if y==t: found=np; q.clear(); break
     if y not in seen: seen.add(y); q.append((y,np))
    if found: break
   out={'source':s,'target':t,'mode':mode,'found':found is not None,'path':found}
  else:
   seed=resolve(cur,args.seed); seen={seed}; waves=[[seed]]
   depth=args.depth
   for _ in range(depth):
    nxt=set()
    for x in waves[-1]:
     if getattr(args,'direction','both') in ('out','both'): nxt.update(e['target_handle'] for e in gout.get(x,[]))
     if getattr(args,'direction','both') in ('in','both'): nxt.update(e['source_handle'] for e in gin.get(x,[]))
    nxt-=seen
    if not nxt: break
    if len(seen)+len(nxt)>args.limit: nxt=set(sorted(nxt)[:max(0,args.limit-len(seen))])
    seen|=nxt; waves.append(sorted(nxt))
    if len(seen)>=args.limit: break
   if args.cmd=='recover': out={'seed':seed,'mode':mode,'iterations_used':len(waves)-1,'wave_counts':[len(w) for w in waves],'recovered_count':len(seen),'recovered':sorted(seen)}
   else:
    hs=sorted(seen)
    ph=','.join('?'*len(hs)) if hs else "''"
    objs=rows(cur.execute(f'SELECT * FROM object_instances WHERE handle IN ({ph}) ORDER BY handle,namespace',hs)) if hs else []
    eqs=rows(cur.execute(f'SELECT * FROM equations WHERE owner_handle IN ({ph}) ORDER BY owner_handle',hs)) if hs else []
    ed=[e for e in all_edges if e['source_handle'] in seen and e['target_handle'] in seen]
    out={'qmo_type':'LocalUnifiedQMO','seed':seed,'depth':depth,'mode':mode,'handles':hs,'objects':objs,'equations':eqs,'edges':ed[:5000]}
 elif args.cmd=='closure-neighbors':
  h=resolve(cur,args.handle); out=[]
  if args.direction in ('out','both'):
   out += rows(cur.execute("SELECT ns.handle source_handle,'COMPOSED_DEPENDENCY' relation,nt.handle target_handle,ce.closure_pass,ce.shortest_distance,'DERIVED_SELF_CLOSURE_R5' status FROM self_closure_edges ce JOIN self_closure_nodes ns ON ns.node_id=ce.source_id JOIN self_closure_nodes nt ON nt.node_id=ce.target_id WHERE ns.handle=? LIMIT ?",(h,args.limit)))
  if args.direction in ('in','both'):
   out += rows(cur.execute("SELECT ns.handle source_handle,'COMPOSED_DEPENDENCY' relation,nt.handle target_handle,ce.closure_pass,ce.shortest_distance,'DERIVED_SELF_CLOSURE_R5' status FROM self_closure_edges ce JOIN self_closure_nodes ns ON ns.node_id=ce.source_id JOIN self_closure_nodes nt ON nt.node_id=ce.target_id WHERE nt.handle=? LIMIT ?",(h,args.limit)))
  out=out[:args.limit]
 elif args.cmd=='closure-edge':
  s=resolve(cur,args.source); t=resolve(cur,args.target)
  prim=cur.execute("SELECT relation,namespace,trust_class,status,confidence,source_id,source_path FROM edges WHERE source_handle=? AND target_handle=? AND closure_eligible=1 AND navigation_only=0 AND trust_class NOT IN ('METADATA_ONLY','NAVIGATION_ONLY_CROSS_CRAWL') LIMIT 1",(s,t)).fetchone()
  der=cur.execute("SELECT ce.* FROM self_closure_edges ce JOIN self_closure_nodes ns ON ns.node_id=ce.source_id JOIN self_closure_nodes nt ON nt.node_id=ce.target_id WHERE ns.handle=? AND nt.handle=?",(s,t)).fetchone()
  out={'source':s,'target':t,'connected':bool(prim or der),'primitive':dict(prim) if prim else None,'derived':dict(der) if der else None}
 elif args.cmd=='self-closure-status':
  out={'derived_edge_count':cur.execute('SELECT COUNT(*) FROM self_closure_edges').fetchone()[0],'closure':rows(cur.execute("SELECT * FROM closures WHERE closure_id='CLOSURE-MK43-UNIFIED-R5-20260826'"))}
 elif args.cmd=='verify':
  out={'quick_check':cur.execute('PRAGMA quick_check').fetchone()[0],'foreign_key_check':rows(cur.execute('PRAGMA foreign_key_check')),'root':dict(cur.execute('SELECT * FROM qmos WHERE qmo_id=?',('QMO-MK43-UNIFIED-V2-R5-002',)).fetchone() or {})}
 print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
