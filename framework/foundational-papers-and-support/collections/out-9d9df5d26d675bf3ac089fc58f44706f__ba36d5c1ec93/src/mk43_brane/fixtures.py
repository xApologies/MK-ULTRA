from .models import *
from .modules import *
from .loader import BraneLoader
def demo_modules():
    edges=[EdgeRecord('@genesis_field','GENERATES','@resolution','fixture',chirality='CHI:+'),EdgeRecord('@resolution','CONSTRAINS','@bandwidth','fixture',chirality='CHI:-'),EdgeRecord('@bandwidth','STABILIZES','@persistence','fixture',chirality='CHI:+'),EdgeRecord('@persistence','ORGANIZES','@chirality','fixture',chirality='CHI:-'),EdgeRecord('@chirality','PROJECTS_THROUGH','@time_shell','fixture',chirality='CHI:+'),EdgeRecord('@time_shell','REALIZES','@gravity','fixture',chirality='CHI:+')]
    api=InMemoryAPI5(edges,{'time shell':'@time_shell','gravity':'@gravity'},provenance={h:(f'fixture:{h}',) for h in {e.source for e in edges}|{e.target for e in edges}})
    ps={}
    for h in sorted({e.source for e in edges}|{e.target for e in edges}):
        name=h.strip('@').replace('_',' ').title(); ps[h]=KnowledgePackage(h,name,[KnowledgeChunk('definition','Definition',f'{name} is a recoverable component of the demonstration domain with a canonical dependency role.',0,provenance=(f'fixture:{h}',)),KnowledgeChunk('model','Model',f'Within this fixture, `{h}` participates in the typed dependency path and contributes to the requested realization.',1,provenance=(f'fixture:{h}',)),KnowledgeChunk('analogy','Analogy',f'Treat {name} as a station in a routed knowledge path whose handle requests a complete package.',2,provenance=(f'fixture:{h}',))],expected_chunk_types=('definition','model','analogy'))
    return BraneLoader.from_instances(DeterministicCollapseAI(),api,InMemoryLibrary5(ps))
