"""MinimumSpanningTree.py

Kruskal's algorithm for minimum spanning trees. D. Eppstein, April 2006.
"""

import unittest
from UnionFind import UnionFind
from Graphs import isUndirected

def MinimumSpanningTree(G):
    """
    Return the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that iter(G) lists its
    vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    if not isUndirected(G):
        raise ValueError("MinimumSpanningTree: input is not undirected")
    for u in G:
        for v in G[u]:
            if G[u][v] != G[v][u]:
                raise ValueError("MinimumSpanningTree: asymmetric weights")

    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # We use Kruskal's algorithm, first because it is very simple to
    # implement once UnionFind exists, and second, because the only slow
    # part (the sort) is sped up by being built in to Python.
    subtrees = UnionFind()
    tree = []
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree

def MinimumSpanningCost(G):
    """
    Return the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that iter(G) lists its
    vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    if not isUndirected(G):
        raise ValueError("MinimumSpanningTree: input is not undirected")
    for u in G:
        for v in G[u]:
            if G[u][v] != G[v][u]:
                raise ValueError("MinimumSpanningTree: asymmetric weights")

    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # We use Kruskal's algorithm, first because it is very simple to
    # implement once UnionFind exists, and second, because the only slow
    # part (the sort) is sped up by being built in to Python.
    subtrees = UnionFind()
    #tree = []
    cost = 0
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            #tree.append((u,v))
            # MODIFYING. Instead of returning the tree, return the cost
            cost += G[u][v]
            subtrees.union(u,v)
    #return tree
    return cost