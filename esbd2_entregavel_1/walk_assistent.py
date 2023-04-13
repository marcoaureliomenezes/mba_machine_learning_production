from functools import reduce
import time



class WalkAssistent(object):

    _actual_position = None

    def __init__(self, source, target):
        self._actual_position = source
        self._target_position = target
        print(f"Actual position: {self._actual_position}, Target position: {self._target_position}\n")
       

    def __generate_router(self, strategy, graph):
        path = strategy.trace_route(graph, self._actual_position, self._target_position)
        return path


    def follow_route(self, strategy, graph):
        route = self.__generate_router(strategy, graph)
        print("No route found!\n") if route == None else \
            print(f"Path: {reduce(lambda a, b: f'{a}, {b}', route)}")


    def get_actual_position(self):
        return self._actual_position


    def get_target_position(self):
        return self._target_position


    def get_distance(self):
        return self._graph.get_distance(self._actual_position, self._target)


