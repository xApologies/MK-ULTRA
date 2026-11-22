from __future__ import annotations
import sqlite3, json, hashlib, uuid, threading, tempfile, copy
from pathlib import Path
from datetime import datetime, timezone
from typing import Iterable, Any
from .schema import SCHEMA
from .models import KnowledgeChunk, KnowledgePackage, TransactionPreview, TransactionReceipt, QMORecoveryResult

class LibraryError(Exception): pass
class ValidationError(LibraryError): pass
class ConflictError(LibraryError): pass

class MK43Library:
    version='1.B.0'; contract_version='2.0'; internal_dimension=5
    canonical_state_policy='READ_ONLY'; rewrite_policy='DERIVED_ONLY'
    chirality_model='address-placement-neutral'; provenance_model='package-and-block-provenance'
    domain_ids=('generic',)
    capabilities=('recover','recover_batch','recover_model','recover_equations','recover_models','recover_analogies','recover_explanations','assemble_chunk','pull_qmo','add_address','add_many','add_package','replace_address','remove_address','purge_address','rollback_transaction')

    def __init__(self, db_path: str | Path | None=None, *, _read_only=False):
        self._read_only=_read_only
        self._lock=threading.RLock()
        if db_path is None:
            self._tempdir=Path(tempfile.mkdtemp(prefix='mk43_library1b_'))
            self._db_path=self._tempdir/'library.sqlite3'
        else:
            self._tempdir=None; self._db_path=Path(db_path)
        self._conn=sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.row_factory=sqlite3.Row
        self._conn.executescript(SCHEMA); self._conn.commit()

    @staticmethod
    def _now(): return datetime.now(timezone.utc).isoformat()
    @staticmethod
    def _j(v): return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    @classmethod
    def _hash_obj(cls,v): return hashlib.sha256(cls._j(v).encode()).hexdigest()
    @staticmethod
    def _norm_handle(h):
        if not isinstance(h,str) or not h.startswith('@') or len(h)<2: raise ValidationError('invalid_handle')
        return h.strip()

    def dimension_model(self): return {'identity':True,'dependency':True,'chirality':True,'recursion':True,'provenance':True}
    def healthcheck(self):
        try:
            return self._conn.execute('PRAGMA integrity_check').fetchone()[0]=='ok' and self._conn.execute("SELECT count(*) FROM sqlite_master WHERE type='table'").fetchone()[0]>=8
        except Exception:return False
    def canonical_fingerprint(self):
        rows=[]
        for table in ('objects','versions','blocks','aliases','relations','models','model_membership'):
            vals=[dict(r) for r in self._conn.execute(f'SELECT * FROM {table} ORDER BY rowid')]
            rows.append((table,vals))
        return self._hash_obj(rows)
    def fork_request_context(self):
        # Separate connection with write guard over the same canonical database.
        return MK43Library(self._db_path,_read_only=True)
    def close(self): self._conn.close()
    def _require_write(self):
        if self._read_only: raise PermissionError('request_context_is_read_only')

    def validate_address_package(self,p):
        errors=[]
        if not isinstance(p,dict): return ['package_not_object']
        try:self._norm_handle(p.get('handle'))
        except Exception:errors.append('invalid_handle')
        if not p.get('object_type'): errors.append('missing_object_type')
        if not isinstance(p.get('content_blocks'),list) or not p.get('content_blocks'): errors.append('missing_content_blocks')
        if not isinstance(p.get('provenance'),list) or not p.get('provenance'): errors.append('missing_provenance')
        for i,b in enumerate(p.get('content_blocks') or []):
            if not isinstance(b,dict) or not b.get('content_type') or 'body' not in b: errors.append(f'invalid_block:{i}')
        return errors
    def validate_model_package(self,p):
        errors=[]
        if not isinstance(p,dict): return ['package_not_object']
        for k in ('package_handle','root_handle','addresses'):
            if k not in p: errors.append('missing_'+k)
        try:self._norm_handle(p.get('package_handle'))
        except Exception:errors.append('invalid_package_handle')
        addr=p.get('addresses',[])
        if not isinstance(addr,list) or not addr: errors.append('missing_addresses')
        for i,a in enumerate(addr): errors += [f'address_{i}:{e}' for e in self.validate_address_package(a)]
        handles={a.get('handle') for a in addr if isinstance(a,dict)}
        if p.get('root_handle') not in handles: errors.append('root_not_in_package')
        for r in p.get('relations',[]):
            if r.get('required',True) and r.get('source_handle') not in handles: errors.append('required_relation_source_missing')
            if r.get('required',True) and r.get('target_handle') not in handles and not self._exists_any(r.get('target_handle')): errors.append('required_relation_target_missing')
        return errors

    def preview_transaction(self,payload):
        op=payload.get('operation','UNKNOWN'); items=payload.get('packages') if 'packages' in payload else [payload.get('package')] if 'package' in payload else []
        errs=[]; handles=[]
        for p in items:
            if not p:
                errs.append('missing_package'); continue
            handles.append(p.get('handle') or p.get('package_handle',''))
            errs += self.validate_model_package(p) if 'addresses' in p else self.validate_address_package(p)
        return TransactionPreview(uuid.uuid4().hex,op,not errs,tuple(handles),tuple(errs))
    def validate_transaction(self,payload): return self.preview_transaction(payload)
    def commit_transaction(self,transaction_id): raise LibraryError('transactions_commit_through_operation_methods')

    def _snapshot(self):
        out={}
        for t in ('objects','versions','blocks','aliases','relations','models','model_membership'):
            out[t]=[dict(r) for r in self._conn.execute(f'SELECT * FROM {t}')]
        return out
    def _restore_snapshot(self,s):
        self._require_write()
        with self._conn:
            for t in ('model_membership','models','relations','aliases','blocks','versions','objects'): self._conn.execute(f'DELETE FROM {t}')
            for t in ('objects','versions','blocks','aliases','relations','models','model_membership'):
                for row in s.get(t,[]):
                    cols=','.join(row); qs=','.join('?' for _ in row)
                    self._conn.execute(f'INSERT INTO {t}({cols}) VALUES({qs})',tuple(row.values()))
    def _receipt(self,op,handles,pre,details,snapshot=None):
        post=self.canonical_fingerprint(); rid=uuid.uuid4().hex
        with self._conn:
            self._conn.execute('INSERT INTO receipts VALUES(?,?,?,?,?,?,?,?)',(rid,op,self._j(handles),pre,post,'committed',self._j(details),self._now()))
            if snapshot is not None:self._conn.execute('INSERT INTO snapshots VALUES(?,?)',(rid,self._j(snapshot)))
        return TransactionReceipt(rid,op,tuple(handles),pre,post,'committed',details)
    def rollback_transaction(self,receipt_id):
        self._require_write(); row=self._conn.execute('SELECT snapshot_json FROM snapshots WHERE receipt_id=?',(receipt_id,)).fetchone()
        if not row: raise LibraryError('rollback_unavailable')
        pre=self.canonical_fingerprint(); self._restore_snapshot(json.loads(row[0])); return self._receipt('ROLLBACK',[receipt_id],pre,{'rolled_back':receipt_id})

    def _exists_any(self,h): return bool(h and self._conn.execute('SELECT 1 FROM objects WHERE handle=?',(h,)).fetchone())
    def _active_row(self,h):
        h=self._resolve_alias(h)
        return self._conn.execute('SELECT o.handle,o.object_type,o.active_version,o.status,v.package_hash,v.language,v.metadata_json FROM objects o LEFT JOIN versions v ON v.handle=o.handle AND v.version=o.active_version WHERE o.handle=?',(h,)).fetchone()
    def _resolve_alias(self,h):
        h=self._norm_handle(h)
        r=self._conn.execute('SELECT handle FROM aliases WHERE alias=?',(h,)).fetchone(); return r[0] if r else h

    def _insert_address(self,p,replace=False):
        h=self._norm_handle(p['handle']); existing=self._conn.execute('SELECT active_version FROM objects WHERE handle=?',(h,)).fetchone()
        if existing and not replace: raise ConflictError('handle_exists')
        ver=(existing[0] or 0)+1 if existing else 1
        canonical_math=p.get('canonical_math',[]); meta={k:v for k,v in p.items() if k not in ('content_blocks','provenance','aliases','relations','canonical_math')}
        ph=self._hash_obj(p)
        if not existing:self._conn.execute('INSERT INTO objects VALUES(?,?,?,?,?)',(h,p['object_type'],ver,'active',self._now()))
        else:self._conn.execute('UPDATE objects SET object_type=?,active_version=?,status=? WHERE handle=?',(p['object_type'],ver,'active',h))
        self._conn.execute('INSERT INTO versions VALUES(?,?,?,?,?,?,?,?)',(h,ver,ph,self._j(canonical_math),self._j(meta),p.get('language','en-US'),'active',self._now()))
        prov=tuple(self._j(x) if isinstance(x,dict) else str(x) for x in p.get('provenance',[]))
        for i,b in enumerate(p['content_blocks']):
            bid=uuid.uuid4().hex
            bp=tuple(str(x) for x in b.get('provenance',prov))
            self._conn.execute('INSERT INTO blocks VALUES(?,?,?,?,?,?,?,?,?)',(bid,h,ver,b['content_type'],b.get('title',b['content_type']),str(b['body']),b.get('body_format','markdown'),int(b.get('ordinal',i)),self._j(bp)))
        for a in p.get('aliases',[]): self._conn.execute('INSERT OR REPLACE INTO aliases VALUES(?,?)',(a,h))
        for i,r in enumerate(p.get('relations',[])):
            self._conn.execute('INSERT INTO relations VALUES(?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,h,r['relation_type'],r['target_handle'],r.get('model_handle'),r.get('ordinal',i),1 if r.get('required',True) else 0,self._j(r.get('metadata',{}))))
        return h

    def add_address(self,package):
        self._require_write(); errs=self.validate_address_package(package)
        if errs: raise ValidationError(';'.join(errs))
        pre=self.canonical_fingerprint(); snap=self._snapshot()
        try:
            with self._conn:self._insert_address(copy.deepcopy(package),False)
        except Exception: raise
        return self._receipt('ADD_ONE',[package['handle']],pre,{},snap)
    def add_many(self,packages):
        self._require_write(); packages=list(packages); errs=[]
        for i,p in enumerate(packages):errs += [f'{i}:{e}' for e in self.validate_address_package(p)]
        if errs: raise ValidationError(';'.join(errs))
        pre=self.canonical_fingerprint(); snap=self._snapshot(); hs=[]
        with self._conn:
            for p in packages:hs.append(self._insert_address(copy.deepcopy(p),False))
        return self._receipt('ADD_MANY',hs,pre,{},snap)
    def add_package(self,p):
        self._require_write(); errs=self.validate_model_package(p)
        if errs: raise ValidationError(';'.join(errs))
        pre=self.canonical_fingerprint(); snap=self._snapshot(); mh=p['package_handle']; hs=[]
        with self._conn:
            if self._conn.execute('SELECT 1 FROM models WHERE model_handle=?',(mh,)).fetchone(): raise ConflictError('model_exists')
            for a in p['addresses']:hs.append(self._insert_address(copy.deepcopy(a),False))
            ph=self._hash_obj(p)
            self._conn.execute('INSERT INTO models VALUES(?,?,?,?,?,?,?)',(mh,p['root_handle'],p.get('package_name',mh),ph,1,'active',self._j({k:v for k,v in p.items() if k not in ('addresses','relations')})))
            for i,h in enumerate(hs):self._conn.execute('INSERT INTO model_membership VALUES(?,?,?,?)',(mh,h,i,1))
            for i,r in enumerate(p.get('relations',[])):
                self._conn.execute('INSERT INTO relations VALUES(?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,r['source_handle'],r['relation_type'],r['target_handle'],mh,r.get('ordinal',i),1 if r.get('required',True) else 0,self._j(r.get('metadata',{}))))
        return self._receipt('ADD_PACKAGE',[mh,*hs],pre,{},snap)
    def append_content(self,handle,content_block):
        row=self._active_row(handle)
        if not row or row['status']!='active': raise LibraryError('address_not_populated')
        pkg=self.export_address(handle); pkg['content_blocks'].append(content_block); return self.replace_address(handle,pkg)
    def replace_address(self,handle,package):
        self._require_write(); h=self._resolve_alias(handle)
        if h!=package.get('handle'): raise ValidationError('stable_handle_mismatch')
        errs=self.validate_address_package(package)
        if errs:raise ValidationError(';'.join(errs))
        if not self._exists_any(h):raise LibraryError('address_not_populated')
        pre=self.canonical_fingerprint();snap=self._snapshot()
        with self._conn:self._insert_address(copy.deepcopy(package),True)
        return self._receipt('REPLACE',[h],pre,{},snap)
    def replace_package(self,package_handle,model_package):
        self._require_write(); self.remove_package(package_handle); return self.add_package(model_package)
    def remove_address(self,handle):
        self._require_write();h=self._resolve_alias(handle);row=self._active_row(h)
        if not row:raise LibraryError('address_not_populated')
        pre=self.canonical_fingerprint();snap=self._snapshot()
        with self._conn:self._conn.execute("UPDATE objects SET status='inactive' WHERE handle=?",(h,))
        return self._receipt('REMOVE',[h],pre,{},snap)
    def remove_many(self,handles):
        self._require_write();pre=self.canonical_fingerprint();snap=self._snapshot();hs=[]
        with self._conn:
            for h in handles:
                h=self._resolve_alias(h);self._conn.execute("UPDATE objects SET status='inactive' WHERE handle=?",(h,));hs.append(h)
        return self._receipt('REMOVE_MANY',hs,pre,{},snap)
    def remove_package(self,package_handle):
        self._require_write(); rows=self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=?',(package_handle,)).fetchall()
        pre=self.canonical_fingerprint();snap=self._snapshot();hs=[r[0] for r in rows]
        with self._conn:
            self._conn.execute("UPDATE models SET status='inactive' WHERE model_handle=?",(package_handle,))
            for h in hs:self._conn.execute("UPDATE objects SET status='inactive' WHERE handle=?",(h,))
        return self._receipt('REMOVE_PACKAGE',[package_handle,*hs],pre,{},snap)
    def purge_address(self,handle,reason='accidental_admission',cascade=False):
        self._require_write();h=self._resolve_alias(handle);row=self._active_row(h)
        if not row:raise LibraryError('address_not_populated')
        deps=self._conn.execute('SELECT source_handle,target_handle,required FROM relations WHERE target_handle=? OR source_handle=?',(h,h)).fetchall()
        required=[dict(x) for x in deps if x['required'] and x['source_handle']!=h]
        if required and not cascade:raise LibraryError('required_dependents_exist')
        pre=self.canonical_fingerprint();former=row['package_hash']
        with self._conn:
            if cascade:self._conn.execute('DELETE FROM relations WHERE target_handle=? OR source_handle=?',(h,h))
            else:self._conn.execute('DELETE FROM relations WHERE source_handle=?',(h,))
            self._conn.execute('DELETE FROM model_membership WHERE handle=?',(h,))
            self._conn.execute('DELETE FROM objects WHERE handle=?',(h,))
            rid=uuid.uuid4().hex
            self._conn.execute('INSERT INTO purge_receipts VALUES(?,?,?,?,?,?)',(rid,h,former,reason,self._j({'relations':len(deps),'cascade':cascade}),self._now()))
        return self._receipt('PURGE',[h],pre,{'reason':reason,'purge_receipt':rid})
    def purge_package(self,package_handle,reason='accidental_admission'):
        self._require_write(); hs=[r[0] for r in self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=?',(package_handle,))]
        pre=self.canonical_fingerprint()
        with self._conn:
            for h in hs:self._conn.execute('DELETE FROM objects WHERE handle=?',(h,))
            self._conn.execute('DELETE FROM models WHERE model_handle=?',(package_handle,))
        return self._receipt('PURGE_PACKAGE',[package_handle,*hs],pre,{'reason':reason})

    def export_address(self,handle,version=None):
        h=self._resolve_alias(handle); o=self._conn.execute('SELECT * FROM objects WHERE handle=?',(h,)).fetchone()
        if not o:raise LibraryError('address_not_populated')
        v=version or o['active_version'];vr=self._conn.execute('SELECT * FROM versions WHERE handle=? AND version=?',(h,v)).fetchone()
        blocks=[dict(r) for r in self._conn.execute('SELECT * FROM blocks WHERE handle=? AND version=? ORDER BY ordinal,block_id',(h,v))]
        return {'handle':h,'object_type':o['object_type'],'canonical_math':json.loads(vr['canonical_math_json']),'content_blocks':[{'content_type':b['content_type'],'title':b['title'],'body':b['body'],'body_format':b['body_format'],'ordinal':b['ordinal'],'provenance':json.loads(b['provenance_json'])} for b in blocks],'provenance':sorted({p for b in blocks for p in json.loads(b['provenance_json'])}),'package_version':str(v),'language':vr['language']}
    def _package(self,handle,context=None,language='en-US',types=None,version=None):
        try:h=self._resolve_alias(handle)
        except Exception:return KnowledgePackage(str(handle),str(handle),unresolved_reason='invalid_address')
        row=self._active_row(h)
        if not row or row['status']!='active':return KnowledgePackage(h,h,unresolved_reason='address_not_populated')
        if language not in (row['language'],'en','en-US'):return KnowledgePackage(h,h,unresolved_reason='language_not_available')
        v=version or row['active_version']; q='SELECT * FROM blocks WHERE handle=? AND version=?';args=[h,v]
        if types:q+=' AND content_type IN ('+','.join('?' for _ in types)+')';args+=list(types)
        q+=' ORDER BY ordinal,block_id'
        chunks=[]
        for b in self._conn.execute(q,args):
            chunks.append(KnowledgeChunk(b['content_type'],b['title'],b['body'],b['ordinal'],language,tuple(json.loads(b['provenance_json']))))
        key=None
        if context is not None:
            k=getattr(context,'key',None);key=k.encode() if hasattr(k,'encode') else str(k) if k else None
        return KnowledgePackage(h,h,chunks,None,str(v),key,tuple(types or ()))
    def recover(self,handle,context=None,language='en-US'):return self._package(handle,context,language)
    def recover_equations(self,handle,context=None,language='en-US'):return self._package(handle,context,language,('equation','operator','canonical_math')).chunks
    def recover_models(self,handle,context=None,language='en-US'):return self._package(handle,context,language,('model',)).chunks
    def recover_analogies(self,handle,context=None,language='en-US'):return self._package(handle,context,language,('analogy',)).chunks
    def recover_explanations(self,handle,context=None,language='en-US'):return self._package(handle,context,language,('explanation','definition','derivation')).chunks
    def assemble_chunk(self,handle,context=None,language='en-US'):return self._package(handle,context,language)
    def recover_batch(self,handles:Iterable,language='en-US'):
        out=[]
        for item in handles:
            if isinstance(item,tuple):h,c=item
            else:h,c=item,None
            out.append(self.recover(h,c,language))
        return out
    def recover_model(self,model_handle,options=None):
        r=self._conn.execute('SELECT * FROM models WHERE model_handle=? AND status="active"',(model_handle,)).fetchone()
        if not r:return {'model_handle':model_handle,'status':'unresolved','reason':'model_not_populated','packages':[]}
        hs=[x[0] for x in self._conn.execute('SELECT handle FROM model_membership WHERE model_handle=? ORDER BY ordinal',(model_handle,))]
        return {'model_handle':model_handle,'root_handle':r['root_handle'],'status':'recovered','packages':self.recover_batch(hs)}
    def pull_qmo(self,address_plan,options=None):
        options=options or {}; nodes=address_plan.get('ordered_nodes') or address_plan.get('nodes') or []
        recovered=[];unresolved=[]
        for n in nodes:
            h=n['handle'] if isinstance(n,dict) else str(n); p=self.recover(h,None,options.get('language','en-US'))
            if p.resolved:recovered.append(p)
            else:unresolved.append({'handle':h,'reason':p.unresolved_reason,'depth':n.get('depth') if isinstance(n,dict) else None,'relation':n.get('relation') if isinstance(n,dict) else None,'placement':n.get('placement') if isinstance(n,dict) else None})
        total=len(nodes); cov=len(recovered)/total if total else 1.0
        oh=self._hash_obj([p.handle for p in recovered]+[x['handle'] for x in unresolved])
        return QMORecoveryResult(address_plan.get('qmo_id','qmo'),tuple(recovered),tuple(unresolved),cov,oh)
