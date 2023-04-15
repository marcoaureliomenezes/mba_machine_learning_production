from walk_assistent import WalkAssistent
from router import HighlySafetyRouter, SafetyRouter, AcceptableRouter
from graph_generator import Graph
import random

# Teste do padrão singleton para a classe Router e suas subclasses
def test_singleton():
    strategy_1 = HighlySafetyRouter()
    strategy_2 = HighlySafetyRouter()
    print(f"The same instance? {strategy_1 is strategy_2}")

if __name__ == '__main__':


    # Cria variaveis para as estrategias de roteamento
    strategy_1, strategy_2, strategy_3 = HighlySafetyRouter(), SafetyRouter(), AcceptableRouter()

    # Cria um grafo de de 20 localizações e 20 conexões entre elas
    graph = Graph(100, 500)

    
    # Seleciona duas posições aleatórias do grafo
    src_position, target_position = random.sample(graph.get_graph().keys(), 2)
    
    # Printa a posição de origem e destino e plota o grafo

    # Cria um objeto da classe WalkAssistent
    router_generator = WalkAssistent(graph)
    router_generator.set_trajectory(src_position, target_position)
    router_generator.print_state()


    # Gera o caminho mais seguro entre as posições de origem e destino
    safest_path = router_generator.generate_route(strategy_1)
    router_generator.print_route_generated()


    # Gera o caminho razoavelmente seguro entre as posições de origem e destino
    safe_path = router_generator.generate_route(strategy_2)
    router_generator.print_route_generated()


    # Gera um caminho aceitavelmente seguro entre as posições de origem e destino
    fastest_path = router_generator.generate_route(strategy_3)
    router_generator.print_route_generated()


    router_generator.plot_graph()