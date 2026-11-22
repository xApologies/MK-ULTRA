from __future__ import annotations
import sqlite3,json,hashlib,uuid,threading,tempfile,copy,re
from pathlib import Path
from datetime import datetime,timezone
from typing import Iterable
from .schema import SCHEMA
from .models import KnowledgeChunk,KnowledgePackage,TransactionPreview,TransactionReceipt,QMORecoveryResult
class LibraryError(Exception): pass
class ValidationError(LibraryError): pass
class ConflictError(LibraryError): pass

class MK43Library:
 version='1.D.0';contract_version='2.0';internal_dimension=5
 canonical_state_policy='READ_ONLY';rewrite_policy='DERIVED_ONLY';chirality_model='address-placement-neutral';provenance_model='package-and-block-provenance';domain_ids=('generic',)
 capabilities=('recover','recover_batch','recover_model','recover_equations','recover_models','recover_analogies','recover_explanations','assemble_chunk','pull_qmo','add_address','add_many','add_package','replace_address','replace_package','remove_address','remove_package','purge_address','purge_package','preview_transaction','validate_transaction','commit_transaction','rollback_transaction')
 def __init__(self,db_path=None,*,_read_only=False):
  self._read_only=_read_only;self._lock=threading.RLock();self._tempdir=None
  if db_path is None:
   self._tempdir=Path(tempfile.mkdtemp(prefix='mk43_library_'));self._db_path=self._tempdir/'library.sqlite3'
  else:self._db_path=Path(db_path)
  if _read_only:
   self._conn=sqlite3.connect(f'file:{self._db_path}?mode=ro',uri=True,check_same_thread=False)
  else:self._conn=sqlite3.connect(self._db_path,check_same_thread=False)
  self._conn.row_factory=sqlite3.Row
  if not _read_only:self._conn.executescript(SCHEMA);self._conn.commit()
 @staticmethod
 def _now():return datetime.now(timezone.utc).isoformat()
 @staticmethod
 def _j(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False)
 @classmethod
 def _hash_obj(cls,v):return hashlib.sha256(cls._j(v).encode()).hexdigest()
 @staticmethod
 def _norm_handle(h):
  if not isinstance(h,str) or not h.strip().startswith('@') or len(h.strip())<2:raise ValidationError('invalid_handle')
  return h.strip()
 def dimension_model(self):return {'identity':True,'dependency':True,'chirality':True,'recursion':True,'provenance':True}
 def healthcheck(self):
  try:
   if self._conn.execute('PRAGMA integrity_check').fetchone()[0]!='ok':return False
   dangling=self._conn.execute('SELECT count(*) FROM objects o WHERE active_version IS NOT NULL AND NOT EXISTS(SELECT 1 FROM versions v WHERE v.handle=o.handle AND v.version=o.active_version)').fetchone()[0]
   return dangling==0 and self._conn.execute("SELECT count(*) FROM sqlite_master WHERE type='table'").fetchone()[0]>=10
  except Exception:return False
 def close(self):self._conn.close()
 def _require_write(self):
  if self._read_only:raise PermissionError('request_context_is_read_only')
 def fork_request_context(self):return MK43Library(self._db_path,_read_only=True)
 def canonical_fingerprint(self):
  rows=[]
  for t in ('objects','versions','blocks','provenance','aliases','relations','models','model_membership'):
   rows.append((t,[dict(r) for r in self._conn.execute(f'SELECT * FROM {t} ORDER BY rowid')]))
  return self._hash_obj(rows)
 def validate_address_package(self,p):
  e=[]
  if not isinstance(p,dict):return ['package_not_object']
  try:self._norm_handle(p.get('handle'))
  except Exception:e.append('invalid_handle')
  if not p.get('object_type'):e.append('missing_object_type')
  if not isinstance(p.get('content_blocks'),list) or not p.get('content_blocks'):e.append('missing_content_blocks')
  if not isinstance(p.get('provenance'),list) or not p.get('provenance'):e.append('missing_provenance')
  for i,b in enumerate(p.get('content_blocks') or []):
   if not isinstance(b,dict) or not b.get('content_type') or 'body' not in b:e.append(f'invalid_block:{i}')
  return e
 def validate_model_package(self,p):
  e=[]
  if not isinstance(p,dict):return ['package_not_object']
  for k in ('package_handle','root_handle','addresses'):
   if k not in p:e.append('missing_'+k)
  try:self._norm_handle(p.get('package_handle'))
  except Exception:e.append('invalid_package_handle')
  aa=p.get('addresses',[])
  if not isinstance(aa,list) or not aa:e.append('missing_addresses')
  for i,a in enumerate(aa):e += [f'address_{i}:{x}' for x in self.validate_address_package(a)]
  hs={a.get('handle') for a in aa if isinstance(a,dict)}
  if p.get('root_handle') not in hs:e.append('root_not_in_package')
  for r in p.get('relations',[]):
   if r.get('required',True) and r.get('source_handle') not in hs:e.append('required_relation_source_missing')
   if r.get('required',True) and r.get('target_handle') not in hs and not self._exists_any(r.get('target_handle')):e.append('required_relation_target_missing')
  return e
 def preview_transaction(self,payload):
  self._require_write();op=payload.get('operation','UNKNOWN');items=payload.get('packages') if 'packages'in payload else [payload.get('package')] if 'package'in payload else []
  errs=[];hs=[]
  if not items:errs.append('missing_package')
  for p in items:
   if not p:errs.append('missing_package');continue
   hs.append(p.get('handle') or p.get('package_handle',''));errs += self.validate_model_package(p) if 'addresses'in p else self.validate_address_package(p)
  tid=uuid.uuid4().hex
  with self._conn:self._conn.execute('INSERT INTO pending_transactions VALUES(?,?,?,?,?,?)',(tid,op,self._j(payload),0 if errs else 1,self._j(errs),self._now()))
  return TransactionPreview(tid,op,not errs,tuple(hs),tuple(errs))
 def validate_transaction(self,payload):return self.preview_transaction(payload)
 def commit_transaction(self,transaction_id):
  self._require_write();r=self._conn.execute('SELECT * FROM pending_transactions WHERE transaction_id=?',(transaction_id,)).fetchone()
  if not r:raise LibraryError('transaction_not_found')
  if not r['valid']:raise ValidationError(';'.join(json.loads(r['errors_json'])))
  p=json.loads(r['payload_json']);op=r['operation'].upper()
  dispatch={'ADD_ONE':lambda:self.add_address(p['package']),'ADD_MANY':lambda:self.add_many(p['packages']),'ADD_PACKAGE':lambda:self.add_package(p['package']),'REPLACE':lambda:self.replace_address(p['handle'],p['package']),'REPLACE_PACKAGE':lambda:self.replace_package(p['package_handle'],p['package']),'REMOVE':lambda:self.remove_address(p['handle']),'PURGE':lambda:self.purge_address(p['handle'],p.get('reason','accidental_admission'),p.get('cascade',False))}
  if op not in dispatch:raise LibraryError('unsupported_transaction_operation')
  receipt=dispatch[op]();self._conn.execute('DELETE FROM pending_transactions WHERE transaction_id=?',(transaction_id,));self._conn.commit();return receipt
 def _snapshot(self):return {t:[dict(r) for r in self._conn.execute(f'SELECT * FROM {t}')] for t in ('objects','versions','blocks','provenance','aliases','relations','models','model_membership')}
 def _restore_snapshot(self,s):
  self._require_write()
  with self._conn:
   for t in ('model_membership','models','relations','aliases','provenance','blocks','versions','objects'):self._conn.execute(f'DELETE FROM {t}')
   for t in ('objects','versions','blocks','provenance','aliases','relations','models','model_membership'):
    for row in s.get(t,[]):
     cols=','.join(row);qs=','.join('?' for _ in row);self._conn.execute(f'INSERT INTO {t}({cols}) VALUES({qs})',tuple(row.values()))
 def _receipt(self,op,hs,pre,details,snapshot=None):
  post=self.canonical_fingerprint();rid=uuid.uuid4().hex
  with self._conn:
   self._conn.execute('INSERT INTO receipts VALUES(?,?,?,?,?,?,?,?)',(rid,op,self._j(hs),pre,post,'committed',self._j(details),self._now()))
   if snapshot is not None:self._conn.execute('INSERT INTO snapshots VALUES(?,?)',(rid,self._j(snapshot)))
  return TransactionReceipt(rid,op,tuple(hs),pre,post,'committed',details)
 def rollback_transaction(self,rid):
  self._require_write();r=self._conn.execute('SELECT snapshot_json FROM snapshots WHERE receipt_id=?',(rid,)).fetchone()
  if not r:raise LibraryError('rollback_unavailable')
  pre=self.canonical_fingerprint();self._restore_snapshot(json.loads(r[0]));return self._receipt('ROLLBACK',[rid],pre,{'rolled_back':rid})
 def _exists_any(self,h):return bool(h and self._conn.execute('SELECT 1 FROM objects WHERE handle=?',(h,)).fetchone())
 @staticmethod
 def _api_alias(h):
  raw=str(h).strip().lstrip('@')
  raw=re.sub(r'([a-z0-9])([A-Z])',r'\1_\2',raw)
  raw=re.sub(r'[^A-Za-z0-9]+','_',raw).strip('_').lower()
  return '@'+raw
 def _resolve_alias(self,h):
  h=self._norm_handle(h)
  r=self._conn.execute('SELECT handle FROM aliases WHERE alias=?',(h,)).fetchone()
  if r:return r[0]
  if self._exists_any(h):return h
  normalized=self._api_alias(h)
  r=self._conn.execute('SELECT handle FROM aliases WHERE alias=?',(normalized,)).fetchone()
  return r[0] if r else h
 def _active_row(self,h):
  h=self._resolve_alias(h);return self._conn.execute('SELECT o.*,v.package_hash,v.language FROM objects o LEFT JOIN versions v ON v.handle=o.handle AND v.version=o.active_version WHERE o.handle=?',(h,)).fetchone()
 def _insert_address(self,p,replace=False):
  h=self._norm_handle(p['handle']);ex=self._conn.execute('SELECT active_version FROM objects WHERE handle=?',(h,)).fetchone()
  if ex and not replace:raise ConflictError('handle_exists')
  ver=(ex[0] or 0)+1 if ex else 1;ph=self._hash_obj(p);meta={k:v for k,v in p.items() if k not in ('content_blocks','provenance','aliases','relations','canonical_math')}
  if not ex:self._conn.execute('INSERT INTO objects VALUES(?,?,?,?,?)',(h,p['object_type'],None,'active',self._now()))
  self._conn.execute('INSERT INTO versions VALUES(?,?,?,?,?,?,?,?)',(h,ver,ph,self._j(p.get('canonical_math',[])),self._j(meta),p.get('language','en-US'),'active',self._now()))
  self._conn.execute('UPDATE objects SET object_type=?,active_version=?,status="active" WHERE handle=?',(p['object_type'],ver,h))
  prov=[self._j(x) if isinstance(x,dict) else str(x) for x in p.get('provenance',[])]
  for i,x in enumerate(prov):self._conn.execute('INSERT INTO provenance VALUES(?,?,?,?,?)',(uuid.uuid4().hex,h,ver,x,i))
  for i,b in enumerate(p['content_blocks']):
   bp=[self._j(x) if isinstance(x,dict) else str(x) for x in b.get('provenance',prov)]
   self._conn.execute('INSERT INTO blocks VALUES(?,?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,h,ver,b['content_type'],b.get('title',b['content_type']),str(b['body']),b.get('body_format','markdown'),int(b.get('ordinal',i)),self._j(bp)))
  self._conn.execute('INSERT OR REPLACE INTO aliases VALUES(?,?)',(self._api_alias(h),h))
  for a in p.get('aliases',[]):self._conn.execute('INSERT OR REPLACE INTO aliases VALUES(?,?)',(a,h))
  for i,r in enumerate(p.get('relations',[])):self._conn.execute('INSERT INTO relations VALUES(?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,h,r['relation_type'],r['target_handle'],r.get('model_handle'),r.get('ordinal',i),1 if r.get('required',True) else 0,self._j(r.get('metadata',{}))))
  return h
 def add_address(self,p):
  self._require_write();e=self.validate_address_package(p)
  if e:raise ValidationError(';'.join(e))
  pre=self.canonical_fingerprint();s=self._snapshot()
  with self._conn:self._insert_address(copy.deepcopy(p))
  return self._receipt('ADD_ONE',[p['handle']],pre,{},s)
 def add_many(self,ps):
  self._require_write();ps=list(ps);e=[]
  for i,p in enumerate(ps):e += [f'{i}:{x}' for x in self.validate_address_package(p)]
  if e:raise ValidationError(';'.join(e))
  pre=self.canonical_fingerprint();s=self._snapshot();hs=[]
  with self._conn:
   for p in ps:hs.append(self._insert_address(copy.deepcopy(p)))
  return self._receipt('ADD_MANY',hs,pre,{},s)
 def add_package(self,p):
  self._require_write();e=self.validate_model_package(p)
  if e:raise ValidationError(';'.join(e))
  mh=p['package_handle'];pre=self.canonical_fingerprint();s=self._snapshot();hs=[]
  with self._conn:
   if self._conn.execute('SELECT 1 FROM models WHERE model_handle=?',(mh,)).fetchone():raise ConflictError('model_exists')
   for a in p['addresses']:hs.append(self._insert_address(copy.deepcopy(a)))
   self._conn.execute('INSERT INTO models VALUES(?,?,?,?,?,?,?)',(mh,p['root_handle'],p.get('package_name',mh),self._hash_obj(p),1,'active',self._j({k:v for k,v in p.items() if k not in ('addresses','relations')})))
   for i,h in enumerate(hs):self._conn.execute('INSERT INTO model_membership VALUES(?,?,?,?)',(mh,h,i,1))
   for i,r in enumerate(p.get('relations',[])):self._conn.execute('INSERT INTO relations VALUES(?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,r['source_handle'],r['relation_type'],r['target_handle'],mh,r.get('ordinal',i),1 if r.get('required',True) else 0,self._j(r.get('metadata',{}))))
  return self._receipt('ADD_PACKAGE',[mh,*hs],pre,{},s)
 def append_content(self,h,b):
  p=self.export_address(h);p['content_blocks'].append(b);return self.replace_address(h,p)
 def replace_address(self,h,p):
  self._require_write();h=self._resolve_alias(h)
  if h!=p.get('handle'):raise ValidationError('stable_handle_mismatch')
  e=self.validate_address_package(p)
  if e:raise ValidationError(';'.join(e))
  if not self._exists_any(h):raise LibraryError('address_not_populated')
  pre=self.canonical_fingerprint();s=self._snapshot()
  with self._conn:self._insert_address(copy.deepcopy(p),True)
  return self._receipt('REPLACE',[h],pre,{},s)
 def replace_package(self,mh,p):
  self._require_write();e=self.validate_model_package(p)
  if e:raise ValidationError(';'.join(e))
  if mh!=p.get('package_handle'):raise ValidationError('stable_package_handle_mismatch')
  old=self._conn.execute('SELECT version FROM models WHERE model_handle=?',(mh,)).fetchone()
  if not old:raise LibraryError('model_not_populated')
  pre=self.canonical_fingerprint();s=self._snapshot();newhs=[a['handle'] for a in p['addresses']]
  with self._conn:
   oldhs=[r[0] for r in self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=?',(mh,))]
   self._conn.execute('DELETE FROM relations WHERE model_handle=?',(mh,));self._conn.execute('DELETE FROM model_membership WHERE model_handle=?',(mh,))
   for a in p['addresses']:
    self._insert_address(copy.deepcopy(a),self._exists_any(a['handle']))
   for h in oldhs:
    if h not in newhs:self._conn.execute('UPDATE objects SET status="inactive" WHERE handle=?',(h,))
   self._conn.execute('UPDATE models SET root_handle=?,name=?,package_hash=?,version=?,status="active",metadata_json=? WHERE model_handle=?',(p['root_handle'],p.get('package_name',mh),self._hash_obj(p),old[0]+1,self._j({k:v for k,v in p.items() if k not in ('addresses','relations')}),mh))
   for i,h in enumerate(newhs):self._conn.execute('INSERT INTO model_membership VALUES(?,?,?,?)',(mh,h,i,1))
   for i,r in enumerate(p.get('relations',[])):self._conn.execute('INSERT INTO relations VALUES(?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,r['source_handle'],r['relation_type'],r['target_handle'],mh,r.get('ordinal',i),1 if r.get('required',True) else 0,self._j(r.get('metadata',{}))))
  return self._receipt('REPLACE_PACKAGE',[mh,*newhs],pre,{},s)
 def remove_address(self,h):
  self._require_write();h=self._resolve_alias(h)
  if not self._exists_any(h):raise LibraryError('address_not_populated')
  pre=self.canonical_fingerprint();s=self._snapshot()
  with self._conn:self._conn.execute('UPDATE objects SET status="inactive" WHERE handle=?',(h,))
  return self._receipt('REMOVE',[h],pre,{},s)
 def remove_many(self,hs):
  self._require_write();pre=self.canonical_fingerprint();s=self._snapshot();out=[]
  with self._conn:
   for h in hs:h=self._resolve_alias(h);self._conn.execute('UPDATE objects SET status="inactive" WHERE handle=?',(h,));out.append(h)
  return self._receipt('REMOVE_MANY',out,pre,{},s)
 def remove_package(self,mh):
  self._require_write();hs=[r[0] for r in self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=?',(mh,))];pre=self.canonical_fingerprint();s=self._snapshot()
  with self._conn:
   self._conn.execute('UPDATE models SET status="inactive" WHERE model_handle=?',(mh,))
   for h in hs:self._conn.execute('UPDATE objects SET status="inactive" WHERE handle=?',(h,))
  return self._receipt('REMOVE_PACKAGE',[mh,*hs],pre,{},s)
 def purge_address(self,h,reason='accidental_admission',cascade=False):
  self._require_write();h=self._resolve_alias(h);row=self._active_row(h)
  if not row:raise LibraryError('address_not_populated')
  deps=[dict(r) for r in self._conn.execute('SELECT * FROM relations WHERE source_handle=? OR target_handle=?',(h,h))];required=[r for r in deps if r['required'] and r['source_handle']!=h]
  if required and not cascade:raise LibraryError('required_dependents_exist')
  pre=self.canonical_fingerprint();former=row['package_hash']
  with self._conn:
   self._conn.execute('DELETE FROM relations WHERE source_handle=? OR target_handle=?',(h,h));self._conn.execute('DELETE FROM model_membership WHERE handle=?',(h,));self._conn.execute('DELETE FROM objects WHERE handle=?',(h,));rid=uuid.uuid4().hex;self._conn.execute('INSERT INTO purge_receipts VALUES(?,?,?,?,?,?)',(rid,h,former,reason,self._j({'relations':len(deps),'cascade':cascade}),self._now()))
  return self._receipt('PURGE',[h],pre,{'reason':reason,'purge_receipt':rid})
 def purge_package(self,mh,reason='accidental_admission'):
  self._require_write();hs=[r[0] for r in self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=?',(mh,))];pre=self.canonical_fingerprint()
  with self._conn:
   if hs:
    marks=','.join('?' for _ in hs);self._conn.execute(f'DELETE FROM relations WHERE model_handle=? OR source_handle IN ({marks}) OR target_handle IN ({marks})',(mh,*hs,*hs))
   else:self._conn.execute('DELETE FROM relations WHERE model_handle=?',(mh,))
   self._conn.execute('DELETE FROM models WHERE model_handle=?',(mh,))
   for h in hs:self._conn.execute('DELETE FROM objects WHERE handle=?',(h,))
   rid=uuid.uuid4().hex;self._conn.execute('INSERT INTO purge_receipts VALUES(?,?,?,?,?,?)',(rid,mh,None,reason,self._j({'handles':hs}),self._now()))
  return self._receipt('PURGE_PACKAGE',[mh,*hs],pre,{'reason':reason,'purge_receipt':rid})
 def export_address(self,h,version=None):
  h=self._resolve_alias(h);o=self._conn.execute('SELECT * FROM objects WHERE handle=?',(h,)).fetchone()
  if not o:raise LibraryError('address_not_populated')
  v=version or o['active_version'];vr=self._conn.execute('SELECT * FROM versions WHERE handle=? AND version=?',(h,v)).fetchone();bs=[dict(r) for r in self._conn.execute('SELECT * FROM blocks WHERE handle=? AND version=? ORDER BY ordinal,block_id',(h,v))];prov=[json.loads(r[0]) for r in self._conn.execute('SELECT record_json FROM provenance WHERE handle=? AND version=? ORDER BY ordinal',(h,v))]
  return {'handle':h,'object_type':o['object_type'],'canonical_math':json.loads(vr['canonical_math_json']),'content_blocks':[{'content_type':b['content_type'],'title':b['title'],'body':b['body'],'body_format':b['body_format'],'ordinal':b['ordinal'],'provenance':json.loads(b['provenance_json'])} for b in bs],'provenance':prov,'package_version':str(v),'language':vr['language']}
 def _package(self,h,context=None,language='en-US',types=None,version=None,relation=None,depth=None,placement=None):
  try:h=self._resolve_alias(h)
  except Exception:return KnowledgePackage(str(h),str(h),unresolved_reason='invalid_address',relation=relation,depth=depth,placement=placement)
  row=self._active_row(h)
  if not row or row['status']!='active':return KnowledgePackage(h,h,unresolved_reason='address_not_populated',relation=relation,depth=depth,placement=placement)
  if language not in (row['language'],'en','en-US'):return KnowledgePackage(h,h,unresolved_reason='language_not_available',relation=relation,depth=depth,placement=placement)
  v=version or row['active_version'];q='SELECT * FROM blocks WHERE handle=? AND version=?';args=[h,v]
  if types:q+=' AND content_type IN ('+','.join('?' for _ in types)+')';args+=list(types)
  q+=' ORDER BY ordinal,block_id';chunks=[]
  for b in self._conn.execute(q,args):chunks.append(KnowledgeChunk(b['content_type'],b['title'],b['body'],b['ordinal'],language,tuple(json.loads(b['provenance_json']))))
  prov=tuple(r[0] for r in self._conn.execute('SELECT record_json FROM provenance WHERE handle=? AND version=? ORDER BY ordinal',(h,v)))
  k=getattr(context,'key',None) if context is not None else None;key=k.encode() if hasattr(k,'encode') else str(k) if k else None
  return KnowledgePackage(h,h,chunks,None,str(v),key,tuple(types or ()),relation,depth,placement,prov,row['package_hash'])
 def recover(self,h,context=None,language='en-US'):return self._package(h,context,language)
 def recover_equations(self,h,context=None,language='en-US'):return self._package(h,context,language,('equation','operator','canonical_math')).chunks
 def recover_models(self,h,context=None,language='en-US'):return self._package(h,context,language,('model',)).chunks
 def recover_analogies(self,h,context=None,language='en-US'):return self._package(h,context,language,('analogy',)).chunks
 def recover_explanations(self,h,context=None,language='en-US'):return self._package(h,context,language,('explanation','definition','derivation')).chunks
 def assemble_chunk(self,h,context=None,language='en-US'):return self._package(h,context,language)
 def recover_batch(self,handles:Iterable,language='en-US'):
  out=[]
  for x in handles:
   h,c=x if isinstance(x,tuple) else (x,None);out.append(self.recover(h,c,language))
  return out
 def recover_model(self,mh,options=None):
  r=self._conn.execute('SELECT * FROM models WHERE model_handle=? AND status="active"',(mh,)).fetchone()
  if not r:return {'model_handle':mh,'status':'unresolved','reason':'model_not_populated','packages':[]}
  hs=[x[0] for x in self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=? ORDER BY ordinal',(mh,))]
  return {'model_handle':mh,'root_handle':r['root_handle'],'status':'recovered','packages':self.recover_batch(hs)}
 def pull_qmo(self,plan,options=None):
  options=options or {};nodes=plan.get('ordered_nodes') or plan.get('nodes') or [];rec=[];un=[]
  for n in nodes:
   h=n['handle'] if isinstance(n,dict) else str(n);rel=n.get('relation') if isinstance(n,dict) else None;dep=n.get('depth') if isinstance(n,dict) else None;pl=n.get('placement') if isinstance(n,dict) else None;p=self._package(h,None,options.get('language','en-US'),relation=rel,depth=dep,placement=pl)
   if p.resolved:rec.append(p)
   else:un.append({'handle':h,'reason':p.unresolved_reason,'depth':dep,'relation':rel,'placement':pl})
  cov=len(rec)/len(nodes) if nodes else 1.0;oh=self._hash_obj([{'handle':p.handle,'relation':p.relation,'depth':p.depth,'placement':p.placement} for p in rec]+un);pm={p.handle:p.provenance_map for p in rec};hm={p.handle:p.package_hash for p in rec}
  return QMORecoveryResult(plan.get('qmo_id','qmo'),tuple(rec),tuple(un),cov,oh,pm,hm)
