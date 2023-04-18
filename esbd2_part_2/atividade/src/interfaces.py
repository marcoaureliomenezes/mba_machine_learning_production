from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):

    @abstractmethod
    def attach(self, observer) -> None:
        raise NotImplementedError


    @abstractmethod
    def detach(self, observer) -> None:
        raise NotImplementedError


    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        raise NotImplementedError

