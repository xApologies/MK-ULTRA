#!/usr/bin/env python3
import argparse,json,sqlite3,hashlib,re
from pathlib import Path
from collections import deque
ROOT=Path(__file__).resolve().parents[1];API=ROOT/'api';LIVE=ROOT/'live_model';LIB=ROOT/'library';DB=ROOT/'db'/'astraeus_math.sqlite';GLIB=LIB/'dependency_graphs';GLIB.mkdir(parents=True,exist_ok=True)
def load(p): return json.load(open(p,encoding='utf-8'))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def state():
 s=load(API/'LIVE_RUNTIME_STATE.json');return s.get('api_release','0.7.0'),s.get('live_model_revision','v0.20.0')
def resolve(h):
 if h.startswith('@'):return h
 for x in load(API/'ALIAS_REGISTRY.json')['aliases']:
  if x['alias'].lower()==h.lower():return x['handle']
 return h
def edges(): return [e for e in load(API/'EDGE_REGISTRY.json')['edges'] if e.get('graph_family') not in ('landscape_metadata','dependency_graph_metadata','dependency_chain_metadata')]
def graphs(): return {x['qmo_address']:x for x in load(API/'DEPENDENCY_GRAPH_REGISTRY.json')['graphs']}
def objects(): return {o['handle'] for o in load(API/'OBJECT_REGISTRY.json')['objects']}
def shortest(src,tgt,es,direction='bidirectional',max_depth=12):
 out={};inc={}
 for e in es:out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 q=deque([(src,[])]);seen={src}
 while q:
  n,p=q.popleft()
  if len(p)>=max_depth:continue
  moves=[]
  if direction in ('downstream','bidirectional'):moves += [(e,e['target']) for e in out.get(n,[])]
  if direction in ('upstream','bidirectional'):moves += [(e,e['source']) for e in inc.get(n,[])]
  for e,nx in moves:
   np=p+[e]
   if nx==tgt:return np
   if nx not in seen:seen.add(nx);q.append((nx,np))
 return []
def expand_roots(roots,depth,direction,es):
 out={};inc={}
 for e in es:out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 nodes=set(roots);ids=set();q=deque([(x,0) for x in roots]);seen=set(roots)
 while q:
  n,d=q.popleft()
  if d>=depth:continue
  mv=[]
  if direction in ('downstream','bidirectional'):mv += [(e,e['target']) for e in out.get(n,[])]
  if direction in ('upstream','bidirectional'):mv += [(e,e['source']) for e in inc.get(n,[])]
  for e,nx in mv:
   ids.add(e['edge_id']);nodes.update([e['source'],e['target']])
   if nx not in seen:seen.add(nx);q.append((nx,d+1))
 return nodes,ids
def preview(inputs,mode='path',depth=1,direction='bidirectional'):
 inputs=[resolve(x) for x in inputs];gs=graphs();oset=objects();es=edges();nodes=set();ids=set();roots=[];kinds=[]
 for h in inputs:
  if h in gs:
   g=gs[h];nodes.update(g['member_qmos']);ids.update(g['member_edge_ids']);roots+=g.get('roots',[]);kinds.append({'handle':h,'kind':'dependency_graph'})
  elif h in oset:nodes.add(h);roots.append(h);kinds.append({'handle':h,'kind':'qmo'})
  else:raise SystemExit('unknown graph input '+h)
 roots=list(dict.fromkeys(roots))
 if mode=='path':
  if len(roots)!=2:raise SystemExit('path mode requires exactly two resolved roots')
  p=shortest(roots[0],roots[1],es,direction,max(2,depth*4+4));ids.update(e['edge_id'] for e in p);nodes.update([z for e in p for z in (e['source'],e['target'])]);path_found=bool(p) or roots[0]==roots[1]
 elif mode=='ego':
  n,i=expand_roots(roots,depth,direction,es);nodes.update(n);ids.update(i);path_found=None
 elif mode=='induced':
  n,i=expand_roots(roots,depth,direction,es);nodes.update(n)
  for e in es:
   if e['source'] in nodes and e['target'] in nodes:ids.add(e['edge_id'])
  path_found=None
 else:raise SystemExit('unknown mode')
 by={e['edge_id']:e for e in es};mem=[by[i] for i in sorted(ids) if i in by]
 return {'inputs':kinds,'roots':roots,'graph_type':mode,'member_qmos':sorted(nodes),'member_edge_ids':sorted(ids),'member_edges':mem,'statistics':{'qmo_count':len(nodes),'edge_count':len(mem),'path_found':path_found},'resolution_context':{'operator':'@resolution','graph_resolution':f'{mode.upper()}_REGISTERED_DEPENDENCY_VIEW','depth':depth},'bandwidth_context':{'operator':'@bandwidth_algebra','policy':'ONLY_CURRENTLY_REGISTERED_DEPENDENCY_EDGES_ARE_AVAILABLE'}}
