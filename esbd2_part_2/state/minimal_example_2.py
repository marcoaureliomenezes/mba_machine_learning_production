from abc import ABC, abstractmethod


class State(ABC):


    @abstractmethod
    def button_pressed(self, context):
        pass


    @abstractmethod
    def sensor_activated(self, context):
        pass


class OpenState(State):

    def button_pressed(self, context):
        print("Open")
        context.change_state(ClosingState())

    def sensor_activated(self, context):
        pass

class ClosedState(State):

    def button_pressed(self, context):
        print("Closed")
        context.change_state(OpeningState())

    def sensor_activated(self, context):
        pass


class StopedState(State):

    def button_pressed(self, context):
        if isinstance(context.state, OpenState):
            print("Stoped")
            context.change_state(ClosingState())
        elif isinstance(context.state, ClosedState):
            print("Stoped")
            context.change_state(OpeningState())
            

    def sensor_activated(self, context):
        pass

class OpeningState(State):

    def button_pressed(self, context):
        print("Opening")
        context.change_state(StopedState())

    def sensor_activated(self, context):
        pass

class ClosingState(State):

    def button_pressed(self, context):
        print("Closing")
        context.change_state(StopedState())

    def sensor_activated(self, context):
        pass


class EletronicGate():
    __current_state= None
    __previous_state = None

    def __init__(self):
        self.__current_state = OpeningState()
        self.__previous_state = OpenState()

    def button_pressed(self):
        self.__current_state.button_pressed(self)


    def sensor_activated(self):
        self.__current_state.sensor_activated(self)



class Main:
    def main(self):
        gate = EletronicGate()
        gate.button_pressed()

if __name__ == "__main__":
    Main().main()
    