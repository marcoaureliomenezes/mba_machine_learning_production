import time



class WalkAssistent(object):

    _actual_position = None

    def __init__(self, graph, source, target):
        self._graph = graph
        self._actual_position = source
        self._target = target


    def generate_router(self, strategy):
        path = strategy.trace_route(self._graph, self._actual_position, self._target)
        for next_position in path:
            self._walk(next_position)
            print(self._actual_position)
            time.sleep(1)


    def _walk(self, next_position):
        self._actual_position = next_position

    def get_distance(self):
        return self._graph.get_distance(self._actual_position, self._target)


