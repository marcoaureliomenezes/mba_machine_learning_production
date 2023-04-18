import random
from base_observers import Subject, Observer

class ConcreteSubject(Subject):

    __list_of_observers = []
    __movement_state = None
    __emergency_state = None

    def __init__(self) -> None:
        self.__movement_state = 0
        self.__emergency_state = False
        self._observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def set_state(self, state: int) -> None:
        self.__movement_state = state


    def get_state(self) -> int:
        return self.__movement_state

