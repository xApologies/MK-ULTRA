from __future__ import annotations
import hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
WORKSPACE=ROOT/"REPORTS/MK_43_ULTRA_MASTER_THEORY"
LEDGER=WORKSPACE/"chapter_ledger.jsonl"
API_LEDGER=ROOT/"MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
CHAPTER_ID="V03-C01"
HANDLES=["@api_contract"]

def sha256(path:Path)->str:
    d=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(8*1024*1024),b""): d.update(b)
    return d.hexdigest()

def read_jsonl(path:Path)->list[dict[str,object]]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def write_jsonl(path:Path,rows:list[dict[str,object]])->None:
    t=path.with_suffix(path.suffix+".tmp")
    t.write_text("".join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding="utf-8")
    os.replace(t,path)

def main()->None:
    api={str(r["short_handle"]) for r in read_jsonl(API_LEDGER)}
    if HANDLES[0] not in api: raise RuntimeError("@api_contract absent from Library 4.1")
    rows=read_jsonl(LEDGER); chapter=next(r for r in rows if r["chapter_id"]==CHAPTER_ID)
    if chapter.get("status")!="PLANNED" or chapter.get("path") is not None: raise RuntimeError("chapter boundary changed")
    if chapter.get("handles")!=HANDLES or int(chapter.get("handle_count") or 0)!=1: raise RuntimeError("preassigned API contract changed")
    chapter.update({"assignment_basis":"Library 4.1 canonical API contract address defining the constrained interface boundary for API 4.3","assignment_api_ledger_sha256":sha256(API_LEDGER)})
    write_jsonl(LEDGER,rows)
    toc=(WORKSPACE/"MASTER_TOC.md").read_text(encoding="utf-8")
    expected=f"- {CHAPTER_ID} [PLANNED] API 4.3 as a Constrained Mathematical Domain - 1 assigned handles"
    if expected not in toc: raise RuntimeError("TOC assignment boundary is unexpected")
    receipt={"schema":"mk-ultra-tome-chapter-handle-assignment/v1","created_at":datetime.now(timezone.utc).isoformat(),"chapter_id":CHAPTER_ID,"assigned_handle_count":1,"handles":HANDLES,"basis":"Native Library 4.1 canonical API contract address preserved from the initialized chapter ledger","library_api_ledger_path":API_LEDGER.relative_to(ROOT).as_posix(),"library_api_ledger_sha256":sha256(API_LEDGER),"missing_handles":[],"chapter_ledger_sha256_after":sha256(LEDGER)}
    (WORKSPACE/"V03_C01_handle_assignment_receipt.json").write_text(json.dumps(receipt,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"chapter_id":CHAPTER_ID,"assigned":1}))

if __name__=="__main__": main()
