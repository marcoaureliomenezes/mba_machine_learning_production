import networkx as nx
import matplotlib.pyplot as plt


def plot_bidirectional_graph(adjacent_list):
    G = nx.DiGraph(adjacent_list)
    nx.draw(G, with_labels=True)
    plt.show()