def next_edge_id(es):
 ns=[]
 for e in es:
  m=re.fullmatch(r'E-(\d+)',e['edge_id']);
  if m:ns.append(int(m.group(1)))
 return f'E-{max(ns+[0])+1:05d}'
def refresh(meta,es):
 inc={};out={}
 for e in es:out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 for h,r in meta.items():
  ii=inc.get(h,[]);oo=out.get(h,[]);r['relations']={'incoming_count':len(ii),'outgoing_count':len(oo),'incoming_edge_ids':[e['edge_id'] for e in ii],'outgoing_edge_ids':[e['edge_id'] for e in oo],'incoming_relations':sorted({e['relation'] for e in ii}),'outgoing_relations':sorted({e['relation'] for e in oo}),'neighbors_in':sorted({e['source'] for e in ii}),'neighbors_out':sorted({e['target'] for e in oo})}
def default_handle(inputs,mode):return '@dg_'+hashlib.sha256((mode+'|'+'|'.join(inputs)).encode()).hexdigest()[:12]
def register(inputs,mode,depth,direction,handle=None):
 rel,lr=state();inputs=[resolve(x) for x in inputs];h=resolve(handle) if handle else default_handle(inputs,mode);h=h if h.startswith('@') else '@'+h
 greg=load(API/'DEPENDENCY_GRAPH_REGISTRY.json');ex=next((x for x in greg['graphs'] if x['qmo_address']==h),None)
 if ex:return {'registered':False,'reason':'already_registered','graph':ex}
 pv=preview(inputs,mode,depth,direction);gid='DG-'+hashlib.sha256((h+'|'+mode+'|'+','.join(inputs)).encode()).hexdigest()[:12]
 rec={**pv,'graph_id':gid,'qmo_address':h,'canonical_name':'Dependency Graph: '+', '.join(inputs),'status':'DERIVED_CLOSED_INTERNAL','construction':{'operator':'@dependency_graph','mode':mode,'depth':depth,'direction':direction,'edge_policy':'REGISTERED_EDGES_ONLY','member_claim_promotion':False},'history':{'policy':'APPEND_ONLY','created_in_api_release':rel,'created_live_model_revision':lr,'parent_graphs':[x['handle'] for x in pv['inputs'] if x['kind']=='dependency_graph'],'parent_qmos':[x['handle'] for x in pv['inputs'] if x['kind']=='qmo']},'provenance':['GENESIS_DIRECTION::2026-08-22_dependency_graph','API_4.3::DEPENDENCY_GRAPH_IS_MATHEMATICAL_OBJECT','RUNTIME_REGISTER']+[f'QMO:{x}' for x in inputs],'semantic_guard':'Dependency Graph construction preserves registered member status and edge provenance; it does not infer missing edges.'}
 O=load(API/'OBJECT_REGISTRY.json');E=load(API/'EDGE_REGISTRY.json');A=load(API/'ALIAS_REGISTRY.json');C=load(API/'CLOSURE_CERTIFICATE_REGISTRY.json');M=load(LIB/'QMO_METADATA_LIBRARY.json');RT=load(API/'LIVE_RUNTIME_STATE.json');AL=load(LIVE/'API_LIVE_MODEL.json')
 o={'handle':h,'canonical_name':rec['canonical_name'],'type':'dependency graph QMO','status':'DERIVED_CLOSED_INTERNAL','branch':'dependency_graph','definition':f"{mode.title()} Dependency Graph QMO built from {', '.join(inputs)}; contains {pv['statistics']['qmo_count']} member QMOs and {pv['statistics']['edge_count']} registered dependency edges.",'provenance':rec['provenance'],'source_status':'GENERATED_FROM_REGISTERED_QMO_GRAPH','metadata':{'graph_id':gid,'graph_type':mode,'resolution_context':pv['resolution_context'],'bandwidth_context':pv['bandwidth_context'],'history_policy':'APPEND_ONLY','member_status_preserved':True,'live_model_revision':lr}}
 O['objects'].append(o);O['object_count']=len(O['objects']);A['aliases'].append({'alias':h,'handle':h})
 def ae(s,r,t):
  eid=next_edge_id(E['edges']);E['edges'].append({'edge_id':eid,'source':s,'relation':r,'target':t,'graph_family':'dependency_graph_metadata','status':'DERIVED_ARCHITECTURE','confidence':'high','audit_status':'architectural','provenance':rec['provenance']})
 ae('@dependency_graph','CONSTRUCTS_GRAPH',h)
 for x in pv['inputs']:ae(h,'COMPOSES_GRAPH' if x['kind']=='dependency_graph' else 'HAS_GRAPH_ROOT',x['handle'])
 E['edge_count']=len(E['edges']);cert={'certificate_id':'CERT-DG-'+gid.split('-',1)[1],'handle':h,'status':'VALID','domain':'@rainbow_road_recursive_domain','rule':'DEPENDENCY_GRAPH_CONSTRUCTION_V1','premises':inputs,'obligations':{'inputs_registered':True,'edges_registered':True,'no_unregistered_edges_added':True,'member_status_preserved':True,'provenance_complete':True,'history_attached':True,'qmo_address_registered':True},'provenance':rec['provenance'],'semantic_guard':'Certificate validates graph construction only; it does not promote member claims.'};C['certificates'].append(cert);C['certificate_count']=len(C['certificates']);greg['graphs'].append(rec);greg['graph_count']=len(greg['graphs']);greg['api_release']=rel
 meta=M['qmo'];meta[h]={'qmo_address':h,'canonical_name':o['canonical_name'],'aliases':[h],'type':o['type'],'status':o['status'],'branch':o['branch'],'meaning':{'definition':o['definition'],'semantic_role':'QUERYABLE_MATHEMATICAL_OBJECT','source_status':o['source_status'],'interpretive_note':None},'relations':{},'mathematical_links':{'equation_handle':None,'theorem_handle':None,'candidate_id':None,'frontier_status':None},'closure':{'closure_status':'CERTIFIED_INTERNAL','certificate_id':cert['certificate_id'],'certificate_status':'VALID','audit_status':'architectural'},'provenance':o['provenance'],'recovery':{'canonical_structure_recoverable_required':True,'provenance_refs':o['provenance'],'closure_certificate':cert['certificate_id'],'history_policy':'APPEND_ONLY_WHEN_HISTORY_BEARING','identity_witness':None,'source_live_model_revision':lr},'native_metadata':o['metadata'],'revision':{'api_release':rel,'live_model_revision':lr,'source_live_model_revision':lr,'metadata_revision':1}}
 refresh(meta,E['edges']);M['address_count']=len(meta);M['qmo']=meta;MR={'schema':'ASTRAEUS_QMO_METADATA_REGISTRY_V2','record_count':len(meta),'records':[meta[x] for x in sorted(meta)]}
 for pth,data in [(API/'OBJECT_REGISTRY.json',O),(API/'EDGE_REGISTRY.json',E),(API/'ALIAS_REGISTRY.json',A),(API/'CLOSURE_CERTIFICATE_REGISTRY.json',C),(API/'DEPENDENCY_GRAPH_REGISTRY.json',greg),(LIB/'QMO_METADATA_LIBRARY.json',M),(API/'QMO_METADATA_REGISTRY.json',MR)]:dump(pth,data)
 dump(GLIB/(h.strip('@')+'.json'),rec)
 with open(LIVE/'DEPENDENCY_GRAPH_HISTORY.jsonl','a',encoding='utf-8') as f:f.write(json.dumps({'event_type':'DEPENDENCY_GRAPH_QMO_CREATED','qmo_address':h,'graph_id':gid,'api_release':rel,'live_model_revision':lr,'inputs':pv['inputs'],'graph_type':mode,'qmo_count':pv['statistics']['qmo_count'],'edge_count':pv['statistics']['edge_count']},ensure_ascii=False)+'\n')
 with open(LIVE/'QMO_METADATA_HISTORY.jsonl','a',encoding='utf-8') as f:f.write(json.dumps({'event_type':'METADATA_RUNTIME_REGISTER','qmo_address':h,'api_release':rel,'live_model_revision':lr,'status':o['status']},ensure_ascii=False)+'\n')
 RT.update({'object_count':len(O['objects']),'edge_count':len(E['edges']),'dependency_graph_count':len(greg['graphs']),'qmo_address_count':len(meta)});dump(API/'LIVE_RUNTIME_STATE.json',RT);AL['inventory']['qmo_addresses']=len(meta);AL['inventory']['typed_edges']=len(E['edges']);AL['inventory']['dependency_graphs']=len(greg['graphs']);AL['runtime_state']=RT;dump(LIVE/'API_LIVE_MODEL.json',AL);dump(LIVE/'QMO_ADDRESS_INDEX.json',{'schema':'ASTRAEUS_QMO_ADDRESS_INDEX_V2','count':len(meta),'addresses':sorted(meta)})
 con=sqlite3.connect(DB);cur=con.cursor();cur.execute('CREATE TABLE IF NOT EXISTS dependency_graphs(qmo_address TEXT PRIMARY KEY, graph_id TEXT, graph_type TEXT, status TEXT, inputs_json TEXT, roots_json TEXT, member_qmos_json TEXT, member_edge_ids_json TEXT, resolution_context_json TEXT, bandwidth_context_json TEXT, history_json TEXT, raw_json TEXT)');cur.execute('INSERT INTO objects VALUES(?,?,?,?,?,?,?,?)',(h,o['canonical_name'],o['type'],o['status'],o['branch'],o['definition'],json.dumps(o['provenance']),json.dumps(o['metadata'])));cur.execute('INSERT INTO aliases VALUES(?,?)',(h,h))
 for e in E['edges'][-(1+len(pv['inputs'])):]:cur.execute('INSERT INTO edges VALUES(?,?,?,?,?,?,?,?,?)',(e['edge_id'],e['source'],e['relation'],e['target'],e['graph_family'],e['status'],e['confidence'],e['audit_status'],json.dumps(e['provenance'])))
 cur.execute('DELETE FROM qmo_metadata')
 for mh,mr in meta.items():cur.execute('INSERT INTO qmo_metadata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(mh,mr['canonical_name'],mr['type'],mr['status'],mr['branch'],mr['meaning']['definition'],json.dumps(mr['aliases']),json.dumps(mr['relations']),json.dumps(mr['closure']),json.dumps(mr['provenance']),json.dumps(mr['recovery']),json.dumps(mr['revision']),json.dumps(mr)))
 cur.execute('INSERT INTO dependency_graphs VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(h,gid,mode,rec['status'],json.dumps(rec['inputs']),json.dumps(rec['roots']),json.dumps(rec['member_qmos']),json.dumps(rec['member_edge_ids']),json.dumps(rec['resolution_context']),json.dumps(rec['bandwidth_context']),json.dumps(rec['history']),json.dumps(rec)));cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(h,h+' '+o['canonical_name']+' '+o['definition']));con.commit();con.close();return {'registered':True,'qmo_address':h,'graph_id':gid,'graph_type':mode,'statistics':pv['statistics']}
p=argparse.ArgumentParser();sp=p.add_subparsers(dest='cmd',required=True)
a=sp.add_parser('preview');a.add_argument('inputs',nargs='+');a.add_argument('--mode',choices=['path','induced','ego'],default='path');a.add_argument('--depth',type=int,default=1);a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional')
a=sp.add_parser('register');a.add_argument('inputs',nargs='+');a.add_argument('--mode',choices=['path','induced','ego'],default='path');a.add_argument('--depth',type=int,default=1);a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional');a.add_argument('--handle')
a=sp.add_parser('get');a.add_argument('handle');a=sp.add_parser('list');a=sp.add_parser('history');a.add_argument('handle',nargs='?')
args=p.parse_args();gs=graphs()
if args.cmd=='preview':out=preview(args.inputs,args.mode,args.depth,args.direction)
elif args.cmd=='register':out=register(args.inputs,args.mode,args.depth,args.direction,args.handle)
elif args.cmd=='get':out=gs.get(resolve(args.handle))
elif args.cmd=='list':out=[{'qmo_address':x['qmo_address'],'graph_type':x['graph_type'],'inputs':x['inputs'],'qmo_count':x['statistics']['qmo_count'],'edge_count':x['statistics']['edge_count']} for x in gs.values()]
else:
 rows=[];p0=LIVE/'DEPENDENCY_GRAPH_HISTORY.jsonl'
 if p0.exists():
  for line in p0.read_text(encoding='utf-8').splitlines():
   x=json.loads(line)
   if not args.handle or x.get('qmo_address')==resolve(args.handle):rows.append(x)
 out=rows
print(json.dumps(out,indent=2,ensure_ascii=False))
