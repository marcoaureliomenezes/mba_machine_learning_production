from base_observers import Subject, Observer

class ConcreteObserverA(Observer):
    """Concrete class that defines the Observer interface."""

    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, subject: Subject) -> None:
        state_subject = subject.get_state()
        msg_not_interesting = f"Não é um evento de interesse para {self._name}."
        msg_interesting = f"Evento de interesse. Começando ação para {self._name}."
        print(msg_interesting if state_subject == 0 else msg_not_interesting)

class ConcreteObserverB(Observer):
    """Concrete class that defines the Observer interface."""

    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, subject: Subject) -> None:
        state_subject = subject.get_state()
        msg_not_interesting = f"Não é um evento de interesse para {self._name}."
        msg_interesting = f"Evento de interesse. Começando ação para {self._name}."
        print(msg_interesting if state_subject == 1 else msg_not_interesting)

