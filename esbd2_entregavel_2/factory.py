# Exemplo de padrão de projeto Factory
from abc import ABC
from typing import List

class Cliente(ABC):
    def operation(self) -> str:
        raise NotImplementedError()


class Creator(ABC):
    def factory_method(self) -> Cliente:
        raise NotImplementedError()

        
class ConcreteCreator(Creator):
    def factory_method(self, tipo) -> Cliente:
        dicionario = {"PF": ClienteFisico(), "PJ": ClienteJuridico(), "Governo": ClienteGoverno()}
        return dicionario[tipo]


class ClienteFisico(Cliente):
    def operation(self) -> str:
        return "Resultado de Cliente Fisico."


class ClienteJuridico(Cliente):
    def operation(self) -> str:
        return "Resultado de Cliente Juridico."


class ClienteGoverno(Cliente):
    def operation(self) -> str:
        return "Resultado de Cliente Governo."



if __name__ == "__main__":

    print("App: Launched with the ConcreteCreator.")
    obj1: Creator = ConcreteCreator().factory_method("PF")
    print(obj1.operation())
    print(type(obj1))


    obj2: Creator = ConcreteCreator().factory_method("PJ")
    print(obj2.operation())
    print(type(obj2))


    obj3: Creator = ConcreteCreator().factory_method("Governo")
    print(obj3.operation())
    print(type(obj3))