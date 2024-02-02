import networkx as nx
import copy
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def split_edge(graph: nx.Graph, v1: int, v2: int, node: int) -> nx.Graph:
    graph_copy = copy.deepcopy(graph)
    if not graph_copy.has_edge(v1, v2):
        raise Exception('no such edge')
    graph_copy.remove_edge(v1, v2)
    graph_copy.add_node(node)
    graph_copy.add_edge(v1, node)
    graph_copy.add_edge(node, v2)
    return graph_copy

def graph_diff(graph1: nx.Graph, graph2: nx.Graph) -> nx.Graph:
    graph_copy = copy.deepcopy(graph1)
    graph_copy.remove_edges_from(edge for edge in graph1.edges if edge in graph2.edges)
    # graph_copy.remove_nodes_from(node for node in graph1.nodes if node in graph2.nodes)
    return graph_copy

def graph_from_incidence_matrix(incidence_matrix) -> nx.Graph:
    adjacency_matrix = (np.dot(incidence_matrix, incidence_matrix.T) > 0).astype(int)
    np.fill_diagonal(adjacency_matrix, 0)
    G = nx.Graph(adjacency_matrix)
    return G

def print_graph(G):
    nx.draw(G, with_labels=True)

def main():
    graphs_to_print = []
    graphs_names = []
    G_incidence_matrix  = np.array([
        [1, 0, 0, 0, 0 ,0],
        [0, 1, 1, 0 ,0 ,0],
        [0, 1, 0, 1, 1, 0],
        [1, 0, 0 ,1 ,0 ,1],
        [0, 0, 1, 0, 1, 1],
    ])
    H_icidence_matrix = np.array([
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0 ,1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ])
    G = graph_from_incidence_matrix(G_incidence_matrix)
    H = graph_from_incidence_matrix(H_icidence_matrix)
    graphs_to_print.extend((G, H))
    graphs_names.extend(('G', 'H'))

    union = nx.compose(G, H)
    intersect = nx.intersection(G, H)
    G_extended = copy.deepcopy(G)
    G_extended.add_node(5)
    G_difference_H = graph_diff(G, H)
    H_difference_G = graph_diff(H, G)
    complement = nx.complement(G)
    graphs_to_print.extend((union, intersect, G_difference_H, H_difference_G, complement))
    graphs_names.extend(('union', 'intersect', 'G_difference_H', 'H_difference_G', 'complement'))

    G_without_edge = copy.deepcopy(G)
    G_without_edge.remove_edge(0, 3)

    G_with_vertex = copy.deepcopy(G)
    G_with_vertex.add_node(5)

    G_with_edge = copy.deepcopy(G)
    G_with_edge.add_edge(0, 4)

    G_without_vertex = copy.deepcopy(G)
    G_without_vertex.remove_node(4)

    graphs_to_print.extend((G_with_edge, G_without_edge, G_with_vertex, G_without_vertex))
    graphs_names.extend(('G_with_edge', 'G_without_edge', 'G_with_vertex', 'G_without_vertex'))

    G_with_contracted_nodes = nx.contracted_nodes(G, 0, 4)
    G_with_splitted_edge = split_edge(G, 0, 3, G.number_of_nodes())

    graphs_to_print.extend((G_with_contracted_nodes, G_with_splitted_edge))
    graphs_to_print.extend(('G_with_contracted_nodes', 'G_with_splitted_edge'))

    for idx, (graph_to_print, graph_name) in enumerate(zip(graphs_to_print, graphs_names)):
        # if not 'difference' in graph_name:
        #     continue
        fig = plt.figure(idx)
        fig.suptitle(graph_name)
        print_graph(graph_to_print)
    
    plt.show()

if __name__ == '__main__':
    main()