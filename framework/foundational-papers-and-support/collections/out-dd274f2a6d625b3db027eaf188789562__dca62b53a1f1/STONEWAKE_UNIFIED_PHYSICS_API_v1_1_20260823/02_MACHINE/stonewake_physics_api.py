#!/usr/bin/env python3
"""STONEWAKE Unified Physics QMO v1.1 query/compiler surface."""
from __future__ import annotations
import sqlite3, json, argparse, re
from collections import deque
from pathlib import Path
DB=Path(__file__).with_name("STONEWAKE_PHYSICS_QMO.sqlite")

def connect():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def stats():
    with connect() as c:
        out={t:c.execute(f"select count(*) n from {t}").fetchone()['n'] for t in ('objects','equations','edges')}
        out['templates']=c.execute('select count(*) n from templates').fetchone()['n']
        return out

def object(handle):
    with connect() as c:
        return [dict(r) for r in c.execute("select * from objects where handle=? order by domain",(handle,))]

def _tokens(q): return [t for t in re.split(r'[^A-Za-z0-9_@]+',q.lower()) if t]

def search(query, limit=30):
    """Precision ladder: exact handle/name -> exact phrase -> token AND -> token OR fallback."""
    with connect() as c:
        out={'query':query,'mode':None,'objects':[],'equations':[]}
        # exact handle/name first
        rows=[dict(r) for r in c.execute("select * from objects where lower(handle)=lower(?) or lower(name)=lower(?) limit ?",(query,query,limit))]
        eqs=[dict(r) for r in c.execute("select * from equations where lower(uid)=lower(?) or lower(owner)=lower(?) limit ?",(query,query,limit))]
        if rows or eqs:
            out.update(mode='exact',objects=rows,equations=eqs); return out
        # exact phrase substring
        like=f'%{query}%'
        rows=[dict(r) for r in c.execute("select * from objects where handle like ? or name like ? or definition like ? limit ?",(like,like,like,limit))]
        eqs=[dict(r) for r in c.execute("select * from equations where expression like ? or meaning like ? or owner like ? limit ?",(like,like,like,limit))]
        if rows or eqs:
            out.update(mode='phrase',objects=rows,equations=eqs); return out
        toks=_tokens(query)
        if toks:
            andq=' AND '.join(t+'*' for t in toks)
            try:
                rows=[dict(r) for r in c.execute("select o.* from object_fts f join objects o on o.id=f.rowid where object_fts match ? limit ?",(andq,limit))]
                eqs=[dict(r) for r in c.execute("select e.* from equation_fts f join equations e on e.id=f.rowid where equation_fts match ? limit ?",(andq,limit))]
                if rows or eqs:
                    out.update(mode='and',objects=rows,equations=eqs); return out
                orq=' OR '.join(t+'*' for t in toks)
                rows=[dict(r) for r in c.execute("select o.* from object_fts f join objects o on o.id=f.rowid where object_fts match ? limit ?",(orq,limit))]
                eqs=[dict(r) for r in c.execute("select e.* from equation_fts f join equations e on e.id=f.rowid where equation_fts match ? limit ?",(orq,limit))]
                out.update(mode='or_fallback',objects=rows,equations=eqs); return out
            except sqlite3.OperationalError: pass
        out['mode']='none'; return out

def equations(query=None, owner=None, domain=None, limit=100):
    with connect() as c:
        sql='select * from equations where 1=1'; args=[]
        if owner: sql+=' and owner=?'; args.append(owner)
        if domain: sql+=' and domain=?'; args.append(domain)
        if query:
            like=f'%{query}%'; sql+=' and (expression like ? or meaning like ? or owner like ? or uid like ?)'; args += [like]*4
        sql+=' limit ?'; args.append(limit)
        return [dict(r) for r in c.execute(sql,args)]

def route(source,target,max_depth=16,relations=None):
    with connect() as c:
        q=deque([(source,[])]); seen={source}
        while q:
            node,path=q.popleft()
            if len(path)>=max_depth: continue
            rows=c.execute("select source,target,relation,domain,status,confidence from edges where source=?",(node,)).fetchall()
            for r in rows:
                if relations and r['relation'] not in relations: continue
                step=dict(r); nxt=r['target']; np=path+[step]
                if nxt==target: return np
                if nxt not in seen: seen.add(nxt); q.append((nxt,np))
    return None

