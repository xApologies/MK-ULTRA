#!/usr/bin/env python3
import argparse,json,sqlite3,hashlib,re
from pathlib import Path
from collections import deque
ROOT=Path(__file__).resolve().parents[1]; API=ROOT/'api'; LIVE=ROOT/'live_model'; LIB=ROOT/'library'; DB=ROOT/'db'/'astraeus_math.sqlite'; LANDLIB=LIB/'dependency_landscapes'
LANDLIB.mkdir(parents=True,exist_ok=True)
def load(p): return json.load(open(p,encoding='utf-8'))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def state():
 s=load(API/'LIVE_RUNTIME_STATE.json'); return s.get('api_release','0.7.0'),s.get('live_model_revision','v0.20.0')
def resolve(h):
 if h.startswith('@'): return h
 for x in load(API/'ALIAS_REGISTRY.json')['aliases']:
  if x['alias'].lower()==h.lower(): return x['handle']
 return h
def graph_edges(): return [x for x in load(API/'EDGE_REGISTRY.json')['edges'] if x.get('graph_family') not in ('landscape_metadata','dependency_graph_metadata','dependency_chain_metadata')]
def landscapes(): return {x['qmo_address']:x for x in load(API/'DEPENDENCY_LANDSCAPE_REGISTRY.json')['landscapes']}
def depgraphs():
 p=API/'DEPENDENCY_GRAPH_REGISTRY.json'; return {x['qmo_address']:x for x in load(p)['graphs']} if p.exists() else {}
def shortest(src,tgt,es,max_depth=12):
 out={};inc={}
 for e in es: out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 q=deque([(src,[])]);seen={src}
 while q:
  n,p=q.popleft()
  if len(p)>=max_depth: continue
  for e,nx in [(e,e['target']) for e in out.get(n,[])]+[(e,e['source']) for e in inc.get(n,[])]:
   np=p+[e]
   if nx==tgt:return np
   if nx not in seen:seen.add(nx);q.append((nx,np))
 return []
def preview(inputs,depth=2,direction='bidirectional'):
 inputs=[resolve(x) for x in inputs]; ls=landscapes(); gs=depgraphs(); objs={o['handle'] for o in load(API/'OBJECT_REGISTRY.json')['objects']}; es=graph_edges();out={};inc={}
 for e in es:out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 nodes=set();ids=set();roots=[];kinds=[]
 for h in inputs:
  if h in ls:
   L=ls[h];nodes.update(L['member_qmos']);ids.update(L['member_edge_ids']);roots+=L.get('roots',[]);kinds.append({'handle':h,'kind':'landscape'})
  elif h in gs:
   G=gs[h];nodes.update(G['member_qmos']);ids.update(G['member_edge_ids']);roots+=G.get('roots',[]);kinds.append({'handle':h,'kind':'dependency_graph'})
  elif h in objs:nodes.add(h);roots.append(h);kinds.append({'handle':h,'kind':'qmo'})
  else:raise SystemExit('unknown input '+h)
 roots=list(dict.fromkeys(roots));q=deque([(n,0) for n in roots]);seen=set(roots)
 while q:
  n,d=q.popleft()
  if d>=depth:continue
  ee=[]
  if direction in ('downstream','bidirectional'):ee += [(e,e['target']) for e in out.get(n,[])]
  if direction in ('upstream','bidirectional'):ee += [(e,e['source']) for e in inc.get(n,[])]
  for e,nx in ee:
   ids.add(e['edge_id']);nodes.update([e['source'],e['target']])
   if nx not in seen:seen.add(nx);q.append((nx,d+1))
 for i in range(len(roots)):
  for j in range(i+1,len(roots)):
   for e in shortest(roots[i],roots[j],es):ids.add(e['edge_id']);nodes.update([e['source'],e['target']])
 by={e['edge_id']:e for e in es};mem=[by[i] for i in sorted(ids) if i in by]
 return {'inputs':kinds,'roots':roots,'member_qmos':sorted(nodes),'member_edge_ids':sorted(ids),'member_edges':mem,'statistics':{'qmo_count':len(nodes),'edge_count':len(mem)},'resolution_context':{'operator':'@resolution','policy':'PRESERVE_MEMBER_RESOLUTION_STATE; NO_EXTRA_QUOTIENT_BY_LANDSCAPE','landscape_resolution':'QUERY_RELATIVE_AND_HISTORY_BEARING'},'bandwidth_context':{'operator':'@bandwidth_algebra','policy':'REGISTERED_EDGE_AVAILABILITY_ONLY; LANDSCAPE_DOES_NOT_INVENT_AVAILABLE_TRANSFORMATIONS','landscape_bandwidth':'AVAILABLE_MEMBER_DEPENDENCY_STRUCTURE'}}
