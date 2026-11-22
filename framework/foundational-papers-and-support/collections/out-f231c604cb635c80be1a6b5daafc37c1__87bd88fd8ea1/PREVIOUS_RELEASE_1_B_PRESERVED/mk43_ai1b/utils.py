import hashlib,json,time

def stable_hash(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),default=lambda x:getattr(x,'__dict__',str(x))).encode()).hexdigest()

def edge_key(e): return (str(getattr(e,'relation','')),str(getattr(e,'target','')),str(getattr(e,'source','')),str(getattr(e,'provenance','') or ''))
def direction_value(v): return getattr(v,'value',v)
def coverage_value(v): return getattr(v,'value',v)
