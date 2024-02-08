import networkx as nx
import matplotlib.pyplot as plt

def init_K3_3():
    G = nx.Graph()
    for i in range(6):
        G.add_node(i)
    for i in range(3):
        for j in range(3, 6):
            G.add_edge(i, j)
    return G

def init_G():
    K3_3 = init_K3_3()
    K3_3.add_edge(0, 1)
    K3_3.add_edge(1, 2)
    K3_3.add_edge(4, 5)
    return K3_3

def plt_graph(G, title, colors):
    fig = plt.figure()
    fig.suptitle(title)
    nx.draw_networkx(G, node_color=colors)

def main():
    G = init_G()
    plt_graph(G, 'bare', ['blue'] * 6)
    plt_graph(G, 'K5', ['blue'] * 3 +['red'] + ['blue'] * 2)
    plt_graph(G, 'K3_3', ['blue'] * 3 +['red'] * 3)
    plt.show()

if __name__ == "__main__":
    main()