def next_edge_id(edges):
 ns=[]
 for e in edges:
  m=re.fullmatch(r'E-(\d+)',e['edge_id']);
  if m:ns.append(int(m.group(1)))
 return f'E-{max(ns+[0])+1:05d}'
def default_handle(inputs): return '@dl_'+hashlib.sha256('|'.join(inputs).encode()).hexdigest()[:12]
def refresh_meta_relations(meta,edges):
 inc={};out={}
 for e in edges:out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 for h,r in meta.items():
  ii=inc.get(h,[]);oo=out.get(h,[]);r['relations']={'incoming_count':len(ii),'outgoing_count':len(oo),'incoming_edge_ids':[e['edge_id'] for e in ii],'outgoing_edge_ids':[e['edge_id'] for e in oo],'incoming_relations':sorted(set(e['relation'] for e in ii)),'outgoing_relations':sorted(set(e['relation'] for e in oo)),'neighbors_in':sorted(set(e['source'] for e in ii)),'neighbors_out':sorted(set(e['target'] for e in oo))}
def register(inputs,depth,direction,handle=None):
 rel,lr=state(); inputs=[resolve(x) for x in inputs]; h=resolve(handle) if handle else default_handle(inputs); h=h if h.startswith('@') else '@'+h
 lreg=load(API/'DEPENDENCY_LANDSCAPE_REGISTRY.json'); existing=next((x for x in lreg['landscapes'] if x['qmo_address']==h),None)
 if existing:return {'registered':False,'reason':'already_registered','landscape':existing}
 pv=preview(inputs,depth,direction); lid='DL-'+hashlib.sha256((h+'|'+','.join(inputs)).encode()).hexdigest()[:12]
 rec={**pv,'landscape_id':lid,'qmo_address':h,'canonical_name':'Dependency Landscape: '+', '.join(inputs),'status':'DERIVED_CLOSED_INTERNAL','construction':{'operator':'@dependency_landscape','depth':depth,'direction':direction,'edge_policy':'REGISTERED_EDGES_ONLY','member_claim_promotion':False},'history':{'policy':'APPEND_ONLY','created_in_api_release':rel,'created_live_model_revision':lr,'parent_landscapes':[x['handle'] for x in pv['inputs'] if x['kind']=='landscape'],'parent_graphs':[x['handle'] for x in pv['inputs'] if x['kind']=='dependency_graph'],'parent_qmos':[x['handle'] for x in pv['inputs'] if x['kind']=='qmo']},'provenance':['API_4.3::DEPENDENCY_LANDSCAPE_ARCHITECTURE','GENESIS_DIRECTION::2026-08-22','RUNTIME_REGISTER']+[f'QMO:{x}' for x in inputs],'semantic_guard':'Landscape membership preserves member status; registration does not promote member claims.'}
 O=load(API/'OBJECT_REGISTRY.json');E=load(API/'EDGE_REGISTRY.json');A=load(API/'ALIAS_REGISTRY.json');C=load(API/'CLOSURE_CERTIFICATE_REGISTRY.json');M=load(LIB/'QMO_METADATA_LIBRARY.json');RT=load(API/'LIVE_RUNTIME_STATE.json');AL=load(LIVE/'API_LIVE_MODEL.json')
 o={'handle':h,'canonical_name':rec['canonical_name'],'type':'dependency landscape QMO','status':'DERIVED_CLOSED_INTERNAL','branch':'dependency_landscape','definition':f"Dependency Landscape QMO built from {', '.join(inputs)}; contains {pv['statistics']['qmo_count']} member QMOs and {pv['statistics']['edge_count']} preserved registered dependency edges.",'provenance':rec['provenance'],'source_status':'GENERATED_FROM_REGISTERED_QMO_GRAPH','metadata':{'landscape_id':lid,'resolution_context':pv['resolution_context'],'bandwidth_context':pv['bandwidth_context'],'history_policy':'APPEND_ONLY','member_status_preserved':True,'live_model_revision':lr}}
 O['objects'].append(o);O['object_count']=len(O['objects']);A['aliases'].append({'alias':h,'handle':h})
 def ae(s,r,t):
  eid=next_edge_id(E['edges']);E['edges'].append({'edge_id':eid,'source':s,'relation':r,'target':t,'graph_family':'landscape_metadata','status':'DERIVED_ARCHITECTURE','confidence':'high','audit_status':'architectural','provenance':rec['provenance']})
 ae('@dependency_landscape','CONSTRUCTS_LANDSCAPE',h)
 for x in pv['inputs']:
  reln='COMPOSES_LANDSCAPE' if x['kind']=='landscape' else ('COMPOSES_GRAPH' if x['kind']=='dependency_graph' else 'HAS_LANDSCAPE_ROOT');ae(h,reln,x['handle'])
 E['edge_count']=len(E['edges'])
 cert={'certificate_id':'CERT-DL-'+lid.split('-',1)[1],'handle':h,'status':'VALID','domain':'@rainbow_road_recursive_domain','rule':'DEPENDENCY_LANDSCAPE_CONSTRUCTION_V2','premises':inputs,'obligations':{'inputs_registered':True,'member_edges_registered':True,'no_unregistered_mathematical_edges_added':True,'member_status_preserved':True,'provenance_complete':True,'history_attached':True,'resolution_context_attached':True,'bandwidth_context_attached':True,'qmo_address_registered':True},'provenance':rec['provenance'],'semantic_guard':'Certificate validates landscape construction only; it does not promote member claims.'};C['certificates'].append(cert);C['certificate_count']=len(C['certificates']);lreg['landscapes'].append(rec);lreg['landscape_count']=len(lreg['landscapes']);lreg['api_release']=rel
 meta=M['qmo']; meta[h]={'qmo_address':h,'canonical_name':o['canonical_name'],'aliases':[h],'type':o['type'],'status':o['status'],'branch':o['branch'],'meaning':{'definition':o['definition'],'semantic_role':'QUERYABLE_MATHEMATICAL_OBJECT','source_status':o['source_status'],'interpretive_note':None},'relations':{},'mathematical_links':{'equation_handle':None,'theorem_handle':None,'candidate_id':None,'frontier_status':None},'closure':{'closure_status':'CERTIFIED_INTERNAL','certificate_id':cert['certificate_id'],'certificate_status':'VALID','audit_status':'architectural'},'provenance':o['provenance'],'recovery':{'canonical_structure_recoverable_required':True,'provenance_refs':o['provenance'],'closure_certificate':cert['certificate_id'],'history_policy':'APPEND_ONLY_WHEN_HISTORY_BEARING','identity_witness':None,'source_live_model_revision':lr},'native_metadata':o['metadata'],'revision':{'api_release':rel,'live_model_revision':lr,'source_live_model_revision':lr,'metadata_revision':1}}
 refresh_meta_relations(meta,E['edges']);M['address_count']=len(meta);M['qmo']=meta
 MR={'schema':'ASTRAEUS_QMO_METADATA_REGISTRY_V2','record_count':len(meta),'records':[meta[x] for x in sorted(meta)]}
 for pth,data in [(API/'OBJECT_REGISTRY.json',O),(API/'EDGE_REGISTRY.json',E),(API/'ALIAS_REGISTRY.json',A),(API/'CLOSURE_CERTIFICATE_REGISTRY.json',C),(API/'DEPENDENCY_LANDSCAPE_REGISTRY.json',lreg),(LIB/'QMO_METADATA_LIBRARY.json',M),(API/'QMO_METADATA_REGISTRY.json',MR)]:dump(pth,data)
 dump(LANDLIB/(h.strip('@')+'.json'),rec)
 with open(LIVE/'DEPENDENCY_LANDSCAPE_HISTORY.jsonl','a',encoding='utf-8') as f:f.write(json.dumps({'event_type':'LANDSCAPE_QMO_CREATED','qmo_address':h,'landscape_id':lid,'api_release':rel,'live_model_revision':lr,'inputs':pv['inputs'],'qmo_count':pv['statistics']['qmo_count'],'edge_count':pv['statistics']['edge_count']},ensure_ascii=False)+'\n')
 with open(LIVE/'QMO_METADATA_HISTORY.jsonl','a',encoding='utf-8') as f:f.write(json.dumps({'event_type':'METADATA_RUNTIME_REGISTER','qmo_address':h,'api_release':rel,'live_model_revision':lr,'status':o['status']},ensure_ascii=False)+'\n')
 RT.update({'object_count':len(O['objects']),'edge_count':len(E['edges']),'dependency_landscape_count':len(lreg['landscapes']),'qmo_address_count':len(meta)});dump(API/'LIVE_RUNTIME_STATE.json',RT);AL['inventory']['qmo_addresses']=len(meta);AL['inventory']['typed_edges']=len(E['edges']);AL['inventory']['dependency_landscapes']=len(lreg['landscapes']);AL['runtime_state']=RT;dump(LIVE/'API_LIVE_MODEL.json',AL);dump(LIVE/'QMO_ADDRESS_INDEX.json',{'schema':'ASTRAEUS_QMO_ADDRESS_INDEX_V2','count':len(meta),'addresses':sorted(meta)})
 con=sqlite3.connect(DB);cur=con.cursor();cur.execute('INSERT INTO objects VALUES(?,?,?,?,?,?,?,?)',(h,o['canonical_name'],o['type'],o['status'],o['branch'],o['definition'],json.dumps(o['provenance']),json.dumps(o['metadata'])));cur.execute('INSERT INTO aliases VALUES(?,?)',(h,h))
 for e in E['edges'][-(1+len(pv['inputs'])):]:cur.execute('INSERT INTO edges VALUES(?,?,?,?,?,?,?,?,?)',(e['edge_id'],e['source'],e['relation'],e['target'],e['graph_family'],e['status'],e['confidence'],e['audit_status'],json.dumps(e['provenance'])))
 cur.execute('DELETE FROM qmo_metadata')
 for mh,mr in meta.items():cur.execute('INSERT INTO qmo_metadata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(mh,mr['canonical_name'],mr['type'],mr['status'],mr['branch'],mr['meaning']['definition'],json.dumps(mr['aliases']),json.dumps(mr['relations']),json.dumps(mr['closure']),json.dumps(mr['provenance']),json.dumps(mr['recovery']),json.dumps(mr['revision']),json.dumps(mr)))
 cur.execute('INSERT INTO dependency_landscapes VALUES(?,?,?,?,?,?,?,?,?,?,?)',(h,lid,rec['status'],json.dumps(rec['inputs']),json.dumps(rec['roots']),json.dumps(rec['member_qmos']),json.dumps(rec['member_edge_ids']),json.dumps(rec['resolution_context']),json.dumps(rec['bandwidth_context']),json.dumps(rec['history']),json.dumps(rec)));cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(h,h+' '+o['canonical_name']+' '+o['definition']));con.commit();con.close()
 return {'registered':True,'qmo_address':h,'landscape_id':lid,'statistics':pv['statistics']}
