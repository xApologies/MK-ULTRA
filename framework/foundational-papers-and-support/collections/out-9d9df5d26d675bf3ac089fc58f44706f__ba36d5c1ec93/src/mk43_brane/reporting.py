from pathlib import Path
from datetime import datetime, timezone
import re, os
from .errors import ReportGenerationError
class StreamingMarkdownRenderer:
    def build(self,q,outdir):
        if not q.realization: raise ReportGenerationError('no realization')
        directory=Path(outdir); directory.mkdir(parents=True,exist_ok=True); safe=re.sub(r'[^A-Za-z0-9._-]+','_',q.intent.subject.strip('@')) or 'report'; final=directory/f'{safe}_{q.request_id}.md'; partial=directory/f'.{safe}_{q.request_id}.partial'
        try:
            with partial.open('w',encoding='utf-8',newline='\n') as writer:
                writer.write(f'# {q.intent.title}\n\n## Recovery Metadata\n\n- Root: `{q.realization.root}`\n- Generated: {datetime.now(timezone.utc).isoformat()}\n- Model: `BRANE⁶ / Module⁵ / QMO⁶`\n\n')
                for depth,nodes in q.realization.layers():
                    writer.write(f'## Dependency Layer {depth}\n\n')
                    for node in nodes:
                        key=q.key_for_node(node); lifted=q.lifted[key]; package=q.packages.get(key); display=package.display_name if package else node.handle
                        writer.write(f'### {display} (`{node.handle}`)\n\n')
                        if node.parent: writer.write(f'**Dependency context:** `{node.parent}` —[{node.incoming_relation}]→ `{node.handle}`\n\n')
                        if not package or not package.resolved: writer.write(f'> Unresolved: `{package.unresolved_reason if package else "NOT_RETURNED"}`\n\n')
                        else:
                            for chunk in sorted(package.chunks,key=lambda x:(x.sequence,x.chunk_type,x.title)):
                                writer.write(f'#### {chunk.title}\n\n{chunk.content.rstrip()}\n\n')
                                if chunk.provenance: writer.write('**Provenance:** '+'; '.join(chunk.provenance)+'\n\n')
                        q.rendered_realizations.add(key)
                writer.write('## Continuation Handles\n\n'); writer.write('\n'.join(f'- `{h}`' for h in q.realization.continuation_handles) if q.realization.continuation_handles else 'None.'); writer.write('\n\n## Unresolved Coverage\n\n'); unresolved=q.coverage.unresolved if q.coverage else (); writer.write('\n'.join(f'- `{h}`' for h in unresolved) if unresolved else 'All realizations resolved.'); writer.write('\n')
                writer.flush(); os.fsync(writer.fileno())
            partial.replace(final); return final
        except Exception:
            partial.unlink(missing_ok=True); final.unlink(missing_ok=True); raise
