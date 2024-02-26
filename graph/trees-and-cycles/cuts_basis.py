import numpy as np
from copy import deepcopy
import networkx as nx

FLOAT_ERROR = 1e-10
def main():
    G = nx.complete_bipartite_graph(3, 3)
    spanning_tree = nx.random_spanning_tree(G)
    cuts = []
    for edge in spanning_tree.edges:
        cut_edges = []
        cuts.append(cut_edges)
        clonned = deepcopy(spanning_tree)
        clonned.remove_edge(edge[0], edge[1])
        component1, component2 = nx.connected_components(clonned)
        for connecting_edge in spanning_tree.edges:
            if (connecting_edge[0] in component1 and connecting_edge[1] in component2) or (connecting_edge[0] in component2 and connecting_edge[1] in component1):
                cut_edges.append(connecting_edge)

    print(cuts)
    print(len(cuts))

if __name__ == "__main__":
    main()
