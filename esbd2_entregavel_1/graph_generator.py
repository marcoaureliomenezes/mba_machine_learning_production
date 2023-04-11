from random import randint
import random
import uuid



class Location(object):

    def __init__(self, uid, is_safety):
        self._uid = uid
        self._is_safety = is_safety

    def get_uid(self):
        return self._uid
    
    def get_safety(self):
        return self._is_safety


class Graph(object):


    def __init__(self, _num_locations, num_connections):
        self._num_locations = _num_locations
        self._num_connections = num_connections
        self.graph = self._generate_graph()


    def __generate_connections(self, locations):
        conn_num = 0
        graph = {}
        graph_aux = {} # criando um grafo auxiliar para agilizar algumas buscas
        while conn_num < self._num_connections:
            location_1, location_2 = random.sample(locations, 2)
            location_1_uid = location_1.get_uid()
            location_2_uid = location_2.get_uid()

            if location_1_uid not in graph:
                graph[location_1_uid] = {'this': location_1, 'connections': []}
                graph_aux[location_1_uid] = {}

            if location_2_uid not in graph:
                graph[location_2_uid] = {'this': location_2, 'connections': []}
                graph_aux[location_2_uid] = {}

            if location_1_uid == location_2_uid or \
                location_2_uid in graph_aux[location_1_uid]:
                continue

            graph[location_1_uid]['connections'].append(location_2)
            graph[location_2_uid]['connections'].append(location_1)
            graph_aux[location_1_uid][location_2_uid] = True
            graph_aux[location_2_uid][location_1_uid] = True
            conn_num += 1
        return graph, graph_aux


    def _generate_graph(self):
        locations = []
        graph = {}
        graph_aux = {} # criando um grafo auxiliar para agilizar algumas buscas

        for _ in range(self._num_locations):
            uid = str(uuid.uuid4())[:8]
            is_safety = bool(randint(0, 1))
            locations.append(Location(uid, is_safety))
        graph, graph_aux = self.__generate_connections(locations)
        return graph
        
    def get_graph(self):
        return self.graph

    def print_graph(self):
        my_print = lambda connection: {"location": connection.get_uid(), "is_safe": connection.get_safety()}
        for location in self.graph:
            connections = [my_print(connection) for connection in self.graph[location]['connections']]
            location_uid = self.graph[location]['this'].get_uid()
            print("Location: ", location_uid, "Connections: ", connections)
if __name__ == '__main__': 
    pass