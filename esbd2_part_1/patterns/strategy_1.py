from abc import ABC, abstractmethod
import random

class Searcher(ABC):
    @abstractmethod
    def search(self, value):
        raise NotImplementedError


class LinearSearch(Searcher):

    def __init__(self, lista) -> None:
        self.lista = lista

    def search(self, value):
        print("Linear search")
        return True if value in self.lista else False

class BinarySearch(Searcher):

    def __init__(self, lista) -> None:
        self.lista = lista

    def search(self, value):
        print("Binary search")
        return True if value in self.lista else False


class HashSearch(Searcher):

    def __init__(self, lista) -> None:
        self.dic = {i: None for i in lista}

    def search(self, value):
        print("Hash search")
        return True if self.dic.get(value) is not None else False


class SearcherContext:

    def search(self, value, strategy: Searcher):
        strategy.search(value)


if __name__ == "__main__":

    sample_lista = lambda magnitude: [random.randint(0, 10**magnitude) for i in range(10**magnitude)]
    lista = sample_lista(6)
    searcher = SearcherContext()
    searcher.search(10, LinearSearch(lista))
    searcher.search(10, BinarySearch(lista))
    searcher.search(10, HashSearch(lista))