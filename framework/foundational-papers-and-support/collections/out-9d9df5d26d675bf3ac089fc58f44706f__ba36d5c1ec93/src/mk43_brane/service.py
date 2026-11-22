from __future__ import annotations
import multiprocessing as mp
from pathlib import Path
from .brane import Brane
from .models import RuntimeResponse, ArtifactReceipt


def _worker(conn,modules,output_dir):
    brane=Brane(modules,output_dir)
    try:
        while True:
            msg=conn.recv()
            op=msg.get('op')
            if op=='handle': conn.send(brane.handle(msg['payload']).to_dict())
            elif op=='replace':
                try: conn.send({'ok':True,'value':brane.replace_module(msg['role'],msg['candidate'])})
                except Exception as e: conn.send({'ok':False,'error':type(e).__name__})
            elif op=='close': conn.send({'ok':True}); break
            else: conn.send({'ok':False,'error':'invalid operation'})
    finally:
        brane.close(); conn.close()

class IsolatedBrane:
    """Runtime-facing process boundary. The runtime holds only this IPC client."""
    __slots__=('__conn','__proc')
    def __init__(self,modules,output_dir):
        ctx=mp.get_context('fork') if 'fork' in mp.get_all_start_methods() else mp.get_context()
        parent,child=ctx.Pipe(); proc=ctx.Process(target=_worker,args=(child,modules,str(Path(output_dir))),daemon=True); proc.start(); child.close(); self.__conn=parent; self.__proc=proc
    def handle(self,envelope):
        self.__conn.send({'op':'handle','payload':envelope}); d=self.__conn.recv(); art=d.get('artifact'); receipt=ArtifactReceipt(**art) if art else None; return RuntimeResponse(d['request_id'],d['status'],receipt,d.get('recovery_receipt',{}),tuple(d.get('errors',())))
    def replace_module(self,role,candidate):
        self.__conn.send({'op':'replace','role':role,'candidate':candidate}); out=self.__conn.recv()
        if not out.get('ok'): raise RuntimeError(out.get('error','replacement failed'))
        return out['value']
    def close(self):
        if self.__proc.is_alive():
            self.__conn.send({'op':'close'}); self.__conn.recv(); self.__proc.join(timeout=5)
            if self.__proc.is_alive(): self.__proc.terminate()
        self.__conn.close()
    def __dir__(self): return ['close','handle','replace_module']
