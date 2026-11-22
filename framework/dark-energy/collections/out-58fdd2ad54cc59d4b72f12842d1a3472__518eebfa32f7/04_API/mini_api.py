#!/usr/bin/env python3
import sqlite3, argparse, json
from pathlib import Path

DB = Path(__file__).with_name("genesis_chirality_closure_qmo.sqlite")

def rows(con, sql, args=()):
    con.row_factory=sqlite3.Row
    return [dict(r) for r in con.execute(sql,args).fetchall()]

def main():
    ap=argparse.ArgumentParser(description="GENESIS Chirality Fabric closure QMO mini API")
    sp=ap.add_subparsers(dest="cmd",required=True)

    p=sp.add_parser("get"); p.add_argument("address")
    p=sp.add_parser("search"); p.add_argument("term")
    p=sp.add_parser("deps"); p.add_argument("address")
    p=sp.add_parser("equations"); p.add_argument("address")
    p=sp.add_parser("provenance"); p.add_argument("address",nargs="?")
    p=sp.add_parser("closure"); p.add_argument("address",nargs="?")
    sp.add_parser("frontier")
    sp.add_parser("retired")
    sp.add_parser("sources")
    sp.add_parser("status")

    a=ap.parse_args()
    con=sqlite3.connect(DB)

    if a.cmd=="get":
        out=rows(con,"SELECT * FROM v_qmo_current WHERE qmo_address=?",(a.address,))
    elif a.cmd=="search":
        t=f"%{a.term}%"
        out=rows(con,"SELECT * FROM v_qmo_current WHERE qmo_address LIKE ? OR title LIKE ? OR definition LIKE ? OR summary LIKE ? ORDER BY qmo_address",(t,t,t,t))
    elif a.cmd=="deps":
        out=rows(con,"SELECT * FROM v_dependencies WHERE source=? OR target=? ORDER BY source,relation,target",(a.address,a.address))
    elif a.cmd=="equations":
        out=rows(con,"SELECT * FROM v_equation_ledger WHERE qmo_address=? ORDER BY equation_id",(a.address,))
    elif a.cmd=="provenance":
        if a.address:
            out=rows(con,"SELECT * FROM v_provenance WHERE qmo_address=? ORDER BY provenance_id",(a.address,))
        else:
            out=rows(con,"SELECT * FROM v_provenance ORDER BY provenance_id")
    elif a.cmd=="closure":
        if a.address:
            out=rows(con,"SELECT * FROM v_closure WHERE qmo_address=? ORDER BY closure_id",(a.address,))
        else:
            out=rows(con,"SELECT * FROM v_closure ORDER BY closure_id")
    elif a.cmd=="frontier":
        out=rows(con,"SELECT * FROM v_open_frontier ORDER BY priority DESC,frontier_id")
    elif a.cmd=="retired":
        out=rows(con,"SELECT * FROM v_retired_aliases ORDER BY alias")
    elif a.cmd=="sources":
        out=rows(con,"SELECT * FROM v_sources ORDER BY source_id")
    else:
        out={
            "integrity":con.execute("PRAGMA integrity_check").fetchone()[0],
            "foreign_key_violations":len(con.execute("PRAGMA foreign_key_check").fetchall()),
            "qmo_objects":con.execute("SELECT count(*) FROM qmo_objects").fetchone()[0],
            "equations":con.execute("SELECT count(*) FROM equations").fetchone()[0],
            "dependencies":con.execute("SELECT count(*) FROM dependencies").fetchone()[0],
            "provenance_events":con.execute("SELECT count(*) FROM provenance").fetchone()[0],
            "closure_records":con.execute("SELECT count(*) FROM closure_records").fetchone()[0],
            "open_frontier":con.execute("SELECT count(*) FROM open_frontier WHERE status='OPEN'").fetchone()[0],
            "sources":con.execute("SELECT count(*) FROM source_receipts").fetchone()[0]
        }
    print(json.dumps(out,indent=2,ensure_ascii=False))
    con.close()

if __name__=="__main__":
    main()
