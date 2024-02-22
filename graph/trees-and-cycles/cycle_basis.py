import numpy as np
from copy import deepcopy
import networkx as nx

FLOAT_ERROR = 1e-10
def main():
    G = nx.complete_bipartite_graph(3, 3)
    spanning_tree = nx.random_spanning_tree(G)
    # spanning_tree count should be edges - verticies + 1
    complement = nx.complement(deepcopy(spanning_tree))
    cycles = []
    for edge in complement.edges:
        clonned = deepcopy(spanning_tree)
        clonned.add_edge(edge[0], edge[1])
        cycle = nx.find_cycle(clonned)
        cycles.append(cycle)
    print(cycles)
    print(len(cycles))

if __name__ == "__main__":
    main()