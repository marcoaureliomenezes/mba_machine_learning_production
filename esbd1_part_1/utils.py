import networkx as nx
import matplotlib.pyplot as plt
import csv

def generate_graph_plot(adjacent_list):
    G = nx.DiGraph(adjacent_list)
    nx.draw(G, with_labels=True)
    plt.show()


def append_csv(path, data):
    with open(path, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)