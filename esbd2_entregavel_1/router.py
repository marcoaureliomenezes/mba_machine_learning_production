from abc import ABC, abstractmethod
import random
from typing import List
from queue import Queue

class Singleton(object):

    _instance: object = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Singleton already instantiated. Returning the same instance")
        return cls._instance

# Classe abstrata para representar um roteador. Herda da classe Singleton para garantir que apenas uma instância
class Router(ABC, Singleton):


    # Método abstrato para implementar a lógica de roteamento
    @abstractmethod
    def trace_route(self, graph, source, target) -> List:
        pass


    # Método privado para calcular o caminho entre dois vértices de um grafo
    # Recebe uma função lambda que define a lógica com que os vizinhos serão visitados
    def _compute_specific_path(self, graph, source, target, lambda_funct):
        graph = graph.get_graph()
        initial_distances = { i: None if i != source else 0 for i in graph.keys()}
        fila, path_list = Queue(), []
        fila.put(graph[source]['this'])
        while not fila.empty():
            vertex_uid = fila.get().get_uid()
            if vertex_uid == target: break
            for neighbor in graph[vertex_uid]['connections']:  
                neighbor_id = neighbor.get_uid()
                if initial_distances[neighbor_id] is None:
                    cond_neighbor_equals_target = neighbor_id == target
                    if lambda_funct(neighbor) and not cond_neighbor_equals_target: continue            
                    initial_distances[neighbor_id] = initial_distances[vertex_uid] + 1
                    path_list.append((vertex_uid, neighbor_id))
                    fila.put(neighbor)
        path = self.__generate_path(path_list, source, target)
        return path


    # Método privado para gerar o caminho a partir da lista de arestas. Usa recursão para gerar o caminho de forma reversa
    def __generate_path(self, path_list, source, target):
        if target == source: return [source]
        last_index = [i for i in path_list if i[1] == target]
        if last_index == []: return None
        return self.__generate_path(path_list, source, last_index[0][0]) + [target]


# Classe para representar um roteador que observa a segurança do caminho em todos os vizinhos. Herda a classe a
class HighlySafetyRouter(Router):

    # Método para calcular o caminho a ser seguido pelo usuário.
    def trace_route(self, graph, source, target) -> List:
        logic_trace_route = lambda neighbor: neighbor.get_safety() != True
        path = self._compute_specific_path(graph, source, target, logic_trace_route)
        return path


# Classe para representar um roteador tem 70% de chance de observar a segurança do caminho ao visitar um vizinho.
class SafetyRouter(Router):

    # Método para calcular o caminho a ser seguido pelo usuário.
    def trace_route(self, graph, source, target) -> List:
        logic_trace_route = lambda neighbor: neighbor.get_safety() != True if random.random() < 0.2 else False
        path = self._compute_specific_path(graph, source, target, logic_trace_route)
        return path

# Classe para representar um roteador que sempre aceita a rota
class AcceptableRouter(Router):

    # Método para calcular o caminho a ser seguido pelo usuário.
    def trace_route(self, graph, source, target) -> List:
        logic_trace_route = lambda neighbor: neighbor.get_safety() != True if random.random() < 0.2 else False
        path = self._compute_specific_path(graph, source, target, logic_trace_route)
        return path