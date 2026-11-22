from __future__ import annotations
import hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
WORKSPACE=ROOT/"REPORTS/MK_43_ULTRA_MASTER_THEORY"
LEDGER=WORKSPACE/"chapter_ledger.jsonl"
API_LEDGER=ROOT/"MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
CHAPTER_ID="V02-C10"
HANDLES=sorted({
    "@canonical_artifact","@canonical_identity","@canonical_object","@canonical_presentation_route",
    "@classification","@compile_recovered_object","@concept_lookup_endpoint","@correspondence_registry",
    "@handle_invocation_contract","@mathematical_object","@mathematical_registry","@object_identity_rule",
    "@prime_mathematical_object","@proof_dependency_graph","@provenance","@realization_graph",
    "@recovery_handle_contract","@recovery_intermediate_representation","@representation_graph",
    "@required_object_classes","@source_graph","@stable_handle_naming","@theorem_graph",
    "@type_declaration","@version_record",
})

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
    rows=read_jsonl(LEDGER); chapter=next(r for r in rows if r["chapter_id"]==CHAPTER_ID)
    if chapter.get("status")!="PLANNED" or chapter.get("path") is not None: raise RuntimeError("chapter boundary changed")
    api={str(r["short_handle"]) for r in read_jsonl(API_LEDGER)}; missing=sorted(set(HANDLES)-api)
    if missing: raise RuntimeError(f"handles absent from Library 4.1: {missing}")
    chapter.update({"handles":HANDLES,"handle_count":len(HANDLES),"assignment_basis":"Library 4.1 QMO identity, type, class, registry, graph, provenance, version, recovery, and presentation address set","assignment_api_ledger_sha256":sha256(API_LEDGER)})
    write_jsonl(LEDGER,rows)
    toc_path=WORKSPACE/"MASTER_TOC.md"; toc=toc_path.read_text(encoding="utf-8")
    old=f"- {CHAPTER_ID} [PLANNED] QMO Grammar - 0 assigned handles"; new=f"- {CHAPTER_ID} [PLANNED] QMO Grammar - {len(HANDLES)} assigned handles"
    if old in toc: toc_path.write_text(toc.replace(old,new),encoding="utf-8",newline="\n")
    elif new not in toc: raise RuntimeError("TOC assignment boundary is unexpected")
    receipt={"schema":"mk-ultra-tome-chapter-handle-assignment/v1","created_at":datetime.now(timezone.utc).isoformat(),"chapter_id":CHAPTER_ID,"assigned_handle_count":len(HANDLES),"handles":HANDLES,"basis":"Native Library 4.1 address selection for persistent QMO grammar and provenance-preserving compilation","library_api_ledger_path":API_LEDGER.relative_to(ROOT).as_posix(),"library_api_ledger_sha256":sha256(API_LEDGER),"missing_handles":[],"chapter_ledger_sha256_after":sha256(LEDGER)}
    (WORKSPACE/"V02_C10_handle_assignment_receipt.json").write_text(json.dumps(receipt,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"chapter_id":CHAPTER_ID,"assigned":len(HANDLES)}))

if __name__=="__main__": main()