def _expand_handles(seeds,depth=2,direction='both',max_nodes=400):
    with connect() as c:
        seen=set(seeds); frontier=list(seeds); traversed=[]
        for _ in range(depth):
            nxt=[]
            for h in frontier:
                clauses=[]; args=[]
                if direction in ('out','both'): clauses.append('source=?'); args.append(h)
                if direction in ('in','both'): clauses.append('target=?'); args.append(h)
                if not clauses: continue
                sql='select * from edges where '+ ' or '.join(clauses)
                for r in c.execute(sql,args):
                    d=dict(r); traversed.append(d)
                    other=r['target'] if r['source']==h else r['source']
                    if other not in seen and len(seen)<max_nodes:
                        seen.add(other); nxt.append(other)
            frontier=nxt
            if not frontier: break
        return list(seen),traversed

def local_qmo(concepts,depth=2,limit_per_concept=20,max_nodes=400):
    """Resolve concepts, then expand the dependency fabric into a bounded local mathematical object."""
    if isinstance(concepts,str): concepts=[concepts]
    seed_handles=[]; seed_eq=[]; search_log=[]
    with connect() as c:
        for concept in concepts:
            s=search(concept,limit_per_concept); search_log.append({'concept':concept,'mode':s['mode']})
            for o in s['objects']:
                if o['handle'] not in seed_handles: seed_handles.append(o['handle'])
            for e in s['equations']:
                if e['uid'] not in seed_eq: seed_eq.append(e['uid'])
        handles,edges=_expand_handles(seed_handles,depth=depth,max_nodes=max_nodes)
        objects=[]
        if handles:
            ph=','.join('?'*len(handles)); objects=[dict(r) for r in c.execute(f"select * from objects where handle in ({ph}) order by handle,domain",handles)]
        eqs=[]; seen=set(seed_eq)
        for uid in seed_eq:
            r=c.execute('select * from equations where uid=?',(uid,)).fetchone()
            if r: eqs.append(dict(r))
        if handles:
            ph=','.join('?'*len(handles))
            for r in c.execute(f"select * from equations where owner in ({ph}) order by owner,uid",handles):
                if r['uid'] not in seen: seen.add(r['uid']); eqs.append(dict(r))
    return {'root':'@stonewake_physics','concepts':concepts,'search_log':search_log,'seed_handles':seed_handles,'objects':objects,'equations':eqs,'edges':edges,'closure':{'depth':depth,'bounded_nodes':len(handles),'status':'BOUNDED_DEPENDENCY_VIEW'}}

def templates(name=None):
    with connect() as c:
        if name:
            r=c.execute('select * from templates where name=?',(name,)).fetchone(); return dict(r) if r else None
        return [dict(r) for r in c.execute('select * from templates order by name')]

def derive(name,depth=2):
    t=templates(name)
    if not t: return {'error':'unknown template','name':name}
    req=json.loads(t['required_handles_json']); opt=json.loads(t['optional_handles_json'])
    q=local_qmo([t['model_handle']]+req,depth=depth)
    with connect() as c:
        missing=[h for h in req if not c.execute('select 1 from objects where handle=?',(h,)).fetchone()]
        open_objs=[]
        for h in req+opt:
            for r in c.execute("select handle,status,definition from objects where handle=? and status like 'OPEN%'",(h,)):
                open_objs.append(dict(r))
    q['template']=t; q['required_handles']=req; q['optional_handles']=opt; q['missing_required_handles']=missing; q['open_requirements']=open_objs
    q['status']='READY_AS_ABSTRACT_QMO' if not missing else 'UNRESOLVED_REQUIRED_HANDLES'
    return q

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('stats')
    p=sub.add_parser('search'); p.add_argument('query'); p.add_argument('--limit',type=int,default=30)
    p=sub.add_parser('object'); p.add_argument('handle')
    p=sub.add_parser('equations'); p.add_argument('query',nargs='?'); p.add_argument('--owner'); p.add_argument('--domain'); p.add_argument('--limit',type=int,default=100)
    p=sub.add_parser('route'); p.add_argument('source'); p.add_argument('target'); p.add_argument('--max-depth',type=int,default=16)
    p=sub.add_parser('local-qmo'); p.add_argument('concepts',nargs='+'); p.add_argument('--depth',type=int,default=2)
    p=sub.add_parser('templates'); p.add_argument('name',nargs='?')
    p=sub.add_parser('derive'); p.add_argument('name'); p.add_argument('--depth',type=int,default=2)
    a=ap.parse_args()
    if a.cmd=='stats': x=stats()
    elif a.cmd=='search': x=search(a.query,a.limit)
    elif a.cmd=='object': x=object(a.handle)
    elif a.cmd=='equations': x=equations(a.query,a.owner,a.domain,a.limit)
    elif a.cmd=='route': x=route(a.source,a.target,a.max_depth)
    elif a.cmd=='local-qmo': x=local_qmo(a.concepts,a.depth)
    elif a.cmd=='templates': x=templates(a.name)
    else: x=derive(a.name,a.depth)
    print(json.dumps(x,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
