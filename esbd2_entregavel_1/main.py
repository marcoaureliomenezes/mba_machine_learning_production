from walk_assistent import WalkAssistent
from router import HighlySafetyRouter, SafetyRouter, accetableRouter
from graph_generator import Graph
import random

def test_singleton():
    strategy_1 = HighlySafetyRouter()
    strategy_2 = HighlySafetyRouter()
    print(f"The same instance? {strategy_1 is strategy_2}")



if __name__ == '__main__':

    # testando o padrão singleton aplicado a classe Router e suas subclasses
    #test_singleton()

    strategy_1, strategy_2, strategy_3 = HighlySafetyRouter(), SafetyRouter(), accetableRouter()

    graph = Graph(10, 20)



    source_pos, target_pos = random.sample(graph.graph.keys(), 2)
    router_generator = WalkAssistent(source_pos, target_pos)


    safest_path = router_generator.follow_route(strategy_1, graph)
    safe_path = router_generator.follow_route(strategy_2, graph)
    fastest_path = router_generator.follow_route(strategy_3, graph)
    