from abc import ABC, abstractmethod
import random
from typing import List
from queue import Queue

class Singleton(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Singleton already instantiated. Returning the same instance")
        return cls._instance


class Router(ABC, Singleton):

    @abstractmethod
    def logic_trace_route(self, graph, source, target) -> List:
        pass


    def trace_route(self, graph, source, target) -> List:
        path = self._compute_specific_path(graph, source, target, self.logic_trace_route)
        return path
   

    def _compute_specific_path(self, graph, source, target, lambda_funct):
        initial_distances = { i: None if i != source else 0 for i in graph.graph.keys()}
        fila, path_list = Queue(), []
        fila.put(graph.graph[source]['this'])
        while not fila.empty():
            vertex_uid = fila.get().get_uid()
            if vertex_uid == target: break
            for neighbor in graph.graph[vertex_uid]['connections']:  
                neighbor_id = neighbor.get_uid()
                if initial_distances[neighbor_id] is None:
                    if lambda_funct(neighbor): continue            
                    initial_distances[neighbor_id] = initial_distances[vertex_uid] + 1
                    path_list.append((vertex_uid, neighbor_id))
                    fila.put(neighbor)
        path = self.__generate_path(path_list, source, target)
        return path


    def __generate_path(self, path_list, source, dst):
        if dst == source: return [source]
        last_index = [i for i in path_list if i[1] == dst]
        if last_index == []: return None
        return self.__generate_path(path_list, source, last_index[0][0]) + [dst]



class HighlySafetyRouter(Router):



    def logic_trace_route(self, neighbor):
        return neighbor.get_safety() != True


class SafetyRouter(Router):



    def logic_trace_route(self, neighbor):
        if random.random() < 0.7:
            return neighbor.get_safety() != True
        return False


class accetableRouter(Router):

    def logic_trace_route(self, neighbor):
        return False
