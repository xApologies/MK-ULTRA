from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from mk43_brane.contracts.models import (
    RuntimeRequest, CompiledRequest, CanonicalGraph, TraversalRealization,
    TraversalNode,
)


@dataclass
class DeterministicCollapseIntelligence:
    """Standalone AI-port implementation of the 5.0–5.2 collapse contract."""

    version: str = "1.0.0"
    contract_version: str = "1.0"
    default_max_depth: int = 256
    default_edge_budget: int = 100_000

    def compile_request(self, request: RuntimeRequest) -> CompiledRequest:
        title = request.title or f"{request.subject.lstrip('@').replace('_', ' ').title()} Recovery Report"
        policy = {
            "max_depth": int(request.options.get("max_depth", self.default_max_depth)),
            "edge_budget": int(request.options.get("edge_budget", self.default_edge_budget)),
            "order": request.options.get("order", "stable"),
            "termination_handles": tuple(request.options.get("termination_handles", [])),
        }
        return CompiledRequest(
            operation=request.operation,
            subject=request.subject,
            root_hint=request.subject,
            language=request.language,
            format=request.format,
            depth=request.depth,
            direction=request.direction,
            coverage_mode=request.coverage_mode,
            title=title,
            policy=policy,
        )

    def realize(self, graph: CanonicalGraph, request: CompiledRequest) -> TraversalRealization:
        out = TraversalRealization(root=graph.root)
        max_depth = request.policy["max_depth"]
        edge_budget = request.policy["edge_budget"]
        termination = set(request.policy.get("termination_handles", ()))
        visited: set[str] = set()
        queued: set[str] = {graph.root}
        queue = deque([(graph.root, 0, None, None)])
        order = 0
        inspected = 0

        while queue:
            handle, depth, parent, relation = queue.popleft()
            queued.discard(handle)
            if handle in visited:
                if parent is not None:
                    out.cycle_references.append((parent, handle))
                continue
            visited.add(handle)
            kind = "root" if handle == graph.root else "branch"
            out.ordered_nodes.append(TraversalNode(handle, depth, parent, relation, order, kind))
            order += 1

            candidates = sorted(
                graph.neighbors(handle, request.direction),
                key=lambda edge: (edge.relation, edge.target, edge.source),
            )
            for edge in candidates:
                inspected += 1
                if inspected > edge_budget:
                    out.frontier.append(edge.target)
                    continue
                candidate = edge.target
                if candidate in visited or candidate in queued:
                    out.cycle_references.append((handle, candidate))
                    continue
                if candidate in termination or depth + 1 >= max_depth:
                    out.ordered_nodes.append(
                        TraversalNode(candidate, depth + 1, handle, edge.relation, order, "leaf")
                    )
                    order += 1
                    out.continuation_handles.append(candidate)
                    visited.add(candidate)
                    continue
                queue.append((candidate, depth + 1, handle, edge.relation))
                queued.add(candidate)

        return out


def create_port() -> DeterministicCollapseIntelligence:
    return DeterministicCollapseIntelligence()
