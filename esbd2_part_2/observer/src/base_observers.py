from abc import ABC, abstractmethod
class Subject(ABC):
    """Abstract class that defines the Observer interface."""

    def attach(self, observer) -> None:
        raise NotImplementedError

    def detach(self, observer) -> None:
        raise NotImplementedError

    def __notify(self) -> None:
        for observer in self.__list_of_observers:
            observer.update(self)
        raise NotImplementedError

class Observer(ABC):
    """Abstract class that defines the Observer interface."""

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Update the observer with the subject's state."""
        pass

