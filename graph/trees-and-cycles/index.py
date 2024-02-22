import networkx as nx
import numpy as np

FLOAT_ERROR = 1e-10
def main():
    G1 = nx.cubical_graph()
    G2 = nx.complete_bipartite_graph(3, 3)
    labels = ("cube", "K3,3")
    graphs = (G1, G2)
    for G, label in zip(graphs, labels):
        laplacian = nx.laplacian_matrix(G)
        laplacian = laplacian.toarray()
        eigh_vals = np.linalg.eigvals(laplacian)
        non_zero_eigh = np.abs(eigh_vals) >= FLOAT_ERROR
        if np.invert(non_zero_eigh).sum() != 1:
            raise Exception("expectde only 1 zero element")
        eigh_vals = eigh_vals[non_zero_eigh]
        trees_count = eigh_vals.prod()
        trees_count /= laplacian.shape[0]
        if np.abs(trees_count - round(trees_count)) >= FLOAT_ERROR:
            raise Exception(f"expected integer trees count, but got {trees_count=}")
        trees_count = round(trees_count)
        print(f"{trees_count=} for graph {label}")

if __name__ == "__main__":
    main()