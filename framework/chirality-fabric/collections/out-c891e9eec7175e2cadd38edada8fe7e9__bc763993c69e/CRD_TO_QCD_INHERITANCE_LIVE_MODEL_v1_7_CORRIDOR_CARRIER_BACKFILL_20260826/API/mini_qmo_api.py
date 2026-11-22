#!/usr/bin/env python3
import sqlite3, sys, json
from pathlib import Path
DB=Path(__file__).resolve().parents[1]/'DATABASE'/'inheritance.sqlite3'

def rows(q,args=()):
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    out=[dict(r) for r in con.execute(q,args).fetchall()]; con.close(); return out

def emit(x): print(json.dumps(x,indent=2,ensure_ascii=False))

def main():
    if len(sys.argv)<2:
        print('commands: status | roadmap | run <ID> | object <HANDLE> | objects | equation <ID> | source <ID> | sources | open | retired | search <TERM> | meta')
        return
    cmd=sys.argv[1]
    if cmd=='status':
        emit({'meta':rows('select * from meta'), 'active':rows("select * from runs where status='ACTIVE'"), 'finish':rows("select * from runs where authority='FINISH_LINE'")})
    elif cmd=='roadmap': emit(rows('select * from runs order by rowid'))
    elif cmd=='run' and len(sys.argv)>2: emit(rows('select * from runs where id=?',(sys.argv[2].upper(),)))
    elif cmd=='object' and len(sys.argv)>2: emit(rows('select * from objects where handle=?',(sys.argv[2],)))
    elif cmd=='objects': emit(rows('select * from objects order by handle'))
    elif cmd=='equation' and len(sys.argv)>2: emit(rows('select * from equations where id=?',(sys.argv[2],)))
    elif cmd=='source' and len(sys.argv)>2: emit(rows('select * from sources where id=?',(sys.argv[2],)))
    elif cmd=='sources': emit(rows('select * from sources order by id'))
    elif cmd=='open': emit(rows("select * from open_questions where status in ('OPEN','LOCKED') order by id"))
    elif cmd=='retired': emit({'runs':rows("select * from runs where authority='RETIRED'"),'supersessions':rows('select * from supersessions order by id')})
    elif cmd=='meta': emit(rows('select * from meta order by key'))
    elif cmd=='search' and len(sys.argv)>2:
        term=' '.join(sys.argv[2:])
        try: emit(rows('select kind,key,text from search_fts where search_fts match ?',(term,)))
        except sqlite3.OperationalError: emit(rows('select kind,key,text from search_fts where text like ?',('%'+term+'%',)))
    else: raise SystemExit('bad command')
if __name__=='__main__': main()
