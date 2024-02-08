import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

def init_K5():
    return nx.complete_graph(5)

def init_K3_3():
    G = nx.Graph()
    for i in range(6):
        G.add_node(i)
    for i in range(3):
        for j in range(3, 6):
            G.add_edge(i, j)
    return G

def plt_graph(G, title):
    fig = plt.figure()
    fig.suptitle(title)
    nx.draw(G, with_labels=True)

def main():
    K3_3 = init_K3_3()
    K5 = init_K5()

    # all from K5

    K5_copy = deepcopy(K5)
    K5_copy.add_node(5)
    K5_copy.add_edge(0, 5)

    K3_3_copy_1 = deepcopy(K3_3)
    K3_3_copy_1.add_edge(0, 1)
    K3_3_copy_1.add_edge(1, 2)

    K3_3_copy_2 = deepcopy(K3_3)
    K3_3_copy_2.add_edge(0, 1)
    K3_3_copy_2.add_edge(3, 4)

    plt_graph(K5_copy, 'K5')
    plt_graph(K3_3_copy_1, 'K3_3 - 1')
    plt_graph(K3_3_copy_2, 'K3_3 - 2')
    plt.show()

if __name__ == "__main__":
    main()