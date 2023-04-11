
from abc import ABC, abstractmethod
from typing import List


class Router(ABC):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        else:
            print("Já existe uma instancia")            
        return cls.__instance


    @abstractmethod
    def trace_route(self, graph, source, target) -> List:
        pass




class HighlySafetyRouter(Router):
    def trace_route(self, graph, source, target) -> List:
        print("Highly safety mode activated")
        return ['A', 'B']


class SafetyRouter(Router):

    def trace_route(self, graph, source, target) -> List:
        print("Safety mode activated")
        return ['A', 'C']


class accetableRouter(Router):
    def trace_route(self, graph, source, target) -> List:
        print("Acceptable mode activated")
        return ['A', 'D']