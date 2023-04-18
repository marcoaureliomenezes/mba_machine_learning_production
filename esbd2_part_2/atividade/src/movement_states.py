
from abc import ABC, abstractmethod
import time

class Singleton(object):

    _instance: object = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class ElevatorState(Singleton, ABC):

    @abstractmethod
    def elevador_step(self, elevador):
        raise NotImplementedError

    def emergency_button(self, elevador):
        print("Elevador em emergência")
        elevador.current_state = StoppedState()
        elevador.floor_requests = []
        elevador.is_emergency = True
        elevador.notify()
        return

    def maintainance_button(self, elevador):
        print("Elevador em manutenção")
        elevador.current_state = StoppedState()
        elevador.floor_requests = []
        elevador.is_maintainance = True
        elevador.notify()
        return

class MovingUpState(ElevatorState):

    def elevador_step(self, elevador):
        target = min([i for i in elevador.floor_requests if i > elevador.current_floor])
        elevador.current_floor += 1
        print(f"{elevador.current_floor - 1} -> {elevador.current_floor}")
        if elevador.current_floor == target:
            elevador.floor_requests.remove(target)
            elevador.previous_state, elevador.current_state = self, StoppedState()
            return 
        else:
            elevador.current_state = MovingUpState()


class MovingDownState(ElevatorState):

    def elevador_step(self, elevador):
        if len(elevador.floor_requests) == 0:
            elevador.previous_state, elevador.current_state = self, StoppedState()
            return
        
        target = max([i for i in elevador.floor_requests if i < elevador.current_floor])
        elevador.current_floor -= 1
        print(f"{elevador.current_floor + 1} -> {elevador.current_floor}")

        if elevador.current_floor == target:
            elevador.floor_requests.remove(target)
            elevador.previous_state, elevador.current_state = self, StoppedState()
            return
        else:
            elevador.previous_state, elevador.current_state = self, MovingDownState()
            

class StoppedState(ElevatorState):

    def elevador_step(self, elevador):
        required_floors = elevador.floor_requests
        actual_floor = elevador.current_floor

        elevador.notify()
        if len(elevador.floor_requests) == 0: return 

        max_greater_than = max(required_floors) > actual_floor
        min_greater_than = min(required_floors) > actual_floor
        max_less_than = max(required_floors) < actual_floor
        min_less_than = min(required_floors) < actual_floor
   
        if max_greater_than and min_greater_than:
            elevador.previous_state, elevador.current_state = self, MovingUpState()
            return

        if max_less_than and min_less_than:
            elevador.previous_state, elevador.current_state = self, MovingDownState()
            return

        if elevador.previous_state == MovingDownState() and max_greater_than:
            elevador.previous_state, elevador.current_state = self, MovingDownState()
            return

        if elevador.previous_state == MovingUpState() and max_less_than:
            elevador.previous_state, elevador.current_state = self, MovingUpState()
            return
        else:
            elevador.previous_state, elevador.current_state = self, MovingUpState()
            return