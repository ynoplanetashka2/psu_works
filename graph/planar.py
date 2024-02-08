import networkx as nx
import matplotlib.pyplot as plt

def init_G():
    G = nx.Graph()
    for i in range(7):
        G.add_node(i)
    for i in range(7):
        G.add_edge(i, (i + 1) % 7)
    for i in range(7):
        shift = 2
        G.add_edge(i, (i + shift) % 7)
        G.add_edge((i + shift) % 7, (i + 2 * shift) % 7)
    return G

def main():
    G = init_G()
    is_planar, counterexample = nx.check_planarity(G, True)
    print(is_planar, counterexample)
    nx.draw(counterexample, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()