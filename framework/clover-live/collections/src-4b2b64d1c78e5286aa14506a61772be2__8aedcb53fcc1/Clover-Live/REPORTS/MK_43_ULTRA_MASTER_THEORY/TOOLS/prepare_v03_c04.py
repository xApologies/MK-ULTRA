from __future__ import annotations
import hashlib,json,os
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; W=ROOT/"REPORTS/MK_43_ULTRA_MASTER_THEORY"; L=W/"chapter_ledger.jsonl"; A=ROOT/"MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"; CID="V03-C04"
H=sorted({"@api_interpretation","@canonical_artifact","@canonical_identity","@canonical_object","@canonical_presentation_route","@classification","@compile_recovered_object","@correspondence_registry","@handle_invocation_contract","@mathematical_object","@mathematical_registry","@object_identity_rule","@prime_mathematical_object","@proof_dependency_graph","@provenance","@realization_graph","@recovery_handle_contract","@recovery_intermediate_representation","@representation_graph","@required_object_classes","@source_graph","@stable_handle_naming","@theorem_graph","@type_declaration","@version_record"})
def sha(p):
 d=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(8388608),b""):d.update(b)
 return d.hexdigest()
def rows(p):return[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
def write(p,r):
 t=p.with_suffix(p.suffix+".tmp");t.write_text("".join(json.dumps(x,ensure_ascii=False,sort_keys=True)+"\n" for x in r),encoding="utf-8");os.replace(t,p)
def main():
 api={str(x["short_handle"]) for x in rows(A)};m=sorted(set(H)-api)
 if m:raise RuntimeError(m)
 r=rows(L);c=next(x for x in r if x["chapter_id"]==CID)
 if c.get("status")!="PLANNED" or c.get("path") is not None:raise RuntimeError("boundary changed")
 c.update({"handles":H,"handle_count":len(H),"assignment_basis":"Library 4.1 QMO identity, interpretation, representation, realization, theorem, proof, provenance, recovery, typing, registry, and version neighborhood","assignment_api_ledger_sha256":sha(A)});write(L,r)
 tp=W/"MASTER_TOC.md";t=tp.read_text(encoding="utf-8");old=f"- {CID} [PLANNED] Quantum Mathematical Objects - 1 assigned handles";new=f"- {CID} [PLANNED] Quantum Mathematical Objects - {len(H)} assigned handles"
 if old in t:tp.write_text(t.replace(old,new),encoding="utf-8",newline="\n")
 elif new not in t:raise RuntimeError("TOC boundary")
 q={"schema":"mk-ultra-tome-chapter-handle-assignment/v1","created_at":datetime.now(timezone.utc).isoformat(),"chapter_id":CID,"assigned_handle_count":len(H),"handles":H,"basis":"Native Library 4.1 QMO structural neighborhood expanded from the initialized @api_interpretation seed","library_api_ledger_path":A.relative_to(ROOT).as_posix(),"library_api_ledger_sha256":sha(A),"missing_handles":[],"chapter_ledger_sha256_after":sha(L)};(W/"V03_C04_handle_assignment_receipt.json").write_text(json.dumps(q,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8");print(json.dumps({"chapter_id":CID,"assigned":len(H)}))
if __name__=="__main__":main()
