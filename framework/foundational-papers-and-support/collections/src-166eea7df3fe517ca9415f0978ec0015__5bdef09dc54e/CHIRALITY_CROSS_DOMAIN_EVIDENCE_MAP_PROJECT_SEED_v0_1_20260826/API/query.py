#!/usr/bin/env python3
import sqlite3,sys,json
from pathlib import Path

DB=Path(__file__).resolve().parents[1]/"DATABASE"/"chirality_evidence.sqlite3"

def rows(q,args=()):
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    out=[dict(r) for r in con.execute(q,args).fetchall()]
    con.close(); return out

def emit(x): print(json.dumps(x,indent=2,ensure_ascii=False))

def main():
    if len(sys.argv)<2:
        print("commands: status | roadmap | domains | domain <ID> | objects | object <HANDLE> | claims | claim <ID> | mappings | sources | gaps | chronology | supersessions | search <TERM>")
        return
    cmd=sys.argv[1]
    if cmd=="status":
        emit({"meta":rows("select * from meta order by key"),
              "resume":rows("select * from roadmap where authority='RESUME_TARGET'"),
              "finish":rows("select * from roadmap where authority='FINISH_LINE'")})
    elif cmd=="roadmap": emit(rows("select * from roadmap order by rowid"))
    elif cmd=="domains": emit(rows("select * from domains order by id"))
    elif cmd=="domain" and len(sys.argv)>2: emit(rows("select * from domains where id=?",(sys.argv[2],)))
    elif cmd=="objects": emit(rows("select * from objects order by handle"))
    elif cmd=="object" and len(sys.argv)>2: emit(rows("select * from objects where handle=?",(sys.argv[2],)))
    elif cmd=="claims": emit(rows("select * from claims order by id"))
    elif cmd=="claim" and len(sys.argv)>2: emit(rows("select * from claims where id=?",(sys.argv[2],)))
    elif cmd=="mappings": emit(rows("select * from mappings order by id"))
    elif cmd=="sources": emit(rows("select * from sources order by id"))
    elif cmd=="gaps": emit(rows("select * from gaps order by id"))
    elif cmd=="chronology": emit(rows("select * from chronology order by date,id"))
    elif cmd=="supersessions": emit(rows("select * from supersessions order by id"))
    elif cmd=="search" and len(sys.argv)>2:
        term=" ".join(sys.argv[2:])
        try: emit(rows("select kind,key,text from search_fts where search_fts match ?",(term,)))
        except sqlite3.OperationalError: emit(rows("select kind,key,text from search_index where text like ?",("%"+term+"%",)))
    else:
        raise SystemExit("bad command")
if __name__=="__main__": main()
