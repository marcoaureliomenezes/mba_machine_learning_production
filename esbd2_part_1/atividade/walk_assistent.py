from functools import reduce
import time
from graph_generator import Location, Graph

# Classe para representar a aplicação de auxílio a caminhadas seguras em um ambiente desconhecido.
class WalkAssistent(object):

    __actual_pos: Location = None
    __target_pos: Location = None
    __graph: Graph  = None
    __path: list = None
    
    # Construtor da classe
    def __init__(self, graph) -> None:
        self.__graph = graph


    # Método para gerar o caminho a ser percorrido
    def generate_route(self, strategy) -> list:
        self.__path = strategy.trace_route(self.__graph, self.__actual_pos, self.__target_pos)


    # Método para setar a trajetória a ser percorrida
    def set_trajectory(self, src_pos, target_pos) -> None:
        self.__actual_pos = src_pos
        self.__target_pos = target_pos


    # Método para plotar o mapa
    def plot_graph(self) -> None:
        self.__graph.plot_graph()


    # Método para imprimir o estado atual do usuário
    def print_state(self) -> None:
        print(f'Posição atual: {self.__actual_pos} Posição destino: {self.__target_pos}')
  

    # Método para imprimir o caminho percorrido
    def print_route_generated(self) -> None:
        print(f'Caminho: {reduce(lambda a, b: f"{a} -> {b}", self.__path) if len(self.__path) > 0 else "Nenhum caminho encontrado"}')


    # Método para setar a posição atual do usuário  
    def set_actual_position(self, position) -> None:
        self.__actual_pos = self.__graph.get_graph()[position]


    # Método getter para a posição atual do usuário
    def get_actual_position(self) -> Location:
        return self.__actual_pos


    # Método para setar a localização destino do usuário
    def set_target_position(self, position) -> None:
        self._target_position = position


    # Método getter para a localização destino do usuário
    def get_target_position(self) -> Location: 
        return self.__target_pos


