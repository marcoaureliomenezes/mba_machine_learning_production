from walk_assistent import WalkAssistent
from router import HighlySafetyRouter, SafetyRouter, accetableRouter
from graph_generator import Graph


def test_singleton():
    strategy_1 = HighlySafetyRouter()
    strategy_2 = HighlySafetyRouter()
    print(f"A instância de strategy_1 é a mesma de strategy_4? {strategy_1 == strategy_2}")

def generate_graph():
    graph = Graph(10, 15)
    graph.print_graph()
    return graph


if __name__ == '__main__':

    # testando o padrão singleton aplicado a classe Router e suas subclasses
    test_singleton()

    graph = generate_graph()
    # print(graph.graph)
    # source_pos = 'A'
    # target_pos = 'F'

    
    # strategy_1, strategy_2, strategy_3 = HighlySafetyRouter(), SafetyRouter(), accetableRouter()
    # router_generator = WalkAssistent(graph, source_pos, target_pos)

    # router_generator.generate_router(strategy_1)
    # router_generator.generate_router(strategy_2)
    # router_generator.generate_router(strategy_3)


# Path: ESBD2/entregavel_1/router_generator.py



