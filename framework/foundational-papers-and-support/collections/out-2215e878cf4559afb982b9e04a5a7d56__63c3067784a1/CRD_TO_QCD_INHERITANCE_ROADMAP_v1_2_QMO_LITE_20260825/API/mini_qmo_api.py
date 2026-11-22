#!/usr/bin/env python3
import sqlite3, sys, json
from pathlib import Path
DB=Path(__file__).resolve().parents[1]/'DATABASE'/'inheritance.sqlite3'

def rows(q,args=()):
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    out=[dict(r) for r in con.execute(q,args).fetchall()]; con.close(); return out

def main():
    if len(sys.argv)<2:
        print('commands: roadmap | run <ID> | recover <term> | open | objects') ; return
    cmd=sys.argv[1]
    if cmd=='roadmap':
        print(json.dumps(rows('select * from runs order by id'),indent=2))
    elif cmd=='run' and len(sys.argv)>2:
        print(json.dumps(rows('select * from runs where id=?',(sys.argv[2].upper(),)),indent=2))
    elif cmd=='objects':
        print(json.dumps(rows('select * from objects order by handle'),indent=2))
    elif cmd=='open':
        print(json.dumps(rows("select * from open_questions where status in ('OPEN','LOCKED') order by id"),indent=2))
    elif cmd=='recover' and len(sys.argv)>2:
        term=' '.join(sys.argv[2:])
        print(json.dumps(rows('select kind,key,text from search_fts where search_fts match ?',(term,)),indent=2))
    else:
        raise SystemExit('bad command')
if __name__=='__main__': main()
