#!/usr/bin/env python3
import sqlite3,json,argparse
from pathlib import Path
DB=Path(__file__).with_name("genesis_chirality_qmo.sqlite")
def rs(c,s,a=()):
 c.row_factory=sqlite3.Row; return [dict(r) for r in c.execute(s,a).fetchall()]
def main():
 p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
 q=sub.add_parser("get"); q.add_argument("address")
 q=sub.add_parser("search"); q.add_argument("term")
 q=sub.add_parser("deps"); q.add_argument("address")
 q=sub.add_parser("equations"); q.add_argument("address")
 q=sub.add_parser("provenance"); q.add_argument("address",nargs="?")
 sub.add_parser("open"); sub.add_parser("list"); sub.add_parser("status")
 a=p.parse_args(); c=sqlite3.connect(DB)
 if a.cmd=="get": out=rs(c,"SELECT * FROM v_qmo_current WHERE qmo_address=?",(a.address,))
 elif a.cmd=="search":
  t="%"+a.term+"%"; out=rs(c,"SELECT * FROM v_qmo_current WHERE qmo_address LIKE ? OR title LIKE ? OR summary LIKE ?",(t,t,t))
 elif a.cmd=="deps": out=rs(c,"SELECT * FROM v_dependencies WHERE source=? OR target=?",(a.address,a.address))
 elif a.cmd=="equations": out=rs(c,"SELECT * FROM v_equations WHERE qmo_address=?",(a.address,))
 elif a.cmd=="provenance": out=rs(c,"SELECT * FROM v_provenance"+(" WHERE qmo_address=?" if a.address else ""),(a.address,) if a.address else ())
 elif a.cmd=="open": out=rs(c,"SELECT * FROM v_open_questions WHERE status='OPEN' ORDER BY priority DESC")
 elif a.cmd=="list": out=rs(c,"SELECT qmo_address,title,object_type,authority,status FROM v_qmo_current ORDER BY qmo_address")
 else: out={"integrity":c.execute("PRAGMA integrity_check").fetchone()[0],"foreign_key_violations":len(c.execute("PRAGMA foreign_key_check").fetchall()),"qmos":c.execute("SELECT count(*) FROM qmo_objects").fetchone()[0],"equations":c.execute("SELECT count(*) FROM equations").fetchone()[0],"dependencies":c.execute("SELECT count(*) FROM dependencies").fetchone()[0],"provenance":c.execute("SELECT count(*) FROM provenance").fetchone()[0],"open_questions":c.execute("SELECT count(*) FROM open_questions WHERE status='OPEN'").fetchone()[0]}
 print(json.dumps(out,indent=2,ensure_ascii=False)); c.close()
if __name__=="__main__": main()
