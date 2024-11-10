from ...classes.graph import Graph

__all__ = [
    "union",
    "compose",
    "disjoint_union",
    "intersection",
    "difference",
    "symmetric_difference",
    "full_join",
]

def union(G: Graph, H, rename: tuple = ..., name: str | None = None): ...
def disjoint_union(G: Graph, H): ...
def intersection(G: Graph, H): ...
def difference(G: Graph, H): ...
def symmetric_difference(G: Graph, H): ...
def compose(G: Graph, H): ...
def full_join(G: Graph, H, rename: tuple = ...): ...
