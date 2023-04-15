from functools import reduce
import random
import networkx as nx
import matplotlib.pyplot as plt


# Classe para representar uma localização. Cada localização possui um identificador único e um indicador de segurança
class Location(object):


    __uid: int = None
    __is_safety: bool = None

    # Construtor da classe
    def __init__(self, uid, safe_chance) -> None:
        self.__uid = uid
        self.__is_safety = True if random.random() < safe_chance else False

    # Método getter para o identificador único
    def get_uid(self) :
        return self.__uid
    

    # Método getter para indicador de segurança da localidade
    def get_safety(self) -> bool:
        return self.__is_safety


# Classe para representar um grafo de localizações com conexões bidirecionais entre elas.
class Graph(object):

    __graph: dict = None
    __num_locations: int = None
    __num_connections: int = None

    # Construtor da classe
    def __init__(self, num_locations, num_connections):
        self.__num_locations = num_locations
        self.__num_connections = num_connections
        self.__graph = self.__generate_graph()

    # Método getter para o grafo
    def get_graph(self):
        return self.__graph

    # Método privado para gerar o grafo de forma randômica.
    def __generate_graph(self):
        locations, graph = [], {}
        for uid in range(self.__num_locations):
            locations.append(Location(uid, 0.3))
        graph, graph_aux = self.__generate_connections(locations)
        return graph

    # Método para gerar as conexões do grafo
    def __generate_connections(self, locations) -> dict:
        conn_num = 0
        graph = {}
        graph_aux = {} # criando um grafo auxiliar para agilizar algumas buscas
        while conn_num < self.__num_connections:
            vertex_1, vertex_2 = random.sample(locations, 2)
            vertex_1_uid = vertex_1.get_uid()
            vertex_2_uid = vertex_2.get_uid()

            if vertex_1_uid not in graph:
                graph[vertex_1_uid] = {'this': vertex_1, 'connections': []}
                graph_aux[vertex_1_uid] = {}

            if vertex_2_uid not in graph:
                graph[vertex_2_uid] = {'this': vertex_2, 'connections': []}
                graph_aux[vertex_2_uid] = {}

            if vertex_1_uid == vertex_2_uid or vertex_2_uid in graph_aux[vertex_1_uid]:
                continue

            graph[vertex_1_uid]['connections'].append(vertex_2)
            graph[vertex_2_uid]['connections'].append(vertex_1)
            graph_aux[vertex_1_uid][vertex_2_uid] = True
            graph_aux[vertex_2_uid][vertex_1_uid] = True
            conn_num += 1
        return graph, graph_aux

    # Método para imprimir o grafo
    def print_graph(self):
        for location in self.graph:
            connections = [conn.get_uid() for conn in self.graph[location]['connections']]
            location_uid = self.graph[location]['this'].get_uid()
            is_safe = self.graph[location]['this'].get_safety()
            print(f"{location_uid}, {is_safe}: {connections}")


    # Método para parsear o grafo para um formato passivel de ser plotado.
    def __simplify_graph_of_objects(self):
        graph = nx.Graph()
        for vertex in self.__graph:
            safety = self.__graph[vertex]['this'].get_safety()
            color = "green" if safety else "red"
            graph.add_node(vertex, id="", color=color)
        for vertex in self.__graph:
            for connection in self.__graph[vertex]['connections']:
                graph.add_edge(vertex, connection.get_uid())
        return graph


    # Método para plotar o grafo
    def plot_graph(self) -> None:
        graph = self.__simplify_graph_of_objects()
        colors = [graph.nodes[n]['color'] for n in graph.nodes()]
        pos = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_color=colors)
        nx.draw_networkx_edges(graph, pos)
        nx.draw_networkx_labels(graph, pos)
        plt.show()


if __name__ == '__main__': 
    pass