from src.observer import ConcreteObserverA, ConcreteObserverB
from src.subject import ConcreteSubject




if __name__ == "__main__":

    observers = [ConcreteObserverA("Observer A-1"), ConcreteObserverA("Observer A-2"), 
                ConcreteObserverB("Observer B-1"), ConcreteObserverB("Observer B-2")]

    subject = ConcreteSubject()

    for i in observers:
        subject.attach(i)


    subject.notify()
    subject.set_state(1)
    subject.notify()