p=argparse.ArgumentParser();sp=p.add_subparsers(dest='cmd',required=True)
a=sp.add_parser('preview');a.add_argument('inputs',nargs='+');a.add_argument('--depth',type=int,default=2);a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional')
a=sp.add_parser('register');a.add_argument('inputs',nargs='+');a.add_argument('--depth',type=int,default=2);a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional');a.add_argument('--handle')
a=sp.add_parser('get');a.add_argument('handle');a=sp.add_parser('list');a=sp.add_parser('history');a.add_argument('handle',nargs='?')
args=p.parse_args();ls=landscapes()
if args.cmd=='preview':out=preview(args.inputs,args.depth,args.direction)
elif args.cmd=='register':out=register(args.inputs,args.depth,args.direction,args.handle)
elif args.cmd=='get':out=ls.get(resolve(args.handle))
elif args.cmd=='list':out=[{'qmo_address':x['qmo_address'],'inputs':x['inputs'],'qmo_count':x['statistics']['qmo_count'],'edge_count':x['statistics']['edge_count']} for x in ls.values()]
else:
 rows=[];pth=LIVE/'DEPENDENCY_LANDSCAPE_HISTORY.jsonl'
 if pth.exists():
  for line in pth.read_text(encoding='utf-8').splitlines():
   x=json.loads(line)
   if not args.handle or x.get('qmo_address')==resolve(args.handle):rows.append(x)
 out=rows
print(json.dumps(out,indent=2,ensure_ascii=False))
