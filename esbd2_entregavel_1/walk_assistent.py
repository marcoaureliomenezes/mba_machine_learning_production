from functools import reduce
import time
from graph_generator import Location

# Classe para representar a aplicação de auxílio a caminhadas seguras em um ambiente desconhecido.
class WalkAssistent(object):

    __actual_position: Location = None
    __target_position: Location = None
    __graph = None


    # Construtor da classe
    def __init__(self, graph) -> None:
        self.__graph = graph


    # Método para setar a posição atual do usuário  
    def set_actual_position(self, position) -> None:
        self.__actual_position = self.__graph.get_graph()[position]


    # Método getter para a posição atual do usuário
    def get_actual_position(self) -> Location:
        return self.__actual_position


    # Método para setar a localização destino do usuário
    def set_target_position(self, position) -> None:
        self._target_position = position


    # Método getter para a localização destino do usuário
    def get_target_position(self) -> Location: 
        return self.__target_position


    # Método para plotar o mapa
    def plot_map(self) -> None:
        self.__graph.plot_map()


    # Método para gerar o caminho a ser seguido pelo usuário
    def __generate_router(self, strategy) -> list:
        """
        Metodo privado para gerar o caminho a ser seguido pelo usuario. Recebe como parametro uma estrategia de roteamento.
        Essas estrategias estao definidas nas classes HighlySafetyRouter, SafetyRouter e AcceptableRouter e sao uma implementacao do padrao Strategy.
        """
        
        path = strategy.trace_route(self.__graph, self._actual_position, self._target_position)
        return path


    def follow_route(self, strategy, src_position, target_position):
        self._actual_position = src_position
        self._target_position = target_position
        route = self.__generate_router(strategy)
        print("No route found!\n") if route == None else \
            print(f"Path: {reduce(lambda a, b: f'{a}, {b}', route)}")



    def get_distance(self):
        return self._graph.get_distance(self._actual_position, self._target)


